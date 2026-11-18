# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Mağaralar nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 41, "paperId": "topic:magaralar-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Solution Caves",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/subjects/caves/solution-caves.htm"
  },
  {
    "id": "k2",
    "title": "Speleothems",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/subjects/caves/speleothems.htm"
  },
  {
    "id": "k3",
    "title": "Lava Caves or Tubes",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/subjects/caves/lava-caves-or-tubes.htm"
  },
  {
    "id": "k4",
    "title": "Sea or Littoral Caves",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/subjects/caves/sea-or-littoral-caves.htm"
  },
  {
    "id": "k5",
    "title": "Glacier Ice Caves",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/articles/000/glacier-ice-caves.htm"
  },
  {
    "id": "k6",
    "title": "Caves and Karst",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/subjects/caves/index.htm"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Erime mağaraları en çok kireçtaşı, mermer ve dolomit gibi kayaçlarda bulunur.",
    "numbers": [],
    "quote": "Solution caves are most often found in rock types such as limestone, marble, dolomite",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Bu kayaçlar yağmur suyu asidik olduğu için çözünür; mağaraları oluşturan asit genellikle karbonik asittir; bu asit karbondioksit suda çözününce oluşur.",
    "numbers": [],
    "quote": "The reason these rocks dissolve is because rainwater is acidic / When caves form the acid that makes them is usually carbonic acid. / This acid forms when carbon dioxide (made of one Carbon and two Oxygen atoms and known as CO2) dissolves in water.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Su tortuları ve çözünmüş kayayı aşağı taşıdıkça düdenler genişler.",
    "numbers": [],
    "quote": "Sinkholes enlarge as water carries sediments and dissolved rock downward.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Karst, kireçtaşı ya da başka çözünebilir kayaçların bulunduğu bölgelerde oluşan bir yer şekli türüdür.",
    "numbers": [],
    "quote": "Karst is a type of landscape and topography formed in areas with limestone or the other soluble rocks.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Jeologlara göre içinden dere akan mağara geçitleri yılda en fazla yaklaşık 1 milimetre büyüyebilir.",
    "numbers": [
      "1"
    ],
    "quote": "Geologists have determined that cave passages with active streams can grow a maximum of about 1 mm per year.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Birçok mağara yüz binlerce, hatta milyonlarca yaşındadır.",
    "numbers": [],
    "quote": "Many caves are hundreds of thousands or even millions of years old.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Mamut Mağarası 400 milden uzun ölçüsüyle Dünya'nın en uzun mağarasıdır.",
    "numbers": [
      "400"
    ],
    "quote": "This is the longest cave on Earth at more than 400 miles.",
    "location": "National Park Service — Solution Caves"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Sarkıtlar genellikle kalsitten oluşur; tavandan sarkan buz saçaklarına ya da havuçlara benzerler; sarkıt kelimesi (stalaktit) Yunancada 'damla damla sızmak' demektir.",
    "numbers": [],
    "quote": "Stalactites are usually composed of calcite, but they may consist of other minerals. / they resemble icicles or carrots hanging from cave ceilings. / the word stalactite is Greek for “oozing out in drops.”",
    "location": "National Park Service — Speleothems"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Dikitler, yukarıdaki bir sarkıttan ya da tavandan damlayan suyun yerde biriktirdiği tümsek çökeltilerdir.",
    "numbers": [],
    "quote": "Stalagmites are convex floor deposits built up by water dripping from an overhead stalactite",
    "location": "National Park Service — Speleothems"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Bir dikit kendisini besleyen sarkıtla birleşince sütun oluşur; sütunlar bazen 20 metreyi aşan yükseklik ve çapa ulaşabilir.",
    "numbers": [
      "20"
    ],
    "quote": "When a stalagmite grows together with its counterpart feeder stalactite, a new speleothem is formed: a column or pillar. / Columns can reach gigantic proportions, sometimes over 65 feet (20 m) in height and diameter.",
    "location": "National Park Service — Speleothems"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Lav binlerce derece sıcaktır ve bir nehir gibi akabilir; erimiş lav geçip gidince geride lav tüpü denen boş bir tünel kalır.",
    "numbers": [],
    "quote": "Lava is thousands of degrees hot and can flow like a river. / Once the molten lava has passed through, it leaves an empty tunnel called a lava cave, or more commonly, a lava tube.",
    "location": "National Park Service — Lava Caves or Tubes"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Deniz mağaraları çoğunlukla dalgaların yol açtığı aşınmayla oluşur.",
    "numbers": [],
    "quote": "Sea caves or littoral caves are formed primarily from erosion caused by waves.",
    "location": "National Park Service — Sea or Littoral Caves"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Bazen bir buzulun kenarındaki erime, buzun içinde küçük mağaralar oluşturabilir; buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.",
    "numbers": [],
    "quote": "Sometimes, melting at the margin of a glacier may cause small caves to form within the ice, / Glacier ice caves are cold, with icy water dripping from their roofs.",
    "location": "National Park Service — Glacier Ice Caves"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Lav mağaraları kireçtaşı mağaraları kadar canlı çeşitliliğine sahiptir, içlerinde birçok küçük ve sıra dışı hayvan yaşar; bazı yerlerde büyük yarasa tünekleri vardır.",
    "numbers": [],
    "quote": "Lava caves are just as biologically diverse as limestone caves with many small, unusual animals inside. / In other locations, large bat roosts lie in the caves.",
    "location": "National Park Service — Lava Caves or Tubes"
  },
  {
    "id": "f15",
    "kind": "number",
    "statement": "ABD milli parklarında 4.700'den fazla mağara vardır.",
    "numbers": [
      "4.700"
    ],
    "quote": "This includes over 4,700 caves with at least four of these that extend for more than 135 miles",
    "location": "National Park Service — Caves and Karst"
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
