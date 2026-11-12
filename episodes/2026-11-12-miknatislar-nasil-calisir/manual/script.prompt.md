# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Mıknatıslar nasıl çalışır?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 18, "paperId": "topic:miknatislar-nasil-calisir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Magnetism",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/magnetism/"
  },
  {
    "id": "k2",
    "title": "Earth's Magnetosphere",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/science-research/earth-science/earths-magnetosphere/"
  },
  {
    "id": "k3",
    "title": "What Is an Aurora?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/aurora/en/"
  },
  {
    "id": "k4",
    "title": "Wandering of the Geomagnetic Poles",
    "publisher": "NOAA",
    "url": "https://www.ncei.noaa.gov/products/wandering-geomagnetic-poles"
  },
  {
    "id": "k5",
    "title": "An Overview of the Earth's Magnetic Field",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://geomag.bgs.ac.uk/education/earthmag.html"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir; elektrik yüklerinin hareketinden kaynaklanır; manyetik alan, mıknatısın çevresinde manyetik kuvvetin etkili olduğu bölgedir.",
    "numbers": [],
    "quote": "Magnetism is the force exerted by magnets when they attract or repel each other / Magnetism is caused by the motion of electric charges. / The magnetic field is the area around a magnet that has magnetic force.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Bütün mıknatısların kuzey ve güney kutbu vardır; zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.",
    "numbers": [],
    "quote": "All magnets have north and south poles. / Opposite poles are attracted to each other, while the same poles repel each other.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Elektronlar topaç gibi dönerek atom çekirdeğinin çevresinde dolanır; bu hareket her elektronun mikroskobik bir mıknatıs gibi davranmasına yol açar.",
    "numbers": [],
    "quote": "Spinning like tops, the electrons circle the nucleus, or core, of an atom. / Their movement generates an electric current and causes each electron to act like a microscopic magnet.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Demir, kobalt ve nikel gibi maddelerde elektronların çoğu aynı yönde döner; çoğu maddede eşit sayıda elektron zıt yönlerde döner ve manyetizmalarını birbirine sıfırlar; bu yüzden kumaş ya da kâğıt zayıf manyetik sayılır.",
    "numbers": [],
    "quote": "In substances such as iron, cobalt, and nickel, most of the electrons spin in the same direction. / In most substances, equal numbers of electrons spin in opposite directions, which cancels out their magnetism. / That is why materials such as cloth or paper are said to be weakly magnetic.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Bir tel bobininden elektrik geçince manyetik alan oluşur; akım kesilince bobinin çevresindeki alan kaybolur.",
    "numbers": [],
    "quote": "When electricity runs through a coil of wire, it produces a magnetic field. / The field around the coil will disappear, however, as soon as the electric current is turned off.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Dünya'nın manyetik alanı, sıvı dış çekirdekte kendi kendini besleyen bir dinamo süreciyle oluşur; yavaş hareket eden erimiş demirde akan elektrik akımları manyetik alanı üretir.",
    "numbers": [],
    "quote": "The Earth's magnetic field is generated in the fluid outer core by a self-exciting dynamo process. / Electrical currents flowing in the slowly moving molten iron generate the magnetic field.",
    "location": "British Geological Survey — An Overview of the Earth's Magnetic Field"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Jeomanyetik kutuplar Kuzey ve Güney Kutbu ile aynı değildir; mıknatısın kuzey ucu, güney manyetik yük taşıyan Kuzey Manyetik Kutbu'nu gösterir.",
    "numbers": [],
    "quote": "The geomagnetic poles are not the same as the North and South Poles. / The north end of a magnet points toward the North Magnetic Pole, which holds a south magnetic charge.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f8",
    "kind": "number",
    "statement": "Son ölçüme göre Kuzey Manyetik Kutbu yılda yaklaşık 55 kilometre hızla kuzey-kuzeybatıya doğru ilerliyor; Kanada Arktiği boyunca yavaşça sürükleniyor.",
    "numbers": [
      "55"
    ],
    "quote": "The most recent survey determined that the Pole is moving approximately north-northwest at 55km per year. / the North Magnetic Pole, which is slowly drifting across the Canadian Arctic",
    "location": "NOAA NCEI — Wandering of the Geomagnetic Poles"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Jeomanyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirdi; bu dönüşler yavaş ve düzensiz olur.",
    "numbers": [],
    "quote": "the geomagnetic poles have reversed—changed into the opposite kind of pole—hundreds of times since Earth formed. / These reversals occur slowly and irregularly",
    "location": "National Geographic Education — Magnetism; British Geological Survey — An Overview of the Earth's Magnetic Field"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Manyetosfer, Güneş'ten saatte 1 milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır; Dünya'yı parçacıkların çoğundan korur.",
    "numbers": [
      "1"
    ],
    "quote": "It deflects most of the solar material sweeping towards us from our star at 1 million miles per hour or more. / The magnetosphere protects Earth from most of the particles, but some leak through it and become trapped.",
    "location": "NASA Science — Earth's Magnetosphere; National Geographic Education — Magnetism"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Mars, manyetosferini yaklaşık 4,2 milyar yıl önce kaybetmiş bir gezegendir.",
    "numbers": [
      "4.2"
    ],
    "quote": "Compare Earth to Mars – a planet that lost its magnetosphere about 4.2 billion years ago.",
    "location": "NASA Science — Earth's Magnetosphere"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Parçacıklar atmosferdeki gazlarla etkileşir ve gökyüzünde güzel ışık gösterileri oluşur; oksijen yeşil ve kırmızı, azot mavi ve mor ışık verir; Kuzey Kutbu yakınında buna kuzey ışıkları denir.",
    "numbers": [],
    "quote": "There, the particles interact with gases in our atmosphere resulting in beautiful displays of light in the sky. / Oxygen gives off green and red light. Nitrogen glows blue and purple. / If you're near the North Pole, it is called an aurora borealis or northern lights.",
    "location": "NASA Space Place — What Is an Aurora?"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Pusulanın manyetik iğnesi Dünya'nın manyetik kutuplarıyla aynı hizaya gelir; insanlar yüzlerce yıldır yön bulmak için pusula kullanıyor.",
    "numbers": [],
    "quote": "The magnetic needle of a compass lines up with Earth’s magnetic poles. / For hundreds of years, people have used magnetic compasses to navigate using Earth’s magnetic field.",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f14",
    "kind": "number",
    "statement": "Eski Yunanlılar ve Çinliler mıknatıs taşı denen doğal manyetik taşları biliyordu; Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslayabileceklerini keşfetti; pusulayla yön bulmaya ilişkin en eski yazılar 11. yüzyıla aittir.",
    "numbers": [
      "11"
    ],
    "quote": "The ancient Greeks and Chinese knew about naturally magnetic stones called \"lodestones.\" / The Chinese discovered that they could make a needle magnetic by stroking it against a lodestone / The earliest writings about compass navigation are credited to the Chinese and date from 11th century A.D.",
    "location": "National Geographic Education — Magnetism; British Geological Survey — An Overview of the Earth's Magnetic Field"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Güvercinler, arılar ve somonlar gibi bazı hayvanlar Dünya'nın manyetik alanını algılayıp yön bulmak için kullanabilir; bilim insanları bunu nasıl yaptıklarından emin değil.",
    "numbers": [],
    "quote": "Some animals, such as pigeons, bees, and salmon, can detect Earth's magnetic field and use it to navigate. / Scientists aren't sure how they do this",
    "location": "National Geographic Education — Magnetism"
  },
  {
    "id": "f16",
    "kind": "number",
    "statement": "Son zamanların en şiddetli manyetik fırtınası Mart 1989'da oldu; Kanada'nın Quebec eyaletinde elektrik iletim sistemi 9 saatten uzun süre kapandı.",
    "numbers": [
      "1989",
      "9"
    ],
    "quote": "The most severe magnetic storm in recent times occurred in March 1989 / the power transmission system in Quebec, Canada, was shut down for over 9 hours.",
    "location": "British Geological Survey — An Overview of the Earth's Magnetic Field"
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
