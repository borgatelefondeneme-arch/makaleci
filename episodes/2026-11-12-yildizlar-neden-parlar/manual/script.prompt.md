# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Yıldızlar neden parlar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 13, "paperId": "topic:yildizlar-neden-parlar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Stars",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/universe/stars/"
  },
  {
    "id": "k2",
    "title": "Star Types",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/universe/stars/types/"
  },
  {
    "id": "k3",
    "title": "Sun: Facts",
    "publisher": "NASA",
    "url": "https://science.nasa.gov/sun/facts/"
  },
  {
    "id": "k4",
    "title": "How Does Our Sun Compare With Other Stars?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/sun-compare/en/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Yıldızlar sıcak gazdan oluşan dev toplardır; çoğunlukla hidrojenden, biraz helyumdan ve az miktarda başka elementlerden oluşurlar.",
    "numbers": [],
    "quote": "Stars are giant balls of hot gas – mostly hydrogen, with some helium and small amounts of other elements.",
    "location": "NASA Science — Stars (Star Basics)"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur; plazma denen çok sıcak, elektrik yüklü gazdan oluşur.",
    "numbers": [],
    "quote": "The Sun is a huge ball of hydrogen and helium held together by its own gravity. / The Sun is made of super-hot, electrically charged gas called plasma.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Yıldızlar moleküler bulut denen büyük gaz ve toz bulutlarında oluşur; kütle çekimi bazı topakların çökmesine yol açar; topak yüz binlerce yıl boyunca kütle kazanır, dönmeye başlar ve ısınır; sonunda bir önyıldız (bebek yıldız) gelişir.",
    "numbers": [],
    "quote": "Stars form in large clouds of gas and dust called molecular clouds. / Eventually, gravity causes some of these clumps to collapse. / Over hundreds of thousands of years, the clump gains mass, starts to spin, and heats up. / which eventually leads to the development of a protostar – a baby star.",
    "location": "NASA Science — Stars (Star Basics); NASA Science — Star Types"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Yıldızın çekirdeğindeki muazzam basınç ve sıcaklık hidrojen atomlarının çekirdeklerini sıkıştırarak helyum oluşturur; çekirdek kaynaşması (füzyon) enerji açığa çıkarır, yıldızı ısıtır ve kütle çekimi altında çökmesini önler; oluşan basınç kütle çekimine karşı iter.",
    "numbers": [],
    "quote": "immense pressures and temperatures in the star's core squeeze the nuclei of hydrogen atoms together to form helium / Nuclear fusion releases energy, which heats the star and prevents it from further collapsing under the force of gravity. / Fusion releases energy that heats the star, creating pressure that pushes against the force of its gravity.",
    "location": "NASA Science — Stars (Star Basics); NASA Science — Star Types"
  },
  {
    "id": "f5",
    "kind": "number",
    "statement": "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir; yüzeyinde 5.500 santigrat derece.",
    "numbers": [
      "15",
      "5.500"
    ],
    "quote": "The temperature in the Sun's core is about 27 million degrees Fahrenheit (15 million degrees Celsius) / It's 10,000 degrees Fahrenheit (5,500 degrees Celsius) at the surface",
    "location": "NASA Science — Sun: Facts; NASA Space Place — How Does Our Sun Compare With Other Stars?"
  },
  {
    "id": "f6",
    "kind": "number",
    "statement": "Güneş yaklaşık 4,6 milyar yıl önce oluştu; Dünya'dan yaklaşık 150 milyon kilometre uzaktadır; hacmini doldurmak için 1,3 milyon Dünya gerekir.",
    "numbers": [
      "4.6",
      "150",
      "1.3"
    ],
    "quote": "The Sun formed about 4.6 billion years ago in a giant, spinning cloud of gas and dust called the solar nebula. / The Sun is about 93 million miles (150 million kilometers) from Earth. / it would take 1.3 million Earths to fill the Sun's volume",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Çekirdeğinde hidrojeni helyuma kaynaştıran yıldıza ana kol yıldızı denir; Güneş ana kol evresinin aşağı yukarı ortasındadır.",
    "numbers": [],
    "quote": "Scientists call a star that is fusing hydrogen to helium in its core a main sequence star. / Our Sun is roughly midway through its main sequence stage.",
    "location": "NASA Science — Star Types; NASA Science — Stars (Star Basics)"
  },
  {
    "id": "f8",
    "kind": "number",
    "statement": "Kırmızı cüceler en küçük ana kol yıldızlarıdır; çapı Güneş'inkinin 1.000 katı olan yıldızlar bulunmuştur.",
    "numbers": [
      "1.000"
    ],
    "quote": "Red dwarfs are the smallest main sequence stars – just a fraction of the Sun's size and mass. / We have found stars that are 1,000 times bigger in diameter than our sun.",
    "location": "NASA Science — Star Types; NASA Space Place — How Does Our Sun Compare With Other Stars?"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Güneş yaklaşık 5 milyar yıl sonra kırmızı dev olacak; Merkür'ü ve Venüs'ü, belki Dünya'yı da yutacak kadar büyüyecek.",
    "numbers": [
      "5"
    ],
    "quote": "The Sun will become a red giant in about 5 billion years. / becoming so large that it will engulf Mercury and Venus, and possibly Earth as well.",
    "location": "NASA Science — Star Types; NASA Science — Sun: Facts"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Genişleyen toz ve gaz bulutuna gezegenimsi bulutsu, geriye kalan yıldız kalıntısına beyaz cüce denir.",
    "numbers": [],
    "quote": "creating an expanding cloud of dust and gas called a planetary nebula. / Scientists call this kind of stellar remnant a white dwarf.",
    "location": "NASA Science — Star Types"
  },
  {
    "id": "f11",
    "kind": "number",
    "statement": "Büyük kütleli yıldızların sonu süpernova denen dev bir patlamadır; kütlesi Güneş'in yaklaşık 8 ile 20 katı arasındaki yıldızlardan nötron yıldızı oluşur; daha ağır yıldızlar kara delik üretir.",
    "numbers": [
      "8",
      "20"
    ],
    "quote": "The result is a huge explosion called a supernova. / A neutron star forms when a main sequence star with between about eight and 20 times the Sun's mass / (Heavier stars produce stellar-mass black holes.)",
    "location": "NASA Science — Star Types"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Füzyon karbonu oksijen, neon ve magnezyum gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir silisyumun demire kaynaşmasına kadar sürer; süpernovaların uzaya saçtığı madde gelecekteki moleküler bulutları zenginleştirir.",
    "numbers": [],
    "quote": "Fusion converts carbon into heavier elements like oxygen, neon, and magnesium / For the largest stars, this chain continues until silicon fuses into iron. / Material cast into the cosmos by supernovae and other stellar events will enrich future molecular clouds",
    "location": "NASA Science — Stars (Star Basics)"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Samanyolu'nda 100 milyardan fazla yıldız vardır; evrende bir septilyona kadar yıldız olabilir: 1'in yanında 24 sıfır.",
    "numbers": [
      "100",
      "1",
      "24"
    ],
    "quote": "Our Milky Way alone contains more than 100 billion, including our most well-studied star, the Sun. / Astronomers estimate that the universe could contain up to one septillion stars – that's a one followed by 24 zeros.",
    "location": "NASA Science — Stars (Star Basics)"
  },
  {
    "id": "f14",
    "kind": "number",
    "statement": "En yakın yıldız komşumuz kırmızı cüce Proxima Centauri'dir; 4,24 ışık yılı uzaktadır. Işık yılı, ışığın bir yılda aldığı yoldur.",
    "numbers": [
      "4.24"
    ],
    "quote": "Our closest stellar neighbor, shown here in this Hubble image, is the red dwarf Proxima Centauri. / red dwarf star Proxima Centauri is 4.24 light-years away / A light-year is the distance light travels in one year",
    "location": "NASA Science — Star Types; NASA Science — Sun: Facts"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Sirius gece gökyüzünün en parlak yıldızıdır; birçok ana kol yıldızı çıplak gözle görülebilir.",
    "numbers": [],
    "quote": "Sirius – the brightest star in the night sky / Many main sequence stars can be seen with the unaided eye, such as Sirius",
    "location": "NASA Science — Star Types"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Gözleri korumadan Güneş'e asla doğrudan bakılmamalıdır.",
    "numbers": [],
    "quote": "never look directly at the Sun without protecting your eyes.",
    "location": "NASA Science — Sun: Facts"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Her yıldızın kendi yaşam döngüsü vardır; birkaç milyon yıldan trilyonlarca yıla kadar sürer.",
    "numbers": [],
    "quote": "Every star has its own life cycle, ranging from a few million to trillions of years",
    "location": "NASA Science — Stars (Star Basics)"
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
            "storm"
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
