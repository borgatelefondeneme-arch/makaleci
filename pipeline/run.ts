// Orkestratör: aşamaları sırayla, ayrı süreçler olarak çalıştırır.
//   npm run episode -- --url <makale linki>          (tek makale, doğrudan onaylı)
//   npm run episode -- --episode episodes/<id>       (kuyruktan onaylanmış bölüm)
//   bayraklar: --from script|sceneplan|voice|render  --force  --allow-duration  --no-video  --mock
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Paper } from "../schemas/index.ts";
import { createEpisode, manualSelection } from "./lib/episode.ts";
import { fail, P, parseArgs, readJson } from "./lib/io.ts";

const { flags } = parseArgs();
const run = (cmd: string, args: string[]) => {
  console.log(`\n━━ ${cmd} ${args.join(" ")}`);
  try { execFileSync(cmd, args, { stdio: "inherit" }); } catch { process.exit(1); } // alt süreç hatasını zaten yazdı
};
const tsx = (file: string, args: string[]) => run("npx", ["tsx", file, ...args]);

let dir: string;
if (typeof flags.url === "string") {
  // 1. fetch + 2. select (tek link doğrudan onaylı sayılır)
  const tmp = mkdtempSync(join(tmpdir(), "gb-"));
  const out = join(tmp, "paper.json"), ft = join(tmp, "fulltext.txt");
  run("python3", ["-m", "pipeline.fetch.cli", "--url", flags.url, "--out", out, "--fulltext", ft]);
  const paper = readJson(out, Paper);
  dir = createEpisode(manualSelection(paper), flags.url, existsSync(ft) ? readFileSync(ft, "utf8") : null);
} else if (typeof flags.episode === "string") dir = flags.episode;
else fail("Kullanım: npm run episode -- --url <link> | --episode <klasör>");
console.log(`\nBölüm klasörü: ${dir!}`);

const p = P(dir!);
const stages = [
  { name: "script", file: "pipeline/script/cli.ts", done: p.script, args: [] as string[] },
  { name: "sceneplan", file: "pipeline/sceneplan/cli.ts", done: p.scenes, args: [] },
  { name: "voice", file: "pipeline/voice/cli.ts", done: p.voice, args: [...(flags["allow-duration"] ? ["--allow-duration"] : []), ...(flags.mock ? ["--mock"] : [])] },
  { name: "render", file: "pipeline/render/cli.ts", done: join(p.out, "video.mp4"), args: flags["no-video"] ? ["--no-video"] : [] },
];
const from = typeof flags.from === "string" ? stages.findIndex((s) => s.name === flags.from) : 0;
if (from < 0) fail(`Bilinmeyen aşama: ${flags.from}`);
stages.forEach((s, i) => {
  // Çıktısı olan aşama atlanır; --force ya da --from ile o aşamadan itibaren yeniden üretilir.
  const redo = flags.force || (typeof flags.from === "string" && i >= from);
  if (existsSync(s.done) && !redo) return console.log(`\n━━ ${s.name}: çıktı var, atlandı (${s.done})`);
  tsx(s.file, [dir!, ...s.args, ...(redo && s.name === "script" ? ["--force"] : [])]);
});
console.log(`\nBitti → ${p.out}`);
