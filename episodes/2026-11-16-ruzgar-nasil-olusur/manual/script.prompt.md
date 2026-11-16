# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Rüzgâr nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 26, "paperId": "topic:ruzgar-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Wind",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/wind/"
  },
  {
    "id": "k2",
    "title": "Global Atmospheric Circulations",
    "publisher": "NOAA",
    "url": "https://www.noaa.gov/jetstream/global/global-atmospheric-circulations"
  },
  {
    "id": "k3",
    "title": "The Sea Breeze",
    "publisher": "NOAA",
    "url": "https://www.noaa.gov/jetstream/ocean/sea-breeze"
  },
  {
    "id": "k4",
    "title": "Beaufort Wind Scale",
    "publisher": "Ulusal Hava Servisi",
    "url": "https://www.weather.gov/mfl/beaufort"
  },
  {
    "id": "k5",
    "title": "Explore a Wind Turbine - Text Version",
    "publisher": "ABD Enerji Bakanlığı",
    "url": "https://www.energy.gov/eere/wind/how-wind-turbine-works-text-version"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Rüzgâr, Dünya'nın Güneş tarafından eşit olmayan biçimde ısıtılmasından kaynaklanan hava hareketidir; göremez ya da tutamazsın ama kuvvetini hissedebilirsin.",
    "numbers": [],
    "quote": "Wind is the movement of air caused by the uneven heating of the Earth by the sun. / It does not have much substance—you cannot see it or hold it—but you can feel its force.",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Atmosfer basıncındaki farklar rüzgârı oluşturur; rüzgâr genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere eser.",
    "numbers": [],
    "quote": "Differences in atmospheric pressure generate winds. / Winds generally blow from high-pressure areas to low-pressure areas.",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Hava ısındıkça yoğunluğu azalır ve 'termal alçak' denen zayıf bir alçak basınç bölgesi oluşur.",
    "numbers": [],
    "quote": "As the air warms, its density decreases, creating a weak low-pressure area called a \"thermal low\"",
    "location": "NOAA JetStream — The Sea Breeze"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Ekvator'da Güneş suyu ve karayı dünyanın geri kalanından daha çok ısıtır; ılık ekvator havası atmosferde yükselir ve kutuplara doğru gider; daha serin, yoğun hava yeryüzünde Ekvator'a doğru ilerleyip ısınan havanın yerini alır.",
    "numbers": [],
    "quote": "At the Equator, the sun warms the water and land more than it does the rest of the globe. / Warm equatorial air rises higher into the atmosphere and migrates toward the poles. / cooler, denser air moves over Earth's surface toward the Equator to replace the heated air.",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Deniz meltemi gündüz, kara meltemi gece eser; gündüz ile gece arasındaki sıcaklık farkı karada denizdekinden çok daha büyüktür; gece kara sıcaklığı denizinkinin altına düşer.",
    "numbers": [],
    "quote": "While sea breezes occur during the day, land breezes occur at night. / temperature fluctuations between daytime and nighttime are much greater over land than over water. / At night, the land temperature falls to below that of the ocean, resulting in an increase in the air's density.",
    "location": "NOAA JetStream — The Sea Breeze"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Karadaki ılık hava yükselir ve sudaki serin hava karaya doğru ilerleyerek iç kesimlere esen bir meltem oluşturur.",
    "numbers": [],
    "quote": "Warm air above the land rises, and cooler air above the water moves in over the land, creating an inland breeze.",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Dünya'nın dönmesi havanın doğuya doğru sapmasına yol açar; buna Coriolis etkisi denir; her yarım kürede tek büyük dolaşım yerine üç dolaşım vardır.",
    "numbers": [],
    "quote": "The Earth's rotation results in an easterly-movement of air, called the Coriolis effect / Instead of one large circulation in each hemisphere, there are three circulations in each:",
    "location": "NOAA JetStream — Global Atmospheric Circulations"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Hâkim rüzgârlar genellikle kuzey-güney değil doğu-batı doğrultusunda eser; alize rüzgârları tropiklerde doğudan esen güçlü rüzgârlardır; batı rüzgârları orta enlemlerde batıdan eser.",
    "numbers": [],
    "quote": "Generally, prevailing winds blow east-west rather than north-south. / Trade winds are the powerful prevailing winds that blow from the east across the tropics. / Westerlies are prevailing winds that blow from the west at midlatitudes.",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Jet akımları üst atmosferde saatte 480 kilometreye kadar esebilen güçlü, hızlı rüzgârlardır.",
    "numbers": [
      "480"
    ],
    "quote": "These strong, fast winds in the upper atmosphere can blow 480 kph (298 mph).",
    "location": "National Geographic Education — Wind"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Anemometre rüzgâr hızını, rüzgâr gülü (yön göstergesi) rüzgârın yönünü ölçer.",
    "numbers": [],
    "quote": "a device that measures wind speed. / The wind vane measures wind direction",
    "location": "National Geographic Education — Wind; U.S. Department of Energy — Explore a Wind Turbine"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Beaufort ölçeği 0'dan başlar ve 12'ye kadar gider; Amiral Sir Francis Beaufort ölçeği 1805'te denizcilerin rüzgârı gözle tahmin etmesine yardım etmek için geliştirdi.",
    "numbers": [
      "0",
      "12",
      "1805"
    ],
    "quote": "The scale starts with 0 and goes to a force of 12. / He developed the scale in 1805 to help sailors estimate the winds via visual observations.",
    "location": "U.S. National Weather Service (Miami) — Beaufort Wind Scale"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Beaufort 0: sakin, duman dümdüz yükselir; 3: yapraklar ve küçük dallar sürekli hareket eder, hafif bayrağı açar; 7: bütün ağaçlar sallanır, rüzgâra karşı yürümek zorlaşır; 10: ağaçlar kökünden sökülür.",
    "numbers": [
      "0",
      "3",
      "7",
      "10"
    ],
    "quote": "Calm; smoke rises vertically. / Leaves and small twigs in constant motion; wind extends light flag. / Whole trees in motion; inconvenience felt when walking against the wind. / trees uprooted; considerable structural damage occurs.",
    "location": "U.S. National Weather Service (Miami) — Beaufort Wind Scale"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Rüzgâr, doğrudan kirlilik yaratmayan yenilenebilir bir kaynaktır; rüzgâr kanatları çevirince kanatlar bir jeneratörü döndürür ve elektrik üretir; rüzgâr hızı yükseklikle arttığı için daha uzun kuleler daha çok enerji yakalar.",
    "numbers": [],
    "quote": "Wind is a renewable resource that does not directly cause pollution. / When the wind turns the blades, the blades turn a generator and create electricity. / Because wind speed increases with height, taller towers enable turbines to capture more energy",
    "location": "National Geographic Education — Wind; U.S. Department of Energy — Explore a Wind Turbine"
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
