// yayin.md: başlık, açıklama, bölüm zaman damgaları, künye ve kaynak linkleri.
import type { EpisodeProps, Facts } from "../../schemas/index.ts";

const mmss = (f: number, fps: number) => { const s = Math.floor(f / fps); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; };
const SECTION_TR: Record<string, string> = { hook: "Giriş", context: "Konu ve kaynak", method: "Ne yaptılar?", finding: "Ne buldular?", importance: "Neden önemli?", limitations: "Sınırlılıklar", summary: "Bugün bunu öğrendik" };

export const publishMd = ({ paper, script, plan, voice }: EpisodeProps, facts: Facts): string => {
  const chapters: string[] = ["0:00 Açılış"];
  let prev = "";
  plan.scenes.forEach((s, i) => { if (s.section !== prev) { chapters.push(`${mmss(voice.scenes[i].startFrame, voice.fps)} ${SECTION_TR[s.section]}`); prev = s.section; } });
  const authors = paper.authors.map((a) => a.name);
  const status = paper.isPreprint ? "Ön baskı (preprint) — henüz hakem değerlendirmesinden geçmedi" : paper.peerReviewStatus === "peer_reviewed" ? "Hakemli dergi makalesi" : "Hakemlik durumu bilinmiyor";
  const doiUrl = paper.doi ? `https://doi.org/${paper.doi}` : paper.url;
  return `# ${script.videoTitle}

**Günün Makalesi #${script.episodeNumber}** · süre ${mmss(voice.totalFrames, voice.fps)}

## Açıklama

${script.description}
${paper.isPreprint ? "\n⚠️ Bu video bir ön baskıya (preprint) dayanıyor: çalışma henüz bağımsız hakemlerce değerlendirilmedi, sonuçlar değişebilir.\n" : ""}
Bu videoda anlatılan her bilgi aşağıdaki makaleden alınmıştır. Grafikler makaledeki sayılardan yeniden çizilmiştir; makalenin kendi şekilleri kullanılmamıştır.

## Bölümler

${chapters.join("\n")}

## Kaynak

- **Makale:** ${paper.title}
- **Yazarlar:** ${authors.join(", ")}
- **Kurum:** ${paper.institutions.join("; ") || "Belirtilmemiş"}
- **${paper.isPreprint ? "Ön baskı sunucusu" : "Dergi"}:** ${paper.venue ?? "Belirtilmemiş"}${paper.publishedAt ? ` (${paper.publishedAt.slice(0, 10)})` : ""}
- **Durum:** ${status}
- **DOI:** ${paper.doi ? `[${paper.doi}](${doiUrl})` : "Yok"}
- **Bağlantı:** ${paper.url}
- **Lisans:** ${paper.license ?? "Belirtilmemiş"}
- **Senaryonun dayanağı:** ${facts.basis === "full_text" ? "makalenin tam metni" : "yalnızca makale özeti (tam metne erişilemedi)"}

## Videoda geçen sayılar ve dayanakları

${facts.facts.filter((f) => f.kind === "number").map((f) => `- ${f.statement} — _"${f.quote}"_ (${f.location})`).join("\n") || "- (sayısal olgu yok)"}

## Üretim notları

- Seslendirme: ${voice.provider === "mock" ? "MOCK (sessiz) — yayın öncesi gerçek seslendirme gerekir" : "ElevenLabs"}
- ${voice.wordCount} kelime, ${plan.scenes.length} sahne, abone ol hatırlatması videonun %${voice.reminder.atPercent} noktasında
- Thumbnail: \`thumbnail.png\`
`;
};
