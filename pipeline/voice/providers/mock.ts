// Mock ses: sessiz PCM + hece sayısından tahmin edilen kelime zaman damgaları.
// Hız, Türkçe anlatım için ~150 kelime/dk'ya ayarlıdır; gerçek seste ±%15 sapma beklenir.
import { syllables, words as split } from "../../lib/io.ts";
import { SAMPLE_RATE, type VoiceProvider } from "./types.ts";

const SYLLABLE = 0.132, GAP = 0.035, COMMA = 0.2, STOP = 0.4;

export const mock: VoiceProvider = {
  name: "mock",
  async synthesize(text) {
    let t = 0.05;
    const words = split(text).map((w) => {
      const start = t;
      t += Math.max(0.14, syllables(w) * SYLLABLE);
      const end = t;
      t += /[.!?…]["')]?$/.test(w) ? STOP : /[,;:—–]$/.test(w) ? COMMA : GAP;
      return { text: w, start, end };
    });
    return { pcm: new Int16Array(Math.ceil(t * SAMPLE_RATE)), words };
  },
};
