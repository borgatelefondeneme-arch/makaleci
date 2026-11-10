import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { C, W, H, ACCENTS } from "../theme";

// Arka planda hafif hareket: yavaş kayan degrade lekeler + süzülen noktalar.
const DOTS = Array.from({ length: 34 }, (_, i) => {
  const r = (n: number) => { const x = Math.sin(i * 127.1 + n * 311.7) * 43758.5453; return x - Math.floor(x); };
  return { x: r(1) * W, y: r(2) * H, s: 3 + r(3) * 7, sp: 0.15 + r(4) * 0.35, ph: r(5) * 6.28, c: ACCENTS[i % 4] };
});

export const Background: React.FC = () => {
  const f = useCurrentFrame();
  const blob = (cx: number, cy: number, r: number, color: string, k: number) => (
    <div style={{
      position: "absolute", left: cx - r + Math.sin(f / (140 + k * 30) + k) * 90, top: cy - r + Math.cos(f / (170 + k * 20) + k * 2) * 70,
      width: r * 2, height: r * 2, borderRadius: "50%", background: `radial-gradient(closest-side, ${color}, transparent)`, opacity: 0.22, // blur filtresi yerine degrade: render çok daha hızlı
    }} />
  );
  return (
    <AbsoluteFill style={{ background: `linear-gradient(160deg, ${C.bg} 0%, ${C.bg2} 100%)`, overflow: "hidden" }}>
      {blob(300, 240, 620, C.purple, 0)}
      {blob(1620, 860, 680, C.teal, 1)}
      {blob(1500, 120, 440, C.coral, 2)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        {DOTS.map((d, i) => (
          <circle key={i} cx={d.x + Math.sin(f / 90 + d.ph) * 26} cy={((d.y - f * d.sp) % (H + 40) + H + 40) % (H + 40) - 20}
            r={d.s} fill={d.c} opacity={0.14 + 0.1 * Math.sin(f / 40 + d.ph)} />
        ))}
      </svg>
    </AbsoluteFill>
  );
};
