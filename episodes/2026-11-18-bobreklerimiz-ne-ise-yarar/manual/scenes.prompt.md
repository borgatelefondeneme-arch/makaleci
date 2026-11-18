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
        "display": "Vücudunda gece gündüz çalışan iki minik temizlik fabrikası var. Sen uyurken bile durmuyorlar!",
        "spoken": "Vücudunda gece gündüz çalışan iki minik temizlik fabrikası var. Sen uyurken bile durmuyorlar!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l2",
        "display": "Bu fabrikalar kanını temizliyor. Adları: böbrekler!",
        "spoken": "Bu fabrikalar kanını temizliyor. Adları: böbrekler!",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün böbreklerin içindeki minik süzgeçlere bakıyoruz!",
        "spoken": "Bugün böbreklerin içindeki minik süzgeçlere bakıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Böbrekler nerededir? Kanı nasıl süzer? Ve başka hangi işleri yapar?",
        "spoken": "Üç sorumuz var. Böbrekler nerededir? Kanı nasıl süzer? Ve başka hangi işleri yapar?",
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
        "display": "NIDDK'ye göre böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır.",
        "spoken": "En Ay Di Di Key'ye göre böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Kaburgalarının hemen altında, omurganın iki yanında birer tane bulunur. Elini belinin biraz yukarısına, arkana koy: işte oradalar! Gıdıklanmak serbest!",
        "spoken": "Kaburgalarının hemen altında, omurganın iki yanında birer tane bulunur. Elini belinin biraz yukarısına, arkana koy: işte oradalar! Gıdıklanmak serbest!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "İnsanların genellikle iki böbreği vardır, ama tek böbrekle de sağlıklı bir yaşam sürülebilir.",
        "spoken": "İnsanların genellikle iki böbreği vardır, ama tek böbrekle de sağlıklı bir yaşam sürülebilir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Benim böbreğim yok. Benim filtrem sadece toz tutuyor, o da haftada bir tıkanıyor!",
        "spoken": "Benim böbreğim yok. Benim filtrem sadece toz tutuyor, o da haftada bir tıkanıyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l10",
        "display": "Her böbrekte nefron denen yaklaşık bir milyon minik süzme birimi vardır.",
        "spoken": "Her böbrekte nefron denen yaklaşık bir milyon minik süzme birimi vardır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Nefronlar, zararlı maddeleri kandan ayıran süzgeçler gibidir. Mutfaktaki çay süzgeci bile bu kadar çalışkan değil!",
        "spoken": "Nefronlar, zararlı maddeleri kandan ayıran süzgeçler gibidir. Mutfaktaki çay süzgeci bile bu kadar çalışkan değil!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "NIDDK'ye göre sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer!",
        "spoken": "En Ay Di Di Key'ye göre sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Süzme sırasında atıklar ve fazla su ayrılır. Bunlardan idrar oluşur.",
        "spoken": "Süzme sırasında atıklar ve fazla su ayrılır. Bunlardan idrar oluşur.",
        "factIds": [
          "f4",
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "İdrar, vücudun ihtiyaç duymadığı atıklardan ve fazla sudan kurtulma yoludur.",
        "spoken": "İdrar, vücudun ihtiyaç duymadığı atıklardan ve fazla sudan kurtulma yoludur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "İdrar böbreklerden çıkar ve üreter denen iki ince borudan aşağı akar.",
        "spoken": "İdrar böbreklerden çıkar ve üreter denen iki ince borudan aşağı akar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Sonra mesaneye gelir. Mesane, tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir.",
        "spoken": "Sonra mesaneye gelir. Mesane, tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Sonunda üretra denen boru, idrarı vücudun dışına taşır.",
        "spoken": "Sonunda üretra denen boru, idrarı vücudun dışına taşır.",
        "factIds": [
          "f6"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Böbreklerin başka işleri de var. Vücuttaki su, tuz ve minerallerin dengesini korurlar.",
        "spoken": "Böbreklerin başka işleri de var. Vücuttaki su, tuz ve minerallerin dengesini korurlar.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "KidsHealth'e göre böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.",
        "spoken": "Kids Helt'e göre böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Böbrekler hormon da yapar! Bu hormonlar kırmızı kan hücrelerinin yapımına ve kemiklerinin güçlü kalmasına yardım eder.",
        "spoken": "Böbrekler hormon da yapar! Bu hormonlar kırmızı kan hücrelerinin yapımına ve kemiklerinin güçlü kalmasına yardım eder.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Hormon, vücutta bir yerden başka bir yere mesaj taşıyan kimyasal bir haberci gibidir.",
        "spoken": "Hormon, vücutta bir yerden başka bir yere mesaj taşıyan kimyasal bir haberci gibidir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Çok su içtiğinde daha sık tuvalete gidersin ve idrarın açık sarı olur. Böbreklerin fazla suyu dışarı atar.",
        "spoken": "Çok su içtiğinde daha sık tuvalete gidersin ve idrarın açık sarı olur. Böbreklerin fazla suyu dışarı atar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Ben su içmem. İçsem kısa devre yaparım!",
        "spoken": "Ben su içmem. İçsem kısa devre yaparım!",
        "factIds": []
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! Bir gün boyunca içtiğin her bardak suyu bir kâğıda çizgiyle işaretle.",
        "spoken": "Şimdi sıra sende! Bir gün boyunca içtiğin her bardak suyu bir kâğıda çizgiyle işaretle.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Akşam çizgileri say. Yeterince su içmiş misin? Böbreklerin sana teşekkür eder!",
        "spoken": "Akşam çizgileri say. Yeterince su içmiş misin? Böbreklerin sana teşekkür eder!",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l26",
        "display": "Bunu biliyor muydun? KidsHealth'e göre böbreklerini sağlıklı tutmak için su içmek, besleyici yemekler yemek ve bol bol hareket etmek önemlidir.",
        "spoken": "Bunu biliyor muydun? Kids Helt'e göre böbreklerini sağlıklı tutmak için su içmek, besleyici yemekler yemek ve bol bol hareket etmek önemlidir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Böbreklerdeki minik süzme birimlerine ne denir?",
        "spoken": "Hızlı soru! Böbreklerdeki minik süzme birimlerine ne denir?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: nefron!",
        "spoken": "Düşün bakalım... Evet: nefron!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l29",
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
        "id": "l30",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Abone olmayı ve zili açmayı unutma. Şimdi git bir bardak su iç!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Şimdi git bir bardak su iç!",
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
    "statement": "Böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır; kaburgaların hemen altında, omurganın iki yanında birer tane bulunur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "İnsanların genellikle iki böbreği vardır ama tek böbrekle de normal, sağlıklı bir yaşam sürebilirler.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Her böbrek, nefron denen yaklaşık bir milyon süzme biriminden oluşur; bu minik birimler zararlı maddeleri kandan uzaklaştırır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer; atıkları ve fazla suyu ayırarak idrar yapar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Vücut, ihtiyaç duymadığı atıklardan ve fazla sudan kurtulmak için idrar üretir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Üreterler idrarı böbreklerden mesaneye taşıyan iki ince borudur; mesane tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir; üretra idrarı mesaneden vücut dışına taşıyan borudur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Böbrekler su, tuz ve minerallerin sağlıklı dengesini korur; idrar da vücudun doğru miktarda su tutmasının bir yoludur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Böbrekler kırmızı kan hücrelerinin üretimini denetleyen bir hormon yapar; böbreklerin yaptığı hormonlar kırmızı kan hücresi yapımına ve kemiklerin güçlü ve sağlıklı kalmasına yardım eder.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Çok su içince daha çok idrara çıkılır ve idrar açık sarı olur.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Böbrekleri ve idrar yollarını sağlıklı tutmak için yeterince su içilmeli, besleyici beslenilmeli ve bol egzersiz yapılmalıdır.",
    "numbers": []
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
