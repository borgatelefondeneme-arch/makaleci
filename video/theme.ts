// Tek stil kaynağı: palet, font, ölçüler.
export const C = {
  bg: "#0E1730",
  bg2: "#172349",
  card: "#1D2B57",
  cardLine: "#2E3F78",
  text: "#F5F7FF",
  dim: "#A9B4DA",
  teal: "#2EC4B6",
  yellow: "#FFD23F",
  coral: "#FF6B6B",
  purple: "#9B8CFF",
  ink: "#141E3F", // karakter konturu
};
export const ACCENTS = [C.teal, C.yellow, C.coral, C.purple];
export const EMOJI = "'Noto Color Emoji'";
export const F = {
  head: `Nunito, ${EMOJI}, sans-serif`,
  body: `Inter, ${EMOJI}, sans-serif`,
};
export const W = 1920;
export const H = 1080;
export const FPS = 30;
export const XFADE = 12; // sahne geçiş bindirmesi (kare)
// İçerik güvenli alanı (altta altyazı bandı var)
export const SAFE = { left: 110, right: 110, top: 96, bottom: 270 };
