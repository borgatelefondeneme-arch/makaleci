# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Okyanusun derinlerinde ne var?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 15, "paperId": "topic:okyanusun-derinlerinde-ne-var".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "How far does light travel in the ocean?",
    "publisher": "NOAA",
    "url": "https://oceanservice.noaa.gov/facts/light_travel.html"
  },
  {
    "id": "k2",
    "title": "How deep is the ocean?",
    "publisher": "NOAA",
    "url": "https://oceanexplorer.noaa.gov/facts/ocean-depth.html"
  },
  {
    "id": "k3",
    "title": "How much of the ocean has been explored?",
    "publisher": "NOAA",
    "url": "https://oceanexplorer.noaa.gov/facts/explored.html"
  },
  {
    "id": "k4",
    "title": "What is bioluminescence?",
    "publisher": "NOAA",
    "url": "https://oceanexplorer.noaa.gov/facts/bioluminescence.html"
  },
  {
    "id": "k5",
    "title": "What is a hydrothermal vent?",
    "publisher": "NOAA",
    "url": "https://oceanservice.noaa.gov/facts/vents.html"
  },
  {
    "id": "k6",
    "title": "How does pressure change with ocean depth?",
    "publisher": "NOAA",
    "url": "https://oceanservice.noaa.gov/facts/pressure.html"
  },
  {
    "id": "k7",
    "title": "Bioluminescence",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/bioluminescence/"
  },
  {
    "id": "k8",
    "title": "How much water is in the ocean?",
    "publisher": "NOAA",
    "url": "https://oceanservice.noaa.gov/facts/oceanwater.html"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "number",
    "statement": "Okyanus gezegenimizin yüzeyinin %70'inden fazlasını kaplar; Dünya'daki suyun yaklaşık %97'si okyanustadır.",
    "numbers": [
      "70",
      "97"
    ],
    "quote": "The ocean covers more than 70 percent of the surface of our planet. / About 97 percent of Earth's water is in the ocean.",
    "location": "NOAA — How much water is in the ocean?"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Okyanusun ortalama derinliği 3.682 metredir.",
    "numbers": [
      "3.682"
    ],
    "quote": "The average depth of the ocean is 3,682 meters, or 12,080 feet.",
    "location": "NOAA Ocean Exploration — How deep is the ocean?"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Okyanusun üst 200 metresine öfotik, yani 'güneşli' bölge denir.",
    "numbers": [
      "200"
    ],
    "quote": "The upper 200 meters of the ocean is called the euphotic, or \"sunlight,\" zone.",
    "location": "NOAA — How far does light travel in the ocean?"
  },
  {
    "id": "f4",
    "kind": "number",
    "statement": "200–1.000 metre arası genellikle 'alacakaranlık' bölgesi olarak anılır; 200 metrenin ötesinde kayda değer ışık nadiren bulunur.",
    "numbers": [
      "200",
      "1.000"
    ],
    "quote": "is usually referred to as the \"twilight\" zone, but is officially the dysphotic zone / there is rarely any significant light beyond 200 meters",
    "location": "NOAA — How far does light travel in the ocean?"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Afotik bölge 1.000 metrenin altındadır; Güneş ışığı ulaşmaz, bölge karanlıktır.",
    "numbers": [
      "1.000"
    ],
    "quote": "The aphotic zone exists in depths below 1,000 meters. / sunlight does not penetrate; the zone is bathed in darkness",
    "location": "NOAA — How far does light travel in the ocean?"
  },
  {
    "id": "f6",
    "kind": "number",
    "statement": "200 metrenin ötesine o kadar az ışık ulaşır ki fotosentez artık mümkün olmaz.",
    "numbers": [
      "200"
    ],
    "quote": "Such a minuscule amount of light penetrates beyond a depth of 200 meters that photosynthesis is no longer possible.",
    "location": "NOAA — How far does light travel in the ocean?"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Her 33 fitte (10,06 metre) basınç bir atmosfer artar; deniz seviyesinde çevremizdeki hava bedenimize basınç uygular.",
    "numbers": [
      "10.06"
    ],
    "quote": "For every 33 feet (10.06 meters) you go down, the pressure increases by one atmosphere. / At sea level, the air that surrounds us presses down on our bodies at 14.7 pounds per square inch.",
    "location": "NOAA — How does pressure change with ocean depth?"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Denizde ne kadar derine inilirse üstteki suyun aşağı doğru yaptığı basınç o kadar artar; balinalar bedenleri daha esnek olduğu için büyük basınç değişimlerine dayanabilir.",
    "numbers": [],
    "quote": "The deeper you go under the sea, the greater the pressure of the water pushing down on you. / Whales, for instance, can withstand dramatic pressure changes because their bodies are more flexible.",
    "location": "NOAA — How does pressure change with ocean depth?"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Okyanusun en derin yeri 10.935 metredir; Büyük Okyanus'taki Mariana Çukuru'nda, Challenger Derinliği denen yerdedir.",
    "numbers": [
      "10.935"
    ],
    "quote": "The deepest place in the ocean measures 10,935 meters (35,876 feet) / found in the Pacific Ocean's Mariana Trench, at a place called Challenger Deep",
    "location": "NOAA Ocean Exploration — How deep is the ocean?"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Biyolüminesans, bir canlının kimyasal tepkimeyle ürettiği ışıktır; okyanusta çok yaygındır; 200 ile 1.000 metre arasında yaşayan hayvanların %80'i biyolüminesanstır.",
    "numbers": [
      "200",
      "1.000",
      "80"
    ],
    "quote": "Bioluminescence is light produced by an organism using a chemical reaction. / bioluminescence is very common in the ocean / 80 percent of the animals that live between 200 and 1,000 meters (656 and 3,280 feet) depth are bioluminescent",
    "location": "NOAA Ocean Exploration — What is bioluminescence?"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Biyolüminesans 'soğuk ışıktır': çok az ısı yayar. Işığı asıl üreten bileşik lusiferindir.",
    "numbers": [],
    "quote": "Bioluminescence is a \"cold light.\" Cold light means less than 20% of the light generates thermal radiation, or heat. / Luciferin is the compound that actually produces light.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Canlılar biyolüminesansı av yakalamak, avcılardan korunmak ve eş bulmak için kullanır; yine de asıl amacı ya da işlevi tam olarak bilinmiyor.",
    "numbers": [],
    "quote": "Bioluminescence is used by living things to hunt prey, defend against predators, find mates / we don't really know the main purpose or function of bioluminescence",
    "location": "National Geographic Education — Bioluminescence; NOAA Ocean Exploration — What is bioluminescence?"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Fener balığı avını çekmek için biyolüminesans kullanır; ipliğin ucundaki topu yakabilir.",
    "numbers": [],
    "quote": "The most famous predator to use bioluminescence may be the anglerfish, which uses bioluminescence to lure prey. / On the end of the filament is a ball (called the esca) that the anglerfish can light up.",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Vampir kalamar, avcıları ürkütüp şaşırtan ve oyalayan yapışkan, biyolüminesans bir salgı fırlatır.",
    "numbers": [],
    "quote": "the vampire squid ejects sticky bioluminescent mucus, which can startle, confuse, and delay predators",
    "location": "National Geographic Education — Bioluminescence"
  },
  {
    "id": "f15",
    "kind": "number",
    "statement": "Hidrotermal bacalar deniz suyunun magmayla karşılaştığı yerlerde oluşur; buradaki sıcak su, derinlikteki aşırı basınç nedeniyle kaynamaz; ilk kez 1977'de Galapagos Adaları yakınında keşfedildi ve çevrelerinde daha önce hiç görülmemiş çok sayıda canlı vardı.",
    "numbers": [
      "1977"
    ],
    "quote": "Hydrothermal vents form at locations where seawater meets magma. / Hot seawater in hydrothermal vents does not boil because of the extreme pressure at the depths / Scientists first discovered hydrothermal vents in 1977 while exploring an oceanic spreading ridge near the Galapagos Islands. / the hydrothermal vents were surrounded by large numbers of organisms that had never been seen before",
    "location": "NOAA — What is a hydrothermal vent?"
  },
  {
    "id": "f16",
    "kind": "number",
    "statement": "Nisan 2026 itibarıyla küresel deniz tabanının %28,7'sinin haritası çıkarılmıştı; kâşifler derin okyanus tabanının %0,001'inden azını görmüştür.",
    "numbers": [
      "2026",
      "28.7",
      "0.001"
    ],
    "quote": "As of April 2026, 28.7% of the global seafloor had been mapped / explorers have seen less than 0.001% of the deep ocean seafloor",
    "location": "NOAA Ocean Exploration — How much of the ocean has been explored?"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Derinler, uzaktan kumandalı araçlar gibi dalış araçlarıyla ve genellikle gemilere takılan sonarla incelenir.",
    "numbers": [],
    "quote": "deploy submersibles, like remotely operated vehicles / usually mounted to ships, that can reveal the seafloor in greater detail",
    "location": "NOAA Ocean Exploration — How much of the ocean has been explored?"
  },
  {
    "id": "f18",
    "kind": "number",
    "statement": "Bilim insanlarının tahminine göre okyanusta 700.000 ile 1 milyon arasında tür olabilir.",
    "numbers": [
      "700.000",
      "1"
    ],
    "quote": "Scientists estimate there may be between 700,000 and 1 million species in the ocean",
    "location": "NOAA Ocean Exploration — How much of the ocean has been explored?"
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
