# SİSTEM

Bir animasyon yönetmenisin. Hazır bir seslendirme senaryosunu, önceden tanımlı sahne tiplerinden oluşan bir sahne planına bölüyorsun. Sahneler React bileşenleriyle çizilir; sen yalnızca parametreleri verirsin. Makaledeki şekiller kullanılmaz, tüm grafikler olgu listesindeki sayılardan çizilir.

# İSTEM

Senaryoyu 12–20 sahneye böl. Her satır tam olarak bir sahnede, sıra bozulmadan yer almalı.

Sahne alanları:
- "id": "s1", "s2", ...; "section": satırların bölümü; "lineIds": bu sahnede seslendirilen satırlar (1–5 satır; sahne 8–30 saniye sürmeli).
- "factIds": sahnedeki görselin dayandığı olgular. Görselde rakamla yazılan her sayı bu olguların "numbers" listesinde bulunmalı.
- "sourceNote": sayı içeren sahnelerde kısa dipnot (ör. "Özet", "Bulgular bölümü").
- "visual": aşağıdaki tiplerden biri. Aynı tip art arda gelmesin; en az beş farklı tip kullan.
  - "hook": açılış sorusu { question, emoji? } — ilk sahne.
  - "source-card": künye kartı — yalnızca makale bölümlerinde; konu bölümlerinde KULLANMA (kaynaklar cümle içinde anılır).
  - "big-number": tek çarpıcı sayı { value, unit?, label, sub? }. "value" makaledeki yazımla.
  - "bar-chart": 2–6 çubuk { title, unit?, bars: [{ label, value (sayı), display (ekranda yazılacak hali), highlight? }] }.
  - "line-chart": zaman/sıra içinde değişim { title, xLabel, yLabel, points: [...] }.
  - "comparison": iki şeyin yan yana kıyası { title, left: { title, value?, items[] }, right: {...} }.
  - "diagram": 2–5 adımlı süreç { title, layout: "flow" | "cycle", nodes: [{ label, emoji? }] } — yöntem anlatımı için ideal.
  - "analogy": benzetme { template: "scale" (alan kıyası) | "fill" (dolan kap) | "race" (yarış) | "zoom" (iç içe ölçek), title, a: { label, value, display? }, b: {...}, caption }. Benzetmede makalede olmayan sayı gösterme; "display" boş bırakılırsa sayı yazılmaz, yalnızca oran çizilir.
  - "quote-card": makaleden kısa alıntı { quote (Türkçe çeviri, en çok iki cümle), attribution }.
  - "bullets": 1–4 madde { title, items[], tone?: "neutral" | "caution" } — sınırlılıklar için "caution".
  - "song": kapanış şarkısı (senaryoda "song" varsa zorunlu) — sondan bir önceki sahne; yalnızca şarkıya davet eden satırı içerir. Zerre/Muma bu sahnede sağda ve büyük durur (x≈0,86, y≈0,52, scale≈1,3, state "talk").
  - "clock": dönen gün-gece kadranı { title, center, markers: [{ at (0–24, yalnızca konum), label, emoji? }], note? } — günlük döngüler için; saat rakamı yazılmaz.
  - "spotlight": ortada büyük simge, çevresinde cümlelerle beliren etiketler { title, emoji, chips: [{ label, emoji? }] }.
  - "stages": sahne boyunca çizilen evre çizgisi { title, rows: [{ label, emoji? }], path: [satır indeksleri], highlightRow?, note } — evreler/aşamalar arasında gidip gelmeyi göstermek için; şematiktir.
  - "meter": dolup boşalan depo { title, label, emoji?, phases: [{ label, level (0–1), emoji? }], note } — biriken/azalan şeyler için.
HAREKET KURALI: hiçbir sahne durağan kalmamalı. Sahne en çok 3 satır sürer; her satırda ekranda yeni bir şey belirmeli. Mümkün olan her yerde yukarıdaki hareketli tipleri kullan; "bullets" ve "quote-card" üst üste gelmesin. Her sahneye "stickers" (konuyla ilgili 2–4 emoji) ve "keywords" (lineIds ile aynı sırada, satır başına büyük harfli 1–3 kelimelik anahtar ifade; gerekmiyorsa boş dize) ver.
  - "outro": kapanış — son sahne, summary bölümünün tüm satırlarını kapsar.
- "mascot": karakter Zerre'nin bu sahnedeki hali { state: "idle" | "talk" | "point" | "think", x, y (0–1, ekran oranı, merkez), scale (0,5–1,6), pointAt? }.
  NOT: Muma yalnızca açılışta ve kapanışta görünür; ara sahnelerdeki "mascot" değerleri kullanılmaz (şema gereği yine de doldur), yalnızca son sahneninki (outro) geçerlidir.
  İçerik sol-ortadadır; Zerre genelde sağda durur (x≈0,86, y≈0,62, scale≈1). Geniş sahnelerde (bar-chart, line-chart, diagram, analogy, comparison) küçülüp köşeye çekilsin (x≈0,9, y≈0,72, scale≈0,7). "hook" sahnesinde solda ve büyük (x≈0,17, y≈0,5, scale≈1,6, state "think"). Bir sayıya ya da grafiğe dikkat çekerken "point" kullan ve "pointAt" ile hedefi ver. Sahneden sahneye konum ve boyut değişsin ki karakter ekranda gezsin.

<senaryo>
[
  {
    "id": "hook",
    "lines": [
      {
        "id": "l1",
        "display": "Dizini sıyırdığında kırmızı bir damla belirir. Birkaç gün sonra da yerinde bir kabuk oluşur. Bu kırmızı sıvı ne, ve o kabuğu kim yaptı?",
        "spoken": "Dizini sıyırdığında kırmızı bir damla belirir. Birkaç gün sonra da yerinde bir kabuk oluşur. Bu kırmızı sıvı ne, ve o kabuğu kim yaptı?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l2",
        "display": "Kan, vücudunda hiç durmadan dolaşan bir taşıma ağıdır.",
        "spoken": "Kan, vücudunda hiç durmadan dolaşan bir taşıma ağıdır.",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün minicik olup bir kan damarının içinde yolculuğa çıkıyoruz!",
        "spoken": "Bugün minicik olup bir kan damarının içinde yolculuğa çıkıyoruz!",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kan neyden oluşur? Hangi hücre ne iş yapar? Ve kan nerede üretilir?",
        "spoken": "Üç sorumuz var. Kan neyden oluşur? Hangi hücre ne iş yapar? Ve kan nerede üretilir?",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum.",
        "spoken": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum.",
        "factIds": []
      }
    ]
  },
  {
    "id": "method",
    "lines": [
      {
        "id": "l6",
        "display": "KidsHealth'e göre kanın görevi, oksijeni ve besinleri vücudunun her yerine götürmektir. Böylece her bölüm çalışmaya devam eder.",
        "spoken": "Kids Helt'e göre kanın görevi, oksijeni ve besinleri vücudunun her yerine götürmektir. Böylece her bölüm çalışmaya devam eder.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l7",
        "display": "Kan dönüşte karbondioksiti ve diğer atıkları akciğerlere, böbreklere ve sindirim sistemine taşır.",
        "spoken": "Kan dönüşte karbondioksiti ve diğer atıkları akciğerlere, böbreklere ve sindirim sistemine taşır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l8",
        "display": "Benim damarlarımda kan yok, kablo var. Ben de elektrik taşırım, ama kabuk bağlamam!",
        "spoken": "Benim damarlarımda kan yok, kablo var. Ben de elektrik taşırım, ama kabuk bağlamam!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Amerikan Hematoloji Derneği'ne göre kanın dört ana bileşeni var: plazma, alyuvarlar, akyuvarlar ve trombositler.",
        "spoken": "Amerikan Hematoloji Derneği'ne göre kanın dört ana bileşeni var: plazma, alyuvarlar, akyuvarlar ve trombositler.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l10",
        "display": "Kan yaklaşık yüzde 55 plazma ve yüzde 45 kan hücresinden oluşur.",
        "spoken": "Kan yaklaşık yüzde elli beş plazma ve yüzde kırk beş kan hücresinden oluşur.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Plazma sarımsı bir sıvıdır. İçinde besinler, proteinler, hormonlar ve atık maddeler taşır.",
        "spoken": "Plazma sarımsı bir sıvıdır. İçinde besinler, proteinler, hormonlar ve atık maddeler taşır.",
        "factIds": [
          "f2"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Kana kırmızı rengini veren alyuvarlardır. Alyuvarların içinde hemoglobin denen, oksijen taşıyan bir protein vardır.",
        "spoken": "Kana kırmızı rengini veren alyuvarlardır. Alyuvarların içinde hemoglobin denen, oksijen taşıyan bir protein vardır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Hemoglobin akciğerlerde oksijeni yakalayınca kan parlak kırmızı olur. Sonra alyuvarlar bu oksijeni dokulara ve organlara götürür.",
        "spoken": "Hemoglobin akciğerlerde oksijeni yakalayınca kan parlak kırmızı olur. Sonra alyuvarlar bu oksijeni dokulara ve organlara götürür.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Alyuvar, ortası basık bir disk gibidir; iki yüzü de içe doğru çöküktür.",
        "spoken": "Alyuvar, ortası basık bir disk gibidir; iki yüzü de içe doğru çöküktür.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "MedlinePlus'a göre bir alyuvar yaklaşık 120 gün yaşar.",
        "spoken": "Medlayn Plas'a göre bir alyuvar yaklaşık yüz yirmi gün yaşar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Benim pilim yüz yirmi gün dayansaydı, ne güzel olurdu!",
        "spoken": "Benim pilim yüz yirmi gün dayansaydı, ne güzel olurdu!",
        "factIds": []
      },
      {
        "id": "l17",
        "display": "Akyuvarlar vücudun savunma ekibidir. Farklı türdeki akyuvarlar bakteri ve virüs gibi mikroplarla savaşır.",
        "spoken": "Akyuvarlar vücudun savunma ekibidir. Farklı türdeki akyuvarlar bakteri ve virüs gibi mikroplarla savaşır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Trombositler ise minik tamircilerdir. Bir kan damarı yırtılınca o bölgede toplanır ve sızıntıyı kapatmaya yardım ederler.",
        "spoken": "Trombositler ise minik tamircilerdir. Bir kan damarı yırtılınca o bölgede toplanır ve sızıntıyı kapatmaya yardım ederler.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Buna pıhtılaşma denir. Dizindeki o kabuk da pıhtılaşmanın bir parçasıdır.",
        "spoken": "Buna pıhtılaşma denir. Dizindeki o kabuk da pıhtılaşmanın bir parçasıdır.",
        "factIds": [
          "f8"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l20",
        "display": "Peki bu hücreler nerede üretilir? Kemiklerinin içindeki süngerimsi madde olan kemik iliğinde!",
        "spoken": "Peki bu hücreler nerede üretilir? Kemiklerinin içindeki süngerimsi madde olan kemik iliğinde!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Kemik iliği sürekli yeni kan hücreleri yapar. Böylece eskiyen hücrelerin yerine yenileri gelir.",
        "spoken": "Kemik iliği sürekli yeni kan hücreleri yapar. Böylece eskiyen hücrelerin yerine yenileri gelir.",
        "factIds": [
          "f9",
          "f6"
        ]
      },
      {
        "id": "l22",
        "display": "Kanı dolaştıran ise kalptir. Kalp her atışta kanı tüm vücuduna pompalar.",
        "spoken": "Kanı dolaştıran ise kalptir. Kalp her atışta kanı tüm vücuduna pompalar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Atardamarlar, akciğerlerden oksijen almış kanı kalpten vücudun geri kalanına taşır.",
        "spoken": "Atardamarlar, akciğerlerden oksijen almış kanı kalpten vücudun geri kalanına taşır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Kan sonra toplardamarlarla kalbe ve akciğerlere geri döner. Böylece döngü yeniden başlar.",
        "spoken": "Kan sonra toplardamarlarla kalbe ve akciğerlere geri döner. Böylece döngü yeniden başlar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Herkesin bir kan grubu vardır. MedlinePlus'a göre dört kan grubu var: A, B, AB ve O. Kan ayrıca Rh pozitif ya da Rh negatiftir.",
        "spoken": "Herkesin bir kan grubu vardır. Medlayn Plas'a göre dört kan grubu var: A, B, A B ve O. Kan ayrıca R h pozitif ya da R h negatiftir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Benim kan grubum yok. Olsa olsa yağ grubum var!",
        "spoken": "Benim kan grubum yok. Olsa olsa yağ grubum var!",
        "factIds": []
      },
      {
        "id": "l27",
        "display": "Şimdi sıra sende! Kalbinin pompaladığı kanı hissedebilirsin. İki parmağını bileğinin iç tarafına, başparmak hizasına hafifçe koy.",
        "spoken": "Şimdi sıra sende! Kalbinin pompaladığı kanı hissedebilirsin. İki parmağını bileğinin iç tarafına, başparmak hizasına hafifçe koy.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Hafif vuruşları hissediyor musun? Her vuruş, kalbinin bir atışıdır. Bir de zıpladıktan sonra dene: vuruşlar değişiyor mu?",
        "spoken": "Hafif vuruşları hissediyor musun? Her vuruş, kalbinin bir atışıdır. Bir de zıpladıktan sonra dene: vuruşlar değişiyor mu?",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l29",
        "display": "Bunu biliyor muydun? Amerikan Hematoloji Derneği'ne göre vücut ağırlığının yaklaşık yüzde 7 ile 8'i kandır!",
        "spoken": "Bunu biliyor muydun? Amerikan Hematoloji Derneği'ne göre vücut ağırlığının yaklaşık yüzde yedi ile sekizi kandır!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l30",
        "display": "Hızlı soru! Alyuvarların içinde oksijen taşıyan proteinin adı neydi?",
        "spoken": "Hızlı soru! Alyuvarların içinde oksijen taşıyan proteinin adı neydi?",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l31",
        "display": "Düşün bakalım... Evet: hemoglobin!",
        "spoken": "Düşün bakalım... Evet: hemoglobin!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l32",
        "display": "Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!",
        "spoken": "Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!",
        "factIds": []
      }
    ]
  },
  {
    "id": "summary",
    "lines": [
      {
        "id": "l33",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Abone olmayı ve zili açmayı unutma. Kalbin hep neşeyle atsın!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Kalbin hep neşeyle atsın!",
        "factIds": []
      }
    ]
  }
]
</senaryo>

<olgular>
[
  {
    "id": "f1",
    "statement": "Kanın dört ana bileşeni vardır: plazma, alyuvarlar, akyuvarlar ve trombositler.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Plazma; besinler, proteinler, hormonlar ve atık maddeler içeren sarımsı bir sıvıdır; kanın yarısından fazlası plazmadır; kan yaklaşık yüzde 55 plazma ve yüzde 45 kan hücresinden oluşan bir karışımdır.",
    "numbers": [
      "55",
      "45"
    ]
  },
  {
    "id": "f3",
    "statement": "Kanın görevi oksijeni ve besinleri vücudun her yerine götürmektir; kan karbondioksiti ve diğer atıkları akciğerlere, böbreklere ve sindirim sistemine taşır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Alyuvarlar oksijen taşıyan hemoglobin proteinini içerir; hemoglobin akciğerlerde oksijen alınca kan parlak kırmızı rengini alır; alyuvarlar oksijeni akciğerlerden doku ve organlara götürür.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Alyuvar, ortası basık, iki yüzü içe çökük bir disk biçimindedir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Bir alyuvar ortalama 120 gün yaşar.",
    "numbers": [
      "120"
    ]
  },
  {
    "id": "f7",
    "statement": "Farklı türdeki akyuvarlar bakteri ve virüs gibi mikroplarla savaşır; akyuvarlar vücudu enfeksiyondan korur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Trombositler pıhtılaşmaya yardım eden minik hücrelerdir; bir kan damarı yırtılınca o bölgede toplanıp sızıntıyı kapatmaya yardım ederler.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Kemiklerin içindeki süngerimsi madde olan kemik iliği yeni kan hücreleri yapar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Toplam vücut ağırlığının yaklaşık yüzde 7 ile 8'i kandır.",
    "numbers": [
      "7",
      "8"
    ]
  },
  {
    "id": "f11",
    "statement": "Kalp her atışta kanı vücuda pompalar; atardamarlar oksijenli kanı kalpten vücudun geri kalanına taşır; kan toplardamarlarla kalbe ve akciğerlere geri döner.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Dört kan grubu vardır: A, B, AB ya da O; ayrıca kan Rh pozitif ya da Rh negatiftir.",
    "numbers": []
  }
]
</olgular>

# ÇIKTI ŞEMASI (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "scenes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "section": {
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
          "lineIds": {
            "minItems": 1,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "visual": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "hook"
                  },
                  "question": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "question"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "source-card"
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "big-number"
                  },
                  "value": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "label": {
                    "type": "string"
                  },
                  "sub": {
                    "type": "string"
                  },
                  "icon": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "value",
                  "label"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "clock"
                  },
                  "title": {
                    "type": "string"
                  },
                  "center": {
                    "type": "string"
                  },
                  "markers": {
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "at": {
                          "type": "number",
                          "minimum": 0,
                          "maximum": 24
                        },
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "at",
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "center",
                  "markers"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "spotlight"
                  },
                  "title": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  },
                  "chips": {
                    "minItems": 2,
                    "maxItems": 6,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "emoji",
                  "chips"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "stages"
                  },
                  "title": {
                    "type": "string"
                  },
                  "rows": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "path": {
                    "minItems": 3,
                    "maxItems": 40,
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "minimum": 0,
                      "maximum": 9007199254740991
                    }
                  },
                  "highlightRow": {
                    "type": "integer",
                    "minimum": -9007199254740991,
                    "maximum": 9007199254740991
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "rows",
                  "path"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "meter"
                  },
                  "title": {
                    "type": "string"
                  },
                  "label": {
                    "type": "string"
                  },
                  "emoji": {
                    "type": "string"
                  },
                  "phases": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "level": {
                          "type": "number",
                          "minimum": 0,
                          "maximum": 1
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label",
                        "level"
                      ],
                      "additionalProperties": false
                    }
                  },
                  "note": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "title",
                  "label",
                  "phases"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "bar-chart"
                  },
                  "title": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "bars": {
                    "minItems": 2,
                    "maxItems": 6,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "value": {
                          "type": "number"
                        },
                        "display": {
                          "type": "string"
                        },
                        "highlight": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "label",
                        "value",
                        "display"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "bars"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "line-chart"
                  },
                  "title": {
                    "type": "string"
                  },
                  "xLabel": {
                    "type": "string"
                  },
                  "yLabel": {
                    "type": "string"
                  },
                  "points": {
                    "minItems": 2,
                    "maxItems": 12,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "value": {
                          "type": "number"
                        },
                        "display": {
                          "type": "string"
                        },
                        "highlight": {
                          "type": "boolean"
                        }
                      },
                      "required": [
                        "label",
                        "value",
                        "display"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "xLabel",
                  "yLabel",
                  "points"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "comparison"
                  },
                  "title": {
                    "type": "string"
                  },
                  "left": {
                    "type": "object",
                    "properties": {
                      "title": {
                        "type": "string"
                      },
                      "value": {
                        "type": "string"
                      },
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "title",
                      "items"
                    ],
                    "additionalProperties": false
                  },
                  "right": {
                    "type": "object",
                    "properties": {
                      "title": {
                        "type": "string"
                      },
                      "value": {
                        "type": "string"
                      },
                      "items": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "required": [
                      "title",
                      "items"
                    ],
                    "additionalProperties": false
                  }
                },
                "required": [
                  "type",
                  "title",
                  "left",
                  "right"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "diagram"
                  },
                  "title": {
                    "type": "string"
                  },
                  "layout": {
                    "type": "string",
                    "enum": [
                      "flow",
                      "cycle"
                    ]
                  },
                  "nodes": {
                    "minItems": 2,
                    "maxItems": 5,
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "emoji": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "label"
                      ],
                      "additionalProperties": false
                    }
                  }
                },
                "required": [
                  "type",
                  "title",
                  "layout",
                  "nodes"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "analogy"
                  },
                  "template": {
                    "type": "string",
                    "enum": [
                      "scale",
                      "fill",
                      "race",
                      "zoom"
                    ]
                  },
                  "title": {
                    "type": "string"
                  },
                  "a": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "string"
                      },
                      "value": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "label",
                      "value"
                    ],
                    "additionalProperties": false
                  },
                  "b": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "string"
                      },
                      "value": {
                        "type": "number"
                      },
                      "display": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "label",
                      "value"
                    ],
                    "additionalProperties": false
                  },
                  "caption": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "template",
                  "title",
                  "a",
                  "b",
                  "caption"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "quote-card"
                  },
                  "quote": {
                    "type": "string"
                  },
                  "attribution": {
                    "type": "string"
                  }
                },
                "required": [
                  "type",
                  "quote",
                  "attribution"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "bullets"
                  },
                  "title": {
                    "type": "string"
                  },
                  "items": {
                    "minItems": 1,
                    "maxItems": 4,
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "tone": {
                    "type": "string",
                    "enum": [
                      "neutral",
                      "caution"
                    ]
                  }
                },
                "required": [
                  "type",
                  "title",
                  "items"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "song"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "type": {
                    "type": "string",
                    "const": "outro"
                  }
                },
                "required": [
                  "type"
                ],
                "additionalProperties": false
              }
            ]
          },
          "mascot": {
            "type": "object",
            "properties": {
              "state": {
                "type": "string",
                "enum": [
                  "idle",
                  "talk",
                  "point",
                  "think"
                ]
              },
              "x": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
              },
              "y": {
                "type": "number",
                "minimum": 0,
                "maximum": 1
              },
              "scale": {
                "type": "number",
                "minimum": 0.3,
                "maximum": 2.5
              },
              "pointAt": {
                "type": "object",
                "properties": {
                  "x": {
                    "type": "number"
                  },
                  "y": {
                    "type": "number"
                  }
                },
                "required": [
                  "x",
                  "y"
                ],
                "additionalProperties": false
              },
              "pose": {
                "type": "string",
                "enum": [
                  "point",
                  "crossed",
                  "thumbs",
                  "book",
                  "wave"
                ]
              }
            },
            "required": [
              "state",
              "x",
              "y",
              "scale"
            ],
            "additionalProperties": false
          },
          "factIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "sourceNote": {
            "type": "string"
          },
          "stickers": {
            "maxItems": 6,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "fx": {
            "type": "string",
            "enum": [
              "blackhole",
              "shake",
              "flash",
              "meteor",
              "dig",
              "erupt",
              "rain",
              "sparkle"
            ]
          },
          "keywords": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "id",
          "section",
          "lineIds",
          "visual",
          "mascot",
          "factIds"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "scenes"
  ],
  "additionalProperties": false
}
```
