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
        "display": "Okyanus, gezegenimizin yüzeyinin %70'inden fazlasını kaplar. Ama derinlerini neredeyse hiç görmedik!",
        "spoken": "Okyanus, gezegenimizin yüzeyinin yüzde yetmişinden fazlasını kaplar. Ama derinlerini neredeyse hiç görmedik!",
        "factIds": [
          "f1",
          "f16"
        ]
      },
      {
        "id": "l2",
        "display": "Güneş ışığının hiç ulaşmadığı o karanlıkta kimler yaşıyor? Ve kendi ışığını üreten canlılar gerçek mi?",
        "spoken": "Güneş ışığının hiç ulaşmadığı o karanlıkta kimler yaşıyor? Ve kendi ışığını üreten canlılar gerçek mi?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün denizin dibine dalıyoruz!",
        "spoken": "Bugün denizin dibine dalıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Okyanus ne kadar derin? Işık ve basınç derinlikle nasıl değişir? Ve karanlıkta canlılar nasıl yaşar?",
        "spoken": "Üç sorumuz var. Okyanus ne kadar derin? Işık ve basınç derinlikle nasıl değişir? Ve karanlıkta canlılar nasıl yaşar?",
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
        "display": "ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre Dünya'daki suyun yaklaşık %97'si okyanustadır.",
        "spoken": "A Be De Ulusal Okyanus ve Atmosfer Dairesi, Noa'ya göre Dünya'daki suyun yaklaşık yüzde doksan yedisi okyanustadır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Okyanusun ortalama derinliği 3.682 metredir.",
        "spoken": "Okyanusun ortalama derinliği üç bin altı yüz seksen iki metredir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "En derin noktası Büyük Okyanus'taki Mariana Çukuru'ndadır. Challenger Derinliği denen bu yer 10.935 metre derinliktedir.",
        "spoken": "En derin noktası Büyük Okyanus'taki Mariana Çukuru'ndadır. Çelıncır Derinliği denen bu yer on bin dokuz yüz otuz beş metre derinliktedir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l9",
        "display": "Ben oraya inemem. Su geçirmezlik belgem yok!",
        "spoken": "Ben oraya inemem. Su geçirmezlik belgem yok!",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Derine indikçe iki şey hızla değişir: ışık ve basınç. Önce ışığa bakalım.",
        "spoken": "Derine indikçe iki şey hızla değişir: ışık ve basınç. Önce ışığa bakalım.",
        "factIds": []
      },
      {
        "id": "l11",
        "display": "İlk 200 metreye güneşli bölge denir. Fotosentez yalnızca burada mümkündür; çünkü daha derine neredeyse hiç ışık ulaşmaz.",
        "spoken": "İlk iki yüz metreye güneşli bölge denir. Fotosentez yalnızca burada mümkündür; çünkü daha derine neredeyse hiç ışık ulaşmaz.",
        "factIds": [
          "f3",
          "f6"
        ]
      },
      {
        "id": "l12",
        "display": "200 ile 1.000 metre arası alacakaranlık bölgesidir. Burada kayda değer ışık nadiren bulunur.",
        "spoken": "İki yüz ile bin metre arası alacakaranlık bölgesidir. Burada kayda değer ışık nadiren bulunur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "1.000 metrenin altına ise Güneş ışığı hiç ulaşmaz. Burası zifiri karanlıktır.",
        "spoken": "Bin metrenin altına ise Güneş ışığı hiç ulaşmaz. Burası zifiri karanlıktır.",
        "factIds": [
          "f5"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Şimdi basınç. Üstündeki su seni aşağı doğru iter; ne kadar derine inersen basınç o kadar artar.",
        "spoken": "Şimdi basınç. Üstündeki su seni aşağı doğru iter; ne kadar derine inersen basınç o kadar artar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l15",
        "display": "NOAA'ya göre yaklaşık her on metrede basınç bir atmosfer daha artar. Bir atmosfer, deniz kıyısında havanın üstümüze yaptığı basınç kadardır.",
        "spoken": "Noa'ya göre yaklaşık her on metrede basınç bir atmosfer daha artar. Bir atmosfer, deniz kıyısında havanın üstümüze yaptığı basınç kadardır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Peki canlılar buna nasıl dayanır? Örneğin balinaların bedenleri daha esnektir; bu sayede büyük basınç değişimlerine dayanabilirler.",
        "spoken": "Peki canlılar buna nasıl dayanır? Örneğin balinaların bedenleri daha esnektir; bu sayede büyük basınç değişimlerine dayanabilirler.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Karanlığa gelince: derinlerdeki pek çok canlı kendi ışığını üretir! Buna biyolüminesans denir: bir canlının kimyasal tepkimeyle ışık üretmesi.",
        "spoken": "Karanlığa gelince: derinlerdeki pek çok canlı kendi ışığını üretir! Buna biyolüminesans denir: bir canlının kimyasal tepkimeyle ışık üretmesi.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l18",
        "display": "200 ile 1.000 metre arasında yaşayan hayvanların %80'i biyolüminesanstır.",
        "spoken": "İki yüz ile bin metre arasında yaşayan hayvanların yüzde sekseni biyolüminesanstır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l19",
        "display": "National Geographic'e göre bu ışığı üreten maddenin adı lusiferindir. Üstelik bu soğuk bir ışıktır: çok az ısı yayar.",
        "spoken": "Neşınıl Ciyografik'e göre bu ışığı üreten maddenin adı lusiferindir. Üstelik bu soğuk bir ışıktır: çok az ısı yayar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l20",
        "display": "Canlılar bu ışığı av yakalamak, düşmandan korunmak ve eş bulmak için kullanır.",
        "spoken": "Canlılar bu ışığı av yakalamak, düşmandan korunmak ve eş bulmak için kullanır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l21",
        "display": "En ünlüsü fener balığı: başından uzanan ipliğin ucundaki topu yakar ve avını kendine çeker.",
        "spoken": "En ünlüsü fener balığı: başından uzanan ipliğin ucundaki topu yakar ve avını kendine çeker.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l22",
        "display": "Başında lamba taşıyan bir balık! Bence antenimdeki yıldızı kıskanmış.",
        "spoken": "Başında lamba taşıyan bir balık! Bence antenimdeki yıldızı kıskanmış.",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l23",
        "display": "Vampir kalamar ise tehlike anında yapışkan ve parlayan bir salgı fırlatır; düşmanını şaşırtıp oyalar.",
        "spoken": "Vampir kalamar ise tehlike anında yapışkan ve parlayan bir salgı fırlatır; düşmanını şaşırtıp oyalar.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l24",
        "display": "Derinlerde bir sürpriz daha var: hidrotermal bacalar. Deniz suyunun magmayla karşılaştığı yerlerde oluşurlar.",
        "spoken": "Derinlerde bir sürpriz daha var: hidrotermal bacalar. Deniz suyunun magmayla karşılaştığı yerlerde oluşurlar.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l25",
        "display": "Bu bacalardaki su çok sıcaktır; ama o derinlikteki aşırı basınç yüzünden kaynamaz.",
        "spoken": "Bu bacalardaki su çok sıcaktır; ama o derinlikteki aşırı basınç yüzünden kaynamaz.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l26",
        "display": "Bilim insanları bu bacaları ilk kez 1977'de, Galapagos Adaları yakınında keşfetti. Çevrelerinde daha önce hiç görülmemiş pek çok canlı vardı.",
        "spoken": "Bilim insanları bu bacaları ilk kez bin dokuz yüz yetmiş yedide, Galapagos Adaları yakınında keşfetti. Çevrelerinde daha önce hiç görülmemiş pek çok canlı vardı.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l27",
        "display": "Peki okyanusu ne kadar tanıyoruz? Nisan 2026 itibarıyla deniz tabanının yalnızca %28,7'sinin haritası çıkarılmıştı.",
        "spoken": "Peki okyanusu ne kadar tanıyoruz? Nisan iki bin yirmi altı itibarıyla deniz tabanının yalnızca yüzde yirmi sekiz virgül yedisinin haritası çıkarılmıştı.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l28",
        "display": "Derin deniz tabanının gözle görülen kısmı ise %0,001'den az!",
        "spoken": "Derin deniz tabanının gözle görülen kısmı ise yüz binde birden az!",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l29",
        "display": "Bilim insanları derinleri, gemilere takılan sonar cihazlarıyla ve uzaktan kumandalı araçlarla inceler.",
        "spoken": "Bilim insanları derinleri, gemilere takılan sonar cihazlarıyla ve uzaktan kumandalı araçlarla inceler.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l30",
        "display": "Uzaktan kumandalı araçlar benim kuzenlerim sayılır. Aile toplantılarımız biraz ıslak geçiyor!",
        "spoken": "Uzaktan kumandalı araçlar benim kuzenlerim sayılır. Aile toplantılarımız biraz ıslak geçiyor!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Tahminlere göre okyanusta 700.000 ile 1 milyon arasında tür yaşıyor olabilir.",
        "spoken": "Tahminlere göre okyanusta yedi yüz bin ile bir milyon arasında tür yaşıyor olabilir.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Büyük bir kâğıdı üçe böl: güneşli bölge, alacakaranlık bölgesi ve karanlık bölge.",
        "spoken": "Şimdi sıra sende! Büyük bir kâğıdı üçe böl: güneşli bölge, alacakaranlık bölgesi ve karanlık bölge.",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Her bölgeye oraya uygun canlılar çiz. Karanlık bölgedekileri fosforlu kalemle boya; ışığı kapatınca kendi derin denizin parlasın!",
        "spoken": "Her bölgeye oraya uygun canlılar çiz. Karanlık bölgedekileri fosforlu kalemle boya; ışığı kapatınca kendi derin denizin parlasın!",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l34",
        "display": "Bunu biliyor muydun? NOAA'ya göre biyolüminesansın asıl işlevinin ne olduğu hâlâ tam olarak bilinmiyor.",
        "spoken": "Bunu biliyor muydun? Noa'ya göre biyolüminesansın asıl işlevinin ne olduğu hâlâ tam olarak bilinmiyor.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l35",
        "display": "Hızlı soru! Fotosentez okyanusun hangi bölgesinde yapılabilir?",
        "spoken": "Hızlı soru! Fotosentez okyanusun hangi bölgesinde yapılabilir?",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l36",
        "display": "Düşün bakalım... Evet: ilk 200 metredeki güneşli bölgede!",
        "spoken": "Düşün bakalım... Evet: ilk iki yüz metredeki güneşli bölgede!",
        "factIds": [
          "f3",
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben yüzeyde kalıyorum; aşağıdaki kuzenlerime selam söyle!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben yüzeyde kalıyorum; aşağıdaki kuzenlerime selam söyle!",
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
    "statement": "Okyanus gezegenimizin yüzeyinin %70'inden fazlasını kaplar; Dünya'daki suyun yaklaşık %97'si okyanustadır.",
    "numbers": [
      "70",
      "97"
    ]
  },
  {
    "id": "f2",
    "statement": "Okyanusun ortalama derinliği 3.682 metredir.",
    "numbers": [
      "3.682"
    ]
  },
  {
    "id": "f3",
    "statement": "Okyanusun üst 200 metresine öfotik, yani 'güneşli' bölge denir.",
    "numbers": [
      "200"
    ]
  },
  {
    "id": "f4",
    "statement": "200–1.000 metre arası genellikle 'alacakaranlık' bölgesi olarak anılır; 200 metrenin ötesinde kayda değer ışık nadiren bulunur.",
    "numbers": [
      "200",
      "1.000"
    ]
  },
  {
    "id": "f5",
    "statement": "Afotik bölge 1.000 metrenin altındadır; Güneş ışığı ulaşmaz, bölge karanlıktır.",
    "numbers": [
      "1.000"
    ]
  },
  {
    "id": "f6",
    "statement": "200 metrenin ötesine o kadar az ışık ulaşır ki fotosentez artık mümkün olmaz.",
    "numbers": [
      "200"
    ]
  },
  {
    "id": "f7",
    "statement": "Her 33 fitte (10,06 metre) basınç bir atmosfer artar; deniz seviyesinde çevremizdeki hava bedenimize basınç uygular.",
    "numbers": [
      "10.06"
    ]
  },
  {
    "id": "f8",
    "statement": "Denizde ne kadar derine inilirse üstteki suyun aşağı doğru yaptığı basınç o kadar artar; balinalar bedenleri daha esnek olduğu için büyük basınç değişimlerine dayanabilir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Okyanusun en derin yeri 10.935 metredir; Büyük Okyanus'taki Mariana Çukuru'nda, Challenger Derinliği denen yerdedir.",
    "numbers": [
      "10.935"
    ]
  },
  {
    "id": "f10",
    "statement": "Biyolüminesans, bir canlının kimyasal tepkimeyle ürettiği ışıktır; okyanusta çok yaygındır; 200 ile 1.000 metre arasında yaşayan hayvanların %80'i biyolüminesanstır.",
    "numbers": [
      "200",
      "1.000",
      "80"
    ]
  },
  {
    "id": "f11",
    "statement": "Biyolüminesans 'soğuk ışıktır': çok az ısı yayar. Işığı asıl üreten bileşik lusiferindir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Canlılar biyolüminesansı av yakalamak, avcılardan korunmak ve eş bulmak için kullanır; yine de asıl amacı ya da işlevi tam olarak bilinmiyor.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Fener balığı avını çekmek için biyolüminesans kullanır; ipliğin ucundaki topu yakabilir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Vampir kalamar, avcıları ürkütüp şaşırtan ve oyalayan yapışkan, biyolüminesans bir salgı fırlatır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Hidrotermal bacalar deniz suyunun magmayla karşılaştığı yerlerde oluşur; buradaki sıcak su, derinlikteki aşırı basınç nedeniyle kaynamaz; ilk kez 1977'de Galapagos Adaları yakınında keşfedildi ve çevrelerinde daha önce hiç görülmemiş çok sayıda canlı vardı.",
    "numbers": [
      "1977"
    ]
  },
  {
    "id": "f16",
    "statement": "Nisan 2026 itibarıyla küresel deniz tabanının %28,7'sinin haritası çıkarılmıştı; kâşifler derin okyanus tabanının %0,001'inden azını görmüştür.",
    "numbers": [
      "2026",
      "28.7",
      "0.001"
    ]
  },
  {
    "id": "f17",
    "statement": "Derinler, uzaktan kumandalı araçlar gibi dalış araçlarıyla ve genellikle gemilere takılan sonarla incelenir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Bilim insanlarının tahminine göre okyanusta 700.000 ile 1 milyon arasında tür olabilir.",
    "numbers": [
      "700.000",
      "1"
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
