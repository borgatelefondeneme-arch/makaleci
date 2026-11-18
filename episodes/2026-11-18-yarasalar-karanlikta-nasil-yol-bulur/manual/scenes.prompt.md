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
        "display": "Zifiri karanlık bir gece. Gözlerini kapatsan bile yolunu bulabilir misin? Yarasalar her gece bunu yapar, hem de uçarken!",
        "spoken": "Zifiri karanlık bir gece. Gözlerini kapatsan bile yolunu bulabilir misin? Yarasalar her gece bunu yapar, hem de uçarken!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Peki ışık olmadan nasıl görüyorlar?",
        "spoken": "Peki ışık olmadan nasıl görüyorlar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün yarasaların gizli süper gücünü keşfediyoruz: sesle görmek!",
        "spoken": "Bugün yarasaların gizli süper gücünü keşfediyoruz: sesle görmek!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Yarasalar karanlıkta nasıl yol bulur? Neden uçabilen tek memelilerdir? Ve doğa için neden bu kadar önemlidirler?",
        "spoken": "Üç sorumuz var. Yarasalar karanlıkta nasıl yol bulur? Neden uçabilen tek memelilerdir? Ve doğa için neden bu kadar önemlidirler?",
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
        "display": "ABD Milli Parklar Servisi'ne göre yarasalar yön bulmak ve böcek avlamak için ekolokasyon kullanır.",
        "spoken": "ABD Milli Parklar Servisi'ne göre yarasalar yön bulmak ve böcek avlamak için ekolokasyon kullanır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Ekolokasyon, sesle ve yankıyla yer bulmak demektir. Yarasa, insanların duyamayacağı kadar tiz sesler çıkarır. Bunlara ultrason denir.",
        "spoken": "Ekolokasyon, sesle ve yankıyla yer bulmak demektir. Yarasa, insanların duyamayacağı kadar tiz sesler çıkarır. Bunlara ultrason denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Ses dalgaları çevredeki cisimlere çarpıp geri döner ve yarasanın kulaklarına ulaşır.",
        "spoken": "Ses dalgaları çevredeki cisimlere çarpıp geri döner ve yarasanın kulaklarına ulaşır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "National Geographic'e göre bu yankı, yarasaya cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler.",
        "spoken": "Neşınıl Ciyogrefik'e göre bu yankı, yarasaya cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Kulakları da kendi özgün çağrılarını tanıyacak kadar ince ayarlıdır. Yani kalabalık bir mağarada bile kendi sesini ayırt eder!",
        "spoken": "Kulakları da kendi özgün çağrılarını tanıyacak kadar ince ayarlıdır. Yani kalabalık bir mağarada bile kendi sesini ayırt eder!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Benim de bir sensörüm var. Ama ben duvarı ancak çarptıktan sonra fark ediyorum!",
        "spoken": "Benim de bir sensörüm var. Ama ben duvarı ancak çarptıktan sonra fark ediyorum!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Bir de şu var: Benekli yarasa denen bir türün sesini, iyi duyan insanlar belli belirsiz duyabilir.",
        "spoken": "Bir de şu var: Benekli yarasa denen bir türün sesini, iyi duyan insanlar belli belirsiz duyabilir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Yarasalar kör de değildir. USGS'ye göre gözleri küçüktür ama görüşleri çok hassastır.",
        "spoken": "Yarasalar kör de değildir. Yu Es Ci Es'e göre gözleri küçüktür ama görüşleri çok hassastır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l14",
        "display": "Bu hassas gözler, bizim zifiri karanlık sandığımız yerlerde bile görmelerine yardım eder.",
        "spoken": "Bu hassas gözler, bizim zifiri karanlık sandığımız yerlerde bile görmelerine yardım eder.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l15",
        "display": "Yarasaların bilimsel adı Chiroptera'dır. Yunanca 'el kanat' demektir.",
        "spoken": "Yarasaların bilimsel adı Kiroptera'dır. Yunanca el kanat demektir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Çünkü kanatları aslında bir eldir: Dört uzun parmak ve bir başparmak, ince bir deriyle birbirine bağlanmıştır.",
        "spoken": "Çünkü kanatları aslında bir eldir: Dört uzun parmak ve bir başparmak, ince bir deriyle birbirine bağlanmıştır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Bu sayede yarasalar dünyada uçabilen tek memelilerdir!",
        "spoken": "Bu sayede yarasalar dünyada uçabilen tek memelilerdir!",
        "factIds": [
          "f7"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "National Geographic'e göre dünyada 1.300'den fazla yarasa türü var. Kemirgenlerden sonra en kalabalık ikinci memeli grubu!",
        "spoken": "Neşınıl Ciyogrefik'e göre dünyada bin üç yüzden fazla yarasa türü var. Kemirgenlerden sonra en kalabalık ikinci memeli grubu!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Çoğu, gece çıkan güve gibi böcekleri yiyen mikro yarasalardır. Mega yarasalar ise tropiklerde yaşar; meyve, nektar ve polen yer.",
        "spoken": "Çoğu, gece çıkan güve gibi böcekleri yiyen mikro yarasalardır. Mega yarasalar ise tropiklerde yaşar; meyve, nektar ve polen yer.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Vampir yarasalar mı? Kanla beslenen tek mikro yarasa türü onlardır. Merak etme, ben vampir değilim; ben sadece elektrik içerim!",
        "spoken": "Vampir yarasalar mı? Kanla beslenen tek mikro yarasa türü onlardır. Merak etme, ben vampir değilim; ben sadece elektrik içerim!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Böcek yiyen yarasalar bir gecede milyonlarca böcek yer. Bitkiler için doğal bir zararlı kontrolüdürler.",
        "spoken": "Böcek yiyen yarasalar bir gecede milyonlarca böcek yer. Bitkiler için doğal bir zararlı kontrolüdürler.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Ayrıca mango, muz ve avokado dahil 500'den fazla bitki türü tozlaşma için yarasalara bağlıdır.",
        "spoken": "Ayrıca mango, muz ve avokado dahil beş yüzden fazla bitki türü tozlaşma için yarasalara bağlıdır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Meyve yiyen yarasalar tohumları yayar ve yağmur ormanlarının büyümesine yardım eder.",
        "spoken": "Meyve yiyen yarasalar tohumları yayar ve yağmur ormanlarının büyümesine yardım eder.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! Boş bir koridorda ya da büyük bir odada ellerini bir kez çırp ve sesi dinle.",
        "spoken": "Şimdi sıra sende! Boş bir koridorda ya da büyük bir odada ellerini bir kez çırp ve sesi dinle.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l25",
        "display": "Duvara yaklaşıp uzaklaşarak tekrar çırp. Yankı değişiyor mu? Ama gerçek bir yarasa görürsen asla dokunma, uzaktan izle!",
        "spoken": "Duvara yaklaşıp uzaklaşarak tekrar çırp. Yankı değişiyor mu? Ama gerçek bir yarasa görürsen asla dokunma, uzaktan izle!",
        "factIds": [
          "f3",
          "f4"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l26",
        "display": "Bunu biliyor muydun? Bazı yarasalar kışın mağaralarda kış uykusuna yatar. Ne yazık ki 2007'de bulunan beyaz burun sendromu, kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtı.",
        "spoken": "Bunu biliyor muydun? Bazı yarasalar kışın mağaralarda kış uykusuna yatar. Ne yazık ki iki bin yedide bulunan beyaz burun sendromu, kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtı.",
        "factIds": [
          "f13",
          "f14"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Yarasaların sesle ve yankıyla yol bulmasına ne denir?",
        "spoken": "Hızlı soru! Yarasaların sesle ve yankıyla yol bulmasına ne denir?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: ekolokasyon!",
        "spoken": "Düşün bakalım... Evet: ekolokasyon!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l29",
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
        "id": "l30",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Abone olmayı ve zili açmayı unutma. İyi geceler, yarasalar!",
        "spoken": "Abone olmayı ve zili açmayı unutma. İyi geceler, yarasalar!",
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
    "statement": "Yarasalar yön bulmak ve böcek avlamak için ekolokasyon kullanır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Yarasalar insanların duyabileceğinden yüksek frekansta, ultrason denen ses dalgaları üretir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Yarasaların çıkardığı ses dalgaları çevredeki cisimlere çarpıp geri döner; sesler, yarasanın kendi özgün çağrılarını tanımak için ince ayarlı kulaklarına ulaşır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Yarasalar bir cisme çarpıp geri dönen tiz bir ses çıkararak ekolokasyon yapar; bu yankı onlara cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Benekli yarasanın sesi, iyi duyan insanlar tarafından belli belirsiz duyulabilir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Yarasaların bilimsel adı Chiroptera, Yunancada 'el kanat' demektir; yarasaların her biri ince bir deriyle bir sonrakine bağlı dört uzun parmağı ve bir başparmağı vardır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Yarasalar dünyada uçabilen tek memelilerdir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Dünyada 1.300'den fazla yarasa türü vardır; bu onları kemirgenlerden sonra en yaygın ikinci memeli grubu yapar.",
    "numbers": [
      "1.300"
    ]
  },
  {
    "id": "f9",
    "statement": "Yarasaların çoğu güve gibi gece çıkan böcekleri yiyen mikro yarasalardır; mega yarasalar tropiklerde yaşar ve meyve, nektar ve polen yer; vampir yarasalar böcek yerine kanla beslenen tek mikro yarasa türüdür.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Böcek yiyen mikro yarasalar bir gecede milyonlarca böcek yer ve bitkiler için doğal bir zararlı kontrolü sağlar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Mango, muz ve avokado dahil 500'den fazla bitki türü tozlaşma için yarasalara bağlıdır; meyve yiyen yarasalar tohumları yayarak yağmur ormanlarının büyümesine yardım eder.",
    "numbers": [
      "500"
    ]
  },
  {
    "id": "f12",
    "statement": "Yarasaların gözleri küçüktür ama görüşleri çok hassastır; bu, bizim zifiri karanlık sayacağımız koşullarda görmelerine yardım eder.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bazı yarasalar kışın mağaralarda kış uykusuna yatar.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Beyaz burun sendromu ilk kez 2007'de New York'ta bulundu ve kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtığı tahmin ediliyor.",
    "numbers": [
      "2007"
    ]
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
