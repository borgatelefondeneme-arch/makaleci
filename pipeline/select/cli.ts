// select aşaması: aday havuzu (fetch --recent çıktısı) → merak puanı → en iyi 2 aday kuyruğa (pending).
//   npm run select -- data/pool/<tarih>.json [--top 2]
import { existsSync, mkdirSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { z } from "zod";
import { Paper, Selection } from "../../schemas/index.ts";
import { fail, loadEnv, parseArgs, readJson, slugify, writeJson } from "../lib/io.ts";
import { generateJson } from "../llm/index.ts";

export const QUEUE = "data/queue";
const SYSTEM = `"Günün Bilimi" kanalının editörüsün. Kanal her gün iki bilimsel makaleyi 12 yaşındaki çocuklara 5–6 dakikalık animasyonlu videolarla anlatıyor. Görevin, aday makaleleri "merak uyandırıcılık" açısından puanlamak. Yalnızca başlık ve özete dayan; özetin söylemediği bir sonucu varsayma.`;
const Score = z.object({ id: z.string(), surprise: z.number(), explainable: z.number(), visual: z.number(), concrete: z.number(), rationale: z.string() });

loadEnv();
const { pos, flags } = parseArgs();
if (!pos[0]) fail("Kullanım: npm run select -- <havuz.json> [--top 2]");
const pool = readJson(pos[0], z.array(Paper));
const state = existsSync("data/state.json") ? JSON.parse(readFileSync("data/state.json", "utf8")) : { episodes: {} };
const queued = existsSync(QUEUE) ? new Set(readdirSync(QUEUE).map((f) => readJson(join(QUEUE, f), Selection).paperId)) : new Set<string>();
// Daha önce işlenmiş ya da kuyrukta olanlar elenir.
const fresh = pool.filter((p) => !state.episodes[(p.doi ?? p.id).toLowerCase()] && !queued.has(p.id));
console.log(`${pool.length} aday, ${fresh.length} yeni`);

const scores: z.infer<typeof Score>[] = [];
const BATCH = 40;
for (let i = 0; i < fresh.length; i += BATCH) {
  const batch = fresh.slice(i, i + BATCH);
  const res = await generateJson({
    stage: `select-${String(i / BATCH + 1).padStart(2, "0")}`, manualDir: "data/pool/manual", system: SYSTEM, schema: z.object({ scores: z.array(Score) }),
    prompt: `Her makale için dört ölçütü 0–25 arasında puanla ve bir cümlelik Türkçe gerekçe yaz:
- "surprise": sonuç şaşırtıcı mı, "vay!" dedirtir mi?
- "explainable": 12 yaşındaki bir çocuğa uzmanlık terimi olmadan anlatılabilir mi?
- "visual": animasyonla gösterilebilecek somut bir şey var mı (karşılaştırma, süreç, ölçek)?
- "concrete": özet somut sayılar ve net bir bulgu içeriyor mu?
Yalnızca yöntem geliştiren, çok dar teknik ya da özeti bulgu içermeyen makalelere düşük puan ver. Sağlık konularında yanlış umut doğurabilecek erken aşama çalışmalarda "explainable" puanını düşür.

<adaylar>
${JSON.stringify(batch.map((p) => ({ id: p.id, title: p.title, venue: p.venue, isPreprint: p.isPreprint, abstract: p.abstract.slice(0, 1800) })), null, 1)}
</adaylar>`,
  });
  scores.push(...res.scores);
}

const byId = new Map(fresh.map((p) => [p.id, p]));
const top = scores.filter((s) => byId.has(s.id)).map((s) => ({ s, total: s.surprise + s.explainable + s.visual + s.concrete }))
  .sort((a, b) => b.total - a.total).slice(0, Number(flags.top) || 2);
mkdirSync(QUEUE, { recursive: true });
for (const { s, total } of top) {
  const paper = byId.get(s.id)!;
  const sel: Selection = { paperId: paper.id, paper, score: total, criteria: { surprise: s.surprise, explainable: s.explainable, visual: s.visual, concrete: s.concrete }, rationale: s.rationale, status: "pending", queuedAt: new Date().toISOString(), decidedAt: null };
  writeJson(join(QUEUE, `${slugify(paper.id)}.json`), Selection, sel);
}
console.log(`\n${top.length} aday onay bekliyor → npm run queue -- list`);
