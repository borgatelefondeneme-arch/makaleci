import React from "react";
import { C, F, GRADIENT } from "../theme";
import { pop } from "../anim";
import { SceneProps, Stage } from "./common";

export const Hook: React.FC<SceneProps<"hook">> = ({ visual, frame }) => {
  const words = visual.question.split(" ");
  return (
    <Stage style={{ justifyContent: "center", alignItems: "center" }}>
      {visual.emoji && (
        <div style={{ fontSize: 130, marginBottom: 20, transform: `scale(${pop(frame, 4, 9)}) rotate(${Math.sin(frame / 18) * 5}deg)`, transformOrigin: "center bottom", fontFamily: F.head }}>
          {visual.emoji}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 92, lineHeight: 1.12, color: C.text, display: "flex", flexWrap: "wrap", justifyContent: "center", textAlign: "center", gap: "0 24px" }}>
        {words.map((w, i) => {
          const p = pop(frame, 10 + i * 4);
          const hot = w.includes("?") || i === words.length - 1;
          return <span key={i} style={{ opacity: p, transform: `translateY(${(1 - p) * 40}px)`, display: "inline-block", color: C.text, ...(hot ? { backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" } : {}) }}>{w}</span>;
        })}
      </div>
    </Stage>
  );
};
