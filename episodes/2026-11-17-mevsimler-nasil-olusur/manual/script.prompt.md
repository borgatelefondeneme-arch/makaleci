# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Mevsimler nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 30, "paperId": "topic:mevsimler-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "What Causes the Seasons?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/seasons/en/"
  },
  {
    "id": "k2",
    "title": "Season",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/season/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Mevsimlere Dünya'nın eğik ekseni yol açar; Dünya'nın ekseni dimdik durmaz; Dünya yörünge düzlemine göre eksenine eğiktir.",
    "numbers": [],
    "quote": "Earth's tilted axis causes the seasons. / Earth has seasons because its axis doesn't stand up straight. / Seasons occur because Earth is tilted on its axis relative to the orbital plane,",
    "location": "NASA Space Place — What Causes the Seasons?; National Geographic Education — Season"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Dünya Güneş'in çevresinde dolanırken eğik ekseni hep aynı yöne bakar.",
    "numbers": [],
    "quote": "As Earth orbits the Sun, its tilted axis always points in the same direction.",
    "location": "NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Dünya bu eksen çevresinde döner ve her gün bir tam tur atar.",
    "numbers": [],
    "quote": "Earth spins around this pole, making one complete turn each day.",
    "location": "NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Kuzey Kutbu Güneş'e doğru eğikken (Haziran civarı) Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir ve orada yaz olur.",
    "numbers": [],
    "quote": "Sometimes it is the North Pole tilting toward the Sun (around June) / the Sun's rays hit that part of Earth more directly than at any other time of the year / So, when the North Pole tilts toward the Sun, it's summer in the Northern Hemisphere.",
    "location": "NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Bir yarım küre Güneş'ten uzağa eğikken daha az güneş ışığı alır ve kış olur.",
    "numbers": [],
    "quote": "When it is pointing away, there is less sunlight, leading to winter.",
    "location": "NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Güneş'e doğru eğik yarım küre daha fazla gün ışığı saati alır; Aralık'ta Güneş'ten uzağa eğik olan Kuzey Yarım Küre daha az gün ışığı saati alır.",
    "numbers": [],
    "quote": "This means it gets more hours of daylight. / In December, when the Northern Hemisphere is tilted away from the sun, it receives fewer hours of daylight.",
    "location": "National Geographic Education — Season"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Kuzey Yarım Küre'deki mevsimler Güney Yarım Küre'dekilerin tersidir.",
    "numbers": [],
    "quote": "The seasons in the Northern Hemisphere are the opposite of those in the Southern Hemisphere. / As the poles are on opposite ends of Earth, they experience opposite timing for the seasons.",
    "location": "National Geographic Education — Season; NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Pek çok kişi yazın Dünya'nın Güneş'e daha yakın olduğunu sanır; oysa Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir; yani uzaklık mevsimlerin nedeni değildir.",
    "numbers": [],
    "quote": "Many people believe that Earth is closer to the Sun in the summer and that is why it is hotter. / aphelion (when Earth is farthest from the Sun) occurs in July, and perihelion (when we are closest) occurs in January. / That just goes to prove that Earth's distance from the Sun is not the cause of the seasons.",
    "location": "NASA Space Place — What Causes the Seasons?"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Yaz 20 ya da 21 Haziran'daki yaz gündönümüyle başlar; bu, yılın en çok gün ışığı olan günüdür; kış gündönümü en kısa gündüzün olduğu gündür.",
    "numbers": [
      "20",
      "21"
    ],
    "quote": "Summer begins on June 20 or 21, the summer solstice, which has the most daylight of any day in the year. / This is the winter solstice, the day of the year with the shortest period of daylight.",
    "location": "National Geographic Education — Season"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "İlkbahar ve sonbahar, gece ile gündüzün eşit olduğu ekinokslarla başlar; ilkbahar ekinoksu 20 ya da 21 Mart'ta, sonbahar ekinoksu 22 ya da 23 Eylül'dedir.",
    "numbers": [
      "20",
      "21",
      "22",
      "23"
    ],
    "quote": "Spring and fall, or autumn, begin on equinoxes, days that have equal amounts of daylight and darkness. / The vernal, or spring, equinox falls on March 20 or 21, and the autumnal equinox is on September 22 or 23.",
    "location": "National Geographic Education — Season"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Helsinki'de Haziran ortasında 18,5 saat gün ışığı olur; Atina'da Haziran'da 14,5, Aralık'ta 9,5 saat gün ışığı vardır.",
    "numbers": [
      "18.5",
      "14.5",
      "9.5"
    ],
    "quote": "Helsinki, Finland, sees 18.5 hours of daylight in the middle of June. / It has 14.5 hours of daylight in June and 9.5 hours in December.",
    "location": "National Geographic Education — Season"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Alaska'daki Barrow'da Mayıs ortasından Ağustos başına kadar gün boyu aydınlık olur; Kasım ortasından Ocak'a kadar ise tam karanlık hüküm sürer.",
    "numbers": [],
    "quote": "stays light all day long between mid-May and early August / in total darkness between mid-November and January",
    "location": "National Geographic Education — Season"
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
