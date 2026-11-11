# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Gökkuşağı nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 4, "paperId": "topic:gokkusagi-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Rainbow",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/rainbow/"
  },
  {
    "id": "k2",
    "title": "How Are Rainbows Formed?",
    "publisher": "Kraliyet Meteoroloji Derneği",
    "url": "https://www.rmets.org/metmatters/how-are-rainbows-formed"
  },
  {
    "id": "k3",
    "title": "Visible Light",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/ems/09_visiblelight/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.",
    "numbers": [],
    "quote": "A rainbow is a multicolored arc made by light striking water droplets.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Gökkuşağı bir optik yanılsamadır; gökyüzünde belirli bir noktada gerçekten bulunmaz.",
    "numbers": [],
    "quote": "A rainbow is an optical illusion—it does not actually exist in a specific spot in the sky.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Beyaz ışık, gökkuşağının bütün renklerinin karışımını gözümüzün algılama biçimidir.",
    "numbers": [],
    "quote": "White light is how our eyes perceive all the colors of the rainbow mixed together.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Kırmızı, görünür ışığın en uzun dalga boyuna; mor en kısa dalga boyuna sahiptir. İnsan gözü ışığın yalnızca belirli dalga boylarını algılar.",
    "numbers": [],
    "quote": "Red has the longest wavelength of visible light / Violet has the shortest wavelength / Typically, the human eye can detect wavelengths from 380 to 700 nanometers.",
    "location": "National Geographic Education — Rainbow; NASA Science — Visible Light"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Kırılma, Güneş ışığının havadan daha yoğun bir ortamdan geçerken yön değiştirmesidir.",
    "numbers": [],
    "quote": "Refraction occurs when the light from the sun changes direction when passing through a medium denser than air",
    "location": "Royal Meteorological Society — How Are Rainbows Formed?"
  },
  {
    "id": "f6",
    "kind": "number",
    "statement": "Güneş ışığının renkleri bir ortamda farklı hızlarda ilerler; her renk dalga boyuna göre biraz farklı açıyla kırılır. Isaac Newton 1665'te prizmanın görünür ışığı büktüğünü gösterdi.",
    "numbers": [
      "1665"
    ],
    "quote": "Sunlight is made of many different wavelengths, or colours, that travel at different speeds when passing through a medium. / Isaac Newton's experiment in 1665 showed that a prism bends visible light / each color refracts at a slightly different angle depending on the wavelength of the color.",
    "location": "Royal Meteorological Society — How Are Rainbows Formed?; NASA Science — Visible Light"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Damlaya giren ışık kırılır, damlanın arkasından yansır ve çıkarken yeniden kırılır.",
    "numbers": [],
    "quote": "Light entering a water droplet is refracted. It is then reflected by the back of the droplet. / As this reflected light leaves the droplet, it is refracted again, at multiple angles.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Güneş genellikle gökkuşağını gören kişinin arkasındadır; su damlacıkları gözlemcinin önünde olmalıdır.",
    "numbers": [],
    "quote": "The sun or other source of light is usually behind the person seeing the rainbow. / Water droplets such as rain or fog must be in front of the observer.",
    "location": "National Geographic Education — Rainbow; Royal Meteorological Society — How Are Rainbows Formed?"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Güneş ışığı izleyicinin önündeki damlalara belirli bir açıyla (42 derece) çarpar; birincil gökkuşağının merkezi, Güneş'in tam karşısındaki hayali antisolar noktadır.",
    "numbers": [
      "42"
    ],
    "quote": "sunlight strikes raindrops in front of a viewer at a precise angle (42 degrees) / the center of a primary rainbow is the antisolar point, the imaginary point exactly opposite the sun.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Gökkuşakları aslında tam çemberdir; yerdekiler yalnızca ufkun üstündeki damlalardan gelen ışığı görür; uçaktakiler bazen çemberin tamamını görebilir.",
    "numbers": [],
    "quote": "Rainbows are actually full circles. / Viewers in aircraft can sometimes see these circular rainbows. / Viewers on the ground can only see the light reflected by raindrops above the horizon.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Güneş gökyüzünde ne kadar alçaksa gözlemci yayın o kadar büyük bölümünü görür.",
    "numbers": [],
    "quote": "The lower the sun in the sky, the more of an arc of a rainbow the observer will see",
    "location": "Royal Meteorological Society — How Are Rainbows Formed?"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Renkler kırmızı, turuncu, sarı, yeşil, mavi, çivit mavisi ve mordur; kırmızı yayın dış kısmında, mor iç kısmında görünür. Birçok bilim insanına göre çivit mavisi maviye ayırt edilemeyecek kadar yakındır.",
    "numbers": [],
    "quote": "red, orange, yellow, green, blue, indigo, and violet / It usually appears on the outer part of a rainbow's arch. / it usually appears on the inner arch of the rainbow. / (Many scientists, however, think \"indigo\" is too close to blue to be truly distinguishable.)",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Gökkuşağının renkleri kenarlarında üst üste biner.",
    "numbers": [],
    "quote": "At their edges, the colors of a rainbow actually overlap.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Bazen birincil yayın üstünde soluk, ikincil bir gökkuşağı belirir; nedeni ışığın damlada iki kez yansımasıdır; bu yayda kırmızı içte, mor dıştadır.",
    "numbers": [],
    "quote": "a faint, secondary rainbow appears above the primary one. / Double rainbows are caused by light being reflected twice inside the raindrop. / red is on the inner section of the arch, while violet is on the outside.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Gökkuşağı sis, deniz serpintisi ya da şelale çevresinde de görülebilir; ay gökkuşağı Ay'ın yansıttığı ışıkla oluşur.",
    "numbers": [],
    "quote": "Rainbows can also be viewed around fog, sea spray, or waterfalls. / A moonbow, also called a lunar rainbow, is a rainbow produced by light reflected by the moon.",
    "location": "National Geographic Education — Rainbow"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Kimse aynı gökkuşağını görmez: her insanın antisolar noktası ve ufku farklıdır.",
    "numbers": [],
    "quote": "no one sees the same rainbow—each person has a different antisolar point, each person has a different horizon. / every rainbow is unique to the observer.",
    "location": "National Geographic Education — Rainbow; Royal Meteorological Society — How Are Rainbows Formed?"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Gökkuşaklarının 'ucu' yoktur, çünkü çemberdirler.",
    "numbers": [],
    "quote": "because no one sees the same rainbow and rainbows don't \"end\" (they're circles)",
    "location": "National Geographic Education — Rainbow"
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
