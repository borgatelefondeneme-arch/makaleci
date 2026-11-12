import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import type { Actor } from "../../schemas/index";
import { C, F, H, W } from "../theme";
import { clamp } from "../anim";

// Konuya özel sahneleme: arka plan dünyaları, ortamda gezen karakterler ve sahne efektleri.
// Koyu dünyalarda (uzay, okyanus, yer altı, fırtına) içerik krem bir panonun üstünde durur; dünya çevresinde ve altında görünür.
const rnd = (i: number, n: number) => { const x = Math.sin(i * 127.1 + n * 311.7) * 43758.5453; return x - Math.floor(x); };
export type BackdropName = "space" | "underground" | "meadow" | "ocean" | "storm";
export const BACKDROPS: Record<BackdropName, { panel: boolean; dark: boolean; ground: number }> = {
  space: { panel: true, dark: true, ground: 960 }, underground: { panel: true, dark: false, ground: 950 },
  meadow: { panel: false, dark: false, ground: 940 }, ocean: { panel: true, dark: true, ground: 950 }, storm: { panel: true, dark: true, ground: 955 },
};
// Pano: içerik alanı. Alt bant (yer) karakterlere kalır.
export const PANEL = { left: 176, right: 176, top: 78, bottom: 236 };

export const ThemedBackdrop: React.FC<{ name: BackdropName }> = ({ name }) => {
  const f = useCurrentFrame();
  if (name === "space") {
    return (
      <AbsoluteFill style={{ background: "linear-gradient(180deg, #141B3A 0%, #252E63 55%, #4A3F7A 100%)", overflow: "hidden" }}>
        <div style={{ position: "absolute", left: -200, top: 200, width: 2400, height: 520, background: "radial-gradient(closest-side, rgba(190,170,255,0.28), transparent)", transform: "rotate(-14deg)" }} />
        <svg width={W} height={H} style={{ position: "absolute" }}>
          {Array.from({ length: 130 }, (_, i) => {
            const tw = 0.45 + 0.55 * Math.abs(Math.sin(f / (16 + rnd(i, 4) * 30) + i));
            return <circle key={i} cx={rnd(i, 1) * W} cy={rnd(i, 2) * H} r={1.4 + rnd(i, 3) * 3.4} fill={["#fff", "#FFE9B8", "#CFE0FF"][i % 3]} opacity={tw} />;
          })}
          {/* takımyıldız çizgileri */}
          {[[60, 300, 120, 420, 80, 560, 150, 660], [1800, 200, 1860, 330, 1790, 450, 1850, 600]].map((p, k) => (
            <g key={k} opacity={0.5 + 0.2 * Math.sin(f / 40 + k)}>
              <polyline points={p.join(" ")} fill="none" stroke="#CFE0FF" strokeWidth={2} strokeDasharray="4 8" />
              {[0, 2, 4, 6].map((q) => <circle key={q} cx={p[q]} cy={p[q + 1]} r={6} fill="#FFE9B8" />)}
            </g>
          ))}
          {/* kayan yıldız: birkaç saniyede bir */}
          {[0, 1].map((k) => { const t = ((f + k * 170) % 340) / 40; if (t > 1) return null; const x = W * (0.15 + k * 0.5) + t * 520, y = 40 + k * 30 + t * 210; return <line key={k} x1={x} y1={y} x2={x - 150} y2={y - 60} stroke="#fff" strokeWidth={5} strokeLinecap="round" opacity={Math.sin(t * Math.PI)} />; })}
        </svg>
        <div style={{ position: "absolute", left: 40, bottom: 60, fontSize: 120, opacity: 0.85, fontFamily: F.head, transform: `rotate(${Math.sin(f / 80) * 6}deg)` }}>🪐</div>
      </AbsoluteFill>
    );
  }
  if (name === "underground") {
    const layers = [["#E9D3B0", 150], ["#D9B98C", 300], ["#C79F74", 470], ["#B5895F", 650], ["#A0744E", 830], ["#8A6040", 1080]] as const;
    let top = 110;
    return (
      <AbsoluteFill style={{ background: "linear-gradient(180deg, #CDE9F7 0%, #EAF6FB 100%)", overflow: "hidden" }}>
        <div style={{ position: "absolute", left: 1640 + Math.sin(f / 200) * 20, top: 10, fontSize: 80, fontFamily: F.head }}>☀️</div>
        {[0, 1, 2].map((k) => <div key={k} style={{ position: "absolute", left: ((k * 700 + f * (0.3 + k * 0.12)) % (W + 300)) - 200, top: 8 + k * 14, fontSize: 70, opacity: 0.9, fontFamily: F.head }}>☁️</div>)}
        <svg width={W} height={H} style={{ position: "absolute" }}>
          <path d={`M 0 110 Q 480 84 960 108 T ${W} 100 V ${H} H 0 Z`} fill="#7DB36A" />
          {layers.map(([col, bottom], i) => {
            const y0 = top + 18; top = bottom;
            let d = `M 0 ${y0}`; for (let x = 0; x <= W; x += 60) d += ` L ${x} ${y0 + Math.sin(x / (170 + i * 40) + i * 2) * (10 + i * 2)}`;
            return <path key={i} d={d + ` V ${H} H 0 Z`} fill={col} />;
          })}
          {Array.from({ length: 46 }, (_, i) => <ellipse key={i} cx={rnd(i, 1) * W} cy={170 + rnd(i, 2) * 900} rx={5 + rnd(i, 3) * 14} ry={4 + rnd(i, 4) * 9} fill="#5E4330" opacity={0.25} />)}
        </svg>
        {["🦴", "🐚", "🦷", "🐌", "🦴", "🐚", "🍂", "🦕"].map((e, i) => (
          <div key={i} style={{ position: "absolute", left: [30, 1780, 60, 1800, 1760, 40, 420, 1420][i], top: [250, 300, 520, 560, 800, 780, 960, 970][i], fontSize: 78, opacity: 0.5, fontFamily: F.head, filter: "grayscale(0.5) sepia(0.4)", transform: `rotate(${(i * 47) % 360 + Math.sin(f / 90 + i) * 4}deg)` }}>{e}</div>
        ))}
      </AbsoluteFill>
    );
  }
  if (name === "ocean") {
    return (
      <AbsoluteFill style={{ background: "linear-gradient(180deg, #7FD0E8 0%, #2C8FB8 45%, #134B78 100%)", overflow: "hidden" }}>
        <svg width={W} height={H} style={{ position: "absolute" }}>
          {[0, 1, 2, 3].map((k) => <path key={k} d={`M ${300 + k * 420} -20 L ${120 + k * 420 + Math.sin(f / 60 + k) * 60} ${H} L ${420 + k * 420 + Math.sin(f / 60 + k) * 60} ${H} Z`} fill="#fff" opacity={0.07} />)}
          {Array.from({ length: 34 }, (_, i) => { const r = 6 + rnd(i, 3) * 20, y = ((rnd(i, 2) * H - f * (0.8 + rnd(i, 4) * 1.6)) % (H + 80) + H + 80) % (H + 80) - 40; return <circle key={i} cx={rnd(i, 1) * W + Math.sin(f / 30 + i) * 14} cy={y} r={r} fill="none" stroke="#fff" strokeWidth={3} opacity={0.35} />; })}
          {[0, 1].map((k) => { let d = `M 0 ${H}`; for (let x = 0; x <= W; x += 50) d += ` L ${x} ${H - 70 - k * 40 + Math.sin(x / 140 + k * 2 + f / 50) * 16}`; return <path key={k} d={d + ` L ${W} ${H} Z`} fill={["#E8D2A0", "#D6BC84"][k]} />; })}
        </svg>
        {["🌿", "🪸", "🌿", "🪸", "🐚"].map((e, i) => <div key={i} style={{ position: "absolute", left: [30, 150, 1700, 1810, 900][i], bottom: 30 + (i % 2) * 14, fontSize: 96, fontFamily: F.head, transformOrigin: "50% 100%", transform: `rotate(${Math.sin(f / 30 + i) * 8}deg)` }}>{e}</div>)}
      </AbsoluteFill>
    );
  }
  if (name === "storm") {
    return (
      <AbsoluteFill style={{ background: "linear-gradient(180deg, #3C4763 0%, #5C6B8C 55%, #8E9BB8 100%)", overflow: "hidden" }}>
        {Array.from({ length: 9 }, (_, i) => <div key={i} style={{ position: "absolute", left: ((i * 290 + f * (0.5 + (i % 3) * 0.25)) % (W + 500)) - 300, top: [-20, 30, 0, 50, 10, 40, -10, 20, 60][i], fontSize: 190 + (i % 3) * 50, opacity: 0.85, fontFamily: F.head, filter: "brightness(0.78)" }}>☁️</div>)}
        <svg width={W} height={H} style={{ position: "absolute" }}>
          {Array.from({ length: 90 }, (_, i) => { const y = ((rnd(i, 2) * H + f * (16 + rnd(i, 3) * 10)) % (H + 60)) - 30, x = rnd(i, 1) * (W + 200) - 100 - y * 0.12; return <line key={i} x1={x} y1={y} x2={x - 5} y2={y + 30} stroke="#DCE8FF" strokeWidth={3} strokeLinecap="round" opacity={0.4} />; })}
          <path d={`M 0 ${H} V 1010 Q 480 980 960 1004 T ${W} 996 V ${H} Z`} fill="#2E3A52" />
        </svg>
      </AbsoluteFill>
    );
  }
  // meadow: açık gök, güneş, bulutlar, tepeler ve çiçekler
  return (
    <AbsoluteFill style={{ background: "linear-gradient(180deg, #CDEBFA 0%, #EEF9FF 60%, #F8FBEF 100%)", overflow: "hidden" }}>
      <div style={{ position: "absolute", left: 1650, top: 30, width: 190, height: 190, borderRadius: "50%", background: "radial-gradient(closest-side, #FFE28A, #FFD15C 60%, transparent)", transform: `scale(${1 + 0.05 * Math.sin(f / 30)})` }} />
      {[0, 1, 2, 3].map((k) => <div key={k} style={{ position: "absolute", left: ((k * 560 + f * (0.35 + k * 0.1)) % (W + 400)) - 260, top: 20 + k * 34, fontSize: 120 + k * 16, opacity: 0.9, fontFamily: F.head }}>☁️</div>)}
      <svg width={W} height={H} style={{ position: "absolute" }}>
        <path d={`M 0 ${H} V 900 Q 400 800 820 890 T ${W} 850 V ${H} Z`} fill="#BFE3A6" />
        <path d={`M 0 ${H} V 960 Q 500 880 1000 960 T ${W} 930 V ${H} Z`} fill="#9FD488" />
      </svg>
      {["🌼", "🌷", "🌻", "🌸", "🌼", "🌺", "🌷", "🌻"].map((e, i) => <div key={i} style={{ position: "absolute", left: 40 + i * 250 + (i % 2) * 60, bottom: 14 + (i % 3) * 18, fontSize: 84, fontFamily: F.head, transformOrigin: "50% 100%", transform: `rotate(${Math.sin(f / 26 + i * 1.3) * 7}deg)` }}>{e}</div>)}
    </AbsoluteFill>
  );
};

// İçerik panosu: koyu dünyalarda yazılar bunun üstünde okunur.
export const Panel: React.FC<{ opacity?: number; inset?: Partial<typeof PANEL> }> = ({ opacity = 1, inset }) => {
  const p = { ...PANEL, ...inset };
  return <div style={{ position: "absolute", left: p.left, right: p.right, top: p.top, bottom: p.bottom, borderRadius: 54, background: "rgba(251,248,243,0.95)", boxShadow: "0 24px 70px rgba(10,14,40,0.35), inset 0 0 0 6px rgba(255,255,255,0.55)", opacity }} />;
};

// Tek karakteri çizer; sola bakan emoji sağa giderken çevrilir.
const Sprite: React.FC<{ emoji: string; x: number; y: number; size: number; right: boolean; facesRight?: boolean; rot?: number; opacity?: number }> = ({ emoji, x, y, size, right, facesRight, rot = 0, opacity = 1 }) => (
  <div style={{ position: "absolute", left: x - size / 2, top: y - size, fontSize: size, lineHeight: 1, fontFamily: F.head, opacity, transform: `scaleX(${right !== !!facesRight ? -1 : 1}) rotate(${rot}deg)`, filter: "drop-shadow(0 8px 10px rgba(10,14,40,0.25))" }}>{emoji}</div>
);

// Karakter davranışları. mode "ambient": yer bandında, ara sıra geçer. mode "show": şarkıda, büyük ve vuruşla.
export const Actors: React.FC<{ actors: Actor[]; t: number; ground: number; mode: "ambient" | "show"; beat?: number; energy?: number }> = ({ actors, t, ground, mode, beat = 15, energy = 1 }) => {
  const show = mode === "show";
  return (<>
    {actors.map((a, i) => {
      const size = a.size ?? (show ? 210 : 104);
      const period = Math.round((a.every ?? (show ? 9 : 14)) * 30);
      const tt = ((t + i * 97) % period + period) % period;
      const dur = show ? Math.min(period, 250) : Math.min(period, 330);
      const p = tt / dur; // 0..1 geçiş; >1 ise sahne dışında
      const right = i % 2 === 0;
      const span = W + size * 4;
      const xAt = (q: number) => (right ? -size * 2 + q * span : W + size * 2 - q * span);
      const hop = Math.abs(Math.sin((Math.PI * t) / beat));
      if (a.kind === "walk" || a.kind === "swim") {
        if (p > 1) return null;
        const y = a.kind === "swim" ? ground - 60 + Math.sin(t / 14 + i) * 26 : ground - hop * (show ? 34 * energy : 10);
        return <Sprite key={i} emoji={a.emoji} x={xAt(p)} y={y} size={size} right={right} facesRight={a.facesRight} rot={Math.sin(t / 6 + i) * 4} />;
      }
      if (a.kind === "fly") {
        if (p > 1) return null;
        const base = show ? 690 + (i % 2) * 60 : ground - 70;
        return <Sprite key={i} emoji={a.emoji} x={xAt(p)} y={base + Math.sin(p * Math.PI * 5 + i) * (show ? 56 : 26)} size={size} right={right} facesRight={a.facesRight} rot={Math.cos(p * Math.PI * 5 + i) * 10} />;
      }
      if (a.kind === "chase") {
        if (p > 1) return null;
        // küçük önde kaçar, büyük arkadan kovalar; ara mesafe nefes gibi açılıp kapanır
        const gap = size * (1.5 + 0.5 * Math.sin(t / 22));
        const xb = xAt(p), xs = xb + (right ? gap : -gap);
        return (<React.Fragment key={i}>
          <Sprite emoji={a.emoji2 ?? a.emoji} x={xs} y={ground - Math.abs(Math.sin(t / 4)) * 22} size={size * 0.55} right={right} facesRight={a.facesRight} rot={Math.sin(t / 3) * 8} />
          <Sprite emoji={a.emoji} x={xb} y={ground - Math.abs(Math.sin(t / 7)) * (show ? 40 * energy : 14)} size={size} right={right} facesRight={a.facesRight} rot={Math.sin(t / 7) * 5} />
        </React.Fragment>);
      }
      if (a.kind === "dig") {
        // kazma sallanır, toprak sıçrar, bulunan şey yavaşça yükselir
        const x = show ? 330 + i * 420 : 250 + i * 520, sw = Math.sin(t / 5);
        const found = Math.min(1, (((t + i * 200) % 600) / 420));
        return (<React.Fragment key={i}>
          {a.emoji2 && <div style={{ position: "absolute", left: x + 30, top: ground - 30 - found * 64, fontSize: size * 0.78, lineHeight: 1, fontFamily: F.head, opacity: Math.min(1, found * 2) }}>{a.emoji2}</div>}
          {[0, 1, 2, 3, 4].map((k) => { const q = ((t * 1.3 + k * 9) % 30) / 30; return <div key={k} style={{ position: "absolute", left: x + 60 + (k - 2) * 26 * q * 2, top: ground - 30 - Math.sin(q * Math.PI) * 70, width: 14, height: 14, borderRadius: 5, background: "#8A6040", opacity: (1 - q) * (sw > 0 ? 1 : 0.3) }} />; })}
          <div style={{ position: "absolute", left: x - size * 0.5, top: ground - size * 1.25, fontSize: size, lineHeight: 1, fontFamily: F.head, transformOrigin: "80% 80%", transform: `rotate(${-20 + sw * 38}deg)`, filter: "drop-shadow(0 8px 10px rgba(10,14,40,0.25))" }}>{a.emoji}</div>
        </React.Fragment>);
      }
      if (a.kind === "hop") {
        const hops = actors.filter((b) => b.kind === "hop"), hi = hops.indexOf(a);
        const x = (W / (hops.length + 1)) * (hi + 1);
        const ph = Math.pow(Math.abs(Math.sin((Math.PI * (t - i * 4)) / beat)), 1.5);
        return <Sprite key={i} emoji={a.emoji} x={x} y={ground - ph * (show ? 130 * energy : 30)} size={size} right={false} facesRight={false} rot={Math.sin((Math.PI * (t - i * 4)) / (beat * 2)) * 12} />;
      }
      if (a.kind === "orbit") {
        const ang = t * 0.022 + (i * Math.PI * 2) / actors.length, d = Math.sin(ang);
        return <Sprite key={i} emoji={a.emoji} x={W / 2 + Math.cos(ang) * (show ? 700 : 820)} y={(show ? 720 : ground) + d * (show ? 150 : 30)} size={size * (0.8 + 0.25 * (d + 1) / 2)} right={false} facesRight={false} rot={Math.sin(t / 20 + i) * 10} opacity={0.8 + 0.2 * (d + 1) / 2} />;
      }
      // swarm: bir noktanın çevresinde vızıldayan küçük sürü
      const cx = (W / (actors.length + 1)) * (i + 1) + Math.sin(t / 90 + i) * 200, cy = show ? 640 : ground - 60;
      return (<React.Fragment key={i}>
        {Array.from({ length: show ? 7 : 4 }, (_, k) => {
          const ax = cx + Math.sin(t / (9 + k * 2) + k * 2.1) * (show ? 190 : 90), ay = cy + Math.cos(t / (7 + k * 1.7) + k) * (show ? 110 : 34);
          return <Sprite key={k} emoji={a.emoji} x={ax} y={ay} size={size * 0.5} right={Math.cos(t / (9 + k * 2) + k * 2.1) > 0} facesRight={a.facesRight} rot={Math.sin(t / 3 + k) * 10} />;
        })}
      </React.Fragment>);
    })}
  </>);
};

// Sahne efekti: sahnenin kendi içeriğinin üstünde/altında oynar. frame: sahne karesi, dur: sahne süresi, beats: cümle başlangıçları.
export const SceneEffect: React.FC<{ fx: string; frame: number; dur: number; beats: number[] }> = ({ fx, frame, dur, beats }) => {
  const sinceBeat = Math.min(...beats.map((b) => (frame >= b ? frame - b : 9999)));
  if (fx === "blackhole") {
    // köşede dönen küçük kara delik; sahne biterken büyür ve her şeyi içine alır
    const grow = interpolate(frame, [dur - 30, dur + 1], [0, 1], clamp);
    const r = 70 + grow * 1500, cx = interpolate(grow, [0, 1], [1560, W / 2]), cy = interpolate(grow, [0, 1], [250, H / 2]);
    return (
      <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0, opacity: interpolate(frame, [dur + 1, dur + 12], [1, 0], clamp) }}>
        <g transform={`translate(${cx} ${cy})`}>
          <g transform={`rotate(${frame * 3})`}>
            <ellipse rx={r * 1.9} ry={r * 0.62} fill="none" stroke="#F2B544" strokeWidth={r * 0.2} opacity={0.85} />
            <ellipse rx={r * 2.4} ry={r * 0.8} fill="none" stroke="#E08A55" strokeWidth={r * 0.1} strokeDasharray={`${r * 0.6} ${r * 0.4}`} opacity={0.7} />
          </g>
          <circle r={r} fill="#0B0D1E" />
          <circle r={r * 1.06} fill="none" stroke="#FFE9B8" strokeWidth={r * 0.05} opacity={0.8} />
        </g>
      </svg>
    );
  }
  if (fx === "flash") {
    const o = sinceBeat < 10 ? [0.9, 0.2, 0.7, 0.1, 0.35, 0.1, 0, 0, 0, 0][sinceBeat] : 0;
    return (<>
      <div style={{ position: "absolute", inset: 0, background: "#fff", opacity: o * 0.7 }} />
      {sinceBeat < 9 && <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}><polyline points="1500,0 1430,260 1520,300 1410,560 1500,600 1400,860" fill="none" stroke="#FFE9B8" strokeWidth={14} strokeLinejoin="round" opacity={1 - sinceBeat / 9} /></svg>}
    </>);
  }
  if (fx === "meteor") {
    const t = (frame % 150) / 34;
    if (t > 1.25) return null;
    const x = 1900 - t * 1500, y = -60 + t * 760;
    return (
      <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
        {t <= 1 ? (<><line x1={x} y1={y} x2={x + 300} y2={y - 150} stroke="#F2B544" strokeWidth={26} strokeLinecap="round" opacity={0.6} /><line x1={x} y1={y} x2={x + 160} y2={y - 80} stroke="#E25D4E" strokeWidth={34} strokeLinecap="round" /><circle cx={x} cy={y} r={34} fill="#5E4330" /></>)
          : <circle cx={400} cy={700} r={(t - 1) * 1400} fill="none" stroke="#F2B544" strokeWidth={30} opacity={1 - (t - 1) * 4} />}
      </svg>
    );
  }
  if (fx === "erupt") {
    return (
      <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
        {Array.from({ length: 26 }, (_, i) => { const q = ((frame * (1 + rnd(i, 1) * 0.6) + i * 11) % 60) / 60, vx = (rnd(i, 2) - 0.5) * 520; return <circle key={i} cx={W / 2 + vx * q} cy={900 - Math.sin(q * Math.PI) * (360 + rnd(i, 3) * 260) + q * 120} r={8 + rnd(i, 4) * 14} fill={["#E25D4E", "#F2B544", "#E08A55"][i % 3]} opacity={1 - q} />; })}
      </svg>
    );
  }
  if (fx === "rain") {
    return (
      <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
        {Array.from({ length: 70 }, (_, i) => { const y = ((rnd(i, 2) * H + frame * (18 + rnd(i, 3) * 10)) % (H + 60)) - 30, x = rnd(i, 1) * W; return <line key={i} x1={x} y1={y} x2={x - 6} y2={y + 34} stroke="#4F75B3" strokeWidth={4} strokeLinecap="round" opacity={0.35} />; })}
      </svg>
    );
  }
  if (fx === "sparkle") {
    return (<>
      {Array.from({ length: 16 }, (_, i) => { const q = ((frame + i * 13) % 50) / 50; return <div key={i} style={{ position: "absolute", left: 200 + rnd(i, 1) * (W - 400), top: 120 + rnd(i, 2) * 620, fontSize: 30 + rnd(i, 3) * 40, opacity: Math.sin(q * Math.PI), transform: `scale(${0.5 + q}) rotate(${q * 90}deg)`, fontFamily: F.head }}>✨</div>; })}
    </>);
  }
  if (fx === "dig") {
    return <Actors actors={[{ kind: "dig", emoji: "⛏️", emoji2: "🦴" }]} t={frame} ground={830} mode="ambient" />;
  }
  return null; // "shake": kamera sarsıntısı SceneShell'de uygulanır
};
// Sarsıntı ve kara delik gibi efektlerin sahne dönüşümüne katkısı.
export const fxTransform = (fx: string | undefined, frame: number, dur: number, beats: number[]) => {
  if (fx === "shake") {
    const since = Math.min(...beats.map((b) => (frame >= b ? frame - b : 9999)));
    const k = since < 26 ? (1 - since / 26) : 0;
    return `translate(${Math.sin(frame * 2.3) * 16 * k}px, ${Math.cos(frame * 3.1) * 11 * k}px) rotate(${Math.sin(frame * 1.7) * 0.6 * k}deg)`;
  }
  if (fx === "blackhole") {
    const g = interpolate(frame, [dur - 24, dur + 6], [0, 1], clamp);
    return `scale(${1 - g * 0.85}) rotate(${g * 200}deg)`;
  }
  return "";
};
export const ink = (dark: boolean) => (dark ? "#FFFFFF" : C.dim);
