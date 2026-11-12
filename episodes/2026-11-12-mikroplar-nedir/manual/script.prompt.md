# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Mikroplar nedir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 21, "paperId": "topic:mikroplar-nedir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Fighting Germs",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/germs.html"
  },
  {
    "id": "k2",
    "title": "Immune System",
    "publisher": "KidsHealth",
    "url": "https://kidshealth.org/en/kids/immune.html"
  },
  {
    "id": "k3",
    "title": "About Handwashing",
    "publisher": "CDC",
    "url": "https://www.cdc.gov/clean-hands/about/index.html"
  },
  {
    "id": "k4",
    "title": "How to wash your hands",
    "publisher": "NHS",
    "url": "https://www.nhs.uk/live-well/healthy-body/best-way-to-wash-your-hands/"
  },
  {
    "id": "k5",
    "title": "Genetics Glossary: Bacteria",
    "publisher": "NIH",
    "url": "https://www.genome.gov/genetics-glossary/Bacteria"
  },
  {
    "id": "k6",
    "title": "Genetics Glossary: Virus",
    "publisher": "NIH",
    "url": "https://www.genome.gov/genetics-glossary/Virus"
  },
  {
    "id": "k7",
    "title": "About Antimicrobial Resistance",
    "publisher": "CDC",
    "url": "https://www.cdc.gov/antimicrobial-resistance/about/index.html"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "'Mikrop' sözcüğü hastalığa yol açabilen mikroskobik bakterileri, virüsleri, mantarları ve protozoaları anlatır.",
    "numbers": [],
    "quote": "The term \"germs\" refers to the microscopic bacteria, viruses, fungi, and protozoa that can cause disease.",
    "location": "Nemours KidsHealth — Fighting Germs"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Mikropların çoğu zararsızdır, hatta insanlara yararlıdır; enfeksiyona yol açanlara patojen denir.",
    "numbers": [],
    "quote": "Pathogens are germs that cause infections. Most germs are harmless and even helpful to people.",
    "location": "CDC — About Antimicrobial Resistance"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Bakteriler küçük, tek hücreli canlılardır; insan vücudu bakteriyle doludur ve insan hücresinden daha çok bakteri hücresi içerdiği tahmin edilir; vücuttaki bakterilerin çoğu zararsız, bazıları yararlıdır; görece az sayıda tür hastalık yapar.",
    "numbers": [],
    "quote": "Bacteria are small single-celled organisms. / The human body is full of bacteria, and in fact is estimated to contain more bacterial cells than human cells. / Most bacteria in the body are harmless, and some are even helpful. / A relatively small number of species cause disease.",
    "location": "NIH (NHGRI) — Genetics Glossary: Bacteria"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Bakteriler küre, çubuk ya da sarmal biçiminde olabilir; sindirim sistemimizdeki bakteriler vücudumuzun normal çalışması için gereklidir.",
    "numbers": [],
    "quote": "They can be spheres, they can be rods, or they can be spirals. / in our digestive system, in the gut, we have bacteria that are very necessary to help our bodies function in a normal way.",
    "location": "NIH (NHGRI) — Genetics Glossary: Bacteria"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Virüs, bir protein kılıfla çevrili bir nükleik asit (DNA ya da RNA) parçasından oluşan bulaşıcı bir mikroptur; tek başına çoğalamaz, hücreleri enfekte edip konak hücrenin parçalarıyla kendini kopyalar; çoğu zaman bu sırada konak hücreyi öldürür.",
    "numbers": [],
    "quote": "A virus is an infectious microbe consisting of a segment of nucleic acid (either DNA or RNA) surrounded by a protein coat. / A virus cannot replicate alone; instead, it must infect cells and use components of the host cell to make copies of itself. / Often, a virus ends up killing the host cell in the process",
    "location": "NIH (NHGRI) — Genetics Glossary: Virus"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Mikropların çoğu hapşırık ve öksürükle havadan ya da ter ve tükürük gibi vücut sıvılarıyla yayılır; yıkanmamış ellerle göze, buruna ve ağza dokunmak, ellere hapşırıp başkalarının ellerine ya da ortak eşyalara dokunmak mikropları yayar.",
    "numbers": [],
    "quote": "Most germs spread through the air in sneezes or coughs or through body fluids like sweat, saliva (spit), / Touch your eyes, nose, and mouth with unwashed hands / Blow your nose, cough, or sneeze into hands and then touch other people's hands or common objects",
    "location": "Nemours KidsHealth — Fighting Germs; CDC — About Handwashing"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Bağışıklık sistemi vücudun enfeksiyonlara karşı savunmasıdır; deri, mikropların vücuda girmesini engelleyen bir engel görevi görür.",
    "numbers": [],
    "quote": "The immune system is the body's defense against infections. / For example, the skin acts as a barrier to block germs from entering the body.",
    "location": "Nemours KidsHealth — Immune System"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Akyuvarlar (lökositler) bağışıklıkta önemli rol oynar: fagositler istilacı canlıları yer; lenfositler vücudun istilacıları hatırlamasına ve yok etmesine yardım eder; T hücreleri asker gibidir; B lenfositleri antikor yapar.",
    "numbers": [],
    "quote": "White blood cells, also called leukocytes (pronounced: LOO-kuh-sytes), play an important role in the immune system. / phagocytes (pronounced: FAH-guh-sytes), chew up invading organisms. / lymphocytes (pronounced: LIM-fuh-sytes), help the body remember the invaders and destroy them. / T cells are like the soldiers / B lymphocytes are triggered to make antibodies",
    "location": "Nemours KidsHealth — Immune System"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Antikorlar yapıldıktan sonra aynı mikropla yeniden savaşmak gerekirse diye genellikle vücutta kalır; bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.",
    "numbers": [],
    "quote": "After they're made, antibodies usually stay in our bodies in case we have to fight the same germ again. / That's why someone who gets sick with a disease, like chickenpox, usually won't get sick from it again.",
    "location": "Nemours KidsHealth — Immune System"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Aşılar hastalığa yol açan mikrobun ölü ya da zayıflatılmış hâlini (ya da parçalarını) içerir; bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar yapar.",
    "numbers": [],
    "quote": "Vaccines contain either a dead or a weakened germ (or parts of it) that causes a particular disease. / When someone gets a vaccine, their immune system acts as if there's a real infection. / It makes antibodies that recognize parts of that germ.",
    "location": "Nemours KidsHealth — Fighting Germs"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez; antimikrobiyal direnç, mikropların kendilerini öldürmek için tasarlanan ilaçları yenme yeteneği kazanmasıdır; bu, vücudun antibiyotiğe dirençli olduğu anlamına gelmez.",
    "numbers": [],
    "quote": "Antibiotics and antifungals do not work on viruses, such as colds and the flu. / Antimicrobial resistance (AR) happens when germs develop the ability to defeat the drugs designed to kill them. / It does NOT mean your body is resistant to antibiotics or antifungals.",
    "location": "CDC — About Antimicrobial Resistance"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Elleri temiz akan suyla ıslat, sabunla köpürt, en az 20 saniye ov (Doğum Günü şarkısını baştan sona iki kez), temiz suyla durula ve temiz havluyla kurula. Çoğu durumda mikroplardan kurtulmanın en iyi yolu sabun ve suyla yıkamaktır.",
    "numbers": [
      "20"
    ],
    "quote": "Wet your hands with clean, running water (warm or cold), turn off the tap, and apply soap. / Scrub your hands for at least 20 seconds. Need a timer? Hum the \"Happy Birthday\" song from beginning to end twice. / Rinse your hands well under clean, running water. / Washing hands with soap and water is the best way to get rid of germs in most situations.",
    "location": "CDC — About Handwashing"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Burnu sildikten, öksürdükten ya da hapşırdıktan sonra, yemek hazırlamadan önce ve sonra, tuvaletten sonra eller yıkanmalıdır; el yıkamak solunum ve ishal enfeksiyonlarının yayılmasını önleyebilir.",
    "numbers": [],
    "quote": "After blowing your nose, coughing, or sneezing / Before and after preparing food / After using the toilet / Washing hands can keep you healthy and prevent the spread of respiratory and diarrheal infections.",
    "location": "CDC — About Handwashing"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Hapşırırken ya da öksürürken ağzını ve burnunu mendille kapat ve mendili at; mendil yoksa eline değil dirseğine hapşır.",
    "numbers": [],
    "quote": "If you sneeze or cough, cover your mouth and nose with a tissue, and then throw it out. / If you don't have a tissue, sneeze or cough into your elbow, not your hands.",
    "location": "Nemours KidsHealth — Fighting Germs"
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
