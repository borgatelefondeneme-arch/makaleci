# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Buzullar nasıl hareket eder?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 43, "paperId": "topic:buzullar-nasil-hareket-eder".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Glaciers",
    "publisher": "NSIDC",
    "url": "https://nsidc.org/learn/parts-cryosphere/glaciers"
  },
  {
    "id": "k2",
    "title": "Science of Glaciers",
    "publisher": "NSIDC",
    "url": "https://nsidc.org/learn/parts-cryosphere/glaciers/science-glaciers"
  },
  {
    "id": "k3",
    "title": "Glacier Quick Facts",
    "publisher": "NSIDC",
    "url": "https://nsidc.org/learn/parts-cryosphere/glaciers/glacier-quick-facts"
  },
  {
    "id": "k4",
    "title": "Glacier",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/glacier/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.",
    "numbers": [],
    "quote": "A glacier is an accumulation of ice and snow that slowly flows over land.",
    "location": "NSIDC — Glaciers"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Buzullar karada oluşur ve yüzyıllar boyunca sıkışarak buza dönüşen yağmış kardan yapılır.",
    "numbers": [],
    "quote": "Glaciers form on land, and they are made up of fallen snow that gets compressed into ice over many centuries.",
    "location": "National Geographic Education — Glacier"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Her yıl yeni kar katmanları öncekileri gömer ve sıkıştırır; yaklaşık bir yıl sonra kar, kar ile buzul buzu arasında bir ara hal olan firne dönüşür; çoğu buzul için bu süreç yüz yıldan uzun sürer.",
    "numbers": [],
    "quote": "Each year, new layers of snow bury and compress the previous layers. / After about a year, the snow turns into firn—an intermediate state between snow and glacier ice. / For most glaciers, this process takes more than a hundred years.",
    "location": "NSIDC — Glaciers"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Çok yaşlı buzul buzunda kristaller bir yetişkin yumruğu büyüklüğüne ulaşabilir.",
    "numbers": [],
    "quote": "In very old glacier ice, crystals can reach the size of an adult fist.",
    "location": "NSIDC — Glacier Quick Facts"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Buzul buzu çok yoğunlaşıp kabarcıklardan arınınca çoğu zaman mavi görünür; buz kırmızı ışığın küçük bir bölümünü soğurur.",
    "numbers": [],
    "quote": "Glacial ice often appears blue when it has become very dense and free of bubbles. / Ice absorbs a small amount of red light.",
    "location": "NSIDC — Glacier Quick Facts"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Buzul kendi ağırlığının basıncıyla dışarıya ve aşağıya doğru akmaya başlar; kalın bir buz katmanının ağırlığı, yani buz kütlesine etki eden yer çekimi buzulları akıtır.",
    "numbers": [],
    "quote": "Under the pressure of its own weight, a glacier will begin to move, or flow, outwards and downwards. / The sheer weight of a thick layer of ice, or the force of gravity on the ice mass, causes glaciers to flow.",
    "location": "NSIDC — Science of Glaciers"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Buzullar buzun iç deformasyonuyla ve tabandaki kayaların ve tortuların üzerinde kayarak hareket eder; dik yamaçlardaki ince, soğuk buzulların hareketinin çoğu bu taban kaymasından gelebilir.",
    "numbers": [],
    "quote": "Glaciers move by internal deformation of the ice, and by sliding over the rocks and sediments at the base. / This basal sliding may account for most of the movement of thin, cold glaciers on steep slopes.",
    "location": "NSIDC — Science of Glaciers"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Yarıklar buzul buzundaki çatlaklardır; buzulun hızlı aktığı yerlerde sürtünme bu dev çatlakları oluşturur.",
    "numbers": [],
    "quote": "Crevasse are cracks in glacier ice. / At locations where a glacier flows rapidly, friction creates these giant cracks.",
    "location": "NSIDC — Science of Glaciers"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Buzullar ani atılımlar yaparak haftalarca, hatta aylarca günde birkaç metre ilerleyebilir; en hızlı atılım rekoru Pakistan'daki Kutiah Buzulu'nundur: 1953'te üç ayda 12 kilometreden fazla ilerledi, günde ortalama yaklaşık 112 metre.",
    "numbers": [
      "1953",
      "12",
      "112"
    ],
    "quote": "Glaciers may surge, racing forward several meters per day for weeks or even months. / The Kutiah Glacier in Pakistan holds the record for the fastest glacial surge. / In 1953, it raced more than 12 kilometers (7.5 miles) in three months, averaging about 112 meters (367 feet) per day.",
    "location": "NSIDC — Science of Glaciers; NSIDC — Glacier Quick Facts"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "ABD Jeoloji Araştırmaları Kurumu'na göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde 68,7'sini depolar.",
    "numbers": [
      "68.7"
    ],
    "quote": "Glaciers and ice caps store about 68.7 percent of the world's fresh water, according to the US Geological Survey.",
    "location": "NSIDC — Glacier Quick Facts"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Dünyada yalnızca iki buz tabakası vardır: Antarktika ve Grönland buz tabakaları; ikisi birlikte Dünya'daki tatlı su buzunun yüzde 99'undan fazlasını içerir; buzul buzunun çoğu Antarktika'dadır.",
    "numbers": [
      "99"
    ],
    "quote": "Currently, there are only two ice sheets on Earth: the Antarctic and Greenland Ice Sheets. / Together, the Antarctic and Greenland Ice Sheets contain more than 99 percent of the freshwater ice on Earth. / Most of the world’s glacier ice is in Antarctica.",
    "location": "NSIDC — Glaciers"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Dünyadaki buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir.",
    "numbers": [],
    "quote": "Most of the world’s glaciers exist in the polar regions, in areas like Greenland, the Canadian Arctic, and Antarctica.",
    "location": "National Geographic Education — Glacier"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Son 60 ila 100 yılda dünyadaki buzullar genel olarak geri çekildi; son birkaç on yılda buzullar giderek artan bir hızla küçülüyor, hatta yok oluyor.",
    "numbers": [
      "60",
      "100"
    ],
    "quote": "Over the past 60 to 100 years, glaciers worldwide have tended to retreat. / Indeed, glaciers worldwide have been shrinking—and even disappearing—at an accelerated rate for the past several decades.",
    "location": "NSIDC — Science of Glaciers; National Geographic Education — Glacier"
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
            "snow",
            "gut",
            "night"
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
