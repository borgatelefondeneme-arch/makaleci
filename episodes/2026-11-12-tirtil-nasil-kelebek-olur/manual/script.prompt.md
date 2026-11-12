# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Tırtıl nasıl kelebek olur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 19, "paperId": "topic:tirtil-nasil-kelebek-olur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Monarch Butterfly Biology",
    "publisher": "ABD Orman Servisi",
    "url": "https://www.fs.usda.gov/wildflowers/pollinators/Monarch_Butterfly/biology/index.shtml"
  },
  {
    "id": "k2",
    "title": "Monarch Migration and Overwintering",
    "publisher": "ABD Orman Servisi",
    "url": "https://www.fs.usda.gov/wildflowers/pollinators/Monarch_Butterfly/migration/index.shtml"
  },
  {
    "id": "k3",
    "title": "Pollinators: Monarch butterfly",
    "publisher": "Ulusal Park Servisi",
    "url": "https://www.nps.gov/articles/monarch-butterfly.htm"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Monark kelebeğinin dört ayrı yaşam evresi vardır: yumurta, larva (tırtıl), pupa (krizalit) ve ergin; bu dört evreli sürece tam başkalaşım denir.",
    "numbers": [],
    "quote": "The monarch has four distinct life stages: egg, larva (caterpillar), pupa (chrysalis), and adult. / The completion of the four life-stage process is called complete metamorphosis.",
    "location": "USDA Forest Service — Monarch Butterfly Biology"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Dişi monarklar yumurtalarını zehirli süt otu yapraklarının alt yüzüne bırakır; bir dişi ömrü boyunca 100 ile 300 arasında yumurta bırakır; yumurtalar bırakıldıktan yaklaşık dört gün sonra açılır.",
    "numbers": [
      "100",
      "300"
    ],
    "quote": "Female monarchs lay their eggs on the underside of poisonous milkweed leaves. / A female Monarch butterfly lays from 100 to 300 eggs during her life. / The eggs hatch about four days after they are laid.",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly; USDA Forest Service — Monarch Butterfly Biology"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Tırtıl yumurtadan çıkınca kendi yumurtasını yer, sonra süt otu yapraklarıyla beslenmeye geçer.",
    "numbers": [],
    "quote": "As the caterpillar hatches, it eats its own egg; then switches to a diet of milkweed leaves.",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly"
  },
  {
    "id": "f4",
    "kind": "number",
    "statement": "Larvalar yumurtadan çıktığında 1 santimetreden küçüktür ve yaklaşık 5 santimetreye kadar büyür; larvanın deri değiştirmeleri arasındaki evrelere instar denir.",
    "numbers": [
      "1",
      "5"
    ],
    "quote": "When larvae first hatch they are less than 1 centimeter (cm) and grow to be about 5 cm. / The stages between larval molts are called instars.",
    "location": "USDA Forest Service — Monarch Butterfly Biology"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Monark, en az beş günde pupadan ergine dönüşebilir; kelebeğin pupadan çıkmasına eklozyon denir.",
    "numbers": [],
    "quote": "In as few as five days, the monarch develops from a pupa to an adult. / The emergence of the butterfly from the pupal stage to an adult is called eclosion.",
    "location": "USDA Forest Service — Monarch Butterfly Biology"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Ergin kelebek uzun hortumunu açıp uzatarak çeşitli çiçeklerden nektar içer; kullanılmadığında bu esnek 'dil' yeniden sarmal biçiminde kıvrılır.",
    "numbers": [],
    "quote": "The adult butterfly drinks nectar from a variety of flowers, uncoiling and extending its long proboscis to sip food. / When not in use, this flexible “tongue” coils back into a spiral.",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Süt otunun zehirleri, tırtıl kelebeğe dönüştükten sonra bile monarkın vücudunda kalır; canlı desenleri bir uyarı işaretidir; monarkı yiyen hayvanlar çok hastalanır ve sonra bu desenli kelebekten uzak durur.",
    "numbers": [],
    "quote": "The milkweeds' toxins remain permanently in the monarch's system, even after the caterpillar metamorphoses into a butterfly. / serves as a “skull and crossbones” warning / Animals that eat a monarch become very sick and, thereafter, will avoid this distinctively patterned butterfly.",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Monarkların çoğu yalnızca birkaç hafta yaşar; ama yaz sonu ve sonbahar başında çıkan kuşak farklıdır: göç için doğarlar ve sekiz dokuz ay yaşayabilirler.",
    "numbers": [],
    "quote": "Most monarchs will live only a few weeks, but the generation that emerges in late summer and early fall is different. / These butterflies are born to travel and may live for eight or nine months to accomplish their lengthy migration.",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Monark, kuşlar gibi iki yönlü göç yaptığı bilinen tek kelebektir; bazıları kışlık evlerine ulaşmak için 3.000 mile kadar uçar; günde 50–100 mil yol alabilirler.",
    "numbers": [
      "3.000",
      "50",
      "100"
    ],
    "quote": "The monarch is the only butterfly known to make a two-way migration as birds do. / Some fly as far as 3,000 miles to reach their winter home! / Monarchs can travel between 50-100 miles a day",
    "location": "USDA Forest Service — Monarch Migration and Overwintering"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Kuzey Amerika'nın doğu monark topluluğu kışı Meksika'da aynı 11–12 dağlık bölgede geçirir; tek bir ağaçta on binlerce monark kümelenebilir.",
    "numbers": [
      "11",
      "12"
    ],
    "quote": "The eastern population of North America's monarchs overwinters in the same 11 to 12 mountain areas / Tens of thousands of monarchs can cluster on a single tree.",
    "location": "USDA Forest Service — Monarch Migration and Overwintering"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Kuzey ABD'ye ve Kanada'ya ulaşmak 3–4 kuşak sürer; her yaz dört kuşağa kadar yetişir ve her kuşak bir öncekinden biraz daha kuzeye gider.",
    "numbers": [
      "3",
      "4"
    ],
    "quote": "It will take 3-4 generations to reach the northern United States and Canada. / Monarchs have up to four generations each summer, each one traveling a little further north than the last.",
    "location": "USDA Forest Service — Monarch Migration and Overwintering; USDA Forest Service — Monarch Butterfly Biology"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Monarkların yumurta bırakmak için süt otuna ihtiyacı vardır; ama süt otları çoğu zaman zararlı ot diye yok edilir; Meksika ve Kaliforniya'daki kışlak alanları ormansızlaşma yüzünden hızla küçülüyor.",
    "numbers": [],
    "quote": "Monarch butterflies need milkweed plants to lay their eggs. / Unfortunately, milkweeds are often eradicated as noxious weeds. / The butterflies' winter habitat in Mexico and California is rapidly shrinking due to deforestation",
    "location": "U.S. National Park Service — Pollinators: Monarch butterfly"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Bir gramdan hafif olan bu kelebekler 2.000 ile 3.000 mil arasında uçar.",
    "numbers": [
      "2.000",
      "3.000"
    ],
    "quote": "Weighing less than a gram, these unique butterflies will fly between 2,000 to 3,000 miles",
    "location": "USDA Forest Service — Monarch Butterfly Biology"
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
            "aurora"
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
