// Aşamalar arası tek sözleşme. Her JSON dosyası buradaki bir şemaya uyar.
import { z } from "zod";

// ---------- episode.json ----------
export const EpisodeMeta = z.object({ id: z.string(), episodeNumber: z.number().int(), sourceUrl: z.string().nullable(), createdAt: z.string() });
export type EpisodeMeta = z.infer<typeof EpisodeMeta>;

// ---------- 01_paper.json ----------
export const Paper = z.object({
  // "paper": bilimsel makale bölümü; "topic": çocukların merak ettiği bir soru (makalesiz konu bölümü).
  kind: z.enum(["paper", "topic"]).default("paper"),
  id: z.string(),
  title: z.string(),
  abstract: z.string(),
  authors: z.array(z.object({ name: z.string(), affiliations: z.array(z.string()) })),
  institutions: z.array(z.string()),
  venue: z.string().nullable(), // dergi / preprint sunucusu
  doi: z.string().nullable(),
  url: z.string(),
  fullTextUrl: z.string().nullable(),
  license: z.string().nullable(),
  publishedAt: z.string().nullable(),
  isPreprint: z.boolean(),
  peerReviewStatus: z.enum(["peer_reviewed", "preprint", "unknown"]),
  categories: z.array(z.string()),
  sources: z.array(z.string()), // hangi API'lerden geldi
  fetchedAt: z.string(),
});
export type Paper = z.infer<typeof Paper>;

// ---------- data/queue/*.json, 02_selection.json ----------
export const Selection = z.object({
  paperId: z.string(),
  paper: Paper,
  score: z.number().min(0).max(100),
  criteria: z.object({
    surprise: z.number(), // şaşırtıcılık
    explainable: z.number(), // 12 yaşa anlatılabilirlik
    visual: z.number(), // görselleştirilebilirlik
    concrete: z.number(), // somut sayı içerme
  }),
  rationale: z.string(),
  status: z.enum(["pending", "approved", "rejected"]),
  queuedAt: z.string(),
  decidedAt: z.string().nullable(),
});
export type Selection = z.infer<typeof Selection>;

// ---------- 03_facts.json ----------
export const Fact = z.object({
  id: z.string(), // f1, f2 ...
  kind: z.enum(["number", "claim", "meta"]),
  statement: z.string(), // Türkçe, sade
  // Bu olguya ait, senaryoda geçebilecek sayılar — makalede yazıldığı gibi.
  numbers: z.array(z.string()),
  quote: z.string(), // makaleden birebir alıntı (kaynak dilinde)
  location: z.string(), // "Özet", "Bölüm 3" ...
});
export const Facts = z.object({
  paperId: z.string(),
  basis: z.enum(["full_text", "abstract_only"]),
  // API'ler kurum vermediyse (ör. arXiv) makale metninden çıkarılan kurumlar.
  institutions: z.array(z.string()),
  // Konu bölümlerinde olguların dayandığı kaynaklar (ekranda ve yayin.md'de gösterilir).
  sources: z.array(z.object({ id: z.string(), title: z.string(), publisher: z.string(), url: z.string() })).default([]),
  facts: z.array(Fact),
});
export type Fact = z.infer<typeof Fact>;
export type Facts = z.infer<typeof Facts>;

// ---------- 03_script.json ----------
export const SectionId = z.enum([
  "hook", "context", "method", "finding", "importance", "limitations", "summary",
]);
export type SectionId = z.infer<typeof SectionId>;

export const Line = z.object({
  id: z.string(), // l1, l2 ...
  display: z.string(), // ekranda (altyazı) görünen metin
  spoken: z.string(), // seslendirilen metin (sayılar/adlar okunuşla)
  factIds: z.array(z.string()),
});
export type Line = z.infer<typeof Line>;

// --- Konuya özel sahneleme (kullanıcı kararı: görseller konuya göre kurulur) ---
// Arka plan dünyası: konu neredeyse orası (uzay, yer altı, çayır, okyanus, fırtına).
export const Backdrop = z.enum(["space", "underground", "meadow", "ocean", "storm", "mouth", "aurora", "sky", "micro", "snow"]);
// Sahnede hareket eden konu karakteri (emoji). kind: yürür, uçar, kovalar (emoji2 kaçar), yüzer, kazar, zıplar, döner, sürü.
export const Actor = z.object({
  kind: z.enum(["walk", "fly", "chase", "swim", "dig", "hop", "orbit", "swarm"]),
  emoji: z.string(), emoji2: z.string().optional(),
  size: z.number().optional(), // piksel; verilmezse yere göre seçilir
  every: z.number().optional(), // geçişler arası süre (sn); ortam karakterleri için
  facesRight: z.boolean().optional(), // emoji sağa bakıyorsa true (çoğu sola bakar)
});
export type Actor = z.infer<typeof Actor>;
// Sahneye özel efekt: kara deliğin sahneyi içine çekmesi, sarsıntı, şimşek, göktaşı, kazı, püskürme, yağmur, pırıltı.
export const SceneFx = z.enum(["blackhole", "shake", "flash", "meteor", "dig", "erupt", "rain", "sparkle"]);

export const Script = z.object({
  paperId: z.string(),
  episodeNumber: z.number().int(),
  videoTitle: z.string(),
  paperTitleTr: z.string(), // makale başlığının Türkçesi (açılışta)
  sections: z.array(z.object({ id: SectionId, lines: z.array(Line) })),
  takeaways: z.array(z.string()).length(3),
  nextTeaser: z.string(),
  // Konuya özel dünya: arka plan + ortamda gezen karakterler. Verilmezse bölüm numarasından türeyen desen kullanılır.
  theme: z.object({ backdrop: Backdrop, actors: z.array(Actor).max(6).default([]) }).optional(),
  // Kapanış şarkısı (isteğe bağlı): sözler yalnızca bölümün olgularına dayanır.
  song: z.object({
    title: z.string(),
    style: z.array(z.string()).min(1), // İngilizce tarz tarifleri; sanatçı/eser adı içeremez
    negativeStyle: z.array(z.string()).default([]),
    // Şarkıda dans eden, konuya özel karakterler (emoji). Muma şarkı sahnesinde görünmez.
    cast: z.array(z.object({ emoji: z.string(), name: z.string() })).min(2).max(6),
    // Şarkı sahnesinin gösterisi: konunun karakterleri hareket eder (kovalar, uçar, zıplar). Verilirse rozet sırası yerine bu oynar.
    show: z.array(Actor).max(6).optional(),
    sections: z.array(z.object({
      tag: z.string(), // müzik modeline giden bölüm adı: "Intro", "Verse 1", "Chorus" ...
      label: z.string(), // ekranda görünen Türkçe ad: "Nakarat" ...
      direction: z.string().optional(), // çalgı yönergesi (İngilizce), ör. "snare drum roll"
      lines: z.array(z.string()).min(1),
      durationMs: z.number().int().min(3000).max(120000),
    })).min(1).max(30),
  }).optional(),
  description: z.string(), // yayin.md için kısa açıklama
  // Videoda geçen, çocukların bilmeyebileceği kelimeler; yayin.md'deki "Sözlük" bölümüne yazılır.
  glossary: z.array(z.object({ term: z.string(), meaning: z.string() })).default([]),
});
export type Script = z.infer<typeof Script>;

// ---------- 04_scenes.json ----------
const Item = z.object({ label: z.string(), value: z.number(), display: z.string(), highlight: z.boolean().optional() });

export const Visual = z.discriminatedUnion("type", [
  z.object({ type: z.literal("hook"), question: z.string(), emoji: z.string().optional() }),
  z.object({ type: z.literal("source-card"), note: z.string().optional() }),
  z.object({ type: z.literal("big-number"), value: z.string(), unit: z.string().optional(), label: z.string(), sub: z.string().optional(), icon: z.string().optional() }),
  // --- hareketli anlatım tipleri (her cümlede ekranda bir şey değişir) ---
  // Gün-gece kadranı: akrep sürekli döner; işaretler cümlelerle belirir. Saat rakamı yazılmaz (konum şematiktir).
  z.object({ type: z.literal("clock"), title: z.string(), center: z.string(), markers: z.array(z.object({ at: z.number().min(0).max(24), label: z.string(), emoji: z.string().optional() })).max(5), note: z.string().optional() }),
  // Ortada büyük bir simge, çevresinde cümlelerle beliren etiketler.
  z.object({ type: z.literal("spotlight"), title: z.string(), emoji: z.string(), chips: z.array(z.object({ label: z.string(), emoji: z.string().optional() })).min(2).max(6) }),
  // Evre çizgisi (ör. uyku evreleri): satırlar arasında gezen çizgi sahne boyunca çizilir. Şematiktir.
  z.object({ type: z.literal("stages"), title: z.string(), rows: z.array(z.object({ label: z.string(), emoji: z.string().optional() })).min(2).max(5), path: z.array(z.number().int().min(0)).min(3).max(40), highlightRow: z.number().int().optional(), note: z.string().optional() }),
  // Dolup boşalan depo: düzey, o an anlatılan aşamaya göre değişir.
  z.object({ type: z.literal("meter"), title: z.string(), label: z.string(), emoji: z.string().optional(), phases: z.array(z.object({ label: z.string(), level: z.number().min(0).max(1), emoji: z.string().optional() })).min(2).max(5), note: z.string().optional() }),
  z.object({ type: z.literal("bar-chart"), title: z.string(), unit: z.string().optional(), bars: z.array(Item).min(2).max(6) }),
  z.object({ type: z.literal("line-chart"), title: z.string(), xLabel: z.string(), yLabel: z.string(), points: z.array(Item).min(2).max(12) }),
  z.object({
    type: z.literal("comparison"), title: z.string(),
    left: z.object({ title: z.string(), value: z.string().optional(), items: z.array(z.string()) }),
    right: z.object({ title: z.string(), value: z.string().optional(), items: z.array(z.string()) }),
  }),
  z.object({ type: z.literal("diagram"), title: z.string(), layout: z.enum(["flow", "cycle"]), nodes: z.array(z.object({ label: z.string(), emoji: z.string().optional() })).min(2).max(5) }),
  z.object({
    type: z.literal("analogy"), template: z.enum(["scale", "fill", "race", "zoom"]), title: z.string(),
    a: z.object({ label: z.string(), value: z.number(), display: z.string().optional() }),
    b: z.object({ label: z.string(), value: z.number(), display: z.string().optional() }),
    caption: z.string(),
  }),
  z.object({ type: z.literal("quote-card"), quote: z.string(), attribution: z.string() }),
  z.object({ type: z.literal("bullets"), title: z.string(), items: z.array(z.string()).min(1).max(4), tone: z.enum(["neutral", "caution"]).optional() }),
  z.object({ type: z.literal("song") }), // kapanış şarkısı: sözler ve zamanlama 05_song.json'dan gelir
  z.object({ type: z.literal("outro") }),
]);
export type Visual = z.infer<typeof Visual>;
export type VisualOf<T extends Visual["type"]> = Extract<Visual, { type: T }>;

export const MascotCue = z.object({
  state: z.enum(["idle", "talk", "point", "think"]),
  x: z.number().min(0).max(1), // ekranın oranı (merkez)
  y: z.number().min(0).max(1),
  scale: z.number().min(0.3).max(2.5),
  // point durumunda işaret edilen ekran noktası (oran)
  pointAt: z.object({ x: z.number(), y: z.number() }).optional(),
  // Poz seçimi (isteğe bağlı). Verilmezse durumdan türetilir: talk/point → point, idle/think → crossed.
  pose: z.enum(["point", "crossed", "thumbs", "book", "wave"]).optional(),
});
export type MascotCue = z.infer<typeof MascotCue>;

export const Scene = z.object({
  id: z.string(), // s1, s2 ...
  section: SectionId,
  lineIds: z.array(z.string()).min(1),
  visual: Visual,
  mascot: MascotCue,
  factIds: z.array(z.string()),
  sourceNote: z.string().optional(), // sahne dipnotu ("Kaynak: Tablo 2")
  // Sahne kenarlarında süzülen, cümle başlarında zıplayan konu simgeleri (emoji).
  stickers: z.array(z.string()).max(6).optional(),
  // Sahneye özel efekt (konuya göre): bkz. SceneFx.
  fx: SceneFx.optional(),
  // Satır başına ekranda büyük beliren anahtar kelime (lineIds ile aynı sırada; yoksa boş dize).
  keywords: z.array(z.string()).optional(),
});
export type Scene = z.infer<typeof Scene>;
export const ScenePlan = z.object({ paperId: z.string(), scenes: z.array(Scene) });
export type ScenePlan = z.infer<typeof ScenePlan>;

// ---------- 05_song.json ----------
const SongLine = z.object({ text: z.string(), start: z.number(), end: z.number() }); // saniye, şarkı başına göre
export const Song = z.object({
  provider: z.enum(["mock", "elevenlabs"]),
  model: z.string().nullable(),
  audioFile: z.string(), // bölüm klasörüne göre
  durationSec: z.number(),
  title: z.string(),
  // Satır zamanları bölüm sürelerinden oransal hesaplanır (yaklaşık eşleme).
  sections: z.array(z.object({ label: z.string(), start: z.number(), end: z.number(), lines: z.array(SongLine) })),
});
export type Song = z.infer<typeof Song>;

// ---------- 05_voice.json ----------
export const Word = z.object({ text: z.string(), start: z.number(), end: z.number() });
export const VoiceScene = z.object({
  sceneId: z.string(),
  startFrame: z.number().int(),
  durationFrames: z.number().int(),
  audioStartFrame: z.number().int(), // sahne içinde sesin başladığı kare
  lineStartFrames: z.array(z.number().int()), // sahneye göre
  lineEndFrames: z.array(z.number().int()),
});
export const Voice = z.object({
  provider: z.enum(["mock", "piper", "elevenlabs"]),
  fps: z.number(),
  introFrames: z.number().int(),
  outroTailFrames: z.number().int(),
  totalFrames: z.number().int(),
  durationSec: z.number(),
  wordCount: z.number().int(),
  audioFile: z.string(), // bölüm klasörüne göre
  scenes: z.array(VoiceScene),
  words: z.array(Word), // bölüm zaman çizelgesinde (saniye)
  amplitude: z.array(z.number()), // kare başına 0..1
  reminder: z.object({ startFrame: z.number().int(), durationFrames: z.number().int(), atPercent: z.number() }),
  // Sabit açılış/kapanış cümleleri ("MuMa Library'ye hoş geldin!" / "…görüşürüz!"): bölüm zaman çizelgesinde kare aralığı.
  bumpers: z.array(z.object({ startFrame: z.number().int(), endFrame: z.number().int(), text: z.string() })).default([]),
  // Kapanış şarkısı: bölüm zaman çizelgesinde kare cinsinden. Ses ayrı dosyadır, render'da karıştırılır.
  song: z.object({
    sceneId: z.string(), audioFile: z.string(), title: z.string(),
    cast: z.array(z.object({ emoji: z.string(), name: z.string() })).default([]),
    startFrame: z.number().int(), endFrame: z.number().int(),
    sections: z.array(z.object({ label: z.string(), startFrame: z.number().int(), endFrame: z.number().int(), lines: z.array(z.object({ text: z.string(), startFrame: z.number().int(), endFrame: z.number().int() })) })),
  }).optional(),
});
export type Voice = z.infer<typeof Voice>;

// ---------- Remotion girdi props'u ----------
export const EpisodeProps = z.object({
  paper: Paper,
  script: Script,
  plan: ScenePlan,
  voice: Voice,
  sources: z.array(z.object({ id: z.string(), title: z.string(), publisher: z.string(), url: z.string() })).default([]),
});
export type EpisodeProps = z.infer<typeof EpisodeProps>;
