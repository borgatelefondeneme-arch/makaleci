# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Tsunami nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 46, "paperId": "topic:tsunami-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Tsunamis",
    "publisher": "NOAA",
    "url": "https://www.noaa.gov/education/resource-collections/ocean-coasts/tsunamis"
  },
  {
    "id": "k2",
    "title": "Tsunami Safety",
    "publisher": "Ulusal Hava Durumu Servisi",
    "url": "https://www.weather.gov/safety/tsunami"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Tsunami, okyanus suyunun büyük ve ani biçimde yerinden oynamasıyla oluşan bir dizi son derece uzun dalgadır; bu genellikle okyanus tabanının altında ya da yakınında olan bir depremin sonucudur.",
    "numbers": [],
    "quote": "A tsunami is a series of extremely long waves caused by a large and sudden displacement of the ocean / usually the result of an earthquake below or near the ocean floor.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Tsunamiler okyanus tabanından yüzeyine kadar tüm su sütunu boyunca hareket eder.",
    "numbers": [],
    "quote": "tsunamis move through the entire water column, from the ocean floor to the ocean surface.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Tsunamilerin çoğu yakınlaşan levha sınırlarındaki depremlerden kaynaklanır; heyelanlar ve volkanik etkinlik de tsunamiye yol açabilir.",
    "numbers": [],
    "quote": "Most tsunamis are caused by earthquakes on converging tectonic plate boundaries. / tsunamis can also be caused by landslides, volcanic activity,",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f4",
    "kind": "number",
    "statement": "1900'den bu yana olası tsunamilerin yüzde 80'inden fazlası depremlerle oluştu.",
    "numbers": [
      "1900",
      "80"
    ],
    "quote": "since 1900, over 80% of likely tsunamis were generated by earthquakes.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Derin okyanusta bir tsunami jet uçağı kadar hızlı hareket edebilir; dalga boyu, yani tepeden tepeye uzaklık, yüzlerce mil olabilir.",
    "numbers": [],
    "quote": "In the deep ocean, a tsunami can move as fast as a jet plane, over 500 mph, / its wavelength, the distance from crest to crest, may be hundreds of miles.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Derin suda dalganın tepesi okyanusun olağan dalgalanmasının çok az üstüne çıkar; tsunami ancak karaya yaklaşınca tehlikeli olur.",
    "numbers": [],
    "quote": "in deep water, the top of the wave rarely reaches more than three feet higher than the ocean swell. / A tsunami only becomes hazardous when it approaches land.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Tsunami kıyıya yakın sığ suya girince yavaşlar; dalga boyu kısalır, yüksekliği artar ve akıntılar güçlenir.",
    "numbers": [],
    "quote": "As a tsunami enters shallow water near coastal shorelines, it slows to 20 to 30 mph. / The wavelength decreases, the height increases, and currents intensify.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Doğal uyarı işaretleri arasında güçlü ya da uzun depremler, okyanustan gelen tren ya da uçak sesine benzer yüksek bir uğultu ve gelgitle ilgisi olmayan ani bir deniz yükselmesi ya da çekilmesi vardır.",
    "numbers": [],
    "quote": "These include strong or long earthquakes, a loud roar (like that of a train or an airplane) coming from the ocean, / a sudden rise or fall of the sea level that is not related to the tide.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Resmi uyarıyı beklemeye zaman olmayabilir; tahliye yolu görülmüyorsa yüksek bir yere ya da olabildiğince iç kesimlere gidilmeli; yetkililer güvenli diyene kadar tehlike bölgesinden uzak durulmalı; ilk dalga son, en büyük ya da en yıkıcı dalga olmayabilir.",
    "numbers": [],
    "quote": "There may not be time to wait for an official warning, / If you do not see an evacuation route, go to high ground or as far inland as possible. / Stay out of the tsunami hazard zone until local officials tell you it is safe, / The first wave in a tsunami may not be the last, the largest, or the most damaging.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "DART şamandıraları deniz seviyesindeki küçük değişiklikleri algılayıp tsunami uyarı merkezlerine iletebilir; bilim insanları bir sonraki tsunaminin ne zaman ve nerede olacağını önceden kestiremez.",
    "numbers": [],
    "quote": "are able to detect small changes in sea-level height and transmit this information to tsunami warning centers. / Scientists cannot predict when and where the next tsunami will strike.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "2004 Hint Okyanusu tsunamisi Güneydoğu ve Güney Asya'da 17 ülkeyi etkiledi; o zamandan bu yana tsunami uyarı yetenekleri çok gelişti.",
    "numbers": [
      "2004",
      "17"
    ],
    "quote": "The 2004 Indian Ocean tsunami, for example, impacted 17 countries in Southeastern and Southern Asia / Tsunami warning capabilities have become dramatically better since the 2004 Indian Ocean tsunami.",
    "location": "NOAA — Tsunamis (education resource collection)"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Tsunamiler Dünya'nın en seyrek görülen tehlikelerindendir; tsunaminin mevsimi yoktur ve her okyanus kıyısını her an vurabilir.",
    "numbers": [],
    "quote": "Tsunamis are among Earth's most infrequent hazards. / There is no season for tsunamis. / A tsunami can strike any ocean coast at any time.",
    "location": "National Weather Service — Tsunami Safety"
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
