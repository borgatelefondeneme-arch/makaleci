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
        "display": "Dağın tepesinde dev bir buz kütlesi var. Hiç kıpırdamıyor gibi görünüyor, ama aslında akıyor! Hem de bir nehir gibi, sadece çok çok yavaş.",
        "spoken": "Dağın tepesinde dev bir buz kütlesi var. Hiç kıpırdamıyor gibi görünüyor, ama aslında akıyor! Hem de bir nehir gibi, sadece çok çok yavaş.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Buz nasıl akar? Ve bu dev buzlar nereden gelir?",
        "spoken": "Buz nasıl akar? Ve bu dev buzlar nereden gelir?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün buzulların soğuk ve sessiz yolculuğuna katılıyoruz!",
        "spoken": "Bugün buzulların soğuk ve sessiz yolculuğuna katılıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Buzul nasıl oluşur? Nasıl hareket eder? Ve neden önemlidir?",
        "spoken": "Üç sorumuz var. Buzul nasıl oluşur? Nasıl hareket eder? Ve neden önemlidir?",
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
        "display": "ABD Ulusal Kar ve Buz Veri Merkezi NSIDC'ye göre buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.",
        "spoken": "ABD Ulusal Kar ve Buz Veri Merkezi En Es Ay Di Si'ye göre buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Her şey kar ile başlar. Her yıl yağan yeni kar katmanları, alttaki eski katmanları gömer ve sıkıştırır.",
        "spoken": "Her şey kar ile başlar. Her yıl yağan yeni kar katmanları, alttaki eski katmanları gömer ve sıkıştırır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l8",
        "display": "Yaklaşık bir yıl sonra kar, firn denen bir ara hale dönüşür: Artık kar değildir ama henüz buzul buzu da değildir.",
        "spoken": "Yaklaşık bir yıl sonra kar, firn denen bir ara hale dönüşür: Artık kar değildir ama henüz buzul buzu da değildir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Çoğu buzul için kardan buzul buzuna dönüşmek yüz yıldan uzun sürer!",
        "spoken": "Çoğu buzul için kardan buzul buzuna dönüşmek yüz yıldan uzun sürer!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Ben yüz yıl beklemeye dayanamam. Pilim çoktan biterdi!",
        "spoken": "Ben yüz yıl beklemeye dayanamam. Pilim çoktan biterdi!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Buzul buzu çok yoğunlaşıp içindeki kabarcıklardan arınınca mavi görünür. Çünkü buz, kırmızı ışığın küçük bir bölümünü soğurur.",
        "spoken": "Buzul buzu çok yoğunlaşıp içindeki kabarcıklardan arınınca mavi görünür. Çünkü buz, kırmızı ışığın küçük bir bölümünü soğurur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Çok yaşlı buzul buzunda buz kristalleri bir yetişkinin yumruğu kadar büyüyebilir!",
        "spoken": "Çok yaşlı buzul buzunda buz kristalleri bir yetişkinin yumruğu kadar büyüyebilir!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Peki buzul neden akar? Cevap: Kendi ağırlığı! Kalın bir buz katmanı o kadar ağırdır ki yer çekimi onu dışarıya ve aşağıya doğru akıtır.",
        "spoken": "Peki buzul neden akar? Cevap: Kendi ağırlığı! Kalın bir buz katmanı o kadar ağırdır ki yer çekimi onu dışarıya ve aşağıya doğru akıtır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Buzul iki yolla hareket eder. Birincisi, buzun kendi içinde yavaşça şekil değiştirmesidir. Buna iç deformasyon denir.",
        "spoken": "Buzul iki yolla hareket eder. Birincisi, buzun kendi içinde yavaşça şekil değiştirmesidir. Buna iç deformasyon denir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l15",
        "display": "İkincisi, tabandaki kayaların ve tortuların üzerinde kaymasıdır. Dik yamaçlardaki ince buzulların hareketinin çoğu bu kaymadan gelebilir.",
        "spoken": "İkincisi, tabandaki kayaların ve tortuların üzerinde kaymasıdır. Dik yamaçlardaki ince buzulların hareketinin çoğu bu kaymadan gelebilir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Buzulun hızlı aktığı yerlerde sürtünme dev çatlaklar açar. Bunlara yarık denir.",
        "spoken": "Buzulun hızlı aktığı yerlerde sürtünme dev çatlaklar açar. Bunlara yarık denir.",
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
        "id": "l17",
        "display": "Buzullar genelde yavaştır, ama bazen ani atılımlar yapar ve haftalarca günde birkaç metre ilerler.",
        "spoken": "Buzullar genelde yavaştır, ama bazen ani atılımlar yapar ve haftalarca günde birkaç metre ilerler.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l18",
        "display": "Rekor, Pakistan'daki Kutiah Buzulu'nda: 1953'te üç ayda 12 kilometreden fazla ilerledi. Günde ortalama yaklaşık 112 metre!",
        "spoken": "Rekor, Pakistan'daki Kutiah Buzulu'nda: bin dokuz yüz elli üçte üç ayda on iki kilometreden fazla ilerledi. Günde ortalama yaklaşık yüz on iki metre!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l19",
        "display": "Buzul olsam ben de bir gün koşuya çıkardım. Ama sonra yüz yıl dinlenirdim!",
        "spoken": "Buzul olsam ben de bir gün koşuya çıkardım. Ama sonra yüz yıl dinlenirdim!",
        "factIds": []
      },
      {
        "id": "l20",
        "display": "Buzullar dev su depolarıdır. NSIDC'ye göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde 68,7'sini depolar.",
        "spoken": "Buzullar dev su depolarıdır. En Es Ay Di Si'ye göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde altmış sekiz virgül yedisini depolar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l21",
        "display": "Buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir. Buzul buzunun çoğu ise Antarktika'dadır.",
        "spoken": "Buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir. Buzul buzunun çoğu ise Antarktika'dadır.",
        "factIds": [
          "f11",
          "f12"
        ]
      },
      {
        "id": "l22",
        "display": "Ama buzullar küçülüyor. Son 60 ila 100 yılda dünyadaki buzullar genel olarak geri çekildi.",
        "spoken": "Ama buzullar küçülüyor. Son altmış ila yüz yılda dünyadaki buzullar genel olarak geri çekildi.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l23",
        "display": "Şimdi sıra sende! Eldivenlerini giy ve bir avuç kar ya da dondurucudaki karlanmış buzdan al.",
        "spoken": "Şimdi sıra sende! Eldivenlerini giy ve bir avuç kar ya da dondurucudaki karlanmış buzdan al.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l24",
        "display": "Onu ellerinle iyice sıkıştır. Kar topu sertleşip buza benziyor mu? Buzulun ilk adımı da böyle bir sıkışmadır!",
        "spoken": "Onu ellerinle iyice sıkıştır. Kar topu sertleşip buza benziyor mu? Buzulun ilk adımı da böyle bir sıkışmadır!",
        "factIds": [
          "f3"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l25",
        "display": "Bunu biliyor muydun? Dünyada yalnızca iki buz tabakası var: Antarktika ve Grönland. İkisi birlikte Dünya'daki tatlı su buzunun yüzde 99'undan fazlasını içerir!",
        "spoken": "Bunu biliyor muydun? Dünyada yalnızca iki buz tabakası var: Antarktika ve Grönland. İkisi birlikte Dünya'daki tatlı su buzunun yüzde doksan dokuzundan fazlasını içerir!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "Hızlı soru! Kar ile buzul buzu arasındaki ara hale ne denir?",
        "spoken": "Hızlı soru! Kar ile buzul buzu arasındaki ara hale ne denir?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l27",
        "display": "Düşün bakalım... Evet: firn!",
        "spoken": "Düşün bakalım... Evet: firn!",
        "factIds": [
          "f3"
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
        "display": "Abone olmayı ve zili açmayı unutma. Sıcak bir şeyler iç, görüşürüz!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Sıcak bir şeyler iç, görüşürüz!",
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
    "statement": "Buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Buzullar karada oluşur ve yüzyıllar boyunca sıkışarak buza dönüşen yağmış kardan yapılır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Her yıl yeni kar katmanları öncekileri gömer ve sıkıştırır; yaklaşık bir yıl sonra kar, kar ile buzul buzu arasında bir ara hal olan firne dönüşür; çoğu buzul için bu süreç yüz yıldan uzun sürer.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Çok yaşlı buzul buzunda kristaller bir yetişkin yumruğu büyüklüğüne ulaşabilir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Buzul buzu çok yoğunlaşıp kabarcıklardan arınınca çoğu zaman mavi görünür; buz kırmızı ışığın küçük bir bölümünü soğurur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Buzul kendi ağırlığının basıncıyla dışarıya ve aşağıya doğru akmaya başlar; kalın bir buz katmanının ağırlığı, yani buz kütlesine etki eden yer çekimi buzulları akıtır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Buzullar buzun iç deformasyonuyla ve tabandaki kayaların ve tortuların üzerinde kayarak hareket eder; dik yamaçlardaki ince, soğuk buzulların hareketinin çoğu bu taban kaymasından gelebilir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Yarıklar buzul buzundaki çatlaklardır; buzulun hızlı aktığı yerlerde sürtünme bu dev çatlakları oluşturur.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Buzullar ani atılımlar yaparak haftalarca, hatta aylarca günde birkaç metre ilerleyebilir; en hızlı atılım rekoru Pakistan'daki Kutiah Buzulu'nundur: 1953'te üç ayda 12 kilometreden fazla ilerledi, günde ortalama yaklaşık 112 metre.",
    "numbers": [
      "1953",
      "12",
      "112"
    ]
  },
  {
    "id": "f10",
    "statement": "ABD Jeoloji Araştırmaları Kurumu'na göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde 68,7'sini depolar.",
    "numbers": [
      "68.7"
    ]
  },
  {
    "id": "f11",
    "statement": "Dünyada yalnızca iki buz tabakası vardır: Antarktika ve Grönland buz tabakaları; ikisi birlikte Dünya'daki tatlı su buzunun yüzde 99'undan fazlasını içerir; buzul buzunun çoğu Antarktika'dadır.",
    "numbers": [
      "99"
    ]
  },
  {
    "id": "f12",
    "statement": "Dünyadaki buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Son 60 ila 100 yılda dünyadaki buzullar genel olarak geri çekildi; son birkaç on yılda buzullar giderek artan bir hızla küçülüyor, hatta yok oluyor.",
    "numbers": [
      "60",
      "100"
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
