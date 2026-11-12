import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { C, F, W, H } from "../theme";
import { DEFAULT_LOOK, Look } from "../look";

// Açık, sıcak zemin; deseni ve tonu bölümden bölüme değişir (look.bg): lekeler, dalgalar, nokta ızgarası,
// ışınlar ya da balonlar. Üstünde bölümün konu simgeleri soluk biçimde süzülür.
const INK = ["#E08A55", "#4F75B3", "#7B6BD6", "#F2B544", "#17855A"];
const rnd = (i: number, n: number) => { const x = Math.sin(i * 127.1 + n * 311.7) * 43758.5453; return x - Math.floor(x); };
const SHAPES = Array.from({ length: 26 }, (_, i) => ({ x: rnd(i, 1) * W, y: rnd(i, 2) * H, s: 10 + rnd(i, 3) * 22, sp: 0.2 + rnd(i, 4) * 0.45, ph: rnd(i, 5) * 6.28, c: INK[i % 5], kind: i % 3 }));

export const Background: React.FC<{ look?: Look }> = ({ look = DEFAULT_LOOK }) => {
  const f = useCurrentFrame();
  const P = look.pastel;
  const blob = (cx: number, cy: number, r: number, color: string, k: number, o = 0.75) => (
    <div key={`b${k}`} style={{
      position: "absolute", left: cx - r + Math.sin(f / (140 + k * 30) + k) * 110, top: cy - r + Math.cos(f / (170 + k * 20) + k * 2) * 80,
      width: r * 2, height: r * 2, borderRadius: "50%", background: `radial-gradient(closest-side, ${color}, transparent)`, opacity: o,
    }} />
  );
  const wrapY = (y: number) => ((y % (H + 120)) + H + 120) % (H + 120) - 60;
  let layer: React.ReactNode = null;
  if (look.bg === 0) {
    layer = (<>
      {blob(260, 220, 620, P[0], 0)}{blob(1640, 880, 700, P[1], 1)}{blob(1520, 140, 480, P[2], 2)}{blob(420, 980, 520, P[3], 3)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        {SHAPES.map((d, i) => {
          const x = d.x + Math.sin(f / 90 + d.ph) * 30, y = wrapY(d.y - f * d.sp);
          const o = 0.16 + 0.1 * Math.sin(f / 40 + d.ph), rot = f * (0.4 + d.sp) + i * 40;
          if (d.kind === 0) return <circle key={i} cx={x} cy={y} r={d.s / 2} fill={d.c} opacity={o} />;
          if (d.kind === 1) return <rect key={i} x={x - d.s / 2} y={y - d.s / 2} width={d.s} height={d.s} rx={d.s * 0.28} fill="none" stroke={d.c} strokeWidth={4} opacity={o + 0.08} transform={`rotate(${rot} ${x} ${y})`} />;
          return <path key={i} d={`M ${x} ${y - d.s * 0.6} L ${x + d.s * 0.55} ${y + d.s * 0.4} L ${x - d.s * 0.55} ${y + d.s * 0.4} Z`} fill={d.c} opacity={o} transform={`rotate(${rot} ${x} ${y})`} />;
        })}
      </svg>
    </>);
  } else if (look.bg === 1) {
    // dalgalar: üstte ve altta yana doğru akan katmanlı dalga bantları
    const wave = (y0: number, amp: number, len: number, speed: number, flip: boolean) => {
      let d = `M -200 ${flip ? -50 : H + 50}`;
      for (let x = -200; x <= W + 200; x += 40) d += ` L ${x} ${y0 + Math.sin((x + f * speed) / len) * amp + Math.sin((x - f * speed * 0.6) / (len * 0.47)) * amp * 0.35}`;
      return d + ` L ${W + 200} ${flip ? -50 : H + 50} Z`;
    };
    layer = (<>
      {blob(960, 520, 760, P[2], 0, 0.45)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        <path d={wave(190, 46, 210, 1.4, true)} fill={P[1]} opacity={0.55} />
        <path d={wave(110, 34, 150, -2.0, true)} fill={P[0]} opacity={0.6} />
        <path d={wave(H - 250, 52, 230, 1.7, false)} fill={P[3]} opacity={0.5} />
        <path d={wave(H - 150, 40, 170, -1.2, false)} fill={P[1]} opacity={0.55} />
        <path d={wave(H - 70, 28, 120, 2.4, false)} fill={P[0]} opacity={0.7} />
      </svg>
    </>);
  } else if (look.bg === 2) {
    // nokta ızgarası: çapraz kayan noktalar + iki büyük leke
    const G = 96, ox = (f * 0.5) % G, oy = (f * 0.3) % G;
    layer = (<>
      {blob(380, 300, 700, P[0], 0, 0.7)}{blob(1560, 800, 760, P[1], 1, 0.7)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        {Array.from({ length: 22 * 13 }, (_, i) => {
          const cx = (i % 22) * G - G + ox, cy = Math.floor(i / 22) * G - G + oy;
          const pulse = 0.5 + 0.5 * Math.sin(f / 28 + (i % 22) * 0.5 + Math.floor(i / 22) * 0.7);
          return <circle key={i} cx={cx} cy={cy} r={4 + pulse * 5} fill={INK[(i + Math.floor(i / 22)) % 5]} opacity={0.1 + pulse * 0.1} />;
        })}
      </svg>
    </>);
  } else if (look.bg === 3) {
    // ışınlar: köşeden yayılan, çok yavaş dönen geniş pastel ışın demeti
    layer = (<>
      <svg width={W} height={H} style={{ position: "absolute" }}>
        <g transform={`translate(${W * 0.12} ${H * 0.1}) rotate(${f * 0.05})`}>
          {Array.from({ length: 16 }, (_, i) => <path key={i} d="M 0 0 L -170 -2600 L 170 -2600 Z" fill={P[i % 4]} opacity={0.28} transform={`rotate(${i * 22.5})`} />)}
        </g>
        <circle cx={W * 0.12} cy={H * 0.1} r={150 + Math.sin(f / 30) * 14} fill={P[3]} opacity={0.85} />
      </svg>
      {blob(1500, 900, 620, P[1], 1, 0.55)}
    </>);
  } else {
    // balonlar: farklı hızlarda yükselen halkalar
    layer = (<>
      {blob(300, 860, 640, P[0], 0, 0.7)}{blob(1600, 240, 640, P[2], 2, 0.7)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        {Array.from({ length: 30 }, (_, i) => {
          const r = 16 + rnd(i, 3) * 58, x = rnd(i, 1) * W + Math.sin(f / (50 + i * 3) + i) * 28, y = wrapY(rnd(i, 2) * H - f * (0.5 + rnd(i, 4) * 1.1));
          return <g key={i} opacity={0.2 + rnd(i, 5) * 0.16}><circle cx={x} cy={y} r={r} fill={P[i % 4]} stroke={INK[i % 5]} strokeWidth={3} /><circle cx={x - r * 0.35} cy={y - r * 0.35} r={r * 0.16} fill="#fff" /></g>;
        })}
      </svg>
    </>);
  }
  return (
    <AbsoluteFill style={{ background: `linear-gradient(160deg, ${C.bg} 0%, ${C.bg2} 100%)`, overflow: "hidden" }}>
      {layer}
      {/* konu simgeleri: soluk, yavaş süzülür; içerikle yarışmaz */}
      {look.motifs.length > 0 && Array.from({ length: 9 }, (_, i) => {
        const size = 70 + rnd(i, 7) * 70;
        const x = rnd(i, 8) * (W - 160) + Math.sin(f / (70 + i * 9) + i * 2) * 40;
        const y = wrapY(rnd(i, 9) * H + (i % 2 ? 1 : -1) * f * (0.18 + rnd(i, 10) * 0.25));
        return <div key={i} style={{ position: "absolute", left: x, top: y, fontSize: size, lineHeight: 1, fontFamily: F.head, opacity: 0.1, transform: `rotate(${Math.sin(f / (60 + i * 7) + i) * 18}deg)` }}>{look.motifs[i % look.motifs.length]}</div>;
      })}
    </AbsoluteFill>
  );
};
