# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Kemiklerimiz neden güçlü?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 25, "paperId": "topic:kemiklerimiz-neden-guclu".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Bones, Muscles & Joints",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/bones.html"
  },
  {
    "id": "k2",
    "title": "Broken Bones (Fractures)",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/broken-bones.html"
  },
  {
    "id": "k3",
    "title": "Child Activity: An Overview",
    "publisher": "CDC",
    "url": "https://www.cdc.gov/physical-activity-basics/guidelines/children.html"
  },
  {
    "id": "k4",
    "title": "Calcium",
    "publisher": "NHS",
    "url": "https://www.nhs.uk/conditions/vitamins-and-minerals/calcium/"
  },
  {
    "id": "k5",
    "title": "Vitamin D",
    "publisher": "NHS",
    "url": "https://www.nhs.uk/conditions/vitamins-and-minerals/vitamin-d/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Kemikler vücudumuza destek olur ve biçimini oluşturur; kafatası beyni korur; kaburgalar kalbi ve akciğerleri barındıran bir kafes oluşturur; kaslar eklemleri çekerek hareket etmemizi sağlar.",
    "numbers": [],
    "quote": "Bones provide support for our bodies and help form our shape. / The skull protects the brain and forms the shape of the face. / The ribs form a cage that shelters the heart and lungs / Muscles pull on the joints, allowing us to move.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Kemikler kalsiyum depolar ve gerektiğinde bir kısmını kana verir; vücudun kan hücrelerinin çoğu kemiklerin içindeki yumuşak kemik iliğinde yapılır.",
    "numbers": [],
    "quote": "Bones store calcium and release some into the bloodstream when it's needed by other parts of the body. / In this soft bone is where most of the body's blood cells are made.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Kemikler kolajen adlı bir proteinden yapılmış bir çatı ile kalsiyum fosfat adlı bir mineralden oluşur.",
    "numbers": [],
    "quote": "Bones are made up of a framework of a protein called collagen with a mineral called calcium phosphate",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Kompakt kemik kemiğin katı, sert dış kısmıdır; içinden kan damarları ve sinirler taşıyan delikler ve kanallar geçer; süngere benzeyen süngerimsi kemik kompakt kemiğin içindedir.",
    "numbers": [],
    "quote": "Compact bone is the solid, hard outside part of the bone. / Holes and channels run through it, carrying blood vessels and nerves. / Cancellous (KAN-suh-lus) bone, which looks like a sponge, is inside compact bone.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Vücut kemiklerin canlı dokusunu sürekli yeniler ve yeniden biçimlendirir; osteoblastlar yeni kemik yapar ve hasarı onarır; osteoklastlar kemiği yıkar ve biçimlendirir.",
    "numbers": [],
    "quote": "a body constantly renews and reshapes the bones' living tissue. / osteoblasts (AHS-tee-uh-blastz), which make new bone and help repair damage / osteoclasts (AHS-tee-o-klasts), which break down bone and help to sculpt and shape it",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Çocukların ve genç ergenlerin kemiklerinde büyüme plakları denen 'büyüme bölgeleri' vardır; kızlar daha erken olgunlaştığı için büyüme plakları daha erken sert kemiğe dönüşür.",
    "numbers": [],
    "quote": "The bones of kids and young teens are smaller than those of adults and contain \"growing zones\" called growth plates. / Because girls mature at an earlier age than boys, their growth plates change into hard bone at an earlier age.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Kafatasının kubbesi, doğum sırasında biraz hareket eden ve kafatası büyümesini tamamlayınca birbirine kaynayan kemik plakalardan oluşur.",
    "numbers": [],
    "quote": "bony plates, which move slightly during birth and then fuse together as the skull finishes growing.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Eklemler iki kemiğin buluştuğu yerdir ve iskeleti esnek yapar; kemikler birbirine bağ denen uzun, lifli kayışlarla bağlanır; kıkırdak eklemlerde kemikleri destekleyen ve koruyan esnek bir maddedir; kaslar kemiğe kiriş denen ip gibi yapılarla bağlanır; menteşe eklemler dizde ve dirsekte olduğu gibi tek yönde hareket sağlar.",
    "numbers": [],
    "quote": "Joints are where two bones meet. They make the skeleton flexible — without them, movement would be impossible. / Bones are fastened to other bones by long, fibrous straps called ligaments / Cartilage (KAR-tul-ij), a flexible, rubbery substance in our joints, supports bones and protects them / Skeletal muscle is attached by cord-like tendons to bone / Hinge joints allow movement in one direction, as seen in the knees and elbows.",
    "location": "Nemours KidsHealth — Bones, Muscles & Joints"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "D vitamini vücuttaki kalsiyum ve fosfat miktarını düzenler; vücut, açık havada deriye düşen doğrudan güneş ışığıyla D vitamini üretir; kalsiyum eksikliği çocuklarda raşitizme yol açabilir.",
    "numbers": [],
    "quote": "Vitamin D helps regulate the amount of calcium and phosphate in the body. / The body creates vitamin D from direct sunlight on the skin when outdoors. / A lack of calcium could lead to a condition called rickets in children",
    "location": "NHS — Vitamin D; NHS — Calcium"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "6–17 yaş arasındaki çocuk ve gençler her gün en az 60 dakika hareketli olmalıdır; zıplama ya da koşma gibi kemik güçlendiren etkinlikler haftada en az 3 gün yer almalıdır.",
    "numbers": [
      "6",
      "17",
      "60",
      "3"
    ],
    "quote": "Children and adolescents 6 to 17 need to be active for at least 60 minutes every day. / Includes activities such as jumping or running, at least 3 days a week.",
    "location": "CDC — Child Activity: An Overview"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Kırık kemiklerin, özellikle çocuklarda, iyileşme yeteneği çok yüksektir; kırık uçları kallus denen yeni dokuyla birleşir; kallus başta yumuşaktır, sonraki haftalarda sertleşir; kırıkların çoğu alçı, atel ya da destekle tedavi edilir; tam iyileşme genellikle birkaç ay sürer; çocukların kemikleri daha yumuşak olduğu için tamamen kırılmaktan çok bükülür.",
    "numbers": [],
    "quote": "Broken bones have an amazing ability to heal, especially in children. / This is called a callus, and it joins the broken bones together. / It's soft at first, then gets harder and stronger over the following weeks. / Doctors treat most broken bones with a cast, splint, or brace. / Broken bones usually take a few months to heal completely. / Kids' bones are more likely to bend than break completely because they're softer.",
    "location": "Nemours KidsHealth — Broken Bones"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Sardalya gibi kılçığıyla yenen balıklar kalsiyum kaynağıdır; kalsiyum kemikleri yapmaya ve dişleri sağlıklı tutmaya yardım eder.",
    "numbers": [],
    "quote": "fish where you eat the bones – such as sardines and pilchards / helping build bones and keep teeth healthy",
    "location": "NHS — Calcium"
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
