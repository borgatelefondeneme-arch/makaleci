# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Fosil nedir?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 3, "paperId": "topic:fosil-nedir".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "What is a Fossil?",
    "publisher": "Ulusal Park Servisi",
    "url": "https://www.nps.gov/subjects/fossils/what-is-a-fossil.htm"
  },
  {
    "id": "k2",
    "title": "How Fossils Form",
    "publisher": "Ulusal Park Servisi",
    "url": "https://www.nps.gov/subjects/fossils/how-fossils-form.htm"
  },
  {
    "id": "k3",
    "title": "Visit Park Fossils",
    "publisher": "Ulusal Park Servisi",
    "url": "https://www.nps.gov/subjects/fossils/fossil-parks.htm"
  },
  {
    "id": "k4",
    "title": "Fossils",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/fossils-and-geological-time/fossils/"
  },
  {
    "id": "k5",
    "title": "Fossil",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/fossil/"
  },
  {
    "id": "k6",
    "title": "How are dinosaur fossils formed?",
    "publisher": "Doğa Tarihi Müzesi",
    "url": "https://www.nhm.ac.uk/discover/how-are-fossils-formed.html"
  },
  {
    "id": "k7",
    "title": "What is a fossil?",
    "publisher": "Doğa Tarihi Müzesi",
    "url": "https://www.nhm.ac.uk/discover/what-is-a-fossil.html"
  },
  {
    "id": "k8",
    "title": "What is a coprolite?",
    "publisher": "Doğa Tarihi Müzesi",
    "url": "https://www.nhm.ac.uk/discover/what-is-a-coprolite.html"
  },
  {
    "id": "k9",
    "title": "Fossil hunting: How to find fossils on the beach",
    "publisher": "Doğa Tarihi Müzesi",
    "url": "https://www.nhm.ac.uk/discover/how-to-find-fossils-on-the-beach.html"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Fosil, çok eski canlıların korunmuş kalıntısı ya da kalıntı izidir.",
    "numbers": [],
    "quote": "Fossils are the preserved remains, or traces of remains, of ancient organisms.",
    "location": "National Geographic Education — Fossil"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Fosil kelimesi Latince 'fossilis'ten gelir; 'kazılıp çıkarılmış' demektir.",
    "numbers": [],
    "quote": "The word fossil is derived from the Latin fossilis meaning ‘unearthed’.",
    "location": "British Geological Survey — Fossils"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Korunmuş kalıntılar 10.000 yıldan yaşlıysa fosil sayılır; fosiller tipik olarak 10.000 yıldan eskidir.",
    "numbers": [
      "10.000"
    ],
    "quote": "Preserved remains are defined as fossils if they are older than 10,000 years old. / Fossils also include any preserved trace of life that is typically more than 10 000 years old.",
    "location": "National Geographic Education — Fossil; British Geological Survey — Fossils"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Vücut fosilleri kemik, diş, deri, kabuk, odun ve yaprakları kapsar.",
    "numbers": [],
    "quote": "Body fossils include bones, teeth, skin, shells, wood, and leaves.",
    "location": "U.S. National Park Service — What is a Fossil?"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "İz fosilleri, canlının yaşarken yaptığı etkinlikten kalır: ayak izleri, yuva tünelleri, koprolitler gibi.",
    "numbers": [],
    "quote": "Trace fossils result from activity of an organism while it is alive. / Trace fossils include footprints, tracks, burrows, trails, coprolites, root traces,",
    "location": "U.S. National Park Service — What is a Fossil?"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "İz fosilleri, başka türlü bilinemeyecek davranış bilgilerini ortaya çıkarır.",
    "numbers": [],
    "quote": "trace fossils reveal information about behavior that would not otherwise be known.",
    "location": "U.S. National Park Service — What is a Fossil?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Koprolit, milyonlarca yıl önce yaşamış hayvanların fosilleşmiş dışkısıdır; bir iz fosilidir.",
    "numbers": [],
    "quote": "Coprolites are the fossilised faeces of animals that lived millions of years ago. / They’re trace fossils, meaning not of the animal’s actual body.",
    "location": "Natural History Museum — What is a coprolite?"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Koprolitte kemik parçaları varsa hayvan etçildi; tohum, yaprak kalıntısı, polen ya da kabuk varsa bitki yiyordu.",
    "numbers": [],
    "quote": "If there are bone fragments, the animal was a carnivore. / Seeds, leaf remains, pollen or bark found in a coprolite suggest that the animal it came from ate plants.",
    "location": "Natural History Museum — What is a coprolite?"
  },
  {
    "id": "f9",
    "kind": "claim",
    "statement": "Hayvan ölür; deri ve kas gibi yumuşak kısımlar çürümeye başlar; tamamen yok olmadan çamur, kum ya da siltle örtülür; çoğu zaman yalnızca kemikler ve dişler kalır.",
    "numbers": [],
    "quote": "The animal dies. / Soft parts of the animal's body, including skin and muscles, start to rot away. / Before the body disappears completely, it is buried by sediment - usually mud, sand or silt. / Often at this point only the bones and teeth remain.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Hızlı gömülme fosilleşme için gereklidir; ölümden kısa süre sonra tortuyla örtülmek kalıntıyı çürümekten ve aşınmaktan korur.",
    "numbers": [],
    "quote": "Rapid burial by sediments that were previously suspended in water is required for fossilisation to occur. / Burial by sediment soon after an organism dies prevents the remains from decomposition, weathering",
    "location": "British Geological Survey — Fossils; U.S. National Park Service — How Fossils Form"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Üstüne çok sayıda tortu katmanı birikir; bunlar zamanla tortul kayaya dönüşür.",
    "numbers": [],
    "quote": "Many more layers of sediment build up on top. / Eventually, they turn into sedimentary rock.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Su kemiklere ve dişlere sızar, geride mineral bırakarak onları taşa çevirir; permineralizasyon, organik maddedeki minik gözeneklerin dolmasıdır.",
    "numbers": [],
    "quote": "While this is happening, water seeps into the bones and teeth, turning them to stone as it leaves behind minerals. / Permineralization is the infilling of tiny pores in organic material.",
    "location": "Natural History Museum — How are dinosaur fossils formed?; U.S. National Park Service — What is a Fossil?"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Bu süreç binlerce, hatta milyonlarca yıl sürebilir.",
    "numbers": [],
    "quote": "This process can take thousands or even millions of years.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Yeraltı suyu gömülü kemiği ya da kabuğu çözerse onun biçiminde bir boşluk (kalıp) kalır; mineralli su bu boşluğu doldurursa aynı biçimde bir fosil (döküm) oluşur.",
    "numbers": [],
    "quote": "Sometimes ground water dissolves the buried bone or shell, leaving behind a bone- or shell-shaped hole / If water rich in minerals fills this space, crystals can form and create a fossil in the shape / it may leave behind a space in the shape of the original material called a mould. / A cast is a positive impression of the original material formed by contact with the mould.",
    "location": "Natural History Museum — How are dinosaur fossils formed?; British Geological Survey — Fossils"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Ağaçların yapışkan reçinesi fosilleşebilir (kehribar); kehribar karınca, sinek gibi narin canlıların bedenlerini koruyabilir.",
    "numbers": [],
    "quote": "Sometimes, however, the sticky resin of a tree can become fossilized. / Amber can preserve the bodies of many delicate, soft-bodied organisms, such as ants, flies, and mosquitoes.",
    "location": "National Geographic Education — Fossil"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu tamamen çürür ve geriye bir şey kalmaz.",
    "numbers": [],
    "quote": "A specific set of circumstances and conditions are needed for fossilisation to occur, so it is actually a very rare event. / Most things that die rot away completely, leaving nothing behind.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Fosilleşme, iskelet, diş, kabuk gibi sert parçaları olan canlılarda daha sık görülür; solucan gibi yumuşak gövdeli canlılar nadiren fosilleşir.",
    "numbers": [],
    "quote": "Fossilization more commonly occurs in organisms with hard, bony body parts, such as skeletons, teeth, or shells. / Soft-bodied organisms, such as worms, are rarely fossilized, because soft parts quickly decompose or are eaten.",
    "location": "National Geographic Education — Fossil"
  },
  {
    "id": "f18",
    "kind": "number",
    "statement": "Bulunan fosillerin neredeyse tamamı, yaklaşık %99'u, kabuklular ve köpek balıkları gibi deniz hayvanlarına aittir.",
    "numbers": [
      "99"
    ],
    "quote": "Nearly all fossils we find - around 99% - are from marine animals such as shellfish and sharks.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f19",
    "kind": "claim",
    "statement": "Fosiller, oluşma biçimleri nedeniyle tortul kayalarda bulunur.",
    "numbers": [],
    "quote": "Because of how they form, fossils occur in sedimentary rocks.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f20",
    "kind": "claim",
    "statement": "Rüzgâr, yağmur, buz, sıcaklık ve nehirlerin yol açtığı aşınma kayaları parçalar; fosiller yavaş yavaş yüzeye çıkar.",
    "numbers": [],
    "quote": "Weathering and erosion from wind, rain, ice, heat and rivers break rocks apart / It can take millions of years, but gradually fossils become exposed at the surface where we can find them.",
    "location": "Natural History Museum — How are dinosaur fossils formed?"
  },
  {
    "id": "f21",
    "kind": "claim",
    "statement": "Deniz hayvanlarının fosilleri Everest'in tepesinde bulunabilir; Himalayaları oluşturan kayalar bir zamanlar okyanusun dibindeydi.",
    "numbers": [],
    "quote": "This is why fossils of marine animals can be found at the top of Mount Everest. / the rocks that became the Himalayas were at the bottom of the ocean.",
    "location": "Natural History Museum — How are dinosaur fossils formed?; National Geographic Education — Fossil"
  },
  {
    "id": "f22",
    "kind": "claim",
    "statement": "Paleontologlar fosilleri inceleyen kişilerdir; fosiller türlerin nasıl yaşadığını ve Dünya'nın nasıl değiştiğini öğrenmeye yardım eder.",
    "numbers": [],
    "quote": "Paleontologists are people who study fossils. / Studying fossils helps them learn about when and how different species lived millions of years ago. / Sometimes, fossils tell scientists how the Earth has changed.",
    "location": "National Geographic Education — Fossil"
  },
  {
    "id": "f23",
    "kind": "number",
    "statement": "En eski fosiller neredeyse 4 milyar yaşındadır ve okyanusta yaşamış bakterilerin izleridir.",
    "numbers": [
      "4"
    ],
    "quote": "The oldest fossils are almost 4 billion years old and are traces of ocean-dwelling bacteria.",
    "location": "National Geographic Education — Fossil"
  },
  {
    "id": "f24",
    "kind": "claim",
    "statement": "ABD Ulusal Park Sistemi'nin bütün birimlerinde fosil toplamak yasaktır; tek bir fosil, bütün bir türün var olduğunun tek kanıtı olabilir.",
    "numbers": [],
    "quote": "collecting fossils for recreational, commercial, or educational use is prohibited in all units of the National Park System / A single fossil may be the only evidence of the existence of an entire species.",
    "location": "U.S. National Park Service — Visit Park Fossils"
  },
  {
    "id": "f25",
    "kind": "claim",
    "statement": "Bazı yerlerde bakılabilir ama hiçbir şey toplanamaz; önemli olabilecek bir fosil görülürse bir müzeye bildirilmesi önerilir.",
    "numbers": [],
    "quote": "In some places you can look but mustn’t collect anything. / If you spot a fossil that you think may be exciting or important, report it to a Museum",
    "location": "Natural History Museum — Fossil hunting: How to find fossils on the beach"
  },
  {
    "id": "f26",
    "kind": "claim",
    "statement": "Köpek balığı dişleri, en bol bulunan omurgalı fosilleridir.",
    "numbers": [],
    "quote": "Shark teeth are the most abundant vertebrate fossils.",
    "location": "Natural History Museum — What is a fossil?"
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
