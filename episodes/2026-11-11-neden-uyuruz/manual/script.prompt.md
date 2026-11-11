# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır; context bölümünde kendini "Ben Muma!" diye tanıtır.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Neden uyuruz?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

Bölümler, bu sırayla ve bu kimliklerle:
1. "hook" — merak uyandıran açılış (30–40 kelime).
2. "context" — selamlama, günün sorusu ve bilgilerin hangi kaynaklardan geldiği (kaynak kurumları adıyla an).
3. "method" — "Nasıl oluyor?": anlamak için gereken temel bilgiler.
4. "finding" — "İşin sırrı": sorunun yanıtı, adım adım.
5. "importance" — "Sen de dene": çocuğun gelişimini destekleyen, evde ya da dışarıda güvenle yapılabilecek bir gözlem ya da etkinlik.
6. "limitations" — "Bunu biliyor muydun?": şaşırtıcı bir ek bilgi ve kısa bir tekrar sorusu.
7. "summary" — "Bugün bunu öğrendik": üç ana fikir birer cümleyle, ardından abone olma ve soru gönderme daveti.

Satır kuralları makale bölümleriyle aynıdır: her satırda "id" ("l1"...), "display" (ekran; sayılar rakamla), "spoken" (seslendirme; sayılar yazıyla, kısaltmalar okunuşuyla), "factIds". "display" içinde rakamla yazılan her sayı o satırın olgularının "numbers" listesinde bulunmalı; bilgi taşımayan sayıları yazıyla yaz.
"glossary": videoda geçen ve 7–14 yaşındaki bir çocuğun bilmeyebileceği kelimeler (3–8 tane), her biri { "term", "meaning" } — anlamı tek, sade bir cümleyle. Anlatımda bir kez "Bilmediğin kelimeler için sana açıklamalarda bir sözlük bırakıyorum" de.
Konuyu 7–14 yaşa göre ele al: ne bebekçe ne ders kitabı gibi. Bir fikri anlatmadan terimini kullanma; aynı anda en çok bir yeni kavram tanıt.
"song": videonun son dakikasında söylenecek, konuyu özetleyen neşeli kapanış şarkısı. "title"; "style" (İngilizce tarz tarifleri: neşeli çocuk şarkısı, marş ritmi, çizgi film enerjisi, 120 BPM, Türkçe net vokal; sanatçı, şarkı ya da eser adı YAZMA); "negativeStyle"; "cast" (şarkıda dans edecek, konuyla ilgili 4–5 karakter: { "emoji", "name" }; ör. uzay konusunda gezegenler ve yıldızlar, DNA konusunda DNA sarmalı; Muma şarkıda görünmez); sözlerde şarkının adı geçmez; "sections": toplam yaklaşık 60 saniye, her biri { "tag" (Intro / Verse 1 / Chorus ...), "label" (Türkçe: Giriş / Kıta / Nakarat), "direction"? (İngilizce çalgı yönergesi), "lines" (kısa, kafiyeli Türkçe dizeler), "durationMs" }. Sözlerde rakam olmaz ve yalnızca olgu listesindeki bilgiler geçer; nakarat bölümün üç ana fikrini taşır. Şarkı varsa "limitations" bölümünün son satırı izleyiciyi şarkıya davet eder ve "summary" bölümü kısa tutulur (özeti şarkı yapar); anlatım yaklaşık 420–460 kelime olur.
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 2, "paperId": "topic:neden-uyuruz".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Uyku hakkında (About Sleep)",
    "publisher": "CDC",
    "url": "https://www.cdc.gov/sleep/about/index.html"
  },
  {
    "id": "k2",
    "title": "Çocuklar ve uyku (Kids and Sleep)",
    "publisher": "Nemours KidsHealth",
    "url": "https://kidshealth.org/en/kids/not-tired.html"
  },
  {
    "id": "k3",
    "title": "Uyku neden önemli? (Why Is Sleep Important?)",
    "publisher": "NIH",
    "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"
  },
  {
    "id": "k4",
    "title": "Vücut saati (Circadian Rhythms)",
    "publisher": "NIH",
    "url": "https://www.nigms.nih.gov/education/fact-sheets/Pages/circadian-rhythms"
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
    "location": "NHLBI (NIH) — Why Is Sleep Important?"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "Vücut saati (sirkadiyen ritim), bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.",
    "numbers": [
      "24"
    ],
    "quote": "Circadian rhythms include some of the physical, mental, and behavioral changes an organism experiences over a 24-hour cycle.",
    "location": "NIGMS (NIH) — Circadian Rhythms"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "İnsanda ana saat beyindedir; büyük bir sinir hücresi grubudur.",
    "numbers": [],
    "quote": "In vertebrate animals, including humans, the master clock exists in the brain. The human master clock is a large group of nerve cells",
    "location": "NIGMS (NIH) — Circadian Rhythms"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Vücut saatini en çok ışık ve karanlık etkiler; yemek, stres, hareket, sosyal çevre ve sıcaklık da etkiler.",
    "numbers": [],
    "quote": "Light and dark have the biggest influence on circadian rhythms, but food intake, stress, physical activity, social environment, and temperature also affect them.",
    "location": "NIGMS (NIH) — Circadian Rhythms"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Akşam ana saat beyne daha çok melatonin üretmesini söyler; bu uyku getirir. Melatonin bir hormondur.",
    "numbers": [],
    "quote": "In the evening, a person's master clock tells their brain to make more melatonin, causing sleepiness.",
    "location": "NIGMS (NIH) — Circadian Rhythms"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Sabah vücut, uyanmaya yardım eden kortizol gibi hormonlar salgılar.",
    "numbers": [],
    "quote": "In the morning, your body releases hormones that promote alertness, such as cortisol, which helps you wake up.",
    "location": "NHLBI (NIH) — Why Is Sleep Important?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Uyurken beyin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.",
    "numbers": [],
    "quote": "As we sleep, our brains move between two types of sleep — non-REM and REM (rapid eye movement) sleep.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f8",
    "kind": "number",
    "statement": "Okul çağında bir uyku döngüsü yaklaşık 90 dakika sürer.",
    "numbers": [
      "90"
    ],
    "quote": "By the time kids start school, one complete sleep cycle lasts about 90 minutes, which is similar to an adult's.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "REM olmayan uykunun üçüncü aşamasında vücut, büyüme ve gelişme için gereken hormonları salgılar.",
    "numbers": [],
    "quote": "It's during this stage that the body releases hormones needed for growth and development.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "REM uykusunda gözler göz kapaklarının altında hızlı hareket eder.",
    "numbers": [],
    "quote": "The eyes move quickly under the eyelids, breathing gets faster, and the heart beats faster.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "En canlı rüyalar REM uykusunda görülür.",
    "numbers": [],
    "quote": "This is when we have our most vivid dreams.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "REM uykusunda kollar ve bacaklar hareket ettirilemez.",
    "numbers": [],
    "quote": "You can't move your arms or legs during REM sleep.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "REM uykusu öğrenme ve hafıza için önemlidir.",
    "numbers": [],
    "quote": "REM sleep is important for learning and memory.",
    "location": "Nemours KidsHealth — Kids and Sleep"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
    "numbers": [],
    "quote": "Sleep helps with learning and the formation of long-term memories.",
    "location": "NHLBI (NIH) — Why Is Sleep Important?"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Çocuklarda ve gençlerde uyku, büyümeyi ve gelişmeyi de destekler.",
    "numbers": [],
    "quote": "In children and teens, sleep also helps support growth and development.",
    "location": "NHLBI (NIH) — Why Is Sleep Important?"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
    "numbers": [],
    "quote": "when you sleep, a particular type of immune cell works harder. That is why people who do not sleep enough may be more likely to get colds and other infections.",
    "location": "NHLBI (NIH) — Why Is Sleep Important?"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz, sinirli ya da keyifsiz olabilir.",
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
    "location": "NIGMS (NIH) — Circadian Rhythms"
  },
  {
    "id": "f23",
    "kind": "claim",
    "statement": "Yatak odasının sessiz, rahatlatıcı ve serin olması önerilir.",
    "numbers": [],
    "quote": "Keeping your bedroom quiet, relaxing, and at a cool temperature.",
    "location": "CDC — About Sleep"
  },
  {
    "id": "f24",
    "kind": "claim",
    "statement": "Düzenli hareket etmek ve sağlıklı beslenmek daha iyi uykuya yardım eder.",
    "numbers": [],
    "quote": "Exercising regularly and maintaining a healthy diet.",
    "location": "CDC — About Sleep"
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
