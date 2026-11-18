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
        "display": "Dünya Sağlık Örgütü'ne göre mikroplar her yerde: çevremizde ve hatta vücudumuzda. Peki vücudun onlarla nasıl başa çıkar?",
        "spoken": "Dünya Sağlık Örgütü'ne göre mikroplar her yerde: çevremizde ve hatta vücudumuzda. Peki vücudun onlarla nasıl başa çıkar?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Hiç karşılaşmadığın bir hastalığa karşı önceden hazırlanmak mümkün mü?",
        "spoken": "Hiç karşılaşmadığın bir hastalığa karşı önceden hazırlanmak mümkün mü?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün vücudunun savunma ordusunu ve aşıların onu nasıl eğittiğini keşfediyoruz!",
        "spoken": "Bugün vücudunun savunma ordusunu ve aşıların onu nasıl eğittiğini keşfediyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Vücudun mikroplarla nasıl savaşır? Aşı içinde ne vardır? Ve aşı neden başkalarını da korur?",
        "spoken": "Üç sorumuz var. Vücudun mikroplarla nasıl savaşır? Aşı içinde ne vardır? Ve aşı neden başkalarını da korur?",
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
        "display": "Hastalığa yol açabilen bakteri, virüs, parazit ya da mantarlara patojen denir.",
        "spoken": "Hastalığa yol açabilen bakteri, virüs, parazit ya da mantarlara patojen denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l7",
        "display": "Her patojenin üzerinde antijen denen bir parça vardır. Antijen, vücudunun 'Bu bir yabancı!' diye tanıdığı kimlik kartı gibidir.",
        "spoken": "Her patojenin üzerinde antijen denen bir parça vardır. Antijen, vücudunun 'Bu bir yabancı!' diye tanıdığı kimlik kartı gibidir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l8",
        "display": "Vücudun antijeni tanıyınca antikor üretir. Dünya Sağlık Örgütü'ne göre antikorlar savunma sisteminin askerleri gibidir.",
        "spoken": "Vücudun antijeni tanıyınca antikor üretir. Dünya Sağlık Örgütü'ne göre antikorlar savunma sisteminin askerleri gibidir.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l9",
        "display": "Her antikor tek bir antijeni tanımak üzere eğitilmiştir. Yani her askerin tek bir hedefi vardır!",
        "spoken": "Her antikor tek bir antijeni tanımak üzere eğitilmiştir. Yani her askerin tek bir hedefi vardır!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Benim de bir savunma sistemim var: antivirüs programı. Ama o sadece bilgisayar virüslerini tanıyor!",
        "spoken": "Benim de bir savunma sistemim var: antivirüs programı. Ama o sadece bilgisayar virüslerini tanıyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Savaş bitince bir şey daha olur: Hafıza hücreleri oluşur. Patojen yenildikten sonra da hayatta kalırlar.",
        "spoken": "Savaş bitince bir şey daha olur: Hafıza hücreleri oluşur. Patojen yenildikten sonra da hayatta kalırlar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Aynı patojen bir daha gelirse, antikor yanıtı ilk seferden çok daha hızlı ve etkili olur. Vücudun onu hatırlar!",
        "spoken": "Aynı patojen bir daha gelirse, antikor yanıtı ilk seferden çok daha hızlı ve etkili olur. Vücudun onu hatırlar!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "İşte aşıların sırrı bu hafızada. Aşılar, belirli bir mikrobun zayıflatılmış ya da etkisiz parçalarını, yani antijenlerini içerir.",
        "spoken": "İşte aşıların sırrı bu hafızada. Aşılar, belirli bir mikrobun zayıflatılmış ya da etkisiz parçalarını, yani antijenlerini içerir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Bazı yeni aşılar ise antijenin kendisini değil, onu üretmenin planını taşır: DNA ya da RNA.",
        "spoken": "Bazı yeni aşılar ise antijenin kendisini değil, onu üretmenin planını taşır: DNA ya da RNA.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "CDC'ye göre aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir.",
        "spoken": "Si Di Si'ye göre aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Böylece vücudun, gerçek bir hastalığın tehlikeleri olmadan kendini korumayı öğrenir. Bir tatbikat gibi!",
        "spoken": "Böylece vücudun, gerçek bir hastalığın tehlikeleri olmadan kendini korumayı öğrenir. Bir tatbikat gibi!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Ben de tatbikat yaparım: her sabah kendimi kapatıp açıyorum. Ama hâlâ kapatma düğmemi bulamadım!",
        "spoken": "Ben de tatbikat yaparım: her sabah kendimi kapatıp açıyorum. Ama hâlâ kapatma düğmemi bulamadım!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Bazı aşılar haftalar ya da aylar arayla birden çok doz gerektirir.",
        "spoken": "Bazı aşılar haftalar ya da aylar arayla birden çok doz gerektirir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l19",
        "display": "Bu, uzun ömürlü antikorların ve hafıza hücrelerinin gelişmesi için gerekebilir. Bağışıklığın gelişmesi de haftalar sürebilir.",
        "spoken": "Bu, uzun ömürlü antikorların ve hafıza hücrelerinin gelişmesi için gerekebilir. Bağışıklığın gelişmesi de haftalar sürebilir.",
        "factIds": [
          "f9",
          "f10"
        ]
      },
      {
        "id": "l20",
        "display": "Aşıdan sonra bir iki gün biraz yorgun ya da rahatsız hissedebilirsin. CDC'ye göre bu, vücudunun bağışıklık yanıtıdır.",
        "spoken": "Aşıdan sonra bir iki gün biraz yorgun ya da rahatsız hissedebilirsin. Si Di Si'ye göre bu, vücudunun bağışıklık yanıtıdır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l21",
        "display": "Aşıların bir süper gücü daha var. Bir toplulukta çok kişi aşılanınca patojen yayılmakta zorlanır. Buna sürü bağışıklığı denir.",
        "spoken": "Aşıların bir süper gücü daha var. Bir toplulukta çok kişi aşılanınca patojen yayılmakta zorlanır. Buna sürü bağışıklığı denir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l22",
        "display": "Böylece aşılanamayan insanlar da korunur. Aşı olmak sadece seni değil, çevreni de korur.",
        "spoken": "Böylece aşılanamayan insanlar da korunur. Aşı olmak sadece seni değil, çevreni de korur.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l23",
        "display": "Şimdi sıra sende! Domino taşlarını sıraya diz ve ilkini devir. Hepsi birbirini devirir, değil mi?",
        "spoken": "Şimdi sıra sende! Domino taşlarını sıraya diz ve ilkini devir. Hepsi birbirini devirir, değil mi?",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l24",
        "display": "Şimdi aralardan bazı taşları çıkar ve tekrar dene. Zincir duruyor mu? Sürü bağışıklığı da yayılmayı böyle durdurur!",
        "spoken": "Şimdi aralardan bazı taşları çıkar ve tekrar dene. Zincir duruyor mu? Sürü bağışıklığı da yayılmayı böyle durdurur!",
        "factIds": [
          "f12"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l25",
        "display": "Bunu biliyor muydun? Küresel aşılama çalışmalarından sonra, Dünya Sağlık Örgütü 1980'de çiçek hastalığının yok edildiğini onayladı!",
        "spoken": "Bunu biliyor muydun? Küresel aşılama çalışmalarından sonra, Dünya Sağlık Örgütü bin dokuz yüz sekseninde çiçek hastalığının yok edildiğini onayladı!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Hızlı soru! Bir mikrobu hatırlayıp ikinci seferde hızlı yanıt veren hücrelere ne denir?",
        "spoken": "Hızlı soru! Bir mikrobu hatırlayıp ikinci seferde hızlı yanıt veren hücrelere ne denir?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l27",
        "display": "Düşün bakalım... Evet: hafıza hücreleri!",
        "spoken": "Düşün bakalım... Evet: hafıza hücreleri!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l28",
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
        "id": "l29",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Abone olmayı ve zili açmayı unutma. Sağlıkla kal!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Sağlıkla kal!",
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
    "statement": "Mikroplar hem çevremizde hem vücudumuzda, her yerdedir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Patojen, vücutta hastalığa yol açabilen bir bakteri, virüs, parazit ya da mantardır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Patojenin antikor oluşumuna yol açan parçasına antijen denir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Antikorlar vücudun savunma sistemindeki askerler gibidir; her antikor tek bir belirli antijeni tanımak üzere eğitilmiştir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Patojen antikorlarca yenildikten sonra da hayatta kalan hafıza hücreleri oluşur; aynı patojenle yeniden karşılaşınca antikor yanıtı ilk seferden çok daha hızlı ve etkili olur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Aşılar belirli bir organizmanın zayıflatılmış ya da etkisiz parçalarını (antijen) içerir; yeni aşılar antijenin kendisi yerine onu üretmenin planını (DNA ya da RNA) içerir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir; vücudun, tam bir enfeksiyonun tehlikeleri olmadan kendini korumayı öğrenmesine yardım eder.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Akyuvarlar kemik iliğinde üretilir ama vücudun her yerine az sayıda dağılır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Bazı aşılar haftalar ya da aylar arayla birden çok doz gerektirir; bu, uzun ömürlü antikorların ve hafıza hücrelerinin gelişmesi için gerekebilir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Bağışıklığın gelişmesi aşıdan sonra haftalar sürebilir.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Aşıya verilen bağışıklık yanıtı bir iki gün yorgunluk ve rahatsızlık yapabilir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Bir toplulukta çok kişi aşılanınca patojen yayılmakta zorlanır; buna sürü bağışıklığı denir; aşılanmak yalnızca kişinin kendisini değil, aşılanamayanları da korur.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Çiçek hastalığının yok edildiği, küresel aşılama ve gözetim çalışmalarının ardından 1980'de Dünya Sağlık Örgütü tarafından onaylandı.",
    "numbers": [
      "1980"
    ]
  },
  {
    "id": "f14",
    "statement": "2000 ile 2023 arasında kızamık aşılamasının tahminen 60 milyon ölümü önlediği hesaplanıyor.",
    "numbers": [
      "2000",
      "2023",
      "60"
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
