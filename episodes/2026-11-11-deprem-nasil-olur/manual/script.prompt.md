# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Deprem nasıl olur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 7, "paperId": "topic:deprem-nasil-olur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Earthquakes",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/earthquakes/"
  },
  {
    "id": "k2",
    "title": "What causes earthquakes?",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/earthquakes/what-causes-earthquakes/"
  },
  {
    "id": "k3",
    "title": "How are earthquakes detected, located and measured?",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/earthquakes/how-are-earthquakes-detected/"
  },
  {
    "id": "k4",
    "title": "Earthquakes",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/earthquakes/"
  },
  {
    "id": "k5",
    "title": "The Science of Earthquakes",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/programs/earthquake-hazards/science-earthquakes"
  },
  {
    "id": "k6",
    "title": "Can you predict earthquakes?",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/faqs/can-you-predict-earthquakes"
  },
  {
    "id": "k7",
    "title": "What Is an Earthquake?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/earthquakes/en/"
  },
  {
    "id": "k8",
    "title": "Earthquakes",
    "publisher": "Ready.gov",
    "url": "https://www.ready.gov/kids/disaster-facts/earthquakes"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Deprem, yer kabuğunda biriken gerinim enerjisinin aniden serbest kalmasıdır.",
    "numbers": [],
    "quote": "An earthquake is the sudden release of strain energy in the Earth’s crust",
    "location": "British Geological Survey — Earthquakes"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Dünya'nın dört temel katmanı vardır: katı kabuk, sıcak ve neredeyse katı manto, sıvı dış çekirdek ve katı iç çekirdek.",
    "numbers": [],
    "quote": "a solid crust, a hot, nearly solid mantle, a liquid outer core and a solid inner core. / The earth has four major layers: the inner core, outer core, mantle and crust",
    "location": "NASA Space Place — What Is an Earthquake?; USGS — The Science of Earthquakes"
  },
  {
    "id": "f3",
    "kind": "number",
    "statement": "Dünya'nın en dış katmanı tektonik levha denen yaklaşık 15 büyük parçaya bölünmüştür; levhalar birbirine göre çok yavaş, tipik olarak yılda birkaç santimetre hareket eder.",
    "numbers": [
      "15"
    ],
    "quote": "The Earth’s outermost layer is fragmented into about 15 major slabs called tectonic plates. / Tectonic plates move very slowly relative to each other, typically a few centimetres per year",
    "location": "British Geological Survey — What causes earthquakes?"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Levhalar birbirine doğru hareket edebilir, birbirine sürtünerek kayabilir ya da birbirinden ayrılabilir.",
    "numbers": [],
    "quote": "Continental and oceanic plates may move toward each other, scrape past each other, or pull apart",
    "location": "National Geographic Education — Earthquakes"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Sürtünme kayaları yerinde tutar ve gerilim birikir; fayın iki yanındaki kayalar yavaş yavaş biçim değiştirir; blokları kaydıracak enerji depolanır.",
    "numbers": [],
    "quote": "Friction, however, holds the rocks in place, causing stresses to build. / Before an earthquake, the buildup of stress in the rocks on either side of a fault results in gradual deformation. / the energy that would normally cause the blocks to slide past one another is being stored up.",
    "location": "National Geographic Education — Earthquakes; British Geological Survey — What causes earthquakes?; USGS — The Science of Earthquakes"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Elastik geri sekme: kayalar özgün biçimine döner ama fayın iki yanında yer değiştirmiş olur.",
    "numbers": [],
    "quote": "return to their original shape (elastic rebound) but are offset on either side of the fault.",
    "location": "British Geological Survey — What causes earthquakes?"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Depremin başladığı noktaya odak ya da hiposantr denir ve kilometrelerce derinde olabilir; odağın tam üstündeki yüzey noktası merkez üssüdür.",
    "numbers": [],
    "quote": "The point where an earthquake starts is termed the focus or hypocentre and may be many kilometres deep within the earth. / The point at the surface directly above the focus is called the earthquake epicentre.",
    "location": "British Geological Survey — Earthquakes"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Enerji, gölcükteki halkalar gibi her yöne yayılır.",
    "numbers": [],
    "quote": "the energy spreads out in all directions like ripples on a pond.",
    "location": "British Geological Survey — Earthquakes"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "P dalgaları ilerleme yönü boyunca sıkışma ve genleşmelerden oluşur; S dalgalarının hareketi ilerleme yönüne diktir; P dalgaları S dalgalarından hızlıdır. Tipik yer kabuğunda P 5–7 km/s, S 3–4 km/s hızla ilerler.",
    "numbers": [
      "5",
      "7",
      "3",
      "4"
    ],
    "quote": "P-waves are longitudinal waves that consist of a series of compressions and dilations along the direction of travel. / S-waves are transverse waves, whose motion is perpendicular to the direction of travel. / P waves are also faster than S waves / VP 5–7 km/s in typical Earth’s crust / VS 3–4 km/s in typical Earth’s crust",
    "location": "British Geological Survey — How are earthquakes detected, located and measured?; USGS — The Science of Earthquakes"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "P dalgaları şimşek, S dalgaları gök gürültüsü gibidir; P'nin S'den hızlı olması depremin nerede olduğunu bulmayı sağlar.",
    "numbers": [],
    "quote": "P waves are like the lightning, and S waves are like the thunder. / P waves are also faster than S waves, and this fact is what allows us to tell where an earthquake was.",
    "location": "USGS — The Science of Earthquakes"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Sismograf ya da sismometre, sismogramı oluşturan ölçüm aletidir.",
    "numbers": [],
    "quote": "A seismograph or seismometer is the measuring instrument that creates the seismogram.",
    "location": "British Geological Survey — How are earthquakes detected, located and measured?"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Büyüklük ölçekleri logaritmiktir: büyüklükte bir birimlik artış, genlikte on katlık artışa karşılık gelir.",
    "numbers": [],
    "quote": "Earthquake magnitude scales are logarithmic, i.e. a one unit increase in magnitude corresponds to a tenfold increase in amplitude.",
    "location": "British Geological Survey — How are earthquakes detected, located and measured?"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Şiddet, depremin yol açtığı sarsıntının gücünün nitel ölçüsüdür ve normalde merkez üssünden uzaklaştıkça azalır; büyüklük ise uzaklıktan bağımsızdır.",
    "numbers": [],
    "quote": "Intensity is a qualitative measure of the strength of shaking caused by an earthquake / normally decreases with distance from the epicentre / is independent of distance from the epicentre.",
    "location": "British Geological Survey — How are earthquakes detected, located and measured?"
  },
  {
    "id": "f14",
    "kind": "number",
    "statement": "Dünya'da her gün yüzlerce deprem olur; ciddi hasar verebilecek büyüklükte olanlar yılda yaklaşık 100 tanedir.",
    "numbers": [
      "100"
    ],
    "quote": "Hundreds of earthquakes occur on Earth everyday. / There are around 100 earthquakes each year of a size that could cause serious damage.",
    "location": "National Geographic Education — Earthquakes; British Geological Survey — Earthquakes"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "Artçı sarsıntılar ana depremden sonra haftalarca, aylarca, hatta yıllarca sürebilir.",
    "numbers": [],
    "quote": "aftershocks can continue for weeks, months, and even years after the mainshock!",
    "location": "USGS — The Science of Earthquakes"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Ne USGS ne de başka bilim insanları bugüne kadar büyük bir depremi önceden bildi; bir tahminin tarih ve saati, yeri ve büyüklüğü belirtmesi gerekir. Bilim insanları belirli bir fayda gelecekte yeniden deprem olacağını bilir.",
    "numbers": [],
    "quote": "Neither the USGS nor any other scientists have ever predicted a major earthquake. / 1) the date and time, 2) the location, and 3) the magnitude. / On any particular fault, scientists know there will be another earthquake sometime in the future",
    "location": "USGS — Can you predict earthquakes?; USGS — The Science of Earthquakes"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Erken uyarı, deprem başladıktan sonra yapılan bir bildirimdir.",
    "numbers": [],
    "quote": "Early warning is a notification that is issued after an earthquake starts.",
    "location": "USGS — Can you predict earthquakes?"
  },
  {
    "id": "f18",
    "kind": "claim",
    "statement": "Deprem anında: yere çök, sağlam bir masanın altına gir, sarsıntı bitene kadar tutun; camlardan ve devrilebilecek eşyalardan uzak dur; dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.",
    "numbers": [],
    "quote": "DROP to the ground. / Take COVER under a sturdy table or other heavy furniture. / HOLD ON until the shaking stops. / STAY AWAY from windows, glass, lighting fixtures, or furniture that could fall, like bookcases. / Move away from buildings, streetlights, and wires.",
    "location": "Ready.gov Kids — Earthquakes"
  },
  {
    "id": "f19",
    "kind": "claim",
    "statement": "Hızla tahliye gerekirse ihtiyaç duyulacak eşyalarla bir acil durum çantası hazırlanmalıdır.",
    "numbers": [],
    "quote": "Build an emergency kit with items that you will need if you have to evacuate quickly.",
    "location": "Ready.gov Kids — Earthquakes"
  },
  {
    "id": "f20",
    "kind": "number",
    "statement": "Büyüklüğü 10 ya da daha fazla olan depremler olamaz.",
    "numbers": [
      "10"
    ],
    "quote": "No, earthquakes of magnitude 10 or larger cannot happen.",
    "location": "USGS — Can you predict earthquakes?"
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
