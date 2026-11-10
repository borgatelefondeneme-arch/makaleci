import React from "react";
import { interpolate } from "remotion";
import type { EpisodeProps } from "../../schemas/index";
import { C, F } from "../theme";
import { clamp, pop } from "../anim";

// Standart 5 sn açılış: logo animasyonu + "Günün Makalesi #n" + makale başlığı.
export const Intro: React.FC<{ frame: number; data: EpisodeProps }> = ({ frame, data }) => {
  const logo = pop(frame, 4, 9);
  const up = interpolate(frame, [38, 58], [0, 1], clamp);
  const chip = pop(frame, 46);
  const title = pop(frame, 62);
  const letters = "Günün Bilimi".split("");
  return (
    <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", paddingLeft: 520, paddingRight: 90 }}>
      <div style={{ transform: `translateY(${(1 - up) * 150}px) scale(${1.25 - 0.25 * up})`, display: "flex", alignItems: "center", gap: 26 }}>
        <svg width={120} height={120} viewBox="-60 -60 120 120" style={{ transform: `scale(${logo}) rotate(${frame * 1.2}deg)` }}>
          {[0, 60, 120].map((r) => <ellipse key={r} rx={54} ry={20} fill="none" stroke={C.teal} strokeWidth={6} transform={`rotate(${r})`} />)}
          <circle r={15} fill={C.yellow} />
        </svg>
        <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 124, color: C.text, display: "flex" }}>
          {letters.map((l, i) => {
            const p = pop(frame, 8 + i * 2, 9);
            return <span key={i} style={{ display: "inline-block", whiteSpace: "pre", transform: `translateY(${(1 - p) * 70}px) scale(${p})`, color: i >= 6 ? C.yellow : C.text }}>{l}</span>;
          })}
        </div>
      </div>
      <div style={{ marginTop: 40, opacity: chip, transform: `scale(${chip})`, background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 44, padding: "12px 40px", borderRadius: 50 }}>
        {data.paper.kind === "topic" ? "Günün Sorusu" : "Günün Makalesi"} #{data.script.episodeNumber}
      </div>
      <div style={{ marginTop: 36, opacity: title, transform: `translateY(${(1 - title) * 30}px)`, fontFamily: F.head, fontWeight: 800, fontSize: 60, lineHeight: 1.18, color: C.text, textAlign: "center", maxWidth: 1250 }}>
        {data.script.paperTitleTr}
      </div>
      {data.paper.isPreprint && (
        <div style={{ marginTop: 26, opacity: pop(frame, 80), background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 30, padding: "8px 26px", borderRadius: 30 }}>
          ÖN BASKI · henüz hakem değerlendirmesinden geçmedi
        </div>
      )}
    </div>
  );
};
