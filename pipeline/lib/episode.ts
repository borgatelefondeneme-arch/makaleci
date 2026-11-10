// Bölüm klasörü ve sayaç yönetimi (data/state.json).
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { EpisodeMeta, Paper, Selection } from "../../schemas/index.ts";
import { P, slugify, writeJson } from "./io.ts";

const STATE = "data/state.json";
type State = { lastEpisodeNumber: number; episodes: Record<string, { id: string; episodeNumber: number }> };

const readState = (): State => (existsSync(STATE) ? JSON.parse(readFileSync(STATE, "utf8")) : { lastEpisodeNumber: 0, episodes: {} });

// Onaylanmış bir makale için bölüm klasörü açar. Aynı makale yeniden gelirse aynı klasör ve numara korunur.
export const createEpisode = (sel: Selection, sourceUrl: string | null, fullText?: string | null): string => {
  const state = readState();
  const key = (sel.paper.doi ?? sel.paper.id).toLowerCase();
  let entry = state.episodes[key];
  if (!entry) {
    const date = new Date().toISOString().slice(0, 10);
    entry = { id: `${date}-${slugify(sel.paper.title)}`, episodeNumber: state.lastEpisodeNumber + 1 };
    state.lastEpisodeNumber = entry.episodeNumber;
    state.episodes[key] = entry;
    mkdirSync("data", { recursive: true });
    writeFileSync(STATE, JSON.stringify(state, null, 2) + "\n");
  }
  const dir = join("episodes", entry.id);
  const p = P(dir);
  mkdirSync(dir, { recursive: true });
  if (!existsSync(p.meta)) writeJson(p.meta, EpisodeMeta, { id: entry.id, episodeNumber: entry.episodeNumber, sourceUrl, createdAt: new Date().toISOString() });
  writeJson(p.paper, Paper, sel.paper);
  writeJson(p.selection, Selection, sel);
  if (fullText) writeFileSync(p.fulltext, fullText);
  return dir;
};

export const manualSelection = (paper: Paper): Selection => ({
  paperId: paper.id, paper, score: 0, criteria: { surprise: 0, explainable: 0, visual: 0, concrete: 0 },
  rationale: "Elle seçildi (tek makale linki).", status: "approved", queuedAt: new Date().toISOString(), decidedAt: new Date().toISOString(),
});
