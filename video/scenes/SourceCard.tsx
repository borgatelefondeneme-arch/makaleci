import React from "react";
import { C, F } from "../theme";
import { beatAt, pop } from "../anim";
import { Card, SceneProps, Stage, Title } from "./common";

const short = (names: string[], max = 4) => (names.length <= max ? names.join(", ") : `${names.slice(0, max).join(", ")} ve ${names.length - max} yazar daha`);

// Konu bölümlerinde künye yerine kaynak listesi gösterilir.
const TopicSources: React.FC<SceneProps<"source-card">> = ({ visual, frame, beats, dur, data }) => (
  <Stage>
    <Title frame={frame} color={C.purple}>Bunları nereden biliyoruz?</Title>
    <div style={{ display: "flex", flexDirection: "column", gap: 22 }}>
      {data.sources.slice(0, 4).map((s, i) => {
        const a = pop(frame, beatAt(beats, i, dur, Math.min(4, data.sources.length)));
        return (
          <Card key={s.id} style={{ display: "flex", alignItems: "center", gap: 28, padding: "24px 34px", opacity: a, transform: `translateX(${(1 - a) * 60}px)` }}>
            <div style={{ fontSize: 58, fontFamily: F.head }}>📚</div>
            <div>
              <div style={{ fontFamily: F.head, fontWeight: 800, fontSize: 28, color: C.teal, textTransform: "uppercase", letterSpacing: 1 }}>{s.publisher}</div>
              <div style={{ fontFamily: F.body, fontWeight: 600, fontSize: 36, color: C.text, lineHeight: 1.25 }}>{s.title}</div>
            </div>
          </Card>
        );
      })}
    </div>
    <div style={{ marginTop: 22, fontFamily: F.body, fontSize: 28, color: C.dim, opacity: pop(frame, 30) }}>{visual.note ?? "Kaynak bağlantıları video açıklamasında."}</div>
  </Stage>
);

export const SourceCard: React.FC<SceneProps<"source-card">> = (props) => {
  if (props.data.paper.kind === "topic") return <TopicSources {...props} />;
  const { visual, frame, beats, dur, data } = props;
  const p = data.paper;
  const rows: [string, string][] = [
    ["Makale", p.title],
    ["Yazarlar", short(p.authors.map((a) => a.name))],
    ["Kurum", p.institutions.slice(0, 3).join(" · ") || "Belirtilmemiş"],
    [p.isPreprint ? "Ön baskı sunucusu" : "Dergi", [p.venue, p.publishedAt?.slice(0, 10)].filter(Boolean).join(" · ") || "Belirtilmemiş"],
    ["DOI", p.doi ?? "Yok"],
  ];
  const badge = p.isPreprint
    ? { t: "ÖN BASKI — hakem değerlendirmesinden geçmedi", c: C.coral }
    : p.peerReviewStatus === "peer_reviewed" ? { t: "HAKEMLİ DERGİ MAKALESİ", c: C.teal } : { t: "HAKEMLİK DURUMU BİLİNMİYOR", c: C.yellow };
  return (
    <Stage>
      <Title frame={frame} color={C.purple}>Bu bilgi nereden geliyor?</Title>
      <Card style={{ display: "flex", flexDirection: "column", gap: 22 }}>
        {rows.map(([k, v], i) => {
          const a = pop(frame, beatAt(beats, i, dur, rows.length));
          return (
            <div key={k} style={{ display: "flex", gap: 28, opacity: a, transform: `translateX(${(1 - a) * 50}px)`, alignItems: "baseline" }}>
              <div style={{ width: 250, flexShrink: 0, fontFamily: F.head, fontWeight: 800, fontSize: 30, color: C.teal, textTransform: "uppercase", letterSpacing: 1 }}>{k}</div>
              <div style={{ fontFamily: k === "DOI" ? "monospace" : F.body, fontWeight: 600, fontSize: i === 0 ? 34 : 36, color: C.text, lineHeight: 1.25, wordBreak: "break-word" }}>{v}</div>
            </div>
          );
        })}
      </Card>
      <div style={{ marginTop: 26, alignSelf: "flex-start", opacity: pop(frame, 20), background: badge.c, color: C.ink, fontFamily: F.head, fontWeight: 900, fontSize: 28, padding: "10px 26px", borderRadius: 30 }}>
        {badge.t}
      </div>
      {visual.note && <div style={{ marginTop: 16, fontFamily: F.body, fontSize: 26, color: C.dim }}>{visual.note}</div>}
    </Stage>
  );
};
