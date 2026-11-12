import React from "react";
import { interpolate } from "remotion";
import { ACCENTS, C, F, GRADIENT, H, W } from "../theme";
import { clamp, pop } from "../anim";

// Sahnelerin "boşta" bile canlı kalmasını sağlayan ortak hareket öğeleri.
export const activeIndex = (beats: number[], frame: number) => { let k = 0; for (let i = 0; i < beats.length; i++) if (beats[i] <= frame) k = i; return k; };
// Vuruş anında kısa zıplama (0..1..0): cümle başında öğeyi öne çıkarır.
export const kick = (frame: number, at: number, len = 14) => { const t = (frame - at) / len; return t < 0 || t > 1 ? 0 : Math.sin(t * Math.PI); };

// Kenarlarda süzülen konu simgeleri: sırayla belirir, her cümle başında biri zıplar.
const SLOTS = [[70, 210], [1765, 250], [90, 560], [1750, 600], [150, 820], [1700, 830]];
export const Stickers: React.FC<{ items: string[]; frame: number; beats: number[]; avoid?: { x: number; y: number } }> = ({ items, frame, beats, avoid }) => {
  // Muma'nın kafasının durduğu köşeye yakın yerler boş bırakılır.
  const slots = SLOTS.filter(([x, y]) => !avoid || Math.hypot(x + 43 - avoid.x, y + 43 - avoid.y) > 300);
  return (
  <>
    {items.slice(0, slots.length).map((e, i) => {
      const [x, y] = slots[i];
      const p = pop(frame, 6 + i * 9, 8);
      const jump = beats.reduce((a, b, k) => a + (k % items.length === i ? kick(frame, b, 18) : 0), 0);
      return (
        <div key={i} style={{
          position: "absolute", left: x, top: y + Math.sin(frame / (17 + i * 3) + i * 2) * 16 - jump * 46, fontSize: 86, lineHeight: 1, fontFamily: F.head, opacity: p * 0.95,
          transform: `scale(${p * (1 + jump * 0.25)}) rotate(${Math.sin(frame / (23 + i * 4) + i) * 11 + jump * (i % 2 ? 14 : -14)}deg)`, filter: "drop-shadow(0 10px 14px rgba(27,34,56,0.14))",
        }}>{e}</div>
      );
    })}
  </>
  );
};

// Her cümlede beliren büyük anahtar kelime (içerik ile altyazı arasında).
export const Keyword: React.FC<{ words: string[]; beats: number[]; ends: number[]; frame: number; variant?: number }> = ({ words, beats, ends, frame, variant = 0 }) => {
  const k = activeIndex(beats, frame);
  const w = words[k];
  if (!w || frame < beats[k]) return null;
  const p = pop(frame, beats[k] + 3, 9);
  const out = interpolate(frame, [ends[k] - 2, ends[k] + 8], [1, 0], clamp);
  return (
    <div style={{ position: "absolute", left: 0, width: W, bottom: 146, display: "flex", justifyContent: "center", opacity: Math.min(1, p * 2) * out }}>
      {variant === 1 ? (
        // beyaz kart + renkli şerit: soldan kayarak gelir
        <div style={{ background: "#fff", color: C.text, borderLeft: `14px solid ${C.yellow}`, fontFamily: F.head, fontWeight: 800, fontSize: 46, letterSpacing: 1, padding: "10px 38px 10px 28px", borderRadius: 18, boxShadow: `0 14px 34px ${C.shadow}`, transform: `translateX(${(1 - p) * -80}px) scale(${0.9 + 0.1 * p})` }}>{w}</div>
      ) : variant === 2 ? (
        // lacivert eğik etiket: yukarıdan düşer
        <div style={{ background: C.text, color: "#fff", fontFamily: F.head, fontWeight: 800, fontSize: 46, letterSpacing: 2, padding: "10px 40px", borderRadius: 12, boxShadow: `0 14px 34px ${C.shadow}`, borderBottom: `8px solid ${C.gold}`, transform: `translateY(${(1 - p) * -40}px) rotate(${-2 + Math.sin(frame / 22) * 1.2}deg)` }}>{w}</div>
      ) : (
        <div style={{ backgroundImage: GRADIENT, color: "#fff", fontFamily: F.head, fontWeight: 800, fontSize: 46, letterSpacing: 1, padding: "10px 40px", borderRadius: 60, boxShadow: `0 14px 34px ${C.shadow}`, transform: `scale(${0.6 + 0.4 * p}) rotate(${(1 - p) * -5 + Math.sin(frame / 20) * 1.2}deg)` }}>{w}</div>
      )}
    </div>
  );
};

// Soru sahnelerinde uçuşan soru işaretleri.
export const QuestionMarks: React.FC<{ frame: number }> = ({ frame }) => (
  <>
    {Array.from({ length: 9 }, (_, i) => {
      const r = (n: number) => { const x = Math.sin(i * 71.3 + n * 19.9) * 43758.5453; return x - Math.floor(x); };
      const y = H - ((frame * (1.2 + r(1) * 1.6) + r(2) * H) % (H + 200)) + 60;
      return <div key={i} style={{ position: "absolute", left: 80 + r(3) * (W - 240) + Math.sin(frame / 30 + i) * 30, top: y, fontFamily: F.head, fontWeight: 800, fontSize: 70 + r(4) * 90, color: ACCENTS[i % 4], opacity: 0.16, transform: `rotate(${Math.sin(frame / 25 + i) * 20}deg)` }}>?</div>;
    })}
  </>
);
