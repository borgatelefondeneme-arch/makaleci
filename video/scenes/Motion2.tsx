import React from "react";
import { interpolate, spring } from "remotion";
import { ACCENTS, C, F, FPS, GRADIENT } from "../theme";
import { beatAt, clamp, pop } from "../anim";
import { activeIndex, kick } from "../components/Motion";
import { SceneProps, Stage, Title } from "./common";

// ---------- Gün-gece kadranı ----------
export const Clock: React.FC<SceneProps<"clock">> = ({ visual, frame, beats, dur }) => {
  const R = 250, cx = 420, cy = 300;
  const turn = (frame / 300) * 360; // 10 saniyede bir tur
  const pt = (deg: number, r: number) => [cx + Math.sin((deg * Math.PI) / 180) * r, cy - Math.cos((deg * Math.PI) / 180) * r];
  const ang = (at: number) => ((at - 12) / 24) * 360; // öğle üstte, gece yarısı altta
  const act = activeIndex(beats, frame);
  return (
    <Stage>
      <Title frame={frame} color={C.gold}>{visual.title}</Title>
      <div style={{ position: "relative", width: 1480, height: 620 }}>
        <svg width={1480} height={620} style={{ position: "absolute", overflow: "visible" }}>
          <defs>
            <linearGradient id="dn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stopColor="#FFE9B8" /><stop offset="48%" stopColor="#FFD08A" /><stop offset="52%" stopColor="#5E78B8" /><stop offset="100%" stopColor="#27345E" /></linearGradient>
          </defs>
          <circle cx={cx} cy={cy} r={R + 26} fill="#fff" opacity={0.9} />
          <circle cx={cx} cy={cy} r={R} fill="url(#dn)" transform={`scale(${pop(frame, 4, 10)})`} style={{ transformOrigin: `${cx}px ${cy}px` }} />
          {Array.from({ length: 24 }, (_, i) => { const [x1, y1] = pt(i * 15, R - 8), [x2, y2] = pt(i * 15, R - (i % 6 ? 24 : 40)); return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#fff" strokeWidth={i % 6 ? 3 : 6} strokeLinecap="round" opacity={0.8} />; })}
          {/* yıldızlar gece yarısında kırpışır */}
          {[[-70, 120], [40, 170], [90, 95], [-20, 200]].map(([dx, dy], i) => <circle key={i} cx={cx + dx} cy={cy + dy} r={4 + 2 * Math.sin(frame / 7 + i * 2)} fill="#fff" opacity={0.85} />)}
          {/* akrep */}
          <g transform={`rotate(${turn} ${cx} ${cy})`}>
            <line x1={cx} y1={cy} x2={cx} y2={cy - R + 46} stroke={C.text} strokeWidth={10} strokeLinecap="round" />
            <circle cx={cx} cy={cy - R + 46} r={16} fill={C.coral} stroke="#fff" strokeWidth={5} />
          </g>
          <circle cx={cx} cy={cy} r={84} fill="#fff" stroke={C.text} strokeWidth={6} />
          <text x={cx} y={cy + 14} textAnchor="middle" fontFamily={F.head} fontWeight={800} fontSize={40} fill={C.text}>{visual.center}</text>
          {/* işaretler: kadrandan etikete çizgi */}
          {visual.markers.map((m, i) => {
            const s = beatAt(beats, i, dur, visual.markers.length), p = pop(frame, s, 10);
            const [mx, my] = pt(ang(m.at), R), ly = 70 + i * (460 / Math.max(1, visual.markers.length - 1 || 1));
            return (
              <g key={i} opacity={p}>
                <path d={`M ${mx} ${my} C ${mx + 160} ${my}, ${740} ${ly}, ${860} ${ly}`} fill="none" stroke={ACCENTS[i % 4]} strokeWidth={5} strokeDasharray="10 12" strokeDashoffset={-frame * 1.2} />
                <circle cx={mx} cy={my} r={16 + kick(frame, s, 16) * 14 + (act === i ? 3 * Math.sin(frame / 5) : 0)} fill={ACCENTS[i % 4]} stroke="#fff" strokeWidth={5} />
              </g>
            );
          })}
        </svg>
        <div style={{ position: "absolute", left: cx - 44, top: cy - R - 88, fontSize: 80, fontFamily: F.head, transform: `rotate(${frame * 0.6}deg)` }}>☀️</div>
        <div style={{ position: "absolute", left: cx - 40, top: cy + R + 6, fontSize: 72, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 20) * 12}deg)` }}>🌙</div>
        {visual.markers.map((m, i) => {
          const s = beatAt(beats, i, dur, visual.markers.length), p = pop(frame, s + 6, 10);
          const ly = 70 + i * (460 / Math.max(1, visual.markers.length - 1 || 1));
          const on = act === i;
          return (
            <div key={i} style={{ position: "absolute", left: 870, top: ly - 44, display: "flex", alignItems: "center", gap: 18, background: "#fff", border: `4px solid ${on ? ACCENTS[i % 4] : C.cardLine}`, borderRadius: 30, padding: "14px 28px", opacity: p, transform: `translateX(${(1 - p) * 60}px) scale(${on ? 1.05 : 1})`, boxShadow: `0 12px 30px ${C.shadow}` }}>
              {m.emoji && <span style={{ fontSize: 50, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 12 + i) * 10}deg)`, display: "inline-block" }}>{m.emoji}</span>}
              <span style={{ fontFamily: F.head, fontWeight: 800, fontSize: 38, color: C.text }}>{m.label}</span>
            </div>
          );
        })}
      </div>
      {visual.note && <div style={{ fontFamily: F.body, fontSize: 24, color: C.dim }}>{visual.note}</div>}
    </Stage>
  );
};

// ---------- Ortada simge, çevresinde beliren etiketler ----------
export const Spotlight: React.FC<SceneProps<"spotlight">> = ({ visual, frame, beats, dur }) => {
  const n = visual.chips.length, cx = 740, cy = 300;
  const act = activeIndex(beats, frame);
  const pos = visual.chips.map((_, i) => { const a = -Math.PI / 2 + ((i + 0.5) * 2 * Math.PI) / n + Math.sin(frame / 90) * 0.06; return [cx + Math.cos(a) * 520, cy + Math.sin(a) * 235]; });
  return (
    <Stage>
      <Title frame={frame} color={C.purple}>{visual.title}</Title>
      <div style={{ position: "relative", width: 1480, height: 620 }}>
        <svg width={1480} height={620} style={{ position: "absolute", overflow: "visible" }}>
          {[0, 1, 2].map((k) => { const t = ((frame + k * 30) % 90) / 90; return <circle key={k} cx={cx} cy={cy} r={120 + t * 150} fill="none" stroke={C.purple} strokeWidth={5} opacity={(1 - t) * 0.35} />; })}
          {visual.chips.map((_, i) => {
            const p = pop(frame, beatAt(beats, i, dur, n), 10);
            return <line key={i} x1={cx} y1={cy} x2={cx + (pos[i][0] - cx) * p} y2={cy + (pos[i][1] - cy) * p} stroke={ACCENTS[i % 4]} strokeWidth={5} strokeDasharray="4 14" strokeLinecap="round" strokeDashoffset={-frame} opacity={0.8} />;
          })}
        </svg>
        <div style={{ position: "absolute", left: cx - 130, top: cy - 130, width: 260, height: 260, borderRadius: "50%", background: "#fff", boxShadow: `0 20px 50px ${C.shadow}`, display: "flex", alignItems: "center", justifyContent: "center", transform: `scale(${pop(frame, 4, 8) * (1 + 0.04 * Math.sin(frame / 9))})` }}>
          <span style={{ fontSize: 160, lineHeight: 1, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 22) * 7}deg)`, display: "inline-block" }}>{visual.emoji}</span>
        </div>
        {visual.chips.map((c, i) => {
          const s = beatAt(beats, i, dur, n), p = pop(frame, s, 9), on = act === i || (act > n - 1 && i === n - 1);
          return (
            <div key={i} style={{ position: "absolute", left: pos[i][0], top: pos[i][1], transform: `translate(-50%, -50%) scale(${p * (on ? 1.08 : 1) + kick(frame, s, 16) * 0.12})`, opacity: p, background: on ? ACCENTS[i % 4] : "#fff", color: on ? "#fff" : C.text, border: `4px solid ${ACCENTS[i % 4]}`, borderRadius: 34, padding: "14px 28px", fontFamily: F.head, fontWeight: 800, fontSize: 36, whiteSpace: "nowrap", boxShadow: `0 12px 30px ${C.shadow}`, display: "flex", gap: 14, alignItems: "center" }}>
              {c.emoji && <span style={{ fontSize: 44 }}>{c.emoji}</span>}{c.label}
            </div>
          );
        })}
      </div>
    </Stage>
  );
};

// ---------- Evre çizgisi: sahne boyunca çizilir ----------
export const Stages: React.FC<SceneProps<"stages">> = ({ visual, frame, dur }) => {
  const AW = 1480, AH = 520, x0 = 330, x1 = AW - 30, top = 50, gap = (AH - 100) / (visual.rows.length - 1);
  const X = (i: number) => x0 + ((x1 - x0) * i) / (visual.path.length - 1), Y = (r: number) => top + r * gap;
  const prog = interpolate(frame, [18, Math.max(60, dur - 30)], [0, visual.path.length - 1], clamp);
  const seg = Math.min(visual.path.length - 2, Math.floor(prog)), t = prog - seg;
  // basamaklı yol: önce yatay, sonra dikey
  let d = `M ${X(0)} ${Y(visual.path[0])}`;
  for (let i = 1; i <= seg; i++) d += ` H ${X(i)} V ${Y(visual.path[i])}`;
  const hx = X(seg) + (X(seg + 1) - X(seg)) * Math.min(1, t * 2), hy = Y(visual.path[seg]) + (Y(visual.path[seg + 1]) - Y(visual.path[seg])) * Math.max(0, t * 2 - 1);
  d += ` H ${hx} V ${hy}`;
  const curRow = t < 0.5 ? visual.path[seg] : visual.path[seg + 1];
  return (
    <Stage>
      <Title frame={frame} color={C.teal}>{visual.title}</Title>
      <div style={{ position: "relative", width: AW, height: AH }}>
        <svg width={AW} height={AH} style={{ position: "absolute", overflow: "visible" }}>
          {visual.rows.map((r, i) => <line key={i} x1={x0 - 10} x2={x1} y1={Y(i)} y2={Y(i)} stroke={i === visual.highlightRow ? C.yellow : C.cardLine} strokeWidth={i === visual.highlightRow ? 5 : 3} strokeDasharray="4 14" strokeLinecap="round" />)}
          <path d={d} fill="none" stroke={C.teal} strokeWidth={9} strokeLinejoin="round" strokeLinecap="round" />
          <circle cx={hx} cy={hy} r={30 + 6 * Math.sin(frame / 4)} fill={C.coral} opacity={0.25} />
          <circle cx={hx} cy={hy} r={15} fill={C.coral} stroke="#fff" strokeWidth={5} />
        </svg>
        {visual.rows.map((r, i) => {
          const on = curRow === i;
          return (
            <div key={i} style={{ position: "absolute", left: 0, top: Y(i) - 36, width: 300, display: "flex", alignItems: "center", gap: 14, justifyContent: "flex-end", transform: `scale(${on ? 1.1 : 1})`, transformOrigin: "right center" }}>
              {r.emoji && <span style={{ fontSize: 46, fontFamily: F.head, transform: `rotate(${on ? Math.sin(frame / 5) * 12 : 0}deg)`, display: "inline-block" }}>{r.emoji}</span>}
              <span style={{ fontFamily: F.head, fontWeight: 800, fontSize: 34, color: on ? "#fff" : C.text, background: on ? (i === visual.highlightRow ? C.yellow : C.teal) : "#fff", border: `3px solid ${on ? "transparent" : C.cardLine}`, borderRadius: 24, padding: "8px 20px", whiteSpace: "nowrap" }}>{r.label}</span>
            </div>
          );
        })}
        {/* yükselen "z"ler */}
        {[0, 1, 2].map((k) => { const tt = ((frame + k * 25) % 75) / 75; return <div key={k} style={{ position: "absolute", left: hx + 20 + tt * 40, top: hy - 40 - tt * 90, fontFamily: F.head, fontWeight: 800, fontSize: 30 + tt * 26, color: C.purple, opacity: (1 - tt) * 0.8 }}>z</div>; })}
      </div>
      {visual.note && <div style={{ fontFamily: F.body, fontSize: 24, color: C.dim, marginTop: 8 }}>{visual.note}</div>}
    </Stage>
  );
};

// ---------- Dolup boşalan depo ----------
export const Meter: React.FC<SceneProps<"meter">> = ({ visual, frame, beats }) => {
  const n = visual.phases.length;
  // aşamalar cümlelere yayılır
  const act = Math.min(n - 1, Math.floor((activeIndex(beats, frame) * n) / Math.max(1, beats.length)));
  const since = beats.length ? frame - beats[Math.min(beats.length - 1, Math.ceil((act * beats.length) / n))] : frame;
  const prev = visual.phases[Math.max(0, act - 1)].level, cur = visual.phases[act].level;
  const k = act === 0 ? spring({ frame: frame - 6, fps: FPS, config: { damping: 20 } }) : spring({ frame: since, fps: FPS, config: { damping: 16, mass: 1.2 } });
  const level = act === 0 ? cur * k : prev + (cur - prev) * k;
  const TW = 360, TH = 500, tx = 150, ty = 40, hgt = (TH - 20) * level, wave = Math.sin(frame / 6) * 7;
  return (
    <Stage>
      <Title frame={frame} color={C.yellow}>{visual.title}</Title>
      <div style={{ position: "relative", width: 1480, height: 650 }}>
        <svg width={700} height={600} style={{ position: "absolute", overflow: "visible" }}>
          <clipPath id="tank"><rect x={tx} y={ty} width={TW} height={TH} rx={50} /></clipPath>
          <rect x={tx} y={ty} width={TW} height={TH} rx={50} fill="#fff" />
          <g clipPath="url(#tank)">
            <path d={`M ${tx} ${ty + TH - hgt + wave} Q ${tx + TW / 4} ${ty + TH - hgt - wave * 2} ${tx + TW / 2} ${ty + TH - hgt + wave} T ${tx + TW} ${ty + TH - hgt - wave} V ${ty + TH + 4} H ${tx} Z`} fill={C.yellow} opacity={0.92} />
            {Array.from({ length: 10 }, (_, i) => { const tt = ((frame * (1 + (i % 3) * 0.4) + i * 37) % 120) / 120; const by = ty + TH - tt * hgt; return hgt > 30 ? <circle key={i} cx={tx + 40 + ((i * 53) % (TW - 80)) + Math.sin(frame / 9 + i) * 8} cy={by} r={6 + (i % 4) * 3} fill="#fff" opacity={0.55 * (1 - tt)} /> : null; })}
          </g>
          <rect x={tx} y={ty} width={TW} height={TH} rx={50} fill="none" stroke={C.text} strokeWidth={9} />
          {[0.25, 0.5, 0.75].map((g) => <line key={g} x1={tx + TW - 46} x2={tx + TW - 12} y1={ty + TH - (TH - 20) * g} y2={ty + TH - (TH - 20) * g} stroke={C.text} strokeWidth={5} strokeLinecap="round" opacity={0.5} />)}
        </svg>
        {visual.emoji && <div style={{ position: "absolute", left: tx + TW / 2 - 60, top: ty + TH / 2 - 70, fontSize: 120, fontFamily: F.head, transform: `rotate(${Math.sin(frame / 14) * 8}deg) scale(${1 + 0.05 * Math.sin(frame / 7)})` }}>{visual.emoji}</div>}
        <div style={{ position: "absolute", left: tx - 30, top: ty + TH + 14, width: TW + 60, textAlign: "center", fontFamily: F.head, fontWeight: 800, fontSize: 36, backgroundImage: GRADIENT, WebkitBackgroundClip: "text", backgroundClip: "text", color: "transparent" }}>{visual.label}</div>
        <div style={{ position: "absolute", left: 660, top: 30, width: 800, display: "flex", flexDirection: "column", gap: 22 }}>
          {visual.phases.map((ph, i) => {
            const shown = i <= act, on = i === act, p = shown ? pop(frame, i === 0 ? 8 : frame - since, 10) : 0;
            return (
              <div key={i} style={{ display: "flex", alignItems: "center", gap: 20, background: on ? C.text : "#fff", color: on ? "#fff" : C.text, border: `4px solid ${on ? C.text : C.cardLine}`, borderRadius: 30, padding: "18px 30px", opacity: shown ? Math.max(0.001, Math.min(1, p * 2)) : 0.25, transform: `translateX(${shown ? (1 - p) * 60 : 0}px) scale(${on ? 1.04 : 1})`, transformOrigin: "left center", boxShadow: `0 12px 30px ${C.shadow}` }}>
                {ph.emoji && <span style={{ fontSize: 50, fontFamily: F.head }}>{ph.emoji}</span>}
                <span style={{ fontFamily: F.head, fontWeight: 800, fontSize: 38 }}>{ph.label}</span>
                <div style={{ marginLeft: "auto", width: 150, height: 18, borderRadius: 9, background: on ? "rgba(255,255,255,0.25)" : C.bg2 }}><div style={{ width: `${ph.level * 100}%`, height: "100%", borderRadius: 9, background: C.yellow }} /></div>
              </div>
            );
          })}
        </div>
      </div>
      {visual.note && <div style={{ fontFamily: F.body, fontSize: 24, color: C.dim, transform: "translateY(48px)" }}>{visual.note}</div>}
    </Stage>
  );
};
