# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Kulağımız nasıl duyar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 24, "paperId": "topic:kulagimiz-nasil-duyar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "How Do We Hear?",
    "publisher": "NIH",
    "url": "https://www.nidcd.nih.gov/health/how-do-we-hear"
  },
  {
    "id": "k2",
    "title": "Ears",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/ears.html"
  },
  {
    "id": "k3",
    "title": "Noise-Induced Hearing Loss",
    "publisher": "NIH",
    "url": "https://www.nidcd.nih.gov/health/noise-induced-hearing-loss"
  },
  {
    "id": "k4",
    "title": "Balance Disorders",
    "publisher": "NIH",
    "url": "https://www.nidcd.nih.gov/health/balance-disorders"
  },
  {
    "id": "k5",
    "title": "Understanding Sound",
    "publisher": "Ulusal Park Servisi",
    "url": "https://www.nps.gov/subjects/sound/understandingsound.htm"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler; işitme, havadaki ses dalgalarını elektrik sinyallerine dönüştüren karmaşık adımlara dayanır.",
    "numbers": [],
    "quote": "Sound moves through a medium such as air or water as waves. / Hearing depends on a series of complex steps that change sound waves in the air into electrical signals.",
    "location": "U.S. National Park Service — Understanding Sound; NIH (NIDCD) — How Do We Hear?"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Frekans (perde), ses basınç dalgasının saniyede kaç kez tekrarlandığıdır; genlik, ses dalgalarının göreli gücüdür ve yükseklik olarak algılanır; desibel (dB) ile ölçülür.",
    "numbers": [],
    "quote": "Frequency, sometimes referred to as pitch, is the number of times per second that a sound pressure wave repeats itself. / Amplitude is the relative strength of sound waves (transmitted vibrations), which we perceive as loudness or volume. / Amplitude is measured in decibels (dB)",
    "location": "U.S. National Park Service — Understanding Sound"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Normal işiten insanlar 20 Hz ile 20.000 Hz arasındaki sesleri duyabilir.",
    "numbers": [
      "20",
      "20.000"
    ],
    "quote": "Humans with normal hearing can hear sounds between 20 Hz and 20,000 Hz.",
    "location": "U.S. National Park Service — Understanding Sound"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Dış kulağın görevi sesleri toplayıp kulak kanalına yönlendirmektir; ses dalgaları kulak kanalından kulak zarına ulaşır.",
    "numbers": [],
    "quote": "Its main job is to gather sounds and funnel them to the ear canal / Sound waves enter the outer ear and travel through a narrow passageway called the ear canal, which leads to the eardrum.",
    "location": "Nemours KidsHealth — Ears; NIH (NIDCD) — How Do We Hear?"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Kulak zarı gelen ses dalgalarıyla titreşir ve bu titreşimleri orta kulaktaki üç minik kemiğe gönderir: çekiç, örs ve üzengi; üzengi vücudun en küçük kemiğidir.",
    "numbers": [],
    "quote": "The eardrum vibrates from the incoming sound waves and sends these vibrations to three tiny bones in the middle ear. / malleus (pronounced: MAH-lee-us) (\"hammer\") / incus (pronounced: IN-kus) (\"anvil\") / stapes (pronounced: STAY-peez) (\"stirrup\"), which is attached to the incus and is the smallest bone in the body",
    "location": "NIH (NIDCD) — How Do We Hear?; Nemours KidsHealth — Ears"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Orta kulaktaki kemikler ses titreşimlerini güçlendirir ve salyangoz biçimli kokleaya gönderir.",
    "numbers": [],
    "quote": "The bones in the middle ear amplify, or increase, the sound vibrations and send them to the cochlea,",
    "location": "NIH (NIDCD) — How Do We Hear?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Baziler zarın üstündeki duyu hücreleri olan tüy hücreleri dalgayla hareket eder; salyangozun geniş ucundaki tüy hücreleri tiz sesleri, merkeze yakın olanlar pes sesleri algılar; hücrelere kimyasallar akar ve elektrik sinyali oluşur; işitme siniri bu sinyali beyne taşır.",
    "numbers": [],
    "quote": "Hair cells—sensory cells sitting on top of the basilar membrane—ride the wave. / Hair cells near the wide end of the snail-shaped cochlea detect higher-pitched sounds / Those closer to the center detect lower-pitched sounds / chemicals rush into the cells, creating an electrical signal. / The auditory nerve carries this electrical signal to the brain",
    "location": "NIH (NIDCD) — How Do We Hear?"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Kuş ve amfibilerin tersine insan tüy hücreleri yeniden çıkmaz; gürültüye bağlı işitme kaybının çoğu bu hücrelerin hasar görüp ölmesinden kaynaklanır.",
    "numbers": [],
    "quote": "Unlike bird and amphibian hair cells, human hair cells don’t grow back. They are gone for good. / Most NIHL is caused by the damage and eventual death of these hair cells.",
    "location": "NIH (NIDCD) — Noise-Induced Hearing Loss"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "70 dBA ve altındaki sesler uzun süre dinlense bile işitme kaybına yol açma olasılığı düşüktür; 85 dBA ve üstündeki seslere uzun ya da tekrarlı maruz kalmak işitme kaybına yol açabilir; ses ne kadar yüksekse hasar o kadar çabuk oluşur.",
    "numbers": [
      "70",
      "85"
    ],
    "quote": "Sounds at or below 70 A-weighted decibels (dBA), even after long exposure, are unlikely to cause hearing loss. / long or repeated exposure to sounds at or above 85 dBA can cause hearing loss. / The louder the sound, the shorter the amount of time it takes for NIHL to happen.",
    "location": "NIH (NIDCD) — Noise-Induced Hearing Loss"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Normal konuşma 60–70 dBA, sirenler 110–129 dBA, havai fişek gösterisi 140–160 dBA düzeyindedir.",
    "numbers": [
      "60",
      "70",
      "110",
      "129",
      "140",
      "160"
    ],
    "quote": "Normal conversation 60-70 dBA / Sirens 110-129 dBA / Fireworks show 140-160 dBA",
    "location": "NIH (NIDCD) — Noise-Induced Hearing Loss"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Telefonların, oyunların ve televizyonun sesi kısılmalı; gürültülü bir etkinlikte kulak tıkacı takılmalı; gürültü azaltılamıyorsa ondan uzaklaşılmalı.",
    "numbers": [],
    "quote": "Turn down the volume on phones, video games, TVs, and other devices, especially when listening with earbuds or headphones. / Wear earplugs or other protective devices when involved in a loud activity / If you can’t reduce the noise or protect yourself from it, move away from it.",
    "location": "Nemours KidsHealth — Ears; NIH (NIDCD) — Noise-Induced Hearing Loss"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Kulağın dengeye yardım eden bölümüne vestibüler sistem denir; yarım daire kanalları, birbirine aşağı yukarı dik açılarla dizilmiş üç sıvı dolu kanaldır ve başın ne zaman döndüğünü beyne bildirir.",
    "numbers": [],
    "quote": "The part of the ear that assists in balance is known as the vestibular system, or the labyrinth, / The semicircular canals contain three fluid-filled ducts, which form loops arranged roughly at right angles to one another. / They tell your brain when your head rotates.",
    "location": "NIH (NIDCD) — Balance Disorders"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Gök gürültüsü 120 desibeli aşabilir; bu, insan kulağında acıya yol açacak kadar yüksektir.",
    "numbers": [
      "120"
    ],
    "quote": "The crack of thunder can exceed 120 decibels, loud enough to cause pain to the human ear.",
    "location": "U.S. National Park Service — Understanding Sound"
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
