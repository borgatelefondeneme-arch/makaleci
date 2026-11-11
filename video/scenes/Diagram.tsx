import React from "react";
import { ACCENTS, C, F } from "../theme";
import { beatAt, ease, pop } from "../anim";
import { activeIndex } from "../components/Motion";
import { SceneProps, Stage, Title } from "./common";

// Basit diyagram: akış (kutu → ok → kutu) veya döngü.
export const Diagram: React.FC<SceneProps<"diagram">> = ({ visual, frame, beats, dur }) => {
  const n = visual.nodes.length;
  const AW = 1480, AH = 580;
  const bw = visual.layout === "flow" ? Math.min(360, (AW - (n - 1) * 90) / n) : 290, bh = visual.layout === "flow" ? 280 : 200;
  const pos = visual.nodes.map((_, i) => {
    if (visual.layout === "flow") {
      const gap = (AW - n * bw) / Math.max(1, n - 1);
      return { x: i * (bw + gap) + bw / 2, y: AH / 2 - 20 };
    }
    const a = -Math.PI / 2 + (i * 2 * Math.PI) / n;
    return { x: AW / 2 - 120 + Math.cos(a) * 430, y: AH / 2 - 10 + Math.sin(a) * 185 };
  });
  const edges = visual.layout === "flow" ? n - 1 : n;
  return (
    <Stage>
      <Title frame={frame} color={C.purple}>{visual.title}</Title>
      <div style={{ position: "relative", width: AW, height: AH, margin: "auto 0" }}>
        <svg width={AW} height={AH} style={{ position: "absolute", overflow: "visible" }}>
          {Array.from({ length: edges }, (_, i) => {
            const a = pos[i], b = pos[(i + 1) % n];
            const dx = b.x - a.x, dy = b.y - a.y, L = Math.hypot(dx, dy);
            const ux = dx / L, uy = dy / L;
            const m = visual.layout === "flow" ? bw / 2 + 12 : 175;
            const x1 = a.x + ux * m, y1 = a.y + uy * m, x2 = b.x - ux * m, y2 = b.y - uy * m;
            const t = ease(frame, beatAt(beats, (i + 1) % n || n - 1, dur, n) - 12, 14);
            const ex = x1 + (x2 - x1) * t, ey = y1 + (y2 - y1) * t;
            const ang = (Math.atan2(dy, dx) * 180) / Math.PI;
            return (
              <g key={i} opacity={t > 0 ? 1 : 0}>
                <line x1={x1} y1={y1} x2={ex} y2={ey} stroke={C.dim} strokeWidth={8} strokeLinecap="round" />
                {t >= 1 && [0, 1, 2].map((k) => { const u = ((frame * 0.035 + k / 3) % 1); return <circle key={k} cx={x1 + (x2 - x1) * u} cy={y1 + (y2 - y1) * u} r={9} fill={ACCENTS[i % 4]} opacity={Math.sin(u * Math.PI)} />; })}
                <path d="M -22 -16 L 6 0 L -22 16 Z" fill={C.dim} transform={`translate(${ex} ${ey}) rotate(${ang})`} />
              </g>
            );
          })}
        </svg>
        {visual.nodes.map((nd, i) => {
          const p = pop(frame, beatAt(beats, i, dur, n));
          const col = ACCENTS[i % 4];
          return (
            <div key={i} style={{
              position: "absolute", left: pos[i].x - bw / 2, top: pos[i].y - bh / 2, width: bw, height: bh, boxSizing: "border-box",
              background: C.card, border: `4px solid ${col}`, borderRadius: 32, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 8, padding: 14,
              transform: `translateY(${Math.sin(frame / 16 + i * 1.3) * 7}px) scale(${p * (1 + (activeIndex(beats, frame) === Math.min(i, beats.length - 1) ? 0.06 + 0.02 * Math.sin(frame / 5) : 0))}) rotate(${Math.sin(frame / 21 + i) * 1.5}deg)`, opacity: p, boxShadow: `0 14px 36px ${C.shadow}`,
            }}>
              {nd.emoji && <div style={{ fontSize: visual.layout === "flow" ? 104 : 68, lineHeight: 1.1, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 9 + i * 2) * 9}deg) scale(${1 + 0.06 * Math.sin(frame / 7 + i)})` }}>{nd.emoji}</div>}
              <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: visual.layout === "flow" ? 36 : 32, color: C.text, textAlign: "center", lineHeight: 1.15 }}>{nd.label}</div>
              <div style={{ position: "absolute", top: -22, left: -22, width: 52, height: 52, borderRadius: "50%", background: col, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 30, display: "flex", alignItems: "center", justifyContent: "center" }}>{i + 1}</div>
            </div>
          );
        })}
      </div>
    </Stage>
  );
};
