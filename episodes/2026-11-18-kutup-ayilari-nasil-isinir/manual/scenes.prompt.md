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
        "display": "Buzlu bir denizde yüzmeyi düşün. Brrr! Bir dakika bile dayanamazsın, değil mi? Ama kutup ayıları buzlu sularda rahatça yüzer!",
        "spoken": "Buzlu bir denizde yüzmeyi düşün. Brrr! Bir dakika bile dayanamazsın, değil mi? Ama kutup ayıları buzlu sularda rahatça yüzer!",
        "factIds": [
          "f1",
          "f6"
        ]
      },
      {
        "id": "l2",
        "display": "Bu dev beyaz ayılar donmuş dünyada nasıl sıcak kalır?",
        "spoken": "Bu dev beyaz ayılar donmuş dünyada nasıl sıcak kalır?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Arktik'e, kutup ayılarının evine gidiyoruz!",
        "spoken": "Bugün Arktik'e, kutup ayılarının evine gidiyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kutup ayıları nasıl ısınır? Buzda ve suda nasıl hareket eder? Ve ne yerler?",
        "spoken": "Üç sorumuz var. Kutup ayıları nasıl ısınır? Buzda ve suda nasıl hareket eder? Ve ne yerler?",
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
        "display": "National Geographic'e göre kutup ayıları Arktik buz örtülerinde dolaşır ve kıyı sularında yüzer.",
        "spoken": "Neşınıl Ciyogrefik'e göre kutup ayıları Arktik buz örtülerinde dolaşır ve kıyı sularında yüzer.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Kutup ayısı bir memelidir. Bilimsel adı Ursus maritimus'tur.",
        "spoken": "Kutup ayısı bir memelidir. Bilimsel adı Ursus maritimus'tur.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l8",
        "display": "Isınmanın ilk sırrı: kalın, yalıtkan bir kürk.",
        "spoken": "Isınmanın ilk sırrı: kalın, yalıtkan bir kürk.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Yalıtkan demek, ısının kaçmasını zorlaştıran demek. Kürk, vücut ısısını içeride tutan bir mont gibidir.",
        "spoken": "Yalıtkan demek, ısının kaçmasını zorlaştıran demek. Kürk, vücut ısısını içeride tutan bir mont gibidir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "İkinci sır kürkün altında saklı: kalın bir yağ katmanı. Bu yağ, ayıyı içeriden ısıtan ikinci bir kat gibidir.",
        "spoken": "İkinci sır kürkün altında saklı: kalın bir yağ katmanı. Bu yağ, ayıyı içeriden ısıtan ikinci bir kat gibidir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Benim de iki katmanım var: metal kasam ve boyam. Ama ikisi de beni ısıtmıyor!",
        "spoken": "Benim de iki katmanım var: metal kasam ve boyam. Ama ikisi de beni ısıtmıyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Üçüncü sır daha da şaşırtıcı: Kutup ayısının kürkü beyaz ama derisi siyahtır!",
        "spoken": "Üçüncü sır daha da şaşırtıcı: Kutup ayısının kürkü beyaz ama derisi siyahtır!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "National Geographic'e göre bu siyah deri, güneşin ısıtan ışınlarını daha iyi emer.",
        "spoken": "Neşınıl Ciyogrefik'e göre bu siyah deri, güneşin ısıtan ışınlarını daha iyi emer.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l14",
        "display": "Peki kürk neden beyaz? Bembeyaz kürk, kar ve buzun arasında kamuflaj sağlar. Ayı çevresine karışır.",
        "spoken": "Peki kürk neden beyaz? Bembeyaz kürk, kar ve buzun arasında kamuflaj sağlar. Ayı çevresine karışır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l15",
        "display": "Ben kara karışamam. Gümüş rengim hemen göze batıyor!",
        "spoken": "Ben kara karışamam. Gümüş rengim hemen göze batıyor!",
        "factIds": []
      },
      {
        "id": "l16",
        "display": "Dördüncü sır ayaklarında: Pençelerinin altında bile kürk vardır!",
        "spoken": "Dördüncü sır ayaklarında: Pençelerinin altında bile kürk vardır!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Bu kürk, ayının ayaklarını soğuk yüzeylere karşı korur ve buzda kaymadan yürümesini sağlar.",
        "spoken": "Bu kürk, ayının ayaklarını soğuk yüzeylere karşı korur ve buzda kaymadan yürümesini sağlar.",
        "factIds": [
          "f5"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Kutup ayıları çok güçlü yüzücülerdir. Büyük ön pençelerini kürek gibi kullanırlar ve bu pençeler hafifçe perdelidir.",
        "spoken": "Kutup ayıları çok güçlü yüzücülerdir. Büyük ön pençelerini kürek gibi kullanırlar ve bu pençeler hafifçe perdelidir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Bazı kutup ayıları karadan yüzlerce mil uzakta yüzerken görülmüştür!",
        "spoken": "Bazı kutup ayıları karadan yüzlerce mil uzakta yüzerken görülmüştür!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l20",
        "display": "Kutup ayıları etçildir ve genellikle fok avlar.",
        "spoken": "Kutup ayıları etçildir ve genellikle fok avlar.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l21",
        "display": "Fokların nefes almak için yüzeye çıkabildiği, buzun kayıp çatladığı yerlerde beklerler.",
        "spoken": "Fokların nefes almak için yüzeye çıkabildiği, buzun kayıp çatladığı yerlerde beklerler.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l22",
        "display": "Fırsat bulurlarsa ölü balina gibi leşleri de yerler. Yani yemek seçmezler!",
        "spoken": "Fırsat bulurlarsa ölü balina gibi leşleri de yerler. Yani yemek seçmezler!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l23",
        "display": "Yavrular kar altındaki sıcak inlerde doğar. Dişiler derin kar yığınlarını kazarak in yapar; bu in onları korur ve yalıtır.",
        "spoken": "Yavrular kar altındaki sıcak inlerde doğar. Dişiler derin kar yığınlarını kazarak in yapar; bu in onları korur ve yalıtır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l24",
        "display": "Kışın genellikle ikiz doğururlar.",
        "spoken": "Kışın genellikle ikiz doğururlar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Bir yetişkinle bir kaba buzlu su koy. Elini çok kısa bir süre suya sok ve soğuğu hisset.",
        "spoken": "Şimdi sıra sende! Bir yetişkinle bir kaba buzlu su koy. Elini çok kısa bir süre suya sok ve soğuğu hisset.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l26",
        "display": "Sonra elini bir poşete koy, poşetin etrafını bitkisel katı yağla dolu başka bir poşetle sar ve tekrar dene. Fark var mı? İşte yağ katmanı! Elini fazla bekletme.",
        "spoken": "Sonra elini bir poşete koy, poşetin etrafını bitkisel katı yağla dolu başka bir poşetle sar ve tekrar dene. Fark var mı? İşte yağ katmanı! Elini fazla bekletme.",
        "factIds": [
          "f2"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l27",
        "display": "Bunu biliyor muydun? National Geographic'e göre kutup ayıları doğada ortalama 25 ile 30 yıl yaşar. Ve IUCN Kırmızı Listesi'nde 'hassas' tür olarak sınıflandırılırlar.",
        "spoken": "Bunu biliyor muydun? Neşınıl Ciyogrefik'e göre kutup ayıları doğada ortalama yirmi beş ile otuz yıl yaşar. Ve Ay Yu Si En Kırmızı Listesi'nde hassas tür olarak sınıflandırılırlar.",
        "factIds": [
          "f10",
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Hızlı soru! Kutup ayısının kürkünün altındaki derisi ne renktir?",
        "spoken": "Hızlı soru! Kutup ayısının kürkünün altındaki derisi ne renktir?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l29",
        "display": "Düşün bakalım... Evet: siyah!",
        "spoken": "Düşün bakalım... Evet: siyah!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l30",
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
        "id": "l31",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Abone olmayı ve zili açmayı unutma. Sıkı giyin, görüşürüz!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Sıkı giyin, görüşürüz!",
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
    "statement": "Kutup ayıları Arktik buz örtülerinde dolaşır ve bölgenin kıyı sularında yüzer.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Kutup ayıları, ısıtan bir yağ katmanını örten kalın, yalıtkan bir kürke dayanır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Kutup ayılarının kürkünün altında siyah deri vardır; bu deri güneşin ısıtan ışınlarını daha iyi emer.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Ayının bembeyaz kürkü, çevredeki kar ve buzda kamuflaj sağlar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Pençelerinin altında bile kürk büyür; bu, soğuk yüzeylere karşı korur ve buzda iyi tutunma sağlar.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kutup ayıları çok güçlü yüzücülerdir; kürek gibi kullandıkları büyük ön pençeleri hafifçe perdelidir; bazıları karadan yüzlerce mil uzakta yüzerken görülmüştür.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Bu güçlü avcılar genellikle fokları avlar; fokların nefes almak için yüzeye çıkabildiği, buzun kayıp çatladığı bölgeleri dolaşırlar; fırsat bulunca ölü balina gibi leşleri de yerler; etçildirler.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Kutup ayısının bilimsel adı Ursus maritimus'tur; bir memelidir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Dişiler derin kar yığınlarını kazarak in yapar; bu inler onları Arktik koşullarından korur ve yalıtır; kışın genellikle ikiz doğururlar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Kutup ayılarının doğadaki ortalama ömrü 25 ile 30 yıldır.",
    "numbers": [
      "25",
      "30"
    ]
  },
  {
    "id": "f11",
    "statement": "Kutup ayısı IUCN Kırmızı Listesi'nde 'hassas' olarak sınıflandırılır.",
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
