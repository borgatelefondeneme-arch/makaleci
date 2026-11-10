import React from "react";
import { interpolate } from "remotion";
import { C, F } from "../theme";
import { clamp, pop } from "../anim";
import { SceneProps, Stage } from "./common";

export const BigNumber: React.FC<SceneProps<"big-number">> = ({ visual, frame, beats }) => {
  const start = (beats[0] ?? 0) + 8;
  const p = pop(frame, start, 10);
  // Yalnızca düz tam sayılar sayarak gelir; son değer her zaman makaledeki yazımla gösterilir.
  const isInt = /^\d{1,9}$/.test(visual.value);
  const t = interpolate(frame, [start, start + 40], [0, 1], clamp);
  const shown = isInt && t < 1 ? String(Math.round(Number(visual.value) * (1 - Math.pow(1 - t, 3)))) : visual.value;
  const size = visual.value.length > 7 ? 190 : visual.value.length > 4 ? 250 : 320;
  const lp = pop(frame, start + 26);
  return (
    <Stage style={{ justifyContent: "center", alignItems: "flex-start", paddingLeft: 60 }}>
      <div style={{ position: "relative", transform: `scale(${0.6 + 0.4 * p})`, opacity: p, transformOrigin: "left center" }}>
        <div style={{ position: "absolute", left: -50, top: "50%", width: 560, height: 560, marginTop: -280, borderRadius: "50%", background: `radial-gradient(closest-side, ${C.purple}, transparent)`, opacity: 0.3 }} />
        <div style={{ position: "relative", display: "flex", alignItems: "baseline", gap: 26 }}>
          <span style={{ fontFamily: F.head, fontWeight: 900, fontSize: size, color: C.yellow, lineHeight: 1, letterSpacing: -4, fontVariantNumeric: "tabular-nums" }}>{shown}</span>
          {visual.unit && <span style={{ fontFamily: F.head, fontWeight: 800, fontSize: size * 0.34, color: C.text }}>{visual.unit}</span>}
        </div>
      </div>
      <div style={{ marginTop: 34, fontFamily: F.head, fontWeight: 800, fontSize: 58, color: C.text, opacity: lp, transform: `translateY(${(1 - lp) * 24}px)`, maxWidth: 1180, lineHeight: 1.2 }}>{visual.label}</div>
      {visual.sub && <div style={{ marginTop: 14, fontFamily: F.body, fontSize: 36, color: C.dim, opacity: pop(frame, start + 40), maxWidth: 1100 }}>{visual.sub}</div>}
    </Stage>
  );
};
