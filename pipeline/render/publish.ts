// yayin.md: başlık, açıklama, bölüm zaman damgaları, künye ve kaynak linkleri.
import type { EpisodeProps, Facts } from "../../schemas/index.ts";

const mmss = (f: number, fps: number) => { const s = Math.floor(f / fps); return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; };
const SECTION_TR: Record<string, string> = { hook: "Giriş", context: "Konu ve kaynak", method: "Ne yaptılar?", finding: "Ne buldular?", importance: "Neden önemli?", limitations: "Sınırlılıklar", summary: "Bugün bunu öğrendik" };

const TOPIC_TR: Record<string, string> = { hook: "Giriş", context: "Günün sorusu", method: "Nasıl oluyor?", finding: "İşin sırrı", importance: "Sen de dene", limitations: "Bunu biliyor muydun?", summary: "Bugün bunu öğrendik" };
const voiceNote = (v: EpisodeProps["voice"]) => v.provider === "mock" ? "MOCK (sessiz) — yayın öncesi gerçek seslendirme gerekir"
  : v.provider === "piper" ? "Piper (yerel, tr_TR-dfki) — taslak ses; ses verisinin lisansı ticari kullanıma izin vermez (CC BY-NC-SA 4.0)" : "ElevenLabs";

const topicMd = ({ paper, script, plan, voice }: EpisodeProps, facts: Facts): string => {
  const chapters: string[] = ["0:00 Açılış"];
  let prev = "";
  plan.scenes.forEach((s, i) => { if (s.section !== prev) { chapters.push(`${mmss(voice.scenes[i].startFrame, voice.fps)} ${TOPIC_TR[s.section]}`); prev = s.section; } });
  return `# ${script.videoTitle}

**Günün Sorusu #${script.episodeNumber}** · ${paper.title} · süre ${mmss(voice.totalFrames, voice.fps)}

## Açıklama

${script.description}

## Bölümler

${chapters.join("\n")}

## Kaynaklar

${facts.sources.map((s) => `- **${s.publisher}** — [${s.title}](${s.url})`).join("\n")}

## Videodaki bilgiler ve dayanakları

${facts.facts.map((f) => `- ${f.statement} — _"${f.quote}"_ (${f.location})`).join("\n")}

${script.glossary.length ? `## Sözlük\n\n${script.glossary.map((g) => `- **${g.term}:** ${g.meaning}`).join("\n")}\n\n` : ""}${script.song ? `## Kapanış şarkısı: ${script.song.title}\n\n${script.song.sections.map((s) => `**${s.label}**\n${s.lines.join("  \n")}`).join("\n\n")}\n\n_Müzik ElevenLabs Music ile yapay zekâ kullanılarak üretilmiştir; sözler MuMa Library'ye aittir. Platformun yapay zekâ içerik beyanı gerekiyorsa işaretleyin._\n\n` : ""}## Üretim notları

- Seslendirme: ${voiceNote(voice)}
- ${voice.wordCount} kelime, ${plan.scenes.length} sahne, abone ol hatırlatması videonun %${voice.reminder.atPercent} noktasında
- Thumbnail: \`thumbnail.png\`
`;
};

export const publishMd = (props: EpisodeProps, facts: Facts): string => {
  if (props.paper.kind === "topic") return topicMd(props, facts);
  const { paper, script, plan, voice } = props;
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

- Seslendirme: ${voiceNote(voice)}
- ${voice.wordCount} kelime, ${plan.scenes.length} sahne, abone ol hatırlatması videonun %${voice.reminder.atPercent} noktasında
- Thumbnail: \`thumbnail.png\`
`;
};
