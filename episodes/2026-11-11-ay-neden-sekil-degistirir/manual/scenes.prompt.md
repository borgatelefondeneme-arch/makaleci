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
        "display": "Bir gece gökyüzünde incecik bir hilal görürsün. Günler sonra aynı gökyüzünde kocaman, yusyuvarlak bir Ay!",
        "spoken": "Bir gece gökyüzünde incecik bir hilal görürsün. Günler sonra aynı gökyüzünde kocaman, yusyuvarlak bir Ay!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Ay gerçekten biçim mi değiştiriyor? Yoksa bizi yanıltan başka bir şey mi var?",
        "spoken": "Ay gerçekten biçim mi değiştiriyor? Yoksa bizi yanıltan başka bir şey mi var?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Ay'ın çevresinde bir tur atıyoruz!",
        "spoken": "Bugün Ay'ın çevresinde bir tur atıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Ay'a kadar uçmayı çok isterdim. Ama şarjım yarı yolda biter!",
        "spoken": "Ay'a kadar uçmayı çok isterdim. Ama şarjım yarı yolda biter!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Ay nasıl parlar? Neden her gece farklı görünür? Ve bize neden hep aynı yüzünü gösterir?",
        "spoken": "Üç sorumuz var. Ay nasıl parlar? Neden her gece farklı görünür? Ve bize neden hep aynı yüzünü gösterir?",
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
        "display": "NASA'ya göre Ay kendi ışığını üretmez. Ay ışığı dediğimiz şey, aslında Ay'dan yansıyan Güneş ışığıdır.",
        "spoken": "Nasa'ya göre Ay kendi ışığını üretmez. Ay ışığı dediğimiz şey, aslında Ay'dan yansıyan Güneş ışığıdır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.",
        "spoken": "Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l9",
        "display": "Ben ise kendi ışığımı üretirim. Gözlerim LED!",
        "spoken": "Ben ise kendi ışığımı üretirim. Gözlerim led!",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "İşin püf noktası şu: Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.",
        "spoken": "İşin püf noktası şu: Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Ay'ın biçimi ay boyunca hiç değişmez. Değişen, bizim ona bakış açımızdır.",
        "spoken": "Ay'ın biçimi ay boyunca hiç değişmez. Değişen, bizim ona bakış açımızdır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Ay, Dünya'nın çevresinde bir yörüngede dolanır. Dolandıkça aydınlık yarısının bazen tamamını, bazen bir kısmını görürüz; bazen de hiç göremeyiz.",
        "spoken": "Ay, Dünya'nın çevresinde bir yörüngede dolanır. Dolandıkça aydınlık yarısının bazen tamamını, bazen bir kısmını görürüz; bazen de hiç göremeyiz.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Bu farklı görünümlere Ay'ın evreleri denir.",
        "spoken": "Bu farklı görünümlere Ay'ın evreleri denir.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Peki Dünya'nın gölgesi? Evrelerin nedeni o değildir. Dünya'nın gölgesi Ay'a yalnızca Ay tutulmasında düşer.",
        "spoken": "Peki Dünya'nın gölgesi? Evrelerin nedeni o değildir. Dünya'nın gölgesi Ay'a yalnızca Ay tutulmasında düşer.",
        "factIds": [
          "f3",
          "f13"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l15",
        "display": "Sekiz evre var. İlki yeni ay: Ay, Dünya ile Güneş arasındadır ve aydınlık yüzü bize dönük değildir.",
        "spoken": "Sekiz evre var. İlki yeni ay: Ay, Dünya ile Güneş arasındadır ve aydınlık yüzü bize dönük değildir.",
        "factIds": [
          "f4",
          "f13"
        ]
      },
      {
        "id": "l16",
        "display": "Sonra incecik bir hilal belirir ve gece gece büyür.",
        "spoken": "Sonra incecik bir hilal belirir ve gece gece büyür.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l17",
        "display": "Ardından ilk dördün gelir: Ay'ı yarım daire gibi görürüz.",
        "spoken": "Ardından ilk dördün gelir: Ay'ı yarım daire gibi görürüz.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l18",
        "display": "Sonra şişkin ay: yarım ay ile dolunay arasındaki evre.",
        "spoken": "Sonra şişkin ay: yarım ay ile dolunay arasındaki evre.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l19",
        "display": "Ve dolunay! Aydınlık yüzün tamamı bize dönüktür.",
        "spoken": "Ve dolunay! Aydınlık yüzün tamamı bize dönüktür.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l20",
        "display": "Sonra her şey tersine döner: şişkin ay, son dördün, küçülen hilal ve yeniden yeni ay.",
        "spoken": "Sonra her şey tersine döner: şişkin ay, son dördün, küçülen hilal ve yeniden yeni ay.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l21",
        "display": "Bir yeni aydan ötekine kadar yaklaşık 29,5 gün geçer.",
        "spoken": "Bir yeni aydan ötekine kadar yaklaşık yirmi dokuz buçuk gün geçer.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l22",
        "display": "İlginç olan şu: Ay, Dünya'nın çevresindeki bir turunu yaklaşık 27,3 günde tamamlar. Aradaki fark, Dünya'nın da bu sırada Güneş'in çevresinde ilerlemesinden kaynaklanır.",
        "spoken": "İlginç olan şu: Ay, Dünya'nın çevresindeki bir turunu yaklaşık yirmi yedi virgül üç günde tamamlar. Aradaki fark, Dünya'nın da bu sırada Güneş'in çevresinde ilerlemesinden kaynaklanır.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l23",
        "display": "Bir ipucu daha: dolunay, Güneş batarken doğar. Ay her gün biraz daha geç doğar ve gündüz gökyüzünde bile sık sık görülebilir.",
        "spoken": "Bir ipucu daha: dolunay, Güneş batarken doğar. Ay her gün biraz daha geç doğar ve gündüz gökyüzünde bile sık sık görülebilir.",
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
        "id": "l24",
        "display": "Ay bize hep aynı yüzünü gösterir. NASA bunu, eşinin çevresinde dönerken yüzünü hep ona çeviren bir dansçıya benzetiyor.",
        "spoken": "Ay bize hep aynı yüzünü gösterir. Nasa bunu, eşinin çevresinde dönerken yüzünü hep ona çeviren bir dansçıya benzetiyor.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l25",
        "display": "Ben de fotoğraflarda hep iyi tarafımı dönerim. Ay'dan öğrendim!",
        "spoken": "Ben de fotoğraflarda hep iyi tarafımı dönerim. Ay'dan öğrendim!",
        "factIds": []
      },
      {
        "id": "l26",
        "display": "Göremediğimiz yüze karanlık yüz denmesi ise yanıltıcıdır. Doğru adı uzak yüzdür; çünkü Ay'ın yarısı her zaman aydınlıktır.",
        "spoken": "Göremediğimiz yüze karanlık yüz denmesi ise yanıltıcıdır. Doğru adı uzak yüzdür; çünkü Ay'ın yarısı her zaman aydınlıktır.",
        "factIds": [
          "f8",
          "f2"
        ]
      },
      {
        "id": "l27",
        "display": "Ay tutulması dolunayda olur: Dünya tam olarak Güneş ile Ay'ın arasına girer ve gölgesi Ay'ın üstüne düşer.",
        "spoken": "Ay tutulması dolunayda olur: Dünya tam olarak Güneş ile Ay'ın arasına girer ve gölgesi Ay'ın üstüne düşer.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Peki neden her dolunayda tutulma olmaz? Çünkü Ay'ın yörüngesi, Dünya'nın yörüngesine göre yaklaşık 5 derece eğiktir.",
        "spoken": "Peki neden her dolunayda tutulma olmaz? Çünkü Ay'ın yörüngesi, Dünya'nın yörüngesine göre yaklaşık beş derece eğiktir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l29",
        "display": "Ay yalnızca gökyüzünü süslemez. Kütle çekimi okyanusları kabartır: gelgitlerin nedeni budur.",
        "spoken": "Ay yalnızca gökyüzünü süslemez. Kütle çekimi okyanusları kabartır: gelgitlerin nedeni budur.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l30",
        "display": "Biraz da sayı: Ay bize ortalama 384.400 kilometre uzaklıktadır ve genişliği Dünya'nınkinin üçte birinden azdır.",
        "spoken": "Biraz da sayı: Ay bize ortalama üç yüz seksen dört bin dört yüz kilometre uzaklıktadır ve genişliği Dünya'nınkinin üçte birinden azdır.",
        "factIds": [
          "f9",
          "f10"
        ]
      },
      {
        "id": "l31",
        "display": "Nasıl oluştu? NASA'ya göre büyük olasılıkla, milyarlarca yıl önce Mars büyüklüğünde bir gök cismi Dünya'ya çarptıktan sonra.",
        "spoken": "Nasıl oluştu? Nasa'ya göre büyük olasılıkla, milyarlarca yıl önce Mars büyüklüğünde bir gök cismi Dünya'ya çarptıktan sonra.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Karanlık bir odada masa lambasını yak: o Güneş olsun. Elindeki top Ay, sen de Dünya'sın.",
        "spoken": "Şimdi sıra sende! Karanlık bir odada masa lambasını yak: o Güneş olsun. Elindeki top Ay, sen de Dünya'sın.",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Topu kolunu uzatarak tut ve olduğun yerde yavaşça dön. Topun aydınlık kısmının nasıl değiştiğine bak: hilal, dördün, dolunay!",
        "spoken": "Topu kolunu uzatarak tut ve olduğun yerde yavaşça dön. Topun aydınlık kısmının nasıl değiştiğine bak: hilal, dördün, dolunay!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l34",
        "display": "İkinci görev: bir ay boyunca her akşam Ay'ı çiz. Böylece kendi Ay günlüğün olur.",
        "spoken": "İkinci görev: bir ay boyunca her akşam Ay'ı çiz. Böylece kendi Ay günlüğün olur.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l35",
        "display": "Bunu biliyor muydun? Ay bizden yavaş yavaş uzaklaşıyor: yılda yaklaşık 3,8 santimetre.",
        "spoken": "Bunu biliyor muydun? Ay bizden yavaş yavaş uzaklaşıyor: yılda yaklaşık üç virgül sekiz santimetre.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l36",
        "display": "Alınma, kişisel bir şey değil!",
        "spoken": "Alınma, kişisel bir şey değil!",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "Hızlı soru! Ay kendi ışığını üretir mi?",
        "spoken": "Hızlı soru! Ay kendi ışığını üretir mi?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l38",
        "display": "Düşün bakalım... Hayır! Güneş'in ışığını yansıtır.",
        "spoken": "Düşün bakalım... Hayır! Güneş'in ışığını yansıtır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l39",
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
        "id": "l40",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l41",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l42",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de gözlerimi parlatmaya gidiyorum; bu gece dolunayla yarışacağım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de gözlerimi parlatmaya gidiyorum; bu gece dolunayla yarışacağım!",
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
    "statement": "Ay kendi ışığını üretmez; 'ay ışığı' aslında yansıyan Güneş ışığıdır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Ay Dünya'nın çevresinde dolandıkça farklı kısımları farklı zamanlarda Güneş ışığında ya da karanlıkta olur; bizim bakış açımızdan Ay'ın evrelerden geçmesinin nedeni budur. Ay'ın biçimi ay boyunca değişmez; değişen bizim görüşümüzdür.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Sekiz evre sırayla: yeni ay, büyüyen hilal, ilk dördün, büyüyen şişkin ay, dolunay, küçülen şişkin ay, son dördün, küçülen hilal. Şişkin ay evresi yarım ay ile dolunay arasındadır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Ay'ın Dünya çevresindeki bir turu yaklaşık 27,3 gün sürer; bir yeni aydan ötekine ise yaklaşık 29,5 gün geçer.",
    "numbers": [
      "27.3",
      "29.5"
    ]
  },
  {
    "id": "f6",
    "statement": "Fark, Dünya'nın da hareket etmesinden (Güneş'in çevresinde dolanmasından) kaynaklanır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Ay bize sırtını hiç dönmez; eşinin çevresinde dönerken hep ona bakan bir dansçı gibidir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Dünya'dan hiç görmediğimiz yarıküreye (uzak yüz) 'karanlık yüz' denmesi yanıltıcıdır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Ay ortalama 384.400 kilometre uzaklıktadır.",
    "numbers": [
      "384.400"
    ]
  },
  {
    "id": "f10",
    "statement": "Ay'ın genişliği Dünya'nınkinin üçte birinden azdır.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Ay büyük olasılıkla, birkaç milyar yıl önce Mars büyüklüğünde bir cismin Dünya'ya çarpmasından sonra oluştu.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Ay yılda yaklaşık 3,8 santimetre hızla yavaşça uzaklaşmaktadır.",
    "numbers": [
      "3.8"
    ]
  },
  {
    "id": "f13",
    "statement": "Ay tutulmaları dolunay evresinde olur: Dünya tam olarak Ay ile Güneş arasına girince gölgesi Ay'ın yüzeyine düşer. Güneş tutulmaları yalnızca yeni ay evresinde, Ay Dünya ile Güneş arasındayken olur. Ay'ın yörüngesi Dünya'nın yörünge düzlemine göre yaklaşık 5 derece eğiktir.",
    "numbers": [
      "5"
    ]
  },
  {
    "id": "f14",
    "statement": "Ay'ın kütle çekimi Dünya'daki gelgitlere yol açar; okyanuslar kabarır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Ay gündüz de sık sık soluk biçimde görülebilir; her gün biraz daha geç doğar; dolunay gün batımı sıralarında doğar.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.",
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
