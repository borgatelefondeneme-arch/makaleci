import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { C, W, H } from "../theme";

// Açık, sıcak zemin: yavaş gezen pastel lekeler + süzülen renkli şekiller (hafif ama canlı hareket).
const PASTEL = ["#FFD9BF", "#CFE0FF", "#E3DBFF", "#FFE9B8", "#CDEFDD"];
const SHAPES = Array.from({ length: 26 }, (_, i) => {
  const r = (n: number) => { const x = Math.sin(i * 127.1 + n * 311.7) * 43758.5453; return x - Math.floor(x); };
  return { x: r(1) * W, y: r(2) * H, s: 10 + r(3) * 22, sp: 0.2 + r(4) * 0.45, ph: r(5) * 6.28, c: ["#E08A55", "#4F75B3", "#7B6BD6", "#F2B544", "#17855A"][i % 5], kind: i % 3 };
});

export const Background: React.FC = () => {
  const f = useCurrentFrame();
  const blob = (cx: number, cy: number, r: number, color: string, k: number) => (
    <div style={{
      position: "absolute", left: cx - r + Math.sin(f / (140 + k * 30) + k) * 110, top: cy - r + Math.cos(f / (170 + k * 20) + k * 2) * 80,
      width: r * 2, height: r * 2, borderRadius: "50%", background: `radial-gradient(closest-side, ${color}, transparent)`, opacity: 0.75,
    }} />
  );
  return (
    <AbsoluteFill style={{ background: `linear-gradient(160deg, ${C.bg} 0%, ${C.bg2} 100%)`, overflow: "hidden" }}>
      {blob(260, 220, 620, PASTEL[0], 0)}
      {blob(1640, 880, 700, PASTEL[1], 1)}
      {blob(1520, 140, 480, PASTEL[2], 2)}
      {blob(420, 980, 520, PASTEL[3], 3)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        {SHAPES.map((d, i) => {
          const x = d.x + Math.sin(f / 90 + d.ph) * 30;
          const y = ((d.y - f * d.sp) % (H + 60) + H + 60) % (H + 60) - 30;
          const o = 0.16 + 0.1 * Math.sin(f / 40 + d.ph);
          const rot = f * (0.4 + d.sp) + i * 40;
          if (d.kind === 0) return <circle key={i} cx={x} cy={y} r={d.s / 2} fill={d.c} opacity={o} />;
          if (d.kind === 1) return <rect key={i} x={x - d.s / 2} y={y - d.s / 2} width={d.s} height={d.s} rx={d.s * 0.28} fill="none" stroke={d.c} strokeWidth={4} opacity={o + 0.08} transform={`rotate(${rot} ${x} ${y})`} />;
          return <path key={i} d={`M ${x} ${y - d.s * 0.6} L ${x + d.s * 0.55} ${y + d.s * 0.4} L ${x - d.s * 0.55} ${y + d.s * 0.4} Z`} fill={d.c} opacity={o} transform={`rotate(${rot} ${x} ${y})`} />;
        })}
      </svg>
    </AbsoluteFill>
  );
};
