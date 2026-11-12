# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Ay neden şekil değiştirir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 8, "paperId": "topic:ay-neden-sekil-degistirir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Moon Phases",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/moon/moon-phases/"
  },
  {
    "id": "k2",
    "title": "What Are the Moon's Phases?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/moon-phases/en/"
  },
  {
    "id": "k3",
    "title": "Moon Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/moon/facts/"
  },
  {
    "id": "k4",
    "title": "Tidal Locking",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/moon/tidal-locking/"
  },
  {
    "id": "k5",
    "title": "The Moon & Eclipses",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/moon/eclipses/"
  },
  {
    "id": "k6",
    "title": "Tides",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/moon/tides/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Ay kendi ışığını üretmez; 'ay ışığı' aslında yansıyan Güneş ışığıdır.",
    "numbers": [],
    "quote": "The Moon does not make its own light. \"Moonlight\" is actually reflected sunlight.",
    "location": "NASA Science — Moon Phases"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.",
    "numbers": [],
    "quote": "The Moon is always half-lit by the Sun.",
    "location": "NASA Science — Moon Phases"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Ay Dünya'nın çevresinde dolandıkça farklı kısımları farklı zamanlarda Güneş ışığında ya da karanlıkta olur; bizim bakış açımızdan Ay'ın evrelerden geçmesinin nedeni budur. Ay'ın biçimi ay boyunca değişmez; değişen bizim görüşümüzdür.",
    "numbers": [],
    "quote": "As the Moon orbits Earth, different parts are in sunlight or darkness at different times. / The changing illumination is why, from our perspective, the Moon goes through phases. / The shape of the Moon isn't changing throughout the month. However, our view of the Moon does change.",
    "location": "NASA Science — Moon Facts; NASA Space Place — What Are the Moon's Phases?"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Sekiz evre sırayla: yeni ay, büyüyen hilal, ilk dördün, büyüyen şişkin ay, dolunay, küçülen şişkin ay, son dördün, küçülen hilal. Şişkin ay evresi yarım ay ile dolunay arasındadır.",
    "numbers": [],
    "quote": "The eight lunar phases are, in order: new Moon, waxing crescent, first quarter, waxing gibbous, full Moon, waning gibbous, third quarter, and waning crescent. / Waxing means it is getting bigger. / Waning means it is getting smaller. / The waxing gibbous phase is between a half moon and full moon.",
    "location": "NASA Science — Moon Phases; NASA Space Place — What Are the Moon's Phases?"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Ay'ın Dünya çevresindeki bir turu yaklaşık 27,3 gün sürer; bir yeni aydan ötekine ise yaklaşık 29,5 gün geçer.",
    "numbers": [
      "27.3",
      "29.5"
    ],
    "quote": "It takes about 27.3 days for the Moon to orbit Earth. / it takes about 29.5 days to go from one new moon to the next new moon.",
    "location": "NASA Space Place — What Are the Moon's Phases?"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Fark, Dünya'nın da hareket etmesinden (Güneş'in çevresinde dolanmasından) kaynaklanır.",
    "numbers": [],
    "quote": "Because Earth is moving as well – rotating on its axis as it orbits the Sun –",
    "location": "NASA Science — Moon Facts"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Ay bize sırtını hiç dönmez; eşinin çevresinde dönerken hep ona bakan bir dansçı gibidir.",
    "numbers": [],
    "quote": "As a result, the Moon never turns its back to us, like a dancer circling ― but always facing ― its partner.",
    "location": "NASA Science — Tidal Locking"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Dünya'dan hiç görmediğimiz yarıküreye (uzak yüz) 'karanlık yüz' denmesi yanıltıcıdır.",
    "numbers": [],
    "quote": "Some people call the far side – the hemisphere we never see from Earth – the \"dark side\", but that's misleading.",
    "location": "NASA Science — Moon Facts"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Ay ortalama 384.400 kilometre uzaklıktadır.",
    "numbers": [
      "384.400"
    ],
    "quote": "The Moon is an average of 238,855 miles (384,400 kilometers) away.",
    "location": "NASA Science — Moon Facts"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Ay'ın genişliği Dünya'nınkinin üçte birinden azdır.",
    "numbers": [],
    "quote": "the Moon is less than a third of the width of Earth.",
    "location": "NASA Science — Moon Facts"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Ay büyük olasılıkla, birkaç milyar yıl önce Mars büyüklüğünde bir cismin Dünya'ya çarpmasından sonra oluştu.",
    "numbers": [],
    "quote": "The Moon likely formed after a Mars-sized body collided with Earth several billion years ago.",
    "location": "NASA Science — Moon Facts"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Ay yılda yaklaşık 3,8 santimetre hızla yavaşça uzaklaşmaktadır.",
    "numbers": [
      "3.8"
    ],
    "quote": "has been slowly drifting outward at the rate of about 1.5 inches (3.8 cm) per year.",
    "location": "NASA Science — The Moon & Eclipses"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Ay tutulmaları dolunay evresinde olur: Dünya tam olarak Ay ile Güneş arasına girince gölgesi Ay'ın yüzeyine düşer. Güneş tutulmaları yalnızca yeni ay evresinde, Ay Dünya ile Güneş arasındayken olur. Ay'ın yörüngesi Dünya'nın yörünge düzlemine göre yaklaşık 5 derece eğiktir.",
    "numbers": [
      "5"
    ],
    "quote": "Lunar eclipses occur at the full Moon phase. / When Earth is positioned precisely between the Moon and Sun, Earth's shadow falls upon the surface of the Moon / Solar eclipses happen only at the new Moon phase, when the Moon is between Earth and the Sun. / The Moon's orbit is tilted about 5 degrees compared to the plane of Earth's orbit around the Sun.",
    "location": "NASA Science — The Moon & Eclipses"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Ay'ın kütle çekimi Dünya'daki gelgitlere yol açar; okyanuslar kabarır.",
    "numbers": [],
    "quote": "The Moon's gravity drives Earth's tides / On Earth, the Moon's gravitational pull causes the oceans to bulge out on both the side closest to the Moon",
    "location": "NASA Science — Tides"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Ay gündüz de sık sık soluk biçimde görülebilir; her gün biraz daha geç doğar; dolunay gün batımı sıralarında doğar.",
    "numbers": [],
    "quote": "it's often visible during the day as a faint, pale presence. / Every day, the Moon rises a little bit later. / A full Moon rises around sunset and sets around sunrise.",
    "location": "NASA Science — Moon Phases"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.",
    "numbers": [],
    "quote": "In our entire solar system, the only object that shines with its own light is the Sun.",
    "location": "NASA Science — Moon Phases"
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
