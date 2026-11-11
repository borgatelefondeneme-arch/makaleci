import React from "react";
import { Easing, interpolate, spring, useCurrentFrame } from "remotion";
import type { MascotCue } from "../../schemas/index";
import { clamp } from "../anim";
import { FPS, W, H } from "../theme";
import { ASPECT, Mascot, type Pose } from "./Mascot";

export type CueAt = { startFrame: number; cue: MascotCue };
const BASE = 540; // scale=1 iken yükseklik (px)
const mix = (a: number, b: number, t: number) => a + (b - a) * t;
// Durum → poz: konuşma ve işaret "parmak havada + açık el", bekleme ve düşünme "kollar kavuşuk".
const poseOf = (c: MascotCue): Pose => (c.state === "talk" || c.state === "point" ? "point" : "crossed");
// Açık el içeriğe baksın: hedef (ya da ekran ortası) soldaysa görsel çevrilir.
const flipOf = (c: MascotCue) => (c.pointAt ? c.pointAt.x < c.x : c.x > 0.5);

// Bölüm düzeyinde tek karakter: sahne değişince konum/ölçek yaylı geçişle akar, poz çapraz geçer.
const FLY_IN = 42, FLY_OUT = 60; // voice aşamasındaki sabitlerle aynı
// Açılışta ekranın sol üstünden süzülerek gelir, kapanışta sağ üste doğru uçup gider.
export const MascotLayer: React.FC<{ cues: CueAt[]; amplitude: number[]; total: number }> = ({ cues, amplitude, total }) => {
  const f = useCurrentFrame();
  let i = 0;
  for (let k = 0; k < cues.length; k++) if (cues[k].startFrame <= f) i = k;
  const cur = cues[i].cue;
  const prev = cues[Math.max(0, i - 1)].cue;
  const since = f - cues[i].startFrame;
  const t = i === 0 ? 1 : spring({ frame: since, fps: FPS, config: { damping: 18, mass: 0.9 } });

  const scale = mix(prev.scale, cur.scale, t);
  const size = BASE * scale, width = size * ASPECT;
  const cx = mix(prev.x, cur.x, t) * W;
  const cy = mix(prev.y, cur.y, t) * H;
  // Ekran dışına ve altyazı bandına taşmasın.
  const left = Math.min(W - width - 10, Math.max(10, cx - width / 2));
  const top = Math.min(H - 150 - size, Math.max(70, cy - size / 2));
  const think = mix(prev.state === "think" ? 1 : 0, cur.state === "think" ? 1 : 0, t);
  const flip = flipOf(cur), pflip = flipOf(prev);
  // Yön değişiyorsa poz geçişi sırasında bir kez "dönüş" yapılır.
  const blend = i === 0 ? 1 : interpolate(since, [2, 12], [0, 1], clamp);
  const lean = cur.state === "point" && cur.pointAt ? (flip ? -4 : 4) * Math.min(1, t) : 0;
  const raw = amplitude[f] ?? 0;
  const mouth = cur.state === "idle" ? 0 : (raw + (amplitude[f - 1] ?? raw)) / 2;
  const hop = Math.sin(Math.min(1, Math.max(0, t)) * Math.PI) * (i === 0 ? 0 : 22);
  // Uçuş: giriş (0..FLY_IN) ve çıkış (son FLY_OUT kare, kararma öncesi).
  const path = (ff: number) => {
    const ti = interpolate(ff, [0, FLY_IN], [0, 1], { ...clamp, easing: Easing.out(Easing.back(1.4)) });
    const to = interpolate(ff, [total - FLY_OUT - 12, total - 12], [0, 1], { ...clamp, easing: Easing.in(Easing.cubic) });
    return { ti, to, x: (1 - ti) * -(left + width + 80) + to * (W - left + 120), y: (1 - ti) * -(top + 60) * 0.7 - Math.sin(Math.min(1, ti) * Math.PI) * 60 + to * -(top + size * 0.6) };
  };
  const fly = path(f);
  const fscale = (0.55 + 0.45 * Math.min(1, fly.ti)) * (1 - 0.45 * fly.to);
  const frot = (1 - Math.min(1, fly.ti)) * 22 + fly.to * 26; // uçuş yönüne yatma
  const flying = f < FLY_IN + 6 || f > total - FLY_OUT - 12;
  const trail = flying ? [1, 2, 3, 4, 5].map((k) => ({ ...path(f - k * 3.2), k })) : [];
  return (
    <>
      {trail.map((p) => (
        <div key={p.k} style={{ position: "absolute", left: left + width / 2 + p.x - 14 + Math.sin(f / 3 + p.k) * 18, top: top + size * 0.72 + p.y + Math.cos(f / 4 + p.k * 2) * 14, width: 28 - p.k * 3, height: 28 - p.k * 3, borderRadius: "50%", background: p.k % 2 ? "#FFE9A8" : "#BFD4FF", opacity: (0.55 - p.k * 0.09) * (f < FLY_IN + 6 ? 1 - fly.ti * 0.6 : 1) }} />
      ))}
      <div style={{ position: "absolute", left: left + fly.x, top: top - hop + fly.y, width, height: size, transform: `rotate(${frot}deg) scale(${fscale})`, transformOrigin: "50% 40%" }}>
        <Mascot frame={f} mouth={mouth} pose={poseOf(cur)} prevPose={poseOf(prev)} blend={blend} flip={blend < 0.5 && i > 0 ? pflip : flip} think={think} lean={lean} size={size} />
      </div>
    </>
  );
};
