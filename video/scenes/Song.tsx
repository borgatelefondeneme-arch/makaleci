import React from "react";
import { interpolate } from "remotion";
import { ACCENTS, C, F, GRADIENT, H, W } from "../theme";
import { clamp, pop } from "../anim";
import { SceneProps } from "./common";

// Kapanış şarkısı — klip havasında: kelime kelime yanan sözler, vuruşla zıplayan konu rozetleri,
// dönen ışın demeti ve ekolayzır. Muma bu sahnede yoktur; sahnedekiler konunun kendi karakterleridir.
// 7–14 yaşa göre: kollu bacaklı bebeksi figürler yerine rozet/sahne dili kullanılır.
const BEAT = 15; // 120 BPM ≈ 15 karede bir vuruş
const rnd = (i: number, n: number) => { const x = Math.sin(i * 91.7 + n * 47.3) * 43758.5453; return x - Math.floor(x); };

const Badge: React.FC<{ emoji: string; name: string; i: number; n: number; t: number; chorus: boolean; amp: number; enter: number }> = ({ emoji, name, i, n, t, chorus, amp, enter }) => {
  const size = n > 4 ? 200 : 230;
  const col = ACCENTS[i % 4];
  const ph = (t - i * 3) / BEAT; // dalga: soldan sağa gecikmeli
  const hop = Math.pow(Math.abs(Math.sin(Math.PI * ph)), 1.6) * (chorus ? 110 : 46) * (0.75 + amp * 0.45);
  const tilt = Math.sin((Math.PI * ph) / 2) * (chorus ? 12 : 6);
  const pulse = (t / BEAT) % 1; // vuruşla genişleyen halka
  return (
    <div style={{ position: "relative", width: size, height: size + 70, opacity: Math.min(1, enter * 3), transform: `translateY(${(1 - enter) * 300 - hop}px)` }}>
      <div style={{ position: "absolute", left: size * 0.15, top: size + 6 + hop, width: size * 0.7, height: 20, borderRadius: "50%", background: C.text, opacity: 0.12 * (1 - hop / 260) }} />
      <div style={{ position: "absolute", left: 0, top: 0, width: size, height: size, borderRadius: "50%", border: `6px solid ${col}`, opacity: (1 - pulse) * 0.5, transform: `scale(${1 + pulse * 0.45})` }} />
      <div style={{
        position: "absolute", left: 0, top: 0, width: size, height: size, borderRadius: "50%", background: "#fff", border: `10px solid ${col}`, boxSizing: "border-box",
        boxShadow: `0 18px 40px ${C.shadow}, inset 0 -14px 0 rgba(27,34,56,0.05)`, display: "flex", alignItems: "center", justifyContent: "center",
        transform: `rotate(${tilt + (chorus ? Math.sin((Math.PI * ph) / 4) * 10 : 0)}deg) scale(${1 + (chorus ? 0.06 * Math.abs(Math.sin(Math.PI * ph)) : 0)})`,
      }}>
        <div style={{ fontSize: size * 0.52, lineHeight: 1, fontFamily: F.head, transform: `scale(${1 + amp * 0.1})` }}>{emoji}</div>
      </div>
      <div style={{ position: "absolute", left: -40, width: size + 80, top: size + 30 + hop, textAlign: "center", fontFamily: F.head, fontWeight: 800, fontSize: 28, color: col }}>{name}</div>
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
  const on = interpolate(t, [-6, 14], [0, 1], clamp);
  return (
    <div style={{ position: "absolute", inset: 0, opacity: out }}>
      {/* sahne: renkli zemin şeridi ve dönen ışın demeti */}
      <div style={{ position: "absolute", left: -100, right: -100, bottom: -80, height: 430, background: "linear-gradient(100deg, #FFD9BF, #FFE9B8 35%, #CFE0FF 70%, #E3DBFF)", borderRadius: "50% 50% 0 0 / 34% 34% 0 0", opacity: on * 0.95, transform: `translateY(${(1 - on) * 200}px)` }} />
      <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0, opacity: on * (chorus ? 0.5 : 0.22) }}>
        <g transform={`translate(${W / 2} ${H * 0.74}) rotate(${t * (chorus ? 0.9 : 0.35)})`}>
          {Array.from({ length: 12 }, (_, i) => <path key={i} d="M 0 0 L -70 -1300 L 70 -1300 Z" fill={ACCENTS[i % 4]} opacity={0.2} transform={`rotate(${i * 30})`} />)}
        </g>
      </svg>
      {/* konfeti: yalnızca nakaratta */}
      {started && chorus && Array.from({ length: 26 }, (_, i) => {
        const y = ((t * (3 + rnd(i, 1) * 4) + rnd(i, 2) * H) % (H + 80)) - 40;
        return <div key={i} style={{ position: "absolute", left: rnd(i, 3) * W, top: y, width: 14 + rnd(i, 4) * 12, height: 8 + rnd(i, 5) * 8, borderRadius: 3, background: [C.yellow, C.teal, C.purple, C.gold, C.green][i % 5], opacity: 0.8, transform: `rotate(${t * (3 + rnd(i, 6) * 5) + i * 40}deg)` }} />;
      })}
      {/* başlık */}
      <div style={{ position: "absolute", left: 0, right: 0, top: 74, display: "flex", justifyContent: "center", alignItems: "center", gap: 20, opacity: titleP, transform: `translateY(${(1 - titleP) * -30}px)` }}>
        <div style={{ fontSize: 50, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 8) * 12}deg) scale(${1 + beat * 0.15})` }}>🎧</div>
        <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 44, color: C.text }}>{sg.title}</div>
        {started && <div style={{ background: chorus ? C.yellow : C.teal, color: "#fff", fontFamily: F.head, fontWeight: 800, fontSize: 26, padding: "8px 24px", borderRadius: 40, transform: `scale(${0.85 + 0.15 * secIn})` }}>{sec.label}</div>}
      </div>
      {/* sözler: o anki dize kelime kelime yanar */}
      <div style={{ position: "absolute", left: 120, right: 120, top: 168, display: "flex", flexDirection: "column", alignItems: "center", gap: chorus ? 10 : 6, opacity: started ? secIn : 0, transform: `translateY(${(1 - secIn) * 40}px)` }}>
        {(started ? sec.lines : []).map((l, i) => {
          const cur = abs >= l.startFrame && abs < l.endFrame;
          const done = abs >= l.endFrame;
          const words = l.text.split(" ");
          const prog = interpolate(abs, [l.startFrame, l.endFrame - 4], [0, words.length], clamp);
          return (
            <div key={`${sec.startFrame}-${i}`} style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "0 0.28em", fontFamily: F.head, fontWeight: 800, fontSize: chorus ? (cur ? 88 : 60) : cur ? 70 : 48, lineHeight: 1.16, opacity: cur ? 1 : done ? 0.38 : 0.6, transform: `scale(${cur ? 1 + beat * 0.02 : 1})` }}>
              {words.map((w, k) => {
                const lit = cur && k < prog;
                const p = cur ? interpolate(prog, [k, k + 0.6], [0, 1], clamp) : 0;
                return <span key={k} style={{ display: "inline-block", color: C.text, transform: `translateY(${lit ? -6 * Math.sin(p * Math.PI) : 0}px) scale(${1 + (lit ? 0.08 * Math.sin(p * Math.PI) : 0)})`, ...(lit ? { backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" } : {}) }}>{w}</span>;
              })}
            </div>
          );
        })}
      </div>
      {/* ekolayzır */}
      <svg width={W} height={170} style={{ position: "absolute", left: 0, bottom: 0, opacity: on * 0.9 }}>
        {Array.from({ length: 64 }, (_, i) => {
          const h = 8 + (0.2 + amp * 0.8) * (26 + 110 * Math.abs(Math.sin(t / (5 + (i % 5)) + i * 1.7)));
          return <rect key={i} x={i * 30 + 6} y={170 - h} width={18} height={h} rx={8} fill={ACCENTS[i % 4]} opacity={0.55} />;
        })}
      </svg>
      {/* konu karakterleri: rozetler vuruşla dalga dalga zıplar */}
      <div style={{ position: "absolute", left: 0, right: 0, bottom: 150, display: "flex", justifyContent: "center", alignItems: "flex-end", gap: cast.length > 4 ? 76 : 110 }}>
        {cast.map((c, i) => <Badge key={i} emoji={c.emoji} name={c.name} i={i} n={cast.length} t={t} chorus={chorus} amp={amp} enter={pop(t, 2 + i * 7, 9)} />)}
      </div>
    </div>
  );
};
