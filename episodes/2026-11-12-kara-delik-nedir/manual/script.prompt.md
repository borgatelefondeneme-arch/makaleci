# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Kara delik nedir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 10, "paperId": "topic:kara-delik-nedir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Black Holes",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/universe/black-holes/"
  },
  {
    "id": "k2",
    "title": "Black Hole Anatomy",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/universe/black-holes/anatomy/"
  },
  {
    "id": "k3",
    "title": "Black Hole Types",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/universe/black-holes/types/"
  },
  {
    "id": "k4",
    "title": "What Is a Black Hole? (Grades 5-8)",
    "publisher": "NASA",
    "url": "https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-a-black-hole-grades-5-8/"
  },
  {
    "id": "k5",
    "title": "First Image of a Black Hole",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/resource/first-image-of-a-black-hole/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir; güçlü kütle çekimi, maddenin çok küçük bir alana sıkışmasından kaynaklanır.",
    "numbers": [],
    "quote": "A black hole is a region in space where the pulling force of gravity is so strong that light is not able to escape. / The strong gravity occurs because matter has been pressed into a tiny space.",
    "location": "NASA — What Is a Black Hole? (Grades 5-8)"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Kara delikler aslında delik değildir; çok küçük alanlara sıkışmış dev madde yoğunlaşmalarıdır.",
    "numbers": [],
    "quote": "These objects aren’t really holes. / They’re huge concentrations of matter packed into very tiny spaces.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Yıldız kütleli kara delikler, çok büyük kütleli bir yıldızın merkezi kendi üzerine çökünce oluşur; yıldız süpernova olarak patlar; kütlesi Güneş'in yaklaşık 20 katı ya da daha fazlaysa merkez yıldız kütleli bir kara deliğe çöker.",
    "numbers": [
      "20"
    ],
    "quote": "Stellar black holes form when the center of a very massive star collapses in upon itself. / its core collapses, rebounds, and explodes as a supernova. / If it had around 20 times the Sun’s mass or more, the star’s core collapses into a stellar-mass black hole.",
    "location": "NASA — What Is a Black Hole? (Grades 5-8); NASA Science — Black Hole Types"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Güneş'in kütlesi kara deliğe çökmeye yetmez.",
    "numbers": [],
    "quote": "The sun does not have enough mass to collapse into a black hole.",
    "location": "NASA — What Is a Black Hole? (Grades 5-8)"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Olay ufku kara deliğin yüzeyi gibi düşünülebilir; onu geçen her şey, ışık bile, içeride kalmaya mahkûmdur. Bu sınırın içinde kaçış için gereken hız ışık hızını aşar; hiçbir şey ışıktan hızlı gidemez.",
    "numbers": [],
    "quote": "We can think of the event horizon as the black hole’s surface. / So whatever passes into the event horizon is doomed to stay inside it – even light. / Inside this boundary, the velocity needed to escape the black hole exceeds the speed of light, which is as fast as anything can go.",
    "location": "NASA Science — Black Hole Anatomy"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Kara deliğin tam merkezinde maddenin sonsuz yoğunluğa ezildiği bir nokta (tekillik) vardır.",
    "numbers": [],
    "quote": "the very center of a black hole contains a point where matter is crushed to infinite density.",
    "location": "NASA Science — Black Hole Anatomy"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Kara delikten gelen ışığın ana kaynağı birikim diskidir; gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışını yayar.",
    "numbers": [],
    "quote": "The main light source from a black hole is a structure called an accretion disk. / the gas heats to very high temperatures and releases X-ray light in all directions.",
    "location": "NASA Science — Black Hole Anatomy; NASA — What Is a Black Hole? (Grades 5-8)"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Bazı kara deliklerden zıt yönlere fışkıran bir çift jet çıkar.",
    "numbers": [],
    "quote": "a pair of jets that blast away from it in opposite directions.",
    "location": "NASA Science — Black Hole Anatomy"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Kara delikler kütlelerine göre üç gruba ayrılır: yıldız kütleli (Güneş'in birkaç katından yüzlerce katına), orta kütleli ve süper kütleli (Güneş'in yüz binlerce katından milyarlarca katına).",
    "numbers": [],
    "quote": "divide black holes into three categories according to their mass / The masses of these newly born objects can range from a few to hundreds of times the Sun’s mass / These monster objects have hundreds of thousands to billions of times the Sun’s mass / These should range from around one hundred to hundreds of thousands of times the Sun’s mass",
    "location": "NASA Science — Black Hole Types"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Bizim gökadamızın merkezindeki süper kütleli kara delik Sagittarius A*'dır; kütlesi Güneş'in 4 milyon katıdır.",
    "numbers": [
      "4"
    ],
    "quote": "Our is called Sagittarius A* (pronounced ey-star), and it’s 4 million times the Sun’s mass.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için fiilen görünmezdir. Süper kütleli bir kara deliğin güçlü kütle çekimi, yıldızların çevresinde belirli bir biçimde dolanmasına yol açabilir.",
    "numbers": [],
    "quote": "Black holes don’t emit or reflect light, making them effectively invisible to telescopes. / A supermassive black hole’s intense gravity can cause stars to orbit around it in a particular way.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Kara delikler uzay-zamanın dokusunda kütle çekim dalgaları denen dalgalanmalar yaratır.",
    "numbers": [],
    "quote": "they create ripples in the fabric of space-time called gravitational waves.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Bilim insanları Olay Ufku Teleskobu ile M87 gökadasının merkezindeki kara deliğin görüntüsünü elde etti (2019); Dünya'dan yaklaşık 55 milyon ışık yılı uzaktadır.",
    "numbers": [
      "87",
      "55",
      "2019"
    ],
    "quote": "Using the Event Horizon Telescope, scientists obtained an image of the black hole at the center of the galaxy M87. / located about 55 million light years from Earth. (April 10, 2019)",
    "location": "NASA Science — First Image of a Black Hole"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Spagettileşme, maddenin kara deliğe fazla yaklaşınca başına gelenleri anlatan gerçek bir terimdir: madde yatayda sıkışır, dikeyde uzar ve bir erişteye benzer.",
    "numbers": [],
    "quote": "A real term that describes what happens when matter gets too close to a black hole. / It’s squeezed horizontally and stretched vertically, resembling a noodle.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Kara delikler kozmik elektrik süpürgesi değildir; başka maddeleri emmez. Yeterince uzaktan kütle çekim etkileri aynı kütledeki başka cisimlerinkiyle aynıdır.",
    "numbers": [],
    "quote": "Cosmic vacuum cleaners. Black holes don’t suck in other matter. / From far enough away, their gravitational effects are just like those of other objects of the same mass.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Güneş'in yerini aynı kütlede bir kara delik alsaydı Dünya içine düşmezdi; gezegenler şimdi Güneş'in çevresinde dolandıkları gibi dolanmayı sürdürürdü.",
    "numbers": [],
    "quote": "If a black hole with the same mass as the sun were to replace the sun, Earth would not fall in. / The planets would still orbit the black hole as they orbit the sun now.",
    "location": "NASA — What Is a Black Hole? (Grades 5-8)"
  },
  {
    "id": "f17",
    "kind": "number",
    "statement": "Bilinen en yakın kara delik (Gaia BH1) yaklaşık 1.500 ışık yılı uzaktadır.",
    "numbers": [
      "1.500",
      "1"
    ],
    "quote": "The nearest known black hole, called Gaia BH1, is about 1,500 light-years away.",
    "location": "NASA Science — Black Holes"
  },
  {
    "id": "f18",
    "kind": "number",
    "statement": "Gözlenen en büyük kütleli kara delik TON 618'dir: Güneş'in 66 milyar katı kütlededir.",
    "numbers": [
      "618",
      "66"
    ],
    "quote": "The most massive black hole observed, TON 618, tips the scales at 66 billion times the Sun’s mass.",
    "location": "NASA Science — Black Holes"
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
