# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Derimiz ne işe yarar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 42, "paperId": "topic:derimiz-ne-ise-yarar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Your Skin",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/skin.html"
  },
  {
    "id": "k2",
    "title": "Skin",
    "publisher": "Cleveland Clinic",
    "url": "https://my.clevelandclinic.org/health/body/10978-skin"
  },
  {
    "id": "k3",
    "title": "How to apply sunscreen",
    "publisher": "Amerikan Dermatoloji Akademisi",
    "url": "https://www.aad.org/public/everyday-care/sun-protection/shade-clothing-sunscreen/how-to-apply-sunscreen"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Deri en büyük organımızdır ve birçok görevi vardır.",
    "numbers": [],
    "quote": "Skin, our largest organ, has many jobs.",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Deri vücudu mikroplardan korur ve vücut sıcaklığını düzenler; zararlı maddelerin ve mikropların vücuda girmesini önleyen bir engel oluşturur.",
    "numbers": [],
    "quote": "Your skin protects your body from germs and regulates body temperature. / forms a barrier that prevents harmful substances and germs from entering the body",
    "location": "Cleveland Clinic — Skin; Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Epidermis derinin üst katmanıdır; sürekli dökülüp yenilenen hücre katmanlarından oluşur; epidermis hücreleri yaklaşık her 28 günde bir tamamen yenilenir.",
    "numbers": [
      "28"
    ],
    "quote": "The epidermis is the upper layer of skin. / The epidermis has layers of cells that constantly flake off and are renewed. / The cells in the epidermis are completely replaced about every 28 days.",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f4",
    "kind": "number",
    "statement": "Yeni hücreler, vücudun her gün döktüğü yaklaşık 40.000 eski deri hücresinin yerini alır.",
    "numbers": [
      "40.000"
    ],
    "quote": "These new cells replace the approximately 40,000 old skin cells that your body sheds every day.",
    "location": "Cleveland Clinic — Skin"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Epidermis, deriye rengini veren melanin pigmentini içerir; vücut ne kadar çok melanin üretirse deri o kadar koyu olur.",
    "numbers": [],
    "quote": "The epidermis contains melanin, the pigment that gives skin its color. / The more melanin the body produces, the darker the skin.",
    "location": "Cleveland Clinic — Skin; Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri bulunur.",
    "numbers": [],
    "quote": "This is where our blood vessels, nerve endings, sweat glands, and hair follicles are.",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Deri, sıcağı ve soğuğu, dokunmayı ve acıyı hissetmemizi sağlayan sinir uçları taşır; dermisteki sinirler bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu bildirir.",
    "numbers": [],
    "quote": "Skin holds nerve endings that let us feel hot and cold, touch, and pain. / Nerves in the dermis tell you when something is too hot to touch, itchy or super soft.",
    "location": "Nemours KidsHealth — Your Skin; Cleveland Clinic — Skin"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Yağ bezleri deriyi yumuşatan ve su geçirmez yapan sebum yağını üretir.",
    "numbers": [],
    "quote": "These glands make the oil sebum (SEE-bum), which softens the skin and makes it waterproof.",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Ter vücut sıcaklığını düzenlemeye yardım eder; deri sıcakken terleyerek, soğukken ısıyı içeride tutarak sıcaklığı kontrol eder.",
    "numbers": [],
    "quote": "Sweat helps regulate your body temperature. / helps control body temperature through sweating when we're hot and by helping keep heat in the body when we're cold",
    "location": "Cleveland Clinic — Skin; Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Deri altı dokusu vücudu darbelere ve yaralanmalara karşı korur ve vücut ısısını içeride tutar.",
    "numbers": [],
    "quote": "This layer helps protect the body from hits and other injuries, and helps hold in body heat.",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Kesik ve sıyrık gibi küçük yaralanmalar çabuk iyileşebilir.",
    "numbers": [],
    "quote": "minor injuries like cuts and scrapes can heal quickly",
    "location": "Nemours KidsHealth — Your Skin"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Güneş kremi deriyi güneş yanığına ve cilt kanserine karşı korumaya yardım eder; en az 30 SPF'li, suya dayanıklı, geniş spektrumlu güneş kremi seçilmeli; dışarıdayken iki saatte bir ve yüzdükten ya da terledikten hemen sonra yeniden sürülmelidir.",
    "numbers": [
      "30"
    ],
    "quote": "Sunscreen can help protect your skin against skin cancer, sunburn, and premature aging. / Choose a sunscreen that has an SPF of 30 or higher, is water resistant / To remain protected when outdoors, reapply sunscreen every two hours, and immediately after swimming or sweating.",
    "location": "American Academy of Dermatology — How to apply sunscreen"
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
