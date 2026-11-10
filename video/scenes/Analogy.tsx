import React from "react";
import { C, F } from "../theme";
import { beatAt, ease, lerp, pop } from "../anim";
import { SceneProps, Stage, Title } from "./common";

// Benzetme animasyonu — parametreli şablonlar. a ve b değerleri oranı belirler.
export const Analogy: React.FC<SceneProps<"analogy">> = ({ visual, frame, beats, dur }) => {
  const { a, b, template } = visual;
  const max = Math.max(a.value, b.value);
  const sA = beatAt(beats, 0, dur, 2), sB = beatAt(beats, 1, dur, 2);
  const AW = 1400, AH = 490;
  const lab = (x: number, y: number, it: typeof a, col: string, st: number, anchor: "middle" | "start" = "middle") => (
    <g opacity={pop(frame, st + 12)}>
      <text x={x} y={y} textAnchor={anchor} fontFamily={F.head} fontWeight={800} fontSize={38} fill={col}>{it.label}</text>
      {it.display && <text x={x} y={y + 52} textAnchor={anchor} fontFamily={F.head} fontWeight={900} fontSize={50} fill={C.text}>{it.display}</text>}
    </g>
  );
  let art: React.ReactNode = null;
  if (template === "scale") {
    // alanı değerle orantılı iki daire
    const R = 190, rA = R * Math.sqrt(a.value / max), rB = R * Math.sqrt(b.value / max);
    const pA = pop(frame, sA, 10), pB = pop(frame, sB, 10);
    art = (<>
      <circle cx={360} cy={210} r={Math.max(4, rA) * pA} fill={C.teal} />
      <circle cx={1000} cy={210} r={Math.max(4, rB) * pB} fill={C.yellow} />
      {lab(360, 440, a, C.teal, sA)}{lab(1000, 440, b, C.yellow, sB)}
    </>);
  } else if (template === "fill") {
    // dolan iki kap
    const cup = (x: number, it: typeof a, col: string, st: number) => {
      const lvl = (it.value / max) * ease(frame, st, 40);
      const hgt = 330 * lvl, wave = Math.sin(frame / 6) * 5;
      return (<g>
        <clipPath id={`cup${x}`}><rect x={x - 120} y={30} width={240} height={340} rx={26} /></clipPath>
        <g clipPath={`url(#cup${x})`}>
          <path d={`M ${x - 120} ${370 - hgt + wave} Q ${x} ${370 - hgt - wave * 2} ${x + 120} ${370 - hgt + wave} L ${x + 120} 372 L ${x - 120} 372 Z`} fill={col} opacity={0.9} />
        </g>
        <rect x={x - 120} y={30} width={240} height={340} rx={26} fill="none" stroke={C.text} strokeWidth={7} />
        {lab(x, 430, it, col, st)}
      </g>);
    };
    art = <>{cup(380, a, C.teal, sA)}{cup(1000, b, C.yellow, sB)}</>;
  } else if (template === "race") {
    // iki kulvar: mesafe değerle orantılı
    const lane = (y: number, it: typeof a, col: string, st: number) => {
      const t = ease(frame, st, 50);
      const x = lerp(250, 250 + 1050 * (it.value / max), t);
      return (<g>
        <line x1={250} x2={1300} y1={y} y2={y} stroke={C.cardLine} strokeWidth={10} strokeLinecap="round" strokeDasharray="2 26" />
        <line x1={250} x2={x} y1={y} y2={y} stroke={col} strokeWidth={14} strokeLinecap="round" />
        <circle cx={x} cy={y + Math.abs(Math.sin(frame / 4)) * -10 * (t < 1 ? 1 : 0)} r={30} fill={col} stroke={C.ink} strokeWidth={5} />
        <text x={0} y={y - 6} fontFamily={F.head} fontWeight={800} fontSize={34} fill={col}>{it.label}</text>
        {it.display && <text x={0} y={y + 38} fontFamily={F.head} fontWeight={900} fontSize={40} fill={C.text} opacity={pop(frame, st + 40)}>{it.display}</text>}
      </g>);
    };
    art = <>{lane(140, a, C.teal, sA)}{lane(340, b, C.yellow, sB)}</>;
  } else {
    // zoom: küçük olan büyüğün içinde; kamera uzaklaşarak ölçeği gösterir
    const big = a.value >= b.value ? a : b, small = a.value >= b.value ? b : a;
    const ratio = Math.max(0.03, Math.sqrt(small.value / big.value));
    const z = lerp(1 / ratio * 0.5, 1, ease(frame, sB - 10, 50));
    art = (<>
      <g transform={`translate(700 220) scale(${Math.min(z, 12)})`}>
        <circle r={210} fill={C.purple} opacity={0.35} stroke={C.purple} strokeWidth={6 / z} />
        <circle r={210 * ratio} fill={C.yellow} />
      </g>
      {lab(140, 120, small, C.yellow, sA, "start")}{lab(1080, 400, big, C.purple, sB, "start")}
    </>);
  }
  return (
    <Stage>
      <Title frame={frame} color={C.yellow}>{visual.title}</Title>
      <svg width={AW} height={AH} style={{ overflow: "visible" }}>{art}</svg>
      <div style={{ fontFamily: F.body, fontWeight: 600, fontSize: 36, color: C.text, opacity: pop(frame, sB + 30), marginTop: 20, maxWidth: 1300 }}>{visual.caption}</div>
    </Stage>
  );
};
