import React from "react";
import { AbsoluteFill } from "remotion";
import type { EpisodeProps } from "../schemas/index";
import { Background } from "./components/Background";
import { ensureFonts } from "./fonts";
import { Mascot } from "./mascot/Mascot";
import { C, F } from "./theme";

ensureFonts();

export const Thumbnail: React.FC<EpisodeProps> = ({ script, paper }) => (
  <AbsoluteFill>
    <Background />
    <div style={{ position: "absolute", left: 60, top: 190, width: 620, height: 620 }}>
      <Mascot frame={30} mouth={0.7} point={1} think={0} angle={-0.25} size={620} />
    </div>
    <div style={{ position: "absolute", left: 760, right: 90, top: 120, bottom: 120, display: "flex", flexDirection: "column", justifyContent: "center", gap: 36 }}>
      <div style={{ alignSelf: "flex-start", background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 50, padding: "12px 38px", borderRadius: 50 }}>
        Günün Makalesi #{script.episodeNumber}
      </div>
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: script.videoTitle.length > 48 ? 96 : 118, lineHeight: 1.06, color: C.text, textShadow: "0 8px 30px rgba(0,0,0,0.5)" }}>
        {script.videoTitle}
      </div>
      {paper.isPreprint && (
        <div style={{ alignSelf: "flex-start", background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 38, padding: "8px 28px", borderRadius: 30 }}>ÖN BASKI</div>
      )}
    </div>
  </AbsoluteFill>
);
