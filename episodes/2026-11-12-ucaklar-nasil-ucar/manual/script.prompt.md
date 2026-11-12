# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Uçaklar nasıl uçar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 20, "paperId": "topic:ucaklar-nasil-ucar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Four Forces on an Airplane",
    "publisher": "NASA",
    "url": "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/four-forces-on-an-airplane/"
  },
  {
    "id": "k2",
    "title": "What is Lift?",
    "publisher": "NASA",
    "url": "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-lift/"
  },
  {
    "id": "k3",
    "title": "What is Drag?",
    "publisher": "NASA",
    "url": "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-drag/"
  },
  {
    "id": "k4",
    "title": "What is Thrust?",
    "publisher": "NASA",
    "url": "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/what-is-thrust/"
  },
  {
    "id": "k5",
    "title": "How Things Fly",
    "publisher": "Smithsonian",
    "url": "https://airandspace.si.edu/exhibitions/how-things-fly"
  },
  {
    "id": "k6",
    "title": "1903 Wright Flyer",
    "publisher": "Smithsonian",
    "url": "https://airandspace.si.edu/collection-objects/1903-wright-flyer/nasm_A19610048000"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Kuvvet, belirli bir yönde bir itme ya da çekme olarak düşünülebilir.",
    "numbers": [],
    "quote": "A force may be thought of as a push or pull in a specific direction.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Ağırlık her zaman Dünya'nın merkezine doğru yönelen bir kuvvettir; uçuşta uçak ağırlık merkezi denen nokta çevresinde döner.",
    "numbers": [],
    "quote": "Weight is a force that is always directed toward the center of the earth. / In flight, the airplane rotates about the center of gravity.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Ağırlığı yenmek için uçaklar kaldırma denen karşıt bir kuvvet üretir; kaldırmanın büyüklüğü uçağın biçimine, boyutuna ve hızına bağlıdır.",
    "numbers": [],
    "quote": "To overcome the weight force, airplanes generate an opposing force called lift. / The magnitude of the lift depends on several factors including the shape, size, and velocity of the aircraft.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Hava uçağın hareketine direnir; bu direnç kuvvetine sürükleme denir. Sürüklemeyi yenmek için uçaklar bir itki sistemiyle itme kuvveti üretir.",
    "numbers": [],
    "quote": "The air resists the motion of the aircraft and the resistance force is called drag. / To overcome drag, airplanes use a propulsion system to generate a force called thrust.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Kuvvetler dengedeyse uçak sabit hızla yol alır; dengede değilse en büyük kuvvetin yönünde hızlanır.",
    "numbers": [],
    "quote": "If the forces are balanced, the aircraft cruises at constant velocity. / If the forces are unbalanced, the aircraft accelerates in the direction of the largest force.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Kaldırma, hareket eden bir gaz akışı katı bir cisim tarafından döndürüldüğünde oluşur; kaldırma Newton'un etki-tepki yasasına göre ters yönde üretilir; uçak kanadında hem üst hem alt yüzey akışın dönmesine katkıda bulunur.",
    "numbers": [],
    "quote": "Lift occurs when a moving flow of gas is turned by a solid object. / the lift is generated in the opposite direction, according to Newton’s Third Law of action and reaction. / For an aircraft wing, both the upper and lower surfaces contribute to the flow turning.",
    "location": "NASA Glenn — What is Lift?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Kaldırma, cisim ile akışkan arasındaki hız farkıyla oluşur; kaldırma için cismin akışkanla temas etmesi gerekir: akışkan yoksa kaldırma da yok. Kaldıran kanadın üst ve alt yüzeyleri arasında basınç farkı vardır.",
    "numbers": [],
    "quote": "Lift is generated by the difference in velocity between the solid object and the fluid. / no fluid, no lift. / For a lifting wing, there is a pressure difference between the upper and lower surfaces of the wing.",
    "location": "NASA Glenn — What is Lift?; NASA Glenn — What is Drag?"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Kaldırmaya ilişkin açıklamaların birçoğu yanıltıcı ve yanlıştır; üst yüzeyin akışı döndürmedeki payını yok saymak yanlış bir kaldırma kuramına götürür.",
    "numbers": [],
    "quote": "Unfortunately, many of the explanations are misleading and incorrect. / Neglecting the upper surface’s part in turning the flow leads to an incorrect theory of lift.",
    "location": "NASA Glenn — What is Lift?"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Sürükleme, uçağın havadaki hareketine karşı koyan aerodinamik kuvvettir; uçağın biçimine bağlıdır (biçim sürüklemesi); pürüzsüz, cilalı bir yüzey pürüzlü bir yüzeyden daha az sürtünme üretir.",
    "numbers": [],
    "quote": "Drag is the aerodynamic force that opposes an aircraft’s motion through the air. / This source of drag depends on the shape of the aircraft and is called form drag. / a smooth, waxed surface produces less skin friction than a roughened surface.",
    "location": "NASA Glenn — What is Drag?"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "İtme, uçağı havada ilerleten kuvvettir; motorlarda bir itki sistemiyle üretilir; hızlandırılan gazın tersi yönünde oluşur: sıcak gaz arkadan çıkar, itme öne doğru iter (Newton'un etki-tepki yasası).",
    "numbers": [],
    "quote": "Thrust is the force which moves an aircraft through the air. / Thrust is generated by the engines of the aircraft through some kind of propulsion system. / the thrust is generated in the opposite direction from the accelerated gas. / The hot gas goes out the back, but the thrust pushes towards the front.",
    "location": "NASA Glenn — What is Thrust?; NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "İtki sistemleri arasında pervane, türbin ya da jet motoru, ramjet ve roket vardır.",
    "numbers": [],
    "quote": "the propeller, the turbine, or jet, engine, the ramjet, and the rocket",
    "location": "NASA Glenn — What is Thrust?"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Uçağı yalpa, yunuslama ve sapma hareketlerinde aerodinamik yüzeyler denetler; pilot uçağı dengede tutmak için kumandaları sürekli ayarlar.",
    "numbers": [],
    "quote": "Aerodynamic surfaces are used to control the aircraft in roll, pitch, and yaw. / So the pilot must constantly adjust the controls to keep the airplane balanced, or trimmed.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Wright kardeşlerin ilk motorlu uçağı 17 Aralık 1903'te Kitty Hawk'ta uçtu: 12 saniyelik uçuşta 36 metre yol aldı; pilotu Orville'di; günün en iyi uçuşunda Wilbur 59 saniyede 255,6 metre gitti.",
    "numbers": [
      "17",
      "1903",
      "12",
      "36",
      "59",
      "255.6"
    ],
    "quote": "the Wrights' first powered airplane flew at Kitty Hawk, North Carolina, on December 17, 1903 / for a 12-second flight, traveling 36 m (120 ft). / with Orville piloting. / The best flight of the day, with Wilbur at the controls, covered 255.6 m (852 ft) in 59 seconds.",
    "location": "Smithsonian National Air and Space Museum — 1903 Wright Flyer"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Wright kardeşler pervaneleri dönen kanatlar olarak tasarladı; kanat uçlarını ters yönlerde bükerek uçağı yönlendirdiler; verimli bir kanat kesiti geliştirmekle uğraştılar.",
    "numbers": [],
    "quote": "The brothers conceived the propellers as rotary wings, producing a horizontal thrust force aerodynamically. / by twisting, or warping, the tips of the wings in opposite directions / the Wrights had to grapple with developing an efficient airfoil shape",
    "location": "Smithsonian National Air and Space Museum — 1903 Wright Flyer"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Kâğıt uçaklar en bilinen planör örneğidir.",
    "numbers": [],
    "quote": "Paper airplanes are the most obvious example, but there are many kinds of gliders.",
    "location": "NASA Glenn — Four Forces on an Airplane"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Bir uçak nasıl havada kalır? Hava gibi hafif bir şey bütün o ağırlığı nasıl taşır?",
    "numbers": [],
    "quote": "How does an airplane stay aloft? How can something as insubstantial as air support all that weight?",
    "location": "Smithsonian National Air and Space Museum — How Things Fly"
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
            "micro"
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
