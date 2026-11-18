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
        "display": "Sabah perdeyi açtığında yüzüne vuran o ışık, aslında yaklaşık 8 dakika 20 saniye önce Güneş'ten yola çıktı!",
        "spoken": "Sabah perdeyi açtığında yüzüne vuran o ışık, aslında yaklaşık sekiz dakika yirmi saniye önce Güneş'ten yola çıktı!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l2",
        "display": "Peki Güneş bu ışığı nasıl üretiyor? İçinde ateş mi yanıyor?",
        "spoken": "Peki Güneş bu ışığı nasıl üretiyor? İçinde ateş mi yanıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün en yakın yıldızımızın kalbine yolculuk ediyoruz!",
        "spoken": "Bugün en yakın yıldızımızın kalbine yolculuk ediyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Güneş neyden yapılmıştır? Işığını nasıl üretir? Ve içinde hangi katmanlar vardır?",
        "spoken": "Üç sorumuz var. Güneş neyden yapılmıştır? Işığını nasıl üretir? Ve içinde hangi katmanlar vardır?",
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
        "display": "NASA'ya göre yıldız, sıcak ve parlayan bir gaz topudur. Güneş de bir yıldızdır.",
        "spoken": "Nasa'ya göre yıldız, sıcak ve parlayan bir gaz topudur. Güneş de bir yıldızdır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
        "spoken": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Güneş'te sıradan bir ateş yanmaz. Işığın sırrı çekirdekte saklı: nükleer kaynaşma, yani füzyon!",
        "spoken": "Güneş'te sıradan bir ateş yanmaz. Işığın sırrı çekirdekte saklı: nükleer kaynaşma, yani füzyon!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Çekirdekte hidrojen atomları öyle büyük bir kuvvetle çarpışır ki kaynaşıp yeni bir elemente, helyuma dönüşür.",
        "spoken": "Çekirdekte hidrojen atomları öyle büyük bir kuvvetle çarpışır ki kaynaşıp yeni bir elemente, helyuma dönüşür.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Bu kaynaşma, Güneş'in ısısına ve ışığına güç verir. Çekirdekte sıcaklık yaklaşık 15 milyon santigrat derecedir!",
        "spoken": "Bu kaynaşma, Güneş'in ısısına ve ışığına güç verir. Çekirdekte sıcaklık yaklaşık on beş milyon santigrat derecedir!",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Benim içimde de enerji var ama füzyon değil, sadece bir pil. Neyse ki ben de parlıyorum, en azından anten yıldızım!",
        "spoken": "Benim içimde de enerji var ama füzyon değil, sadece bir pil. Neyse ki ben de parlıyorum, en azından anten yıldızım!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Güneş'in içi katmanlıdır: çekirdek, ışınım bölgesi ve konveksiyon bölgesi.",
        "spoken": "Güneş'in içi katmanlıdır: çekirdek, ışınım bölgesi ve konveksiyon bölgesi.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık 170.000 yıl sürer!",
        "spoken": "Enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık yüz yetmiş bin yıl sürer!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Konveksiyon bölgesinde dev sıcak plazma kabarcıkları, kaynayan bir tencere gibi yukarı doğru yükselir.",
        "spoken": "Konveksiyon bölgesinde dev sıcak plazma kabarcıkları, kaynayan bir tencere gibi yukarı doğru yükselir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Güneş'in yüzeyi dediğimiz bölüme fotosfer denir. Sıcaklığı yaklaşık 5.500 santigrat derecedir.",
        "spoken": "Güneş'in yüzeyi dediğimiz bölüme fotosfer denir. Sıcaklığı yaklaşık beş bin beş yüz santigrat derecedir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Yüzeyin üstünde ince kromosfer ve dev korona vardır. İşin garibi, korona 2 milyon santigrat dereceye ulaşır; yani yüzeyden çok daha sıcaktır!",
        "spoken": "Yüzeyin üstünde ince kromosfer ve dev korona vardır. İşin garibi, korona iki milyon santigrat dereceye ulaşır; yani yüzeyden çok daha sıcaktır!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Koronadan ses üstü hızlarla kaçan maddeye güneş rüzgârı denir.",
        "spoken": "Koronadan ses üstü hızlarla kaçan maddeye güneş rüzgârı denir.",
        "factIds": [
          "f9"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Güneş'in yüzeyinde bazen daha karanlık lekeler görülür. Bunlar, manyetik alan çizgilerinin yoğunlaştığı daha serin bölgelerdir.",
        "spoken": "Güneş'in yüzeyinde bazen daha karanlık lekeler görülür. Bunlar, manyetik alan çizgilerinin yoğunlaştığı daha serin bölgelerdir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l19",
        "display": "Güneş lekelerinin sayısı, Güneş'in doğal 11 yıllık döngüsüyle artıp azalır.",
        "spoken": "Güneş lekelerinin sayısı, Güneş'in doğal on bir yıllık döngüsüyle artıp azalır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l20",
        "display": "Güneş patlamaları ve koronal kütle atımları ise Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.",
        "spoken": "Güneş patlamaları ve koronal kütle atımları ise Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l21",
        "display": "Güneş, Dünya'dan yaklaşık 100 kat daha geniştir. Yine de evrende ortalama büyüklükte bir yıldızdır!",
        "spoken": "Güneş, Dünya'dan yaklaşık yüz kat daha geniştir. Yine de evrende ortalama büyüklükte bir yıldızdır!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l22",
        "display": "Güneş yaklaşık 4,6 milyar yıl önce oluştu. Ömrünün yarısını henüz doldurmadı ve yaklaşık 5 milyar yıl daha parlayacak.",
        "spoken": "Güneş yaklaşık dört virgül altı milyar yıl önce oluştu. Ömrünün yarısını henüz doldurmadı ve yaklaşık beş milyar yıl daha parlayacak.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l23",
        "display": "Beş milyar yıl mı? Benim garantim sadece iki yıl!",
        "spoken": "Beş milyar yıl mı? Benim garantim sadece iki yıl!",
        "factIds": []
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! İki beyaz karton al. Birine iğneyle küçük bir delik aç.",
        "spoken": "Şimdi sıra sende! İki beyaz karton al. Birine iğneyle küçük bir delik aç.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l25",
        "display": "Güneşe sırtını dön, delikli kartonu tut ve ışığı diğer kartona düşür. Küçük bir Güneş görüntüsü göreceksin. Ama Güneş'e asla doğrudan bakma!",
        "spoken": "Güneşe sırtını dön, delikli kartonu tut ve ışığı diğer kartona düşür. Küçük bir Güneş görüntüsü göreceksin. Ama Güneş'e asla doğrudan bakma!",
        "factIds": [
          "f15"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l26",
        "display": "Bunu biliyor muydun? NASA'ya göre Güneş, en büyük gezegen Jüpiter'den bile yaklaşık 10 kat daha geniştir!",
        "spoken": "Bunu biliyor muydun? Nasa'ya göre Güneş, en büyük gezegen Jüpiter'den bile yaklaşık on kat daha geniştir!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Güneş'in çekirdeğinde hidrojen hangi elemente dönüşür?",
        "spoken": "Hızlı soru! Güneş'in çekirdeğinde hidrojen hangi elemente dönüşür?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: helyum!",
        "spoken": "Düşün bakalım... Evet: helyum!",
        "factIds": [
          "f3"
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
        "display": "Abone olmayı ve zili açmayı unutma. Güneşli günler dilerim!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Güneşli günler dilerim!",
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
    "statement": "Yıldız, sıcak ve parlayan bir gaz topudur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Çekirdekteki nükleer tepkimelerde hidrojen kaynaşarak helyuma dönüşür ve bu, Güneş'in ısısına ve ışığına güç verir; hidrojen atomları öyle bir kuvvetle çarpışır ki kelimenin tam anlamıyla kaynaşıp yeni bir element olan helyuma dönüşür.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir.",
    "numbers": [
      "15"
    ]
  },
  {
    "id": "f5",
    "statement": "Güneş'in iç bölgeleri çekirdek, ışınım bölgesi ve konveksiyon bölgesidir; enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık 170.000 yıl sürer.",
    "numbers": [
      "170.000"
    ]
  },
  {
    "id": "f6",
    "statement": "Konveksiyon bölgesinde büyük sıcak plazma kabarcıkları fotosfere doğru yükselir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Güneş'in yüzeyi denen bölüm fotosferdir; sıcaklığı yaklaşık 5.500 santigrat dereceye ulaşır.",
    "numbers": [
      "5.500"
    ]
  },
  {
    "id": "f8",
    "statement": "Güneş'in yüzeyinin üstünde ince kromosfer ve dev korona bulunur; korona 2 milyon santigrat dereceye ulaşır, fotosferden çok daha sıcaktır.",
    "numbers": [
      "2"
    ]
  },
  {
    "id": "f9",
    "statement": "Madde koronadan ses üstü hızlarla ayrılınca güneş rüzgârı olur.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Güneş lekeleri, manyetik alan çizgilerinin yoğunlaşmasıyla oluşan daha serin bölgelerdir; sayıları Güneş'in doğal 11 yıllık döngüsüyle artıp azalır.",
    "numbers": [
      "11"
    ]
  },
  {
    "id": "f11",
    "statement": "Güneş patlamaları ve koronal kütle atımları, Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Güneş o kadar uzaktadır ki ışığının bize ulaşması yaklaşık 8 dakika 20 saniye sürer.",
    "numbers": [
      "8",
      "20"
    ]
  },
  {
    "id": "f13",
    "statement": "Güneş, Dünya'dan yaklaşık 100 kat, en büyük gezegen Jüpiter'den yaklaşık 10 kat daha geniştir; ama ortalama büyüklükte bir yıldızdır.",
    "numbers": [
      "100",
      "10"
    ]
  },
  {
    "id": "f14",
    "statement": "Güneş yaklaşık 4,6 milyar yıl önce oluştu; ömrünün yarısından biraz daha azını geçirdi ve beyaz cüceye dönüşmeden önce yaklaşık 5 milyar yıl daha yaşayacak.",
    "numbers": [
      "4.6",
      "5"
    ]
  },
  {
    "id": "f15",
    "statement": "Güneş'e çok özel koruyucu gözlük olmadan asla doğrudan bakılmamalıdır.",
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
