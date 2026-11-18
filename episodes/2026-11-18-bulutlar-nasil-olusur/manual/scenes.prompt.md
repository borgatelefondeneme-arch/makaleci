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
        "display": "Gökyüzüne bak: pamuk gibi bulutlar süzülüyor. Ama bir bulutun içi aslında su doludur. Peki nasıl düşmüyor?",
        "spoken": "Gökyüzüne bak: pamuk gibi bulutlar süzülüyor. Ama bir bulutun içi aslında su doludur. Peki nasıl düşmüyor?",
        "factIds": [
          "f1",
          "f6"
        ]
      },
      {
        "id": "l2",
        "display": "Ve o bulutlar nereden çıkıp geliyor?",
        "spoken": "Ve o bulutlar nereden çıkıp geliyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir su damlacığıyla birlikte gökyüzüne yükseliyoruz!",
        "spoken": "Bugün bir su damlacığıyla birlikte gökyüzüne yükseliyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Bulut neyden yapılır? Nasıl oluşur? Ve neden bazen beyaz, bazen karanlıktır?",
        "spoken": "Üç sorumuz var. Bulut neyden yapılır? Nasıl oluşur? Ve neden bazen beyaz, bazen karanlıktır?",
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
        "display": "National Geographic'e göre bulutlar, havada toplanmış minik su damlacıkları ya da buz kristalleridir.",
        "spoken": "Neşınıl Ciyogrefik'e göre bulutlar, havada toplanmış minik su damlacıkları ya da buz kristalleridir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Her şey su buharıyla başlar. İngiltere'nin meteoroloji kurumu Met Office'e göre su buharı görünmezdir ve havada her zaman çevremizdedir.",
        "spoken": "Her şey su buharıyla başlar. İngiltere'nin meteoroloji kurumu Met Ofis'e göre su buharı görünmezdir ve havada her zaman çevremizdedir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Ama hava ancak belli bir miktar su buharı tutabilir. Fazlası olunca, hava doygun hale gelir ve bulut oluşur.",
        "spoken": "Ama hava ancak belli bir miktar su buharı tutabilir. Fazlası olunca, hava doygun hale gelir ve bulut oluşur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Ben de doygunum. Ama sudan değil, bilgiden! Bir de biraz şarjdan.",
        "spoken": "Ben de doygunum. Ama sudan değil, bilgiden! Bir de biraz şarjdan.",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Peki hava nasıl doygun hale gelir? Hava yükselince soğur.",
        "spoken": "Peki hava nasıl doygun hale gelir? Hava yükselince soğur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Sıcak hava, soğuk havadan daha çok su buharı tutabilir. Hava soğuyunca sanki bir sünger sıkılmış gibi olur.",
        "spoken": "Sıcak hava, soğuk havadan daha çok su buharı tutabilir. Hava soğuyunca sanki bir sünger sıkılmış gibi olur.",
        "factIds": [
          "f4"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Sıkılan süngerden ne çıkar? Su! Su buharı yoğuşur, yani gazdan sıvıya döner ve minik su damlacıkları oluşur.",
        "spoken": "Sıkılan süngerden ne çıkar? Su! Su buharı yoğuşur, yani gazdan sıvıya döner ve minik su damlacıkları oluşur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Bu damlacıklar havadaki minicik toz parçacıklarına tutunur. Bu parçacıklara yoğuşma çekirdeği denir: kil, tuz ya da kirletici zerreleri.",
        "spoken": "Bu damlacıklar havadaki minicik toz parçacıklarına tutunur. Bu parçacıklara yoğuşma çekirdeği denir: kil, tuz ya da kirletici zerreleri.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Bu damlacıklar çok ama çok küçüktür: çapları milimetrenin yüzde biri kadar.",
        "spoken": "Bu damlacıklar çok ama çok küçüktür: çapları milimetrenin yüzde biri kadar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "O kadar küçüktürler ki havada asılı kalırlar. İşte bu yüzden bulut düşmez.",
        "spoken": "O kadar küçüktürler ki havada asılı kalırlar. İşte bu yüzden bulut düşmez.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Ben de hafif olsam uçardım. Ama cin kuyruğum sayesinde zaten uçuyorum!",
        "spoken": "Ben de hafif olsam uçardım. Ama cin kuyruğum sayesinde zaten uçuyorum!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l17",
        "display": "Met Office'e göre bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus.",
        "spoken": "Met Ofis'e göre bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Stratus bulutları yatay ve katmanlıdır; gökyüzünü battaniye gibi örter.",
        "spoken": "Stratus bulutları yatay ve katmanlıdır; gökyüzünü battaniye gibi örter.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "Kümülüs bulutları büyük ve topaklıdır. National Geographic'e göre 12.000 metre yüksekliğe kadar uzanabilirler!",
        "spoken": "Kümülüs bulutları büyük ve topaklıdır. Neşınıl Ciyogrefik'e göre on iki bin metre yüksekliğe kadar uzanabilirler!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l20",
        "display": "Kümülonimbus bulutlarına fırtına bulutu da denir. Bunlar yağmur, gök gürültüsü ve şimşek üretir.",
        "spoken": "Kümülonimbus bulutlarına fırtına bulutu da denir. Bunlar yağmur, gök gürültüsü ve şimşek üretir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Bulutlar genellikle beyaz görünür, çünkü içlerindeki minik damlacıklar sıkı sıkıya dizilmiştir.",
        "spoken": "Bulutlar genellikle beyaz görünür, çünkü içlerindeki minik damlacıklar sıkı sıkıya dizilmiştir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Yağmur yaklaşınca bulutlar kararır. Çünkü su buharı topaklanarak yağmur damlalarına dönüşmeye başlar.",
        "spoken": "Yağmur yaklaşınca bulutlar kararır. Çünkü su buharı topaklanarak yağmur damlalarına dönüşmeye başlar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Damlacıklar ya da buz parçacıkları büyür, büyür ve sonunda yağış olarak yere düşer.",
        "spoken": "Damlacıklar ya da buz parçacıkları büyür, büyür ve sonunda yağış olarak yere düşer.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! Buzdolabından soğuk bir bardak su al ve masaya koy.",
        "spoken": "Şimdi sıra sende! Buzdolabından soğuk bir bardak su al ve masaya koy.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l25",
        "display": "Birkaç dakika bekle. Bardağın dışında damlacıklar beliriyor mu? Havadaki görünmez su buharı soğuk bardağa değince yoğuştu!",
        "spoken": "Birkaç dakika bekle. Bardağın dışında damlacıklar beliriyor mu? Havadaki görünmez su buharı soğuk bardağa değince yoğuştu!",
        "factIds": [
          "f2",
          "f4",
          "f5"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l26",
        "display": "Bunu biliyor muydun? Bulut damlacıkları o kadar küçüktür ki havada asılı kalır. Ama birleşip büyüyünce yağmur olarak düşerler.",
        "spoken": "Bunu biliyor muydun? Bulut damlacıkları o kadar küçüktür ki havada asılı kalır. Ama birleşip büyüyünce yağmur olarak düşerler.",
        "factIds": [
          "f6",
          "f10"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Su buharının gazdan sıvıya dönmesine ne denir?",
        "spoken": "Hızlı soru! Su buharının gazdan sıvıya dönmesine ne denir?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: yoğuşma!",
        "spoken": "Düşün bakalım... Evet: yoğuşma!",
        "factIds": [
          "f5"
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
        "display": "Abone olmayı ve zili açmayı unutma. Bugün gökyüzüne bir bak, hangi bulutu görüyorsun?",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bugün gökyüzüne bir bak, hangi bulutu görüyorsun?",
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
    "statement": "Bulutlar, atmosferde toplanmış görünür minik su damlacıkları ya da buz kristalleridir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Su buharı görünmezdir ve havada her zaman çevremizdedir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Bulutlar hava su buharıyla doygun hale gelince, yani havanın tutabileceğinden fazla su buharı olunca oluşur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Hava yükselince soğur; sıcak hava soğuk havadan daha çok su buharı tutabilir, bu yüzden hava kütlesinin sıcaklığını düşürmek bir süngeri sıkmaya benzer.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Su buharı yoğuşarak minik su damlacıklarına dönüşür ve bunlar küçük toz parçacıklarına tutunur; yoğuşma çekirdekleri, su buharının çevresinde yoğuştuğu mikroskobik kil, tuz ya da kirletici parçacıklarıdır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Bu su damlacıklarının çapı yalnızca milimetrenin yüzde biri kadardır; o kadar küçüktürler ki havada asılı kalırlar.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus; stratus bulutları yatay ve katmanlıdır; kümülüs bulutları büyük ve topaklıdır ve 12.000 metre yüksekliğe kadar uzanabilir.",
    "numbers": [
      "12.000"
    ]
  },
  {
    "id": "f8",
    "statement": "Kümülonimbus bulutlarına fırtına bulutu da denir; yağmur, gök gürültüsü ve şimşek üretirler.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Bulutlar genellikle beyaz görünür çünkü içlerindeki minik su damlacıkları sıkı sıkıya dizilidir; yağmur yaklaşınca bulutlar kararır çünkü su buharı yağmur damlalarına dönüşerek topaklanır.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Bulutu oluşturan su ya da buz parçacıkları büyüyerek yağış olarak yere düşen daha büyük parçacıklara dönüşebilir.",
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
