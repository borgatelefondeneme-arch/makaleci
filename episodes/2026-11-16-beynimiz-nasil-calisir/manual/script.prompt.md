# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Beynimiz nasıl çalışır?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 27, "paperId": "topic:beynimiz-nasil-calisir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "All About the Brain & Nervous System",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/brain.html"
  },
  {
    "id": "k2",
    "title": "The Neuron",
    "publisher": "BrainFacts",
    "url": "https://www.brainfacts.org/brain-anatomy-and-function/anatomy/2012/the-neuron"
  },
  {
    "id": "k3",
    "title": "Why Is Sleep Important?",
    "publisher": "NIH",
    "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Beyin ne düşündüğünü ve hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.",
    "numbers": [],
    "quote": "The brain controls what you think and feel, how you learn and remember, and the way you move and talk.",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Beyin ve omurilik kemikle korunur: beyin kafatası kemikleriyle; ayrıca meninks denen zar katmanları ve beyin omurilik sıvısıyla yastıklanır.",
    "numbers": [],
    "quote": "the brain by the bones of the skull / cushioned by layers of membranes called meninges and a special fluid called cerebrospinal fluid.",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Büyük beynin sağ ve sol yarısı vardır, bunlara yarım küre denir; dört lobu vardır: alın, yan, şakak ve art kafa lobu.",
    "numbers": [],
    "quote": "The cerebrum has right and left halves, called hemispheres. / These are called lobes, and there are four of them: the frontal, parietal, temporal, and occipital lobes.",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Alın lobu karmaşık düşünmenin çoğunu yapar; yan lob dokunma, tat ve sıcaklık bilgisini işler; şakak lobu sesleri ve dili anlamamızı sağlar; art kafa lobu gözlerden gelen görsel bilgiyi işler.",
    "numbers": [],
    "quote": "The frontal lobe, located behind the forehead, does much of the work of complex thinking / The parietal lobe, located behind the frontal lobe, processes information about touch, taste, and temperature. / The temporal lobe, found near the ears, lets us understand sounds and language / The occipital lobe, in the rear of the brain, processes light and other visual information from the eyes",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Beyincik denge, hareket ve koordinasyondan sorumludur; beyin sapı nefes alma, kalp atışı, kan basıncı ve yutma gibi otomatik işlevleri kontrol eder.",
    "numbers": [],
    "quote": "is responsible for balance, movement, and coordination. / It also controls many of the body's automatic functions, like breathing, heart rate, blood pressure, swallowing",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Nöron, beynin temel çalışma birimidir; bilgi iletmek için özelleşmiş bir hücredir; nöronların çoğunda hücre gövdesi, akson ve dendritler bulunur.",
    "numbers": [],
    "quote": "The neuron is the basic working unit of the brain, a specialized cell designed to transmit information / Most neurons have a cell body, an axon, and dendrites.",
    "location": "BrainFacts (Society for Neuroscience) — The Neuron"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Dendritler hücre gövdesinden uzanır ve diğer nöronlardan mesaj alır; akson elektrik uyarılarını iletir; sinapslar bir nöronun diğeriyle iletişim kurduğu temas noktalarıdır; nöronlar bilgiyi elektrokimyasal bir süreçle aktarır.",
    "numbers": [],
    "quote": "Dendrites extend from the neuron cell body and receive messages from other neurons. / they transmit electrical impulses along their axons / Synapses are the contact points where one neuron communicates with another. / All neurons relay information to each other through a complex electrochemical process",
    "location": "BrainFacts (Society for Neuroscience) — The Neuron; Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Aksonların boyu santimetrenin küçük bir kesrinden yaklaşık bir metreye ya da daha fazlasına kadar değişebilir; birçok akson elektrik sinyallerinin iletimini hızlandıran katmanlı bir miyelin kılıfla kaplıdır.",
    "numbers": [],
    "quote": "which can range in length from a tiny fraction of an inch (or centimeter) to three feet (about one meter) or more. / Many axons are covered with a layered myelin sheath, which accelerates the transmission of electrical signals",
    "location": "BrainFacts (Society for Neuroscience) — The Neuron"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Beyinde milyarlarca nöron vardır; beyin, nörondan en az on kat fazla glia hücresi içerir.",
    "numbers": [
      "10"
    ],
    "quote": "The brain has billions of them, and they have many specialized jobs. / The brain contains at least ten times more glia than neurons.",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System; BrainFacts (Society for Neuroscience) — The Neuron"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Büyüyüp öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider; bu yüzden araba sürmek ilk öğrenirken çok dikkat ister ama sonra kendiliğinden yapılır; beyinde dolaşan mesajlar belleğin temeli olan yollar oluşturur.",
    "numbers": [],
    "quote": "As you grow and learn, messages travel from one neuron to another over and over, / It's why driving takes so much concentration when someone first learns, but later it is second nature. / As these messages travel through the brain, they too create pathways that serve as the basis of memory.",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Birçok bilim insanı beyni yeni şeyler öğrenmeye ve yeni bağlantılar kurmaya zorlamanın önemli olduğuna inanır.",
    "numbers": [],
    "quote": "Many scientists believe it's important to keep challenging it to learn new things and make new connections",
    "location": "Nemours KidsHealth — All About the Brain & Nervous System"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder; yeterince ya da kaliteli uyumamak odaklanmayı ve net düşünmeyi zorlaştırabilir.",
    "numbers": [],
    "quote": "Sleep helps with learning and the formation of long-term memories. / Not getting enough sleep or enough high-quality sleep can lead to problems focusing on tasks and thinking clearly.",
    "location": "NIH (NHLBI) — Why Is Sleep Important?"
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
