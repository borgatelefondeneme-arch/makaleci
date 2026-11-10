import React from "react";
import { Composition, Still } from "remotion";
import { EpisodeProps } from "../schemas/index";
import { Episode } from "./Episode";
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
    <Still id="Thumbnail" component={Thumbnail} width={W} height={H} defaultProps={demo as unknown as EpisodeProps} />
  </>
);
