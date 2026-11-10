// Denetim aracı: bölümden örnek kareler çıkarır (render beklemeden).
//   npm run frames -- <episodeDir>                → her sahnenin ortası + açılış, hatırlatma, kapanış
//   npm run frames -- <episodeDir> --at 0,150,900 → belirli kareler
//   npm run frames -- <episodeDir> --transitions  → her sahne sınırının ±6 karesi
import { renderStill, selectComposition } from "@remotion/renderer";
import { mkdirSync } from "node:fs";
import { join } from "node:path";
import { episodeDirArg, P } from "../lib/io.ts";
import { browserOpts, loadProps, makeBundle } from "./lib.ts";

const { dir, flags } = episodeDirArg();
const props = loadProps(dir);
const { voice, plan } = props;
const out = join(P(dir).out, typeof flags.dir === "string" ? flags.dir : "frames");
mkdirSync(out, { recursive: true });

let shots: { frame: number; name: string }[] = [];
if (typeof flags.at === "string") shots = flags.at.split(",").map((x) => ({ frame: Number(x), name: `f${x.padStart(5, "0")}` }));
else if (flags.transitions) shots = voice.scenes.flatMap((s, i) => [-6, 0, 6, 12].map((d) => ({ frame: s.startFrame + d, name: `t${String(i + 1).padStart(2, "0")}_${s.sceneId}_${d < 0 ? "m" : "p"}${Math.abs(d)}` })));
else {
  shots = [{ frame: 40, name: "00_acilis_a" }, { frame: 120, name: "00_acilis_b" }];
  voice.scenes.forEach((s, i) => {
    const tail = i === voice.scenes.length - 1 ? voice.outroTailFrames : 0;
    shots.push({ frame: s.startFrame + Math.round((s.durationFrames - tail) * 0.72), name: `${String(i + 1).padStart(2, "0")}_${s.sceneId}_${plan.scenes[i].visual.type}` });
  });
  shots.push({ frame: voice.reminder.startFrame + Math.round(voice.reminder.durationFrames * 0.35), name: "90_abone_ol_hatirlatma_a" });
  shots.push({ frame: voice.reminder.startFrame + Math.round(voice.reminder.durationFrames * 0.65), name: "90_abone_ol_hatirlatma_b" });
  shots.push({ frame: voice.totalFrames - 120, name: "99_kapanis_abone_ol" });
}

const serveUrl = await makeBundle();
const opts = { serveUrl, inputProps: props, ...browserOpts() };
const composition = await selectComposition({ ...opts, id: "Episode" });
const scale = Number(flags.scale) || 0.5;
for (const s of shots) {
  const frame = Math.max(0, Math.min(voice.totalFrames - 1, s.frame));
  await renderStill({ ...opts, composition, frame, output: join(out, `${s.name}.jpg`), imageFormat: "jpeg", jpegQuality: 88, scale });
  console.log(`✓ ${join(out, s.name)}.jpg (kare ${frame})`);
}
