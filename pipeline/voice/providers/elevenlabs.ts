// ElevenLabs: karakter düzeyinde zaman damgalı sentez → kelime damgaları.
// Not: bu sağlayıcı anahtar olmadan test edilemedi; ilk gerçek çalıştırmada doğrulanmalı.
import { SAMPLE_RATE, type VoiceProvider } from "./types.ts";

type Alignment = { characters: string[]; character_start_times_seconds: number[]; character_end_times_seconds: number[] };

export const elevenlabs = (apiKey: string, voiceId: string, modelId: string): VoiceProvider => ({
  name: "elevenlabs",
  async synthesize(text, previousText) {
    const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}/with-timestamps?output_format=pcm_${SAMPLE_RATE}`;
    let lastErr = "";
    for (let attempt = 0; attempt < 4; attempt++) {
      const res = await fetch(url, {
        method: "POST",
        headers: { "xi-api-key": apiKey, "content-type": "application/json" },
        body: JSON.stringify({ text, model_id: modelId, language_code: "tr", previous_text: previousText, voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
      });
      if (res.ok) {
        const data = (await res.json()) as { audio_base64: string; alignment: Alignment };
        const buf = Buffer.from(data.audio_base64, "base64");
        const pcm = new Int16Array(buf.buffer, buf.byteOffset, Math.floor(buf.byteLength / 2)).slice();
        return { pcm, words: toWords(data.alignment) };
      }
      lastErr = `${res.status} ${await res.text()}`;
      if (![429, 500, 502, 503].includes(res.status)) break;
      await new Promise((r) => setTimeout(r, 2000 * 2 ** attempt));
    }
    throw new Error(`ElevenLabs isteği başarısız: ${lastErr}`);
  },
});

const toWords = (a: Alignment) => {
  const out: { text: string; start: number; end: number }[] = [];
  let cur = "", start = 0, end = 0;
  a.characters.forEach((ch, i) => {
    if (/\s/.test(ch)) { if (cur) out.push({ text: cur, start, end }); cur = ""; return; }
    if (!cur) start = a.character_start_times_seconds[i];
    cur += ch; end = a.character_end_times_seconds[i];
  });
  if (cur) out.push({ text: cur, start, end });
  return out;
};
