# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Midemiz yemeği nasıl sindirir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 28, "paperId": "topic:midemiz-yemegi-nasil-sindirir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Your Digestive System",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/digestive-system.html"
  },
  {
    "id": "k2",
    "title": "Your Digestive System & How It Works",
    "publisher": "NIDDK",
    "url": "https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Besin yakıtımızdır; besin öğeleri hücrelere çalışmak için gereken enerjiyi ve maddeleri verir; ama önce vücudun emip kullanabileceği küçük parçalara sindirilmelidir.",
    "numbers": [],
    "quote": "Food is our fuel, and its nutrients give our bodies' cells the energy and substances they need to work. / But before food can do that, it must be digested into small pieces the body can absorb and use.",
    "location": "Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Sindirim sistemi besin öğelerini vücudun emip enerji için kullanabileceği kadar küçük parçalara ayırır.",
    "numbers": [],
    "quote": "Your digestive system breaks nutrients into parts small enough for your body to absorb and use for energy",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Sindirim ağızda, besin mideye ulaşmadan çok önce başlar; dişler besini koparıp doğrar, tükürük onu ıslatır; tükürüğü tükürük bezleri yapar.",
    "numbers": [],
    "quote": "Digestion begins in the mouth, well before food reaches the stomach. / As the teeth tear and chop the food, spit moistens it for easy swallowing. / Your salivary glands make saliva, a digestive juice",
    "location": "Nemours KidsHealth — Your Digestive System; NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Tükürükteki amilaz adlı sindirim enzimi bazı karbonhidratları parçalamaya başlar; tükürükteki enzim nişastaları parçalamaya başlar.",
    "numbers": [],
    "quote": "A digestive enzyme in saliva called amylase (AH-meh-lace) starts to break down some of the carbohydrates / Saliva also has an enzyme that begins to break down starches in your food.",
    "location": "Nemours KidsHealth — Your Digestive System; NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Yemeği koklamak ya da düşünmek bile ağzı sulandırabilir; beyin tükürük bezlerine sinyal gönderir.",
    "numbers": [],
    "quote": "Just by smelling that homemade apple pie or thinking about how delicious that ripe tomato is going to be / your brain sends a signal that causes your salivary glands to \"make your mouth water\" to prepare you to eat.",
    "location": "Nemours KidsHealth — Your Digestive System; NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Yutarken dil besini boğaza iter; epiglot denen küçük doku kapağı boğulmayı önlemek için soluk borusunun üstüne kapanır.",
    "numbers": [],
    "quote": "When you swallow, your tongue pushes the food into your throat. / A small flap of tissue, called the epiglottis, folds over your windpipe to prevent choking",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Peristalsis denen kas kasılma dalgaları besini yemek borusundan mideye iter.",
    "numbers": [],
    "quote": "Waves of muscle contractions called peristalsis (per-uh-STALL-sus) force food down through the esophagus to the stomach.",
    "location": "Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Yemek borusunun sonundaki sfinkter genelde kapalı durur ve mide içeriğinin yemek borusuna geri akmasını engeller.",
    "numbers": [],
    "quote": "This sphincter usually stays closed to keep what’s in your stomach from flowing back into your esophagus.",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Mide kasları besini asit ve enzim içeren sindirim sıvılarıyla çalkalayıp karıştırır; mide duvarındaki bezler mide asidi ve enzim yapar; midedeki sindirim için asitli ortam gerekir.",
    "numbers": [],
    "quote": "The stomach muscles churn and mix the food with digestive juices that have acids and enzymes / Glands in your stomach lining make stomach acid and enzymes that break down food. / An acidic environment is needed for the digestion that takes place in the stomach.",
    "location": "Nemours KidsHealth — Your Digestive System; NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Mide, kimus denen içeriğini yavaş yavaş ince bağırsağa boşaltır; midenin çıkışındaki ceviz büyüklüğündeki pilor kapağı kimusu midede tutar.",
    "numbers": [],
    "quote": "The stomach slowly empties its contents, called chyme, into your small intestine. / A walnut-sized muscular valve at the outlet of the stomach called the pylorus (pie-LOR-us) keeps chyme in the stomach",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works; Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "İnce bağırsağa uzunluğu yüzünden değil genişliği yüzünden ince denir; aslında kalın bağırsaktan çok daha uzundur.",
    "numbers": [],
    "quote": "The small intestine is called small because of its width, not its length. It's actually much longer than the large intestine.",
    "location": "Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi villus ile kaplıdır; besinler villuslar aracılığıyla kana emilir; ince bağırsak duvarları suyu ve sindirilmiş besinleri kana emer.",
    "numbers": [],
    "quote": "The inner wall of the small intestine is covered with millions of microscopic, finger-like projections called villi (VIH-lie). / The villi are the vehicles through which nutrients can be absorbed into the blood. / The walls of the small intestine absorb water and the digested nutrients into your bloodstream.",
    "location": "Nemours KidsHealth — Your Digestive System; NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "İnce bağırsağın kasları besini pankreas, karaciğer ve bağırsaktan gelen sindirim sıvılarıyla karıştırır; karaciğer yağların sindirimine yardım eden safrayı yapar; safra kesesi safrayı öğünler arasında saklar; pankreas karbonhidrat, yağ ve proteinleri parçalayan enzimler yapar.",
    "numbers": [],
    "quote": "The muscles of the small intestine mix food with digestive juices from the pancreas, liver, and intestine / Your liver makes a digestive juice called bile that helps digest fats and some vitamins. / Your gallbladder stores bile between meals. / Your pancreas makes a digestive juice that has enzymes that break down carbohydrates, fats, and proteins.",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Kalın bağırsak suyu emer ve atığı sıvıdan katı dışkıya dönüştürür.",
    "numbers": [],
    "quote": "The large intestine absorbs water and changes the waste from liquid into stool. / The large intestine's main job is to remove water from the undigested matter and form solid waste (poop) to be excreted.",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works; Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Kalın bağırsaktaki bakteriler kalan besin öğelerini parçalamaya yardım eder ve K vitamini yapar.",
    "numbers": [],
    "quote": "Bacteria in your large intestine help break down remaining nutrients and make vitamin K.",
    "location": "NIDDK (NIH) — Your Digestive System & How It Works"
  },
  {
    "id": "f16",
    "kind": "number",
    "statement": "Bir yetişkinin sindirim kanalı yaklaşık 9 metre uzunluğundadır.",
    "numbers": [
      "9"
    ],
    "quote": "An adult's digestive tract is about 30 feet (about 9 meters) long.",
    "location": "Nemours KidsHealth — Your Digestive System"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Vücudun besini tamamen sindirmesi saatler sürer.",
    "numbers": [],
    "quote": "It takes hours for our bodies to fully digest food.",
    "location": "Nemours KidsHealth — Your Digestive System"
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
            "gut"
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
