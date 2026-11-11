import React from "react";
import { interpolate } from "remotion";
import { ACCENTS, C, F, H, W } from "../theme";
import { clamp, pop } from "../anim";
import { SceneProps } from "./common";

// Kapanış şarkısı: sözler dize dize belirir, konuya özel karakterler ritimle dans eder.
// Muma bu sahnede görünmez. Zamanlama voice.song'dan gelir (bölüm zaman çizelgesinde kare).
const DECOR = ["🎵", "🎶", "✨", "🎵", "🎶", "✨", "🎵", "🎶"];
const rnd = (i: number, n: number) => { const x = Math.sin(i * 91.7 + n * 47.3) * 43758.5453; return x - Math.floor(x); };
const BEAT = 15; // 120 BPM ≈ 15 karede bir vuruş

// Emoji gövdeli, kollu bacaklı dansçı. Her biri farklı fazda ve farklı figürle oynar.
const Dancer: React.FC<{ emoji: string; name: string; i: number; n: number; t: number; chorus: boolean; amp: number; enter: number }> = ({ emoji, name, i, n, t, chorus, amp, enter }) => {
  const size = n > 4 ? 190 : 220;
  const ph = (t + i * 5) / BEAT;
  const hop = Math.abs(Math.sin(Math.PI * ph)) * (chorus ? 92 : 44) * (0.7 + amp * 0.5);
  const sway = Math.sin((Math.PI * ph) / 2) * (chorus ? 15 : 9);
  const squash = 1 + Math.cos(2 * Math.PI * ph) * 0.07;
  const spin = chorus && i % 2 === 0 ? Math.sin((Math.PI * ph) / 4) * 14 : 0;
  const side = Math.sin((Math.PI * ph) / 2 + i) * 26; // sağa sola adım
  const arm = Math.sin(Math.PI * ph + i) * 46; // kol sallama
  const leg = Math.sin(Math.PI * ph) * 16;
  const col = ACCENTS[i % 4];
  const drop = (1 - enter) * -520; // yukarıdan zıplayarak gelir
  return (
    <div style={{ position: "relative", width: size, height: size + 120, transform: `translate(${side}px, ${drop - hop}px)`, opacity: Math.min(1, enter * 4) }}>
      {/* gölge */}
      <div style={{ position: "absolute", left: size * 0.2, top: size + 78 + hop - drop, width: size * 0.6, height: 18, borderRadius: "50%", background: "#000", opacity: 0.25 * enter * (1 - hop / 220) }} />
      <svg width={size} height={size + 120} style={{ position: "absolute", left: 0, top: 0, overflow: "visible", transform: `rotate(${sway + spin}deg)`, transformOrigin: `50% ${size * 0.6}px` }}>
        {/* bacaklar ve ayakkabılar */}
        {[-1, 1].map((d) => (
          <g key={d}>
            <line x1={size / 2 + d * size * 0.16} y1={size * 0.82} x2={size / 2 + d * (size * 0.2 + leg * d)} y2={size + 58 - Math.max(0, leg * d)} stroke={C.text} strokeWidth={9} strokeLinecap="round" />
            <ellipse cx={size / 2 + d * (size * 0.2 + leg * d) + d * 12} cy={size + 64 - Math.max(0, leg * d)} rx={24} ry={13} fill={col} stroke={C.ink} strokeWidth={4} />
          </g>
        ))}
        {/* kollar ve eldivenler */}
        {[-1, 1].map((d) => {
          const hx = size / 2 + d * (size * 0.62), hy = size * 0.5 - (d === 1 ? arm : -arm) - (chorus ? 40 : 0);
          return (
            <g key={d}>
              <path d={`M ${size / 2 + d * size * 0.38} ${size * 0.55} Q ${size / 2 + d * size * 0.55} ${size * 0.62} ${hx} ${hy}`} fill="none" stroke={C.text} strokeWidth={9} strokeLinecap="round" />
              <circle cx={hx} cy={hy} r={17} fill="#fff" stroke={C.ink} strokeWidth={4} />
            </g>
          );
        })}
      </svg>
      <div style={{ position: "absolute", left: 0, top: 0, width: size, height: size, fontSize: size * 0.86, lineHeight: `${size}px`, textAlign: "center", fontFamily: F.head, transform: `rotate(${sway + spin}deg) scale(${squash}, ${2 - squash})`, transformOrigin: "50% 60%" }}>{emoji}</div>
      <div style={{ position: "absolute", left: -30, width: size + 60, top: size + 86 + hop - drop, textAlign: "center", fontFamily: F.head, fontWeight: 800, fontSize: 26, color: col, opacity: enter }}>{name}</div>
    </div>
  );
};

export const Song: React.FC<SceneProps<"song">> = ({ frame, data }) => {
  const sg = data.voice.song;
  const scene = data.voice.scenes.find((s) => s.sceneId === sg?.sceneId);
  if (!sg || !scene) return null;
  const abs = scene.startFrame + frame; // bölüm karesi
  const t = abs - sg.startFrame; // şarkının içindeki kare
  const amp = data.voice.amplitude[Math.max(0, abs)] ?? 0;
  const started = t >= -6;
  const sec = sg.sections.find((s) => abs >= s.startFrame && abs < s.endFrame) ?? (t < 0 ? sg.sections[0] : sg.sections[sg.sections.length - 1]);
  const chorus = /nakarat/i.test(sec.label);
  const secIn = pop(abs, sec.startFrame, 12);
  const beat = Math.abs(Math.sin((Math.PI * t) / BEAT));
  const titleP = pop(frame, 4, 9);
  const out = interpolate(abs, [sg.endFrame - 14, sg.endFrame + 4], [1, 0], clamp);
  const cast = sg.cast;
  return (
    <div style={{ position: "absolute", inset: 0, opacity: out }}>
      {/* sahne ışıkları: nakaratta güçlenir */}
      <div style={{ position: "absolute", inset: 0, background: `radial-gradient(ellipse at 50% 78%, ${chorus ? C.yellow : C.purple}, transparent 60%)`, opacity: started ? 0.12 + amp * 0.12 + (chorus ? 0.1 : 0) : 0 }} />
      {started && [0, 1, 2].map((k) => (
        <div key={k} style={{ position: "absolute", left: 260 + k * 560, top: -80, width: 260, height: 900, background: `linear-gradient(${ACCENTS[(k + Math.floor(t / 60)) % 4]}, transparent)`, opacity: 0.1 + (chorus ? 0.08 : 0), transform: `rotate(${Math.sin(t / 34 + k * 2) * 16}deg)`, transformOrigin: "50% 0", clipPath: "polygon(38% 0, 62% 0, 100% 100%, 0 100%)" }} />
      ))}
      {/* uçuşan notalar */}
      {started && DECOR.map((n, i) => {
        const speed = 2.2 + rnd(i, 1) * 2.4;
        const y = H + 60 - (((t + 40) * speed + rnd(i, 2) * H * 1.3) % (H + 220));
        const x = 40 + rnd(i, 3) * (W - 160) + Math.sin(t / 22 + i) * 46;
        return <div key={i} style={{ position: "absolute", left: x, top: y, fontSize: 40 + rnd(i, 4) * 36, fontFamily: F.head, opacity: 0.4, transform: `rotate(${Math.sin(t / 14 + i) * 18}deg) scale(${1 + beat * 0.12})` }}>{n}</div>;
      })}
      {/* başlık */}
      <div style={{ position: "absolute", left: 110, top: 86, display: "flex", alignItems: "center", gap: 22, opacity: titleP, transform: `translateY(${(1 - titleP) * -30}px)` }}>
        <div style={{ fontSize: 64, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 8) * 12}deg) scale(${1 + beat * 0.15})` }}>🎤</div>
        <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 56, color: C.text }}>{sg.title}</div>
        {started && <div style={{ marginLeft: 12, background: chorus ? C.yellow : C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 28, padding: "8px 26px", borderRadius: 40, transform: `scale(${0.85 + 0.15 * secIn})` }}>{sec.label}</div>}
      </div>
      {/* sözler: ekranın üst yarısında, ortalı */}
      <div style={{ position: "absolute", left: 110, right: 110, top: 190, display: "flex", flexDirection: "column", alignItems: "center", gap: chorus ? 12 : 8, opacity: started ? secIn : 0, transform: `translateY(${(1 - secIn) * 40}px)` }}>
        {(started ? sec.lines : []).map((l, i) => {
          const on = abs >= l.startFrame && abs < l.endFrame;
          const done = abs >= l.endFrame;
          return (
            <div key={`${sec.startFrame}-${i}`} style={{
              fontFamily: F.head, fontWeight: 900, fontSize: chorus ? 72 : 54, lineHeight: 1.14, textAlign: "center",
              color: on ? C.yellow : done ? C.dim : C.text, opacity: on ? 1 : done ? 0.5 : 0.78,
              transform: `scale(${on ? 1.06 + beat * 0.03 : 1})`, textShadow: on ? "0 6px 30px rgba(255,210,63,0.4)" : "none",
            }}>{l.text}</div>
          );
        })}
      </div>
      {/* dans pisti: konuya özel karakterler */}
      <div style={{ position: "absolute", left: 0, right: 0, bottom: 86, display: "flex", justifyContent: "center", alignItems: "flex-end", gap: cast.length > 4 ? 90 : 130 }}>
        {cast.map((c, i) => <Dancer key={i} emoji={c.emoji} name={c.name} i={i} n={cast.length} t={t} chorus={chorus} amp={amp} enter={pop(t, 4 + i * 9, 9)} />)}
      </div>
    </div>
  );
};
