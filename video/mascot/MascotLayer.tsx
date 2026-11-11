import React from "react";
import { Easing, interpolate, spring, useCurrentFrame } from "remotion";
import type { MascotCue } from "../../schemas/index";
import { clamp } from "../anim";
import { FPS, W, H } from "../theme";
import { ASPECT, HEAD, Mascot, MumaHead, type MouthShape, type Pose } from "./Mascot";

export type CueAt = { startFrame: number; cue: MascotCue };
// Muma yalnızca girişte ve çıkışta görünür (kullanıcı kararı). Her "ziyaret" uçarak gelip uçarak gitmektir.
export type Visit = { start: number; end: number; outFrames: number };
type Word = { text: string; start: number; end: number };
const BASE = 540; // scale=1 iken yükseklik (px)
const FLY_IN = 42;
const mix = (a: number, b: number, t: number) => a + (b - a) * t;
const poseOf = (c: MascotCue): Pose => c.pose ?? (c.state === "talk" || c.state === "point" ? "point" : "crossed");
const flipOf = (c: MascotCue) => (c.pointAt ? c.pointAt.x < c.x : c.x > 0.5);

// Ağız biçimi: o an söylenen kelimenin ünlüsüne göre (a/e açık, ı/i yayvan, o/ö/u/ü yuvarlak; m/b/p kapalı).
const VIS: Record<string, MouthShape> = {
  a: { wide: 1, open: 1, round: 0 }, e: { wide: 1.08, open: 0.8, round: 0 }, "ı": { wide: 1.12, open: 0.5, round: 0 }, i: { wide: 1.15, open: 0.45, round: 0 },
  o: { wide: 0.68, open: 0.95, round: 1 }, "ö": { wide: 0.66, open: 0.85, round: 1 }, u: { wide: 0.55, open: 0.6, round: 1 }, "ü": { wide: 0.55, open: 0.55, round: 1 },
};
const REST: MouthShape = { wide: 1, open: 0, round: 0 };
const shapeAt = (words: Word[], t: number): MouthShape => {
  const w = words.find((x) => t >= x.start && t <= x.end);
  if (!w) return REST;
  const s = w.text.toLocaleLowerCase("tr").replace(/[^a-zçğıöşü]/g, "");
  if (!s) return REST;
  const k = Math.min(s.length - 1, Math.floor(((t - w.start) / Math.max(0.01, w.end - w.start)) * s.length));
  if ("mbp".includes(s[k])) return { wide: 1, open: 0.06, round: 0 };
  for (let d = 0; d < s.length; d++) { const v = VIS[s[k - d]] ?? VIS[s[k + d]]; if (v) return v; }
  return { wide: 1, open: 0.7, round: 0 };
};

export const MascotLayer: React.FC<{ cues: CueAt[]; visits: Visit[]; amplitude: number[]; words: Word[] }> = ({ cues, visits, amplitude, words }) => {
  const f = useCurrentFrame();
  const visit = visits.find((v) => f >= v.start && f <= v.end);
  if (!visit) return null;
  let i = 0;
  for (let k = 0; k < cues.length; k++) if (cues[k].startFrame <= f) i = k;
  const cur = cues[i].cue;
  // Ziyaretin ilk işareti için geçiş yok; aynı ziyaret içindeki sonraki işaretlere yaylı geçilir.
  const first = cues[i].startFrame <= visit.start + 2 || i === 0;
  const prev = first ? cur : cues[i - 1].cue;
  const since = f - cues[i].startFrame;
  const t = first ? 1 : spring({ frame: since, fps: FPS, config: { damping: 18, mass: 0.9 } });

  const scale = mix(prev.scale, cur.scale, t);
  const size = BASE * scale, width = size * ASPECT;
  const cx = mix(prev.x, cur.x, t) * W, cy = mix(prev.y, cur.y, t) * H;
  const left = Math.min(W - width - 10, Math.max(10, cx - width / 2));
  const top = Math.min(H - 150 - size, Math.max(70, cy - size / 2));
  const think = mix(prev.state === "think" ? 1 : 0, cur.state === "think" ? 1 : 0, t);
  const blend = first ? 1 : interpolate(since, [2, 12], [0, 1], clamp);
  const lean = cur.state === "point" && cur.pointAt ? (flipOf(cur) ? -4 : 4) * Math.min(1, t) : 0;
  const hop = Math.sin(Math.min(1, Math.max(0, t)) * Math.PI) * (first ? 0 : 22);

  // Ağız: genlik (yumuşatılmış) × ünlü biçimi; komşu karelerle ortalanarak titreme önlenir.
  const amp = (k: number) => amplitude[Math.max(0, k)] ?? 0;
  const level = Math.min(1, (amp(f - 1) + 2 * amp(f) + amp(f + 1)) / 4 * 1.15);
  const sh = [-1, 0, 1].map((d) => shapeAt(words, (f + d) / FPS));
  const shape: MouthShape = { wide: (sh[0].wide + 2 * sh[1].wide + sh[2].wide) / 4, open: ((sh[0].open + 2 * sh[1].open + sh[2].open) / 4) * (0.35 + 0.65 * level), round: (sh[0].round + 2 * sh[1].round + sh[2].round) / 4 };
  const speaking = cur.state !== "idle" && level > 0.05;

  // Uçuş: ekranın yakın kenarından süzülerek gelir, sağ üste doğru uçup gider.
  const fromRight = cur.x > 0.5;
  const outAt = visit.end - visit.outFrames;
  const path = (ff: number) => {
    const ti = interpolate(ff, [visit.start, visit.start + FLY_IN], [0, 1], { ...clamp, easing: Easing.out(Easing.back(1.4)) });
    const to = interpolate(ff, [outAt, visit.end], [0, 1], { ...clamp, easing: Easing.in(Easing.cubic) });
    const inX = fromRight ? W - left + 80 : -(left + width + 80);
    return { ti, to, x: (1 - ti) * inX + to * (W - left + 120), y: (1 - ti) * -(top + 60) * 0.7 - Math.sin(Math.min(1, ti) * Math.PI) * 60 + to * -(top + size * 0.6) };
  };
  const fly = path(f);
  const fscale = (0.55 + 0.45 * Math.min(1, fly.ti)) * (1 - 0.45 * fly.to);
  const frot = (1 - Math.min(1, fly.ti)) * (fromRight ? -22 : 22) + fly.to * 26;
  const inAir = f < visit.start + FLY_IN + 6 || f > outAt;
  let pose = poseOf(cur), prevPose = poseOf(prev), pblend = blend;
  if (f < visit.start + FLY_IN + 8) { prevPose = "fly"; pblend = interpolate(f, [visit.start + FLY_IN - 10, visit.start + FLY_IN + 6], [0, 1], clamp); }
  else if (f > outAt - 10) { prevPose = poseOf(cur); pose = "fly"; pblend = interpolate(f, [outAt - 10, outAt + 4], [0, 1], clamp); }
  const trail = inAir ? [1, 2, 3, 4, 5].map((k) => ({ ...path(f - k * 3.2), k })) : [];
  return (
    <>
      {trail.map((p) => (
        <div key={p.k} style={{ position: "absolute", left: left + width / 2 + p.x - 14 + Math.sin(f / 3 + p.k) * 18, top: top + size * 0.72 + p.y + Math.cos(f / 4 + p.k * 2) * 14, width: 28 - p.k * 3, height: 28 - p.k * 3, borderRadius: "50%", background: p.k % 2 ? "#FFE9A8" : "#BFD4FF", opacity: (0.55 - p.k * 0.09) * (f < outAt ? 1 - fly.ti * 0.6 : 1) }} />
      ))}
      <div style={{ position: "absolute", left: left + fly.x, top: top - hop + fly.y, width, height: size, transform: `rotate(${frot}deg) scale(${fscale})`, transformOrigin: "50% 40%" }}>
        <Mascot frame={f} mouth={speaking ? level : 0} shape={shape} pose={pose} prevPose={prevPose} blend={pblend} flip={flipOf(cur)} think={think} lean={lean} size={size} />
      </div>
    </>
  );
};

// ---------- Anlatım sahnelerinde köşede gezen kafa ----------
// Muma'nın bütün gövdesi yalnızca girişte ve çıkışta görünür; aradaki sahnelerde yalnızca kafası,
// sahneden sahneye köşe değiştirerek ekranda kalır ve anlatımı sese göre "söyler".
export type Corner = "br" | "tr" | "tl";
export const HEAD_SIZE = 250;
const HEAD_H = (HEAD.h * HEAD_SIZE) / HEAD.w;
export const CORNERS: Record<Corner, { left: number; top: number }> = { br: { left: 1640, top: 715 }, tr: { left: 1640, top: 78 }, tl: { left: 30, top: 78 } };
export const cornerCenter = (c: Corner) => ({ x: CORNERS[c].left + HEAD_SIZE / 2, y: CORNERS[c].top + HEAD_H / 2 });
const PATTERN: Corner[] = ["br", "br", "tl", "br", "tr", "br", "tl", "tr"];
export const cornerOf = (sceneIndex: number): Corner => PATTERN[sceneIndex % PATTERN.length];

export const HeadLayer: React.FC<{ scenes: { startFrame: number; corner: Corner }[]; from: number; to: number; amplitude: number[]; words: Word[] }> = ({ scenes, from, to, amplitude, words }) => {
  const f = useCurrentFrame();
  if (f < from - 4 || f > to + 14 || !scenes.length) return null;
  let i = 0;
  for (let k = 0; k < scenes.length; k++) if (scenes[k].startFrame <= f) i = k;
  const cur = CORNERS[scenes[i].corner], prev = CORNERS[scenes[Math.max(0, i - 1)].corner];
  const since = f - scenes[i].startFrame;
  const t = i === 0 ? 1 : spring({ frame: since, fps: FPS, config: { damping: 16, mass: 0.9 } });
  const moving = prev !== cur && t < 0.98;
  const left = mix(prev.left, cur.left, t), top = mix(prev.top, cur.top, t) - (moving ? Math.sin(Math.min(1, Math.max(0, t)) * Math.PI) * 90 : 0);
  const enter = interpolate(f, [from - 4, from + 14], [0, 1], { ...clamp, easing: Easing.out(Easing.back(1.6)) });
  const exit = interpolate(f, [to - 6, to + 12], [0, 1], clamp);
  const amp = (k: number) => amplitude[Math.max(0, k)] ?? 0;
  const level = Math.min(1, ((amp(f - 1) + 2 * amp(f) + amp(f + 1)) / 4) * 1.15);
  const sh = [-1, 0, 1].map((d) => shapeAt(words, (f + d) / FPS));
  const shape: MouthShape = { wide: (sh[0].wide + 2 * sh[1].wide + sh[2].wide) / 4, open: ((sh[0].open + 2 * sh[1].open + sh[2].open) / 4) * (0.35 + 0.65 * level), round: (sh[0].round + 2 * sh[1].round + sh[2].round) / 4 };
  return (
    <div style={{ position: "absolute", left, top, transform: `scale(${Math.max(0, enter) * (1 - exit)}) rotate(${moving ? (cur.left > prev.left ? 1 : -1) * Math.sin(t * Math.PI) * 14 : 0}deg)`, transformOrigin: "50% 80%" }}>
      <MumaHead frame={f} mouth={level > 0.05 ? level : 0} shape={shape} size={HEAD_SIZE} />
    </div>
  );
};
