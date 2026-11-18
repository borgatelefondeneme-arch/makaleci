# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Böbreklerimiz ne işe yarar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 47, "paperId": "topic:bobreklerimiz-ne-ise-yarar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Urinary System & Kidneys",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/kidneys.html"
  },
  {
    "id": "k2",
    "title": "Your Kidneys & How They Work",
    "publisher": "NIDDK",
    "url": "https://www.niddk.nih.gov/health-information/kidney-disease/kidneys-how-they-work"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır; kaburgaların hemen altında, omurganın iki yanında birer tane bulunur.",
    "numbers": [],
    "quote": "The kidneys are two bean-shaped organs, each about the size of a fist. / They are located just below the rib cage, one on each side of your spine.",
    "location": "NIDDK (NIH) — Your Kidneys & How They Work"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "İnsanların genellikle iki böbreği vardır ama tek böbrekle de normal, sağlıklı bir yaşam sürebilirler.",
    "numbers": [],
    "quote": "People usually have two kidneys, but can live a normal, healthy life with just one.",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Her böbrek, nefron denen yaklaşık bir milyon süzme biriminden oluşur; bu minik birimler zararlı maddeleri kandan uzaklaştırır.",
    "numbers": [],
    "quote": "Each of your kidneys is made up of about a million filtering units called nephrons. / one million tiny filtering units in each kidney that remove the harmful substances from the blood.",
    "location": "NIDDK (NIH) — Your Kidneys & How They Work; Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer; atıkları ve fazla suyu ayırarak idrar yapar.",
    "numbers": [],
    "quote": "Healthy kidneys filter about a half cup of blood every minute, removing wastes and extra water to make urine.",
    "location": "NIDDK (NIH) — Your Kidneys & How They Work"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Vücut, ihtiyaç duymadığı atıklardan ve fazla sudan kurtulmak için idrar üretir.",
    "numbers": [],
    "quote": "The body produces pee as a way to get rid of waste and extra water that it doesn't need.",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Üreterler idrarı böbreklerden mesaneye taşıyan iki ince borudur; mesane tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir; üretra idrarı mesaneden vücut dışına taşıyan borudur.",
    "numbers": [],
    "quote": "ureters: two thin tubes that take pee from the kidneys to the bladder / bladder: a sac that holds pee until it's time to go to the bathroom / urethra: the tube that carries urine from the bladder out of the body when you pee",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Böbrekler su, tuz ve minerallerin sağlıklı dengesini korur; idrar da vücudun doğru miktarda su tutmasının bir yoludur.",
    "numbers": [],
    "quote": "maintain a healthy balance of water, salts, and minerals / Pee also is a way for your body to keep the right amount of water.",
    "location": "NIDDK (NIH) — Your Kidneys & How They Work; Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.",
    "numbers": [],
    "quote": "The kidneys also help regulate blood pressure, the level of salts in the blood,",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Böbrekler kırmızı kan hücrelerinin üretimini denetleyen bir hormon yapar; böbreklerin yaptığı hormonlar kırmızı kan hücresi yapımına ve kemiklerin güçlü ve sağlıklı kalmasına yardım eder.",
    "numbers": [],
    "quote": "making a hormone that controls the production of red blood cells. / make red blood cells / keep your bones strong and healthy",
    "location": "Nemours KidsHealth — Urinary System & Kidneys; NIDDK (NIH) — Your Kidneys & How They Work"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Çok su içince daha çok idrara çıkılır ve idrar açık sarı olur.",
    "numbers": [],
    "quote": "Did you ever notice that if you drink a lot, you pee more and the pee is pale yellow?",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Böbrekleri ve idrar yollarını sağlıklı tutmak için yeterince su içilmeli, besleyici beslenilmeli ve bol egzersiz yapılmalıdır.",
    "numbers": [],
    "quote": "Stay hydrated. / Eat a nutritious diet. / Get plenty of exercise.",
    "location": "Nemours KidsHealth — Urinary System & Kidneys"
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
