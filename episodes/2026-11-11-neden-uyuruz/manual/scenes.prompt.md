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
  - "source-card": künye kartı (yazar/kurum/dergi/DOI otomatik dolar) — künyenin okunduğu satırlar için zorunlu.
  - "big-number": tek çarpıcı sayı { value, unit?, label, sub? }. "value" makaledeki yazımla.
  - "bar-chart": 2–6 çubuk { title, unit?, bars: [{ label, value (sayı), display (ekranda yazılacak hali), highlight? }] }.
  - "line-chart": zaman/sıra içinde değişim { title, xLabel, yLabel, points: [...] }.
  - "comparison": iki şeyin yan yana kıyası { title, left: { title, value?, items[] }, right: {...} }.
  - "diagram": 2–5 adımlı süreç { title, layout: "flow" | "cycle", nodes: [{ label, emoji? }] } — yöntem anlatımı için ideal.
  - "analogy": benzetme { template: "scale" (alan kıyası) | "fill" (dolan kap) | "race" (yarış) | "zoom" (iç içe ölçek), title, a: { label, value, display? }, b: {...}, caption }. Benzetmede makalede olmayan sayı gösterme; "display" boş bırakılırsa sayı yazılmaz, yalnızca oran çizilir.
  - "quote-card": makaleden kısa alıntı { quote (Türkçe çeviri, en çok iki cümle), attribution }.
  - "bullets": 1–4 madde { title, items[], tone?: "neutral" | "caution" } — sınırlılıklar için "caution".
  - "song": kapanış şarkısı (senaryoda "song" varsa zorunlu) — sondan bir önceki sahne; yalnızca şarkıya davet eden satırı içerir. Zerre/Muma bu sahnede sağda ve büyük durur (x≈0,86, y≈0,52, scale≈1,3, state "talk").
  - "outro": kapanış — son sahne, summary bölümünün tüm satırlarını kapsar.
- "mascot": karakter Zerre'nin bu sahnedeki hali { state: "idle" | "talk" | "point" | "think", x, y (0–1, ekran oranı, merkez), scale (0,5–1,6), pointAt? }.
  İçerik sol-ortadadır; Zerre genelde sağda durur (x≈0,86, y≈0,62, scale≈1). Geniş sahnelerde (bar-chart, line-chart, diagram, analogy, comparison) küçülüp köşeye çekilsin (x≈0,9, y≈0,72, scale≈0,7). "hook" sahnesinde solda ve büyük (x≈0,17, y≈0,5, scale≈1,6, state "think"). Bir sayıya ya da grafiğe dikkat çekerken "point" kullan ve "pointAt" ile hedefi ver. Sahneden sahneye konum ve boyut değişsin ki karakter ekranda gezsin.

<senaryo>
[
  {
    "id": "hook",
    "lines": [
      {
        "id": "l1",
        "display": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Bir anda sabah oldu.",
        "spoken": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Bir anda sabah oldu.",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Peki aradaki o saatlerde ne oldu? Vücudun düğmesine basılıp kapandı mı?",
        "spoken": "Peki aradaki o saatlerde ne oldu? Vücudun düğmesine basılıp kapandı mı?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Hiç de değil! Sen uyurken içeride koca bir gece vardiyası çalışıyor. Hadi, gizlice bakalım!",
        "spoken": "Hiç de değil! Sen uyurken içeride koca bir gece vardiyası çalışıyor. Hadi, gizlice bakalım!",
        "factIds": [
          "f1"
        ]
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Merhaba! Ben Muma! Gerçi ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!",
        "spoken": "Merhaba! Ben Muma! Gerçi ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?",
        "spoken": "Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?",
        "factIds": []
      },
      {
        "id": "l6",
        "display": "Bilgilerimiz sağlık kurumlarının sayfalarından geliyor: CDC, NIH ve Nemours KidsHealth.",
        "spoken": "Bilgilerimiz sağlık kurumlarının sayfalarından geliyor: Si Di Si, En Ay Eyç ve Nemurs Kids Helt.",
        "factIds": []
      },
      {
        "id": "l7",
        "display": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum!",
        "spoken": "Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum!",
        "factIds": []
      }
    ]
  },
  {
    "id": "method",
    "lines": [
      {
        "id": "l8",
        "display": "Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?",
        "spoken": "Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır.",
        "spoken": "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!",
        "spoken": "Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Ana saati en çok ışık ve karanlık etkiler.",
        "spoken": "Ana saati en çok ışık ve karanlık etkiler.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.",
        "spoken": "Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Yani akşam esnemeye başladıysan suçlu belli: melatonin!",
        "spoken": "Yani akşam esnemeye başladıysan suçlu belli: melatonin!",
        "factIds": [
          "f5"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. İki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.",
        "spoken": "Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. İki tür uyku arasında gidip gelir: Rem olmayan uyku ve Rem uykusu.",
        "factIds": [
          "f1",
          "f7"
        ]
      },
      {
        "id": "l15",
        "display": "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık 90 dakika sürer.",
        "spoken": "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık doksan dakika sürer.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l16",
        "display": "REM olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.",
        "spoken": "Rem olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l17",
        "display": "Yani büyümek, biraz da yastık işi!",
        "spoken": "Yani büyümek, biraz da yastık işi!",
        "factIds": [
          "f9",
          "f15"
        ]
      },
      {
        "id": "l18",
        "display": "REM uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder. En canlı rüyalarımızı da bu sırada görürüz.",
        "spoken": "Rem uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder. En canlı rüyalarımızı da bu sırada görürüz.",
        "factIds": [
          "f10",
          "f11"
        ]
      },
      {
        "id": "l19",
        "display": "İlginç olan şu: REM uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!",
        "spoken": "İlginç olan şu: Rem uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l20",
        "display": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "spoken": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "factIds": [
          "f13",
          "f14"
        ]
      },
      {
        "id": "l21",
        "display": "Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.",
        "spoken": "Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l22",
        "display": "Peki yeterince uyumazsak? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.",
        "spoken": "Peki yeterince uyumazsak? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l23",
        "display": "O zaman ne kadar uyumalıyız? 6–12 yaş arasındaysan günde 9–12 saat.",
        "spoken": "O zaman ne kadar uyumalıyız? Altı ile on iki yaş arasındaysan günde dokuz ile on iki saat.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l24",
        "display": "13–17 yaş arasındaysan 8–10 saat.",
        "spoken": "On üç ile on yedi yaş arasındaysan sekiz ile on saat.",
        "factIds": [
          "f19"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?",
        "spoken": "Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?",
        "factIds": []
      },
      {
        "id": "l26",
        "display": "Bir: Her gün aynı saatte yat, aynı saatte kalk.",
        "spoken": "Bir: Her gün aynı saatte yat, aynı saatte kalk.",
        "factIds": [
          "f20"
        ]
      },
      {
        "id": "l27",
        "display": "İki: Yatmadan en az 30 dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.",
        "spoken": "İki: Yatmadan en az otuz dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.",
        "factIds": [
          "f21",
          "f22"
        ]
      },
      {
        "id": "l28",
        "display": "Üç: Odan sessiz, sakin ve serin olsun.",
        "spoken": "Üç: Odan sessiz, sakin ve serin olsun.",
        "factIds": [
          "f23"
        ]
      },
      {
        "id": "l29",
        "display": "Dört: Her sabah nasıl hissettiğini bir kâğıda not et, hafta sonunda karşılaştır.",
        "spoken": "Dört: Her sabah nasıl hissettiğini bir kâğıda not et, hafta sonunda karşılaştır.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l30",
        "display": "Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?",
        "spoken": "Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l31",
        "display": "Düşün bakalım... Evet: REM uykusunda!",
        "spoken": "Düşün bakalım... Evet: Rem uykusunda!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l32",
        "display": "Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!",
        "spoken": "Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Şimdi öğrendiklerimizi şarkıyla söyleyelim. Arkadaşlarım sahneye geliyor! Hazır mısın? Bir, iki, üç!",
        "spoken": "Şimdi öğrendiklerimizi şarkıyla söyleyelim. Arkadaşlarım sahneye geliyor! Hazır mısın? Bir, iki, üç!",
        "factIds": []
      }
    ]
  },
  {
    "id": "summary",
    "lines": [
      {
        "id": "l34",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l36",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!",
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
    "statement": "Uyurken vücut, beynin sağlıklı çalışmasını ve beden sağlığını desteklemek için çalışır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Vücut saati (sirkadiyen ritim), bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.",
    "numbers": [
      "24"
    ]
  },
  {
    "id": "f3",
    "statement": "İnsanda ana saat beyindedir; büyük bir sinir hücresi grubudur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Vücut saatini en çok ışık ve karanlık etkiler; yemek, stres, hareket, sosyal çevre ve sıcaklık da etkiler.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Akşam ana saat beyne daha çok melatonin üretmesini söyler; bu uyku getirir. Melatonin bir hormondur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Sabah vücut, uyanmaya yardım eden kortizol gibi hormonlar salgılar.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Uyurken beyin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Okul çağında bir uyku döngüsü yaklaşık 90 dakika sürer.",
    "numbers": [
      "90"
    ]
  },
  {
    "id": "f9",
    "statement": "REM olmayan uykunun üçüncü aşamasında vücut, büyüme ve gelişme için gereken hormonları salgılar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "REM uykusunda gözler göz kapaklarının altında hızlı hareket eder.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "En canlı rüyalar REM uykusunda görülür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "REM uykusunda kollar ve bacaklar hareket ettirilemez.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "REM uykusu öğrenme ve hafıza için önemlidir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Çocuklarda ve gençlerde uyku, büyümeyi ve gelişmeyi de destekler.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz, sinirli ya da keyifsiz olabilir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "6–12 yaş için önerilen günlük uyku 9–12 saattir.",
    "numbers": [
      "6",
      "12",
      "9"
    ]
  },
  {
    "id": "f19",
    "statement": "13–17 yaş için önerilen günlük uyku 8–10 saattir.",
    "numbers": [
      "13",
      "17",
      "8",
      "10"
    ]
  },
  {
    "id": "f20",
    "statement": "Her gün aynı saatte yatıp kalkmak daha iyi uykuya yardım eder.",
    "numbers": []
  },
  {
    "id": "f21",
    "statement": "Yatmadan en az 30 dakika önce elektronik cihazları kapatmak önerilir.",
    "numbers": [
      "30"
    ]
  },
  {
    "id": "f22",
    "statement": "Geceleri elektronik cihazların ışığı biyolojik saati şaşırtabilir.",
    "numbers": []
  },
  {
    "id": "f23",
    "statement": "Yatak odasının sessiz, rahatlatıcı ve serin olması önerilir.",
    "numbers": []
  },
  {
    "id": "f24",
    "statement": "Düzenli hareket etmek ve sağlıklı beslenmek daha iyi uykuya yardım eder.",
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
