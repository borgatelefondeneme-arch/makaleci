# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Canlılar nasıl ışık saçar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 29, "paperId": "topic:canlilar-nasil-isik-sacar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Bioluminescence",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/bioluminescence/"
  },
  {
    "id": "k2",
    "title": "Fireflies",
    "publisher": "Milli Parklar Servisi",
    "url": "https://www.nps.gov/grsm/learn/nature/fireflies.htm"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Biyolüminesans, canlıların vücutlarındaki kimyasal tepkimelerle saçtığı ışıktır.",
    "numbers": [],
    "quote": "Bioluminescence is light emitted by living things through chemical reactions in their bodies.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Biyolüminesans ateşböceklerinin yanı sıra bazı mantarlarda, balıklarda, karideslerde, denizanalarında ve planktonlarda da görülür; bazıları karada yaşar.",
    "numbers": [],
    "quote": "a natural process also seen in certain fungi, fish, shrimp, jellyfish, plankton / Some bioluminescent organisms, including fireflies and fungi, are found on land.",
    "location": "National Park Service (Great Smoky Mountains) — Fireflies; National Geographic Education — Bioluminescence"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Biyolüminesans lusiferin ve lusiferaz ya da fotoprotein gerektirir; ışığı asıl üreten bileşik lusiferindir; ateşböcekleri lusiferini oksijen ve lusiferaz enzimiyle karıştırır.",
    "numbers": [],
    "quote": "requires two unique chemicals: luciferin and either luciferase or photoprotein / Luciferin is the compound that actually produces light. / fireflies mix the chemical luciferin with oxygen and the enzyme luciferase",
    "location": "National Geographic Education — Bioluminescence; National Park Service (Great Smoky Mountains) — Fireflies"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Fotoproteinler ışık yapmak için başka bir etkene, çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.",
    "numbers": [],
    "quote": "need another agent, often an ion of the element calcium, to produce light",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Soğuk ışık, ışığın yüzde 20'sinden azının ısı olarak yayılması demektir.",
    "numbers": [
      "20"
    ],
    "quote": "Cold light means less than 20% of the light generates thermal radiation, or heat.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f6",
    "kind": "number",
    "statement": "Akkor ampuller enerjilerinin yalnızca yaklaşık yüzde 10'unu ışık, yüzde 90'ını ısı olarak yayar; ateşböceğinin parıltısı neredeyse yüzde 100 ışıktır ve çok az ısı üretir.",
    "numbers": [
      "10",
      "90",
      "100"
    ],
    "quote": "traditional incandescent bulbs emit only about 10% of their energy as light, with the remaining 90% as heat. / resulting in a 'cool' glow that boasts nearly 100% light / generate light with minimal heat",
    "location": "National Park Service (Great Smoky Mountains) — Fireflies"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Işık saçan deniz canlıları arasında balıklar, bakteriler ve denizanaları vardır; dinoflagellatlar mavimsi yeşil parlar.",
    "numbers": [],
    "quote": "These bioluminescent marine species include fish, bacteria, and jellies. / Dinoflagellates, for instance, bioluminesce in a bluish-green color.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Denizdeki biyolüminesansın çoğu görünür ışığın mavi-yeşil bölümündedir; bu renkler derin okyanusta daha kolay görülür.",
    "numbers": [],
    "quote": "Most marine bioluminescence, for instance, is expressed in the blue-green part of the visible light spectrum. / These colors are more easily visible in the deep ocean.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Ateşböceği türlerinin çoğu yeşilimsi sarı ışık saçar, bazı türler mavi ya da beyaza yakın ışık saçar.",
    "numbers": [],
    "quote": "Most species emit a greenish-yellow light, but some species showcase more of a blue or white hue.",
    "location": "National Park Service (Great Smoky Mountains) — Fireflies"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Ateşböceğinin yanıp sönmesinin önemli bir amacı eş çekmektir; her türün kendine özgü bir yanıp sönme deseni vardır.",
    "numbers": [],
    "quote": "The enchanting flash of a firefly serves a vital purpose: attracting a mate. / Each species of firefly possesses a unique flash pattern that plays a crucial role in their mating display.",
    "location": "National Park Service (Great Smoky Mountains) — Fireflies"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Eşzamanlı ateşböceğinde 5 ile 8 arası belirgin parlamayı 8 saniyelik bir karanlık izler.",
    "numbers": [
      "5",
      "8"
    ],
    "quote": "a remarkable sequence of five to eight distinct flashes, followed by an eight-second pause of darkness",
    "location": "National Park Service (Great Smoky Mountains) — Fireflies"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Biyolüminesansı kullanan en ünlü avcı belki de avını cezbetmek için kullanan fener balığıdır.",
    "numbers": [],
    "quote": "The most famous predator to use bioluminescence may be the anglerfish, which uses bioluminescence to lure prey.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Birçok deniz canlısı kendini korumak için karşı aydınlatma denen bir kamuflaj kullanır; baltabalıklarının ışık organları aşağı bakar, alttan çıkan ışığı yukarıdan gelen ışığa eşitler, böylece gölgelerini gizleyip aşağıdan bakan avcılara neredeyse görünmez olurlar.",
    "numbers": [],
    "quote": "Many marine species use a technique called counterillumination to protect themselves. / Hatchetfish have light-producing organs that point downward. / They adjust the amount of light coming from their undersides to match the light coming from above. / they disguise their shadows and become virtually invisible to predators looking up.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Canlılar biyolüminesansı avlanmak, avcılara karşı korunmak ve eş bulmak için kullanır.",
    "numbers": [],
    "quote": "Bioluminescence is used by living things to hunt prey, defend against predators, find mates",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Birçok kalamar türü avcılarını ürkütmek için parlar; bazı böcek larvaları zehirli olduklarını avcılara bildirmek için ışık saçar.",
    "numbers": [],
    "quote": "Many species of squid, for instance, flash to startle predators, such as fish. / light up to warn predators that they are toxic.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Tatlı su ortamlarına özgü ışık saçan canlı neredeyse yoktur.",
    "numbers": [],
    "quote": "There are almost no bioluminescent organisms native to freshwater habitats.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Demiryolu solucanının başı kırmızı, gövdesi yeşil parlar.",
    "numbers": [],
    "quote": "The head of the railroad worm glows red, while its body glows green.",
    "location": "National Geographic Education — Bioluminescence"
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
