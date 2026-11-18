# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Güneş nasıl parlar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 45, "paperId": "topic:gunes-nasil-parlar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Sun: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/sun/facts/"
  },
  {
    "id": "k2",
    "title": "All About the Sun",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/all-about-the-sun/en/"
  },
  {
    "id": "k3",
    "title": "Where Does the Sun's Energy Come From?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/sun-heat/en/"
  },
  {
    "id": "k4",
    "title": "Sunspots",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/sun/sunspots/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Yıldız, sıcak ve parlayan bir gaz topudur.",
    "numbers": [],
    "quote": "A star is a hot, glowing ball of gas.",
    "location": "NASA Space Place — All About the Sun"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
    "numbers": [],
    "quote": "The Sun is a huge ball of hydrogen and helium held together by its own gravity.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Çekirdekteki nükleer tepkimelerde hidrojen kaynaşarak helyuma dönüşür ve bu, Güneş'in ısısına ve ışığına güç verir; hidrojen atomları öyle bir kuvvetle çarpışır ki kelimenin tam anlamıyla kaynaşıp yeni bir element olan helyuma dönüşür.",
    "numbers": [],
    "quote": "Nuclear reactions here – where hydrogen is fused to form helium – power the Sun's heat and light. / the hydrogen atoms collide with enough force that they literally meld into a new element—helium.",
    "location": "NASA Science — Sun: Facts; NASA Space Place — Where Does the Sun's Energy Come From?"
  },
  {
    "id": "f4",
    "kind": "number",
    "statement": "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir.",
    "numbers": [
      "15"
    ],
    "quote": "The temperature in the Sun's core is about 27 million degrees Fahrenheit (15 million degrees Celsius)",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Güneş'in iç bölgeleri çekirdek, ışınım bölgesi ve konveksiyon bölgesidir; enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık 170.000 yıl sürer.",
    "numbers": [
      "170.000"
    ],
    "quote": "The interior regions include the core, the radiative zone, and the convection zone. / taking about 170,000 years to get from the core to the top of the convection zone.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Konveksiyon bölgesinde büyük sıcak plazma kabarcıkları fotosfere doğru yükselir.",
    "numbers": [],
    "quote": "large bubbles of hot plasma (a soup of ionized atoms) move upward toward the photosphere",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Güneş'in yüzeyi denen bölüm fotosferdir; sıcaklığı yaklaşık 5.500 santigrat dereceye ulaşır.",
    "numbers": [
      "5.500"
    ],
    "quote": "The part of the Sun commonly called its surface is the photosphere. / with temperatures reaching about 10,000 degrees Fahrenheit (5,500 degrees Celsius)",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f8",
    "kind": "number",
    "statement": "Güneş'in yüzeyinin üstünde ince kromosfer ve dev korona bulunur; korona 2 milyon santigrat dereceye ulaşır, fotosferden çok daha sıcaktır.",
    "numbers": [
      "2"
    ],
    "quote": "Above the Sun's surface are its thin chromosphere and the huge corona (crown). / The corona reaches up to 3.5 million °F (2 million °C) – much, much hotter than the photosphere.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Madde koronadan ses üstü hızlarla ayrılınca güneş rüzgârı olur.",
    "numbers": [],
    "quote": "Once material leaves the corona at supersonic speeds, it becomes the solar wind",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Güneş lekeleri, manyetik alan çizgilerinin yoğunlaşmasıyla oluşan daha serin bölgelerdir; sayıları Güneş'in doğal 11 yıllık döngüsüyle artıp azalır.",
    "numbers": [
      "11"
    ],
    "quote": "Sunspots are cooler regions on the Sun caused by a concentration of magnetic field lines. / The number of sunspots goes up and down as the Sun goes through its natural 11-year cycle.",
    "location": "NASA Science — Sunspots"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Güneş patlamaları ve koronal kütle atımları, Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.",
    "numbers": [],
    "quote": "The latter two are giant explosions of energy and particles that can reach Earth.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Güneş o kadar uzaktadır ki ışığının bize ulaşması yaklaşık 8 dakika 20 saniye sürer.",
    "numbers": [
      "8",
      "20"
    ],
    "quote": "The Sun is so far away that it takes light about 8 minutes and 20 seconds for it to get to us",
    "location": "NASA Space Place — All About the Sun"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Güneş, Dünya'dan yaklaşık 100 kat, en büyük gezegen Jüpiter'den yaklaşık 10 kat daha geniştir; ama ortalama büyüklükte bir yıldızdır.",
    "numbers": [
      "100",
      "10"
    ],
    "quote": "The Sun is about 100 times wider than Earth and about 10 times wider than Jupiter, the biggest planet. / Our Sun is about 100 times wider than Earth, but it is just an average sized star.",
    "location": "NASA Science — Sun: Facts; NASA Space Place — All About the Sun"
  },
  {
    "id": "f14",
    "kind": "number",
    "statement": "Güneş yaklaşık 4,6 milyar yıl önce oluştu; ömrünün yarısından biraz daha azını geçirdi ve beyaz cüceye dönüşmeden önce yaklaşık 5 milyar yıl daha yaşayacak.",
    "numbers": [
      "4.6",
      "5"
    ],
    "quote": "The Sun formed about 4.6 billion years ago / Scientists predict the Sun is a little less than halfway through its lifetime / will last another 5 billion years or so before it becomes a white dwarf.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Güneş'e çok özel koruyucu gözlük olmadan asla doğrudan bakılmamalıdır.",
    "numbers": [],
    "quote": "you should never look directly at the Sun without very special protective eyewear.",
    "location": "NASA Space Place — All About the Sun"
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
