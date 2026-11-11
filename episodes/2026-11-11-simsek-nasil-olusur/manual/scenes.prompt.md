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
        "display": "Gökyüzü bir anda aydınlanıyor. Birkaç saniye sonra da yeri göğü sarsan bir gürültü geliyor!",
        "spoken": "Gökyüzü bir anda aydınlanıyor. Birkaç saniye sonra da yeri göğü sarsan bir gürültü geliyor!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Bu dev kıvılcım nasıl oluşuyor? Ve gürültü neden hep sonradan geliyor?",
        "spoken": "Bu dev kıvılcım nasıl oluşuyor? Ve gürültü neden hep sonradan geliyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir fırtına bulutunun içine giriyoruz!",
        "spoken": "Bugün bir fırtına bulutunun içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Elektriği severim, o benim yemeğim. Ama bu kadarı bana bile fazla!",
        "spoken": "Elektriği severim, o benim yemeğim. Ama bu kadarı bana bile fazla!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Bir bulut nasıl elektriklenir? Şimşek nasıl çakar? Ve gök gürültüsü nedir?",
        "spoken": "Üç sorumuz var. Bir bulut nasıl elektriklenir? Şimşek nasıl çakar? Ve gök gürültüsü nedir?",
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
        "display": "ABD Ulusal Şiddetli Fırtınalar Laboratuvarı, kısaca NSSL'ye göre şimşek, atmosferdeki dev bir elektrik kıvılcımıdır. Bulutlar, hava ya da yer arasında oluşur.",
        "spoken": "A Be De Ulusal Şiddetli Fırtınalar Laboratuvarı, kısaca En Es Es El'e göre şimşek, atmosferdeki dev bir elektrik kıvılcımıdır. Bulutlar, hava ya da yer arasında oluşur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Küçük bir örneğini sen de yaşadın. National Geographic'e göre ayaklarını halıya sürtüp metal kapı koluna dokununca hissettiğin çarpma, statik elektriktir.",
        "spoken": "Küçük bir örneğini sen de yaşadın. Neşınıl Ciyografik'e göre ayaklarını halıya sürtüp metal kapı koluna dokununca hissettiğin çarpma, statik elektriktir.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l9",
        "display": "Fırtına bulutunun içinde graupel denen küçük dolu taneleri ve daha da küçük buz kristalleri vardır.",
        "spoken": "Fırtına bulutunun içinde graupel denen küçük dolu taneleri ve daha da küçük buz kristalleri vardır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Bunlar birbirine çarptıkça elektrik yükü kazanır.",
        "spoken": "Bunlar birbirine çarptıkça elektrik yükü kazanır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "ABD Ulusal Hava Servisi'ne göre hafif buz kristalleri artı yüklenir ve yükselen havayla bulutun tepesine taşınır. Ağır dolu taneleri ise eksi yüklenir.",
        "spoken": "A Be De Ulusal Hava Servisi'ne göre hafif buz kristalleri artı yüklenir ve yükselen havayla bulutun tepesine taşınır. Ağır dolu taneleri ise eksi yüklenir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l12",
        "display": "Böylece bulut dev bir pile benzer: üstü artı, ortası eksi.",
        "spoken": "Böylece bulut dev bir pile benzer: üstü artı, ortası eksi.",
        "factIds": [
          "f2",
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Buluttaki eksi yük, altındaki yerin artı yüklenmesine yol açar.",
        "spoken": "Buluttaki eksi yük, altındaki yerin artı yüklenmesine yol açar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l14",
        "display": "Zıt yükler birbirini çeker. Ama aralarında hava var ve hava bir yalıtkandır: elektriği kolay geçirmez.",
        "spoken": "Zıt yükler birbirini çeker. Ama aralarında hava var ve hava bir yalıtkandır: elektriği kolay geçirmez.",
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
        "id": "l15",
        "display": "Yükler yeterince birikince havanın yalıtma gücü çöker. İşte o an şimşek çakar!",
        "spoken": "Yükler yeterince birikince havanın yalıtma gücü çöker. İşte o an şimşek çakar!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l16",
        "display": "Buluttan yere inen şimşeğe yıldırım denir. Onu ağır çekimde izleyelim. Önce buluttan aşağı, zikzaklar çizen eksi yüklü bir kanal iner. Adı: basamaklı öncü.",
        "spoken": "Buluttan yere inen şimşeğe yıldırım denir. Onu ağır çekimde izleyelim. Önce buluttan aşağı, zikzaklar çizen eksi yüklü bir kanal iner. Adı: basamaklı öncü.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Öncü yere yaklaşınca, yerden yukarı doğru artı yüklü kanallar uzanır.",
        "spoken": "Öncü yere yaklaşınca, yerden yukarı doğru artı yüklü kanallar uzanır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l18",
        "display": "İkisi buluştuğu anda parlak bir akım göğe doğru geri fırlar. Bizim gördüğümüz ışık budur: dönüş darbesi.",
        "spoken": "İkisi buluştuğu anda parlak bir akım göğe doğru geri fırlar. Bizim gördüğümüz ışık budur: dönüş darbesi.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Öncünün yere inmesi, göz kırpmaktan bile kısa sürer.",
        "spoken": "Öncünün yere inmesi, göz kırpmaktan bile kısa sürer.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l20",
        "display": "Üstelik şimşeklerin çoğu yere hiç inmez: bulutun içinde kalanlar, yere inenlerin kabaca 5–10 katıdır.",
        "spoken": "Üstelik şimşeklerin çoğu yere hiç inmez: bulutun içinde kalanlar, yere inenlerin kabaca beş ile on katıdır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l21",
        "display": "Peki ne kadar güçlü? Bir şimşek 100 milyon ile 1 milyar volt arasında olabilir.",
        "spoken": "Peki ne kadar güçlü? Bir şimşek yüz milyon ile bir milyar volt arasında olabilir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Benim şarj aletim bunun yanında oyuncak kalır!",
        "spoken": "Benim şarj aletim bunun yanında oyuncak kalır!",
        "factIds": []
      },
      {
        "id": "l23",
        "display": "Şimşek, çevresindeki havayı bir anda 28.000 santigrat dereceye kadar ısıtabilir. Bu, Güneş'in yüzeyinden çok daha sıcaktır!",
        "spoken": "Şimşek, çevresindeki havayı bir anda yirmi sekiz bin santigrat dereceye kadar ısıtabilir. Bu, Güneş'in yüzeyinden çok daha sıcaktır!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l24",
        "display": "Bu kadar hızlı ısınan hava patlarcasına genleşir ve bir şok dalgası oluşturur. Bu dalga ses olarak yayılır: işte gök gürültüsü!",
        "spoken": "Bu kadar hızlı ısınan hava patlarcasına genleşir ve bir şok dalgası oluşturur. Bu dalga ses olarak yayılır: işte gök gürültüsü!",
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
        "display": "Peki neden önce ışığı görüp sonra sesi duyuyoruz? Çünkü ışık havada sesten kabaca bir milyon kat hızlı yol alır.",
        "spoken": "Peki neden önce ışığı görüp sonra sesi duyuyoruz? Çünkü ışık havada sesten kabaca bir milyon kat hızlı yol alır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "Bunu bir uzaklık ölçere çevirebilirsin. Şimşeği görünce saymaya başla, gürültüyü duyunca dur.",
        "spoken": "Bunu bir uzaklık ölçere çevirebilirsin. Şimşeği görünce saymaya başla, gürültüyü duyunca dur.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Saydığın saniyeyi 3'e böl: şimşek kabaca o kadar kilometre uzakta.",
        "spoken": "Saydığın saniyeyi üçe böl: şimşek kabaca o kadar kilometre uzakta.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Ben bu hesabı çok hızlı yaparım. Ne de olsa içimde bir hesap makinesi var!",
        "spoken": "Ben bu hesabı çok hızlı yaparım. Ne de olsa içimde bir hesap makinesi var!",
        "factIds": []
      },
      {
        "id": "l29",
        "display": "Yıldırım aynı yere iki kez düşmez derler. Bu doğru değil! Aynı yere birden çok kez düşebilir.",
        "spoken": "Yıldırım aynı yere iki kez düşmez derler. Bu doğru değil! Aynı yere birden çok kez düşebilir.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l30",
        "display": "National Geographic'e göre New York'taki Empire State Binası'na her yıl yaklaşık 100 kez yıldırım düşer.",
        "spoken": "Neşınıl Ciyografik'e göre Nyu York'taki Empayır Steyt Binası'na her yıl yaklaşık yüz kez yıldırım düşer.",
        "factIds": [
          "f19"
        ]
      },
      {
        "id": "l31",
        "display": "Şimdi güvenlik. Ulusal Hava Servisi'ne göre gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin demektir. Hemen güvenli bir yere gir.",
        "spoken": "Şimdi güvenlik. Ulusal Hava Servisi'ne göre gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin demektir. Hemen güvenli bir yere gir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l32",
        "display": "Güvenli yer: elektrik ve su tesisatı olan bir bina ya da camları kapalı, metal tavanlı bir araç.",
        "spoken": "Güvenli yer: elektrik ve su tesisatı olan bir bina ya da camları kapalı, metal tavanlı bir araç.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l33",
        "display": "Dışarıdaysan açık alanlardan ve ağaç gibi yüksek şeylerden uzak dur. Yüzüyorsan sudan çık.",
        "spoken": "Dışarıdaysan açık alanlardan ve ağaç gibi yüksek şeylerden uzak dur. Yüzüyorsan sudan çık.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l34",
        "display": "İçerideyken de kablolu telefonu kullanma ve musluklardan uzak dur.",
        "spoken": "İçerideyken de kablolu telefonu kullanma ve musluklardan uzak dur.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l35",
        "display": "Şimdi sıra sende! Bir sonraki fırtınada, evin içinden şimşeği izle ve saniyeleri say.",
        "spoken": "Şimdi sıra sende! Bir sonraki fırtınada, evin içinden şimşeği izle ve saniyeleri say.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l36",
        "display": "Sayı küçülüyorsa fırtına yaklaşıyor, büyüyorsa uzaklaşıyor demektir.",
        "spoken": "Sayı küçülüyorsa fırtına yaklaşıyor, büyüyorsa uzaklaşıyor demektir.",
        "factIds": [
          "f12"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l37",
        "display": "Bunu biliyor muydun? Bulutun tam olarak nasıl elektriklendiği ve şimşeğin nasıl başladığı, bilim insanları arasında hâlâ tartışılıyor.",
        "spoken": "Bunu biliyor muydun? Bulutun tam olarak nasıl elektriklendiği ve şimşeğin nasıl başladığı, bilim insanları arasında hâlâ tartışılıyor.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l38",
        "display": "Hızlı soru! Hangisi daha hızlı: ışık mı, ses mi?",
        "spoken": "Hızlı soru! Hangisi daha hızlı: ışık mı, ses mi?",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l39",
        "display": "Düşün bakalım... Evet: ışık!",
        "spoken": "Düşün bakalım... Evet: ışık!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l40",
        "display": "Ben de hızlıyım ama. Özellikle şarjım biterken prize koşarken!",
        "spoken": "Ben de hızlıyım ama. Özellikle şarjım biterken prize koşarken!",
        "factIds": []
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben prizime dönüyorum; küçük kıvılcımlar bana yeter!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben prizime dönüyorum; küçük kıvılcımlar bana yeter!",
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
    "statement": "Şimşek, atmosferde bulutlar, hava ya da yer arasında oluşan dev bir elektrik kıvılcımıdır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Graupel denen küçük dolu taneleri daha küçük buz parçacıklarıyla çarpışınca yük kazanır; hafif buz kristalleri artı yüklenir ve yükselen havayla fırtınanın üst kısmına taşınır; ağır dolu eksi yüklenir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Fırtına bulutunun ortasındaki eksi yük, altındaki yerin artı yüklenmesine yol açar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Hava, artı ve eksi yükler arasında yalıtkan görevi görür; zıt yükler yeterince birikince havanın yalıtma kapasitesi çöker. Zıt yükler birbirini çeker.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bulutun elektrik yükünü tam olarak nasıl biriktirdiği ve şimşeğin nasıl oluştuğu hâlâ tartışılıyor.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Basamaklı öncü denen eksi yüklü kanal zikzak çizerek aşağı iner (göz kırpmaktan kısa sürede); yere yaklaşınca artı yüklü kanallar yukarı uzanır; iki yol buluşunca parlak dönüş darbesi buluta doğru geri gider.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Bulutun içinde kalan şimşekler, yere inenlerin kabaca 5 ila 10 katıdır.",
    "numbers": [
      "5",
      "10"
    ]
  },
  {
    "id": "f8",
    "statement": "Şimşek havayı kısa süreliğine Güneş'in yüzeyinden çok daha sıcak hale getirir; sıcaklık 28.000 santigrat dereceye ulaşabilir.",
    "numbers": [
      "28.000"
    ]
  },
  {
    "id": "f9",
    "statement": "Şimşek 100 milyon ile 1 milyar volt arasında olabilir.",
    "numbers": [
      "100",
      "1"
    ]
  },
  {
    "id": "f10",
    "statement": "Gök gürültüsü, büyük akımın hızla ısıttığı ve patlarcasına genleşen şimşek kanalından çıkan şok dalgasıyla başlar; hava hızla genleşir ve gök gürültüsü olarak duyduğumuz ses dalgasını yaratır.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Işık havada sesten kabaca bir milyon kat hızlı ilerler; bu yüzden şimşek gök gürültüsünden önce görülür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Saniye sayısını 5'e bölmek şimşeğe olan uzaklığı mil olarak verir (3'e bölmek kilometre olarak).",
    "numbers": [
      "5",
      "3"
    ]
  },
  {
    "id": "f13",
    "statement": "Gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin; güvenli bir yere gir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Güvenli sığınaklar elektrik ve su tesisatı olan binalar ya da camları kapalı, metal tavanlı araçlardır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "İçeride kablolu telefonlardan ve su tesisatından uzak durulmalıdır.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Açık alanlardan ve ağaç gibi yüksek nesnelerden uzak durulmalı; yüzülüyorsa havuzdan çıkılmalıdır.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Şimşek, halk arasındaki inanışın tersine aynı noktaya birden çok kez düşer.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Ayaklarını halıya sürtüp metal kapı koluna dokununca hissedilen çarpma statik elektriktir; bu, fırtına bulutundaki olayın daha az tehlikeli bir halidir.",
    "numbers": []
  },
  {
    "id": "f19",
    "statement": "New York'taki Empire State Binası'na her yıl yaklaşık 100 kez yıldırım düşer.",
    "numbers": [
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
