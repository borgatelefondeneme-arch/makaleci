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
    <div style={{ position: "absolute", left: 90, top: 60 }}>
      <Mascot frame={30} mouth={0.5} pose="point" prevPose="point" blend={1} flip={false} think={0} lean={0} size={940} />
    </div>
    <div style={{ position: "absolute", left: 740, right: 80, top: 120, bottom: 120, display: "flex", flexDirection: "column", justifyContent: "center", gap: 36 }}>
      <div style={{ alignSelf: "flex-start", background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 50, padding: "12px 38px", borderRadius: 50 }}>
        {paper.kind === "topic" ? "Günün Sorusu" : "Günün Makalesi"} #{script.episodeNumber}
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
