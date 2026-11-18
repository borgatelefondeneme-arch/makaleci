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
        "display": "Yerin altında, gün ışığının hiç ulaşmadığı dev salonlar var. Tavanlarından taş saçaklar sarkıyor. Bu salonları kim kazdı?",
        "spoken": "Yerin altında, gün ışığının hiç ulaşmadığı dev salonlar var. Tavanlarından taş saçaklar sarkıyor. Bu salonları kim kazdı?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l2",
        "display": "Cevap seni şaşırtabilir: Su! Hem de damla damla. Benim en korktuğum şey!",
        "spoken": "Cevap seni şaşırtabilir: Su! Hem de damla damla. Benim en korktuğum şey!",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün fenerimizi alıp bir mağaraya giriyoruz!",
        "spoken": "Bugün fenerimizi alıp bir mağaraya giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Su taşı nasıl oyar? Sarkıtlar ve dikitler nasıl oluşur? Ve başka hangi tür mağaralar vardır?",
        "spoken": "Üç sorumuz var. Su taşı nasıl oyar? Sarkıtlar ve dikitler nasıl oluşur? Ve başka hangi tür mağaralar vardır?",
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
        "display": "ABD Milli Parklar Servisi'ne göre mağaraların çoğu kireçtaşı, mermer ve dolomit gibi kayaçlarda oluşur. Bunlara erime mağarası denir.",
        "spoken": "ABD Milli Parklar Servisi'ne göre mağaraların çoğu kireçtaşı, mermer ve dolomit gibi kayaçlarda oluşur. Bunlara erime mağarası denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bu kayaçlar çözünür, çünkü yağmur suyu hafifçe asidiktir.",
        "spoken": "Bu kayaçlar çözünür, çünkü yağmur suyu hafifçe asidiktir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Havadaki karbondioksit suda çözünür ve karbonik asit oluşur. Mağaraları oyan asit genellikle budur.",
        "spoken": "Havadaki karbondioksit suda çözünür ve karbonik asit oluşur. Mağaraları oyan asit genellikle budur.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Asitli su kayaçtaki çatlaklardan sızar ve kayayı çok yavaş çözer. Su, çözünen kayayı ve tortuları aşağı taşıdıkça düdenler genişler.",
        "spoken": "Asitli su kayaçtaki çatlaklardan sızar ve kayayı çok yavaş çözer. Su, çözünen kayayı ve tortuları aşağı taşıdıkça düdenler genişler.",
        "factIds": [
          "f2",
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Kireçtaşı gibi çözünebilir kayaçların olduğu bu tür bölgelere karst denir.",
        "spoken": "Kireçtaşı gibi çözünebilir kayaçların olduğu bu tür bölgelere karst denir.",
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
        "id": "l11",
        "display": "Peki bu iş ne kadar sürer? Jeologlara göre içinden dere akan bir mağara geçidi yılda en fazla yaklaşık 1 milimetre büyüyebilir.",
        "spoken": "Peki bu iş ne kadar sürer? Jeologlara göre içinden dere akan bir mağara geçidi yılda en fazla yaklaşık bir milimetre büyüyebilir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Bu yüzden birçok mağara yüz binlerce, hatta milyonlarca yaşındadır!",
        "spoken": "Bu yüzden birçok mağara yüz binlerce, hatta milyonlarca yaşındadır!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l13",
        "display": "Ben bir milimetre ilerlemek için bile acele ederim. Mağaralar ise hiç acele etmez!",
        "spoken": "Ben bir milimetre ilerlemek için bile acele ederim. Mağaralar ise hiç acele etmez!",
        "factIds": []
      },
      {
        "id": "l14",
        "display": "Mağarada tavandan aşağı sarkan taş saçaklara sarkıt denir. Buz saçaklarına ya da havuçlara benzerler.",
        "spoken": "Mağarada tavandan aşağı sarkan taş saçaklara sarkıt denir. Buz saçaklarına ya da havuçlara benzerler.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l15",
        "display": "Sarkıtlar genellikle kalsit denen mineralden oluşur. Adları Yunancada 'damla damla sızmak' anlamına gelen bir kelimeden gelir.",
        "spoken": "Sarkıtlar genellikle kalsit denen mineralden oluşur. Adları Yunancada 'damla damla sızmak' anlamına gelen bir kelimeden gelir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l16",
        "display": "Sarkıttan yere damlayan su da yerde birikip yukarı doğru tümsekler yapar. Bunlara dikit denir.",
        "spoken": "Sarkıttan yere damlayan su da yerde birikip yukarı doğru tümsekler yapar. Bunlara dikit denir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l17",
        "display": "Bir dikit sarkıtla birleşince sütun oluşur. Sütunlar bazen 20 metreyi aşan yüksekliğe ulaşabilir!",
        "spoken": "Bir dikit sarkıtla birleşince sütun oluşur. Sütunlar bazen yirmi metreyi aşan yüksekliğe ulaşabilir!",
        "factIds": [
          "f10"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Her mağara suyla çözünerek oluşmaz. Lav, binlerce derece sıcaktır ve bir nehir gibi akabilir.",
        "spoken": "Her mağara suyla çözünerek oluşmaz. Lav, binlerce derece sıcaktır ve bir nehir gibi akabilir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l19",
        "display": "Erimiş lav geçip gidince geride boş bir tünel kalır. Buna lav tüpü denir.",
        "spoken": "Erimiş lav geçip gidince geride boş bir tünel kalır. Buna lav tüpü denir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l20",
        "display": "Deniz mağaraları ise dalgaların kayaları aşındırmasıyla oluşur. Dalgalar da benim gibi hiç yorulmaz!",
        "spoken": "Deniz mağaraları ise dalgaların kayaları aşındırmasıyla oluşur. Dalgalar da benim gibi hiç yorulmaz!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l21",
        "display": "Bir buzulun kenarındaki erime de buzun içinde küçük mağaralar açabilir. Buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.",
        "spoken": "Bir buzulun kenarındaki erime de buzun içinde küçük mağaralar açabilir. Buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l22",
        "display": "Mağaralar canlılarla da doludur. Lav mağaralarında birçok küçük, sıra dışı hayvan yaşar; bazılarında büyük yarasa tünekleri vardır.",
        "spoken": "Mağaralar canlılarla da doludur. Lav mağaralarında birçok küçük, sıra dışı hayvan yaşar; bazılarında büyük yarasa tünekleri vardır.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l23",
        "display": "Ben mağarada yaşayamam. Wi-fi çekmiyor!",
        "spoken": "Ben mağarada yaşayamam. Wi-fi çekmiyor!",
        "factIds": []
      },
      {
        "id": "l24",
        "display": "Şimdi sıra sende! Bir tabağa bir şeker küpü koy ve üstüne bir damlalıkla ya da kaşıkla damla damla su damlat.",
        "spoken": "Şimdi sıra sende! Bir tabağa bir şeker küpü koy ve üstüne bir damlalıkla ya da kaşıkla damla damla su damlat.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l25",
        "display": "Su, şekeri nasıl oyuyor? Yağmur suyu da kireçtaşını buna benzer biçimde, ama çok çok daha yavaş çözer.",
        "spoken": "Su, şekeri nasıl oyuyor? Yağmur suyu da kireçtaşını buna benzer biçimde, ama çok çok daha yavaş çözer.",
        "factIds": [
          "f2",
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
        "display": "Bunu biliyor muydun? Milli Parklar Servisi'ne göre Dünya'nın en uzun mağarası Mamut Mağarası'dır: 400 milden uzun! Mil, ABD'de kullanılan bir uzunluk birimidir.",
        "spoken": "Bunu biliyor muydun? Milli Parklar Servisi'ne göre Dünya'nın en uzun mağarası Mamut Mağarası'dır: dört yüz milden uzun! Mil, ABD'de kullanılan bir uzunluk birimidir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l27",
        "display": "Hızlı soru! Tavandan aşağı sarkan taş saçaklara ne denir?",
        "spoken": "Hızlı soru! Tavandan aşağı sarkan taş saçaklara ne denir?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l28",
        "display": "Düşün bakalım... Evet: sarkıt!",
        "spoken": "Düşün bakalım... Evet: sarkıt!",
        "factIds": [
          "f8"
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
        "display": "Abone olmayı ve zili açmayı unutma. Bir mağara gezisine gidersen rehberinin yanından ayrılma!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bir mağara gezisine gidersen rehberinin yanından ayrılma!",
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
    "statement": "Erime mağaraları en çok kireçtaşı, mermer ve dolomit gibi kayaçlarda bulunur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Bu kayaçlar yağmur suyu asidik olduğu için çözünür; mağaraları oluşturan asit genellikle karbonik asittir; bu asit karbondioksit suda çözününce oluşur.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Su tortuları ve çözünmüş kayayı aşağı taşıdıkça düdenler genişler.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Karst, kireçtaşı ya da başka çözünebilir kayaçların bulunduğu bölgelerde oluşan bir yer şekli türüdür.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Jeologlara göre içinden dere akan mağara geçitleri yılda en fazla yaklaşık 1 milimetre büyüyebilir.",
    "numbers": [
      "1"
    ]
  },
  {
    "id": "f6",
    "statement": "Birçok mağara yüz binlerce, hatta milyonlarca yaşındadır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Mamut Mağarası 400 milden uzun ölçüsüyle Dünya'nın en uzun mağarasıdır.",
    "numbers": [
      "400"
    ]
  },
  {
    "id": "f8",
    "statement": "Sarkıtlar genellikle kalsitten oluşur; tavandan sarkan buz saçaklarına ya da havuçlara benzerler; sarkıt kelimesi (stalaktit) Yunancada 'damla damla sızmak' demektir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Dikitler, yukarıdaki bir sarkıttan ya da tavandan damlayan suyun yerde biriktirdiği tümsek çökeltilerdir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Bir dikit kendisini besleyen sarkıtla birleşince sütun oluşur; sütunlar bazen 20 metreyi aşan yükseklik ve çapa ulaşabilir.",
    "numbers": [
      "20"
    ]
  },
  {
    "id": "f11",
    "statement": "Lav binlerce derece sıcaktır ve bir nehir gibi akabilir; erimiş lav geçip gidince geride lav tüpü denen boş bir tünel kalır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Deniz mağaraları çoğunlukla dalgaların yol açtığı aşınmayla oluşur.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bazen bir buzulun kenarındaki erime, buzun içinde küçük mağaralar oluşturabilir; buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Lav mağaraları kireçtaşı mağaraları kadar canlı çeşitliliğine sahiptir, içlerinde birçok küçük ve sıra dışı hayvan yaşar; bazı yerlerde büyük yarasa tünekleri vardır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "ABD milli parklarında 4.700'den fazla mağara vardır.",
    "numbers": [
      "4.700"
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
