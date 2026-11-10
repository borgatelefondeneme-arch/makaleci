// Piper: yerel, çevrimdışı Türkçe seslendirme (ElevenLabs anahtarı yokken).
// Kelime hizalaması vermez; bu yüzden satır satır sentezlenir (perLine) ve
// kelime damgaları satır süresine hece oranıyla dağıtılır.
import { execFileSync } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { syllables, words as split } from "../../lib/io.ts";
import { SAMPLE_RATE, type VoiceProvider } from "./types.ts";

export const piperModel = () => process.env.PIPER_MODEL || ".cache/piper/tr_TR-dfki-medium.onnx";
export const piperAvailable = () => existsSync(piperModel());

export const piper = (): VoiceProvider => ({
  name: "piper",
  perLine: true,
  async synthesize(text) {
    const dir = mkdtempSync(join(tmpdir(), "piper-"));
    const wav = join(dir, "a.wav"), raw = join(dir, "a.raw");
    try {
      execFileSync("python3", ["-m", "piper", "-m", piperModel(), "-f", wav, "--length-scale", process.env.PIPER_LENGTH_SCALE || "1.1" /* çocuklar için biraz yavaş ve net */, "--sentence-silence", "0.22"], { input: text, stdio: ["pipe", "ignore", "ignore"] });
      // Ortak biçim: 24 kHz mono 16 bit; baştaki/sondaki sessizlik kırpılır.
      execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", wav, "-af", "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse", "-ar", String(SAMPLE_RATE), "-ac", "1", "-f", "s16le", raw]);
      const buf = readFileSync(raw);
      const pcm = new Int16Array(buf.buffer, buf.byteOffset, Math.floor(buf.byteLength / 2)).slice();
      const dur = pcm.length / SAMPLE_RATE;
      const ws = split(text);
      // Noktalama duraklamaları da paya katılır.
      const weight = (w: string) => syllables(w) + (/[.!?…]$/.test(w) ? 2 : /[,;:]$/.test(w) ? 1 : 0);
      const total = ws.reduce((a, w) => a + weight(w), 0);
      let acc = 0;
      const words = ws.map((w) => {
        const start = (dur * acc) / total;
        const end = (dur * (acc + syllables(w))) / total;
        acc += weight(w);
        return { text: w, start, end };
      });
      return { pcm, words };
    } finally { rmSync(dir, { recursive: true, force: true }); }
  },
});
