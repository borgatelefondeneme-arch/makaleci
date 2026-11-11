import React from "react";
import { interpolate } from "remotion";
import type { EpisodeProps } from "../../schemas/index";
import { C, F, GRADIENT } from "../theme";
import { clamp, pop } from "../anim";

// Standart 5 sn açılış: logo animasyonu + "Günün Makalesi #n" + makale başlığı.
export const Intro: React.FC<{ frame: number; data: EpisodeProps }> = ({ frame, data }) => {
  const logo = pop(frame, 4, 9);
  const up = interpolate(frame, [70, 92], [0, 1], clamp);
  const chip = pop(frame, 84);
  const title = pop(frame, 98);
  const letters = "MuMa Library".split("");
  const hello = pop(frame, 44, 10);
  return (
    <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", paddingLeft: 560, paddingRight: 80 }}>
      <div style={{ transform: `translateY(${(1 - up) * 90}px) scale(${1.15 - 0.15 * up})`, display: "flex", alignItems: "center", gap: 26 }}>
        <svg width={120} height={120} viewBox="-60 -60 120 120" style={{ transform: `scale(${logo}) rotate(${frame * 1.2}deg)` }}>
          {[0, 60, 120].map((r) => <ellipse key={r} rx={54} ry={20} fill="none" stroke={C.teal} strokeWidth={6} transform={`rotate(${r})`} />)}
          <circle r={15} fill={C.yellow} />
        </svg>
        <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 124, color: C.text, display: "flex" }}>
          {letters.map((l, i) => {
            const p = pop(frame, 8 + i * 2, 9);
            return <span key={i} style={{ display: "inline-block", whiteSpace: "pre", transform: `translateY(${(1 - p) * 70}px) scale(${p})`, color: C.text, ...(i >= 5 ? { backgroundImage: GRADIENT, backgroundSize: `${7 * 70}px 100%`, backgroundPosition: `${-(i - 5) * 70}px 0`, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" } : {}) }}>{l}</span>;
          })}
        </div>
      </div>
      <div style={{ marginTop: 8, fontFamily: F.head, fontWeight: 800, fontSize: 62, color: C.text, opacity: hello, transform: `translateY(${(1 - up) * 90}px) scale(${0.8 + 0.2 * hello}) rotate(${(1 - hello) * -4}deg)` }}>
        <span style={{ color: C.coral }}>Hoş geldin!</span> 👋
      </div>
      <div style={{ marginTop: 30, opacity: chip, transform: `scale(${chip})`, background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 44, padding: "12px 40px", borderRadius: 50 }}>
        {data.paper.kind === "topic" ? "Günün Sorusu" : "Günün Makalesi"} #{data.script.episodeNumber}
      </div>
      <div style={{ marginTop: 36, opacity: title, transform: `translateY(${(1 - title) * 30}px)`, fontFamily: F.head, fontWeight: 800, fontSize: 60, lineHeight: 1.18, color: C.text, textAlign: "center", maxWidth: 1250 }}>
        {data.script.paperTitleTr}
      </div>
      {data.paper.isPreprint && (
        <div style={{ marginTop: 26, opacity: pop(frame, 112), background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 30, padding: "8px 26px", borderRadius: 30 }}>
          ÖN BASKI · henüz hakem değerlendirmesinden geçmedi
        </div>
      )}
    </div>
  );
};
