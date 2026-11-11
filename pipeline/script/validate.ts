// Senaryo denetimleri: geçemeyen senaryo sonraki aşamaya gidemez.
import type { Facts, Paper, Script } from "../../schemas/index.ts";
import { numberTokens, words } from "../lib/io.ts";

export type Report = { errors: string[]; warnings: string[]; stats: Record<string, number | string> };

const ORDER = ["hook", "context", "method", "finding", "importance", "limitations", "summary"];
const HYPE = [/mucize/i, /devrim/i, /kesin(likle)? kan[ıi]tla/i, /her şeyi değiştir/i, /inanılmaz/i, /şok/i, /çığır aç/i, /tarihte ilk/i, /bilim insanlarını şaşkına/i, /tedaviyi buldu/i];
const norm = (s: string) => s.toLocaleLowerCase("tr").replace(/\s+/g, " ");

export const validateScript = (script: Script, facts: Facts, paper: Paper): Report => {
  const errors: string[] = [], warnings: string[] = [];
  const factById = new Map(facts.facts.map((f) => [f.id, f]));
  const lines = script.sections.flatMap((s) => s.lines.map((l) => ({ ...l, section: s.id })));
  const allDisplay = norm(lines.map((l) => l.display).join(" "));

  // 1. Bölüm sırası
  const ids = script.sections.map((s) => s.id);
  if (ids.join() !== ORDER.join()) errors.push(`Bölümler eksik ya da sırasız: ${ids.join(" → ")} (beklenen: ${ORDER.join(" → ")})`);

  // 2. Satır kimlikleri ve olgu bağlantıları
  const seen = new Set<string>();
  for (const l of lines) {
    if (seen.has(l.id)) errors.push(`Yinelenen satır kimliği: ${l.id}`);
    seen.add(l.id);
    for (const id of l.factIds) if (!factById.has(id)) errors.push(`${l.id}: bilinmeyen olgu ${id}`);
    if (!l.spoken.trim() || !l.display.trim()) errors.push(`${l.id}: display/spoken boş`);
  }

  // 3. Sayı sadakati: display'deki her sayı, satırın olgularında birebir bulunmalı.
  const doi = paper.doi ?? "";
  for (const l of lines) {
    const text = doi ? l.display.split(doi).join(" ") : l.display; // DOI içindeki rakamlar sayı değildir
    const allowed = new Set(l.factIds.flatMap((id) => factById.get(id)?.numbers ?? []).flatMap(numberTokens));
    for (const n of numberTokens(text)) {
      if (!allowed.has(n)) errors.push(`${l.id}: "${n}" sayısı bağlı olgularda yok (factIds: ${l.factIds.join(", ") || "boş"}) → "${l.display}"`);
    }
  }

  // 4. Kaynaksız satırlar: yalnızca soru/geçiş olabilir, sınırlı sayıda.
  const unsourced = lines.filter((l) => l.factIds.length === 0);
  const core = lines.filter((l) => ["method", "finding", "importance", "limitations"].includes(l.section));
  const coreUnsourced = core.filter((l) => l.factIds.length === 0);
  if (coreUnsourced.length > core.length * 0.25) errors.push(`Yöntem/bulgu/önem/sınırlılık bölümlerinde kaynaksız satır çok fazla (${coreUnsourced.length}/${core.length}): ${coreUnsourced.map((l) => l.id).join(", ")}`);
  if (unsourced.length) warnings.push(`Olgu bağlantısı olmayan ${unsourced.length} satır (geçiş/soru olmalı, elle gözden geçirin): ${unsourced.map((l) => l.id).join(", ")}`);

  const topic = paper.kind === "topic";
  if (topic && facts.sources.length === 0) errors.push("Konu bölümünde en az bir kaynak (facts.sources) gerekli");
  // 5. Künye: yazar, kurum, dergi, DOI ekranda (ve dolayısıyla seslendirilen satırda) geçmeli.
  const ctx = script.sections.find((s) => s.id === "context")?.lines ?? [];
  const surname = paper.authors[0]?.name.trim().split(/\s+/).pop();
  if (topic) {
    // Makale yok: künye yerine kaynak kurumlarının adı senaryoda geçmeli.
    for (const s of facts.sources) if (!allDisplay.includes(norm(s.publisher))) warnings.push(`Kaynak "${s.publisher}" senaryoda adıyla anılmıyor`);
    if (!facts.sources.some((s) => allDisplay.includes(norm(s.publisher)))) errors.push("Hiçbir kaynak senaryoda adıyla anılmıyor");
  } else if (!surname || !allDisplay.includes(norm(surname))) errors.push(`İlk yazarın adı (${surname ?? "?"}) senaryoda geçmiyor`);
  if (!topic && paper.venue && !allDisplay.includes(norm(paper.venue))) errors.push(`Dergi/kaynak (${paper.venue}) senaryoda geçmiyor`);
  const insts = paper.institutions.length ? paper.institutions : facts.institutions;
  if (!topic && insts.length === 0) warnings.push("Kurum bilgisi yok (ne API'lerde ne makale metninde).");
  if (doi) {
    const doiLine = lines.find((l) => l.display.includes(doi));
    if (!doiLine) errors.push(`DOI (${doi}) ekranda tam yazılmamış`);
    else if (!/nokta/i.test(doiLine.spoken) || !/b[öo]l[üu]/i.test(doiLine.spoken)) errors.push(`${doiLine.id}: DOI seslendirmede tam okunmuyor ("nokta", "bölü" ile karakter karakter okunmalı)`);
  }
  if (!ctx.length) errors.push("context bölümü boş");

  // 6. Preprint uyarısı
  if (paper.isPreprint && !/ön baskı/i.test(allDisplay)) errors.push("Makale ön baskı ama senaryoda \"ön baskı\" olduğu söylenmiyor");

  // 7. Abartı
  for (const l of lines) for (const re of HYPE) if (re.test(l.display) || re.test(l.spoken)) errors.push(`${l.id}: abartılı ifade (${re.source}) → "${l.display}"`);

  // 7b. Şarkı sözleri: sayı ve abartı içeremez; içerik olgulara dayanmalı (insan gözüyle doğrulanır).
  if (script.song) {
    const lyr = script.song.sections.flatMap((s) => s.lines);
    for (const l of lyr) {
      if (/\d/.test(l)) errors.push(`Şarkı sözünde rakam var (yazıyla yazın ya da çıkarın): "${l}"`);
      for (const re of HYPE) if (re.test(l)) errors.push(`Şarkı sözünde abartılı ifade (${re.source}): "${l}"`);
      if (l.length > 200) errors.push(`Şarkı dizesi çok uzun (en çok 200 karakter): "${l.slice(0, 40)}…"`);
    }
    const ms = script.song.sections.reduce((a, s) => a + s.durationMs, 0);
    if (ms < 40000 || ms > 80000) warnings.push(`Şarkı ${Math.round(ms / 1000)} sn; hedef yaklaşık 60 sn`);
    warnings.push(`Şarkı sözleri (${lyr.length} dize) olgu listesine göre elle doğrulanmalı`);
  }

  // 7c. Sözlük: varsa anlatımda izleyiciye haber verilmeli; terimler senaryoda geçmeli.
  if (script.glossary.length) {
    if (!/sözlük/i.test(allDisplay)) errors.push('Sözlük var ama anlatımda "açıklamalarda bir sözlük bırakıyorum" duyurusu yok');
    for (const g of script.glossary) if (!allDisplay.includes(norm(g.term))) warnings.push(`Sözlükteki "${g.term}" senaryoda geçmiyor`);
  } else if (topic) warnings.push("Sözlük boş: çocukların bilmeyebileceği kelimeler varsa glossary'ye ekleyin");

  // 8. Uzunluk
  const wc = lines.reduce((a, l) => a + words(l.spoken).length, 0);
  const hookWc = (script.sections.find((s) => s.id === "hook")?.lines ?? []).reduce((a, l) => a + words(l.spoken).length, 0);
  // Kelime sayısı yalnızca kaba bir ön kontrol; kesin kararı voice aşamasındaki süre kapısı verir.
  if (wc < (script.song ? 330 : 450) || wc > 1500) errors.push(`Seslendirme ${wc} kelime; 5–6 dakika için çok ${wc < 450 ? "kısa" : "uzun"}`);
  else if (!topic && (wc < 720 || wc > 880)) warnings.push(`Seslendirme ${wc} kelime; hedef aralığın (720–880) dışında — süre kapısı voice aşamasında kesin karar verir`);
  if (hookWc < 20 || hookWc > 50) warnings.push(`Hook ${hookWc} kelime; ~15 sn için 30–40 kelime hedeflenir`);
  if (script.videoTitle.length > 70) warnings.push(`Video başlığı uzun (${script.videoTitle.length} karakter)`);

  return { errors, warnings, stats: { satir: lines.length, kelime: wc, hookKelime: hookWc, kaynaksizSatir: unsourced.length, olgu: facts.facts.length, dayanak: facts.basis } };
};

export const printReport = (title: string, r: Report) => {
  console.log(`\n── ${title} ──`);
  console.log(Object.entries(r.stats).map(([k, v]) => `${k}: ${v}`).join(" · "));
  for (const w of r.warnings) console.log(`  ⚠ ${w}`);
  for (const e of r.errors) console.log(`  ✗ ${e}`);
  console.log(r.errors.length ? `  SONUÇ: ${r.errors.length} hata` : "  SONUÇ: geçti");
};
