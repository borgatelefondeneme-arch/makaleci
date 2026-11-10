import React from "react";
import { C } from "../theme";

// "Zerre" — atom/gezegen kafalı özgün karakter. Tamamen parametrik, sahneden bağımsız.
export type MascotPose = {
  frame: number; // sürekli animasyonlar için
  mouth: number; // 0..1 ağız açıklığı (ses genliği)
  point: number; // 0..1 işaret etme miktarı
  think: number; // 0..1 düşünme miktarı
  angle: number; // işaret yönü (radyan, ekran koordinatı; 0 = sağ)
};

const INK = C.ink;
const mix = (a: number, b: number, t: number) => a + (b - a) * t;

export const Mascot: React.FC<MascotPose & { size: number }> = ({ frame: f, mouth, point, think, angle, size }) => {
  const bob = Math.sin(f / 13) * 6;
  const blinkT = f % 96;
  const blink = blinkT < 5 ? Math.abs(blinkT - 2.5) / 2.5 : 1;
  const squash = 1 + mouth * 0.035;

  // Yörünge halkası: düşünürken yavaşlar.
  const tilt = -18;
  const RX = 132, RY = 40;
  const th = f * mix(0.11, 0.035, think);
  const ex = RX * Math.cos(th), ey = RY * Math.sin(th);
  const electron = <circle cx={ex} cy={ey} r={11} fill={C.coral} stroke={INK} strokeWidth={4} />;
  const front = Math.sin(th) > 0;

  // Bakış: işaret ederken hedefe, düşünürken yukarı.
  const gx = mix(0, Math.cos(angle) * 7, point) + think * -4;
  const gy = mix(0, Math.sin(angle) * 6, point) + think * -7;

  // Eller: sağ taraf mı sol taraf mı işaret ediyor?
  const right = Math.cos(angle) >= 0;
  const rest = { l: { x: -98, y: 44 + Math.sin(f / 11) * 4 }, r: { x: 98, y: 44 + Math.sin(f / 11 + 1.5) * 4 } };
  const reach = 142;
  const tgt = { x: Math.cos(angle) * reach, y: Math.sin(angle) * reach * 0.9 };
  const chin = { x: 40, y: 70 };
  let L = { ...rest.l }, R = { ...rest.r };
  if (right) { R = { x: mix(R.x, tgt.x, point), y: mix(R.y, tgt.y, point) }; }
  else { L = { x: mix(L.x, tgt.x, point), y: mix(L.y, tgt.y, point) }; }
  R = { x: mix(R.x, chin.x, think), y: mix(R.y, chin.y, think) };
  // konuşurken eller hafif oynar
  const gest = mouth * (1 - point) * (1 - think);
  L.y -= gest * 14; R.y -= gest * 10;

  const hand = (p: { x: number; y: number }, pointing: number, a: number) => (
    <g transform={`translate(${p.x} ${p.y})`}>
      {pointing > 0.05 && (
        <g transform={`rotate(${(a * 180) / Math.PI})`}>
          <rect x={6} y={-6.5} width={10 + 26 * pointing} height={13} rx={6.5} fill="#FFB627" stroke={INK} strokeWidth={4} />
        </g>
      )}
      <circle r={17} fill="#FFB627" stroke={INK} strokeWidth={4.5} />
    </g>
  );

  const open = mouth > 0.07;
  const mh = 4 + mouth * 22;

  return (
    <svg width={size} height={size} viewBox="-170 -170 340 340" style={{ overflow: "visible" }}>
      <defs>
        <radialGradient id="zerre-body" cx="35%" cy="30%" r="80%">
          <stop offset="0%" stopColor="#FFE680" />
          <stop offset="55%" stopColor={C.yellow} />
          <stop offset="100%" stopColor="#F5A623" />
        </radialGradient>
      </defs>
      <ellipse cx={0} cy={138} rx={70 - bob} ry={11} fill="#000" opacity={0.22} />
      <g transform={`translate(0 ${bob})`}>
        <g transform={`rotate(${tilt})`}>
          <path d={`M ${-RX} 0 A ${RX} ${RY} 0 0 1 ${RX} 0`} fill="none" stroke={C.teal} strokeWidth={9} strokeLinecap="round" opacity={0.75} />
          {!front && electron}
        </g>
        {/* ayaklar */}
        <ellipse cx={-30} cy={88} rx={20} ry={12} fill="#F5A623" stroke={INK} strokeWidth={4.5} />
        <ellipse cx={30} cy={88} rx={20} ry={12} fill="#F5A623" stroke={INK} strokeWidth={4.5} />
        <g transform={`scale(${1 / squash} ${squash})`}>
          <circle r={84} fill="url(#zerre-body)" stroke={INK} strokeWidth={6} />
          <ellipse cx={-34} cy={-46} rx={22} ry={12} fill="#fff" opacity={0.45} transform="rotate(-28 -34 -46)" />
          {/* yanaklar */}
          <circle cx={-52} cy={16} r={12} fill={C.coral} opacity={0.45} />
          <circle cx={52} cy={16} r={12} fill={C.coral} opacity={0.45} />
          {/* gözler */}
          {[-28, 28].map((x) => (
            <g key={x} transform={`translate(${x} -12)`}>
              <ellipse rx={17} ry={21 * blink + 1} fill="#fff" stroke={INK} strokeWidth={4} />
              {blink > 0.4 && (<>
                <circle cx={gx} cy={gy + 2} r={9.5} fill={INK} />
                <circle cx={gx + 3} cy={gy - 2} r={3.2} fill="#fff" />
              </>)}
            </g>
          ))}
          {/* kaşlar: düşünürken biri kalkar */}
          <path d={`M -42 ${-42 - think * 4} q 14 -8 28 0`} fill="none" stroke={INK} strokeWidth={4.5} strokeLinecap="round" />
          <path d={`M 14 ${-42 - think * 12} q 14 -8 28 ${think * 6}`} fill="none" stroke={INK} strokeWidth={4.5} strokeLinecap="round" />
          {/* ağız */}
          {open ? (
            <g transform="translate(0 38)">
              <ellipse rx={17 - mouth * 3} ry={mh} fill="#5A1F2E" stroke={INK} strokeWidth={4} />
              <ellipse cx={0} cy={mh * 0.55} rx={9} ry={mh * 0.38} fill={C.coral} />
            </g>
          ) : (
            <path d={think > 0.5 ? "M -10 40 q 10 -4 20 2" : "M -17 34 q 17 16 34 0"} fill="none" stroke={INK} strokeWidth={5} strokeLinecap="round" />
          )}
        </g>
        <g transform={`rotate(${tilt})`}>
          <path d={`M ${-RX} 0 A ${RX} ${RY} 0 0 0 ${RX} 0`} fill="none" stroke={C.teal} strokeWidth={9} strokeLinecap="round" />
          {front && electron}
        </g>
        {hand(L, right ? 0 : point, angle)}
        {hand(R, right ? point * (1 - think) : 0, angle)}
        {/* düşünce baloncukları */}
        {think > 0.05 && (
          <g opacity={think}>
            <circle cx={92} cy={-92} r={8} fill="#fff" stroke={INK} strokeWidth={3.5} />
            <circle cx={112} cy={-118} r={12} fill="#fff" stroke={INK} strokeWidth={3.5} />
            <g transform={`translate(142 ${-162 + Math.sin(f / 9) * 4}) scale(${0.6 + 0.4 * think})`}>
              <circle r={34} fill="#fff" stroke={INK} strokeWidth={4.5} />
              <text y={17} textAnchor="middle" fontFamily="Nunito, sans-serif" fontWeight={900} fontSize={50} fill={C.purple}>?</text>
            </g>
          </g>
        )}
      </g>
    </svg>
  );
};
