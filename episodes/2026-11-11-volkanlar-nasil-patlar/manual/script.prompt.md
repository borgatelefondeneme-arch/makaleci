# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Volkanlar nasıl patlar?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 5, "paperId": "topic:volkanlar-nasil-patlar".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Volcanoes",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/volcanoes/"
  },
  {
    "id": "k2",
    "title": "Types of volcano",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/volcanoes/how-volcanoes-form/"
  },
  {
    "id": "k3",
    "title": "Eruption styles",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/volcanoes/eruption-styles/"
  },
  {
    "id": "k4",
    "title": "Volcanic hazards",
    "publisher": "Britanya Jeoloji Araştırmaları Kurumu",
    "url": "https://www.bgs.ac.uk/discovering-geology/earth-hazards/volcanoes/volcanic-hazards/"
  },
  {
    "id": "k5",
    "title": "Volcanoes",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/volcanoes/"
  },
  {
    "id": "k6",
    "title": "About Volcanoes",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/programs/VHP/about-volcanoes"
  },
  {
    "id": "k7",
    "title": "Comprehensive monitoring provides timely warnings of volcano reawakening",
    "publisher": "USGS",
    "url": "https://www.usgs.gov/programs/VHP/comprehensive-monitoring-provides-timely-warnings-volcano-reawakening"
  },
  {
    "id": "k8",
    "title": "What Is a Volcano?",
    "publisher": "NASA",
    "url": "https://spaceplace.nasa.gov/volcanoes2/en/"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Volkanlar, lavın, tefranın (küçük kaya parçaları) ve buharın yeryüzüne püskürdüğü açıklıklardır.",
    "numbers": [],
    "quote": "Volcanoes are openings, or vents where lava, tephra (small rocks), and steam erupt onto the Earth's surface.",
    "location": "USGS — About Volcanoes"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Erimiş kaya yerin altındayken magma, yüzeye aktığında lav adını alır.",
    "numbers": [],
    "quote": "\"lava\" when it's on the surface, \"magma\" when it's underground / Once it flows onto the surface the magma is known as lava.",
    "location": "NASA Space Place — What Is a Volcano?; National Geographic Education — Volcanoes"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Magma yerin onlarca mil altında oluşur; çevresindeki katı kayadan hafiftir (daha az yoğundur) ve bu yüzden yükselir.",
    "numbers": [],
    "quote": "Originating many tens of miles beneath the ground, magma is lighter than surrounding solid rock. / Hot magma rises because it is less dense than the surrounding rock.",
    "location": "USGS — About Volcanoes; British Geological Survey — Types of volcano"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Etkin bir volkanın içinde magmanın toplandığı bir oda vardır; magma odasında basınç artar.",
    "numbers": [],
    "quote": "Inside an active volcano is a chamber in which molten rock, called magma, collects. / Pressure builds up inside the magma chamber, causing the magma to move through channels in the rock",
    "location": "National Geographic Education — Volcanoes"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Magma, tektonik levhalar birbirinden uzaklaşırken yükselebilir; levhalar birbirine doğru ilerlerken kabuğun bir kısmı derine itilir, ısı ve basınç kabuğu eritir ve magma olarak yükselir; üçüncü yol sıcak noktalardır. Hawaii volkanları bir sıcak noktanın üstünde oluşur.",
    "numbers": [],
    "quote": "Magma can rise when pieces of Earth's crust called tectonic plates slowly move away from each other. / When this happens, part of Earth's crust can be forced deep into its interior. / The high heat and pressure cause the crust to melt and rise as magma. / A final way that magma rises is over hot spots. / while Yellowstone and Hawaiian volcanoes form over a \"hot spot.\"",
    "location": "NASA Space Place — What Is a Volcano?; USGS — About Volcanoes"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Volkanların birçoğu Büyük Okyanus'un çevresinde, 'Ateş Çemberi' denen kuşakta yer alır.",
    "numbers": [],
    "quote": "Many of these are located around the Pacific Ocean in what is known as the \"Ring of Fire.\"",
    "location": "USGS — About Volcanoes"
  },
  {
    "id": "f7",
    "kind": "claim",
    "statement": "Magmada çok gaz hapsolursa basınç giderek artar; bu bir gazoz şişesine benzer: gaz sıvıda hapsolmuştur ve kaçmak ister.",
    "numbers": [],
    "quote": "If a lot of gas is trapped within magma, pressure will build and build / It's a bit like a bottle of fizzy pop: gas is trapped in the liquid but if you shake the bottle the gas wants to escape.",
    "location": "British Geological Survey — Eruption styles"
  },
  {
    "id": "f8",
    "kind": "claim",
    "statement": "Magmanın viskozitesi düşükse (akıcıysa) gaz kolayca kaçar; viskoz (yapışkan) magma yüzeye ulaştığında akamaz. Püskürmenin patlamalı mı efüzif mi olacağı büyük ölçüde magmadaki gaz miktarına bağlıdır.",
    "numbers": [],
    "quote": "If a magma has low viscosity (it is runny), gas can escape easily / When the magma is viscous (or sticky), it can't flow when it reaches the surface / Whether an eruption is explosive or effusive largely depends upon the amount of gas in the magma.",
    "location": "British Geological Survey — Eruption styles"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Kalkan volkanlar neredeyse tümüyle akıcı lav akıntılarından oluşur; eğimleri 10°'den azdır. Mauna Kea ve Mauna Loa kalkan volkandır.",
    "numbers": [
      "10"
    ],
    "quote": "Shield volcanoes are built almost entirely of fluid lava flows. / Shield volcanoes, on the other hand, have gentle slopes that are less than 10° / Mauna Kea and Mauna Loa are shield volcanoes.",
    "location": "USGS — About Volcanoes; British Geological Survey — Types of volcano"
  },
  {
    "id": "f10",
    "kind": "number",
    "statement": "Çok viskoz magmanın püskürmesi, eğimi yaklaşık 30–35° olan dik yamaçlı volkanlar oluşturur; bileşik volkanlara stratovolkan da denir; Fuji Dağı bir örnektir.",
    "numbers": [
      "30",
      "35"
    ],
    "quote": "tends to produce steep-sided volcanoes with slopes that are about 30–35° / Some of the Earth's grandest mountains are composite volcanoes—sometimes called stratovolcanoes. / Mount Fuji in Japan, Mount Cotopaxi in Ecuador, Mount Shasta in California",
    "location": "British Geological Survey — Types of volcano; USGS — About Volcanoes"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Cüruf konileri en basit volkan türüdür.",
    "numbers": [],
    "quote": "Cinder cones are the simplest type of volcano.",
    "location": "USGS — About Volcanoes"
  },
  {
    "id": "f12",
    "kind": "claim",
    "statement": "Kül, saç teli kalınlığında minik tefra parçalarıdır ve rüzgârla taşınabilir.",
    "numbers": [],
    "quote": "Ash, tiny pieces of tephra the thickness of a strand of hair, may be carried by the wind",
    "location": "USGS — About Volcanoes"
  },
  {
    "id": "f13",
    "kind": "number",
    "statement": "Bazalt lavlar tipik olarak 1100–1200°C sıcaklıkta püskürür.",
    "numbers": [
      "1100",
      "1200"
    ],
    "quote": "are typically erupted at temperatures of 1100–1200°C.",
    "location": "British Geological Survey — Volcanic hazards"
  },
  {
    "id": "f14",
    "kind": "number",
    "statement": "Piroklastik akışlar, kaya parçaları ile gaz karışımından oluşan sıcak yoğunluk akıntılarıdır; volkanın yamaçlarından tipik olarak saatte 110 kilometre ya da daha hızlı iner.",
    "numbers": [
      "110"
    ],
    "quote": "Pyroclastic flows are hot 'density currents' consisting of mixtures of rock debris and gas / They typically travel at 110 kilometres per hour or faster down the sides of the volcano.",
    "location": "British Geological Survey — Volcanic hazards"
  },
  {
    "id": "f15",
    "kind": "number",
    "statement": "Dünya'da 1500'den fazla etkin volkan vardır; her yıl yaklaşık 50–70 volkan püskürür.",
    "numbers": [
      "1500",
      "50",
      "70"
    ],
    "quote": "There are more than 1500 active volcanoes on Earth. / Around 50–70 volcanoes erupt every year.",
    "location": "British Geological Survey — Volcanoes"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Mauna Loa dünyanın en büyük etkin volkanıdır.",
    "numbers": [],
    "quote": "the world's largest active volcano, Mauna Loa",
    "location": "USGS — About Volcanoes"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "İzleme; depremler, yer hareketi ve volkanik gaz gibi birkaç tür gözlemi içermelidir; erken fark etmek insanlara hazırlanmak için en çok zamanı kazandırır.",
    "numbers": [],
    "quote": "monitoring should include several types of observations (earthquakes, ground movement, volcanic gas / Early detection gives the maximum amount of time for people to prepare for an eruption.",
    "location": "USGS — Comprehensive monitoring provides timely warnings of volcano reawakening"
  },
  {
    "id": "f18",
    "kind": "claim",
    "statement": "Lav genellikle yavaş aktığı için doğrudan can kaybına yol açması nadirdir.",
    "numbers": [],
    "quote": "In general, it is rare for lava to cause the direct loss of life, because it usually flows slowly",
    "location": "British Geological Survey — Volcanic hazards"
  },
  {
    "id": "f19",
    "kind": "claim",
    "statement": "Surtsey püskürmesi yeni bir ada oluşturdu.",
    "numbers": [],
    "quote": "This eruption formed a new island.",
    "location": "British Geological Survey — Eruption styles"
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
