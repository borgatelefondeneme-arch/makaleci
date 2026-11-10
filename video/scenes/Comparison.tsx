import React from "react";
import { C, F } from "../theme";
import { beatAt, pop } from "../anim";
import { Card, SceneProps, Stage, Title } from "./common";

export const Comparison: React.FC<SceneProps<"comparison">> = ({ visual, frame, beats, dur }) => {
  const side = (s: typeof visual.left, i: number, col: string) => {
    const st = beatAt(beats, i, dur, 2);
    const p = pop(frame, st);
    return (
      <Card accent={col} style={{ flex: 1, opacity: p, transform: `translateY(${(1 - p) * 60}px) rotate(${(1 - p) * (i ? 3 : -3)}deg)`, minHeight: 500 }}>
        <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 44, color: col }}>{s.title}</div>
        {s.value && <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 110, color: C.text, lineHeight: 1.1, margin: "12px 0" }}>{s.value}</div>}
        {s.items.map((it, k) => {
          const a = pop(frame, st + 14 + k * 9);
          return (
            <div key={k} style={{ display: "flex", gap: 16, marginTop: 16, opacity: a, fontFamily: F.body, fontSize: 34, color: C.text, lineHeight: 1.3 }}>
              <span style={{ color: col, fontWeight: 700 }}>●</span><span>{it}</span>
            </div>
          );
        })}
      </Card>
    );
  };
  const v = pop(frame, beatAt(beats, 1, dur, 2) - 6, 8);
  return (
    <Stage style={{ paddingRight: 60 }}>
      <Title frame={frame} color={C.coral}>{visual.title}</Title>
      <div style={{ display: "flex", gap: 90, alignItems: "stretch", position: "relative", width: 1440 }}>
        {side(visual.left, 0, C.teal)}
        {side(visual.right, 1, C.yellow)}
        <div style={{ position: "absolute", left: "50%", top: "50%", width: 110, height: 110, margin: "-55px 0 0 -55px", borderRadius: "50%", background: C.coral, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: F.head, fontWeight: 900, fontSize: 40, color: "#fff", transform: `scale(${v}) rotate(${(1 - v) * -90}deg)`, border: `6px solid ${C.bg}` }}>VS</div>
      </div>
    </Stage>
  );
};
