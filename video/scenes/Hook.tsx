import React from "react";
import { C, F, GRADIENT } from "../theme";
import { pop } from "../anim";
import { QuestionMarks } from "../components/Motion";
import { SceneProps, Stage } from "./common";

export const Hook: React.FC<SceneProps<"hook">> = ({ visual, frame }) => {
  const words = visual.question.split(" ");
  return (
    <>
    <QuestionMarks frame={frame} />
    <Stage style={{ justifyContent: "center", alignItems: "center" }}>
      {visual.emoji && (
        <div style={{ fontSize: 130, marginBottom: 20, transform: `translateY(${-Math.abs(Math.sin(frame / 11)) * 26}px) scale(${pop(frame, 4, 9) * (1 + 0.06 * Math.sin(frame / 6))}) rotate(${Math.sin(frame / 14) * 9}deg)`, transformOrigin: "center bottom", fontFamily: F.head }}>
          {visual.emoji}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 92, lineHeight: 1.12, color: C.text, display: "flex", flexWrap: "wrap", justifyContent: "center", textAlign: "center", gap: "0 24px" }}>
        {words.map((w, i) => {
          const p = pop(frame, 10 + i * 4);
          const hot = w.includes("?") || i === words.length - 1;
          return <span key={i} style={{ opacity: p, transform: `translateY(${(1 - p) * 40 + Math.sin(frame / 9 - i * 0.7) * 7}px) rotate(${Math.sin(frame / 13 - i) * 1.5}deg)`, display: "inline-block", color: C.text, ...(hot ? { backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" } : {}) }}>{w}</span>;
        })}
      </div>
    </Stage>
    </>
  );
};
