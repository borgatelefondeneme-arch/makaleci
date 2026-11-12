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
        "display": "Bir zamanlar bu gezegende dev dinozorlar dolaşıyordu. Sonra bir gün, her şey değişti.",
        "spoken": "Bir zamanlar bu gezegende dev dinozorlar dolaşıyordu. Sonra bir gün, her şey değişti.",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Dinozorları ne yok etti? Ve bunu milyonlarca yıl sonra nasıl bilebiliyoruz?",
        "spoken": "Dinozorları ne yok etti? Ve bunu milyonlarca yıl sonra nasıl bilebiliyoruz?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Dünya tarihinin en ünlü dedektiflik hikâyesini çözüyoruz!",
        "spoken": "Bugün Dünya tarihinin en ünlü dedektiflik hikâyesini çözüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. O gün ne oldu? Bilim insanları bunu nereden biliyor? Ve kimler hayatta kaldı?",
        "spoken": "Üç sorumuz var. O gün ne oldu? Bilim insanları bunu nereden biliyor? Ve kimler hayatta kaldı?",
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
        "display": "Londra'daki Doğa Tarihi Müzesi'ne göre 66 milyon yıl önce dinozorlar çok kötü bir gün geçirdi.",
        "spoken": "Londra'daki Doğa Tarihi Müzesi'ne göre altmış altı milyon yıl önce dinozorlar çok kötü bir gün geçirdi.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Dünya'daki hayvanların yaklaşık %75'i aynı dönemde yok oldu.",
        "spoken": "Dünya'daki hayvanların yaklaşık yüzde yetmiş beşi aynı dönemde yok oldu.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Bu kadar çok canlının birlikte yok olmasına kitlesel yok oluş denir. National Geographic'e göre bu, Dünya tarihindeki beşinci kitlesel yok oluştu.",
        "spoken": "Bu kadar çok canlının birlikte yok olmasına kitlesel yok oluş denir. Neşınıl Ciyografik'e göre bu, Dünya tarihindeki beşinci kitlesel yok oluştu.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l9",
        "display": "Baş şüpheli: bir asteroit. Asteroitler, Güneş'in çevresinde dolanan kayalık gök cisimleridir.",
        "spoken": "Baş şüpheli: bir asteroit. Asteroitler, Güneş'in çevresinde dolanan kayalık gök cisimleridir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "NASA'ya göre Güneş sisteminin yaklaşık 4,6 milyar yıl önceki oluşumundan arta kalan parçalardır.",
        "spoken": "Nasa'ya göre Güneş sisteminin yaklaşık dört virgül altı milyar yıl önceki oluşumundan arta kalan parçalardır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Bu asteroidin genişliği 10–15 kilometre arasındaydı ve bugünkü Meksika'da, Yucatán Yarımadası'na çarptı.",
        "spoken": "Bu asteroidin genişliği on ile on beş kilometre arasındaydı ve bugünkü Meksika'da, Yukatan Yarımadası'na çarptı.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Çok yüksek hızla çarptı ve adeta buharlaştı. Geriye 150 kilometre çapında bir krater bıraktı: Chicxulub krateri.",
        "spoken": "Çok yüksek hızla çarptı ve adeta buharlaştı. Geriye yüz elli kilometre çapında bir krater bıraktı: Çikşulub krateri.",
        "factIds": [
          "f4",
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Chicxulub. Söylemesi zor, biliyorum. Benim ses kartım bile iki kez denedi!",
        "spoken": "Çik, şu, lub. Söylemesi zor, biliyorum. Benim ses kartım bile iki kez denedi!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Çarpışma anında dev bir patlama dalgası ve sıcak dalgası yayıldı. Atmosfere çok büyük miktarda madde savruldu.",
        "spoken": "Çarpışma anında dev bir patlama dalgası ve sıcak dalgası yayıldı. Atmosfere çok büyük miktarda madde savruldu.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Dev dalgalar Amerika kıtalarının bazı bölgelerini kapladı. Büyük yangınlar çıktı.",
        "spoken": "Dev dalgalar Amerika kıtalarının bazı bölgelerini kapladı. Büyük yangınlar çıktı.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Ama asıl felaket sonra geldi. Kurum bütün Dünya'ya yayıldı.",
        "spoken": "Ama asıl felaket sonra geldi. Kurum bütün Dünya'ya yayıldı.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Güneş tamamen kapanmadı; ama yeryüzüne ulaşan ışık azaldı. Bu da bitkilerin büyümesini etkiledi.",
        "spoken": "Güneş tamamen kapanmadı; ama yeryüzüne ulaşan ışık azaldı. Bu da bitkilerin büyümesini etkiledi.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Gerisi domino taşları gibiydi: etki, besin zincirinin basamaklarını birer birer devirdi ve ekosistem çöktü.",
        "spoken": "Gerisi domino taşları gibiydi: etki, besin zincirinin basamaklarını birer birer devirdi ve ekosistem çöktü.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Peki bunu nereden biliyoruz? İpucu, kayaların arasındaki ince bir kil tabakasında saklı.",
        "spoken": "Peki bunu nereden biliyoruz? İpucu, kayaların arasındaki ince bir kil tabakasında saklı.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "1980'de fizikçi Luis Alvarez ve jeolog oğlu Walter, iridyumca zengin bu kil tabakasının büyük bir asteroit çarpmasından kaynaklandığını öne sürdü.",
        "spoken": "Bin dokuz yüz seksende fizikçi Luis Alvares ve jeolog oğlu Voltır, iridyumca zengin bu kil tabakasının büyük bir asteroit çarpmasından kaynaklandığını öne sürdü.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "İridyum, Dünya'da bulunan en nadir metallerden biridir.",
        "spoken": "İridyum, Dünya'da bulunan en nadir metallerden biridir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Keşke ben de nadir bir metalden yapılmış olsaydım. Ama çoğum alüminyum!",
        "spoken": "Keşke ben de nadir bir metalden yapılmış olsaydım. Ama çoğum alüminyum!",
        "factIds": []
      },
      {
        "id": "l23",
        "display": "Başta bu fikir tartışmalıydı. Sonra krater bulundu: yaşı, yok oluşla tam olarak aynıydı!",
        "spoken": "Başta bu fikir tartışmalıydı. Sonra krater bulundu: yaşı, yok oluşla tam olarak aynıydı!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Bugün bu, en yaygın kabul gören açıklamadır.",
        "spoken": "Bugün bu, en yaygın kabul gören açıklamadır.",
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
        "id": "l25",
        "display": "Ama suçlu yalnızca asteroit değil. Çarpışmadan önce de Dünya'nın iklimi değişiyordu.",
        "spoken": "Ama suçlu yalnızca asteroit değil. Çarpışmadan önce de Dünya'nın iklimi değişiyordu.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "Bugünkü Hindistan'ın orta kesiminde iki milyon yıl boyunca çok yoğun volkanik etkinlik yaşandı.",
        "spoken": "Bugünkü Hindistan'ın orta kesiminde iki milyon yıl boyunca çok yoğun volkanik etkinlik yaşandı.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Müzeye göre asteroit, son ve öldürücü darbe oldu. Yok oluşun tam olarak nasıl işlediği ise hâlâ tartışılıyor.",
        "spoken": "Müzeye göre asteroit, son ve öldürücü darbe oldu. Yok oluşun tam olarak nasıl işlediği ise hâlâ tartışılıyor.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Kimler yok oldu? Uçan sürüngenler pterozorlar, büyük deniz sürüngenleri ve ammonitler. Ağırlığı 25 kilogramı geçen bütün kara hayvanları da.",
        "spoken": "Kimler yok oldu? Uçan sürüngenler pterozorlar, büyük deniz sürüngenleri ve ammonitler. Ağırlığı yirmi beş kilogramı geçen bütün kara hayvanları da.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l29",
        "display": "Ben o sınırın altındayım. Hafif olmanın iyi yanları da var!",
        "spoken": "Ben o sınırın altındayım. Hafif olmanın iyi yanları da var!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Peki kimler kurtuldu? Hayatta kalanlar küçüktü. Bitkiler de hayvanlardan daha az etkilendi; çünkü tohumları ve polenleri zor dönemlere daha uzun dayanabilir.",
        "spoken": "Peki kimler kurtuldu? Hayatta kalanlar küçüktü. Bitkiler de hayvanlardan daha az etkilendi; çünkü tohumları ve polenleri zor dönemlere daha uzun dayanabilir.",
        "factIds": [
          "f13",
          "f14"
        ]
      },
      {
        "id": "l31",
        "display": "Ve işte büyük sürpriz: dinozorların hepsi yok olmadı. Dinozorlar, kuşlar olarak hayatta kaldı!",
        "spoken": "Ve işte büyük sürpriz: dinozorların hepsi yok olmadı. Dinozorlar, kuşlar olarak hayatta kaldı!",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l32",
        "display": "Kuşlar, teropod denen etçil bir dinozor grubundan evrildi. Küçük olmaları, çok çeşitli besinler yiyebilmeleri ve uçabilmeleri büyük olasılıkla onlara yardım etti.",
        "spoken": "Kuşlar, teropod denen etçil bir dinozor grubundan evrildi. Küçük olmaları, çok çeşitli besinler yiyebilmeleri ve uçabilmeleri büyük olasılıkla onlara yardım etti.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l33",
        "display": "Bugün en az 11.000 kuş türü var. Yani penceredeki serçe, yaşayan bir dinozor!",
        "spoken": "Bugün en az on bir bin kuş türü var. Yani penceredeki serçe, yaşayan bir dinozor!",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l34",
        "display": "Bir dahaki sefere bir güvercin görürsen selam ver. Sonuçta çok eski bir aileden geliyor!",
        "spoken": "Bir dahaki sefere bir güvercin görürsen selam ver. Sonuçta çok eski bir aileden geliyor!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "National Geographic'e göre dinozorların yok oluşu, memelilerin gelişip büyümesine olanak verdi.",
        "spoken": "Neşınıl Ciyografik'e göre dinozorların yok oluşu, memelilerin gelişip büyümesine olanak verdi.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l36",
        "display": "Şimdi sıra sende! Dört domino taşı diz ve üzerlerine küçük kâğıtlarla şunları yaz: Güneş ışığı, bitki, otçul, etçil.",
        "spoken": "Şimdi sıra sende! Dört domino taşı diz ve üzerlerine küçük kâğıtlarla şunları yaz: Güneş ışığı, bitki, otçul, etçil.",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "İlk taşı devir. Zincirin bir halkası bozulunca ötekilere ne oluyor? Ekosistemin çöküşü işte böyle işler.",
        "spoken": "İlk taşı devir. Zincirin bir halkası bozulunca ötekilere ne oluyor? Ekosistemin çöküşü işte böyle işler.",
        "factIds": [
          "f8"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l38",
        "display": "Bunu biliyor muydun? NASA'nın bir birimi, Dünya için tehlike oluşturabilecek asteroitleri bulmak ve izlemekle görevli.",
        "spoken": "Bunu biliyor muydun? Nasa'nın bir birimi, Dünya için tehlike oluşturabilecek asteroitleri bulmak ve izlemekle görevli.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l39",
        "display": "Hızlı soru! Dinozorların bugün yaşayan temsilcileri hangi hayvanlar?",
        "spoken": "Hızlı soru! Dinozorların bugün yaşayan temsilcileri hangi hayvanlar?",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l40",
        "display": "Düşün bakalım... Evet: kuşlar!",
        "spoken": "Düşün bakalım... Evet: kuşlar!",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l41",
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
        "id": "l42",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l43",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l44",
        "display": "Abone olmayı ve zili açmayı unutma. Arada bir gökyüzüne bakmayı da!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Arada bir gökyüzüne bakmayı da!",
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
    "statement": "66 milyon yıl önce dinozorlar çok kötü bir gün geçirdi; yok oluşun tarihi 66,0 milyon yıl öncedir.",
    "numbers": [
      "66"
    ]
  },
  {
    "id": "f2",
    "statement": "Dünya'daki hayvanların yaklaşık %75'i, dinozorlar dahil, aynı zamanda aniden yok oldu.",
    "numbers": [
      "75"
    ]
  },
  {
    "id": "f3",
    "statement": "Asteroitler Güneş'in çevresinde dolanan büyük, kayalık cisimlerdir; Güneş sisteminin yaklaşık 4,6 milyar yıl önceki oluşumundan arta kalan parçalardır. Bu asteroidin 10–15 kilometre genişliğinde olduğu düşünülüyor.",
    "numbers": [
      "4.6",
      "10",
      "15"
    ]
  },
  {
    "id": "f4",
    "statement": "Çarpma yeri Chicxulub krateri olarak bilinir ve merkezi Meksika'daki Yucatán Yarımadası'ndadır; krater 150 kilometre çapındadır.",
    "numbers": [
      "150"
    ]
  },
  {
    "id": "f5",
    "statement": "Asteroit yüksek hızla çarptı ve fiilen buharlaştı; dev bir patlama dalgası ve sıcak dalgası yayıldı, atmosfere çok büyük miktarda madde savruldu.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Dev dalgalar Amerika kıtalarının bazı bölgelerini kapladı; büyük yangınların kanıtları da var.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Kurum bütün dünyaya yayıldı; Güneş'i tamamen kapatmadı ama yeryüzüne ulaşan ışığı azalttı ve bitki büyümesini etkiledi.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Domino taşları gibi, bu durum besin zincirinin üst basamaklarını etkiledi ve ekosistemin çökmesine yol açtı.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "1980'de fizikçi Luis Walter Alvarez ve jeolog oğlu Walter, iridyumca zengin tarihsel bir kil tabakasının büyük bir asteroidin Dünya'ya çarpmasından kaynaklandığı kuramını yayımladı. İridyum Dünya'da bulunan en nadir metallerden biridir.",
    "numbers": [
      "1980"
    ]
  },
  {
    "id": "f10",
    "statement": "Alvarez hipotezi başta tartışmalıydı ama bugün en yaygın kabul gören kuramdır; krater bulunmuştur ve yaşı kuş olmayan dinozorların yok oluşuyla tam olarak aynıdır.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Suç yalnızca asteroitte değildir: çarpışmadan önce Dünya bir iklim değişikliği dönemindeydi; bugünkü Hindistan'ın orta kesiminde iki milyon yıl boyunca çok büyük volkanik etkinlik sürdü; asteroit son, öldürücü darbeydi. Öldürme mekanizması hâlâ tartışılıyor.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Ammonitler, bazı mikroskobik planktonlar, pterozorlar ve büyük deniz sürüngenleri yok oldu; ağırlığı 25 kilogramın üstündeki bütün kara hayvanları da yok oldu.",
    "numbers": [
      "25"
    ]
  },
  {
    "id": "f13",
    "statement": "Bitkiler hayvanlardan daha az etkilendi; çünkü tohumları ve polenleri zor dönemlere daha uzun dayanabilir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Hayatta kalanlar başlangıçta küçüktü; kuş olmayan bütün dinozorlar yok oldu ama dinozorlar kuşlar olarak hayatta kaldı.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Kuşlar teropod denen etçil bir dinozor grubundan evrildi; hayatta kalmalarında büyük olasılıkla küçük bedenleri, çok farklı besinler yiyebilmeleri ve uçabilmeleri etkili oldu; bugün en az 11.000 kuş türü vardır.",
    "numbers": [
      "11.000"
    ]
  },
  {
    "id": "f16",
    "statement": "Dinozorların yok oluşu memelilerin gelişip büyümesine olanak verdi.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "NASA'nın bir birimi, Dünya için çarpma tehlikesi oluşturabilecek asteroit ve kuyrukluyıldızları bulma, izleme ve daha iyi anlama görevini yürütür.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Yaklaşık 66 milyon yıl önce, Kretase döneminin sonunda beşinci kitlesel yok oluş yaşandı.",
    "numbers": [
      "66"
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
