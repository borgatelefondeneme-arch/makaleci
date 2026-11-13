# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Kar taneleri nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

Bölümler, bu sırayla ve bu kimliklerle:
1. "hook" — merak uyandıran açılış (30–40 kelime).
2. "context" — günün soruları ve sözlük duyurusu (selamlama ve kaynak listesi YOK; kaynaklar ilgili cümlede anılır).
3. "method" — "Nasıl oluyor?": anlamak için gereken temel bilgiler.
4. "finding" — "İşin sırrı": sorunun yanıtı, adım adım.
5. "importance" — "Sen de dene": çocuğun gelişimini destekleyen, evde ya da dışarıda güvenle yapılabilecek bir gözlem ya da etkinlik.
6. "limitations" — "Bunu biliyor muydun?": şaşırtıcı bir ek bilgi ve kısa bir tekrar sorusu.
7. "summary" — "Bugün bunu öğrendik": üç ana fikir birer cümleyle, ardından abone olma ve soru gönderme daveti.

Satır kuralları makale bölümleriyle aynıdır: her satırda "id" ("l1"...), "display" (ekran; sayılar rakamla), "spoken" (seslendirme; sayılar yazıyla, kısaltmalar okunuşuyla), "factIds". "display" içinde rakamla yazılan her sayı o satırın olgularının "numbers" listesinde bulunmalı; bilgi taşımayan sayıları yazıyla yaz.
"glossary": videoda geçen ve 7–14 yaşındaki bir çocuğun bilmeyebileceği kelimeler (3–8 tane), her biri { "term", "meaning" } — anlamı tek, sade bir cümleyle. Anlatımda bir kez "Bilmediğin kelimeler için sana açıklamalarda bir sözlük bırakıyorum" de.
Anlatım düzeyi 10 yaşındaki meraklı bir çocuğa göre olsun; okul öncesi gibi değil. Gerçek bilimsel terimleri kullan ve hemen açıkla (ör. "ana saat" demekle yetinme: "suprakiazmatik çekirdek, kısaca SCN; beynin hipotalamus bölgesinde…"). Mekanizmayı anlat: ne, nerede, nasıl. Benzetme terimin yerine değil, yanına gelsin. Süreye takılma: konu gerektiriyorsa anlatım 10 dakikaya kadar uzayabilir.
Kaynak bölümü yazma: kaynağı cümlenin içinde an ("NIH'ye göre…", "CDC'ye göre…"). Şarkı sözleri de aynı düzeyde olsun ve senaryodaki bilimsel ifadelerden türesin.
"song": videonun son dakikasında söylenecek, konuyu özetleyen neşeli kapanış şarkısı. "title"; "style" (İngilizce tarz tarifleri: neşeli çocuk şarkısı, marş ritmi, çizgi film enerjisi, 120 BPM, Türkçe net vokal; sanatçı, şarkı ya da eser adı YAZMA); "negativeStyle"; "cast" (şarkıda dans edecek, konuyla ilgili 4–5 karakter: { "emoji", "name" }; ör. uzay konusunda gezegenler ve yıldızlar, DNA konusunda DNA sarmalı; Muma şarkıda görünmez); sözlerde şarkının adı geçmez; "sections": toplam yaklaşık 60 saniye, her biri { "tag" (Intro / Verse 1 / Chorus ...), "label" (Türkçe: Giriş / Kıta / Nakarat), "direction"? (İngilizce çalgı yönergesi), "lines" (kısa, kafiyeli Türkçe dizeler), "durationMs" }. Sözlerde rakam olmaz ve yalnızca olgu listesindeki bilgiler geçer; nakarat bölümün üç ana fikrini taşır. Şarkı varsa "limitations" bölümünün son satırı izleyiciyi şarkıya davet eder ve "summary" bölümü kısa tutulur (özeti şarkı yapar); anlatım yaklaşık 420–460 kelime olur.
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 22, "paperId": "topic:kar-taneleri-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "How do snowflakes form? Get the science behind snow",
    "publisher": "NOAA",
    "url": "https://www.noaa.gov/stories/how-do-snowflakes-form-get-science-behind-snow"
  },
  {
    "id": "k2",
    "title": "Severe Weather 101: Winter Weather Types",
    "publisher": "NSSL",
    "url": "https://www.nssl.noaa.gov/education/svrwx101/winter/types/"
  },
  {
    "id": "k3",
    "title": "Science of Snow",
    "publisher": "NSIDC",
    "url": "https://nsidc.org/learn/parts-cryosphere/snow/science-snow"
  },
  {
    "id": "k4",
    "title": "Quick Facts About Snow",
    "publisher": "NSIDC",
    "url": "https://nsidc.org/learn/parts-cryosphere/snow/quick-facts-about-snow"
  },
  {
    "id": "k5",
    "title": "Snow",
    "publisher": "Met Office",
    "url": "https://weather.metoffice.gov.uk/learn-about/weather/types-of-weather/snow"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Bir kar tanesi, çok soğuk bir su damlacığı gökyüzünde bir polen ya da toz parçacığının üzerinde donunca oluşmaya başlar; su buharı ilk kristalin üzerinde donarak yeni kristaller kurar.",
    "numbers": [],
    "quote": "A snowflake begins to form when an extremely cold water droplet freezes onto a pollen or dust particle in the sky. / water vapor freezes onto the primary crystal, building new crystals",
    "location": "NOAA — How do snowflakes form?"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Sıcaklık 0°C'nin altına düşünce su buharı sıvı evreye geçmeden doğrudan buza dönüşür.",
    "numbers": [
      "0"
    ],
    "quote": "when temperatures drop below 0°C (32°F), water vapor condenses directly into ice without going through the liquid stage.",
    "location": "NSIDC — Quick Facts About Snow"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Kar taneleri bulutlardan düşen tek buz kristalleri ya da buz kristali kümeleridir; çok sayıda kar kristalinin birikimidir.",
    "numbers": [],
    "quote": "Snowflakes are single ice crystals or clusters of ice crystals that fall from a cloud. / Snowflakes are accumulations of many snow crystals.",
    "location": "NSIDC — Science of Snow"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Kar tanelerinin biçimi, kristalin su moleküllerinin önceden belirlenmiş yerlere dizilmesindeki iç düzeni yansıtır; altıgen biçim her zaman korunur.",
    "numbers": [],
    "quote": "reflect the internal order of the crystal's water molecules as they arrange themselves in predetermined spaces / Although the six-sided shape is always maintained",
    "location": "NOAA — How do snowflakes form?"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Kristalin biçimini en çok oluştuğu sıcaklık, daha az ölçüde de havanın nemi belirler; daha az soğukta uzun iğne gibi kristaller, çok daha soğukta çok yassı levha gibi kristaller görülür (kaynakta Fahrenhayt değerleriyle).",
    "numbers": [],
    "quote": "it is the temperature at which a crystal forms — and to a lesser extent the humidity of the air / we see long needle-like crystals at 23 degrees F and very flat plate-like crystals at 5 degrees F.",
    "location": "NOAA — How do snowflakes form?"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Kar tanelerinin her biri gökyüzünden yere biraz farklı yollar izler; bu yüzden prizmalardan iğnelere, tanıdık dantel desenine kadar hepsi benzersiz görünme eğilimindedir.",
    "numbers": [],
    "quote": "individual snowflakes all follow slightly different paths from the sky to the ground / they all tend to look unique, resembling everything from prisms and needles to the familiar lacy pattern.",
    "location": "NOAA — How do snowflakes form?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Temiz kar görünür güneş ışığının çoğunu yansıtır ve beyaz görünür; aslında yarı saydamdır; kar tanesinin çok sayıdaki yüzü ışığı her yöne saçar.",
    "numbers": [],
    "quote": "Clean snow, however, reflects most of the visible sunlight, creating a white appearance. / Snow appears white, but it is actually translucent. / The many sides of a snowflake scatter light, diffusing the color spectrum in many directions.",
    "location": "NSIDC — Science of Snow; NSIDC — Quick Facts About Snow"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Kar, bir evin tavanındaki yalıtıma benzer iyi bir yalıtkandır; bir kar katmanının toplam hacminin çoğu havadır.",
    "numbers": [],
    "quote": "snow is a good insulator, similar to the insulation in the ceiling of a house / most of the total volume of a snow layer is made up of air",
    "location": "NSIDC — Science of Snow"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Taze kar sesi bastırır, çünkü ses dalgalarını emer.",
    "numbers": [],
    "quote": "Fresh snow cover dampens sound because it absorbs sound waves.",
    "location": "NSIDC — Quick Facts About Snow"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Kar tanelerinin çoğu 1,3 santimetreden küçüktür; çok daha büyükleri 5 santimetreye yaklaşabilir.",
    "numbers": [
      "1.3",
      "5"
    ],
    "quote": "Most snowflakes are less than 1.3 centimeters (0.5 inches) across. / nearing 5 centimeters (2 inches) across",
    "location": "NSIDC — Science of Snow"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Sulu kar, kar taneleri ince bir ılık hava katmanından geçerken yalnızca kısmen eridiğinde oluşur; donan yağmur, kar taneleri daha ılık bir katmanda tamamen erir ve 0°C'deki ya da daha soğuk her şeye değer değmez yeniden donar.",
    "numbers": [
      "0"
    ],
    "quote": "Sleet occurs when snowflakes only partially melt when they fall through a shallow layer of warm air. / Freezing rain occurs when snowflakes descend into a warmer layer of air and melt completely. / they instantly refreeze upon contact with anything that is at or below 0 degrees C",
    "location": "NOAA NSSL — Severe Weather 101: Winter Weather Types"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Graupel, yuvarlaklaşmış, opak, 2–5 milimetrelik kar taneciklerinden oluşur; bazen doluyla karıştırılır ama dokusu daha yumuşak ve ufalanır.",
    "numbers": [
      "2",
      "5"
    ],
    "quote": "Graupel consists of snowflakes that become rounded, opaque pellets ranging from 2 to 5 millimeters / Graupel is sometimes mistaken for hail, but tends to have a texture that is softer and more crumbly.",
    "location": "NSIDC — Science of Snow"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Kar, atmosfer sıcaklığı donma noktasında ya da altındayken (0°C) oluşur; karın yağması için sıfırın altında olması gerektiği bir efsanedir.",
    "numbers": [
      "0"
    ],
    "quote": "Snow forms when the atmospheric temperature is at or below freezing (0°C or 32°F). / It is a myth that it needs to be below zero to snow.",
    "location": "NSIDC — Science of Snow; Met Office — Snow"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Kar taneleri bulutlardaki minik buz kristallerinin birbirine yapışmasıyla oluşur.",
    "numbers": [],
    "quote": "Snow forms when tiny ice crystals in clouds stick together to become snowflakes.",
    "location": "Met Office — Snow"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Wilson Bentley, hobisi kar tanelerini fotoğraflamak olan bir çiftçiydi.",
    "numbers": [],
    "quote": "Bentley was a farmer whose hobby was photographing snow flakes.",
    "location": "NOAA — How do snowflakes form?"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Küreme kar asla yenmemelidir; içinde kir ve magnezyum klorür gibi kimyasallar vardır; düşük rüzgâr soğuğuna maruz kalmak donmaya ya da hipotermiye yol açabilir.",
    "numbers": [],
    "quote": "never eat plowed snow, which contains snow, dirt, and chemicals like magnesium chloride. / Exposure to low wind chill values can result in frostbite or hypothermia.",
    "location": "NSIDC — Quick Facts About Snow; NSIDC — Science of Snow"
  }
]
</olgular>

# ÇIKTI ŞEMASI (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "paperId": {
      "type": "string"
    },
    "episodeNumber": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "videoTitle": {
      "type": "string"
    },
    "paperTitleTr": {
      "type": "string"
    },
    "sections": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
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
          "lines": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "display": {
                  "type": "string"
                },
                "spoken": {
                  "type": "string"
                },
                "factIds": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              },
              "required": [
                "id",
                "display",
                "spoken",
                "factIds"
              ],
              "additionalProperties": false
            }
          }
        },
        "required": [
          "id",
          "lines"
        ],
        "additionalProperties": false
      }
    },
    "takeaways": {
      "minItems": 3,
      "maxItems": 3,
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "nextTeaser": {
      "type": "string"
    },
    "theme": {
      "type": "object",
      "properties": {
        "backdrop": {
          "type": "string",
          "enum": [
            "space",
            "underground",
            "meadow",
            "ocean",
            "storm",
            "mouth",
            "aurora",
            "sky",
            "micro",
            "snow"
          ]
        },
        "actors": {
          "default": [],
          "maxItems": 6,
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "kind": {
                "type": "string",
                "enum": [
                  "walk",
                  "fly",
                  "chase",
                  "swim",
                  "dig",
                  "hop",
                  "orbit",
                  "swarm"
                ]
              },
              "emoji": {
                "type": "string"
              },
              "emoji2": {
                "type": "string"
              },
              "size": {
                "type": "number"
              },
              "every": {
                "type": "number"
              },
              "facesRight": {
                "type": "boolean"
              }
            },
            "required": [
              "kind",
              "emoji"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "backdrop",
        "actors"
      ],
      "additionalProperties": false
    },
    "song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "style": {
          "minItems": 1,
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "negativeStyle": {
          "default": [],
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "cast": {
          "minItems": 2,
          "maxItems": 6,
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "emoji": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "emoji",
              "name"
            ],
            "additionalProperties": false
          }
        },
        "show": {
          "maxItems": 6,
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "kind": {
                "type": "string",
                "enum": [
                  "walk",
                  "fly",
                  "chase",
                  "swim",
                  "dig",
                  "hop",
                  "orbit",
                  "swarm"
                ]
              },
              "emoji": {
                "type": "string"
              },
              "emoji2": {
                "type": "string"
              },
              "size": {
                "type": "number"
              },
              "every": {
                "type": "number"
              },
              "facesRight": {
                "type": "boolean"
              }
            },
            "required": [
              "kind",
              "emoji"
            ],
            "additionalProperties": false
          }
        },
        "sections": {
          "minItems": 1,
          "maxItems": 30,
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "tag": {
                "type": "string"
              },
              "label": {
                "type": "string"
              },
              "direction": {
                "type": "string"
              },
              "lines": {
                "minItems": 1,
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "durationMs": {
                "type": "integer",
                "minimum": 3000,
                "maximum": 120000
              }
            },
            "required": [
              "tag",
              "label",
              "lines",
              "durationMs"
            ],
            "additionalProperties": false
          }
        }
      },
      "required": [
        "title",
        "style",
        "negativeStyle",
        "cast",
        "sections"
      ],
      "additionalProperties": false
    },
    "description": {
      "type": "string"
    },
    "glossary": {
      "default": [],
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "term": {
            "type": "string"
          },
          "meaning": {
            "type": "string"
          }
        },
        "required": [
          "term",
          "meaning"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "paperId",
    "episodeNumber",
    "videoTitle",
    "paperTitleTr",
    "sections",
    "takeaways",
    "nextTeaser",
    "description",
    "glossary"
  ],
  "additionalProperties": false
}
```
