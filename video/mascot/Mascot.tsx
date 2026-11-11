import React from "react";
import { Img, staticFile } from "remotion";
import { C } from "../theme";

// Kanalın sabit karakteri: kullanıcının verdiği robot (cin kuyruklu, yay antenli).
// Kullanıcının 3B videosu tools/cutout_video.py ile saydam zeminli kare dizisine çevrildi
// (public/robot/seq/NNNN.webp). Karakter bu gerçek hareket karelerini oynatır:
//   40–157  karşılama (eller açık) → işaret pozuna geçiş
//   157–193 işaret pozu (parmak havada + açık el) — konuşma döngüsü
//   193–244 kolları kavuşturma geçişi
//   244–280 kollar kavuşuk — bekleme/düşünme döngüsü
export const SEQ = { first: 40, last: 285, greet: 40, pointA: 157, pointB: 193, crossA: 244, crossB: 280 };
export const ASPECT = 784 / 1168; // kare genişlik / yükseklik
export const seqSrc = (idx: number) => staticFile(`robot/seq/${String(Math.min(SEQ.last, Math.max(SEQ.first, Math.round(idx)))).padStart(4, "0")}.webp`);

export type MascotProps = {
  frame: number;
  idx: number; // oynatılacak kaynak kare
  mouth: number; // 0..1 ses genliği (konuşurken hafif vurgu)
  flip: boolean; // true: açık el ekranın soluna bakar
  think: number; // 0..1 düşünce baloncuğu
  lean: number; // derece; işaret edilen yöne eğilme
  size: number; // yükseklik (px)
};

export const Mascot: React.FC<MascotProps> = ({ frame: f, idx, mouth, flip, think, lean, size }) => {
  const bob = Math.sin(f / 16) * size * 0.01;
  const pulse = 1 + mouth * 0.014;
  const width = size * ASPECT;
  return (
    <div style={{ position: "relative", width, height: size }}>
      <div style={{ position: "absolute", left: "50%", bottom: size * 0.01, width: width * 0.5, height: size * 0.03, marginLeft: -width * 0.25, borderRadius: "50%", background: "#000", opacity: 0.18 }} />
      <div style={{ position: "absolute", inset: 0, transform: `translateY(${bob}px) rotate(${lean}deg) scale(${flip ? -pulse : pulse}, ${pulse})`, transformOrigin: "50% 55%" }}>
        <Img src={seqSrc(idx)} style={{ position: "absolute", left: 0, top: 0, width, height: size }} />
      </div>
      {think > 0.05 && (
        <svg width={size * 0.3} height={size * 0.225} viewBox="0 0 160 120" style={{ position: "absolute", left: flip ? width * 0.02 : width * 0.68, top: size * 0.0 + Math.sin(f / 9) * 3, opacity: think, overflow: "visible", transform: flip ? "scaleX(-1)" : undefined }}>
          <circle cx={14} cy={104} r={7} fill="#fff" /><circle cx={34} cy={82} r={11} fill="#fff" />
          <circle cx={92} cy={46} r={42} fill="#fff" stroke={C.purple} strokeWidth={5} />
          <text x={92} y={66} textAnchor="middle" fontFamily="Nunito, sans-serif" fontWeight={900} fontSize={58} fill={C.purple} transform={flip ? "translate(184 0) scale(-1 1)" : undefined}>?</text>
        </svg>
      )}
    </div>
  );
};
