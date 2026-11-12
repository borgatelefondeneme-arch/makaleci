import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { C, F, W } from "../theme";
import { clamp } from "../anim";

// Uzun satırları okunabilir altyazı parçalarına böler (kelime sınırında, ~maxLen karakter).
export const chunkText = (text: string, maxLen = 84): string[] => {
  const words = text.split(/\s+/);
  const n = Math.max(1, Math.ceil(text.length / maxLen));
  const target = text.length / n;
  const out: string[] = [];
  let cur = "";
  for (const w of words) {
    if (cur && (cur + " " + w).length > target + 10 && out.length < n - 1) { out.push(cur); cur = w; }
    else cur = cur ? cur + " " + w : w;
  }
  if (cur) out.push(cur);
  return out;
};

export type CaptionCue = { start: number; end: number; text: string };

export const Caption: React.FC<{ cues: CaptionCue[] }> = ({ cues }) => {
  const f = useCurrentFrame();
  const cue = cues.find((c) => f >= c.start && f < c.end);
  if (!cue) return null;
  const o = interpolate(f, [cue.start, cue.start + 5, cue.end - 3, cue.end], [0, 1, 1, 0.2], clamp);
  return (
    <div style={{ position: "absolute", left: 0, width: W, bottom: 40, display: "flex", justifyContent: "center" }}>
      <div style={{ maxWidth: 1560, background: "rgba(27,34,56,0.88)", color: "#FFFFFF", borderRadius: 26, padding: "14px 36px", fontFamily: F.body, fontWeight: 600, fontSize: 37, lineHeight: 1.3, textAlign: "center", opacity: o }}>
        {cue.text}
      </div>
    </div>
  );
};

export const PreprintBadge: React.FC = () => (
  <div style={{ position: "absolute", right: 40, top: 30, background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 24, padding: "8px 22px", borderRadius: 30, boxShadow: "0 6px 20px rgba(0,0,0,0.3)" }}>
    ÖN BASKI · henüz hakem değerlendirmesinden geçmedi
  </div>
);

export const Chrome: React.FC<{ episode: number; total: number; source?: string; dark?: boolean }> = ({ episode, total, source, dark }) => {
  const f = useCurrentFrame();
  return (<>
    <div style={{ position: "absolute", left: 44, top: 32, fontFamily: F.head, fontWeight: 800, fontSize: 26, color: dark ? "#fff" : C.dim, display: "flex", gap: 12, alignItems: "center" }}>
      <span style={{ width: 16, height: 16, borderRadius: "50%", background: C.yellow, display: "inline-block" }} />
      MuMa Library · #{episode}
      {source && <span style={{ fontFamily: F.body, fontWeight: 600, fontSize: 22, marginLeft: 18, padding: "4px 16px", borderRadius: 20, border: `2px solid ${C.cardLine}` }}>Kaynak: {source}</span>}
    </div>
    <div style={{ position: "absolute", left: 0, bottom: 0, height: 8, width: (W * f) / total, background: C.teal, borderRadius: "0 4px 4px 0" }} />
  </>);
};

