# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Dişlerimiz nasıl çalışır?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 17, "paperId": "topic:dislerimiz-nasil-calisir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Mouth & Teeth",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/teeth.html"
  },
  {
    "id": "k2",
    "title": "The Tooth Decay Process: How to Reverse It and Avoid a Cavity",
    "publisher": "NIH",
    "url": "https://www.nidcr.nih.gov/health-info/tooth-decay/more-info/tooth-decay-process"
  },
  {
    "id": "k3",
    "title": "How to keep your teeth clean",
    "publisher": "NHS",
    "url": "https://www.nhs.uk/live-well/healthy-teeth-and-gums/how-to-keep-your-teeth-clean/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "number",
    "statement": "İlk diş takımı 20 süt dişidir; yerlerini 32 kalıcı diş alır. Süt dişleri doğumdan önce gelişmeye başlar ve çocuk yaklaşık 6 yaşındayken düşmeye başlar.",
    "numbers": [
      "20",
      "32",
      "6"
    ],
    "quote": "The first set are 20 deciduous (pronounced: duh-SID-you-wus) teeth / They're replaced by a set of 32 permanent teeth, which are also called secondary or adult teeth. / They begin to develop before birth and begin to fall out when a child is around 6 years old.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f2",
    "kind": "number",
    "statement": "İlk kalıcı azı dişleri ('6 yaş dişleri') 5–7 yaş arasında, ikinci kalıcı azılar ('12 yaş dişleri') 11–14 yaş arasında çıkar; üçüncü azılar yirmi yaş dişleridir.",
    "numbers": [
      "6",
      "5",
      "7",
      "12",
      "11",
      "14"
    ],
    "quote": "The first permanent molars called, \"6 year molars,\" come in between the ages of 5 and 7. / The second permanent molars, \"12 year molars,\" come in when a child is between 11 and 14 years old. / The third molars are the wisdom teeth.",
    "location": "NIH (NIDCR) — The Tooth Decay Process; Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Dişler konuşmak ve düzgün yemek için gereklidir; yerken dişlerimiz besini yutmaya hazırlamak için yırtar, keser ve öğütür.",
    "numbers": [],
    "quote": "You need teeth to talk and eat properly. / When we eat, our teeth tear, cut, and grind food in preparation for swallowing.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "İnsan dişleri dört dokudan oluşur: öz (pulpa), dentin, mine ve sement.",
    "numbers": [],
    "quote": "Human teeth are made up of four different types of tissue: pulp, dentin, enamel, and cementum.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Mine vücudun en sert dokusudur; dentini örter ve kronun en dış katmanını oluşturur.",
    "numbers": [],
    "quote": "Enamel, the hardest tissue in the body, covers the dentin and forms the outermost layer of the crown.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Dentin sert, sarı bir maddedir; dişin büyük bölümünü oluşturur ve kemik kadar serttir.",
    "numbers": [],
    "quote": "A hard yellow substance, it makes up most of the tooth and is as hard as bone.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Öz (pulpa) dişin en iç kısmıdır; bağ dokusu, sinirler ve kan damarlarından oluşur.",
    "numbers": [],
    "quote": "The pulp is the innermost portion of the tooth and consists of connective tissue, nerves, and blood vessels,",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Sement kökün dışını diş etinin altında örter ve dişi çene kemiğinde yerinde tutar.",
    "numbers": [],
    "quote": "A layer of cementum covers the outside of the root, under the gum line, and holds the tooth in place within the jawbone.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Kesici dişler ağzın önündeki keskin kenarlı dişlerdir ve ısırdığımızda besini keser; yanlarında sivri köpek dişleri bulunur; küçük azılar besini öğütüp ezer; azı dişleri güçlü çiğnemeyi sağlar.",
    "numbers": [],
    "quote": "Incisors are the squarish, sharp-edged teeth in the front of the mouth that cut foods when we bite into them. / On either side of the incisors are the sharp canines. / Behind the canines are the premolars, or bicuspids, which grind and mash foods. / The molars, found behind the premolars, have points and grooves, and allow for vigorous chewing.",
    "location": "Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Diş çürüğü, besinlerdeki şekerleri kullanarak asit yapan bazı bakterilerin yol açtığı bir enfeksiyondur; asitler minenin sert dış yüzeyini aşındırmaya başlar; tekrarlanan asit saldırıları minenin mineral kaybetmesine yol açar.",
    "numbers": [],
    "quote": "Tooth decay is the result of an infection with certain types of bacteria that use sugars in food to make acids. / These acids begin to eat away at the tooth's hard outer surface, or enamel. / the repeated cycles of acid attacks cause the enamel to continue to lose minerals.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Plak, bakterilerden oluşan yapışkan, renksiz bir tabakadır; ağzımızda yüzlerce farklı türde bakteri yaşar.",
    "numbers": [],
    "quote": "a sticky, colorless film of bacteria / Hundreds of different types live on our teeth, gums, tongue, and other places in our mouths.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Bu aşamada çürük durdurulabilir ya da geri döndürülebilir; mine tükürükteki mineralleri ve diş macunu gibi kaynaklardaki florürü kullanarak kendini onarabilir.",
    "numbers": [],
    "quote": "Tooth decay can be stopped or reversed at this point. / Enamel can repair itself by using minerals from saliva, and fluoride from toothpaste or other sources.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Oyuk (kavite), dişçinin dolguyla onarması gereken kalıcı bir hasardır.",
    "numbers": [],
    "quote": "A cavity is permanent damage that a dentist has to repair with a filling.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Gün boyunca ağzımızda bir halat çekme yarışı sürer.",
    "numbers": [],
    "quote": "Throughout the day, a tug-of-war takes place inside our mouths.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f15",
    "kind": "number",
    "statement": "Dişleri günde iki kez, yaklaşık 2 dakika florürlü diş macunuyla fırçalamak gerekir; dişler arası günde bir kez ip ile temizlenmelidir.",
    "numbers": [
      "2"
    ],
    "quote": "Brush your teeth with fluoride toothpaste twice a day for about 2 minutes to help keep your teeth and mouth healthy. / Brush your teeth twice a day for two minutes at a time. Floss the teeth once a day.",
    "location": "NHS — How to keep your teeth clean; Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Şeker, kurabiye, gazlı ve şekerli içecekler özel günlere saklanmalı; meyve suyu, şekerli atıştırmalıklar ve kuru meyve gibi yapışkan besinler sınırlanmalıdır; dişçiye düzenli gidilmelidir.",
    "numbers": [],
    "quote": "Save candy, cookies, soda, and other sugary drinks for special occasions. / Limit juice, sugary snacks, and sticky foods like dried fruit. / Visit a dentist regularly for cleanings and an examination.",
    "location": "NIH (NIDCR) — The Tooth Decay Process; Nemours KidsHealth — Mouth & Teeth"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Fissür örtücüler, arka dişlerin (azıların) çiğneme yüzeylerine sürülen ince plastik kaplamalardır; çocuklarda ve gençlerde çürüklerin çoğu azı dişlerinde gelişir.",
    "numbers": [],
    "quote": "Sealants are thin, plastic coatings painted onto the chewing surfaces of the back teeth, or molars. / since most cavities in children and adolescents develop in the molars (the back teeth)",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
  },
  {
    "id": "f18",
    "kind": "claim",
    "statement": "Uyku sırasında tükürük akışı azalır.",
    "numbers": [],
    "quote": "Saliva flow decreases during sleep.",
    "location": "NIH (NIDCR) — The Tooth Decay Process"
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
            "mouth"
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
