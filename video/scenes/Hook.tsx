import React from "react";
import { C, F } from "../theme";
import { pop } from "../anim";
import { SceneProps, Stage } from "./common";

export const Hook: React.FC<SceneProps<"hook">> = ({ visual, frame }) => {
  const words = visual.question.split(" ");
  return (
    <Stage style={{ justifyContent: "center", paddingLeft: 520 }}>
      {visual.emoji && (
        <div style={{ fontSize: 130, marginBottom: 20, transform: `scale(${pop(frame, 4, 9)}) rotate(${Math.sin(frame / 18) * 5}deg)`, transformOrigin: "left bottom", fontFamily: F.head }}>
          {visual.emoji}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 92, lineHeight: 1.12, color: C.text, display: "flex", flexWrap: "wrap", gap: "0 24px" }}>
        {words.map((w, i) => {
          const p = pop(frame, 10 + i * 4);
          const hot = w.includes("?") || i === words.length - 1;
          return <span key={i} style={{ opacity: p, transform: `translateY(${(1 - p) * 40}px)`, display: "inline-block", color: hot ? C.yellow : C.text }}>{w}</span>;
        })}
      </div>
    </Stage>
  );
};
