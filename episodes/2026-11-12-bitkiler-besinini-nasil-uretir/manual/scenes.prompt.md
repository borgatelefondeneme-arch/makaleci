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
        "display": "Sen acıkınca mutfağa gidersin. Peki bir ağaç acıkınca ne yapar?",
        "spoken": "Sen acıkınca mutfağa gidersin. Peki bir ağaç acıkınca ne yapar?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Ne ağzı var ne midesi. Ama besinini kendi üretir; üstelik bunu ışıkla yapar!",
        "spoken": "Ne ağzı var ne midesi. Ama besinini kendi üretir; üstelik bunu ışıkla yapar!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün bir yaprağın içine giriyoruz!",
        "spoken": "Bugün bir yaprağın içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Bitki besinini neyle üretir? Yaprağın içinde neler olur? Ve bu olay bizim için neden hayati?",
        "spoken": "Üç sorumuz var. Bitki besinini neyle üretir? Yaprağın içinde neler olur? Ve bu olay bizim için neden hayati?",
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
        "display": "National Geographic'e göre fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.",
        "spoken": "Neşınıl Ciyografik'e göre fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Malzemeler basit: bitki, havadan karbondioksit, topraktan su alır.",
        "spoken": "Malzemeler basit: bitki, havadan karbondioksit, topraktan su alır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Güneş ışığının enerjisini yakalar ve iki şey üretir: oksijen ve glikoz. Glikoz bir şekerdir; enerjiyi kimyasal olarak depolar.",
        "spoken": "Güneş ışığının enerjisini yakalar ve iki şey üretir: oksijen ve glikoz. Glikoz bir şekerdir; enerjiyi kimyasal olarak depolar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Bitki oksijeni havaya geri verir, enerjiyi ise glikoz moleküllerinde saklar.",
        "spoken": "Bitki oksijeni havaya geri verir, enerjiyi ise glikoz moleküllerinde saklar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Bütün bunlar nerede olur? Bitki hücrelerinin içindeki kloroplast adlı minik organellerde.",
        "spoken": "Bütün bunlar nerede olur? Bitki hücrelerinin içindeki kloroplast adlı minik organellerde.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l11",
        "display": "Kloroplastlarda klorofil adlı bir pigment, yani renk maddesi bulunur. Işığın enerjisini soğuran odur.",
        "spoken": "Kloroplastlarda klorofil adlı bir pigment, yani renk maddesi bulunur. Işığın enerjisini soğuran odur.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l12",
        "display": "Klorofil, ışığın mavi ve kırmızı dalgalarını soğurur; yeşil dalgaları ise yansıtır. Yapraklar bu yüzden yeşil görünür.",
        "spoken": "Klorofil, ışığın mavi ve kırmızı dalgalarını soğurur; yeşil dalgaları ise yansıtır. Yapraklar bu yüzden yeşil görünür.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l13",
        "display": "Yani bitkiler, kullanmadığı rengi bize yolluyor. Yeşil aslında artan renk!",
        "spoken": "Yani bitkiler, kullanmadığı rengi bize yolluyor. Yeşil aslında artan renk!",
        "factIds": [
          "f6"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Şimdi yaprağın içindeki fabrikaya girelim. Fotosentez iki aşamada gerçekleşir.",
        "spoken": "Şimdi yaprağın içindeki fabrikaya girelim. Fotosentez iki aşamada gerçekleşir.",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l15",
        "display": "Birinci aşama: ışığa bağımlı tepkimeler. Kloroplastın içindeki tilakoit zarında gerçekleşir ve sürekli Güneş ışığı ister.",
        "spoken": "Birinci aşama: ışığa bağımlı tepkimeler. Kloroplastın içindeki tilakoit zarında gerçekleşir ve sürekli Güneş ışığı ister.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Burada su molekülleri elektron kaybeder; buna yükseltgenme denir. Su, oksijene dönüşür.",
        "spoken": "Burada su molekülleri elektron kaybeder; buna yükseltgenme denir. Su, oksijene dönüşür.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Işığın enerjisi ise ATP ve NADPH adlı iki enerji taşıyıcı moleküle yüklenir.",
        "spoken": "Işığın enerjisi ise A Te Pe ve En A De Pe Ha adlı iki enerji taşıyıcı moleküle yüklenir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Yani ATP, bitkinin şarjlı pili. Sonunda benim de anladığım bir şey!",
        "spoken": "Yani A Te Pe, bitkinin şarjlı pili. Sonunda benim de anladığım bir şey!",
        "factIds": []
      },
      {
        "id": "l19",
        "display": "İkinci aşama: Calvin döngüsü. Işığa bağımlı değildir ve kloroplastın stroma adlı bölümünde gerçekleşir.",
        "spoken": "İkinci aşama: Kalvin döngüsü. Işığa bağımlı değildir ve kloroplastın stroma adlı bölümünde gerçekleşir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Bu aşamada ATP ve NADPH'deki enerji kullanılır ve karbondioksitten glikoz gibi karbonhidrat molekülleri kurulur.",
        "spoken": "Bu aşamada A Te Pe ve En A De Pe Ha'daki enerji kullanılır ve karbondioksitten glikoz gibi karbonhidrat molekülleri kurulur.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Özetle: ışığın enerjisi önce pillere, sonra şekere aktarılır.",
        "spoken": "Özetle: ışığın enerjisi önce pillere, sonra şekere aktarılır.",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l22",
        "display": "Peki bitki glikozu ne yapar? Topraktan aldığı besin maddeleriyle birlikte yeni yapraklar ve başka bölümler üretir.",
        "spoken": "Peki bitki glikozu ne yapar? Topraktan aldığı besin maddeleriyle birlikte yeni yapraklar ve başka bölümler üretir.",
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
        "id": "l23",
        "display": "Bu olay yalnızca bitkiler için önemli değildir. National Geographic'e göre Dünya'daki yaşamın çoğu fotosenteze bağlıdır.",
        "spoken": "Bu olay yalnızca bitkiler için önemli değildir. Neşınıl Ciyografik'e göre Dünya'daki yaşamın çoğu fotosenteze bağlıdır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Çünkü karadan denize, her ekosistemde besin ağları fotosentezle başlar. Bitkiyi yiyen de, onu yiyen de enerjisini en başta buradan alır.",
        "spoken": "Çünkü karadan denize, her ekosistemde besin ağları fotosentezle başlar. Bitkiyi yiyen de, onu yiyen de enerjisini en başta buradan alır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l25",
        "display": "Soluduğun oksijen de fotosentezin ürünüdür.",
        "spoken": "Soluduğun oksijen de fotosentezin ürünüdür.",
        "factIds": [
          "f1",
          "f4"
        ]
      },
      {
        "id": "l26",
        "display": "Fotosentez yapanlar yalnızca bitkiler değildir: algler ve bazı bakteri türleri de yapar.",
        "spoken": "Fotosentez yapanlar yalnızca bitkiler değildir: algler ve bazı bakteri türleri de yapar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Peki sonbaharda yapraklar neden renk değiştirir? NASA'ya göre yeşil klorofil azalınca öteki pigmentler ortaya çıkar.",
        "spoken": "Peki sonbaharda yapraklar neden renk değiştirir? Nasa'ya göre yeşil klorofil azalınca öteki pigmentler ortaya çıkar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Ben sonbaharda renk değiştirmem. Ama pilim azalınca ışığım kırmızıya döner!",
        "spoken": "Ben sonbaharda renk değiştirmem. Ama pilim azalınca ışığım kırmızıya döner!",
        "factIds": []
      },
      {
        "id": "l29",
        "display": "Şimdi sıra sende! Aynı türden iki küçük saksı bitkisi al. Birini pencere önüne, ötekini karanlık bir dolaba koy.",
        "spoken": "Şimdi sıra sende! Aynı türden iki küçük saksı bitkisi al. Birini pencere önüne, ötekini karanlık bir dolaba koy.",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "İkisine de aynı miktarda su ver. Bir hafta boyunca her gün ikisini de gözle: renklerine ve yapraklarına bak.",
        "spoken": "İkisine de aynı miktarda su ver. Bir hafta boyunca her gün ikisini de gözle: renklerine ve yapraklarına bak.",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Gözlemlerini bir tabloya yaz. Işık eksik kalınca bitkide ne değişiyor?",
        "spoken": "Gözlemlerini bir tabloya yaz. Işık eksik kalınca bitkide ne değişiyor?",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Deney bitince dolaptaki bitkiyi yeniden ışığa çıkarmayı unutma!",
        "spoken": "Deney bitince dolaptaki bitkiyi yeniden ışığa çıkarmayı unutma!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Yoksa bitki sana küser. Ben de küserim!",
        "spoken": "Yoksa bitki sana küser. Ben de küserim!",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l34",
        "display": "Bunu biliyor muydun? National Geographic'e göre soluduğumuz oksijenin çoğu, okyanustaki minik bitkilerden gelir.",
        "spoken": "Bunu biliyor muydun? Neşınıl Ciyografik'e göre soluduğumuz oksijenin çoğu, okyanustaki minik bitkilerden gelir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l35",
        "display": "Hızlı soru! Işığın enerjisini soğuran yeşil pigmentin adı neydi?",
        "spoken": "Hızlı soru! Işığın enerjisini soğuran yeşil pigmentin adı neydi?",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l36",
        "display": "Düşün bakalım... Evet: klorofil!",
        "spoken": "Düşün bakalım... Evet: klorofil!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l37",
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
        "id": "l38",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l39",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l40",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de pencere önüne geçeyim; fotosentez yapamam ama güneşlenmeyi severim!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de pencere önüne geçeyim; fotosentez yapamam ama güneşlenmeyi severim!",
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
    "statement": "Fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Bitkiler karbondioksiti ve suyu havadan ve topraktan alır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Bitkiler Güneş ışığının enerjisini yakalayarak oksijen ve glikozda (bir şeker) depolanan kimyasal enerji üretir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Bitki oksijeni havaya geri verir, enerjiyi glikoz moleküllerinde saklar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bitki hücresinin içinde Güneş ışığının enerjisini depolayan kloroplast adlı küçük organeller vardır; klorofil kloroplastlarda bulunur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Klorofil mavi ve kırmızı ışık dalgalarının enerjisini soğurur, yeşil ışık dalgalarını yansıtır; bitkilere yeşil rengini verir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Işığa bağımlı tepkime tilakoit zarında gerçekleşir ve sürekli Güneş ışığı gerektirir; su yükseltgenir (elektron kaybeder) ve oksijene dönüşür; ATP ve NADPH molekülleri oluşur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Işığa bağımlı olmayan aşama (Calvin döngüsü) stromada gerçekleşir; ATP ve NADPH moleküllerindeki enerji, karbondioksitten glikoz gibi karbonhidrat moleküllerini kurmak için kullanılır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Bitkiler glikozu topraktan aldıkları besin maddeleriyle birlikte yeni yapraklar ve başka bitki bölümleri yapmak için kullanır.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Dünya'daki yaşamın çoğu fotosenteze bağlıdır; karadan denize her tür ekosistemde besin ağları fotosentezle başlar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Fotosentezi bitkiler, algler ve bazı bakteri türleri yapar.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Soluduğumuz oksijenin çoğu okyanustaki minik bitkilerden gelir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Sonbaharda yeşil klorofil azaldıkça öteki pigmentler ortaya çıkar.",
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
