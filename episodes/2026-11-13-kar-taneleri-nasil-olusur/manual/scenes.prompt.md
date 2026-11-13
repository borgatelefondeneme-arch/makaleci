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
        "display": "Gökyüzünden yavaşça süzülen beyaz taneler... Her birinin altı kolu var ve hepsi birbirinden farklı görünüyor!",
        "spoken": "Gökyüzünden yavaşça süzülen beyaz taneler... Her birinin altı kolu var ve hepsi birbirinden farklı görünüyor!",
        "factIds": [
          "f4",
          "f6"
        ]
      },
      {
        "id": "l2",
        "display": "Bir kar tanesi nasıl oluşur? Ve neden hep altı köşelidir?",
        "spoken": "Bir kar tanesi nasıl oluşur? Ve neden hep altı köşelidir?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir bulutun içinde, buzdan bir sanat eserinin doğuşunu izliyoruz!",
        "spoken": "Bugün bir bulutun içinde, buzdan bir sanat eserinin doğuşunu izliyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kar tanesi nasıl oluşur? Biçimini ne belirler? Ve kar neden beyazdır?",
        "spoken": "Üç sorumuz var. Kar tanesi nasıl oluşur? Biçimini ne belirler? Ve kar neden beyazdır?",
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
        "display": "ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre her şey bulutun içinde başlar: çok soğuk bir su damlacığı, havadaki bir polen ya da toz parçacığının üzerinde donar.",
        "spoken": "A Be De Ulusal Okyanus ve Atmosfer Dairesi, Noa'ya göre her şey bulutun içinde başlar: çok soğuk bir su damlacığı, havadaki bir polen ya da toz parçacığının üzerinde donar.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Yani her kar tanesinin kalbinde minicik bir toz zerresi var. Ben de tozlanırım ama kimse beni kar tanesi sanmaz!",
        "spoken": "Yani her kar tanesinin kalbinde minicik bir toz zerresi var. Ben de tozlanırım ama kimse beni kar tanesi sanmaz!",
        "factIds": []
      },
      {
        "id": "l8",
        "display": "Sonra havadaki su buharı bu ilk kristalin üzerinde donar ve yeni kristaller ekler.",
        "spoken": "Sonra havadaki su buharı bu ilk kristalin üzerinde donar ve yeni kristaller ekler.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l9",
        "display": "Sıcaklık 0 derecenin altına düşünce su buharı sıvı olmadan, doğrudan buza dönüşebilir.",
        "spoken": "Sıcaklık sıfır derecenin altına düşünce su buharı sıvı olmadan, doğrudan buza dönüşebilir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Kar tanesi aslında çok sayıda kar kristalinin bir araya gelmesiyle oluşur.",
        "spoken": "Kar tanesi aslında çok sayıda kar kristalinin bir araya gelmesiyle oluşur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Neden altı köşeli? NOAA'ya göre bu biçim, su moleküllerinin kristalin içinde belirli yerlere dizilmesinden gelir. Bu yüzden altıgen yapı her zaman korunur.",
        "spoken": "Neden altı köşeli? Noa'ya göre bu biçim, su moleküllerinin kristalin içinde belirli yerlere dizilmesinden gelir. Bu yüzden altıgen yapı her zaman korunur.",
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
        "display": "Peki biçimini ne belirler? En çok, kristalin oluştuğu sıcaklık; biraz da havanın nemi.",
        "spoken": "Peki biçimini ne belirler? En çok, kristalin oluştuğu sıcaklık; biraz da havanın nemi.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Örneğin hava donma noktasının biraz altındayken uzun iğneler, çok daha soğukken ise çok yassı levhalar oluşur.",
        "spoken": "Örneğin hava donma noktasının biraz altındayken uzun iğneler, çok daha soğukken ise çok yassı levhalar oluşur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Her kar tanesi yere inerken biraz farklı bir yoldan geçer. Farklı sıcaklıklar, farklı nem... Bu yüzden her biri benzersiz görünme eğilimindedir.",
        "spoken": "Her kar tanesi yere inerken biraz farklı bir yoldan geçer. Farklı sıcaklıklar, farklı nem... Bu yüzden her biri benzersiz görünme eğilimindedir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Prizmalar, iğneler ve o tanıdık dantel desenleri hep bu yolculuğun sonucu.",
        "spoken": "Prizmalar, iğneler ve o tanıdık dantel desenleri hep bu yolculuğun sonucu.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Kar tanelerinin çoğu 1,3 santimetreden küçüktür. Çok daha büyükleri 5 santimetreye yaklaşabilir.",
        "spoken": "Kar tanelerinin çoğu bir virgül üç santimetreden küçüktür. Çok daha büyükleri beş santimetreye yaklaşabilir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l17",
        "display": "Kar yağması için hava ne kadar soğuk olmalı? Ulusal Kar ve Buz Veri Merkezi NSIDC'ye göre kar, sıcaklık 0 derecede ya da altındayken oluşur.",
        "spoken": "Kar yağması için hava ne kadar soğuk olmalı? Ulusal Kar ve Buz Veri Merkezi, En Es Ay Di Si'ye göre kar, sıcaklık sıfır derecede ya da altındayken oluşur.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l18",
        "display": "Hatta İngiltere Meteoroloji Ofisi'ne göre yerde sıcaklığın sıfırın altında olması gerektiği bir efsanedir.",
        "spoken": "Hatta İngiltere Meteoroloji Ofisi'ne göre yerde sıcaklığın sıfırın altında olması gerektiği bir efsanedir.",
        "factIds": [
          "f13"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l19",
        "display": "Kar neden beyazdır? Aslında kar yarı saydamdır! Ama kar tanesinin sayısız yüzü ışığı her yöne saçar ve bize beyaz görünür.",
        "spoken": "Kar neden beyazdır? Aslında kar yarı saydamdır! Ama kar tanesinin sayısız yüzü ışığı her yöne saçar ve bize beyaz görünür.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l20",
        "display": "Kar, iyi bir yalıtkandır; tıpkı evlerin tavanındaki yalıtım gibi. Çünkü bir kar katmanının büyük kısmı havadır.",
        "spoken": "Kar, iyi bir yalıtkandır; tıpkı evlerin tavanındaki yalıtım gibi. Çünkü bir kar katmanının büyük kısmı havadır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Benim de yalıtımım var. Kablolarımın çevresinde, kardan değil plastikten!",
        "spoken": "Benim de yalıtımım var. Kablolarımın çevresinde, kardan değil plastikten!",
        "factIds": []
      },
      {
        "id": "l22",
        "display": "Karlı bir günde dışarısı neden sessizdir? Taze kar, ses dalgalarını emer.",
        "spoken": "Karlı bir günde dışarısı neden sessizdir? Taze kar, ses dalgalarını emer.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Kışın gökten başka şeyler de düşer. Kar taneleri ılık bir hava katmanından geçerken kısmen eriyip yeniden donarsa sulu kar olur.",
        "spoken": "Kışın gökten başka şeyler de düşer. Kar taneleri ılık bir hava katmanından geçerken kısmen eriyip yeniden donarsa sulu kar olur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Tamamen erir ve yerdeki soğuk yüzeylere değer değmez donarsa buna donan yağmur denir.",
        "spoken": "Tamamen erir ve yerdeki soğuk yüzeylere değer değmez donarsa buna donan yağmur denir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Bir de graupel var: yuvarlaklaşmış, 2–5 milimetrelik kar tanecikleri. Doluya benzer ama daha yumuşaktır ve kolay ufalanır.",
        "spoken": "Bir de graupel var: yuvarlaklaşmış, iki ile beş milimetrelik kar tanecikleri. Doluya benzer ama daha yumuşaktır ve kolay ufalanır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Şimdi sıra sende! Karlı bir günde koyu renkli bir kumaşı birkaç dakika dondurucuda soğut, sonra dışarı çıkıp üstüne düşen kar tanelerine büyüteçle bak.",
        "spoken": "Şimdi sıra sende! Karlı bir günde koyu renkli bir kumaşı birkaç dakika dondurucuda soğut, sonra dışarı çıkıp üstüne düşen kar tanelerine büyüteçle bak.",
        "factIds": []
      },
      {
        "id": "l27",
        "display": "Kaç köşe sayıyorsun? İğne mi, levha mı, dantel mi? Gördüklerini çiz.",
        "spoken": "Kaç köşe sayıyorsun? İğne mi, levha mı, dantel mi? Gördüklerini çiz.",
        "factIds": []
      },
      {
        "id": "l28",
        "display": "Unutma: sıkı giyin, çok soğukta uzun süre kalma. Ve yol kenarındaki karı asla yeme; içinde kir ve kimyasallar olabilir.",
        "spoken": "Unutma: sıkı giyin, çok soğukta uzun süre kalma. Ve yol kenarındaki karı asla yeme; içinde kir ve kimyasallar olabilir.",
        "factIds": [
          "f16"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l29",
        "display": "Bunu biliyor muydun? Wilson Bentley adında bir çiftçinin hobisi, kar tanelerini fotoğraflamaktı.",
        "spoken": "Bunu biliyor muydun? Wilson Bentley adında bir çiftçinin hobisi, kar tanelerini fotoğraflamaktı.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l30",
        "display": "Hızlı soru! Kar taneleri kaç köşelidir?",
        "spoken": "Hızlı soru! Kar taneleri kaç köşelidir?",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l31",
        "display": "Düşün bakalım... Evet: altı!",
        "spoken": "Düşün bakalım... Evet: altı!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l32",
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
        "id": "l33",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de antenimdeki karı silkeleyip gidiyorum!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de antenimdeki karı silkeleyip gidiyorum!",
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
    "statement": "Bir kar tanesi, çok soğuk bir su damlacığı gökyüzünde bir polen ya da toz parçacığının üzerinde donunca oluşmaya başlar; su buharı ilk kristalin üzerinde donarak yeni kristaller kurar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Sıcaklık 0°C'nin altına düşünce su buharı sıvı evreye geçmeden doğrudan buza dönüşür.",
    "numbers": [
      "0"
    ]
  },
  {
    "id": "f3",
    "statement": "Kar taneleri bulutlardan düşen tek buz kristalleri ya da buz kristali kümeleridir; çok sayıda kar kristalinin birikimidir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Kar tanelerinin biçimi, kristalin su moleküllerinin önceden belirlenmiş yerlere dizilmesindeki iç düzeni yansıtır; altıgen biçim her zaman korunur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Kristalin biçimini en çok oluştuğu sıcaklık, daha az ölçüde de havanın nemi belirler; daha az soğukta uzun iğne gibi kristaller, çok daha soğukta çok yassı levha gibi kristaller görülür (kaynakta Fahrenhayt değerleriyle).",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kar tanelerinin her biri gökyüzünden yere biraz farklı yollar izler; bu yüzden prizmalardan iğnelere, tanıdık dantel desenine kadar hepsi benzersiz görünme eğilimindedir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Temiz kar görünür güneş ışığının çoğunu yansıtır ve beyaz görünür; aslında yarı saydamdır; kar tanesinin çok sayıdaki yüzü ışığı her yöne saçar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Kar, bir evin tavanındaki yalıtıma benzer iyi bir yalıtkandır; bir kar katmanının toplam hacminin çoğu havadır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Taze kar sesi bastırır, çünkü ses dalgalarını emer.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Kar tanelerinin çoğu 1,3 santimetreden küçüktür; çok daha büyükleri 5 santimetreye yaklaşabilir.",
    "numbers": [
      "1.3",
      "5"
    ]
  },
  {
    "id": "f11",
    "statement": "Sulu kar, kar taneleri ince bir ılık hava katmanından geçerken yalnızca kısmen eridiğinde oluşur; donan yağmur, kar taneleri daha ılık bir katmanda tamamen erir ve 0°C'deki ya da daha soğuk her şeye değer değmez yeniden donar.",
    "numbers": [
      "0"
    ]
  },
  {
    "id": "f12",
    "statement": "Graupel, yuvarlaklaşmış, opak, 2–5 milimetrelik kar taneciklerinden oluşur; bazen doluyla karıştırılır ama dokusu daha yumuşak ve ufalanır.",
    "numbers": [
      "2",
      "5"
    ]
  },
  {
    "id": "f13",
    "statement": "Kar, atmosfer sıcaklığı donma noktasında ya da altındayken (0°C) oluşur; karın yağması için sıfırın altında olması gerektiği bir efsanedir.",
    "numbers": [
      "0"
    ]
  },
  {
    "id": "f14",
    "statement": "Kar taneleri bulutlardaki minik buz kristallerinin birbirine yapışmasıyla oluşur.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Wilson Bentley, hobisi kar tanelerini fotoğraflamak olan bir çiftçiydi.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Küreme kar asla yenmemelidir; içinde kir ve magnezyum klorür gibi kimyasallar vardır; düşük rüzgâr soğuğuna maruz kalmak donmaya ya da hipotermiye yol açabilir.",
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
