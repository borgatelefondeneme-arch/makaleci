# SİSTEM

Çocuklara yönelik bir bilim kanalının doğruluk editörüsün. Verilen soruyu yanıtlamak için gereken olguları, yalnızca güvenilir kurum kaynaklarına (ör. NASA, ESA, TÜBİTAK, üniversiteler, müzeler) dayanarak listelersin. Emin olmadığın ya da kaynağını gösteremeyeceğin hiçbir bilgiyi ekleme; tahmini sayı yazma.

# İSTEM

Soru: "Gökkuşağı nasıl oluşur?"

Bu soruyu 7–14 yaşındaki çocuklara anlatacak 5 dakikalık bir video için olgu listesi çıkar.
- "sources": dayandığın kaynaklar { id: "k1"..., title, publisher, url }.
- Her olgu: "statement" (sade Türkçe), "numbers" (olguda geçen sayılar, kaynaktaki değerle), "quote" (kaynaktan birebir kısa alıntı), "location" (kaynağın adı), "kind" ("number" | "claim").
- "basis": "full_text", "institutions": [], "paperId": "topic:gokkusagi-nasil-olusur".

Kaynak metni verilmedi: yalnızca kesin olarak bildiğin ve gösterdiğin kaynakta gerçekten yer alan olguları yaz. Bu liste yayın öncesinde bir insan tarafından kaynaklarla karşılaştırılacak.

# ÇIKTI ŞEMASI (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "paperId": {
      "type": "string"
    },
    "basis": {
      "type": "string",
      "enum": [
        "full_text",
        "abstract_only"
      ]
    },
    "institutions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "sources": {
      "default": [],
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "publisher": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "title",
          "publisher",
          "url"
        ],
        "additionalProperties": false
      }
    },
    "facts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "kind": {
            "type": "string",
            "enum": [
              "number",
              "claim",
              "meta"
            ]
          },
          "statement": {
            "type": "string"
          },
          "numbers": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "quote": {
            "type": "string"
          },
          "location": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "kind",
          "statement",
          "numbers",
          "quote",
          "location"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "paperId",
    "basis",
    "institutions",
    "sources",
    "facts"
  ],
  "additionalProperties": false
}
```
