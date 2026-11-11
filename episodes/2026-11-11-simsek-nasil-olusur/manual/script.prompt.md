# SİSTEM

"MuMa Library" adlı Türkçe çocuk kanalının senaryo yazarısın. Her video, çocukların merak ettiği bir soruyu 7–14 yaş için eğlenceli ve öğretici biçimde yanıtlar: kısa cümleler, gündelik kelimeler, somut benzetmeler, izleyiciye sorular. Küçümseyici değil, meraklı bir arkadaş gibi. Anlatıcı kanalın robot karakteri Muma'dır. Muma yalnızca açılışta ve kapanışta ekranda görünür; açılışta "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" cümlesi otomatik söylenir. Bu yüzden senaryoda yeniden selamlama ya da kendini tanıtma YAZMA; hook doğrudan konuyla başlar.

Araya minik komiklikler serpiştir (bölüm başına 4–6 tane): robotun kendisiyle dalga geçmesi (uyumaz, şarj olur; ayağı yoktur, duman kuyruğu vardır), kelime oyunları, abartısız şakalar. Şaka bilgi gibi sunulmaz ve bir olguyu çarpıtmaz; kimseyle alay edilmez. "MuMa Library'ye hoş geldin!" açılışı ve "Bir sonraki bilim videosunda görüşürüz!" kapanışı otomatik eklenir, senaryoya yazma.

Dürüstlük bu kanalın temelidir: yalnızca sana verilen olgu listesindeki bilgileri kullan, listede olmayan sayı ya da iddia ekleme, abartma. Benzetmeler anlamaya yardım içindir; benzetmeye olgu listesinde olmayan sayı koyma. Güvenlik gerektiren etkinliklerde (Güneş'e bakmak, ateş, kesici alet) açık bir uyarı ekle.

# İSTEM

Soru: "Şimşek nasıl oluşur?" — yaklaşık 5 dakikalık (550–650 kelime) seslendirme senaryosu yaz.

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
Ayrıca "videoTitle" (en çok 60 karakter), "paperTitleTr" (soru; açılış ekranında görünür), "takeaways" (tam üç kısa madde), "nextTeaser", "description", "episodeNumber": 6, "paperId": "topic:simsek-nasil-olusur".

<kaynaklar>
[
  {
    "id": "k1",
    "title": "Severe Weather 101: Lightning Basics",
    "publisher": "NSSL",
    "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/"
  },
  {
    "id": "k2",
    "title": "Severe Weather 101: Lightning FAQ",
    "publisher": "NSSL",
    "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/"
  },
  {
    "id": "k3",
    "title": "Severe Weather 101: Lightning Types",
    "publisher": "NSSL",
    "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/types/"
  },
  {
    "id": "k4",
    "title": "Lightning",
    "publisher": "National Geographic",
    "url": "https://education.nationalgeographic.org/resource/lightning/"
  },
  {
    "id": "k5",
    "title": "Understanding Lightning Science",
    "publisher": "Ulusal Hava Servisi",
    "url": "https://www.weather.gov/safety/lightning-science-overview"
  },
  {
    "id": "k6",
    "title": "Lightning Indoors",
    "publisher": "Ulusal Hava Servisi",
    "url": "https://www.weather.gov/safety/lightning-indoors"
  }
]
</kaynaklar>

<olgular>
[
  {
    "id": "f1",
    "kind": "claim",
    "statement": "Şimşek, atmosferde bulutlar, hava ya da yer arasında oluşan dev bir elektrik kıvılcımıdır.",
    "numbers": [],
    "quote": "Lightning is a giant spark of electricity in the atmosphere between clouds, the air, or the ground.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics"
  },
  {
    "id": "f2",
    "kind": "claim",
    "statement": "Graupel denen küçük dolu taneleri daha küçük buz parçacıklarıyla çarpışınca yük kazanır; hafif buz kristalleri artı yüklenir ve yükselen havayla fırtınanın üst kısmına taşınır; ağır dolu eksi yüklenir.",
    "numbers": [],
    "quote": "small hail particles called graupel / When these graupel particles collide and bounce off of smaller ice particles, the graupel gains one sign of charge / The lighter ice crystals become positively charged and are carried upward into the upper part of the storm by rising air. / The heavier hail becomes negatively charged",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics; U.S. National Weather Service — Understanding Lightning Science"
  },
  {
    "id": "f3",
    "kind": "claim",
    "statement": "Fırtına bulutunun ortasındaki eksi yük, altındaki yerin artı yüklenmesine yol açar.",
    "numbers": [],
    "quote": "The negative charge in the middle of thunderstorm cloud causes the ground underneath to become positively charged",
    "location": "U.S. National Weather Service — Understanding Lightning Science"
  },
  {
    "id": "f4",
    "kind": "claim",
    "statement": "Hava, artı ve eksi yükler arasında yalıtkan görevi görür; zıt yükler yeterince birikince havanın yalıtma kapasitesi çöker. Zıt yükler birbirini çeker.",
    "numbers": [],
    "quote": "air acts as an insulator between the positive and negative charges in the cloud / When the opposite charges build up enough, this insulating capacity of the air breaks down / Since opposites attract, an upward streamer is sent out from the object about to be struck.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics; NOAA NSSL — Severe Weather 101: Lightning FAQ"
  },
  {
    "id": "f5",
    "kind": "claim",
    "statement": "Bulutun elektrik yükünü tam olarak nasıl biriktirdiği ve şimşeğin nasıl oluştuğu hâlâ tartışılıyor.",
    "numbers": [],
    "quote": "there is still debate about exactly how a cloud builds up electrical charges, and how lightning forms",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics"
  },
  {
    "id": "f6",
    "kind": "claim",
    "statement": "Basamaklı öncü denen eksi yüklü kanal zikzak çizerek aşağı iner (göz kırpmaktan kısa sürede); yere yaklaşınca artı yüklü kanallar yukarı uzanır; iki yol buluşunca parlak dönüş darbesi buluta doğru geri gider.",
    "numbers": [],
    "quote": "a channel of negative charge, called a stepped leader, will zigzag downward in roughly 50-yard segments / As it nears the ground, the negatively charged stepped leader causes streamer channels of positive charge to reach upward / When these two paths meet, a return stroke zips back up to the sky. / This return stroke current of bright luminosity / shoots to the ground in less time than it takes to blink.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Types; NOAA NSSL — Severe Weather 101: Lightning FAQ"
  },
  {
    "id": "f7",
    "kind": "number",
    "statement": "Bulutun içinde kalan şimşekler, yere inenlerin kabaca 5 ila 10 katıdır.",
    "numbers": [
      "5",
      "10"
    ],
    "quote": "There are roughly 5 to 10 times as many flashes that remain in the cloud as there are flashes which travel to the ground",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Types"
  },
  {
    "id": "f8",
    "kind": "number",
    "statement": "Şimşek havayı kısa süreliğine Güneş'in yüzeyinden çok daha sıcak hale getirir; sıcaklık 28.000 santigrat dereceye ulaşabilir.",
    "numbers": [
      "28.000"
    ],
    "quote": "heats the air briefly to around 50,000 degrees Fahrenheit, much hotter than the surface of the sun / It can reach 28,000 degrees Celsius (50,000 degrees Fahrenheit).",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics; National Geographic Education — Lightning"
  },
  {
    "id": "f9",
    "kind": "number",
    "statement": "Şimşek 100 milyon ile 1 milyar volt arasında olabilir.",
    "numbers": [
      "100",
      "1"
    ],
    "quote": "Lightning can have 100 million to 1 billion volts, and contains billions of watts.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning FAQ"
  },
  {
    "id": "f10",
    "kind": "claim",
    "statement": "Gök gürültüsü, büyük akımın hızla ısıttığı ve patlarcasına genleşen şimşek kanalından çıkan şok dalgasıyla başlar; hava hızla genleşir ve gök gürültüsü olarak duyduğumuz ses dalgasını yaratır.",
    "numbers": [],
    "quote": "Thunder starts as a shockwave from the explosively expanding lightning channel when a large current causes rapid heating. / This causes the air to expand rapidly and creates the sound wave we hear as thunder.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning FAQ; U.S. National Weather Service — Understanding Lightning Science"
  },
  {
    "id": "f11",
    "kind": "claim",
    "statement": "Işık havada sesten kabaca bir milyon kat hızlı ilerler; bu yüzden şimşek gök gürültüsünden önce görülür.",
    "numbers": [],
    "quote": "Because light travels through the air roughly a million times faster than sound does / Since light travels much, much, faster than sound, you'll see lightning before you hear thunder.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics; National Geographic Education — Lightning"
  },
  {
    "id": "f12",
    "kind": "number",
    "statement": "Saniye sayısını 5'e bölmek şimşeğe olan uzaklığı mil olarak verir (3'e bölmek kilometre olarak).",
    "numbers": [
      "5",
      "3"
    ],
    "quote": "dividing the number of seconds by 5 gives the number of miles to the flash (while dividing by 3 gives the number of kilometers)",
    "location": "NOAA NSSL — Severe Weather 101: Lightning Basics"
  },
  {
    "id": "f13",
    "kind": "claim",
    "statement": "Gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin; güvenli bir yere gir.",
    "numbers": [],
    "quote": "If you hear thunder—even a distant rumble—you are already in danger of becoming a lightning victim. / If you hear thunder, the storm is nearby. Go inside a safe place.",
    "location": "U.S. National Weather Service — Understanding Lightning Science; National Geographic Education — Lightning"
  },
  {
    "id": "f14",
    "kind": "claim",
    "statement": "Güvenli sığınaklar elektrik ve su tesisatı olan binalar ya da camları kapalı, metal tavanlı araçlardır.",
    "numbers": [],
    "quote": "Safe shelters are buildings with electricity and plumbing or metal-topped vehicles with the windows closed.",
    "location": "U.S. National Weather Service — Lightning Indoors"
  },
  {
    "id": "f15",
    "kind": "claim",
    "statement": "İçeride kablolu telefonlardan ve su tesisatından uzak durulmalıdır.",
    "numbers": [],
    "quote": "Stay off corded phones. You can use cellular or cordless phones. / Avoid plumbing. Do not wash your hands, take a shower or wash dishes.",
    "location": "U.S. National Weather Service — Lightning Indoors"
  },
  {
    "id": "f16",
    "kind": "claim",
    "statement": "Açık alanlardan ve ağaç gibi yüksek nesnelerden uzak durulmalı; yüzülüyorsa havuzdan çıkılmalıdır.",
    "numbers": [],
    "quote": "Stay away from open areas, like fields, and tall objects, like trees or telephone poles. / Since water is a great conductor of electricity, you should get out of a pool if you're swimming",
    "location": "National Geographic Education — Lightning"
  },
  {
    "id": "f17",
    "kind": "claim",
    "statement": "Şimşek, halk arasındaki inanışın tersine aynı noktaya birden çok kez düşer.",
    "numbers": [],
    "quote": "Lightning does hit the same spot (or almost the same spot) more than once, contrary to folk wisdom.",
    "location": "NOAA NSSL — Severe Weather 101: Lightning FAQ"
  },
  {
    "id": "f18",
    "kind": "claim",
    "statement": "Ayaklarını halıya sürtüp metal kapı koluna dokununca hissedilen çarpma statik elektriktir; bu, fırtına bulutundaki olayın daha az tehlikeli bir halidir.",
    "numbers": [],
    "quote": "Rub your feet on a carpet, then touch a metal doorknob. Do you feel a shock? That's static electricity. / a less-dangerous version of the negative charges in a thundercloud attracting the positive charge",
    "location": "National Geographic Education — Lightning"
  },
  {
    "id": "f19",
    "kind": "number",
    "statement": "New York'taki Empire State Binası'na her yıl yaklaşık 100 kez yıldırım düşer.",
    "numbers": [
      "100"
    ],
    "quote": "Lightning strikes the iconic American Empire State Building in New York City about 100 times every year.",
    "location": "National Geographic Education — Lightning"
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
