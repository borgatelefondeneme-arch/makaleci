// Örnek (uydurma) bölüm: tüm sahne tiplerini dener ve Remotion stüdyosunun varsayılan verisini üretir.
// GERÇEK BİR MAKALE DEĞİLDİR. Çalıştırma: npx tsx episodes/_demo/make.ts
import { EpisodeMeta, Facts, Paper, ScenePlan, Script, type Scene } from "../../schemas/index.ts";
import { writeJson } from "../../pipeline/lib/io.ts";

const d = "episodes/_demo";
const now = "2026-01-01T00:00:00Z";
writeJson(`${d}/episode.json`, EpisodeMeta, { id: "_demo", episodeNumber: 0, sourceUrl: null, createdAt: now });
writeJson(`${d}/01_paper.json`, Paper, {
  id: "demo:0", title: "ÖRNEK VERİ — An Entirely Fictional Study of Sleepy Garden Snails", abstract: "Örnek veri.",
  authors: [{ name: "Ayşe Örnek", affiliations: ["Örnek Üniversitesi"] }, { name: "Çağrı Deneme", affiliations: ["Örnek Üniversitesi"] }],
  institutions: ["Örnek Üniversitesi, Hayali Biyoloji Bölümü"], venue: "Örnek Dergi", doi: "10.0000/ornek.2026.001", url: "https://example.org/ornek",
  fullTextUrl: null, license: null, publishedAt: "2026-01-01", isPreprint: true, peerReviewStatus: "preprint", categories: [], sources: ["demo"], fetchedAt: now,
});
writeJson(`${d}/03_facts.json`, Facts, {
  paperId: "demo:0", basis: "abstract_only", institutions: [],
  facts: [{ id: "f1", kind: "number", statement: "Örnek sayılar", numbers: ["40", "12", "18", "25", "31", "3", "9", "15", "22", "60", "20", "1", "2", "4", "5", "100"], quote: "örnek", location: "Örnek" }],
});
const L = (id: string, t: string, f = ["f1"]) => ({ id, display: t, spoken: t, factIds: f });
writeJson(`${d}/03_script.json`, Script, {
  paperId: "demo:0", episodeNumber: 0, videoTitle: "Salyangozlar gerçekten uyur mu?", paperTitleTr: "ÖRNEK VERİ — Uykucu bahçe salyangozları üzerine tamamen hayali bir çalışma",
  sections: [
    { id: "hook", lines: [L("l1", "Bir salyangoz günde kaç saat uyur dersin? Tahminin ne?", [])] },
    { id: "context", lines: [L("l2", "Bu örnek çalışma Ayşe Örnek ve ekibine ait."), L("l3", "Örnek Üniversitesi'nde yapıldı ve Örnek Dergi'de bir ön baskı olarak yayımlandı."), L("l4", "DOI numarası: 10.0000/ornek.2026.001")] },
    { id: "method", lines: [L("l5", "Araştırmacılar önce salyangozları topladı, sonra kamerayla izledi."), L("l6", "En sonunda uyku sürelerini ölçtüler."), L("l7", "Toplam 40 salyangoz izlendi.")] },
    { id: "finding", lines: [L("l8", "Dört grubun uyku süreleri birbirinden farklıydı."), L("l9", "En uzun uyuyan grup 31 saatle dördüncü gruptu."), L("l10", "Günler geçtikçe uyku süresi arttı."), L("l11", "Genç ve yaşlı salyangozlar farklı davrandı."), L("l12", "Yaşlılar daha çok uyudu.")] },
    { id: "importance", lines: [L("l13", "Küçük bir kap ile büyük bir kabı düşün."), L("l14", "Biri diğerinden üç kat dolu."), L("l15", "Bir yarış gibi düşünelim."), L("l16", "Biri çok daha uzağa gidiyor."), L("l17", "Alanları kıyaslayalım."), L("l18", "Fark böyle görünüyor."), L("l19", "Şimdi uzaklaşalım."), L("l20", "Küçük olan büyüğün içinde kayboluyor."), L("l21", "Yazarlar şöyle diyor: bu sonuçlar ilk adımdır.")] },
    { id: "limitations", lines: [L("l22", "Yalnızca 40 salyangoz incelendi."), L("l23", "Çalışma tek bir bahçede yapıldı."), L("l24", "Sonuçlar henüz başkalarınca tekrarlanmadı.")] },
    { id: "summary", lines: [L("l25", "Bugün üç şey öğrendik. Salyangozlar uyur."), L("l26", "Yaşlılar daha çok uyur."), L("l27", "Ve bu daha ilk adım. Abone olmayı unutma!")] },
  ],
  takeaways: ["Salyangozlar da uyur", "Yaşlı salyangozlar daha çok uyur", "Bu sonuç henüz bir ilk adım"],
  nextTeaser: "Yeni bir keşif seni bekliyor!", description: "Örnek veriyle üretilmiş deneme bölümü.",
});
const sc = (id: string, section: Scene["section"], lineIds: string[], visual: Scene["visual"], mascot: Scene["mascot"], sourceNote?: string): Scene => ({ id, section, lineIds, visual, mascot, factIds: ["f1"], sourceNote });
const corner = { x: 0.9, y: 0.7, scale: 0.75 };
writeJson(`${d}/04_scenes.json`, ScenePlan, {
  paperId: "demo:0",
  scenes: [
    sc("s1", "hook", ["l1"], { type: "hook", question: "Bir salyangoz günde kaç saat uyur?", emoji: "🐌" }, { state: "think", x: 0.17, y: 0.5, scale: 1.6 }),
    sc("s2", "context", ["l2", "l3", "l4"], { type: "source-card" }, { state: "point", x: 0.88, y: 0.55, scale: 1.05, pointAt: { x: 0.5, y: 0.45 } }),
    sc("s3", "method", ["l5", "l6"], { type: "diagram", title: "Nasıl yaptılar?", layout: "flow", nodes: [{ label: "Salyangozları topla", emoji: "🐌" }, { label: "Kamerayla izle", emoji: "🎥" }, { label: "Uykuyu ölç", emoji: "⏱️" }] }, { state: "talk", ...corner }),
    sc("s4", "method", ["l7"], { type: "big-number", value: "40", unit: "salyangoz", label: "izlendi", sub: "Örnek veri" }, { state: "point", x: 0.8, y: 0.55, scale: 1.2, pointAt: { x: 0.3, y: 0.4 } }, "Örnek"),
    sc("s5", "finding", ["l8", "l9"], { type: "bar-chart", title: "Gruplara göre uyku süresi", unit: "saat", bars: [{ label: "1. grup", value: 12, display: "12" }, { label: "2. grup", value: 18, display: "18" }, { label: "3. grup", value: 25, display: "25" }, { label: "4. grup", value: 31, display: "31", highlight: true }] }, { state: "point", x: 0.9, y: 0.6, scale: 0.8, pointAt: { x: 0.62, y: 0.35 } }, "Örnek"),
    sc("s6", "finding", ["l10"], { type: "line-chart", title: "Günlere göre uyku", xLabel: "Gün", yLabel: "Saat", points: [{ label: "1", value: 3, display: "3" }, { label: "2", value: 9, display: "9" }, { label: "3", value: 15, display: "15" }, { label: "4", value: 22, display: "22", highlight: true }] }, { state: "talk", x: 0.9, y: 0.3, scale: 0.7 }),
    sc("s7", "finding", ["l11", "l12"], { type: "comparison", title: "Genç mi, yaşlı mı?", left: { title: "Genç salyangoz", value: "12", items: ["Daha hareketli", "Az uyur"] }, right: { title: "Yaşlı salyangoz", value: "31", items: ["Daha yavaş", "Çok uyur"] } }, { state: "think", x: 0.92, y: 0.72, scale: 0.65 }),
    sc("s8", "importance", ["l13", "l14"], { type: "analogy", template: "fill", title: "Kap benzetmesi", a: { label: "Küçük", value: 20 }, b: { label: "Büyük", value: 60 }, caption: "Biri diğerinden çok daha dolu." }, { state: "talk", ...corner }),
    sc("s9", "importance", ["l15", "l16"], { type: "diagram", title: "Döngü", layout: "cycle", nodes: [{ label: "Uyu", emoji: "😴" }, { label: "Uyan", emoji: "🌞" }, { label: "Ye", emoji: "🥬" }, { label: "Gez", emoji: "🐌" }] }, { state: "idle", x: 0.92, y: 0.25, scale: 0.6 }),
    sc("s10", "importance", ["l17", "l18"], { type: "analogy", template: "race", title: "Yarış benzetmesi", a: { label: "Genç", value: 12, display: "12" }, b: { label: "Yaşlı", value: 31, display: "31" }, caption: "Biri çok daha uzağa gidiyor." }, { state: "point", x: 0.9, y: 0.7, scale: 0.75, pointAt: { x: 0.6, y: 0.5 } }),
    sc("s11", "importance", ["l19"], { type: "analogy", template: "scale", title: "Alan benzetmesi", a: { label: "Küçük", value: 5 }, b: { label: "Büyük", value: 100 }, caption: "Fark böyle görünüyor." }, { state: "talk", ...corner }),
    sc("s12", "importance", ["l20"], { type: "analogy", template: "zoom", title: "Ölçek benzetmesi", a: { label: "Küçük", value: 1 }, b: { label: "Büyük", value: 100 }, caption: "Küçük olan büyüğün içinde kayboluyor." }, { state: "think", ...corner }),
    sc("s13", "importance", ["l21"], { type: "quote-card", quote: "Bu sonuçlar yalnızca bir ilk adımdır; daha fazla çalışma gerekir.", attribution: "Örnek ve ekibi, Örnek Dergi" }, { state: "talk", x: 0.86, y: 0.6, scale: 1.1 }),
    sc("s14", "limitations", ["l22", "l23", "l24"], { type: "bullets", title: "Dikkat: sınırlılıklar", tone: "caution", items: ["Yalnızca 40 salyangoz incelendi", "Tek bir bahçede yapıldı", "Henüz tekrarlanmadı"] }, { state: "think", x: 0.87, y: 0.58, scale: 1.0 }),
    sc("s15", "summary", ["l25", "l26", "l27"], { type: "outro" }, { state: "talk", x: 0.87, y: 0.58, scale: 1.1 }),
  ],
});
