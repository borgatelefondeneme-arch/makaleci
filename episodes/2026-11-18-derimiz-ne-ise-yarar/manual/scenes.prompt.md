# SİSTEM

Bir animasyon yönetmenisin. Hazır bir seslendirme senaryosunu, önceden tanımlı sahne tiplerinden oluşan bir sahne planına bölüyorsun. Sahneler React bileşenleriyle çizilir; sen yalnızca parametreleri verirsin. Makaledeki şekiller kullanılmaz, tüm grafikler olgu listesindeki sayılardan çizilir.

# İSTEM

Senaryoyu 12–20 sahneye böl. Her satır tam olarak bir sahnede, sıra bozulmadan yer almalı.

Sahne alanları:
- "id": "s1", "s2", ...; "section": satırların bölümü; "lineIds": bu sahnede seslendirilen satırlar (1–5 satır; sahne 8–30 saniye sürmeli).
- "factIds": sahnedeki görselin dayandığı olgular. Görselde rakamla yazılan her sayı bu olguların "numbers" listesinde bulunmalı.
- "sourceNote": sayı içeren sahnelerde kısa dipnot (ör. "Özet", "Bulgular bölümü").
- "visual": aşağıdaki tiplerden biri. Aynı tip art arda gelmesin; en az beş farklı tip kullan.
  - "hook": açılış sorusu { question, emoji? } — ilk sahne.
  - "source-card": künye kartı — yalnızca makale bölümlerinde; konu bölümlerinde KULLANMA (kaynaklar cümle içinde anılır).
  - "big-number": tek çarpıcı sayı { value, unit?, label, sub? }. "value" makaledeki yazımla.
  - "bar-chart": 2–6 çubuk { title, unit?, bars: [{ label, value (sayı), display (ekranda yazılacak hali), highlight? }] }.
  - "line-chart": zaman/sıra içinde değişim { title, xLabel, yLabel, points: [...] }.
  - "comparison": iki şeyin yan yana kıyası { title, left: { title, value?, items[] }, right: {...} }.
  - "diagram": 2–5 adımlı süreç { title, layout: "flow" | "cycle", nodes: [{ label, emoji? }] } — yöntem anlatımı için ideal.
  - "analogy": benzetme { template: "scale" (alan kıyası) | "fill" (dolan kap) | "race" (yarış) | "zoom" (iç içe ölçek), title, a: { label, value, display? }, b: {...}, caption }. Benzetmede makalede olmayan sayı gösterme; "display" boş bırakılırsa sayı yazılmaz, yalnızca oran çizilir.
  - "quote-card": makaleden kısa alıntı { quote (Türkçe çeviri, en çok iki cümle), attribution }.
  - "bullets": 1–4 madde { title, items[], tone?: "neutral" | "caution" } — sınırlılıklar için "caution".
  - "song": kapanış şarkısı (senaryoda "song" varsa zorunlu) — sondan bir önceki sahne; yalnızca şarkıya davet eden satırı içerir. Zerre/Muma bu sahnede sağda ve büyük durur (x≈0,86, y≈0,52, scale≈1,3, state "talk").
  - "clock": dönen gün-gece kadranı { title, center, markers: [{ at (0–24, yalnızca konum), label, emoji? }], note? } — günlük döngüler için; saat rakamı yazılmaz.
  - "spotlight": ortada büyük simge, çevresinde cümlelerle beliren etiketler { title, emoji, chips: [{ label, emoji? }] }.
  - "stages": sahne boyunca çizilen evre çizgisi { title, rows: [{ label, emoji? }], path: [satır indeksleri], highlightRow?, note } — evreler/aşamalar arasında gidip gelmeyi göstermek için; şematiktir.
  - "meter": dolup boşalan depo { title, label, emoji?, phases: [{ label, level (0–1), emoji? }], note } — biriken/azalan şeyler için.
HAREKET KURALI: hiçbir sahne durağan kalmamalı. Sahne en çok 3 satır sürer; her satırda ekranda yeni bir şey belirmeli. Mümkün olan her yerde yukarıdaki hareketli tipleri kullan; "bullets" ve "quote-card" üst üste gelmesin. Her sahneye "stickers" (konuyla ilgili 2–4 emoji) ve "keywords" (lineIds ile aynı sırada, satır başına büyük harfli 1–3 kelimelik anahtar ifade; gerekmiyorsa boş dize) ver.
  - "outro": kapanış — son sahne, summary bölümünün tüm satırlarını kapsar.
- "mascot": karakter Zerre'nin bu sahnedeki hali { state: "idle" | "talk" | "point" | "think", x, y (0–1, ekran oranı, merkez), scale (0,5–1,6), pointAt? }.
  NOT: Muma yalnızca açılışta ve kapanışta görünür; ara sahnelerdeki "mascot" değerleri kullanılmaz (şema gereği yine de doldur), yalnızca son sahneninki (outro) geçerlidir.
  İçerik sol-ortadadır; Zerre genelde sağda durur (x≈0,86, y≈0,62, scale≈1). Geniş sahnelerde (bar-chart, line-chart, diagram, analogy, comparison) küçülüp köşeye çekilsin (x≈0,9, y≈0,72, scale≈0,7). "hook" sahnesinde solda ve büyük (x≈0,17, y≈0,5, scale≈1,6, state "think"). Bir sayıya ya da grafiğe dikkat çekerken "point" kullan ve "pointAt" ile hedefi ver. Sahneden sahneye konum ve boyut değişsin ki karakter ekranda gezsin.

<senaryo>
[
  {
    "id": "hook",
    "lines": [
      {
        "id": "l1",
        "display": "Vücudunun en büyük organı hangisi? Kalp mi, beyin mi? Hayır! KidsHealth'e göre en büyük organın derin!",
        "spoken": "Vücudunun en büyük organı hangisi? Kalp mi, beyin mi? Hayır! Kids Helt'e göre en büyük organın derin!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Onu her gün giyiyorsun ama hiç çıkarmıyorsun. Peki ne işe yarıyor?",
        "spoken": "Onu her gün giyiyorsun ama hiç çıkarmıyorsun. Peki ne işe yarıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün derinin katmanlarına iniyoruz!",
        "spoken": "Bugün derinin katmanlarına iniyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Deri hangi katmanlardan oluşur? Bizi nasıl korur? Ve onu nasıl koruruz?",
        "spoken": "Üç sorumuz var. Deri hangi katmanlardan oluşur? Bizi nasıl korur? Ve onu nasıl koruruz?",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum.",
        "spoken": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum.",
        "factIds": []
      }
    ]
  },
  {
    "id": "method",
    "lines": [
      {
        "id": "l6",
        "display": "Cleveland Clinic'e göre deri vücudunu mikroplardan korur ve vücut sıcaklığını düzenler.",
        "spoken": "Klivlınd Klinik'e göre deri vücudunu mikroplardan korur ve vücut sıcaklığını düzenler.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l7",
        "display": "Zararlı maddelerin ve mikropların içeri girmesini önleyen bir kalkan gibidir.",
        "spoken": "Zararlı maddelerin ve mikropların içeri girmesini önleyen bir kalkan gibidir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Benim derim metal. Mikroplar giremez ama kış gelince biraz üşüyorum!",
        "spoken": "Benim derim metal. Mikroplar giremez ama kış gelince biraz üşüyorum!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Derinin en üstteki katmanına epidermis denir. Epidermis sürekli dökülüp yenilenen hücre katmanlarından oluşur.",
        "spoken": "Derinin en üstteki katmanına epidermis denir. Epidermis sürekli dökülüp yenilenen hücre katmanlarından oluşur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "KidsHealth'e göre epidermis hücreleri yaklaşık her 28 günde bir tamamen yenilenir!",
        "spoken": "Kids Helt'e göre epidermis hücreleri yaklaşık her yirmi sekiz günde bir tamamen yenilenir!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Cleveland Clinic'e göre vücudun her gün yaklaşık 40.000 eski deri hücresi döker.",
        "spoken": "Klivlınd Klinik'e göre vücudun her gün yaklaşık kırk bin eski deri hücresi döker.",
        "factIds": [
          "f4"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Epidermiste melanin denen bir pigment vardır. Deriye rengini melanin verir.",
        "spoken": "Epidermiste melanin denen bir pigment vardır. Deriye rengini melanin verir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Vücut ne kadar çok melanin üretirse deri o kadar koyu olur.",
        "spoken": "Vücut ne kadar çok melanin üretirse deri o kadar koyu olur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Epidermisin altında dermis bulunur. Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri vardır.",
        "spoken": "Epidermisin altında dermis bulunur. Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri vardır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Sinir uçları sayesinde sıcağı, soğuğu, dokunmayı ve acıyı hissedersin.",
        "spoken": "Sinir uçları sayesinde sıcağı, soğuğu, dokunmayı ve acıyı hissedersin.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu sana dermisteki sinirler söyler.",
        "spoken": "Bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu sana dermisteki sinirler söyler.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Dermisteki yağ bezleri sebum denen bir yağ üretir. Sebum deriyi yumuşatır ve su geçirmez yapar.",
        "spoken": "Dermisteki yağ bezleri sebum denen bir yağ üretir. Sebum deriyi yumuşatır ve su geçirmez yapar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Su geçirmez mi? Ben de su geçirmez olmak isterdim. Yağmurda hep şemsiye taşıyorum!",
        "spoken": "Su geçirmez mi? Ben de su geçirmez olmak isterdim. Yağmurda hep şemsiye taşıyorum!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l19",
        "display": "Deri bir de termostattır. Sıcakken terlersin; ter, vücut sıcaklığını düzenlemeye yardım eder.",
        "spoken": "Deri bir de termostattır. Sıcakken terlersin; ter, vücut sıcaklığını düzenlemeye yardım eder.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Soğukken ise deri ısıyı içeride tutmaya yardım eder.",
        "spoken": "Soğukken ise deri ısıyı içeride tutmaya yardım eder.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "En alttaki katman deri altı dokusudur. Bu katman vücudu darbelere karşı korur ve ısıyı içeride tutar.",
        "spoken": "En alttaki katman deri altı dokusudur. Bu katman vücudu darbelere karşı korur ve ısıyı içeride tutar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Deri kendini onarmayı da bilir. Kesik ve sıyrık gibi küçük yaralar çabuk iyileşebilir.",
        "spoken": "Deri kendini onarmayı da bilir. Kesik ve sıyrık gibi küçük yaralar çabuk iyileşebilir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Şimdi sıra sende! Bir büyüteçle parmak ucunun ve elinin üstünün derisine bak. Çizgiler ve minik delikler görüyor musun?",
        "spoken": "Şimdi sıra sende! Bir büyüteçle parmak ucunun ve elinin üstünün derisine bak. Çizgiler ve minik delikler görüyor musun?",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l24",
        "display": "Sonra gözlerini kapat ve bir yetişkin önce soğuk, sonra ılık bir kaşıkla elinin üstüne hafifçe dokunsun. Farkı hissedebiliyor musun? Sinir uçların iş başında!",
        "spoken": "Sonra gözlerini kapat ve bir yetişkin önce soğuk, sonra ılık bir kaşıkla elinin üstüne hafifçe dokunsun. Farkı hissedebiliyor musun? Sinir uçların iş başında!",
        "factIds": [
          "f7"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l25",
        "display": "Bunu biliyor muydun? Amerikan Dermatoloji Akademisi'ne göre güneş kremi derini güneş yanığına karşı korumaya yardım eder. En az 30 SPF'li olanı seç ve dışarıdayken iki saatte bir yeniden sür!",
        "spoken": "Bunu biliyor muydun? Amerikan Dermatoloji Akademisi'ne göre güneş kremi derini güneş yanığına karşı korumaya yardım eder. En az otuz es pi ef'li olanı seç ve dışarıdayken iki saatte bir yeniden sür!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Hızlı soru! Deriye rengini veren pigmentin adı neydi?",
        "spoken": "Hızlı soru! Deriye rengini veren pigmentin adı neydi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l27",
        "display": "Düşün bakalım... Evet: melanin!",
        "spoken": "Düşün bakalım... Evet: melanin!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l28",
        "display": "Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!",
        "spoken": "Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!",
        "factIds": []
      }
    ]
  },
  {
    "id": "summary",
    "lines": [
      {
        "id": "l29",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Abone olmayı ve zili açmayı unutma. Güneşli günlerde kremini unutma!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Güneşli günlerde kremini unutma!",
        "factIds": []
      }
    ]
  }
]
</senaryo>

<olgular>
[
  {
    "id": "f1",
    "statement": "Deri en büyük organımızdır ve birçok görevi vardır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Deri vücudu mikroplardan korur ve vücut sıcaklığını düzenler; zararlı maddelerin ve mikropların vücuda girmesini önleyen bir engel oluşturur.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Epidermis derinin üst katmanıdır; sürekli dökülüp yenilenen hücre katmanlarından oluşur; epidermis hücreleri yaklaşık her 28 günde bir tamamen yenilenir.",
    "numbers": [
      "28"
    ]
  },
  {
    "id": "f4",
    "statement": "Yeni hücreler, vücudun her gün döktüğü yaklaşık 40.000 eski deri hücresinin yerini alır.",
    "numbers": [
      "40.000"
    ]
  },
  {
    "id": "f5",
    "statement": "Epidermis, deriye rengini veren melanin pigmentini içerir; vücut ne kadar çok melanin üretirse deri o kadar koyu olur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri bulunur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Deri, sıcağı ve soğuğu, dokunmayı ve acıyı hissetmemizi sağlayan sinir uçları taşır; dermisteki sinirler bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu bildirir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Yağ bezleri deriyi yumuşatan ve su geçirmez yapan sebum yağını üretir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Ter vücut sıcaklığını düzenlemeye yardım eder; deri sıcakken terleyerek, soğukken ısıyı içeride tutarak sıcaklığı kontrol eder.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Deri altı dokusu vücudu darbelere ve yaralanmalara karşı korur ve vücut ısısını içeride tutar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Kesik ve sıyrık gibi küçük yaralanmalar çabuk iyileşebilir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Güneş kremi deriyi güneş yanığına ve cilt kanserine karşı korumaya yardım eder; en az 30 SPF'li, suya dayanıklı, geniş spektrumlu güneş kremi seçilmeli; dışarıdayken iki saatte bir ve yüzdükten ya da terledikten hemen sonra yeniden sürülmelidir.",
    "numbers": [
      "30"
    ]
  }
]
</olgular>

# ÇIKTI ŞEMASI (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "scenes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "section": {
            "type": "string",
            "enum": [
              "hook",
              "context",
              "method",
              "finding",
              "importance",
              "limitations",
              "summary"
            ]
          },
          "lineIds": {
            "minItems": 1,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "visual": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "hook"
                  },
                  "question": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "question"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "source-card"
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "big-number"
                  },
                  "value": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "label": {
                    "type": "string"
                  },
                  "sub": {
                    "type": "string"
                  },
                  "icon": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "value",
                  "label"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "clock"
                  },
                  "title": {
                    "type": "string"
                  },
                  "center": {
                    "type": "string"
                  },
                  "markers": {
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "at": {
                          "type": "number",
                          "minimum": 0,
                          "maximum": 24
                        },
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "at",
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "center",
                  "markers"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "spotlight"
                  },
                  "title": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  },
                  "chips": {
                    "minItems": 2,
                    "maxItems": 6,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "emoji",
                  "chips"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "stages"
                  },
                  "title": {
                    "type": "string"
                  },
                  "rows": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "path": {
                    "minItems": 3,
                    "maxItems": 40,
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 9007199254740991
                    }
                  },
                  "highlightRow": {
                    "type": "integer",
                    "minimum": -9007199254740991,
                    "maximum": 9007199254740991
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "rows",
                  "path"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "meter"
                  },
                  "title": {
                    "type": "string"
                  },
                  "label": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  },
                  "phases": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "level": {
                          "type": "number",
                          "minimum": 0,
                          "maximum": 1
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label",
                        "level"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "label",
                  "phases"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "bar-chart"
                  },
                  "title": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "bars": {
                    "minItems": 2,
                    "maxItems": 6,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "value": {
                          "type": "number"
                        },
                        "display": {
                          "type": "string"
                        },
                        "highlight": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "label",
                        "value",
                        "display"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "bars"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "line-chart"
                  },
                  "title": {
                    "type": "string"
                  },
                  "xLabel": {
                    "type": "string"
                  },
                  "yLabel": {
                    "type": "string"
                  },
                  "points": {
                    "minItems": 2,
                    "maxItems": 12,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "value": {
                          "type": "number"
                        },
                        "display": {
                          "type": "string"
                        },
                        "highlight": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "label",
                        "value",
                        "display"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "xLabel",
                  "yLabel",
                  "points"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "comparison"
                  },
                  "title": {
                    "type": "string"
                  },
                  "left": {
                    "type": "object",
                    "properties": {
                      "title": {
                        "type": "string"
                      },
                      "value": {
                        "type": "string"
                      },
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "title",
                      "items"
                    ],
                    "additionalProperties": false
                  },
                  "right": {
                    "type": "object",
                    "properties": {
                      "title": {
                        "type": "string"
                      },
                      "value": {
                        "type": "string"
                      },
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "title",
                      "items"
                    ],
                    "additionalProperties": false
                  }
                },
                "required": [
                  "type",
                  "title",
                  "left",
                  "right"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "diagram"
                  },
                  "title": {
                    "type": "string"
                  },
                  "layout": {
                    "type": "string",
                    "enum": [
                      "flow",
                      "cycle"
                    ]
                  },
                  "nodes": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "layout",
                  "nodes"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "analogy"
                  },
                  "template": {
                    "type": "string",
                    "enum": [
                      "scale",
                      "fill",
                      "race",
                      "zoom"
                    ]
                  },
                  "title": {
                    "type": "string"
                  },
                  "a": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "string"
                      },
                      "value": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "label",
                      "value"
                    ],
                    "additionalProperties": false
                  },
                  "b": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "string"
                      },
                      "value": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "label",
                      "value"
                    ],
                    "additionalProperties": false
                  },
                  "caption": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "template",
                  "title",
                  "a",
                  "b",
                  "caption"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "quote-card"
                  },
                  "quote": {
                    "type": "string"
                  },
                  "attribution": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "quote",
                  "attribution"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "bullets"
                  },
                  "title": {
                    "type": "string"
                  },
                  "items": {
                    "minItems": 1,
                    "maxItems": 4,
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "tone": {
                    "type": "string",
                    "enum": [
                      "neutral",
                      "caution"
                    ]
                  }
                },
                "required": [
                  "type",
                  "title",
                  "items"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "song"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "outro"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              }
            ]
          },
          "mascot": {
            "type": "object",
            "properties": {
              "state": {
                "type": "string",
                "enum": [
                  "idle",
                  "talk",
                  "point",
                  "think"
                ]
              },
              "x": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
              },
              "y": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
              },
              "scale": {
                "type": "number",
                "minimum": 0.3,
                "maximum": 2.5
              },
              "pointAt": {
                "type": "object",
                "properties": {
                  "x": {
                    "type": "number"
                  },
                  "y": {
                    "type": "number"
                  }
                },
                "required": [
                  "x",
                  "y"
                ],
                "additionalProperties": false
              },
              "pose": {
                "type": "string",
                "enum": [
                  "point",
                  "crossed",
                  "thumbs",
                  "book",
                  "wave"
                ]
              }
            },
            "required": [
              "state",
              "x",
              "y",
              "scale"
            ],
            "additionalProperties": false
          },
          "factIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "sourceNote": {
            "type": "string"
          },
          "stickers": {
            "maxItems": 6,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "fx": {
            "type": "string",
            "enum": [
              "blackhole",
              "shake",
              "flash",
              "meteor",
              "dig",
              "erupt",
              "rain",
              "sparkle"
            ]
          },
          "keywords": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "id",
          "section",
          "lineIds",
          "visual",
          "mascot",
          "factIds"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "scenes"
  ],
  "additionalProperties": false
}
```
