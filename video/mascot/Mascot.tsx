import React from "react";
import { Img, staticFile } from "remotion";
import { C } from "../theme";

// Kanalın sabit karakteri: kullanıcının verdiği robot (cin kuyruklu, yay antenli).
// Görseller public/robot/ altında; tools/cutout.py ile saydam zeminli kesildi.
// Pozlar hazır görsel olduğu için kollar yeniden çizilmez; canlılık süzülme, kuyruk salınımı,
// ağız (ses genliği), anten yıldızı ve poz geçişleriyle sağlanır.
export type Pose = "point" | "crossed";
type Sprite = { src: string; w: number; h: number; waist: number; mouth: { x: number; y: number; w: number; rot: number; depth: number }; star: { x: number; y: number } };
export const SPRITES: Record<Pose, Sprite> = {
  point: { src: "robot/point.png", w: 799, h: 1522, waist: 930, mouth: { x: 366, y: 341, w: 37, rot: 0, depth: 30 }, star: { x: 616, y: 147 } },
  crossed: { src: "robot/crossed.png", w: 543, h: 1041, waist: 585, mouth: { x: 254, y: 174, w: 30, rot: -7, depth: 22 }, star: { x: 434, y: 100 } },
};
export const ASPECT = 0.56; // kapsayıcı genişlik / yükseklik

export type MascotPose = {
  frame: number;
  mouth: number; // 0..1 ses genliği
  pose: Pose;
  blend: number; // 0..1: önceki pozdan bu poza geçiş
  prevPose: Pose;
  flip: boolean; // true: açık el ekranın soluna bakar
  think: number; // 0..1
  lean: number; // derece; işaret edilen yöne eğilme
};

const Layer: React.FC<{ pose: Pose; frame: number; mouth: number; opacity: number; height: number }> = ({ pose, frame: f, mouth, opacity, height }) => {
  if (opacity <= 0.01) return null;
  const s = SPRITES[pose];
  const k = height / s.h;
  const width = s.w * k;
  const sway = Math.sin(f / 17) * 2.2; // kuyruk salınımı (derece)
  const waistPct = (s.waist / s.h) * 100;
  const img: React.CSSProperties = { position: "absolute", left: 0, top: 0, width, height };
  const m = s.mouth;
  const open = Math.max(0, mouth - 0.06);
  const d = m.depth * (0.5 + open * 0.95); // ağız derinliği
  const glow = 0.55 + 0.45 * Math.sin(f / 7) + mouth * 0.5;
  return (
    <div style={{ position: "absolute", left: "50%", top: 0, width, height, marginLeft: -width / 2, opacity }}>
      {/* kuyruk: belden aşağısı hafifçe salınır */}
      <Img src={staticFile(s.src)} style={{ ...img, clipPath: `inset(${waistPct}% 0 0 0)`, transformOrigin: `50% ${waistPct}%`, transform: `skewX(${sway}deg) scaleY(${1 + Math.sin(f / 23) * 0.012})` }} />
      <Img src={staticFile(s.src)} style={{ ...img, clipPath: `inset(0 0 ${100 - waistPct - 0.2}% 0)` }} />
      <svg width={width} height={height} viewBox={`0 0 ${s.w} ${s.h}`} style={{ position: "absolute", left: 0, top: 0, overflow: "visible" }}>
        {/* anten yıldızı: sesle birlikte parlar */}
        <circle cx={s.star.x} cy={s.star.y} r={34 + glow * 16} fill="#FFE9A8" opacity={0.16 + glow * 0.14} />
        <circle cx={s.star.x} cy={s.star.y} r={16 + glow * 6} fill="#FFF6D6" opacity={0.25 + glow * 0.2} />
        {/* ağız: konuşurken mevcut gülüşün üstüne açılır */}
        {open > 0 && (
          <g transform={`translate(${m.x} ${m.y}) rotate(${m.rot})`}>
            <path d={`M ${-m.w} 0 Q 0 ${m.w * 0.16} ${m.w} 0 Q ${m.w * 0.5} ${d * 1.35} 0 ${d * 1.4} Q ${-m.w * 0.5} ${d * 1.35} ${-m.w} 0 Z`} fill="#4A3B42" stroke="#C9CCD8" strokeWidth={2.5} strokeLinejoin="round" />
            <ellipse cx={0} cy={d * 0.95} rx={m.w * 0.45} ry={d * 0.32} fill="#FF9E6B" opacity={0.75} />
          </g>
        )}
      </svg>
    </div>
  );
};

// Kapsayıcı: size = yükseklik (px). İki poz katmanı çapraz geçişle karışır.
export const Mascot: React.FC<MascotPose & { size: number }> = ({ frame: f, mouth, pose, prevPose, blend, flip, think, lean, size }) => {
  const bob = Math.sin(f / 14) * size * 0.014;
  const tilt = Math.sin(f / 29) * 1.2 + lean + think * -3;
  const squash = 1 + mouth * 0.012;
  const width = size * ASPECT;
  return (
    <div style={{ position: "relative", width, height: size }}>
      <div style={{ position: "absolute", left: "50%", bottom: -size * 0.02, width: width * 0.6, height: size * 0.035, marginLeft: -width * 0.3, borderRadius: "50%", background: "#000", opacity: 0.2, transform: `scaleX(${1 - bob / size * 4})` }} />
      <div style={{ position: "absolute", inset: 0, transform: `translateY(${bob}px) rotate(${tilt}deg) scale(${flip ? -1 : 1}, 1) scale(${1 / squash}, ${squash})`, transformOrigin: "50% 60%" }}>
        {prevPose !== pose && <Layer pose={prevPose} frame={f} mouth={mouth} opacity={1 - blend} height={size} />}
        <Layer pose={pose} frame={f} mouth={mouth} opacity={prevPose === pose ? 1 : blend} height={size} />
      </div>
      {/* düşünce baloncuğu (çevrilmez) */}
      {think > 0.05 && (
        <svg width={size * 0.4} height={size * 0.3} viewBox="0 0 160 120" style={{ position: "absolute", left: flip ? -size * 0.2 : width * 0.72, top: -size * 0.06 + Math.sin(f / 9) * 3, opacity: think, overflow: "visible", transform: flip ? "scaleX(-1)" : undefined }}>
          <circle cx={14} cy={104} r={7} fill="#fff" /><circle cx={34} cy={82} r={11} fill="#fff" />
          <circle cx={92} cy={46} r={42} fill="#fff" stroke={C.purple} strokeWidth={5} />
          <text x={92} y={66} textAnchor="middle" fontFamily="Nunito, sans-serif" fontWeight={900} fontSize={58} fill={C.purple} transform={flip ? "translate(184 0) scale(-1 1)" : undefined}>?</text>
        </svg>
      )}
    </div>
  );
};
