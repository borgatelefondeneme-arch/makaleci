import React from "react";
import { C, F } from "../theme";
import { beatAt, ease, pop } from "../anim";
import { Card, SceneProps, Stage, Title } from "./common";

export const QuoteCard: React.FC<SceneProps<"quote-card">> = ({ visual, frame }) => {
  const p = pop(frame, 4);
  const chars = Math.round(visual.quote.length * ease(frame, 12, Math.min(70, visual.quote.length)));
  return (
    <Stage style={{ justifyContent: "center", paddingRight: 340 }}>
      <Card accent={C.purple} style={{ position: "relative", padding: "70px 70px 50px 110px", transform: `scale(${0.9 + 0.1 * p})`, opacity: p }}>
        <div style={{ position: "absolute", left: 26, top: -30, fontFamily: "Georgia, serif", fontSize: 240, lineHeight: 1, color: C.purple }}>“</div>
        <div style={{ fontFamily: F.head, fontWeight: 600, fontSize: 52, lineHeight: 1.3, color: C.text }}>
          {visual.quote.slice(0, chars)}<span style={{ opacity: 0 }}>{visual.quote.slice(chars)}</span>
        </div>
        <div style={{ marginTop: 34, fontFamily: F.body, fontWeight: 600, fontSize: 32, color: C.teal, opacity: pop(frame, 50) }}>— {visual.attribution}</div>
      </Card>
    </Stage>
  );
};

export const Bullets: React.FC<SceneProps<"bullets">> = ({ visual, frame, beats, dur }) => {
  const caution = visual.tone === "caution";
  const col = caution ? C.coral : C.teal;
  return (
    <Stage style={{ paddingRight: 340 }}>
      <Title frame={frame} color={col}>{visual.title}</Title>
      <div style={{ display: "flex", flexDirection: "column", gap: 26 }}>
        {visual.items.map((it, i) => {
          const p = pop(frame, beatAt(beats, i, dur, visual.items.length));
          return (
            <Card key={i} accent={p > 0.5 ? col : undefined} style={{ display: "flex", alignItems: "center", gap: 30, padding: "26px 36px", opacity: p, transform: `translateX(${(1 - p) * 80}px)` }}>
              <svg width={64} height={64} viewBox="-32 -32 64 64" style={{ flexShrink: 0 }}>
                {caution ? (<>
                  <path d="M 0 -26 L 28 22 L -28 22 Z" fill={C.coral} stroke={C.coral} strokeWidth={6} strokeLinejoin="round" />
                  <rect x={-3.5} y={-10} width={7} height={18} rx={3.5} fill={C.ink} /><circle cy={15} r={4} fill={C.ink} />
                </>) : (<><circle r={28} fill={C.teal} /><text y={13} textAnchor="middle" fontFamily={F.head} fontWeight={900} fontSize={36} fill={C.ink}>{i + 1}</text></>)}
              </svg>
              <div style={{ fontFamily: F.body, fontWeight: 600, fontSize: 40, color: C.text, lineHeight: 1.25 }}>{it}</div>
            </Card>
          );
        })}
      </div>
    </Stage>
  );
};
