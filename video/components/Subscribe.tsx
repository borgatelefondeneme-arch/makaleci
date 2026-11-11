import React from "react";
import { interpolate } from "remotion";
import { C, F } from "../theme";
import { clamp, pop } from "../anim";

const Bell: React.FC<{ size: number; frame: number; ring: number }> = ({ size, frame, ring }) => (
  <svg width={size} height={size} viewBox="-32 -32 64 64" style={{ transform: `rotate(${Math.sin(frame / 2.2) * 16 * ring}deg)`, transformOrigin: "50% 15%" }}>
    <path d="M -18 14 Q -18 -20 0 -22 Q 18 -20 18 14 L 24 20 L -24 20 Z" fill={C.gold} stroke={C.text} strokeWidth={4} strokeLinejoin="round" />
    <circle cy={25} r={6} fill={C.gold} stroke={C.text} strokeWidth={4} /><circle cy={-24} r={4} fill={C.text} />
  </svg>
);

// Abone ol düğmesi: start+press karesinde "tıklanır", ABONE OL → ABONE OLUNDU olur.
export const SubscribeButton: React.FC<{ frame: number; press: number; scale?: number }> = ({ frame, press, scale = 1 }) => {
  const done = frame >= press + 4;
  const squish = 1 - 0.1 * interpolate(frame, [press, press + 4, press + 10], [0, 1, 0], clamp);
  const ring = interpolate(frame, [press + 6, press + 12, press + 40], [0, 1, 0], clamp);
  // imleç
  const cx = interpolate(frame, [press - 22, press], [150, 20], clamp), cy = interpolate(frame, [press - 22, press], [110, 18], clamp);
  return (
    <div style={{ position: "relative", display: "flex", alignItems: "center", gap: 22 * scale, transform: `scale(${scale})`, transformOrigin: "left center" }}>
      <div style={{
        background: done ? C.text : C.coral, color: "#fff", fontFamily: F.head, fontWeight: 900, fontSize: 38, padding: "16px 40px", borderRadius: 60,
        transform: `scale(${squish})`, boxShadow: done ? "none" : "0 10px 30px rgba(255,107,107,0.45)", whiteSpace: "nowrap",
      }}>{done ? "ABONE OLUNDU ✓" : "ABONE OL"}</div>
      <Bell size={66} frame={frame} ring={ring} />
      <svg width={54} height={54} viewBox="0 0 24 24" style={{ position: "absolute", left: 150 + cx, top: 22 + cy, opacity: interpolate(frame, [press - 24, press - 18, press + 14, press + 22], [0, 1, 1, 0], clamp) }}>
        <path d="M4 2 L4 19 L8.5 15 L11.5 22 L14.5 20.7 L11.6 14 L18 14 Z" fill={C.text} stroke="#fff" strokeWidth={1.5} strokeLinejoin="round" />
      </svg>
    </div>
  );
};

// Videonun ~%60'ında alttan kayarak gelen kısa hatırlatma bandı.
export const SubscribeReminder: React.FC<{ frame: number; dur: number }> = ({ frame, dur }) => {
  const inP = pop(frame, 0, 13);
  const out = interpolate(frame, [dur - 14, dur], [0, 1], clamp);
  const y = (1 - inP) * 260 + out * 260;
  return (
    <div style={{ position: "absolute", left: 220, bottom: 172, transform: `translateY(${y}px)`, background: C.card, border: `4px solid ${C.coral}`, borderRadius: 44, padding: "14px 36px 14px 32px", display: "flex", alignItems: "center", gap: 30, boxShadow: "0 20px 60px rgba(0,0,0,0.45)" }}>
      <div>
        <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 32, color: C.text }}>Bu videoyu sevdin mi?</div>
        <div style={{ fontFamily: F.body, fontSize: 26, color: C.dim }}>Her gün yeni bir keşif için takip et!</div>
      </div>
      <SubscribeButton frame={frame} press={Math.round(dur * 0.45)} scale={0.85} />
    </div>
  );
};
