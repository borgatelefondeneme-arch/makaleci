# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Kaslarımız nasıl çalışır?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 37, "paperId": "topic:kaslarimiz-nasil-calisir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Bones, Muscles & Joints",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/muscles.html"
  },
  {
    "id": "k2",
    "title": "Muscle",
    "publisher": "Cleveland Clinic",
    "url": "https://my.clevelandclinic.org/health/body/21887-muscle"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "number",
    "statement": "Vücudumuzda neredeyse sürekli kullandığımız 600'den fazla kas vardır.",
    "numbers": [
      "600"
    ],
    "quote": "You have more than 600 muscles in your body that you use almost constantly.",
    "location": "Cleveland Clinic — Muscle"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "İnsanlarda üç tür kas vardır: iskelet kası, düz kas ve kalp kası.",
    "numbers": [],
    "quote": "Humans have three different kinds of muscle: / There are three types of muscle tissue in your body:",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints; Cleveland Clinic — Muscle"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "İskelet kası bacaklarda, kollarda ve yüzde olduğu gibi kemiğe kordon gibi tendonlarla bağlıdır; hareketlerini kontrol edebildiğimiz için istemli kas denir.",
    "numbers": [],
    "quote": "Skeletal muscle is attached by cord-like tendons to bone, such as in the legs, arms, and face. / known as voluntary muscles because you can control their movement",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "İskelet kasları hızlı ve güçlü kasılabilir ama çabuk yorulur.",
    "numbers": [],
    "quote": "They can contract (shorten or tighten) quickly and powerfully, but they tire easily.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Düz kaslar istemsizdir; onları bilinçli olarak kontrol edemeyiz, sinir sistemi otomatik olarak kontrol eder; bazı organların içini kaplarlar.",
    "numbers": [],
    "quote": "Smooth, or involuntary, muscle / We can't consciously control our smooth muscles; rather, they're controlled by the nervous system automatically / Smooth muscles are involuntary muscles that line the inside of some organs.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints; Cleveland Clinic — Muscle"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Kalp kası kalpte bulunur; ritmik ve güçlü kasılmalarıyla kanı kalpten dışarı iter; kalp istemsiz bir kastır, kendiliğinden atar ve günde binlerce kez atar.",
    "numbers": [],
    "quote": "Cardiac muscle is found in the heart. / Its rhythmic, powerful contractions force blood out of the heart as it beats. / Your heart is an involuntary muscle — it beats on its own without your input. / beats thousands of times a day to keep you alive.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints; Cleveland Clinic — Muscle"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Kaslar vücut bölümlerini kasılıp gevşeyerek hareket ettirir; kaslar eklemleri çekerek hareket etmemizi sağlar.",
    "numbers": [],
    "quote": "Muscles move body parts by contracting and then relaxing. / Muscles pull on the joints, allowing us to move.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Kaslar kemikleri çekebilir ama geri itemez; bu yüzden bükücü ve açıcı kaslar olarak çiftler halinde çalışır; üst kolun önündeki biseps bükücü, arkasındaki triseps açıcıdır.",
    "numbers": [],
    "quote": "Muscles can pull bones, but they can't push them back to the original position. / So they work in pairs of flexors and extensors. / the biceps muscle, in the front of the upper arm, is a flexor / the triceps, at the back of the upper arm, is an extensor",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Kaslar birbirine örülmüş binlerce küçük liften oluşur; bazı kas lifleri hızlı kasılır ve kısa enerji patlamaları kullanır.",
    "numbers": [],
    "quote": "Your muscles are made of thousands of small fibers woven together. / Some muscle fibers contract quickly and use short bursts of energy (fast-twitch muscles).",
    "location": "Cleveland Clinic — Muscle"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Kasların hareketlerini beyin ve sinir sistemi düzenler ve kontrol eder.",
    "numbers": [],
    "quote": "The movements your muscles make are coordinated and controlled by the brain and nervous system.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Hiç kıpırdamadan otururken bile vücudumuzdaki kaslar sürekli hareket eder.",
    "numbers": [],
    "quote": "Even when we sit perfectly still, muscles throughout the body are constantly moving.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Egzersizden önce esneme ve ısınma kas sakatlıklarını önlemenin en iyi yoludur.",
    "numbers": [],
    "quote": "Stretching and warming up before exercise or physical activity are the best ways to prevent muscle injuries.",
    "location": "Cleveland Clinic — Muscle"
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
