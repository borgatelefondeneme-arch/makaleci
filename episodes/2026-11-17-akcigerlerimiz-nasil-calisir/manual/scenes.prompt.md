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
        "display": "Bu cümleyi dinlerken farkında olmadan birkaç kez nefes aldın. KidsHealth'e göre günde binlerce kez nefes alıyoruz!",
        "spoken": "Bu cümleyi dinlerken farkında olmadan birkaç kez nefes aldın. Kids Helt'e göre günde binlerce kez nefes alıyoruz!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l2",
        "display": "Peki içine çektiğin hava nereye gider? Ve vücudun onunla ne yapar?",
        "spoken": "Peki içine çektiğin hava nereye gider? Ve vücudun onunla ne yapar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir hava molekülü olup akciğerlerin içine yolculuk ediyoruz! Ben zaten havalı bir robotum, hazırım!",
        "spoken": "Bugün bir hava molekülü olup akciğerlerin içine yolculuk ediyoruz! Ben zaten havalı bir robotum, hazırım!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Hava hangi yollardan geçer? Oksijen kana nasıl karışır? Ve nefes almamızı hangi kas sağlar?",
        "spoken": "Üç sorumuz var. Hava hangi yollardan geçer? Oksijen kana nasıl karışır? Ve nefes almamızı hangi kas sağlar?",
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
        "display": "Solunum sistemi; burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.",
        "spoken": "Solunum sistemi; burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Hava önce burundan ya da ağızdan girer. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre burası havayı ısıtır ve nemlendirir.",
        "spoken": "Hava önce burundan ya da ağızdan girer. Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'ye göre burası havayı ısıtır ve nemlendirir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.",
        "spoken": "Çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Burnunda silia denen minik tüyler vardır. Silialar tozu ve parçacıkları süzer.",
        "spoken": "Burnunda silia denen minik tüyler vardır. Silialar tozu ve parçacıkları süzer.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Soluk borusu da silialarla kaplıdır. Bu tüyler, yabancı parçacıkları süpürge gibi dışarı iter.",
        "spoken": "Soluk borusu da silialarla kaplıdır. Bu tüyler, yabancı parçacıkları süpürge gibi dışarı iter.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Benim de bir hava filtrem var. Ama ben onu ayda bir değiştiriyorum, sen ise kendi kendini temizliyorsun!",
        "spoken": "Benim de bir hava filtrem var. Ama ben onu ayda bir değiştiriyorum, sen ise kendi kendini temizliyorsun!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Soluk borusu aşağıda ikiye ayrılır: sağ ve sol bronşlar. Kıkırdak denen sert halkalar bu tüpleri açık tutar.",
        "spoken": "Soluk borusu aşağıda ikiye ayrılır: sağ ve sol bronşlar. Kıkırdak denen sert halkalar bu tüpleri açık tutar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Akciğerlerin içinde bronşlar binlerce ince tüpe ayrılır. Bunlara bronşiyol denir.",
        "spoken": "Akciğerlerin içinde bronşlar binlerce ince tüpe ayrılır. Bunlara bronşiyol denir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Ters dönmüş bir ağaç gibi: gövde soluk borusu, dallar bronşlar, ince dallar bronşiyoller.",
        "spoken": "Ters dönmüş bir ağaç gibi: gövde soluk borusu, dallar bronşlar, ince dallar bronşiyoller.",
        "factIds": [
          "f4",
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Her bronşiyolün ucunda minik hava kesecikleri vardır: alveoller.",
        "spoken": "Her bronşiyolün ucunda minik hava kesecikleri vardır: alveoller.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "NIH'ye göre akciğerlerinde yaklaşık 150 milyon alveol vardır!",
        "spoken": "En Ay Eyç'ye göre akciğerlerinde yaklaşık yüz elli milyon alveol vardır!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Her alveol, kılcal damar denen minik kan damarlarından bir ağla sarılıdır.",
        "spoken": "Her alveol, kılcal damar denen minik kan damarlarından bir ağla sarılıdır.",
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
        "display": "İşte büyük takas burada olur! Oksijen alveollerden kılcal damarlara, yani kana geçer.",
        "spoken": "İşte büyük takas burada olur! Oksijen alveollerden kılcal damarlara, yani kana geçer.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Alyuvarlar oksijeni yakalar ve vücudundaki hücrelere taşır.",
        "spoken": "Alyuvarlar oksijeni yakalar ve vücudundaki hücrelere taşır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Karbondioksit ise ters yöne gider: kandan alveollerin içindeki havaya geçer. Sen de onu nefesle dışarı verirsin.",
        "spoken": "Karbondioksit ise ters yöne gider: kandan alveollerin içindeki havaya geçer. Sen de onu nefesle dışarı verirsin.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Ben karbondioksit vermem. Olsa olsa biraz sıcak hava üflerim, o da fanımdan!",
        "spoken": "Ben karbondioksit vermem. Olsa olsa biraz sıcak hava üflerim, o da fanımdan!",
        "factIds": []
      },
      {
        "id": "l22",
        "display": "Peki havayı içeri ne çeker? Diyafram! Diyafram, göğüs ile karın arasındaki bir kastır.",
        "spoken": "Peki havayı içeri ne çeker? Diyafram! Diyafram, göğüs ile karın arasındaki bir kastır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Nefes alırken diyafram karnına doğru aşağı iner. Nefes verirken yukarı çıkar ve göğüs kasları gevşer.",
        "spoken": "Nefes alırken diyafram karnına doğru aşağı iner. Nefes verirken yukarı çıkar ve göğüs kasları gevşer.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Alveollerde sürfaktan denen bir madde de vardır. Sürfaktan, akciğerlerin daha kolay şişmesine yardım eder ve nefes almayı kolaylaştırır.",
        "spoken": "Alveollerde sürfaktan denen bir madde de vardır. Sürfaktan, akciğerlerin daha kolay şişmesine yardım eder ve nefes almayı kolaylaştırır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Sırt üstü uzan ve bir elini karnına, diğerini göğsüne koy.",
        "spoken": "Şimdi sıra sende! Sırt üstü uzan ve bir elini karnına, diğerini göğsüne koy.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l26",
        "display": "Yavaşça burnundan derin bir nefes al, sonra ver. Hangi elin daha çok hareket ediyor? Başın dönerse hemen normal nefese dön.",
        "spoken": "Yavaşça burnundan derin bir nefes al, sonra ver. Hangi elin daha çok hareket ediyor? Başın dönerse hemen normal nefese dön.",
        "factIds": [
          "f10"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l27",
        "display": "Bunu biliyor muydun? Her alveol bir kılcal damar ağıyla sarılıdır. Yani akciğerlerinde 150 milyon minik takas noktası var!",
        "spoken": "Bunu biliyor muydun? Her alveol bir kılcal damar ağıyla sarılıdır. Yani akciğerlerinde yüz elli milyon minik takas noktası var!",
        "factIds": [
          "f6",
          "f7"
        ]
      },
      {
        "id": "l28",
        "display": "Benim bir tane bile yok. Ama şarj kablomda iki ucum var, sayılır mı?",
        "spoken": "Benim bir tane bile yok. Ama şarj kablomda iki ucum var, sayılır mı?",
        "factIds": []
      },
      {
        "id": "l29",
        "display": "Hızlı soru! Nefes alırken aşağı inen kasın adı neydi?",
        "spoken": "Hızlı soru! Nefes alırken aşağı inen kasın adı neydi?",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l30",
        "display": "Düşün bakalım... Evet: diyafram!",
        "spoken": "Düşün bakalım... Evet: diyafram!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l31",
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
        "id": "l32",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Abone olmayı ve zili açmayı unutma. Derin bir nefes al, görüşürüz!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Derin bir nefes al, görüşürüz!",
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
    "statement": "Solunum sistemi burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Hava vücuda burundan ya da ağızdan girer; bunlar havayı nemlendirip ısıtır, çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Burundaki silia denen minik tüyler tozu ve parçacıkları süzer; soluk borusu da silialarla kaplıdır ve bunlar yabancı parçacıkları hava yolundan dışarı süpürür.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Soluk borusu aşağıda sol ve sağ iki tüpe, bronşlara ayrılır; kıkırdak denen sert doku halkaları bronş tüplerini açık tutar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Akciğerlerin içinde bronşlar bronşiyol denen binlerce ince tüpe ayrılır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Bronşiyoller alveol denen minik hava keseciği kümelerinde son bulur; akciğerlerde yaklaşık 150 milyon alveol vardır.",
    "numbers": [
      "150"
    ]
  },
  {
    "id": "f7",
    "statement": "Her alveol kılcal damar denen minik kan damarlarından bir ağla sarılıdır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Oksijen alveollerden, alveol duvarlarını kaplayan kılcal damarlar yoluyla kana geçer; alyuvarlar oksijeni alıp vücut hücrelerine taşır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Karbondioksit kandan alveollerin içindeki havaya geçer.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Diyafram göğüs ile karın arasındaki bir kastır; nefes alırken karına doğru aşağı iner, nefes verirken yukarı çıkar ve göğüs duvarı kasları gevşer.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Sürfaktan, nefes alırken akciğerlerin daha kolay şişmesine yardım ederek nefes almak için gereken işi azaltır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Solunum sistemi sayesinde günde binlerce kez nefes alırız.",
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
