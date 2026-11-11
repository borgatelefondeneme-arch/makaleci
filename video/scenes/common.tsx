import React from "react";
import type { EpisodeProps, Visual } from "../../schemas/index";
import { C, F, SAFE } from "../theme";
import { pop } from "../anim";

export type SceneProps<T extends Visual["type"]> = {
  visual: Extract<Visual, { type: T }>;
  beats: number[]; // satır başlangıç kareleri (sahneye göre)
  dur: number; // sahne süresi (kare)
  frame: number; // sahneye göre kare
  data: EpisodeProps;
  tail: number; // sahne sonunda sessiz kuyruk (yalnızca outro)
};

// Sahne içerik alanı: altyazı bandının üstünde kalır.
export const Stage: React.FC<{ children: React.ReactNode; style?: React.CSSProperties }> = ({ children, style }) => (
  <div style={{ position: "absolute", left: SAFE.left, right: SAFE.right, top: SAFE.top, bottom: SAFE.bottom, display: "flex", flexDirection: "column", justifyContent: "center", ...style }}>
    {children}
  </div>
);

export const Title: React.FC<{ frame: number; children: React.ReactNode; color?: string }> = ({ frame, children, color = C.teal }) => {
  const p = pop(frame, 2);
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 20, opacity: p, transform: `translateX(${(1 - p) * -40}px)`, marginBottom: 36 }}>
      <div style={{ width: 14, height: 58, borderRadius: 7, background: color }} />
      <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 56, color: C.text, lineHeight: 1.1 }}>{children}</div>
    </div>
  );
};

export const Card: React.FC<{ children: React.ReactNode; style?: React.CSSProperties; accent?: string }> = ({ children, style, accent }) => (
  <div style={{
    background: C.card, border: `3px solid ${accent ?? C.cardLine}`, borderRadius: 36, padding: "36px 44px",
    boxShadow: `0 16px 44px ${C.shadow}`, ...style,
  }}>{children}</div>
);
