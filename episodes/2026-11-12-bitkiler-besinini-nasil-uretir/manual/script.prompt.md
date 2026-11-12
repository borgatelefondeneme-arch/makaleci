# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Bitkiler besinini nasıl üretir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 11, "paperId": "topic:bitkiler-besinini-nasil-uretir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Photosynthesis",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/photosynthesis/"
  },
  {
    "id": "k2",
    "title": "Chlorophyll",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/chlorophyll/"
  },
  {
    "id": "k3",
    "title": "Earth Observatory",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/earth/earth-observatory/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.",
    "numbers": [],
    "quote": "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar.",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Bitkiler karbondioksiti ve suyu havadan ve topraktan alır.",
    "numbers": [],
    "quote": "plants take in carbon dioxide (CO2) and water (H2O) from the air and soil.",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Bitkiler Güneş ışığının enerjisini yakalayarak oksijen ve glikozda (bir şeker) depolanan kimyasal enerji üretir.",
    "numbers": [],
    "quote": "capture energy from sunlight to produce oxygen (O2) and chemical energy stored in glucose (a sugar)",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Bitki oksijeni havaya geri verir, enerjiyi glikoz moleküllerinde saklar.",
    "numbers": [],
    "quote": "The plant then releases the oxygen back into the air, and stores energy within the glucose molecules.",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Bitki hücresinin içinde Güneş ışığının enerjisini depolayan kloroplast adlı küçük organeller vardır; klorofil kloroplastlarda bulunur.",
    "numbers": [],
    "quote": "Inside the plant cell are small organelles called chloroplasts, which store the energy of sunlight. / Chlorophyll is located in a plant’s chloroplasts, which are tiny structures in a plant’s cells.",
    "location": "National Geographic Education — Photosynthesis; National Geographic Education — Chlorophyll"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Klorofil mavi ve kırmızı ışık dalgalarının enerjisini soğurur, yeşil ışık dalgalarını yansıtır; bitkilere yeşil rengini verir.",
    "numbers": [],
    "quote": "chlorophyll absorbs energy from blue- and red-light waves, and reflects green-light waves / Chlorophyll gives plants their green color because it does not absorb the green wavelengths of white light.",
    "location": "National Geographic Education — Photosynthesis; National Geographic Education — Chlorophyll"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Işığa bağımlı tepkime tilakoit zarında gerçekleşir ve sürekli Güneş ışığı gerektirir; su yükseltgenir (elektron kaybeder) ve oksijene dönüşür; ATP ve NADPH molekülleri oluşur.",
    "numbers": [],
    "quote": "The light-dependent reaction takes place within the thylakoid membrane and requires a steady stream of sunlight / Within the plant cell, the water is oxidized, meaning it loses electrons / energy from the ATP and NADPH molecules",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Işığa bağımlı olmayan aşama (Calvin döngüsü) stromada gerçekleşir; ATP ve NADPH moleküllerindeki enerji, karbondioksitten glikoz gibi karbonhidrat moleküllerini kurmak için kullanılır.",
    "numbers": [],
    "quote": "The light-independent stage, also known as the Calvin cycle, takes place in the stroma / energy from the ATP and NADPH molecules is used to assemble carbohydrate molecules, like glucose, from carbon dioxide.",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Bitkiler glikozu topraktan aldıkları besin maddeleriyle birlikte yeni yapraklar ve başka bitki bölümleri yapmak için kullanır.",
    "numbers": [],
    "quote": "Plants use glucose together with nutrients taken from the soil to make new leaves and other plant parts.",
    "location": "National Geographic Education — Chlorophyll"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Dünya'daki yaşamın çoğu fotosenteze bağlıdır; karadan denize her tür ekosistemde besin ağları fotosentezle başlar.",
    "numbers": [],
    "quote": "Most life on Earth depends on photosynthesis. / Because food webs in every type of ecosystem, from terrestrial to marine, begin with photosynthesis",
    "location": "National Geographic Education — Photosynthesis; National Geographic Education — Chlorophyll"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Fotosentezi bitkiler, algler ve bazı bakteri türleri yapar.",
    "numbers": [],
    "quote": "The process is carried out by plants, algae, and some types of bacteria",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Soluduğumuz oksijenin çoğu okyanustaki minik bitkilerden gelir.",
    "numbers": [],
    "quote": "Did you know that most of the oxygen we breathe comes from tiny plants in the ocean?",
    "location": "National Geographic Education — Photosynthesis"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Sonbaharda yeşil klorofil azaldıkça öteki pigmentler ortaya çıkar.",
    "numbers": [],
    "quote": "As green chlorophyll fades from trees and plants each autumn, other pigments color Earth’s landscapes.",
    "location": "NASA Science — Earth Observatory"
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
