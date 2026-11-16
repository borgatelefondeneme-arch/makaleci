# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Güneş Sistemi'nde hangi gezegenler var?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 23, "paperId": "topic:gunes-sistemi-nde-hangi-gezegenler-var".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Solar System Exploration",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/solar-system/"
  },
  {
    "id": "k2",
    "title": "Solar System: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/solar-system/solar-system-facts/"
  },
  {
    "id": "k3",
    "title": "About the Planets",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/solar-system/planets/"
  },
  {
    "id": "k4",
    "title": "What is a Planet?",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/solar-system/planets/what-is-a-planet/"
  },
  {
    "id": "k5",
    "title": "Jupiter Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/jupiter/jupiter-facts/"
  },
  {
    "id": "k6",
    "title": "Saturn: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/saturn/facts/"
  },
  {
    "id": "k7",
    "title": "Mars: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/mars/facts/"
  },
  {
    "id": "k8",
    "title": "Venus: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/venus/venus-facts/"
  },
  {
    "id": "k9",
    "title": "Pluto: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/dwarf-planets/pluto/facts/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Güneş sistemimizde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ve asteroit vardır.",
    "numbers": [],
    "quote": "Our solar system has one star, eight planets, five dwarf planets, hundreds of moons and thousands of comets and asteroids.",
    "location": "NASA Science — Solar System: Facts"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Güneş sistemimiz yaklaşık 4,6 milyar yıl önce yoğun bir yıldızlar arası gaz ve toz bulutundan oluştu; bulut çöküp dönen bir disk oluşturdu; Güneş mevcut maddenin %99'undan fazlasını topladı.",
    "numbers": [
      "4.6",
      "99"
    ],
    "quote": "Our solar system formed about 4.6 billion years ago from a dense cloud of interstellar gas and dust. / When this dust cloud collapsed, it formed a solar nebula – a spinning, swirling disk of material. / it eventually amassed more than 99% of the available matter.",
    "location": "NASA Science — Solar System: Facts"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Sekiz gezegen: Merkür, Venüs, Dünya, Mars, Jüpiter, Satürn, Uranüs ve Neptün. İlk dördü katı yüzeyleri olduğu için karasal gezegenlerdir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.",
    "numbers": [],
    "quote": "Our solar system has eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. / These inner planets also are known as terrestrial planets because they have solid surfaces. / Jupiter and Saturn are gas giants. Uranus and Neptune are ice giants.",
    "location": "NASA Science — About the Planets"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Asteroit kuşağı, erken güneş sisteminden kalan parçalardan oluşur; Mars ile Jüpiter arasındadır; en büyük cismi cüce gezegen Ceres'tir.",
    "numbers": [],
    "quote": "the asteroid belt is made of bits and pieces of the early solar system / Dwarf planet Ceres is the largest object in the asteroid belt between Mars and Jupiter",
    "location": "NASA Science — Solar System: Facts; NASA Science — About the Planets"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Bir cismin gezegen sayılması için bir yıldızın çevresinde dolanması, küre biçimini alacak kadar kütle çekimine sahip olması ve yörüngesinin çevresini benzer boyuttaki cisimlerden temizlemiş olması gerekir. Plüton 2006'da cüce gezegen olarak yeniden sınıflandırıldı; yörüngesini temizleyemedi.",
    "numbers": [
      "2006"
    ],
    "quote": "It must orbit a star (in our cosmic neighborhood, the Sun). / It must be big enough to have enough gravity to force it into a spherical shape. / its gravity has cleared away any other objects of a similar size near its orbit / Pluto was reclassified as a dwarf planet in 2006 / has not been able to clear its orbit of debris.",
    "location": "NASA Science — What is a Planet?; NASA Science — Pluto: Facts"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Merkür Güneş'e en yakın ve en küçük gezegendir.",
    "numbers": [],
    "quote": "Mercury is the planet nearest to the Sun, and the smallest planet in our solar system.",
    "location": "NASA Science — About the Planets"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Venüs'ün kalın atmosferi ısıyı hapseder ve onu güneş sisteminin en sıcak gezegeni yapar; yüzey sıcaklığı kurşunu eritecek kadardır: yaklaşık 467 santigrat derece; atmosferi çoğunlukla karbondioksittir; Venüs çoğu gezegenin tersi yönde, yavaşça döner.",
    "numbers": [
      "467"
    ],
    "quote": "Its thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system / about 872 degrees Fahrenheit (467 Celsius). / The atmosphere is mostly carbon dioxide / Venus spins slowly in the opposite direction from most planets.",
    "location": "NASA Science — Venus: Facts"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Şimdiye kadar güneş sistemimizde yaşam bulduğumuz tek yer Dünya'dır; Dünya Güneş'ten üçüncü gezegendir.",
    "numbers": [],
    "quote": "So far, Earth is the only place we've found life in our solar system. / Earth – our home planet – is the third planet from the Sun, and the fifth largest planet.",
    "location": "NASA Science — Solar System Exploration; NASA Science — About the Planets"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Mars'ın kırmızı görünmesinin nedeni kayalardaki demirin paslanmasıdır; güneş sisteminin en büyük yanardağı Olympus Mons Mars'tadır; Mars'ın iki küçük uydusu vardır: Phobos ve Deimos.",
    "numbers": [],
    "quote": "The reason Mars looks reddish is due to oxidization — or rusting — of iron in the rocks / Mars is home to the largest volcano in the solar system, Olympus Mons. / Mars has two small moons, Phobos and Deimos",
    "location": "NASA Science — Mars: Facts"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Jüpiter en büyük gezegendir; içi boş bir kabuk olsaydı içine 1.000 Dünya sığardı; Dünya bir üzüm olsaydı Jüpiter bir basketbol topu kadar olurdu; Büyük Kırmızı Leke, Dünya'dan büyük, yüzlerce yıldır süren dev bir fırtınadır; Jüpiter'in Uluslararası Astronomi Birliği'nin resmen tanıdığı 115 uydusu vardır.",
    "numbers": [
      "1.000",
      "115"
    ],
    "quote": "if it were a hollow shell, 1,000 Earths could fit inside. / If Earth were the size of a grape, Jupiter would be about as big as a basketball. / a giant storm bigger than Earth that has raged for hundreds of years. / Jupiter has 115 moons that are officially recognized",
    "location": "NASA Science — Jupiter Facts"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Satürn'ün halkaları, toz gibi maddelerle kaplı milyarlarca küçük buz ve kaya parçasından oluşur; Satürn ortalama yoğunluğu sudan az olan tek gezegendir; Mart 2025 itibarıyla 274 doğrulanmış uydusu vardı.",
    "numbers": [
      "2025",
      "274"
    ],
    "quote": "They are made of billions of small chunks of ice and rock coated with other materials such as dust. / Saturn is the only planet in our solar system with an average density that is less than water. / As of March 2025, Saturn had 274 confirmed moons",
    "location": "NASA Science — Saturn: Facts"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Uranüs Güneş'ten yedinci ve en büyük üçüncü gezegendir; Neptün sekizinci ve en uzak gezegendir.",
    "numbers": [],
    "quote": "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system. / Neptune is the eighth and most distant planet in our solar system.",
    "location": "NASA Science — About the Planets"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Bir astronomik birim, Güneş ile Dünya arasındaki uzaklıktır: yaklaşık 150 milyon kilometre. Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a 13 dakikada, Jüpiter'e 43 dakikada, Satürn'e 80 dakikada ulaşır.",
    "numbers": [
      "150",
      "13",
      "43",
      "80"
    ],
    "quote": "One astronomical unit (or AU) is the distance from the Sun to Earth, or about 93 million miles (150 million kilometers). / about eight minutes for the Sun and Earth / it takes sunlight 13 minutes to travel from the Sun to Mars / 43 minutes to travel from the Sun to Jupiter / 80 minutes to travel from the Sun to Saturn",
    "location": "NASA Science — Solar System: Facts; NASA Science — Venus: Facts; NASA Science — Mars: Facts; NASA Science — Jupiter Facts; NASA Science — Saturn: Facts"
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
