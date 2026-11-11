// voice aşaması: 04_scenes.json → audio/narration.wav + 05_voice.json
// Sahne süreleri sesten türetilir; kelime damgaları satır vuruşlarını ve mascot ağzını sürer.
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { ScenePlan, Script, Voice } from "../../schemas/index.ts";
import { episodeDirArg, fail, loadEnv, P, readJson, syllables, words as split, writeJson } from "../lib/io.ts";
import { elevenlabs } from "./providers/elevenlabs.ts";
import { mock } from "./providers/mock.ts";
import { piper, piperAvailable } from "./providers/piper.ts";
import { SAMPLE_RATE } from "./providers/types.ts";

const FPS = 30, LEAD = 8, TAIL = 14, REMINDER = 150;
// Sabit açılış ve kapanış cümleleri (kanal kimliği). display: altyazı, spoken: okunuş.
const WELCOME = { display: "MuMa Library'ye hoş geldin!", spoken: "Muma Laybrıri'ye hoş geldin!" };
const GOODBYE = { display: "Bir sonraki bilim videosunda görüşürüz! Hoşça kal!", spoken: "Bir sonraki bilim videosunda görüşürüz! Hoşça kal!" };
const FLY_IN = 42, FLY_OUT = 60; // robotun uçarak giriş/çıkış süresi (kare)
const MIN_SEC = 285, MAX_SEC = 360; // hedef 5–6 dk (konu bölümlerinde ~5 dk)

loadEnv();
const { dir, flags } = episodeDirArg();
const p = P(dir);
const script = readJson(p.script, Script);
const plan = readJson(p.scenes, ScenePlan);
const lineById = new Map(script.sections.flatMap((s) => s.lines).map((l) => [l.id, l]));

const key = process.env.ELEVENLABS_API_KEY, voiceId = process.env.ELEVENLABS_VOICE_ID;
const useReal = Boolean(key && voiceId) && !flags.mock;
if (key && !voiceId && !flags.mock) console.log("⚠ ELEVENLABS_API_KEY var ama ELEVENLABS_VOICE_ID yok → mock ses kullanılıyor");
// Öncelik: ElevenLabs → yerel Piper → mock (sessiz).
const provider = useReal ? elevenlabs(key!, voiceId!, process.env.ELEVENLABS_MODEL || "eleven_multilingual_v2") : piperAvailable() && !flags.mock ? piper() : mock;
const LINE_GAP = 0.38; // satır satır sentezde cümle arası boşluk (sn)
console.log(`ses sağlayıcı: ${provider.name}`);

const scenes: Voice["scenes"] = [];
const allWords: Voice["words"] = [];
const clips: { atFrame: number; pcm: Int16Array }[] = [];
// Açılış: robot uçarak gelir, sonra karşılama cümlesi. Süre sese göre uzar (en az 5 sn).
const welcome = await provider.synthesize(WELCOME.spoken);
const goodbye = await provider.synthesize(GOODBYE.spoken);
const fr = (pcm: Int16Array) => Math.ceil((pcm.length / SAMPLE_RATE) * FPS);
const INTRO = Math.max(150, FLY_IN + fr(welcome.pcm) + 55);
const OUTRO_TAIL = Math.max(270, 30 + fr(goodbye.pcm) + 50 + FLY_OUT);
const bumpers: Voice["bumpers"] = [{ startFrame: FLY_IN, endFrame: FLY_IN + fr(welcome.pcm) + 6, text: WELCOME.display }];
clips.push({ atFrame: FLY_IN, pcm: welcome.pcm });
let cursor = INTRO, prevText = "", wordCount = 0;

for (const [i, sc] of plan.scenes.entries()) {
  const lines = sc.lineIds.map((id) => lineById.get(id) ?? fail(`${sc.id}: bilinmeyen satır ${id}`));
  const text = lines.map((l) => l.spoken.trim()).join(" ");
  let pcm: Int16Array, words: { text: string; start: number; end: number }[];
  if (provider.perLine) {
    // Hizalama vermeyen sağlayıcı: her satır ayrı sentezlenir, satır sınırları kesin olur.
    const parts: Int16Array[] = []; words = [];
    let t = 0;
    for (const l of lines) {
      const r = await provider.synthesize(l.spoken.trim());
      for (const w of r.words) words.push({ text: w.text, start: w.start + t, end: w.end + t });
      parts.push(r.pcm, new Int16Array(Math.round(LINE_GAP * SAMPLE_RATE)));
      t += r.pcm.length / SAMPLE_RATE + LINE_GAP;
    }
    parts.pop();
    pcm = new Int16Array(parts.reduce((a, x) => a + x.length, 0));
    let o = 0; for (const x of parts) { pcm.set(x, o); o += x.length; }
    process.stdout.write(".");
  } else ({ pcm, words } = await provider.synthesize(text, prevText.slice(-300) || undefined));
  prevText = text;
  // Kelime damgalarını satırlara dağıt: her satırın kelime sayısı bellidir.
  const counts = lines.map((l) => split(l.spoken).length);
  const total = counts.reduce((a, b) => a + b, 0);
  const audioSec = pcm.length / SAMPLE_RATE;
  const at = (k: number) => (words.length === total ? words[Math.min(k, words.length - 1)] : null);
  const lineStart: number[] = [], lineEnd: number[] = [];
  let acc = 0;
  counts.forEach((c) => {
    // Hizalama kelime sayısı tutmazsa (TTS normalleştirmesi) oransal yaklaşıma düş.
    const s = at(acc)?.start ?? (audioSec * acc) / total;
    const e = at(acc + c - 1)?.end ?? (audioSec * (acc + c)) / total;
    lineStart.push(LEAD + Math.round(s * FPS)); lineEnd.push(LEAD + Math.round(e * FPS));
    acc += c;
  });
  const last = i === plan.scenes.length - 1;
  const durationFrames = Math.max(60, LEAD + Math.ceil(audioSec * FPS) + TAIL) + (last ? OUTRO_TAIL : 0);
  scenes.push({ sceneId: sc.id, startFrame: cursor, durationFrames, audioStartFrame: LEAD, lineStartFrames: lineStart, lineEndFrames: lineEnd });
  const offset = (cursor + LEAD) / FPS;
  for (const w of words) allWords.push({ text: w.text, start: +(w.start + offset).toFixed(3), end: +(w.end + offset).toFixed(3) });
  clips.push({ atFrame: cursor + LEAD, pcm });
  wordCount += total;
  cursor += durationFrames;
}
const totalFrames = cursor;
// Kapanış cümlesi: özet anlatımı bittikten sonra, kuyruk bölümünün başında.
const byeAt = totalFrames - OUTRO_TAIL + 30;
clips.push({ atFrame: byeAt, pcm: goodbye.pcm });
bumpers.push({ startFrame: byeAt, endFrame: byeAt + fr(goodbye.pcm) + 6, text: GOODBYE.display });
for (const [at, r] of [[FLY_IN, welcome], [byeAt, goodbye]] as const) for (const w of r.words) allWords.push({ text: w.text, start: +(w.start + at / FPS).toFixed(3), end: +(w.end + at / FPS).toFixed(3) });
allWords.sort((a, b) => a.start - b.start);
const durationSec = totalFrames / FPS;

// Tek ses dosyası (bölüm zaman çizelgesinde), 16 bit mono WAV.
const track = new Int16Array(Math.ceil(durationSec * SAMPLE_RATE));
for (const c of clips) track.set(c.pcm.subarray(0, Math.max(0, track.length - Math.round((c.atFrame / FPS) * SAMPLE_RATE))), Math.round((c.atFrame / FPS) * SAMPLE_RATE));
mkdirSync(p.audio, { recursive: true });
const data = Buffer.from(track.buffer, track.byteOffset, track.byteLength);
const hdr = Buffer.alloc(44);
hdr.write("RIFF", 0); hdr.writeUInt32LE(36 + data.length, 4); hdr.write("WAVEfmt ", 8); hdr.writeUInt32LE(16, 16); hdr.writeUInt16LE(1, 20); hdr.writeUInt16LE(1, 22);
hdr.writeUInt32LE(SAMPLE_RATE, 24); hdr.writeUInt32LE(SAMPLE_RATE * 2, 28); hdr.writeUInt16LE(2, 32); hdr.writeUInt16LE(16, 34); hdr.write("data", 36); hdr.writeUInt32LE(data.length, 40);
writeFileSync(join(p.audio, "narration.wav"), Buffer.concat([hdr, data]));

// Kare başına genlik zarfı (mascot ağzı). Gerçek seste RMS; mock'ta kelime damgalarından hece vuruşları.
const amplitude = new Array<number>(totalFrames).fill(0);
if (provider.name === "mock") {
  for (const w of allWords) {
    const n = syllables(w.text);
    for (let f = Math.floor(w.start * FPS); f <= Math.ceil(w.end * FPS) && f < totalFrames; f++) {
      const t = (f / FPS - w.start) / Math.max(0.05, w.end - w.start);
      if (t >= 0 && t <= 1) amplitude[f] = +(0.3 + 0.7 * Math.abs(Math.sin(Math.PI * t * n))).toFixed(3);
    }
  }
} else {
  const spf = SAMPLE_RATE / FPS;
  const rms = amplitude.map((_, f) => { let s = 0; for (let k = Math.floor(f * spf); k < Math.floor((f + 1) * spf) && k < track.length; k++) s += track[k] * track[k]; return Math.sqrt(s / spf); });
  const ref = [...rms].sort((a, b) => a - b)[Math.floor(rms.length * 0.95)] || 1;
  rms.forEach((v, f) => { amplitude[f] = +Math.min(1, v / ref).toFixed(3); });
}

// Abone ol hatırlatması: sürenin ~%60'ına en yakın sahne sınırı (kapanış hariç).
const target = totalFrames * 0.6;
const boundary = scenes.slice(1, -1).map((s) => s.startFrame).sort((a, b) => Math.abs(a - target) - Math.abs(b - target))[0] ?? Math.round(target);
const reminder = { startFrame: boundary + 24, durationFrames: REMINDER, atPercent: +(((boundary + 24) / totalFrames) * 100).toFixed(1) };

const voice: Voice = { provider: provider.name, fps: FPS, introFrames: INTRO, outroTailFrames: OUTRO_TAIL, totalFrames, durationSec: +durationSec.toFixed(2), wordCount, audioFile: "audio/narration.wav", scenes, words: allWords, amplitude, reminder, bumpers };
writeJson(p.voice, Voice, voice);

const mmss = (s: number) => `${Math.floor(s / 60)}:${String(Math.round(s % 60)).padStart(2, "0")}`;
console.log(`\n── Zaman çizelgesi ──\nsüre: ${mmss(durationSec)} (${totalFrames} kare) · ${wordCount} kelime · ${plan.scenes.length} sahne · hatırlatma %${reminder.atPercent}`);
for (const [i, s] of scenes.entries()) console.log(`  ${mmss(s.startFrame / FPS).padStart(5)}  ${s.sceneId.padEnd(4)} ${plan.scenes[i].visual.type.padEnd(12)} ${(s.durationFrames / FPS).toFixed(1).padStart(5)} sn  [${plan.scenes[i].section}] mascot: ${plan.scenes[i].mascot.state}`);
// Süre kapısı
if (durationSec < MIN_SEC || durationSec > MAX_SEC) {
  const msg = `Süre ${mmss(durationSec)}; hedef 4:45–6:00. Senaryoyu ${durationSec < MIN_SEC ? "uzatın" : "kısaltın"} (yaklaşık ${Math.abs(Math.round((durationSec - 330) * 2.4))} kelime).`;
  if (flags["allow-duration"]) console.log(`⚠ ${msg} (--allow-duration ile devam)`); else fail(msg);
} else console.log("süre kapısı: geçti");
