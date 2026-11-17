# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Akciğerlerimiz nasıl çalışır?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 32, "paperId": "topic:akcigerlerimiz-nasil-calisir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Lungs & Respiratory System",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/lungs.html"
  },
  {
    "id": "k2",
    "title": "How the Lungs Work - The Respiratory System",
    "publisher": "NIH",
    "url": "https://www.nhlbi.nih.gov/health/lungs/respiratory-system"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Solunum sistemi burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.",
    "numbers": [],
    "quote": "The respiratory system includes the nose, mouth, throat, voice box, windpipe, lungs, and diaphragm.",
    "location": "Nemours KidsHealth — Lungs & Respiratory System"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Hava vücuda burundan ya da ağızdan girer; bunlar havayı nemlendirip ısıtır, çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.",
    "numbers": [],
    "quote": "Air first enters your body through your nose or mouth, which moistens and warms the air since cold, dry air can irritate your lungs. / In the nostrils, air gets warmed and moistened.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System; Nemours KidsHealth — Lungs & Respiratory System"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Burundaki silia denen minik tüyler tozu ve parçacıkları süzer; soluk borusu da silialarla kaplıdır ve bunlar yabancı parçacıkları hava yolundan dışarı süpürür.",
    "numbers": [],
    "quote": "Tiny hairs in the nose called cilia (SIL-ee-uh) filter out dust and other particles. / The trachea is also lined with cilia, which sweep fluids and foreign particles out of the airway",
    "location": "Nemours KidsHealth — Lungs & Respiratory System"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Soluk borusu aşağıda sol ve sağ iki tüpe, bronşlara ayrılır; kıkırdak denen sert doku halkaları bronş tüplerini açık tutar.",
    "numbers": [],
    "quote": "Further down, the trachea divides into two tubes (left and right) called bronchi (BRAHN-kye). / Rings of tough tissue, called cartilage, acts as a support to keep the bronchial tubes open.",
    "location": "Nemours KidsHealth — Lungs & Respiratory System; NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Akciğerlerin içinde bronşlar bronşiyol denen binlerce ince tüpe ayrılır.",
    "numbers": [],
    "quote": "Inside your lungs, the bronchial tubes branch into thousands of thinner tubes called bronchioles.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f6",
    "kind": "number",
    "statement": "Bronşiyoller alveol denen minik hava keseciği kümelerinde son bulur; akciğerlerde yaklaşık 150 milyon alveol vardır.",
    "numbers": [
      "150"
    ],
    "quote": "The bronchioles end in clusters of tiny air sacs called alveoli. / Your lungs have about 150 million alveoli.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Her alveol kılcal damar denen minik kan damarlarından bir ağla sarılıdır.",
    "numbers": [],
    "quote": "Each of these alveoli is made up of a mesh of tiny blood vessels called capillaries.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Oksijen alveollerden, alveol duvarlarını kaplayan kılcal damarlar yoluyla kana geçer; alyuvarlar oksijeni alıp vücut hücrelerine taşır.",
    "numbers": [],
    "quote": "Oxygen moves from the alveoli to the blood through the capillaries (tiny blood vessels) lining the alveolar walls. / Red blood cells pick up the oxygen and deliver it to the body's cells.",
    "location": "Nemours KidsHealth — Lungs & Respiratory System"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Karbondioksit kandan alveollerin içindeki havaya geçer.",
    "numbers": [],
    "quote": "Carbon dioxide moves from the blood into the air inside the alveoli.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Diyafram göğüs ile karın arasındaki bir kastır; nefes alırken karına doğru aşağı iner, nefes verirken yukarı çıkar ve göğüs duvarı kasları gevşer.",
    "numbers": [],
    "quote": "The diaphragm (DYE-uh-fram) is a muscle between the chest and the abdomen / When you breathe in (inhalation), the diaphragm moves down toward the abdomen, / When you breathe out (exhalation), the diaphragm moves up and the chest wall muscles relax,",
    "location": "Nemours KidsHealth — Lungs & Respiratory System"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Sürfaktan, nefes alırken akciğerlerin daha kolay şişmesine yardım ederek nefes almak için gereken işi azaltır.",
    "numbers": [],
    "quote": "Surfactant reduces the work it takes to breathe by helping the lungs inflate more easily when you breathe in.",
    "location": "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Solunum sistemi sayesinde günde binlerce kez nefes alırız.",
    "numbers": [],
    "quote": "We take thousands of breaths a day, thanks to the respiratory system.",
    "location": "Nemours KidsHealth — Lungs & Respiratory System"
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
