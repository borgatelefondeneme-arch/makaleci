import React from "react";
import { interpolate, spring, useCurrentFrame } from "remotion";
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
export const MascotLayer: React.FC<{ cues: CueAt[]; amplitude: number[] }> = ({ cues, amplitude }) => {
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
  return (
    <div style={{ position: "absolute", left, top: top - hop, width, height: size }}>
      <Mascot frame={f} mouth={mouth} pose={poseOf(cur)} prevPose={poseOf(prev)} blend={blend} flip={blend < 0.5 && i > 0 ? pflip : flip} think={think} lean={lean} size={size} />
    </div>
  );
};
