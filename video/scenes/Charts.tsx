import React from "react";
import { interpolate } from "remotion";
import { ACCENTS, C, F } from "../theme";
import { beatAt, clamp, ease, pop } from "../anim";
import { SceneProps, Stage, Title } from "./common";

const CW = 1400, CH = 580; // çizim alanı

// Kendi çizdiğimiz bar grafik: çubuklar sırayla büyür, değerler makaledeki yazımla etiketlenir.
export const BarChart: React.FC<SceneProps<"bar-chart">> = ({ visual, frame, beats, dur }) => {
  const max = Math.max(...visual.bars.map((b) => b.value));
  const n = visual.bars.length;
  const slot = CW / n, bw = Math.min(190, slot * 0.58), base = CH - 70, top = 80;
  return (
    <Stage>
      <Title frame={frame}>{visual.title}</Title>
      <svg width={CW} height={CH} style={{ overflow: "visible" }}>
        <line x1={0} x2={CW} y1={base} y2={base} stroke={C.cardLine} strokeWidth={4} strokeLinecap="round" />
        {[0.25, 0.5, 0.75, 1].map((g) => (
          <line key={g} x1={0} x2={CW} y1={base - (base - top) * g} y2={base - (base - top) * g} stroke={C.cardLine} strokeWidth={2} strokeDasharray="6 12" opacity={0.5} />
        ))}
        {visual.bars.map((b, i) => {
          const s = beatAt(beats, i, dur, n);
          const g = ease(frame, s, 26);
          const h = Math.max(6, ((base - top) * b.value) / max) * g;
          const x = slot * i + (slot - bw) / 2;
          const col = b.highlight ? C.yellow : ACCENTS[i % 4 === 1 ? 3 : i % 4];
          const lp = pop(frame, s + 18);
          return (
            <g key={i}>
              <rect x={x} y={base - h} width={bw} height={h} rx={18} fill={col} />
              <rect x={x} y={base - h} width={bw} height={Math.min(h, 26)} rx={13} fill="#fff" opacity={0.18} />
              <text x={x + bw / 2} y={base - h - 22} textAnchor="middle" fontFamily={F.head} fontWeight={900} fontSize={50} fill={C.text} opacity={lp}>
                {b.display}
              </text>
              <text x={x + bw / 2} y={base + 52} textAnchor="middle" fontFamily={F.body} fontWeight={600} fontSize={32} fill={C.dim} opacity={ease(frame, s, 10)}>
                {b.label}
              </text>
            </g>
          );
        })}
      </svg>
      {visual.unit && <div style={{ position: "absolute", right: 0, top: 14, fontFamily: F.body, fontSize: 28, color: C.dim }}>Birim: {visual.unit}</div>}
    </Stage>
  );
};

export const LineChart: React.FC<SceneProps<"line-chart">> = ({ visual, frame, beats }) => {
  const pts = visual.points;
  const ys = pts.map((p) => p.value);
  const lo = Math.min(...ys), hi = Math.max(...ys);
  const pad = (hi - lo) * 0.18 || 1;
  const x0 = 110, x1 = CW - 50, y0 = CH - 90, y1 = 50;
  const X = (i: number) => x0 + ((x1 - x0) * i) / (pts.length - 1);
  const Y = (v: number) => y0 - ((y0 - y1) * (v - (lo - pad))) / (hi - lo + 2 * pad);
  const d = pts.map((p, i) => `${i ? "L" : "M"} ${X(i)} ${Y(p.value)}`).join(" ");
  let len = 0;
  for (let i = 1; i < pts.length; i++) len += Math.hypot(X(i) - X(i - 1), Y(pts[i].value) - Y(pts[i - 1].value));
  const start = (beats[0] ?? 0) + 10;
  const drawLen = Math.max(45, pts.length * 14);
  const t = interpolate(frame, [start, start + drawLen], [0, 1], clamp);
  return (
    <Stage>
      <Title frame={frame}>{visual.title}</Title>
      <svg width={CW} height={CH} style={{ overflow: "visible" }}>
        <line x1={x0} x2={x1} y1={y0} y2={y0} stroke={C.cardLine} strokeWidth={4} strokeLinecap="round" />
        <line x1={x0} x2={x0} y1={y0} y2={y1 - 20} stroke={C.cardLine} strokeWidth={4} strokeLinecap="round" />
        <text x={(x0 + x1) / 2} y={CH - 4} textAnchor="middle" fontFamily={F.body} fontWeight={600} fontSize={30} fill={C.dim}>{visual.xLabel}</text>
        <text transform={`translate(34 ${(y0 + y1) / 2}) rotate(-90)`} textAnchor="middle" fontFamily={F.body} fontWeight={600} fontSize={30} fill={C.dim}>{visual.yLabel}</text>
        <path d={`${d} L ${X(pts.length - 1)} ${y0} L ${X(0)} ${y0} Z`} fill={C.teal} opacity={0.14 * t} />
        <path d={d} fill="none" stroke={C.teal} strokeWidth={9} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={len} strokeDashoffset={len * (1 - t)} />
        {pts.map((p, i) => {
          const a = pop(frame, start + (drawLen * i) / (pts.length - 1));
          const showVal = pts.length <= 6 || p.highlight || i === 0 || i === pts.length - 1;
          return (
            <g key={i} opacity={a}>
              <circle cx={X(i)} cy={Y(p.value)} r={(p.highlight ? 17 : 12) * a} fill={p.highlight ? C.yellow : C.bg} stroke={p.highlight ? C.yellow : C.teal} strokeWidth={6} />
              {showVal && <text x={X(i)} y={Y(p.value) - 30} textAnchor="middle" fontFamily={F.head} fontWeight={900} fontSize={38} fill={C.text}>{p.display}</text>}
              <text x={X(i)} y={y0 + 42} textAnchor="middle" fontFamily={F.body} fontSize={26} fill={C.dim}>{p.label}</text>
            </g>
          );
        })}
      </svg>
    </Stage>
  );
};
