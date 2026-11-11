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
    <div style={{ position: "absolute", left: 720, right: 70, top: 80, bottom: 80, display: "flex", flexDirection: "column", justifyContent: "center", gap: 30 }}>
      {/* Konu bölümlerinde rozet yok (kullanıcı kararı): başlık kapağı doldurur. */}
      {paper.kind !== "topic" && (
        <div style={{ alignSelf: "flex-start", background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 50, padding: "12px 38px", borderRadius: 50 }}>
          Günün Makalesi #{script.episodeNumber}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: paper.kind !== "topic" ? (len > 48 ? 96 : 118) : len <= 14 ? 250 : len <= 24 ? 185 : len <= 40 ? 145 : 112, lineHeight: 1.02, letterSpacing: -3, color: C.text }}>
        {head}{head ? " " : ""}<span style={{ backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>{last}</span>
      </div>
      {paper.isPreprint && (
        <div style={{ alignSelf: "flex-start", background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 38, padding: "8px 28px", borderRadius: 30 }}>ÖN BASKI</div>
      )}
    </div>
  </AbsoluteFill>
  );
};
