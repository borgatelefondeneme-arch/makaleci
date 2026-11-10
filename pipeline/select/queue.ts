// Onay kuyruğu: adaylar insan onayı gelene kadar burada bekler.
//   npm run queue -- list | approve <id> | reject <id>
import { existsSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { Selection } from "../../schemas/index.ts";
import { createEpisode } from "../lib/episode.ts";
import { fail, parseArgs, readJson, writeJson } from "../lib/io.ts";

const QUEUE = "data/queue";
const { pos } = parseArgs();
const [cmd, id] = pos;
const files = existsSync(QUEUE) ? readdirSync(QUEUE).filter((f) => f.endsWith(".json")) : [];
const all = files.map((f) => ({ file: join(QUEUE, f), key: f.replace(/\.json$/, ""), sel: readJson(join(QUEUE, f), Selection) }));

if (!cmd || cmd === "list") {
  if (!all.length) console.log("Kuyruk boş.");
  for (const { key, sel } of all.sort((a, b) => b.sel.score - a.sel.score)) {
    console.log(`\n[${sel.status}] ${key}  ·  puan ${sel.score}/100${sel.paper.isPreprint ? "  ·  ÖN BASKI" : ""}`);
    console.log(`  ${sel.paper.title}\n  ${sel.paper.venue ?? "?"} · ${sel.paper.url}\n  ${sel.rationale}`);
  }
} else if (cmd === "approve" || cmd === "reject") {
  const item = all.find((x) => x.key === id || x.sel.paperId === id) ?? fail(`Kuyrukta yok: ${id}`);
  if (item.sel.status !== "pending") fail(`Zaten karar verilmiş: ${item.sel.status}`);
  item.sel.status = cmd === "approve" ? "approved" : "rejected";
  item.sel.decidedAt = new Date().toISOString();
  writeJson(item.file, Selection, item.sel);
  if (cmd === "approve") {
    const dir = createEpisode(item.sel, item.sel.paper.url);
    console.log(`\nOnaylandı. Devam: npm run episode -- --episode ${dir}`);
  }
} else fail("Kullanım: npm run queue -- list | approve <id> | reject <id>");
