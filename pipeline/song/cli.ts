// song aşaması: 03_script.json içindeki şarkı sözleri → song.mp3 + 05_song.json
// ElevenLabs Music (POST /v1/music, composition_plan). Anahtar yoksa ya da --mock ile sessiz yer tutucu üretir.
// Üretim kota harcar: çıktı varsa yeniden üretilmez; yeni deneme için --force (eskisi song.prev.mp3 olur).
import { execFileSync, spawnSync } from "node:child_process";
import { copyFileSync, existsSync, mkdtempSync, readdirSync, readFileSync, renameSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Script, Song } from "../../schemas/index.ts";
import { episodeDirArg, fail, loadEnv, P, readJson, syllables, words, writeJson } from "../lib/io.ts";

loadEnv();
const { dir, flags } = episodeDirArg();
const p = P(dir);
const script = readJson(p.script, Script);
if (!script.song) { console.log("Senaryoda şarkı yok; song aşaması atlandı."); process.exit(0); }
if (existsSync(p.song) && existsSync(p.songAudio) && !flags.force) { console.log(`Şarkı zaten var (${p.songAudio}); yeniden üretmek için --force.`); process.exit(0); }

const { song } = script;
const key = process.env.ELEVENLABS_API_KEY;
const useReal = Boolean(key) && !flags.mock;
const model = process.env.ELEVENLABS_MUSIC_MODEL || "music_v2_5";
const totalMs = song.sections.reduce((a, s) => a + s.durationMs, 0);
if (existsSync(p.songAudio)) renameSync(p.songAudio, p.songAudio.replace(/\.mp3$/, ".prev.mp3"));

if (useReal) {
  const body = {
    model_id: model,
    composition_plan: {
      chunks: song.sections.map((s) => ({
        text: [`[${s.tag}]`, ...(s.direction ? [`{${s.direction}}`] : []), ...s.lines].join("\n"),
        duration_ms: s.durationMs, positive_styles: song.style, negative_styles: song.negativeStyle,
      })),
    },
  };
  console.log(`ElevenLabs Music (${model}) · ${(totalMs / 1000).toFixed(0)} sn ...`);
  const res = await fetch("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128", { method: "POST", headers: { "xi-api-key": key!, "content-type": "application/json" }, body: JSON.stringify(body) });
  if (!res.ok) fail(`ElevenLabs Music isteği başarısız: ${res.status} ${(await res.text()).slice(0, 600)}`);
  writeFileSync(p.songAudio, Buffer.from(await res.arrayBuffer()));
  // Şarkıyı Muma'nın sesiyle söylet (kullanıcı kararı): vokal ayrılır, ses dönüştürülür, çalgılarla yeniden karıştırılır.
  // Müzik modeli doğrudan belirli bir sesle söyleyemediği için bu dolaylı yol kullanılır; --no-convert ile atlanır.
  if (!flags["no-convert"]) {
    const voiceId = process.env.ELEVENLABS_VOICE_ID || "j6hEdvUHjDuCExVlNXTi";
    const tmp = mkdtempSync(join(tmpdir(), "song-"));
    const original = p.songAudio.replace(/\.mp3$/, ".original.mp3");
    copyFileSync(p.songAudio, original);
    console.log("vokal ayrılıyor ...");
    const fd = new FormData();
    fd.append("file", new Blob([readFileSync(original)], { type: "audio/mpeg" }), "song.mp3");
    const st = await fetch("https://api.elevenlabs.io/v1/music/stem-separation", { method: "POST", headers: { "xi-api-key": key! }, body: fd });
    if (!st.ok) fail(`Vokal ayırma başarısız: ${st.status} ${(await st.text()).slice(0, 400)} (özgün şarkı duruyor: ${original}; --no-convert ile devam edilebilir)`);
    writeFileSync(join(tmp, "stems.zip"), Buffer.from(await st.arrayBuffer()));
    execFileSync("unzip", ["-o", "-q", join(tmp, "stems.zip"), "-d", tmp]);
    console.log("vokal Muma'nın sesine dönüştürülüyor ...");
    const fv = new FormData();
    fv.append("audio", new Blob([readFileSync(join(tmp, "vocals.mp3"))], { type: "audio/mpeg" }), "vocals.mp3");
    fv.append("model_id", "eleven_multilingual_sts_v2");
    fv.append("remove_background_noise", "false");
    const sv = await fetch(`https://api.elevenlabs.io/v1/speech-to-speech/${voiceId}?output_format=mp3_44100_128`, { method: "POST", headers: { "xi-api-key": key! }, body: fv });
    if (!sv.ok) fail(`Ses dönüştürme başarısız: ${sv.status} ${(await sv.text()).slice(0, 400)}`);
    writeFileSync(join(tmp, "vocals_muma.mp3"), Buffer.from(await sv.arrayBuffer()));
    // Dönüştürülen vokal özgün vokalin ses düzeyine getirilir, sonra çalgı kanallarıyla karıştırılır.
    const vol = (f: string) => Number(/mean_volume: ([-0-9.]+)/.exec(spawnSync("ffmpeg", ["-hide_banner", "-i", f, "-af", "volumedetect", "-f", "null", "-"]).stderr.toString())?.[1] ?? 0);
    const gain = Math.max(-3, Math.min(9, vol(join(tmp, "vocals.mp3")) - vol(join(tmp, "vocals_muma.mp3")) + 1));
    const inst = readdirSync(tmp).filter((f) => f.endsWith(".mp3") && !f.startsWith("vocals"));
    execFileSync("ffmpeg", ["-y", "-loglevel", "error", ...inst.flatMap((f) => ["-i", join(tmp, f)]), "-i", join(tmp, "vocals_muma.mp3"),
      "-filter_complex", `[${inst.length}:a]volume=${gain.toFixed(1)}dB[v];${inst.map((_, i) => `[${i}:a]`).join("")}[v]amix=inputs=${inst.length + 1}:normalize=0`, "-b:a", "192k", p.songAudio]);
    rmSync(tmp, { recursive: true, force: true });
    console.log(`vokal dönüştürüldü (kazanç ${gain.toFixed(1)} dB); özgün sürüm: ${original}`);
  }
} else {
  console.log("şarkı sağlayıcı: mock (sessiz yer tutucu)");
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", String(totalMs / 1000), "-b:a", "64k", p.songAudio]);
}
const durationSec = Number(execFileSync("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p.songAudio]).toString().trim());

// Satır zamanları: model bölüm sürelerine uyar; satırlar bölüm içinde hece ağırlığıyla dağıtılır (yaklaşık).
const scale = durationSec / (totalMs / 1000);
let t = 0;
const sections = song.sections.map((s) => {
  const start = t, len = (s.durationMs / 1000) * scale;
  const lead = s.direction ? Math.min(1.2, len * 0.15) : 0.15; // çalgı girişi payı
  const w = s.lines.map((l) => words(l).reduce((a, x) => a + syllables(x), 0) + 2);
  const sum = w.reduce((a, b) => a + b, 0);
  let acc = 0;
  const lines = s.lines.map((text, i) => { const ls = start + lead + ((len - lead) * acc) / sum; acc += w[i]; return { text, start: +ls.toFixed(2), end: +(start + lead + ((len - lead) * acc) / sum).toFixed(2) }; });
  t += len;
  return { label: s.label, start: +start.toFixed(2), end: +t.toFixed(2), lines };
});
writeJson(p.song, Song, { provider: useReal ? "elevenlabs" : "mock", model: useReal ? model : null, audioFile: "song.mp3", durationSec, title: song.title, sections });
console.log(`✓ ${p.songAudio} (${durationSec.toFixed(1)} sn)`);
