// Tek stil kaynağı: palet, font, ölçüler.
// Palet kullanıcının sitesinden (mumaapp-panel.web.app/tanitim) alındı: krem zemin, lacivert yazı,
// kiremit → turuncu → mavi geçişli vurgu. Anahtar adları eski temadan kaldı; anlamları:
export const C = {
  bg: "#FBF8F3", // krem zemin
  bg2: "#F4EFE7",
  card: "#FFFFFF",
  cardLine: "#E8DFD2",
  text: "#1B2238", // lacivert yazı
  dim: "#5C6478",
  teal: "#4F75B3", // birincil vurgu: mavi
  yellow: "#D9713A", // vurgu yazısı: turuncu (krem zeminde okunur)
  coral: "#E25D4E", // uyarı / abone ol
  purple: "#7B6BD6", // lavanta
  green: "#17855A",
  gold: "#F2B544",
  ink: "#FFFFFF", // vurgu rengi üstündeki yazı ve çizgiler
  shadow: "rgba(27,34,56,0.12)",
};
export const GRADIENT = "linear-gradient(100deg, #B4562A, #E08A55 50%, #4F75B3)"; // sitenin başlık geçişi
export const ACCENTS = [C.teal, C.yellow, C.green, C.purple];
export const EMOJI = "'Noto Color Emoji'";
export const F = {
  head: `Manrope, ${EMOJI}, sans-serif`,
  body: `Manrope, ${EMOJI}, sans-serif`,
};
export const W = 1920;
export const H = 1080;
export const FPS = 30;
export const XFADE = 12; // sahne geçiş bindirmesi (kare)
// İçerik güvenli alanı (altta altyazı bandı var). Ara sahnelerde karakter olmadığı için içerik ortalanır.
export const SAFE = { left: 220, right: 220, top: 96, bottom: 270 };
