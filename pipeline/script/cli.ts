// script aşaması: 01_paper.json (+ tam metin) → 03_facts.json + 03_script.json
import { existsSync, readFileSync } from "node:fs";
import { EpisodeMeta, Facts, Paper, Script } from "../../schemas/index.ts";
import { episodeDirArg, fail, loadEnv, P, readJson, writeJson } from "../lib/io.ts";
import { generateJson, hasClaude } from "../llm/index.ts";
import { FACTS_SYSTEM, factsPrompt, SCRIPT_SYSTEM, scriptPrompt } from "./prompts.ts";
import { printReport, validateScript } from "./validate.ts";

loadEnv();
const { dir, flags } = episodeDirArg();
const p = P(dir);
const paper = readJson(p.paper, Paper);
const meta = readJson(p.meta, EpisodeMeta);
const fullText = existsSync(p.fulltext) ? readFileSync(p.fulltext, "utf8") : null;

// (a) Olgu çıkarımı
let facts: Facts;
if (existsSync(p.facts) && !flags.force) facts = readJson(p.facts, Facts);
else {
  facts = await generateJson({ stage: "facts", manualDir: p.manual, system: FACTS_SYSTEM, prompt: factsPrompt(paper, fullText), schema: Facts });
  // Alıntılar gerçekten makalede geçiyor mu? (boşluk farkları yok sayılır)
  const hay = `${paper.title} ${paper.abstract} ${fullText ?? ""}`.replace(/\s+/g, " ").toLowerCase();
  const missing = facts.facts.filter((f) => f.kind !== "meta" && !hay.includes(f.quote.replace(/\s+/g, " ").toLowerCase().slice(0, 60)));
  if (missing.length) console.log(`  ⚠ ${missing.length} olgunun alıntısı makale metninde birebir bulunamadı (elle doğrulayın): ${missing.map((f) => f.id).join(", ")}`);
  writeJson(p.facts, Facts, facts);
}

// (b) Senaryo — denetimden geçemezse geri bildirimle en çok 2 kez yeniden yazdırılır (yalnızca API modunda).
let feedback: string | undefined;
for (let attempt = 1; ; attempt++) {
  const script = await generateJson({ stage: "script", manualDir: p.manual, system: SCRIPT_SYSTEM, prompt: scriptPrompt(paper, facts, meta.episodeNumber, feedback), schema: Script });
  script.episodeNumber = meta.episodeNumber;
  script.paperId = paper.id;
  const report = validateScript(script, facts, paper);
  printReport(`Senaryo denetimi (deneme ${attempt})`, report);
  if (!report.errors.length) { writeJson(p.script, Script, script); break; }
  if (!hasClaude() || attempt >= 3) fail("Senaryo denetimden geçemedi; yukarıdaki hataları düzeltin.");
  feedback = report.errors.map((e) => `- ${e}`).join("\n");
}
