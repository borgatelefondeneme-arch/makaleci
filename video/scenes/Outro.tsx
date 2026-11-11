import React from "react";
import { interpolate } from "remotion";
import { C, F } from "../theme";
import { clamp, ease, pop } from "../anim";
import { SubscribeButton } from "../components/Subscribe";
import { Card, SceneProps, Stage, Title } from "./common";

// Kapanış: "Bugün bunu öğrendik" + 3 madde tek tek ✓ ile; ardından abone ol + sonraki video.
export const Outro: React.FC<SceneProps<"outro">> = ({ frame, beats, dur, tail, data }) => {
  const talk = dur - tail; // anlatımın bittiği kare
  const items = data.script.takeaways;
  const at = (k: number) => {
    // 3 maddeyi özet satırlarına yay: satır sayısı 3'ten azsa eşit aralık.
    if (beats.length >= 3) return beats[Math.min(beats.length - 1, Math.round((k * (beats.length - 1)) / 2))] + 8;
    return Math.round(12 + (talk * 0.75 * k) / 3);
  };
  const leave = interpolate(frame, [talk - 4, talk + 14], [0, 1], clamp);
  const t2 = talk + 12;
  return (
    <>
      <Stage style={{ paddingRight: 340, opacity: 1 - leave, transform: `translateY(${-leave * 40}px)` }}>
        <Title frame={frame} color={C.yellow}>Bugün bunu öğrendik</Title>
        <div style={{ display: "flex", flexDirection: "column", gap: 28 }}>
          {items.map((it, k) => {
            const s = at(k), p = pop(frame, s);
            const draw = ease(frame, s + 6, 12);
            return (
              <Card key={k} accent={draw > 0.9 ? C.teal : undefined} style={{ display: "flex", alignItems: "center", gap: 32, padding: "28px 38px", opacity: p, transform: `translateX(${(1 - p) * 90}px)` }}>
                <svg width={76} height={76} viewBox="-38 -38 76 76" style={{ flexShrink: 0, transform: `scale(${0.8 + 0.2 * pop(frame, s + 14, 7)})` }}>
                  <circle r={34} fill={draw > 0.05 ? C.teal : "none"} stroke={C.teal} strokeWidth={6} opacity={0.25 + 0.75 * draw} />
                  <path d="M -16 2 L -4 14 L 18 -12" fill="none" stroke={C.ink} strokeWidth={9} strokeLinecap="round" strokeLinejoin="round" strokeDasharray={54} strokeDashoffset={54 * (1 - draw)} />
                </svg>
                <div style={{ fontFamily: F.body, fontWeight: 600, fontSize: 42, color: C.text, lineHeight: 1.25 }}>{it}</div>
              </Card>
            );
          })}
        </div>
      </Stage>
      {frame >= talk - 4 && (
        <Stage style={{ justifyContent: "center", paddingLeft: 420, gap: 36, opacity: leave }}>
          <div style={{ transform: `scale(${pop(frame, t2)})`, transformOrigin: "left center" }}>
            <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 70, color: C.text, lineHeight: 1.1, maxWidth: 1250 }}>Bir sonraki bilim videosunda <span style={{ color: C.yellow }}>görüşürüz!</span></div>
            <div style={{ fontFamily: F.body, fontSize: 38, color: C.dim, marginTop: 10 }}>MuMa Library’de yeni sorular yolda. Abone ol, zili aç!</div>
          </div>
          <div style={{ opacity: pop(frame, t2 + 14), height: 100 }}><SubscribeButton frame={frame} press={t2 + 70} scale={1.35} /></div>
          <Card accent={C.purple} style={{ opacity: pop(frame, t2 + 34), transform: `translateY(${(1 - pop(frame, t2 + 34)) * 50}px)`, display: "flex", alignItems: "center", gap: 30, maxWidth: 1150 }}>
            <svg width={90} height={90} viewBox="-45 -45 90 90" style={{ flexShrink: 0 }}>
              <circle r={41} fill={C.purple} /><path d="M -12 -20 L 22 0 L -12 20 Z" fill="#fff" transform={`translate(${Math.sin(frame / 8) * 3} 0)`} />
            </svg>
            <div>
              <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 30, color: C.purple, textTransform: "uppercase", letterSpacing: 1 }}>Sıradaki video</div>
              <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 44, color: C.text, lineHeight: 1.2 }}>{data.script.nextTeaser}</div>
            </div>
          </Card>
        </Stage>
      )}
    </>
  );
};
