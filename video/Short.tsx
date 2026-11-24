// Dikey kısa video (1080×1920): bölüm sahnesi büyük bir kart olarak ortada, üstte can alıcı başlık,
// üstte ilerleme çubuğu, soru varsa "Düşün!" geri sayımı, sonda abone ol çağrısı. Alt yazı yoktur.
import React from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, spring, useCurrentFrame, useVideoConfig } from "remotion";
import type { EpisodeProps } from "../schemas/index";
import { clamp } from "./anim";
import { Background } from "./components/Background";
import { ThemedBackdrop } from "./components/Themed";
import { Episode } from "./Episode";
import { ensureFonts } from "./fonts";
import { lookOf } from "./look";
import { C, EMOJI, F, H, W } from "./theme";

export type ShortSpec = {
  from: number; to: number; // bölüm karesi [from, to)
  headline: string;          // üst başlık; *yıldızlı* kelime turuncu vurgulanır
  kicker?: string;           // başlık üstündeki küçük etiket
  pause?: { at: number; len: number };     // soru ile cevap arasına eklenen düşünme molası (bölüm karesi, uzunluk)
  song?: boolean;
};
export type ShortProps = EpisodeProps & { short: ShortSpec };

const SW = 1080, SH = 1920;
const K = 0.6;                       // bölüm karesinin ölçeği: 1152×648; kenarlardan çok az kırpılır, köşe kafası görünür
const CW = SW - 40, CH = Math.round(H * K);
const CY = 560;                      // kartın üst kenarı

const Headline: React.FC<{ text: string; frame: number; fps: number }> = ({ text, frame, fps }) => {
  const pop = spring({ frame, fps, config: { damping: 11, stiffness: 140 } });
  const parts = text.split(/(\*[^*]+\*)/).filter(Boolean);
  const size = text.replace(/\*/g, "").length > 30 ? 82 : 96;
  return (
    <div style={{ transform: `scale(${0.6 + 0.4 * pop}) rotate(${(1 - pop) * -4}deg)`, opacity: Math.min(1, pop * 1.4), textAlign: "center", fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 900, fontSize: size, lineHeight: 1.08, color: C.text, letterSpacing: -1 }}>
      {parts.map((p, i) => p.startsWith("*")
        ? <span key={i} style={{ color: "#fff", background: "linear-gradient(90deg,#E2543A,#F28C38)", borderRadius: 18, padding: "0 14px", boxDecorationBreak: "clone", WebkitBoxDecorationBreak: "clone" }}>{p.slice(1, -1)}</span>
        : <span key={i}>{p}</span>)}
    </div>
  );
};

export const Short: React.FC<ShortProps> = (props) => {
  ensureFonts();
  const f = useCurrentFrame();
  const { fps, durationInFrames: dur } = useVideoConfig();
  const { short, script } = props;
  const look = lookOf(script.episodeNumber, script.song?.cast.map((c) => c.emoji) ?? []);
  const theme = script.theme;
  const bgScale = SH / H; // tema arka planı dikey ekranı dolduracak kadar büyütülür
  const cardIn = spring({ frame: f - 4, fps, config: { damping: 14 } });
  const zoom = interpolate(f, [0, dur], [1, 1.06]);           // kart içinde yavaş yaklaşma
  const endCta = interpolate(f, [dur - 75, dur - 60], [0, 1], clamp);
  const bell = Math.sin(f / 3) * 14 * endCta;
  // düşünme molası: bölüm karesi durur, geri sayım oynar, sonra kaldığı yerden sürer
  const p = short.pause;
  const pAt = p ? p.at - short.from : Infinity, pLen = p?.len ?? 0;
  const epFrame = short.from + (f < pAt ? f : f < pAt + pLen ? pAt : f - pLen);
  const thinkOn = p ? interpolate(f, [pAt, pAt + 5, pAt + pLen - 5, pAt + pLen], [0, 1, 1, 0], clamp) : 0;
  const left = p ? Math.max(1, Math.ceil(((pAt + pLen - f) / pLen) * 3)) : 0;
  const cast = (script.song?.cast ?? []).slice(0, 4).map((c) => c.emoji);
  return (
    <AbsoluteFill style={{ background: C.bg, overflow: "hidden" }}>
      {/* tema arka planı */}
      <div style={{ position: "absolute", width: W, height: H, left: (SW - W * bgScale) / 2, top: 0, transform: `scale(${bgScale})`, transformOrigin: "top left" }}>
        {theme ? <ThemedBackdrop name={theme.backdrop} /> : <Background look={look} />}
      </div>
      <AbsoluteFill style={{ background: "linear-gradient(180deg, rgba(251,248,243,0.78) 0%, rgba(251,248,243,0.35) 30%, rgba(251,248,243,0.2) 70%, rgba(27,34,56,0.55) 100%)" }} />

      {/* ilerleme çubuğu */}
      <div style={{ position: "absolute", left: 40, right: 40, top: 46, height: 12, borderRadius: 8, background: "rgba(27,34,56,0.18)" }}>
        <div style={{ width: `${(f / dur) * 100}%`, height: "100%", borderRadius: 8, background: "linear-gradient(90deg,#E2543A,#F28C38,#4A7BD0)" }} />
      </div>

      {/* üst etiket + başlık */}
      <div style={{ position: "absolute", top: 110, left: 50, right: 50, display: "flex", flexDirection: "column", alignItems: "center", gap: 26 }}>
        <div style={{ opacity: interpolate(f, [0, 8], [0, 1], clamp), fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 800, fontSize: 38, color: "#fff", background: C.text, borderRadius: 40, padding: "10px 30px" }}>
          {short.kicker ?? `MuMa Library · #${script.episodeNumber}`}
        </div>
        <Headline text={short.headline} frame={f} fps={fps} />
      </div>

      {/* bölüm sahnesi: alt yazısız */}
      <div style={{ position: "absolute", left: 20, top: CY + (1 - cardIn) * 120, width: CW, height: CH, borderRadius: 40, overflow: "hidden", boxShadow: "0 30px 80px rgba(27,34,56,0.35)", border: "6px solid #fff", opacity: cardIn }}>
        <div style={{ position: "absolute", width: W, height: H, left: (CW - W * K * zoom) / 2, top: (CH - H * K * zoom) / 2, transform: `scale(${K * zoom})`, transformOrigin: "top left" }}>
          {/* her karede kaydırma hesaplanır: içteki bölüm tam olarak epFrame karesini görür (molada sabit kalır) */}
          <Sequence from={f - epFrame} layout="none">
            <Episode {...props} captions={false} />
          </Sequence>
        </div>
      </div>

      {/* konu karakterleri: kartın altında hafifçe zıplar */}
      {!thinkOn && !short.song && cast.length > 0 && (
        <div style={{ position: "absolute", top: CY + CH + 70, left: 0, right: 0, display: "flex", justifyContent: "center", gap: 46 }}>
          {cast.map((e, i) => <div key={i} style={{ fontSize: 110, fontFamily: EMOJI, transform: `translateY(${-Math.abs(Math.sin(f / 9 + i * 0.9)) * 26}px) rotate(${Math.sin(f / 14 + i) * 6}deg)`, opacity: interpolate(f, [10 + i * 4, 18 + i * 4], [0, 1], clamp) }}>{e}</div>)}
        </div>
      )}

      {/* soru varsa: düşün geri sayımı */}
      {thinkOn > 0 && (
        <div style={{ position: "absolute", top: CY + CH + 60, left: 0, right: 0, display: "flex", justifyContent: "center", opacity: thinkOn }}>
          <div style={{ display: "flex", alignItems: "center", gap: 24, background: "#fff", borderRadius: 60, padding: "16px 40px", boxShadow: "0 16px 40px rgba(0,0,0,0.2)", transform: `scale(${1 + 0.06 * Math.sin(f / 4)})` }}>
            <span style={{ fontSize: 70 }}>🤔</span>
            <span style={{ fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 900, fontSize: 62, color: C.text }}>Düşün!</span>
            <span style={{ fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 900, fontSize: 110, color: "#E2543A", width: 90, textAlign: "center", display: "inline-block", transform: `scale(${1.25 - 0.25 * (((pAt + pLen - f) / pLen) * 3 % 1)})` }}>{left}</span>
          </div>
        </div>
      )}

      {/* şarkı kısasında davet */}
      {short.song && !thinkOn && (
        <div style={{ position: "absolute", top: CY + CH + 50, left: 0, right: 0, textAlign: "center", fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 900, fontSize: 64, color: "#fff", textShadow: "0 4px 18px rgba(0,0,0,0.45)", opacity: 1 - endCta, transform: `translateY(${Math.sin(f / 8) * 6}px)` }}>
          🎤 Birlikte söyle!
        </div>
      )}

      {/* alt çağrı: sürekli küçük, son 2 saniyede büyük */}
      <div style={{ position: "absolute", left: 0, right: 0, bottom: 120 + endCta * 60, display: "flex", justifyContent: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 22, background: interpolate(endCta, [0, 1], [0, 1]) > 0.5 ? "#E2543A" : C.text, color: "#fff", borderRadius: 70, padding: `${18 + endCta * 10}px ${44 + endCta * 16}px`, fontFamily: `${F.head}, ${EMOJI}`, fontWeight: 900, fontSize: 46 + endCta * 18, boxShadow: "0 18px 50px rgba(0,0,0,0.35)", transform: `scale(${1 + endCta * 0.04 * Math.sin(f / 5)})` }}>
          <span style={{ display: "inline-block", transform: `rotate(${bell}deg)` }}>🔔</span>
          <span>{endCta > 0.5 ? "Abone ol, devamı kanalda!" : "Tamamı MuMa Library'de"}</span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const SHORT_SIZE = { width: SW, height: SH };
export const shortEase = Easing.out(Easing.cubic);
