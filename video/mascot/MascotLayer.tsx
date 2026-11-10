import React from "react";
import { spring, useCurrentFrame } from "remotion";
import type { MascotCue } from "../../schemas/index";
import { FPS, W, H } from "../theme";
import { Mascot } from "./Mascot";

export type CueAt = { startFrame: number; cue: MascotCue };
const BASE = 300; // scale=1 iken piksel boyutu
const mix = (a: number, b: number, t: number) => a + (b - a) * t;

// Bölüm düzeyinde tek karakter: sahne değişince konum/ölçek/poz yaylı geçişle akar.
export const MascotLayer: React.FC<{ cues: CueAt[]; amplitude: number[] }> = ({ cues, amplitude }) => {
  const f = useCurrentFrame();
  let i = 0;
  for (let k = 0; k < cues.length; k++) if (cues[k].startFrame <= f) i = k;
  const cur = cues[i].cue;
  const prev = cues[Math.max(0, i - 1)].cue;
  const t = i === 0 ? 1 : spring({ frame: f - cues[i].startFrame, fps: FPS, config: { damping: 18, mass: 0.9 } });

  const x = mix(prev.x, cur.x, t) * W;
  const y = mix(prev.y, cur.y, t) * H;
  const scale = mix(prev.scale, cur.scale, t);
  const amt = (c: MascotCue, s: MascotCue["state"]) => (c.state === s ? 1 : 0);
  const point = mix(amt(prev, "point"), amt(cur, "point"), t);
  const think = mix(amt(prev, "think"), amt(cur, "think"), t);
  const pa = cur.pointAt ?? prev.pointAt;
  const angle = pa ? Math.atan2(pa.y * H - cur.y * H, pa.x * W - cur.x * W) : 0;
  // idle durumunda ağız kapalı kalır; diğerlerinde ses genliğini izler.
  const raw = amplitude[f] ?? 0;
  const smooth = (raw + (amplitude[f - 1] ?? raw)) / 2;
  const mouth = cur.state === "idle" ? 0 : smooth;
  // geçiş sırasında hafif zıplama
  const hop = Math.sin(Math.min(1, Math.max(0, t)) * Math.PI) * (i === 0 ? 0 : 26);
  const size = BASE * scale;
  return (
    <div style={{ position: "absolute", left: x - size / 2, top: y - size / 2 - hop, width: size, height: size }}>
      <Mascot frame={f} mouth={mouth} point={point} think={think} angle={angle} size={size} />
    </div>
  );
};
