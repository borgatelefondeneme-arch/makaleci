// Dikey kısa videolar: bölüm sahneleri alt yazısız yeniden çizilir (Short kompozisyonu), ses bölüm videosundan birebir kesilir.
// Yeni ses üretilmez. Kullanım: npx tsx pipeline/render/shorts.ts <episodeDir> tools/shorts/<id>.json
//   spec: [{ name, first, last, headline, kicker?, think?: { q, a } } | { name, song: true, headline }]
//   first/last/q/a: senaryo satırlarının başlangıç metni. *kelime* başlıkta turuncu vurgulanır.
import { renderMedia, selectComposition } from "@remotion/renderer";
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync, rmSync } from "node:fs";
import { cpus } from "node:os";
import { join } from "node:path";
import { episodeDirArg, P } from "../lib/io.ts";
import { browserOpts, loadProps, makeBundle } from "./lib.ts";

type Spec = { name: string; headline: string; kicker?: string; first?: string; last?: string; song?: boolean; think?: { q: string; a: string } };
const { dir, positional } = episodeDirArg() as ReturnType<typeof episodeDirArg> & { positional?: string[] };
const specPath = process.argv.slice(2).find((a) => a.endsWith(".json"))!;
const specs: Spec[] = JSON.parse(readFileSync(specPath, "utf8"));
const props = loadProps(dir);
const { voice, plan, script } = props;
const fps = voice.fps;
const text = new Map(script.sections.flatMap((s) => s.lines).map((l) => [l.id, l.display]));
const lines = plan.scenes.flatMap((sc, i) => sc.lineIds.map((id, k) => ({ t: text.get(id)!, a: voice.scenes[i].startFrame + voice.scenes[i].lineStartFrames[k], b: voice.scenes[i].startFrame + voice.scenes[i].lineEndFrames[k] })));
const find = (prefix: string) => { const l = lines.find((x) => x.t.startsWith(prefix)); if (!l) throw new Error(`Satır bulunamadı: ${prefix}`); return l; };

const outDir = join(P(dir).out, "shorts");
mkdirSync(outDir, { recursive: true });
const serveUrl = await makeBundle();
const MAX = 59.5;
for (const [i, s] of specs.entries()) {
  let from: number, to: number;
  if (s.song) {
    const sg = voice.song!; from = sg.sections[0].lines[0].startFrame - 6; to = sg.endFrame;
  } else {
    from = Math.max(0, find(s.first!).a - 8); to = find(s.last!).b + 14;
  }
  // düşünme molası: cevap satırı ("Düşün bakalım... Evet: …") başlamadan hemen önce 3 sn eklenir;
  // görüntü durur, ses susar, geri sayım oynar. Cevap etiketi molada görünmez.
  const pause = s.think ? { at: find(s.think.a).a - 2, len: 90 } : undefined;
  const short = { from, to, headline: s.headline, kicker: s.kicker, pause, song: !!s.song };
  const inputProps = { ...props, short };
  const opts = { serveUrl, inputProps, ...browserOpts() };
  const comp = await selectComposition({ ...opts, id: "Short" });
  const base = join(outDir, `${i + 1}-${s.name}`);
  const silent = `${base}.silent.mp4`;
  await renderMedia({ ...opts, composition: comp, codec: "h264", outputLocation: silent, muted: true, imageFormat: "jpeg", jpegQuality: 92, crf: 18, concurrency: cpus().length });
  const dur = (to - from + (pause?.len ?? 0)) / fps;
  const k = dur > MAX ? dur / MAX : 1; // şarkı 60 sn'yi az aşarsa perde korunarak hafifçe hızlandırılır
  const od = dur / k;
  const src = join(P(dir).out, "video.mp4");
  // ses: bölüm videosundan birebir; mola varsa araya sessizlik eklenir
  const audio = pause
    ? `[1:a]atrim=${(from / fps).toFixed(3)}:${(pause.at / fps).toFixed(3)},asetpts=PTS-STARTPTS[a1];anullsrc=r=48000:cl=stereo,atrim=0:${(pause.len / fps).toFixed(3)}[sil];[1:a]atrim=${(pause.at / fps).toFixed(3)}:${(to / fps).toFixed(3)},asetpts=PTS-STARTPTS[a2];[a1][sil][a2]concat=n=3:v=0:a=1,aformat=sample_rates=48000:channel_layouts=stereo[ac];[ac]`
    : `[1:a]atrim=${(from / fps).toFixed(3)}:${(to / fps).toFixed(3)},asetpts=PTS-STARTPTS,atempo=${k.toFixed(5)}[ac];[ac]`;
  execFileSync("ffmpeg", ["-v", "error", "-y", "-i", silent, "-i", src,
    "-filter_complex", `[0:v]setpts=PTS/${k.toFixed(5)}[v];${audio}afade=t=in:d=0.2,afade=t=out:st=${Math.max(0, od - 0.5).toFixed(2)}:d=0.5[a]`,
    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-r", String(fps), "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", `${base}.mp4`]);
  execFileSync("ffmpeg", ["-v", "error", "-y", "-ss", "1.2", "-i", `${base}.mp4`, "-frames:v", "1", "-q:v", "3", `${base}.jpg`]);
  rmSync(silent);
  console.log(`✓ ${base}.mp4 (${od.toFixed(1)} sn${k === 1 ? "" : `, x${k.toFixed(3)}`})`);
}
