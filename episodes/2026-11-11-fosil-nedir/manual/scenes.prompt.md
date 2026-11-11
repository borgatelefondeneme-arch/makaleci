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
        "display": "Elinde sıradan bir taş var. Ama üstünde, çok eski zamanlarda yaşamış bir canlının izi duruyor!",
        "spoken": "Elinde sıradan bir taş var. Ama üstünde, çok eski zamanlarda yaşamış bir canlının izi duruyor!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Bir canlı nasıl olur da taşa dönüşür? Ve neden her canlı fosil olmaz?",
        "spoken": "Bir canlı nasıl olur da taşa dönüşür? Ve neden her canlı fosil olmaz?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün yerin altındaki bu dev arşivi açıyoruz!",
        "spoken": "Bugün yerin altındaki bu dev arşivi açıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Baştan söyleyeyim: bende kemik yok, vida var. Ben fosil olmam; olsa olsa antika olurum!",
        "spoken": "Baştan söyleyeyim: bende kemik yok, vida var. Ben fosil olmam; olsa olsa antika olurum!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Fosil tam olarak nedir? Bir canlı nasıl fosilleşir? Ve fosiller bize ne anlatır?",
        "spoken": "Üç sorumuz var. Fosil tam olarak nedir? Bir canlı nasıl fosilleşir? Ve fosiller bize ne anlatır?",
        "factIds": []
      },
      {
        "id": "l6",
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
        "id": "l7",
        "display": "National Geographic'e göre fosil, çok eski zamanlarda yaşamış canlılardan korunarak kalmış kalıntı ya da izdir.",
        "spoken": "Neşınıl Ciyografik'e göre fosil, çok eski zamanlarda yaşamış canlılardan korunarak kalmış kalıntı ya da izdir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Kelime Latinceden gelir. Britanya Jeoloji Araştırmaları Kurumu'na göre \"fossilis\", kazılıp çıkarılmış demektir.",
        "spoken": "Kelime Latinceden gelir. Britanya Jeoloji Araştırmaları Kurumu'na göre fosilis, kazılıp çıkarılmış demektir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Peki ne kadar eski? Bir kalıntının fosil sayılması için genellikle 10.000 yıldan yaşlı olması gerekir.",
        "spoken": "Peki ne kadar eski? Bir kalıntının fosil sayılması için genellikle on bin yıldan yaşlı olması gerekir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Benim garanti belgem bile o kadar dayanmaz!",
        "spoken": "Benim garanti belgem bile o kadar dayanmaz!",
        "factIds": []
      },
      {
        "id": "l11",
        "display": "ABD Ulusal Park Servisi'ne göre fosiller iki büyük gruba ayrılır. Birincisi vücut fosili: canlının kendi parçasıdır. Kemik, diş, kabuk, odun ya da yaprak gibi.",
        "spoken": "A Be De Ulusal Park Servisi'ne göre fosiller iki büyük gruba ayrılır. Birincisi vücut fosili: canlının kendi parçasıdır. Kemik, diş, kabuk, odun ya da yaprak gibi.",
        "factIds": [
          "f4",
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "İkincisi iz fosili: canlının bedeni değil, yaşarken bıraktığı izdir. Ayak izi ya da yuva tüneli gibi.",
        "spoken": "İkincisi iz fosili: canlının bedeni değil, yaşarken bıraktığı izdir. Ayak izi ya da yuva tüneli gibi.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "İz fosilleri çok değerlidir; çünkü canlının davranışı hakkında başka türlü bilemeyeceğimiz şeyleri gösterir.",
        "spoken": "İz fosilleri çok değerlidir; çünkü canlının davranışı hakkında başka türlü bilemeyeceğimiz şeyleri gösterir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "En ilginç iz fosilinin adı koprolit. Londra'daki Doğa Tarihi Müzesi'ne göre koprolit, fosilleşmiş hayvan dışkısıdır. Evet, yanlış duymadın: taşlaşmış kaka!",
        "spoken": "En ilginç iz fosilinin adı koprolit. Londra'daki Doğa Tarihi Müzesi'ne göre koprolit, fosilleşmiş hayvan dışkısıdır. Evet, yanlış duymadın: taşlaşmış kaka!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l15",
        "display": "Gülme, çok işe yarar! İçinde kemik parçaları varsa o hayvan etçildi. Tohum ya da yaprak kalıntısı varsa bitki yiyordu.",
        "spoken": "Gülme, çok işe yarar! İçinde kemik parçaları varsa o hayvan etçildi. Tohum ya da yaprak kalıntısı varsa bitki yiyordu.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l16",
        "display": "Demek ki bilim insanı olmak, bazen gerçekten pis iştir!",
        "spoken": "Demek ki bilim insanı olmak, bazen gerçekten pis iştir!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l17",
        "display": "Peki bir canlı nasıl fosilleşir? Doğa Tarihi Müzesi'nin anlattığı adımları sırayla izleyelim.",
        "spoken": "Peki bir canlı nasıl fosilleşir? Doğa Tarihi Müzesi'nin anlattığı adımları sırayla izleyelim.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l18",
        "display": "Birinci adım: canlı ölür. Deri ve kas gibi yumuşak kısımlar çürümeye başlar.",
        "spoken": "Birinci adım: canlı ölür. Deri ve kas gibi yumuşak kısımlar çürümeye başlar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l19",
        "display": "İkinci adım: tamamen yok olmadan önce çamur, kum ya da silt gibi tortularla örtülür. Çoğu zaman geriye yalnızca kemikler ve dişler kalır.",
        "spoken": "İkinci adım: tamamen yok olmadan önce çamur, kum ya da silt gibi tortularla örtülür. Çoğu zaman geriye yalnızca kemikler ve dişler kalır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Burada hız önemlidir: çabucak gömülmek, kalıntıyı çürümekten ve aşınmaktan korur.",
        "spoken": "Burada hız önemlidir: çabucak gömülmek, kalıntıyı çürümekten ve aşınmaktan korur.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l21",
        "display": "Üçüncü adım: üstüne kat kat yeni tortu birikir. Bu katmanlar zamanla tortul kayaya dönüşür.",
        "spoken": "Üçüncü adım: üstüne kat kat yeni tortu birikir. Bu katmanlar zamanla tortul kayaya dönüşür.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l22",
        "display": "Dördüncü adım: su, kemiklerin içine sızar ve geride mineral bırakır. Mineraller kemiğin minik gözeneklerini doldurur; kemik yavaş yavaş taşa dönüşür.",
        "spoken": "Dördüncü adım: su, kemiklerin içine sızar ve geride mineral bırakır. Mineraller kemiğin minik gözeneklerini doldurur; kemik yavaş yavaş taşa dönüşür.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l23",
        "display": "Bu olayın adı permineralizasyon. Kelime uzun ama anlamı basit: gözeneklerin mineralle dolması.",
        "spoken": "Bu olayın adı permineralizasyon. Kelime uzun ama anlamı basit: gözeneklerin mineralle dolması.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l24",
        "display": "Ve sabır gerekir: bu süreç binlerce, hatta milyonlarca yıl sürebilir.",
        "spoken": "Ve sabır gerekir: bu süreç binlerce, hatta milyonlarca yıl sürebilir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l25",
        "display": "Bazen su kemiği tamamen çözer ve kayada onun biçiminde bir boşluk kalır. Buna kalıp denir. Boşluğu mineraller doldurursa döküm oluşur.",
        "spoken": "Bazen su kemiği tamamen çözer ve kayada onun biçiminde bir boşluk kalır. Buna kalıp denir. Boşluğu mineraller doldurursa döküm oluşur.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l26",
        "display": "Bir yol daha var: kehribar. Ağaç reçinesi fosilleşir ve içine yapışan karınca, sinek gibi böcekleri saklar.",
        "spoken": "Bir yol daha var: kehribar. Ağaç reçinesi fosilleşir ve içine yapışan karınca, sinek gibi böcekleri saklar.",
        "factIds": [
          "f15"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l27",
        "display": "Peki her canlı fosil olur mu? Hayır! Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu çürür ve geriye hiçbir şey kalmaz.",
        "spoken": "Peki her canlı fosil olur mu? Hayır! Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu çürür ve geriye hiçbir şey kalmaz.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l28",
        "display": "Kemik, diş, kabuk gibi sert parçalar daha kolay fosilleşir. Solucan gibi yumuşak gövdeli canlılar ise nadiren fosil olur.",
        "spoken": "Kemik, diş, kabuk gibi sert parçalar daha kolay fosilleşir. Solucan gibi yumuşak gövdeli canlılar ise nadiren fosil olur.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l29",
        "display": "Yani fosil olmak çok zor bir sınav gibi. Üstelik sonuçların açıklanması çok, çok uzun sürüyor!",
        "spoken": "Yani fosil olmak çok zor bir sınav gibi. Üstelik sonuçların açıklanması çok, çok uzun sürüyor!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Bulduğumuz fosillerin neredeyse tamamı, yaklaşık %99'u, deniz hayvanlarına aittir: kabuklular ve köpek balıkları gibi.",
        "spoken": "Bulduğumuz fosillerin neredeyse tamamı, yaklaşık yüzde doksan dokuzu, deniz hayvanlarına aittir: kabuklular ve köpek balıkları gibi.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l31",
        "display": "Fosiller tortul kayaların içinde bulunur. Rüzgâr, yağmur ve buz kayaları aşındırdıkça fosiller yavaş yavaş yüzeye çıkar.",
        "spoken": "Fosiller tortul kayaların içinde bulunur. Rüzgâr, yağmur ve buz kayaları aşındırdıkça fosiller yavaş yavaş yüzeye çıkar.",
        "factIds": [
          "f19",
          "f20"
        ]
      },
      {
        "id": "l32",
        "display": "Şaşırtıcı bir örnek: Everest'in tepesinde deniz hayvanlarının fosilleri bulunabilir! Çünkü o kayalar bir zamanlar okyanusun dibindeydi.",
        "spoken": "Şaşırtıcı bir örnek: Everest'in tepesinde deniz hayvanlarının fosilleri bulunabilir! Çünkü o kayalar bir zamanlar okyanusun dibindeydi.",
        "factIds": [
          "f21"
        ]
      },
      {
        "id": "l33",
        "display": "Fosilleri inceleyen bilim insanlarına paleontolog denir. Fosiller onlara canlıların nasıl yaşadığını ve Dünya'nın nasıl değiştiğini anlatır.",
        "spoken": "Fosilleri inceleyen bilim insanlarına paleontolog denir. Fosiller onlara canlıların nasıl yaşadığını ve Dünya'nın nasıl değiştiğini anlatır.",
        "factIds": [
          "f22"
        ]
      },
      {
        "id": "l34",
        "display": "En eski fosiller neredeyse 4 milyar yaşında: okyanusta yaşamış bakterilerin izleri.",
        "spoken": "En eski fosiller neredeyse dört milyar yaşında: okyanusta yaşamış bakterilerin izleri.",
        "factIds": [
          "f23"
        ]
      },
      {
        "id": "l35",
        "display": "Şimdi sıra sende! Oyun hamuruna bir deniz kabuğu ya da yaprak bastır ve yavaşça kaldır.",
        "spoken": "Şimdi sıra sende! Oyun hamuruna bir deniz kabuğu ya da yaprak bastır ve yavaşça kaldır.",
        "factIds": []
      },
      {
        "id": "l36",
        "display": "Hamurda kalan çukur bir kalıptır. Doğada böyle bir boşluğu mineraller doldurur ve döküm oluşur.",
        "spoken": "Hamurda kalan çukur bir kalıptır. Doğada böyle bir boşluğu mineraller doldurur ve döküm oluşur.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l37",
        "display": "Dışarıda fosil görürsen kural basit: bak, fotoğrafını çek, yerinde bırak. Örneğin ABD'nin milli parklarında fosil toplamak yasaktır; çünkü tek bir fosil, bir türün tek kanıtı olabilir.",
        "spoken": "Dışarıda fosil görürsen kural basit: bak, fotoğrafını çek, yerinde bırak. Örneğin A Be De'nin milli parklarında fosil toplamak yasaktır; çünkü tek bir fosil, bir türün tek kanıtı olabilir.",
        "factIds": [
          "f24",
          "f25"
        ]
      },
      {
        "id": "l38",
        "display": "Önemli bir şey bulduğunu düşünürsen bir büyüğünle birlikte bir müzeye haber ver.",
        "spoken": "Önemli bir şey bulduğunu düşünürsen bir büyüğünle birlikte bir müzeye haber ver.",
        "factIds": [
          "f25"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l39",
        "display": "Bunu biliyor muydun? Omurgalı hayvan fosilleri arasında en bol bulunanı köpek balığı dişleridir.",
        "spoken": "Bunu biliyor muydun? Omurgalı hayvan fosilleri arasında en bol bulunanı köpek balığı dişleridir.",
        "factIds": [
          "f26"
        ]
      },
      {
        "id": "l40",
        "display": "Hızlı soru! Ayak izi, vücut fosili midir yoksa iz fosili mi?",
        "spoken": "Hızlı soru! Ayak izi, vücut fosili midir yoksa iz fosili mi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l41",
        "display": "Düşün bakalım... Evet: iz fosili!",
        "spoken": "Düşün bakalım... Evet: iz fosili!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l42",
        "display": "Ben hiç ayak izi bırakamam. Çünkü yürümüyorum, uçuyorum!",
        "spoken": "Ben hiç ayak izi bırakamam. Çünkü yürümüyorum, uçuyorum!",
        "factIds": []
      },
      {
        "id": "l43",
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
        "id": "l44",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l45",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l46",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de uçayım; burada fazla durursam fosil olacağım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de uçayım; burada fazla durursam fosil olacağım!",
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
    "statement": "Fosil, çok eski canlıların korunmuş kalıntısı ya da kalıntı izidir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Fosil kelimesi Latince 'fossilis'ten gelir; 'kazılıp çıkarılmış' demektir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Korunmuş kalıntılar 10.000 yıldan yaşlıysa fosil sayılır; fosiller tipik olarak 10.000 yıldan eskidir.",
    "numbers": [
      "10.000"
    ]
  },
  {
    "id": "f4",
    "statement": "Vücut fosilleri kemik, diş, deri, kabuk, odun ve yaprakları kapsar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "İz fosilleri, canlının yaşarken yaptığı etkinlikten kalır: ayak izleri, yuva tünelleri, koprolitler gibi.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "İz fosilleri, başka türlü bilinemeyecek davranış bilgilerini ortaya çıkarır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Koprolit, milyonlarca yıl önce yaşamış hayvanların fosilleşmiş dışkısıdır; bir iz fosilidir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Koprolitte kemik parçaları varsa hayvan etçildi; tohum, yaprak kalıntısı, polen ya da kabuk varsa bitki yiyordu.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Hayvan ölür; deri ve kas gibi yumuşak kısımlar çürümeye başlar; tamamen yok olmadan çamur, kum ya da siltle örtülür; çoğu zaman yalnızca kemikler ve dişler kalır.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Hızlı gömülme fosilleşme için gereklidir; ölümden kısa süre sonra tortuyla örtülmek kalıntıyı çürümekten ve aşınmaktan korur.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Üstüne çok sayıda tortu katmanı birikir; bunlar zamanla tortul kayaya dönüşür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Su kemiklere ve dişlere sızar, geride mineral bırakarak onları taşa çevirir; permineralizasyon, organik maddedeki minik gözeneklerin dolmasıdır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bu süreç binlerce, hatta milyonlarca yıl sürebilir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Yeraltı suyu gömülü kemiği ya da kabuğu çözerse onun biçiminde bir boşluk (kalıp) kalır; mineralli su bu boşluğu doldurursa aynı biçimde bir fosil (döküm) oluşur.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Ağaçların yapışkan reçinesi fosilleşebilir (kehribar); kehribar karınca, sinek gibi narin canlıların bedenlerini koruyabilir.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu tamamen çürür ve geriye bir şey kalmaz.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Fosilleşme, iskelet, diş, kabuk gibi sert parçaları olan canlılarda daha sık görülür; solucan gibi yumuşak gövdeli canlılar nadiren fosilleşir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Bulunan fosillerin neredeyse tamamı, yaklaşık %99'u, kabuklular ve köpek balıkları gibi deniz hayvanlarına aittir.",
    "numbers": [
      "99"
    ]
  },
  {
    "id": "f19",
    "statement": "Fosiller, oluşma biçimleri nedeniyle tortul kayalarda bulunur.",
    "numbers": []
  },
  {
    "id": "f20",
    "statement": "Rüzgâr, yağmur, buz, sıcaklık ve nehirlerin yol açtığı aşınma kayaları parçalar; fosiller yavaş yavaş yüzeye çıkar.",
    "numbers": []
  },
  {
    "id": "f21",
    "statement": "Deniz hayvanlarının fosilleri Everest'in tepesinde bulunabilir; Himalayaları oluşturan kayalar bir zamanlar okyanusun dibindeydi.",
    "numbers": []
  },
  {
    "id": "f22",
    "statement": "Paleontologlar fosilleri inceleyen kişilerdir; fosiller türlerin nasıl yaşadığını ve Dünya'nın nasıl değiştiğini öğrenmeye yardım eder.",
    "numbers": []
  },
  {
    "id": "f23",
    "statement": "En eski fosiller neredeyse 4 milyar yaşındadır ve okyanusta yaşamış bakterilerin izleridir.",
    "numbers": [
      "4"
    ]
  },
  {
    "id": "f24",
    "statement": "ABD Ulusal Park Sistemi'nin bütün birimlerinde fosil toplamak yasaktır; tek bir fosil, bütün bir türün var olduğunun tek kanıtı olabilir.",
    "numbers": []
  },
  {
    "id": "f25",
    "statement": "Bazı yerlerde bakılabilir ama hiçbir şey toplanamaz; önemli olabilecek bir fosil görülürse bir müzeye bildirilmesi önerilir.",
    "numbers": []
  },
  {
    "id": "f26",
    "statement": "Köpek balığı dişleri, en bol bulunan omurgalı fosilleridir.",
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
