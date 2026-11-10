export const SAMPLE_RATE = 24000; // 16 bit mono PCM
export type Synth = { pcm: Int16Array; words: { text: string; start: number; end: number }[] };
export type VoiceProvider = { name: "mock" | "piper" | "elevenlabs"; perLine?: boolean; synthesize(text: string, previousText?: string): Promise<Synth> };
