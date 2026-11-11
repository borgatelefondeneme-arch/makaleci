// Fontlar npm paketlerinden gömülür; render sırasında ağ gerekmez. Manrope: sitenin yazı tipi.
import "@fontsource/manrope/latin-500.css";
import "@fontsource/manrope/latin-700.css";
import "@fontsource/manrope/latin-800.css";
import "@fontsource/manrope/latin-ext-500.css";
import "@fontsource/manrope/latin-ext-700.css";
import "@fontsource/manrope/latin-ext-800.css";
import "@fontsource/noto-color-emoji/emoji.css";
import { continueRender, delayRender } from "remotion";

const SAMPLE = "ğüşıöçĞÜŞİÖÇ abc 123";
let started = false;
export const ensureFonts = () => {
  if (started || typeof document === "undefined") return;
  started = true;
  const handle = delayRender("fontlar yükleniyor");
  Promise.all([
    ...["500 40px Manrope", "700 40px Manrope", "800 40px Manrope"].map((s) => document.fonts.load(s, SAMPLE)),
    document.fonts.load("40px 'Noto Color Emoji'", "🔬✅🔔👍❓"),
  ])
    .then(() => document.fonts.ready)
    .then(() => continueRender(handle))
    .catch(() => continueRender(handle));
};
