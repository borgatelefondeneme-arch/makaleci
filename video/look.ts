// Bölümden bölüme değişen görünüm (kullanıcı kararı: videolar birbirinin kopyası gibi durmamalı).
// Sabit kalanlar: giriş/çıkış, köşede gezen Muma kafası, senaryo modeli ve sonda şarkı olması.
// Değişenler: arka plan deseni ve renk tonu, süzülen konu simgeleri, sahne giriş hareketleri,
// anahtar kelime etiketi, şarkı sahnesinin düzeni. Hepsi bölüm numarasından türetilir (aynı bölüm hep aynı görünür).
export type Look = {
  bg: number;        // arka plan deseni: 0 lekeler, 1 dalgalar, 2 nokta ızgarası, 3 ışınlar, 4 balonlar
  pastel: string[];  // dört pastel ton (açık ve sıcak tema içinde)
  motifs: string[];  // arka planda soluk süzülen konu simgeleri
  enterOffset: number; enterStep: number; // sahne giriş hareketlerinin sırası
  keyword: number;   // anahtar kelime etiketi: 0 geçişli hap, 1 beyaz kart, 2 lacivert eğik etiket
  song: number;      // şarkı düzeni: 0 sıra, 1 yörünge, 2 ikiye bölünmüş sahne, 3 dalga bandı
  cornerShift: number; // Muma kafasının köşe sırası kaydırması
};
const PASTELS = [
  ["#FFD9BF", "#CFE0FF", "#E3DBFF", "#FFE9B8"], // şeftali – gök – lila – limon
  ["#CDEFDD", "#CFE0FF", "#FFE9B8", "#FFD9BF"], // nane – gök – limon – şeftali
  ["#FFD3DC", "#E3DBFF", "#FFD9BF", "#CDEFDD"], // gül – lila – şeftali – nane
  ["#C9ECF5", "#CFE0FF", "#E3DBFF", "#FFE9B8"], // su – gök – lila – limon
  ["#FFE9B8", "#CDEFDD", "#FFD9BF", "#C9ECF5"], // limon – nane – şeftali – su
];
export const DEFAULT_LOOK: Look = { bg: 0, pastel: PASTELS[0], motifs: [], enterOffset: 0, enterStep: 1, keyword: 0, song: 0, cornerShift: 0 };
export const lookOf = (episode: number, motifs: string[] = []): Look => {
  const n = Math.max(1, episode);
  return {
    bg: n % 5, pastel: PASTELS[(n * 2 + 1) % 5], motifs: motifs.slice(0, 5),
    enterOffset: (n * 3) % 8, enterStep: [1, 3, 5, 7][n % 4], keyword: n % 3, song: (n + 1) % 4, cornerShift: (n * 3) % 8,
  };
};
