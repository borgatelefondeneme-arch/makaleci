# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Yağmur nasıl yağar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 16, "paperId": "topic:yagmur-nasil-yagar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Water cycle",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/special-topics/water-science-school/science/water-cycle"
  },
  {
    "id": "k2",
    "title": "Condensation and the Water Cycle",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/special-topics/water-science-school/science/condensation-and-water-cycle"
  },
  {
    "id": "k3",
    "title": "Precipitation and the Water Cycle",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/special-topics/water-science-school/science/precipitation-and-water-cycle"
  },
  {
    "id": "k4",
    "title": "Evaporation and the Water Cycle",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/special-topics/water-science-school/science/evaporation-and-water-cycle"
  },
  {
    "id": "k5",
    "title": "How Much Water is There on Earth?",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/special-topics/water-science-school/science/how-much-water-there-earth"
  },
  {
    "id": "k6",
    "title": "Water Cycle",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/water-cycle/"
  },
  {
    "id": "k7",
    "title": "The water cycle",
    "publisher": "NOAA",
    "url": "https://www.noaa.gov/education/resource-collections/freshwater/water-cycle"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Su döngüsü, suyun Dünya'da nerede olduğunu ve nasıl hareket ettiğini anlatır; su hiçbir zaman yerinde durmaz; suyun sürekli hareketini Güneş'in enerjisi ve kütle çekimi sağlar.",
    "numbers": [],
    "quote": "The water cycle describes where water is on Earth and how it moves. / Water is never sitting still. / Energy from the sun and the force of gravity drive the continual movement of water between pools.",
    "location": "USGS Water Science School — Water cycle; USGS Water Science School — How Much Water is There on Earth?"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Buharlaşma, sıvı suyu gaz hâlindeki suya (su buharına) çeviren süreçtir. Atmosferdeki nemin çoğu (yaklaşık %90) okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir; gerisi bitki terlemesinden ve çok az miktarda süblimleşmeden gelir.",
    "numbers": [
      "90"
    ],
    "quote": "Evaporation is the process that changes liquid water to gaseous water (water vapor). / Most of the moisture in the atmosphere (about 90%) came from water evaporating from oceans, seas, lakes, and rivers. / The rest of the moisture in the atmosphere came from plant transpiration and (a very small amount) from sublimation.",
    "location": "USGS Water Science School — Evaporation and the Water Cycle"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Terleme: sıvı su bitkilerin yapraklarından buharlaşır.",
    "numbers": [],
    "quote": "Liquid water evaporates from the leaves of plants in a process called transpiration.",
    "location": "NOAA — The water cycle"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Bulutlar, su buharı içeren hava yükselip soğuduğu için oluşur; su molekülleri havadaki minik toz, tuz ve duman parçacıklarıyla birleşir. Yoğuşma bulutların oluşumundan sorumludur.",
    "numbers": [],
    "quote": "Clouds form in the atmosphere because air containing water vapor rises and cools. / water molecules will combine with tiny particles of dust, salt, and smoke in the air / Condensation is crucial to the water cycle because it is responsible for the formation of clouds.",
    "location": "USGS Water Science School — Condensation and the Water Cycle"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Bulut damlacıkları yağış olarak düşemeyecek kadar küçüktür ama görünür bulutlar oluşturacak kadar büyüktür; bulutu oluşturan yükselen hava onu havada tutar; bir bulut tonlarca ağırlıkta olsa da düşmez.",
    "numbers": [],
    "quote": "These droplets are way too small to fall as precipitation, but they are large enough to form visible clouds. / the rising air responsible for its formation keeps the cloud floating in the air / Even though a cloud weighs tons, it doesn’t fall on you",
    "location": "USGS Water Science School — Precipitation and the Water Cycle; USGS Water Science School — Condensation and the Water Cycle"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir; yeterince çarpışma olur ve damlanın düşme hızı bulutun yükselen hava hızını aşarsa damla düşer.",
    "numbers": [],
    "quote": "millions of cloud droplets are required to produce a single raindrop. / If enough collisions occur to produce a droplet with a fall velocity which exceeds the cloud updraft speed",
    "location": "USGS Water Science School — Precipitation and the Water Cycle"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Yarıçapı 1 milimetreden küçük yağmur damlaları top gibi küreseldir; yaklaşık 2–3 milimetre çapta alt kısım oldukça düzdür: hamburger ekmeği gibi.",
    "numbers": [
      "1",
      "2",
      "3"
    ],
    "quote": "Small raindrops, those with a radius of less than 1 millimeter (mm), are spherical, like a round ball. / at about 2-3 mm in diameter the bottom is quite flat with an indention in the middle - much like a hamburger bun.",
    "location": "USGS Water Science School — Precipitation and the Water Cycle"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Yağış, bulutlardan yağmur, donan yağmur, sulu kar, kar ya da dolu biçiminde bırakılan sudur.",
    "numbers": [],
    "quote": "Precipitation is water released from clouds in the form of rain, freezing rain, sleet, snow, or hail.",
    "location": "USGS Water Science School — Water cycle"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Su, süzülme ve yeraltı suyu beslenmesiyle toprağa girer; yeraltı suyu akiferlerde akar; nehirlere, okyanusa ve kaynaklara boşalarak yüzeye dönebilir. Suyun bir kısmı toprağa sızar ve yeraltı suyu olarak tutulur.",
    "numbers": [],
    "quote": "Water moves into the ground through infiltration and groundwater recharge. / Underground, groundwater flows within aquifers. / Groundwater can return to the surface through natural discharge into rivers, the ocean, and from springs. / Some of it seeps into the soil where it is held underground as groundwater.",
    "location": "USGS Water Science School — Water cycle; National Geographic Education — Water Cycle"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Buharlaşan bir su molekülü havada yaklaşık 10 gün kalır.",
    "numbers": [
      "10"
    ],
    "quote": "Once evaporated, a water molecule spends about 10 days in the air.",
    "location": "USGS Water Science School — Evaporation and the Water Cycle"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Okyanuslar Dünya'daki suyun yaklaşık %97'sini tutar; tatlı su Dünya'daki suyun %2,5'idir; tatlı suyun yaklaşık %68'i donmuş hâldedir; yaklaşık %30'u yer altındadır.",
    "numbers": [
      "97",
      "2.5",
      "68",
      "30"
    ],
    "quote": "The oceans hold about 97% of the water on Earth. / Freshwater makes up 2.5% of Earth’s water. / The water frozen in these pools accounts for approximately 68% of freshwater. / This liquid water is below ground and accounts for approximately 30% of freshwater.",
    "location": "National Geographic Education — Water Cycle; NOAA — The water cycle"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Dünya'daki suyun çok küçük bir bölümü, yalnızca %0,001'i, atmosferde su buharı olarak bulunur.",
    "numbers": [
      "0.001"
    ],
    "quote": "A tiny fraction—just 0.001%—exists in Earth’s atmosphere as water vapor.",
    "location": "National Geographic Education — Water Cycle"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Dünya'nın su döngüsü yaklaşık 3,8 milyar yıl önce, soğuyan Dünya'ya yağmur yağıp okyanuslar oluştuğunda başladı.",
    "numbers": [
      "3.8"
    ],
    "quote": "Earth’s water cycle began about 3.8 billion years ago when rain fell on a cooling Earth, forming the oceans.",
    "location": "National Geographic Education — Water Cycle"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Su Dünya'daki yaşam için vazgeçilmezdir; su, döngünün her bölümünde insanların kullanımına uygun değildir.",
    "numbers": [],
    "quote": "Water is essential to life on Earth. / Water isn’t available for people to use in every part of the cycle",
    "location": "NOAA — The water cycle"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Süblimleşmede buz ya da kar gibi katı su, sıvılaşmadan doğrudan su buharına dönüşebilir.",
    "numbers": [],
    "quote": "In a process called sublimation, solid water, such as ice or snow, can transform directly into water vapor without first becoming a liquid.",
    "location": "National Geographic Education — Water Cycle"
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
            "storm"
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
