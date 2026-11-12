import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";
import type { EpisodeProps } from "../schemas/index";
import { Background } from "./components/Background";
import { ensureFonts } from "./fonts";
import { C, F, GRADIENT } from "./theme";
import { lookOf } from "./look";

ensureFonts();

export const Thumbnail: React.FC<EpisodeProps> = ({ script, paper }) => {
  const words = script.videoTitle.trim().split(/\s+/), len = script.videoTitle.length;
  const last = words[words.length - 1], head = words.slice(0, -1).join(" ");
  return (
  <AbsoluteFill>
    <Background look={{ ...lookOf(script.episodeNumber), motifs: [] }} />
    <div style={{ position: "absolute", left: 90, top: 60 }}>
      {/* thumbnail'de yüksek çözünürlüklü özgün görsel kullanılır */}
      <Img src={staticFile("robot/point.png")} style={{ height: 940 }} />
    </div>
    <div style={{ position: "absolute", left: 720, right: 70, top: 60, bottom: 250, display: "flex", flexDirection: "column", justifyContent: "center", gap: 22 }}>
      {/* Konu bölümlerinde rozet yok (kullanıcı kararı): başlık kapağı doldurur. */}
      {paper.kind !== "topic" && (
        <div style={{ alignSelf: "flex-start", background: C.teal, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 50, padding: "12px 38px", borderRadius: 50 }}>
          Günün Makalesi #{script.episodeNumber}
        </div>
      )}
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: paper.kind !== "topic" ? (len > 48 ? 96 : 118) : len <= 14 ? 225 : len <= 24 ? 185 : len <= 40 ? 145 : 112, lineHeight: 1.02, letterSpacing: -3, color: C.text }}>
        {head}{head ? " " : ""}<span style={{ backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>{last}</span>
      </div>
      {paper.isPreprint && (
        <div style={{ alignSelf: "flex-start", background: C.coral, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 38, padding: "8px 28px", borderRadius: 30 }}>ÖN BASKI</div>
      )}
    </div>
    {/* Sağ alt köşe: yapımcı adı, altında platform simgeleri (yazısız). */}
    <div style={{ position: "absolute", right: 70, bottom: 54, display: "flex", flexDirection: "column", alignItems: "center", gap: 14 }}>
      <div style={{ fontFamily: F.head, fontWeight: 900, fontSize: 64, letterSpacing: -1, backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>MumaApp</div>
      <div style={{ display: "flex", gap: 22 }}>
        <div style={{ width: 96, height: 96, borderRadius: 26, background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", boxShadow: `0 10px 26px ${C.shadow}` }}>
          <svg width={64} height={64} viewBox="0 0 64 64">
            <path d="M8 46 A24 24 0 0 1 56 46 Z" fill="#3DDC84" />
            <line x1={17} y1={14} x2={23} y2={25} stroke="#3DDC84" strokeWidth={4} strokeLinecap="round" />
            <line x1={47} y1={14} x2={41} y2={25} stroke="#3DDC84" strokeWidth={4} strokeLinecap="round" />
            <circle cx={22} cy={36} r={3.4} fill="#fff" /><circle cx={42} cy={36} r={3.4} fill="#fff" />
          </svg>
        </div>
        <div style={{ width: 96, height: 96, borderRadius: 26, background: C.text, display: "flex", alignItems: "center", justifyContent: "center", boxShadow: `0 10px 26px ${C.shadow}` }}>
          <svg width={58} height={58} viewBox="0 0 24 24"><path fill="#fff" d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.675-.546 9.103 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.065 2.09-.987 3.935-.987 1.831 0 2.35.987 3.96.948 1.637-.026 2.676-1.48 3.676-2.948 1.156-1.688 1.636-3.325 1.662-3.415-.039-.013-3.182-1.221-3.22-4.857-.026-3.04 2.48-4.494 2.597-4.559-1.429-2.09-3.623-2.324-4.39-2.376-2-.156-3.675 1.09-4.61 1.09zM15.53 3.83c.843-1.012 1.4-2.427 1.245-3.83-1.207.052-2.662.805-3.532 1.818-.78.896-1.454 2.338-1.273 3.714 1.338.104 2.715-.688 3.559-1.701" /></svg>
        </div>
      </div>
    </div>
  </AbsoluteFill>
  );
};
