import React from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, useCurrentFrame } from "remotion";
import type { EpisodeProps, Scene } from "../schemas/index";
import { Background } from "./components/Background";
import { Caption, CaptionCue, Chrome, chunkText, PreprintBadge } from "./components/Overlays";
import { SubscribeReminder } from "./components/Subscribe";
import { ensureFonts } from "./fonts";
import { cornerCenter, cornerOf, CueAt, HeadLayer, MascotLayer, Visit } from "./mascot/MascotLayer";
import { Analogy } from "./scenes/Analogy";
import { BigNumber } from "./scenes/BigNumber";
import { Bullets, QuoteCard } from "./scenes/Cards";
import { BarChart, LineChart } from "./scenes/Charts";
import { Comparison } from "./scenes/Comparison";
import type { SceneProps } from "./scenes/common";
import { Diagram } from "./scenes/Diagram";
import { Hook } from "./scenes/Hook";
import { Intro } from "./scenes/Intro";
import { Outro } from "./scenes/Outro";
import { Clock, Meter, Spotlight, Stages } from "./scenes/Motion2";
import { Keyword, Stickers } from "./components/Motion";
import { Song } from "./scenes/Song";
import { SourceCard } from "./scenes/SourceCard";
import { clamp } from "./anim";
import { XFADE } from "./theme";
import { Look, lookOf } from "./look";

ensureFonts();

// Sahne tipi → bileşen. Yeni tip eklemek: şemaya ekle, buraya kaydet.
const REGISTRY: { [K in Scene["visual"]["type"]]: React.FC<SceneProps<K>> } = {
  "hook": Hook, "source-card": SourceCard, "big-number": BigNumber, "bar-chart": BarChart, "line-chart": LineChart,
  "comparison": Comparison, "diagram": Diagram, "analogy": Analogy, "quote-card": QuoteCard, "bullets": Bullets, "song": Song, "outro": Outro,
  "clock": Clock, "spotlight": Spotlight, "stages": Stages, "meter": Meter,
};

// Sahne kabuğu: geçişler sahneden sahneye değişir (kayma, yükselme, yakınlaşma); sahne boyunca kamera
// çok yavaş yaklaşır ve kayar, böylece hiçbir kare tamamen durağan kalmaz.
const SceneShell: React.FC<{ dur: number; last: boolean; index: number; camera: boolean; look?: Look; children: (frame: number) => React.ReactNode }> = ({ dur, last, index, camera, look, children }) => {
  const f = useCurrentFrame();
  const inP = interpolate(f, [5, XFADE + 6], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
  const outP = last ? 0 : interpolate(f, [dur - 2, dur + 7], [0, 1], clamp);
  // Giriş hareketi havuzu (8 tür); sırası bölümden bölüme değişir.
  const kind = look ? (look.enterOffset + index * look.enterStep) % 8 : index % 4;
  const q = 1 - inP;
  const enter = [
    `translateX(${q * 90}px)`, `translateY(${q * 70}px)`, `scale(${0.9 + 0.1 * inP})`, `translateX(${q * -90}px) rotate(${q * -1.5}deg)`,
    `scale(${1 + 0.12 * q})`, `translateY(${q * -70}px)`, `rotate(${q * 3}deg) scale(${0.94 + 0.06 * inP})`, `translateX(${q * 120}px) skewX(${q * -6}deg)`,
  ][kind];
  const t = Math.min(1, f / Math.max(1, dur));
  const cam = camera ? `scale(${1 + 0.035 * t}) translate(${(index % 2 ? -1 : 1) * 14 * t}px, ${-8 * t}px)` : "";
  return (
    <AbsoluteFill style={{ opacity: inP * (1 - outP), transform: `${enter} translateX(${-outP * 70}px) scale(${1 - outP * 0.03}) ${cam}`, transformOrigin: index % 2 ? "30% 45%" : "70% 45%" }}>
      {children(f)}
    </AbsoluteFill>
  );
};

export const Episode: React.FC<EpisodeProps> = (data) => {
  const { plan, voice, script, paper } = data;
  const lineById = new Map(script.sections.flatMap((s) => s.lines).map((l) => [l.id, l]));
  const f = useCurrentFrame();

  const cues: CueAt[] = [{ startFrame: 0, cue: { state: "talk", x: 0.16, y: 0.5, scale: 1.45, pose: "wave" } }];
  const captions: CaptionCue[] = [];
  plan.scenes.forEach((sc, i) => {
    const v = voice.scenes[i];
    sc.lineIds.forEach((id, k) => {
      const text = lineById.get(id)!.display;
      const s = v.startFrame + v.lineStartFrames[k], e = v.startFrame + v.lineEndFrames[k];
      const parts = chunkText(text);
      const total = parts.reduce((a, p) => a + p.length, 0);
      let acc = 0;
      parts.forEach((p) => {
        const a = s + ((e - s) * acc) / total; acc += p.length;
        captions.push({ start: Math.round(a), end: Math.round(s + ((e - s) * acc) / total) + (acc === total ? 6 : 0), text: p });
      });
    });
  });
  for (const b of voice.bumpers) captions.push({ start: b.startFrame, end: b.endFrame, text: b.text });
  // Muma yalnızca girişte ve çıkışta görünür: açılışta uçarak gelir, karşılar ve gider; kapanış sahnesinde geri gelir.
  const lastV = voice.scenes[voice.scenes.length - 1];
  const tailStart = lastV.startFrame + lastV.durationFrames - voice.outroTailFrames;
  const lastScene = plan.scenes[plan.scenes.length - 1];
  cues.push({ startFrame: lastV.startFrame - 4, cue: { ...lastScene.mascot, pose: lastScene.mascot.pose ?? "thumbs" } });
  cues.push({ startFrame: tailStart, cue: { state: "talk", x: 0.14, y: 0.5, scale: 1.4, pose: "wave" } });
  const visits: Visit[] = [{ start: 0, end: voice.introFrames + 8, outFrames: 34 }, { start: lastV.startFrame - 4, end: voice.totalFrames - 12, outFrames: 60 }];
  // Ara sahnelerde yalnızca kafa görünür: açılıştan sonra belirir, şarkıdan (yoksa kapanıştan) önce çekilir.
  const shift = lookOf(script.episodeNumber).cornerShift;
  const headOn = (i: number) => i < plan.scenes.length - 1 && plan.scenes[i].visual.type !== "song";
  const headScenes = plan.scenes.map((_, i) => ({ startFrame: voice.scenes[i].startFrame, corner: cornerOf(i + shift) })).filter((_, i) => headOn(i));
  const headTo = voice.song ? voice.scenes.find((x) => x.sceneId === voice.song!.sceneId)!.startFrame + voice.scenes.find((x) => x.sceneId === voice.song!.sceneId)!.lineEndFrames.slice(-1)[0] : lastV.startFrame - 8;
  const fadeOut = interpolate(f, [voice.totalFrames - 15, voice.totalFrames - 1], [1, 0], clamp);
  const look = lookOf(script.episodeNumber, script.song?.cast.map((c) => c.emoji) ?? plan.scenes[0]?.stickers ?? []);
  const cur = plan.scenes.find((_, i) => f >= voice.scenes[i].startFrame && f < voice.scenes[i].startFrame + voice.scenes[i].durationFrames);
  return (
    <AbsoluteFill style={{ background: "#FBF8F3" }}>
      <AbsoluteFill style={{ opacity: fadeOut }}>
        <Background look={look} />
        <Sequence durationInFrames={voice.introFrames + XFADE} name="Açılış">
          <SceneShell dur={voice.introFrames} last={false} index={0} camera={false}>{(fr) => <Intro frame={fr} data={data} />}</SceneShell>
        </Sequence>
        {plan.scenes.map((sc, i) => {
          const v = voice.scenes[i];
          const last = i === plan.scenes.length - 1;
          const Comp = REGISTRY[sc.visual.type] as React.FC<SceneProps<any>>;
          return (
            <Sequence key={sc.id} from={v.startFrame} durationInFrames={v.durationFrames + (last ? 0 : XFADE)} name={`${sc.id} · ${sc.visual.type}`}>
              <SceneShell dur={v.durationFrames} last={last} index={i} look={look} camera={!last && sc.visual.type !== "song"}>
                {(fr) => (<>
                  {sc.stickers?.length ? <Stickers items={sc.stickers} frame={fr} beats={v.lineStartFrames} avoid={headOn(i) ? cornerCenter(cornerOf(i + shift)) : undefined} /> : null}
                  <Comp visual={sc.visual} beats={v.lineStartFrames} dur={v.durationFrames} frame={fr} data={data} tail={last ? voice.outroTailFrames : 0} />
                  {sc.keywords?.length ? <Keyword words={sc.keywords} beats={v.lineStartFrames} ends={v.lineEndFrames} frame={fr} variant={look.keyword} /> : null}
                </>)}
              </SceneShell>
            </Sequence>
          );
        })}
        {f >= voice.introFrames && <Chrome episode={script.episodeNumber} total={voice.totalFrames} />}
        {paper.isPreprint && f >= voice.introFrames && <PreprintBadge />}
        <Sequence from={voice.reminder.startFrame} durationInFrames={voice.reminder.durationFrames} name="Abone ol hatırlatması">
          <ReminderAt dur={voice.reminder.durationFrames} />
        </Sequence>
        <HeadLayer scenes={headScenes} from={voice.introFrames + 6} to={headTo} amplitude={voice.amplitude} words={voice.words} />
        <MascotLayer cues={cues} visits={visits} amplitude={voice.amplitude} words={voice.words} />
        <Caption cues={captions} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const ReminderAt: React.FC<{ dur: number }> = ({ dur }) => <SubscribeReminder frame={useCurrentFrame()} dur={dur} />;
