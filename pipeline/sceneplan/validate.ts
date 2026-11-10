import type { Facts, ScenePlan, Script } from "../../schemas/index.ts";
import { numberTokens } from "../lib/io.ts";
import type { Report } from "../script/validate.ts";

const strings = (v: unknown, skip = new Set(["type", "template", "layout", "tone", "emoji"])): string[] =>
  typeof v === "string" ? [v] : Array.isArray(v) ? v.flatMap((x) => strings(x, skip))
    : v && typeof v === "object" ? Object.entries(v).filter(([k]) => !skip.has(k)).flatMap(([, x]) => strings(x, skip)) : [];

export const validatePlan = (plan: ScenePlan, script: Script, facts: Facts): Report => {
  const errors: string[] = [], warnings: string[] = [];
  const factById = new Map(facts.facts.map((f) => [f.id, f]));
  const lines = script.sections.flatMap((s) => s.lines.map((l) => ({ ...l, section: s.id })));
  const lineById = new Map(lines.map((l) => [l.id, l]));

  // Her satır tam bir kez ve sırayla
  const planned = plan.scenes.flatMap((s) => s.lineIds);
  if (planned.join() !== lines.map((l) => l.id).join()) errors.push("Sahnelerdeki satırlar senaryoyla aynı sırada ve eksiksiz değil");

  plan.scenes.forEach((s, i) => {
    for (const id of s.factIds) if (!factById.has(id)) errors.push(`${s.id}: bilinmeyen olgu ${id}`);
    if (i > 0 && plan.scenes[i - 1].visual.type === s.visual.type) errors.push(`${s.id}: önceki sahneyle aynı tip (${s.visual.type})`);
    // Görseldeki sayılar sahnenin olgularında ya da satırlarının olgularında bulunmalı
    const ids = new Set([...s.factIds, ...s.lineIds.flatMap((id) => lineById.get(id)?.factIds ?? [])]);
    const allowed = new Set([...ids].flatMap((id) => factById.get(id)?.numbers ?? []).flatMap(numberTokens));
    for (const n of strings(s.visual).flatMap(numberTokens)) if (!allowed.has(n)) errors.push(`${s.id}: görseldeki "${n}" sayısı olgularda yok`);
    // Grafik değeri ile etiketi tutarlı mı?
    const items = s.visual.type === "bar-chart" ? s.visual.bars : s.visual.type === "line-chart" ? s.visual.points : [];
    for (const it of items) {
      const t = numberTokens(it.display)[0];
      if (t !== undefined && Math.abs(Number(t) - it.value) > 1e-9 && Math.abs(Number(t.replace(/\./g, "")) - it.value) > 1e-9) errors.push(`${s.id}: "${it.label}" çubuğunda value (${it.value}) ile display (${it.display}) uyuşmuyor`);
    }
    if (s.mascot.state === "point" && !s.mascot.pointAt) warnings.push(`${s.id}: mascot "point" ama pointAt verilmemiş`);
  });

  const first = plan.scenes[0], last = plan.scenes[plan.scenes.length - 1];
  if (first?.visual.type !== "hook") errors.push("İlk sahne hook olmalı");
  if (last?.visual.type !== "outro") errors.push("Son sahne outro olmalı");
  else {
    const summary = script.sections.find((x) => x.id === "summary")!.lines.map((l) => l.id);
    if (last.lineIds.join() !== summary.join()) errors.push("outro sahnesi summary bölümünün tüm satırlarını (ve yalnızca onları) kapsamalı");
  }
  if (!plan.scenes.some((s) => s.visual.type === "source-card")) errors.push("Künye için source-card sahnesi yok");
  const types = new Set(plan.scenes.map((s) => s.visual.type));
  if (types.size < 5) warnings.push(`Yalnızca ${types.size} farklı sahne tipi kullanılmış`);
  const pos = new Set(plan.scenes.map((s) => `${s.mascot.x.toFixed(1)},${s.mascot.y.toFixed(1)},${s.mascot.scale.toFixed(1)}`));
  if (pos.size < 3) warnings.push("Mascot neredeyse hiç yer değiştirmiyor");
  const states = new Set(plan.scenes.map((s) => s.mascot.state));
  return { errors, warnings, stats: { sahne: plan.scenes.length, tip: [...types].join(", "), mascotDurumlari: [...states].join(", "), mascotKonum: pos.size } };
};
