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
        "display": "Sabah kumsalda bir kumdan kale yaptın. Öğleden sonra döndüğünde deniz kalenin üstüne kadar gelmiş! Deniz nasıl yer değiştirdi?",
        "spoken": "Sabah kumsalda bir kumdan kale yaptın. Öğleden sonra döndüğünde deniz kalenin üstüne kadar gelmiş! Deniz nasıl yer değiştirdi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l2",
        "display": "Bunun arkasında gökyüzündeki bir dev var: Ay!",
        "spoken": "Bunun arkasında gökyüzündeki bir dev var: Ay!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün denizin nefes alıp vermesinin sırrını çözüyoruz!",
        "spoken": "Bugün denizin nefes alıp vermesinin sırrını çözüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Gelgit nedir? Ay denizi nasıl çeker? Ve Güneş'in bu işte rolü ne?",
        "spoken": "Üç sorumuz var. Gelgit nedir? Ay denizi nasıl çeker? Ve Güneş'in bu işte rolü ne?",
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
        "display": "National Geographic'e göre yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır. Alçak gelgit ise suyun en uzağa çekildiği an.",
        "spoken": "Neşınıl Ciyogrefik'e göre yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır. Alçak gelgit ise suyun en uzağa çekildiği an.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l7",
        "display": "NASA'ya göre gelgitleri Ay'ın kütle çekimi yönlendirir.",
        "spoken": "Nasa'ya göre gelgitleri Ay'ın kütle çekimi yönlendirir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Kütle çekimi, cisimlerin birbirini kendine çekmesidir. Ay, Dünya'yı ve okyanusları kendine doğru çeker.",
        "spoken": "Kütle çekimi, cisimlerin birbirini kendine çekmesidir. Ay, Dünya'yı ve okyanusları kendine doğru çeker.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l9",
        "display": "Dünya'nın Ay'a en yakın tarafı bu çekimi en güçlü hisseder. Orada okyanus Ay'a doğru kabarır.",
        "spoken": "Dünya'nın Ay'a en yakın tarafı bu çekimi en güçlü hisseder. Orada okyanus Ay'a doğru kabarır.",
        "factIds": [
          "f2",
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Beni de bir şey çeker: şarj aleti. Gördüğüm an ona doğru kabarırım!",
        "spoken": "Beni de bir şey çeker: şarj aleti. Gördüğüm an ona doğru kabarırım!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Ama işin ilginç yanı şu: Okyanus, Ay'dan en uzak tarafta da kabarır!",
        "spoken": "Ama işin ilginç yanı şu: Okyanus, Ay'dan en uzak tarafta da kabarır!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Orada Dünya'nın dönüşünden doğan kuvvet, Ay'ın çekiminden daha güçlüdür. Böylece Dünya'nın iki yanında iki kabarıklık oluşur.",
        "spoken": "Orada Dünya'nın dönüşünden doğan kuvvet, Ay'ın çekiminden daha güçlüdür. Böylece Dünya'nın iki yanında iki kabarıklık oluşur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Bu kabarıklıklar yüksek gelgitlerdir. Aralarındaki alçak noktalarda ise alçak gelgit olur.",
        "spoken": "Bu kabarıklıklar yüksek gelgitlerdir. Aralarındaki alçak noktalarda ise alçak gelgit olur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Dünya döndükçe kıyılar bu kabarıklıklardan ve alçak noktalardan sırayla geçer. Kıyıdaki biri suyun yükselip alçaldığını görür.",
        "spoken": "Dünya döndükçe kıyılar bu kabarıklıklardan ve alçak noktalardan sırayla geçer. Kıyıdaki biri suyun yükselip alçaldığını görür.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "NASA'ya göre çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur. Bir yüksek gelgitten ötekine 12 saatten biraz fazla geçer.",
        "spoken": "Nasa'ya göre çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur. Bir yüksek gelgitten ötekine on iki saatten biraz fazla geçer.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Yani deniz günde iki kez gelir, iki kez gider. Benim gibi: şarja git, şarjdan gel!",
        "spoken": "Yani deniz günde iki kez gelir, iki kez gider. Benim gibi: şarja git, şarjdan gel!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l17",
        "display": "Peki Güneş? National Geographic'e göre Güneş'in çekimi de gelgitlerde küçük bir rol oynar.",
        "spoken": "Peki Güneş? Neşınıl Ciyogrefik'e göre Güneş'in çekimi de gelgitlerde küçük bir rol oynar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Güneş, Ay'dan yaklaşık 390 kat daha uzaktır. Bu yüzden etkisi Ay'ınkinden azdır.",
        "spoken": "Güneş, Ay'dan yaklaşık üç yüz doksan kat daha uzaktır. Bu yüzden etkisi Ay'ınkinden azdır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Güneş ile Ay'ın çekimleri birleşince bahar gelgiti denen olağanüstü yüksek gelgitler olur.",
        "spoken": "Güneş ile Ay'ın çekimleri birleşince bahar gelgiti denen olağanüstü yüksek gelgitler olur.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Güneş, Ay'a dik açıda durunca ise kocakarı gelgiti denen orta düzeyde gelgitler oluşur.",
        "spoken": "Güneş, Ay'a dik açıda durunca ise kocakarı gelgiti denen orta düzeyde gelgitler oluşur.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Yüksek ve alçak gelgit arasındaki yükseklik farkına gelgit genliği denir.",
        "spoken": "Yüksek ve alçak gelgit arasındaki yükseklik farkına gelgit genliği denir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Gelgitin yüksekliği her kıyıda aynı değildir. Geniş bir kumsal ya da kayalık bir koy, kıyının açığındaki suyun derinliği bu yüksekliği etkiler.",
        "spoken": "Gelgitin yüksekliği her kıyıda aynı değildir. Geniş bir kumsal ya da kayalık bir koy, kıyının açığındaki suyun derinliği bu yüksekliği etkiler.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l23",
        "display": "Alçak gelgitte kayaların arasında küçük su birikintileri kalır. Bunlara gelgit havuzu denir.",
        "spoken": "Alçak gelgitte kayaların arasında küçük su birikintileri kalır. Bunlara gelgit havuzu denir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! Bir yetişkinle deniz kıyısındaysan, suyun bittiği yere bir taş koy ve saati not et.",
        "spoken": "Şimdi sıra sende! Bir yetişkinle deniz kıyısındaysan, suyun bittiği yere bir taş koy ve saati not et.",
        "factIds": [
          "f5",
          "f7"
        ]
      },
      {
        "id": "l25",
        "display": "Birkaç saat sonra tekrar bak: su taşa yaklaştı mı, uzaklaştı mı? Asla tek başına suya girme ve yükselen suya karşı dikkatli ol.",
        "spoken": "Birkaç saat sonra tekrar bak: su taşa yaklaştı mı, uzaklaştı mı? Asla tek başına suya girme ve yükselen suya karşı dikkatli ol.",
        "factIds": [
          "f5",
          "f6"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l26",
        "display": "Bunu biliyor muydun? NASA'ya göre yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz. Deniz, Ay'ı biraz geriden izler!",
        "spoken": "Bunu biliyor muydun? Nasa'ya göre yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz. Deniz, Ay'ı biraz geriden izler!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Güneş ile Ay'ın çekimleri birleşince oluşan çok yüksek gelgitin adı neydi?",
        "spoken": "Hızlı soru! Güneş ile Ay'ın çekimleri birleşince oluşan çok yüksek gelgitin adı neydi?",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: bahar gelgiti!",
        "spoken": "Düşün bakalım... Evet: bahar gelgiti!",
        "factIds": [
          "f9"
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
        "display": "Abone olmayı ve zili açmayı unutma. Bu gece Ay'a bir selam ver!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bu gece Ay'a bir selam ver!",
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
    "statement": "Gelgitleri Ay'ın kütle çekimi yönlendirir; okyanus gelgitleri Güneş ve Ay'ın Dünya okyanuslarına uyguladığı çekimden doğar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Dünya'nın Ay'a en yakın tarafı Ay'ın çekimini en güçlü hisseder.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Okyanuslar hem Ay'a en yakın tarafta hem de Ay'dan en uzak tarafta kabarır; Ay'dan uzak tarafta Dünya'nın dönüşünden doğan kuvvet Ay'ın çekiminden güçlüdür.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Bu kabarıklıklar yüksek gelgitleri oluşturur; alçak noktalar alçak gelgitlerin olduğu yerlerdir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır; alçak gelgit suyun en uzağa çekildiği andır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kıyıdaki bir gözlemci kabarıklıklardan geçerken suyun yükseldiğini, alçak noktalardan geçerken alçaldığını görür.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur; bir yüksek gelgitten ötekine geçen süre 12 saatten biraz fazladır.",
    "numbers": [
      "12"
    ]
  },
  {
    "id": "f8",
    "statement": "Güneş'in çekimi de gelgitlerde küçük bir rol oynar; Güneş, Ay'dan yaklaşık 390 kat daha uzaktır.",
    "numbers": [
      "390"
    ]
  },
  {
    "id": "f9",
    "statement": "Güneş ile Ay'ın çekimleri birleşince bahar gelgiti denen olağanüstü yüksek gelgitler olur; Güneş Ay'a dik açıda olunca orta düzeyde, kocakarı gelgiti denen gelgitler olur.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Yüksek gelgit ile alçak gelgit arasındaki yükseklik farkına gelgit genliği denir.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Birçok kıyıda gelgitler gelgit havuzları oluşturur; bu küçük su birikintileri alçak gelgitte kayaların arasında kalır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Geniş kumsal ya da kayalık koy gibi kıyı özellikleri ve kıyı açığındaki suyun derinliği gelgitlerin yüksekliğini etkiler.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz.",
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
