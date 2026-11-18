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
        "display": "Gökyüzünde parlak bir baş ve arkasında upuzun bir kuyruk... Ama adında yıldız geçse de kuyruklu yıldız aslında bir yıldız değil!",
        "spoken": "Gökyüzünde parlak bir baş ve arkasında upuzun bir kuyruk... Ama adında yıldız geçse de kuyruklu yıldız aslında bir yıldız değil!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Peki o zaman ne? Ve o kuyruk nereden çıkıyor?",
        "spoken": "Peki o zaman ne? Ve o kuyruk nereden çıkıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Güneş Sistemi'nin buzlu gezginlerinin peşine düşüyoruz!",
        "spoken": "Bugün Güneş Sistemi'nin buzlu gezginlerinin peşine düşüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kuyruklu yıldız neden yapılır? Kuyruğu nasıl oluşur? Ve nereden gelir?",
        "spoken": "Üç sorumuz var. Kuyruklu yıldız neden yapılır? Kuyruğu nasıl oluşur? Ve nereden gelir?",
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
        "display": "NASA'ya göre kuyruklu yıldızlar, Güneş'in çevresinde dolanan, toz ve buzdan yapılmış cisimlerdir. Donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler.",
        "spoken": "Nasa'ya göre kuyruklu yıldızlar, Güneş'in çevresinde dolanan, toz ve buzdan yapılmış cisimlerdir. Donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Kuyruklu yıldızın merkezine çekirdek denir. Çekirdek genellikle 16 kilometreden küçüktür, yani küçük bir kasaba büyüklüğünde.",
        "spoken": "Kuyruklu yıldızın merkezine çekirdek denir. Çekirdek genellikle on altı kilometreden küçüktür, yani küçük bir kasaba büyüklüğünde.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Bir kasaba büyüklüğünde kartopu! Ben olsam onunla kartopu savaşı yapmazdım.",
        "spoken": "Bir kasaba büyüklüğünde kartopu! Ben olsam onunla kartopu savaşı yapmazdım.",
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
        "id": "l9",
        "display": "Güneş'ten uzaktayken kuyruklu yıldız donmuş ve sessizdir. Ama Güneş'e yaklaşınca ısınmaya başlar.",
        "spoken": "Güneş'ten uzaktayken kuyruklu yıldız donmuş ve sessizdir. Ama Güneş'e yaklaşınca ısınmaya başlar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Isındıkça buzu gaza dönüşmeye başlar. Gaz ve toz, çekirdeğin çevresinde koma denen dev, bulanık bir bulut oluşturur.",
        "spoken": "Isındıkça buzu gaza dönüşmeye başlar. Gaz ve toz, çekirdeğin çevresinde koma denen dev, bulanık bir bulut oluşturur.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "İşte şimdi kuyruklar ortaya çıkar! Kuyruklu yıldızın iki kuyruğu vardır ve Güneş'e yaklaştıkça uzarlar.",
        "spoken": "İşte şimdi kuyruklar ortaya çıkar! Kuyruklu yıldızın iki kuyruğu vardır ve Güneş'e yaklaştıkça uzarlar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Birincisi toz kuyruğudur. Beyaz görünür ve Güneş'ten uzağa doğru geniş, hafifçe kıvrılan bir yol çizer.",
        "spoken": "Birincisi toz kuyruğudur. Beyaz görünür ve Güneş'ten uzağa doğru geniş, hafifçe kıvrılan bir yol çizer.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "İkincisi iyon kuyruğudur. İyon kuyruğu her zaman doğrudan Güneş'in tersine bakar.",
        "spoken": "İkincisi iyon kuyruğudur. İyon kuyruğu her zaman doğrudan Güneş'in tersine bakar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Yani kuyruk, kuyruklu yıldızın arkasında değil, Güneş'in tersinde durur. Benim cin kuyruğum ise hep arkamda, ona güvenebilirim!",
        "spoken": "Yani kuyruk, kuyruklu yıldızın arkasında değil, Güneş'in tersinde durur. Benim cin kuyruğum ise hep arkamda, ona güvenebilirim!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l15",
        "display": "Peki kuyruklu yıldızlar nereden gelir? NASA'ya göre bazıları Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda yaşar.",
        "spoken": "Peki kuyruklu yıldızlar nereden gelir? Nasa'ya göre bazıları Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda yaşar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Bazıları ise Güneş Sistemi'nin dış kenarındaki küre biçimli Oort Bulutu'nda. Güneş'in çevresinde muhtemelen milyarlarca kuyruklu yıldız dolanıyor!",
        "spoken": "Bazıları ise Güneş Sistemi'nin dış kenarındaki küre biçimli Oort Bulutu'nda. Güneş'in çevresinde muhtemelen milyarlarca kuyruklu yıldız dolanıyor!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Bazılarının yolculuğu çok uzun sürer. Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için 250.000 yıldan fazla zaman harcar!",
        "spoken": "Bazılarının yolculuğu çok uzun sürer. Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için iki yüz elli bin yıldan fazla zaman harcar!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "En ünlüsü Halley Kuyruklu Yıldızı'dır. Ortalama 76 yılda bir döner. En son 1986'da görüldü ve 2061'de geri gelecek.",
        "spoken": "En ünlüsü Halley Kuyruklu Yıldızı'dır. Ortalama yetmiş altı yılda bir döner. En son bin dokuz yüz seksen altıda görüldü ve iki bin altmış birde geri gelecek.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "O zaman ben de burada olacağım. Robotlar yaşlanmaz, sadece güncellenir!",
        "spoken": "O zaman ben de burada olacağım. Robotlar yaşlanmaz, sadece güncellenir!",
        "factIds": []
      },
      {
        "id": "l20",
        "display": "Halley her dönüşünde uzaya buz ve kaya püskürtür. Bu döküntü her yıl iki meteor yağmuruna yol açar: Mayıs'ta Eta Akuaridler, Ekim'de Orionidler.",
        "spoken": "Halley her dönüşünde uzaya buz ve kaya püskürtür. Bu döküntü her yıl iki meteor yağmuruna yol açar: Mayıs'ta Eta Akuaridler, Ekim'de Orionidler.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Bilim insanları kuyruklu yıldızları yakından da inceledi. Rosetta aracı bir kuyruklu yıldızın çekirdeğine iniş aracı bıraktı ve iki yıl onun çevresinde dolandı.",
        "spoken": "Bilim insanları kuyruklu yıldızları yakından da inceledi. Rosetta aracı bir kuyruklu yıldızın çekirdeğine iniş aracı bıraktı ve iki yıl onun çevresinde dolandı.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Şimdi sıra sende! Ekim'de Orionid meteor yağmuru zamanı, bir yetişkinle şehir ışıklarından uzak, karanlık bir yere git.",
        "spoken": "Şimdi sıra sende! Ekim'de Orionid meteor yağmuru zamanı, bir yetişkinle şehir ışıklarından uzak, karanlık bir yere git.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Sırt üstü uzan, gözlerin karanlığa alışsın ve gökyüzünü izle. Gördüğün her kayan ışığı say! Gündüz asla Güneş'e doğrudan bakma.",
        "spoken": "Sırt üstü uzan, gözlerin karanlığa alışsın ve gökyüzünü izle. Gördüğün her kayan ışığı say! Gündüz asla Güneş'e doğrudan bakma.",
        "factIds": [
          "f9"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l24",
        "display": "Bunu biliyor muydun? NASA'nın Stardust görevi bir kuyruklu yıldızdan örnek topladı. Bu parçacıklar, yaşamın yapı taşı sayılan hidrokarbonlarca zengin çıktı!",
        "spoken": "Bunu biliyor muydun? Nasa'nın Stardust görevi bir kuyruklu yıldızdan örnek topladı. Bu parçacıklar, yaşamın yapı taşı sayılan hidrokarbonlarca zengin çıktı!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Hızlı soru! İyon kuyruğu her zaman hangi yöne bakar?",
        "spoken": "Hızlı soru! İyon kuyruğu her zaman hangi yöne bakar?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l26",
        "display": "Düşün bakalım... Evet: Güneş'in tam tersine!",
        "spoken": "Düşün bakalım... Evet: Güneş'in tam tersine!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l27",
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
        "id": "l28",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l29",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Abone olmayı ve zili açmayı unutma. Gökyüzüne bakmayı da!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Gökyüzüne bakmayı da!",
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
    "statement": "Kuyruklu yıldızlar Güneş'in çevresinde dolanan, toz ve buzdan yapılmış buzlu cisimlerdir; donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Bu toz ve buz topu, yani çekirdek, genellikle 16 kilometreden küçüktür; aşağı yukarı küçük bir kasaba büyüklüğündedir.",
    "numbers": [
      "16"
    ]
  },
  {
    "id": "f3",
    "statement": "Kuyruklu yıldız Güneş'e yaklaşınca ısınmaya başlar ve sonunda buz gaza dönüşmeye başlar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Gaz ve toz, çekirdeğin çevresinde koma denen dev, bulanık bir bulut oluşturur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Kuyruklu yıldızın Güneş'e yaklaştıkça uzayan iki kuyruğu vardır; biri beyaz görünür ve tozdan yapılmıştır, Güneş'ten uzağa geniş ve hafifçe kıvrılan bir yol çizer; iyon kuyruğu ise her zaman doğrudan Güneş'in tersine bakar.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Bazı kuyruklu yıldızlar Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda, bazıları Güneş Sistemi'nin dış kenarındaki küre biçimli Oort Bulutu'nda yaşar; Güneş'in çevresinde muhtemelen milyarlarca kuyruklu yıldız dolanır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için 250.000 yıldan fazla zaman harcar.",
    "numbers": [
      "250.000"
    ]
  },
  {
    "id": "f8",
    "statement": "Halley'in yörünge dönemi ortalama 76 Dünya yılıdır; en son 1986'da Dünya'nın göğünde görüldü ve 2061'de geri dönecek.",
    "numbers": [
      "76",
      "1986",
      "2061"
    ]
  },
  {
    "id": "f9",
    "statement": "Halley her dönüşünde çekirdeğinden uzaya buz ve kaya püskürtür; bu döküntü her yıl iki zayıf meteor yağmuruna yol açar: Mayıs'ta Eta Akuaridler, Ekim'de Orionidler.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Rosetta, kuyruklu yıldızın çekirdeğine bir iniş aracı bıraktı ve iki yıl boyunca kuyruklu yıldızın çevresinde dolandı.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "NASA'nın Stardust görevi Wild 2 kuyruklu yıldızından örnek topladı; bu parçacıkların, yaşamın yapı taşı sayılan hidrokarbonlarca zengin olduğu bulundu.",
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
