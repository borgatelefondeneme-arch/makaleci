import React, { useMemo } from "react";
import { spring, useCurrentFrame } from "remotion";
import type { MascotCue } from "../../schemas/index";
import { FPS, W, H } from "../theme";
import { ASPECT, Mascot, SEQ } from "./Mascot";

export type CueAt = { startFrame: number; cue: MascotCue };
const BASE = 620; // scale=1 iken kare yüksekliği (px)
const mix = (a: number, b: number, t: number) => a + (b - a) * t;
// Durum → hedef poz: konuşma ve işaret "parmak havada + açık el", bekleme ve düşünme "kollar kavuşuk".
const crossed = (c: MascotCue) => c.state === "idle" || c.state === "think";
// Açık el içeriğe baksın: hedef (ya da ekran ortası) soldaysa görsel çevrilir.
const flipOf = (c: MascotCue) => (c.pointAt ? c.pointAt.x < c.x : c.x > 0.5);

// Her video karesi için oynatılacak kaynak kareyi hesaplar (deterministik benzetim):
// hedef poza gerçek geçiş kareleri üzerinden gidilir, poza varınca kısa bir döngü ileri-geri oynar.
const LOOP = 0.5, PLAY = 0.8, FAST = 2.4; // kaynak kare / video karesi
export const buildTimeline = (cues: CueAt[], total: number): number[] => {
  const out = new Array<number>(total);
  let x = SEQ.greet, dir = -1, ci = 0;
  for (let f = 0; f < total; f++) {
    while (ci + 1 < cues.length && cues[ci + 1].startFrame <= f) ci++;
    const toCrossed = ci > 0 && crossed(cues[ci].cue); // açılış her zaman karşılama + işaret
    if (!toCrossed) {
      if (x < SEQ.pointA) x += x < 62 ? 0.3 : PLAY; // karşılama hareketi ağır çekimde
      else if (x > SEQ.pointB) { x = Math.max(SEQ.pointB, x - FAST); dir = -1; }
      else { x += dir * LOOP; if (x <= SEQ.pointA) dir = 1; if (x >= SEQ.pointB) dir = -1; }
    } else {
      if (x < SEQ.crossA) { x = Math.min(SEQ.crossA, x + (x < SEQ.pointB ? 3.2 : FAST)); dir = 1; }
      else if (x > SEQ.crossB) x -= LOOP;
      else { x += dir * LOOP; if (x >= SEQ.crossB) dir = -1; if (x <= SEQ.crossA) dir = 1; }
    }
    out[f] = Math.round(x);
  }
  return out;
};

// Bölüm düzeyinde tek karakter: sahne değişince konum/ölçek yaylı geçişle akar.
export const MascotLayer: React.FC<{ cues: CueAt[]; amplitude: number[]; total: number }> = ({ cues, amplitude, total }) => {
  const f = useCurrentFrame();
  const timeline = useMemo(() => buildTimeline(cues, total), [cues, total]);
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
  const left = Math.min(W - width + width * 0.08, Math.max(-width * 0.08, cx - width / 2));
  const top = Math.min(H - 130 - size, Math.max(50, cy - size / 2));
  const think = mix(prev.state === "think" ? 1 : 0, cur.state === "think" ? 1 : 0, t);
  // Yön değişimi, yer değiştirme hareketinin ortasında yapılır.
  const flip = i > 0 && t < 0.5 ? flipOf(prev) : flipOf(cur);
  const lean = cur.state === "point" && cur.pointAt ? (flipOf(cur) ? -4 : 4) * Math.min(1, t) : 0;
  const raw = amplitude[f] ?? 0;
  const mouth = cur.state === "idle" ? 0 : (raw + (amplitude[f - 1] ?? raw)) / 2;
  const hop = Math.sin(Math.min(1, Math.max(0, t)) * Math.PI) * (i === 0 ? 0 : 22);
  return (
    <div style={{ position: "absolute", left, top: top - hop, width, height: size }}>
      <Mascot frame={f} idx={timeline[Math.min(total - 1, f)]} mouth={mouth} flip={flip} think={think} lean={lean} size={size} />
    </div>
  );
};
