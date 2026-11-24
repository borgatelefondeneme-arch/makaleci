import React from "react";
import { Composition, Still } from "remotion";
import { EpisodeProps } from "../schemas/index";
import { Episode } from "./Episode";
import { Short, SHORT_SIZE, ShortProps } from "./Short";
import { Thumbnail } from "./Thumbnail";
import { FPS, H, W } from "./theme";
import demo from "./demo-props.json";

// Girdi props'u render aşamasından gelir; stüdyoda demo verisi kullanılır.
export const Root: React.FC = () => (
  <>
    <Composition
      id="Episode" component={Episode} width={W} height={H} fps={FPS} durationInFrames={300}
      defaultProps={demo as unknown as EpisodeProps}
      calculateMetadata={({ props }) => ({ durationInFrames: EpisodeProps.parse(props).voice.totalFrames })}
    />
    <Composition
      id="Short" component={Short as unknown as React.FC<Record<string, unknown>>} {...SHORT_SIZE} fps={FPS} durationInFrames={300}
      defaultProps={{ ...(demo as object), short: { from: 0, to: 300, headline: "Örnek *başlık*" } }}
      calculateMetadata={({ props }) => { const s = (props as unknown as ShortProps).short; return { durationInFrames: Math.max(1, s.to - s.from + (s.pause?.len ?? 0)) }; }}
    />
    <Still id="Thumbnail" component={Thumbnail} width={W} height={H} defaultProps={demo as unknown as EpisodeProps} />
  </>
);
