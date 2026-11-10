// Fontlar npm paketlerinden gömülür; render sırasında ağ gerekmez.
import "@fontsource/nunito/latin-600.css";
import "@fontsource/nunito/latin-800.css";
import "@fontsource/nunito/latin-900.css";
import "@fontsource/nunito/latin-ext-600.css";
import "@fontsource/nunito/latin-ext-800.css";
import "@fontsource/nunito/latin-ext-900.css";
import "@fontsource/inter/latin-400.css";
import "@fontsource/inter/latin-600.css";
import "@fontsource/inter/latin-700.css";
import "@fontsource/inter/latin-ext-400.css";
import "@fontsource/inter/latin-ext-600.css";
import "@fontsource/inter/latin-ext-700.css";
import "@fontsource/noto-color-emoji/emoji.css";
import { continueRender, delayRender } from "remotion";

const SAMPLE = "ğüşıöçĞÜŞİÖÇ abc 123";
let started = false;
export const ensureFonts = () => {
  if (started || typeof document === "undefined") return;
  started = true;
  const handle = delayRender("fontlar yükleniyor");
  const specs = [
    "600 40px Nunito", "800 40px Nunito", "900 40px Nunito",
    "400 40px Inter", "600 40px Inter", "700 40px Inter",
  ];
  Promise.all([
    ...specs.map((s) => document.fonts.load(s, SAMPLE)),
    document.fonts.load("40px 'Noto Color Emoji'", "🔬✅🔔👍❓"),
  ])
    .then(() => document.fonts.ready)
    .then(() => continueRender(handle))
    .catch(() => continueRender(handle));
};
