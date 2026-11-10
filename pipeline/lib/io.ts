// Aşamaların ortak dosya/JSON yardımcıları.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import type { z } from "zod";

export const loadEnv = (path = ".env") => {
  if (!existsSync(path)) return;
  for (const line of readFileSync(path, "utf8").split("\n")) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && m[2] && !process.env[m[1]]) process.env[m[1]] = m[2].replace(/^['"]|['"]$/g, "");
  }
};

export const readJson = <S extends z.ZodType>(path: string, schema: S): z.infer<S> => {
  if (!existsSync(path)) fail(`Girdi bulunamadı: ${path} (önceki aşama çalıştı mı?)`);
  const r = schema.safeParse(JSON.parse(readFileSync(path, "utf8")));
  if (!r.success) fail(`${path} şemaya uymuyor:\n${fmtIssues(r.error)}`);
  return r.data as z.infer<S>;
};

export const writeJson = <S extends z.ZodType>(path: string, schema: S, data: unknown) => {
  const r = schema.safeParse(data);
  if (!r.success) fail(`${path} yazılamadı, çıktı şemaya uymuyor:\n${fmtIssues(r.error)}`);
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, JSON.stringify(r.data, null, 2) + "\n");
  console.log(`✓ ${path}`);
};

export const fmtIssues = (e: z.ZodError) => e.issues.slice(0, 15).map((i) => `  - ${i.path.join(".")}: ${i.message}`).join("\n");

export const fail = (msg: string): never => {
  console.error(`\n✗ ${msg}\n`);
  process.exit(1);
};

// CLI: konumsal bölüm klasörü + bayraklar.
export const parseArgs = (argv = process.argv.slice(2)) => {
  const flags: Record<string, string | true> = {};
  const pos: string[] = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith("--")) {
      const next = argv[i + 1];
      if (next !== undefined && !next.startsWith("--")) { flags[a.slice(2)] = next; i++; } else flags[a.slice(2)] = true;
    } else pos.push(a);
  }
  return { flags, pos };
};

export const episodeDirArg = () => {
  const { pos, flags } = parseArgs();
  if (!pos[0]) fail("Kullanım: <komut> <episodeDir> [--force]");
  return { dir: pos[0], flags };
};

export const P = (dir: string) => ({
  meta: join(dir, "episode.json"),
  paper: join(dir, "01_paper.json"),
  fulltext: join(dir, "01_fulltext.txt"),
  selection: join(dir, "02_selection.json"),
  facts: join(dir, "03_facts.json"),
  script: join(dir, "03_script.json"),
  scenes: join(dir, "04_scenes.json"),
  voice: join(dir, "05_voice.json"),
  audio: join(dir, "audio"),
  out: join(dir, "out"),
  manual: join(dir, "manual"),
});

// Türkçe metin yardımcıları
export const words = (t: string) => t.trim().split(/\s+/).filter(Boolean);
export const syllables = (w: string) => {
  const v = (w.match(/[aeıioöuüâîûAEIİOÖUÜ]/g) ?? []).length;
  const d = (w.match(/\d/g) ?? []).length; // rakamlar okununca uzar
  return Math.max(1, v + Math.round(d * 2.4));
};
// Metindeki sayı belirteçleri; "3,5" ile "3.5" aynı sayılır.
export const numberTokens = (t: string) => (t.match(/\d+(?:[.,]\d+)*/g) ?? []).map((n) => n.replace(/,/g, "."));
export const slugify = (t: string) =>
  t.toLowerCase().replace(/ı/g, "i").replace(/ğ/g, "g").replace(/ü/g, "u").replace(/ş/g, "s").replace(/ö/g, "o").replace(/ç/g, "c")
    .replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 48).replace(/-$/, "");
