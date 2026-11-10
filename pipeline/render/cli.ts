// render aşaması: scenes + voice → out/video.mp4, out/thumbnail.png, out/yayin.md
import { renderMedia, renderStill, selectComposition } from "@remotion/renderer";
import { execFileSync } from "node:child_process";
import { mkdirSync, rmSync, writeFileSync } from "node:fs";
import { cpus } from "node:os";
import { join } from "node:path";
import { Facts } from "../../schemas/index.ts";
import { episodeDirArg, loadEnv, P, readJson } from "../lib/io.ts";
import { browserOpts, loadProps, makeBundle } from "./lib.ts";
import { publishMd } from "./publish.ts";

loadEnv();
const { dir, flags } = episodeDirArg();
const p = P(dir);
const props = loadProps(dir);
mkdirSync(p.out, { recursive: true });

writeFileSync(join(p.out, "yayin.md"), publishMd(props, readJson(p.facts, Facts)));
console.log(`✓ ${join(p.out, "yayin.md")}`);

const serveUrl = await makeBundle();
const opts = { serveUrl, inputProps: props, ...browserOpts() };

const thumb = await selectComposition({ ...opts, id: "Thumbnail" });
await renderStill({ ...opts, composition: thumb, output: join(p.out, "thumbnail.png"), scale: 2 / 3 }); // 1280×720
console.log(`✓ ${join(p.out, "thumbnail.png")}`);

if (!flags["no-video"]) {
  const composition = await selectComposition({ ...opts, id: "Episode" });
  const silent = join(p.out, "silent.mp4");
  const t0 = Date.now();
  let lastPct = -1;
  await renderMedia({
    ...opts, composition, codec: "h264", outputLocation: silent, muted: true, imageFormat: "jpeg", jpegQuality: 92, crf: 18,
    concurrency: Number(flags.concurrency) || cpus().length,
    onProgress: ({ progress }) => { const pct = Math.floor(progress * 20) * 5; if (pct !== lastPct) { lastPct = pct; console.log(`  render %${pct} (${Math.round((Date.now() - t0) / 1000)} sn)`); } },
  });
  // Ses FFmpeg ile eklenir; gerçek seste yayın standardına (−14 LUFS) normalize edilir.
  const final = join(p.out, "video.mp4");
  const af = props.voice.provider === "mock" ? [] : ["-af", "loudnorm=I=-14:TP=-1.5:LRA=11"];
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", silent, "-i", join(dir, props.voice.audioFile), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", ...af, "-shortest", "-movflags", "+faststart", final]);
  rmSync(silent);
  console.log(`✓ ${final}`);
}
