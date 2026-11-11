import React from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, useCurrentFrame } from "remotion";
import type { EpisodeProps, Scene } from "../schemas/index";
import { Background } from "./components/Background";
import { Caption, CaptionCue, Chrome, chunkText, PreprintBadge } from "./components/Overlays";
import { SubscribeReminder } from "./components/Subscribe";
import { ensureFonts } from "./fonts";
import { CueAt, MascotLayer, Visit } from "./mascot/MascotLayer";
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
import { Song } from "./scenes/Song";
import { SourceCard } from "./scenes/SourceCard";
import { clamp } from "./anim";
import { XFADE } from "./theme";

ensureFonts();

// Sahne tipi → bileşen. Yeni tip eklemek: şemaya ekle, buraya kaydet.
const REGISTRY: { [K in Scene["visual"]["type"]]: React.FC<SceneProps<K>> } = {
  "hook": Hook, "source-card": SourceCard, "big-number": BigNumber, "bar-chart": BarChart, "line-chart": LineChart,
  "comparison": Comparison, "diagram": Diagram, "analogy": Analogy, "quote-card": QuoteCard, "bullets": Bullets, "song": Song, "outro": Outro,
};

// Yumuşak geçiş: sahne XFADE kare boyunca bir sonrakiyle bindirilir.
const SceneShell: React.FC<{ dur: number; last: boolean; children: (frame: number) => React.ReactNode }> = ({ dur, last, children }) => {
  const f = useCurrentFrame();
  const inP = interpolate(f, [5, XFADE + 4], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
  const outP = last ? 0 : interpolate(f, [dur - 2, dur + 7], [0, 1], clamp);
  return (
    <AbsoluteFill style={{ opacity: inP * (1 - outP), transform: `translateX(${(1 - inP) * 70 - outP * 70}px) scale(${1 - outP * 0.03})` }}>
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
  const fadeOut = interpolate(f, [voice.totalFrames - 15, voice.totalFrames - 1], [1, 0], clamp);
  const cur = plan.scenes.find((_, i) => f >= voice.scenes[i].startFrame && f < voice.scenes[i].startFrame + voice.scenes[i].durationFrames);
  return (
    <AbsoluteFill style={{ background: "#FBF8F3" }}>
      <AbsoluteFill style={{ opacity: fadeOut }}>
        <Background />
        <Sequence durationInFrames={voice.introFrames + XFADE} name="Açılış">
          <SceneShell dur={voice.introFrames} last={false}>{(fr) => <Intro frame={fr} data={data} />}</SceneShell>
        </Sequence>
        {plan.scenes.map((sc, i) => {
          const v = voice.scenes[i];
          const last = i === plan.scenes.length - 1;
          const Comp = REGISTRY[sc.visual.type] as React.FC<SceneProps<any>>;
          return (
            <Sequence key={sc.id} from={v.startFrame} durationInFrames={v.durationFrames + (last ? 0 : XFADE)} name={`${sc.id} · ${sc.visual.type}`}>
              <SceneShell dur={v.durationFrames} last={last}>
                {(fr) => <Comp visual={sc.visual} beats={v.lineStartFrames} dur={v.durationFrames} frame={fr} data={data} tail={last ? voice.outroTailFrames : 0} />}
              </SceneShell>
            </Sequence>
          );
        })}
        {f >= voice.introFrames && <Chrome episode={script.episodeNumber} total={voice.totalFrames} source={cur?.sourceNote} />}
        {paper.isPreprint && f >= voice.introFrames && <PreprintBadge />}
        <Sequence from={voice.reminder.startFrame} durationInFrames={voice.reminder.durationFrames} name="Abone ol hatırlatması">
          <ReminderAt dur={voice.reminder.durationFrames} />
        </Sequence>
        <MascotLayer cues={cues} visits={visits} amplitude={voice.amplitude} words={voice.words} />
        <Caption cues={captions} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const ReminderAt: React.FC<{ dur: number }> = ({ dur }) => <SubscribeReminder frame={useCurrentFrame()} dur={dur} />;
