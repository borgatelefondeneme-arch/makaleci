import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import type { EpisodeProps } from "../schemas/index";
import { Background } from "./components/Background";
import { ensureFonts } from "./fonts";
import { C, F, GRADIENT } from "./theme";

ensureFonts();

export const Thumbnail: React.FC<EpisodeProps> = ({ script, paper }) => {
  const words = script.videoTitle.trim().split(/\s+/), len = script.videoTitle.length;
  const last = words[words.length - 1], head = words.slice(0, -1).join(" ");
  return (
  <AbsoluteFill>
    <Background />
    <div style={{ position: "absolute", left: 90, top: 60 }}>
      {/* thumbnail'de yüksek çözünürlüklü özgün görsel kullanılır */}
      <Img src={staticFile("robot/point.png")} style={{ height: 940 }} />
    </div>
    <div style={{ position: "absolute", left: 720, right: 70, top: 80, bottom: 80, display: "flex", flexDirection: "column", justifyContent: "center", gap: 22 }}>
      <div style={{ alignSelf: "flex-start", display: "flex", alignItems: "baseline", gap: 14, fontFamily: F.head }}>
        <span style={{ fontWeight: 900, fontSize: 72, letterSpacing: -1, backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>MumaApp</span>
        <span style={{ fontWeight: 800, fontSize: 40, color: C.dim }}>sunar</span>
      </div>
      {/* Konu bölümlerinde rozet yok (kullanıcı kararı): başlık kapağı doldurur. */}
      {paper.kind !== "topic" && (
        <div style={{ alignSelf: "flex-start", background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 50, padding: "12px 38px", borderRadius: 50 }}>
          Günün Makalesi #{script.episodeNumber}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: paper.kind !== "topic" ? (len > 48 ? 96 : 118) : len <= 14 ? 225 : len <= 24 ? 185 : len <= 40 ? 145 : 112, lineHeight: 1.02, letterSpacing: -3, color: C.text }}>
        {head}{head ? " " : ""}<span style={{ backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>{last}</span>
      </div>
      {/* Yapımcı ve mağaza rozetleri: kendi çizimimiz (resmî mağaza logoları kullanılmaz). */}
      <div style={{ display: "flex", alignItems: "center", gap: 22, marginTop: 14 }}>
        {[["Android", "#2E9E6B"], ["iOS", C.text]].map(([label, bg]) => (
          <div key={label} style={{ display: "flex", alignItems: "center", gap: 16, background: bg, color: "#fff", borderRadius: 26, padding: "16px 34px", boxShadow: `0 10px 26px ${C.shadow}` }}>
            <svg width={34} height={54} viewBox="0 0 34 54"><rect x={2} y={2} width={30} height={50} rx={7} fill="none" stroke="#fff" strokeWidth={4} /><circle cx={17} cy={43} r={3} fill="#fff" /></svg>
            <div style={{ fontFamily: F.head, lineHeight: 1.05 }}>
              <div style={{ fontWeight: 700, fontSize: 22, opacity: 0.85 }}>MumaApp</div>
              <div style={{ fontWeight: 900, fontSize: 42 }}>{label}</div>
            </div>
          </div>
        ))}
      </div>
      {paper.isPreprint && (
        <div style={{ alignSelf: "flex-start", background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 38, padding: "8px 28px", borderRadius: 30 }}>ÖN BASKI</div>
      )}
    </div>
  </AbsoluteFill>
  );
};
