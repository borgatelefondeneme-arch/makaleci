import { interpolate, spring, Easing } from "remotion";
import { FPS } from "./theme";

export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
// start karesinden itibaren 0→1 yaylı giriş
export const pop = (frame: number, start: number, damping = 14) =>
  spring({ frame: frame - start, fps: FPS, config: { damping, mass: 0.7 } });
// start..start+len arasında yumuşak 0→1
export const ease = (frame: number, start: number, len = 20) =>
  interpolate(frame, [start, start + len], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
// k. öğenin belireceği kare: satır vuruşları yetmezse eşit aralıkla devam eder.
export const beatAt = (beats: number[], k: number, dur: number, n: number) => {
  if (k < beats.length && n <= beats.length) return beats[k] + 6;
  const span = Math.max(30, dur * 0.7);
  return Math.round(8 + (span * k) / Math.max(1, n));
};
