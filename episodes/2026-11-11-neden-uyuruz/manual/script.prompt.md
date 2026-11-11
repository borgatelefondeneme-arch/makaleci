# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Neden uyuruz?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 2, "paperId": "topic:neden-uyuruz".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "About Sleep",
    "publisher": "CDC",
    "url": "https://www.cdc.gov/sleep/about/index.html"
  },
  {
    "id": "k2",
    "title": "Kids and Sleep",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/not-tired.html"
  },
  {
    "id": "k3",
    "title": "Why Is Sleep Important?",
    "publisher": "NIH",
    "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"
  },
  {
    "id": "k4",
    "title": "Your Sleep/Wake Cycle",
    "publisher": "NIH",
    "url": "https://www.nhlbi.nih.gov/health/sleep/sleep-wake-cycle"
  },
  {
    "id": "k5",
    "title": "Circadian Rhythms",
    "publisher": "NIH",
    "url": "https://www.nigms.nih.gov/education/fact-sheets/Pages/circadian-rhythms"
  },
  {
    "id": "k6",
    "title": "What Is Circadian Rhythm?",
    "publisher": "Sleep Foundation",
    "url": "https://www.sleepfoundation.org/circadian-rhythm"
  },
  {
    "id": "k7",
    "title": "Stages of Sleep",
    "publisher": "Sleep Foundation",
    "url": "https://www.sleepfoundation.org/stages-of-sleep"
  },
  {
    "id": "k8",
    "title": "Adenosine and Sleep",
    "publisher": "Sleep Foundation",
    "url": "https://www.sleepfoundation.org/how-sleep-works/adenosine-and-sleep"
  },
  {
    "id": "k9",
    "title": "Why Is Sleep Important?",
    "publisher": "Sleep Foundation",
    "url": "https://www.sleepfoundation.org/how-sleep-works/why-do-we-need-sleep"
  },
  {
    "id": "k10",
    "title": "Suprachiasmatic nucleus",
    "publisher": "Wikipedia",
    "url": "https://en.wikipedia.org/wiki/Suprachiasmatic_nucleus"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Uyurken vücut, beynin sağlıklı çalışmasını ve beden sağlığını desteklemek için çalışır.",
    "numbers": [],
    "quote": "During sleep, your body is working to support healthy brain function and maintain your physical health.",
    "location": "NIH (NHLBI) — Why Is Sleep Important?"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Sirkadiyen ritimler, bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.",
    "numbers": [
      "24"
    ],
    "quote": "Circadian rhythms include some of the physical, mental, and behavioral changes an organism experiences over a 24-hour cycle.",
    "location": "NIH (NIGMS) — Circadian Rhythms"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "İnsanda ana saat beyindedir; suprakiazmatik çekirdek (SCN) adlı yapıyı oluşturan büyük bir sinir hücresi grubudur.",
    "numbers": [],
    "quote": "The human master clock is a large group of nerve cells that form a structure called the suprachiasmatic nucleus (SCN).",
    "location": "NIH (NIGMS) — Circadian Rhythms"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "SCN, beynin hipotalamus bölgesinde, görme sinirlerinin çaprazlaştığı yerin hemen üstündedir; binlerce nörondan oluşur.",
    "numbers": [],
    "quote": "a small region of the brain in the hypothalamus, situated directly above the optic chiasm. ... It consists of two nuclei composed of approximately 10,000 neurons.",
    "location": "Wikipedia — Suprachiasmatic nucleus"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Sirkadiyen ritimleri en çok ışık ve karanlık etkiler.",
    "numbers": [],
    "quote": "Light and dark have the biggest influence on circadian rhythms",
    "location": "NIH (NIGMS) — Circadian Rhythms"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Gözlerle alınan ışık sinyalleri beyne gündüz olduğunu bildirir.",
    "numbers": [],
    "quote": "light signals received through your eyes tell your brain that it is daytime.",
    "location": "NIH (NHLBI) — Your Sleep/Wake Cycle"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Güneş batınca beyin uyku getiren melatonin hormonunu üretmeye başlar; kandaki melatonin akşam artar, sabaha karşı en yüksek düzeye çıkar.",
    "numbers": [],
    "quote": "As the sun sets in the evening, the brain begins producing melatonin, a hormone that induces sleepiness. / The amount of melatonin in your bloodstream starts to increase in the evening and peaks in the early morning.",
    "location": "Sleep Foundation — What Is Circadian Rhythm?; NIH (NHLBI) — Your Sleep/Wake Cycle"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Uzun süre uyanık kaldıkça uyku ihtiyacı artar; bu ihtiyaç adenozin adlı bileşikle bağlantılıdır ve uyanıkken beyindeki adenozin düzeyi yükselir.",
    "numbers": [],
    "quote": "Your body has a biological need for sleep that increases when you have been awake for a long time. A compound called adenosine is linked to this need for sleep. While you are awake, the level of adenosine in your brain continues to rise.",
    "location": "NIH (NHLBI) — Your Sleep/Wake Cycle"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Uyurken beyin adenozini yeniden ATP'ye (enerji molekülüne) çevirir ve uyku baskısı ortadan kalkar.",
    "numbers": [],
    "quote": "While you sleep, the brain converts adenosine back into ATP, essentially eliminating your sleep drive.",
    "location": "Sleep Foundation — Adenosine and Sleep"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Uyku dört evreden oluşur: üçü REM olmayan (N1, N2, N3), biri REM. Bir gecede dört ila altı döngü yaşanır; bir döngü ortalama 90 dakika sürer.",
    "numbers": [
      "90",
      "4",
      "6",
      "1",
      "2",
      "3"
    ],
    "quote": "one for rapid eye movement (REM) sleep and three that form non-REM (NREM) sleep / In a typical night, a person goes through four to six sleep cycles / on average they last about 90 minutes each.",
    "location": "Sleep Foundation — Stages of Sleep"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Üçüncü evre (N3) derin uykudur; vücudun toparlanması ve büyümesi için kritik sayılır, bağışıklık sistemini de destekleyebilir.",
    "numbers": [
      "3"
    ],
    "quote": "Stage 3 (N3 or deep sleep) ... Experts believe that this stage is critical to restorative sleep, allowing for bodily recovery and growth. It may also bolster the immune system",
    "location": "Sleep Foundation — Stages of Sleep"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Büyüme ve gelişme için gereken hormonlar REM olmayan uykunun üçüncü evresinde salgılanır; büyüme hormonu dokuların büyümesi ve onarılması için gereklidir.",
    "numbers": [],
    "quote": "It's during this stage that the body releases hormones needed for growth and development. / Sleep provides the release of growth hormone necessary for the body's tissues to grow and repair damage.",
    "location": "Nemours KidsHealth — Kids and Sleep; Sleep Foundation — Why Is Sleep Important?"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "REM uykusunda gözler kapalıyken hızla hareket eder; beyin etkinliği uyanıklık düzeyine yaklaşır; kaslar geçici olarak felç olur (atoni); en canlı rüyalar bu evrede görülür.",
    "numbers": [],
    "quote": "brain activity picks up, nearing levels seen when you're awake. / the body experiences atonia, which is a temporary paralysis of the muscles / Even though they're closed, the eyes move rapidly / This is when we have our most vivid dreams.",
    "location": "Sleep Foundation — Stages of Sleep; Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "REM uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir; uyku uzun süreli anıların oluşmasına yardım eder.",
    "numbers": [],
    "quote": "REM sleep is believed to be essential to cognitive functions like memory, learning, and creativity. / Sleep helps with learning and the formation of long-term memories.",
    "location": "Sleep Foundation — Stages of Sleep; NIH (NHLBI) — Why Is Sleep Important?"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Uyku, vücudun enerji tasarrufu yapmasını sağlar.",
    "numbers": [],
    "quote": "Sleep allows people to conserve energy through an extended period of reduced activity.",
    "location": "Sleep Foundation — Why Is Sleep Important?"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
    "numbers": [],
    "quote": "when you sleep, a particular type of immune cell works harder. That is why people who do not sleep enough may be more likely to get colds and other infections.",
    "location": "NIH (NHLBI) — Why Is Sleep Important?"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz ya da keyifsiz olabilir.",
    "numbers": [],
    "quote": "kids who don't get enough sleep can have trouble paying attention ... be cranky, whiny, irritable, or moody",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f18",
    "kind": "number",
    "statement": "6–12 yaş için önerilen günlük uyku 9–12 saattir.",
    "numbers": [
      "6",
      "12",
      "9"
    ],
    "quote": "School age, 6–12 years, 9–12 hours",
    "location": "CDC — About Sleep"
  },
  {
    "id": "f19",
    "kind": "number",
    "statement": "13–17 yaş için önerilen günlük uyku 8–10 saattir.",
    "numbers": [
      "13",
      "17",
      "8",
      "10"
    ],
    "quote": "Teen, 13–17 years, 8–10 hours",
    "location": "CDC — About Sleep"
  },
  {
    "id": "f20",
    "kind": "claim",
    "statement": "Her gün aynı saatte yatıp kalkmak daha iyi uykuya yardım eder.",
    "numbers": [],
    "quote": "Going to bed and getting up at the same time every day.",
    "location": "CDC — About Sleep"
  },
  {
    "id": "f21",
    "kind": "number",
    "statement": "Yatmadan en az 30 dakika önce elektronik cihazları kapatmak önerilir.",
    "numbers": [
      "30"
    ],
    "quote": "Turning off electronic devices at least 30 minutes before bedtime.",
    "location": "CDC — About Sleep"
  },
  {
    "id": "f22",
    "kind": "claim",
    "statement": "Geceleri elektronik cihazların ışığı biyolojik saati şaşırtabilir.",
    "numbers": [],
    "quote": "Light from electronic devices at night can confuse biological clocks.",
    "location": "NIH (NIGMS) — Circadian Rhythms"
  },
  {
    "id": "f23",
    "kind": "claim",
    "statement": "Birçok gencin yetişkinlerden daha geç yatmayı ve sabah daha geç kalkmayı tercih etmesi doğaldır.",
    "numbers": [],
    "quote": "it is natural for many teens to prefer later bedtimes and to sleep later in the morning than adults.",
    "location": "NIH (NHLBI) — Your Sleep/Wake Cycle"
  },
  {
    "id": "f24",
    "kind": "claim",
    "statement": "Kafein temel olarak adenozin alıcılarını kapatarak etki eder.",
    "numbers": [],
    "quote": "The primary way that caffeine works is by blocking adenosine receptors",
    "location": "Sleep Foundation — Adenosine and Sleep"
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
