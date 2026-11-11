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
        "display": "Bir dağ düşün. İçinden, bin derecenin üstünde sıcaklıkta erimiş kaya fışkırıyor!",
        "spoken": "Bir dağ düşün. İçinden, bin derecenin üstünde sıcaklıkta erimiş kaya fışkırıyor!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l2",
        "display": "Bu kaya nereden geliyor? Ve neden bazı volkanlar sakince akarken bazıları patlıyor?",
        "spoken": "Bu kaya nereden geliyor? Ve neden bazı volkanlar sakince akarken bazıları patlıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir volkanın içine iniyoruz!",
        "spoken": "Bugün bir volkanın içine iniyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Merak etme, ben sıcağa alışkınım. İşlemcim bazen fena ısınıyor!",
        "spoken": "Merak etme, ben sıcağa alışkınım. İşlemcim bazen fena ısınıyor!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Magma nedir ve neden yükselir? Bir volkanı patlatan şey nedir? Ve bilim insanları püskürmeyi önceden nasıl anlar?",
        "spoken": "Üç sorumuz var. Magma nedir ve neden yükselir? Bir volkanı patlatan şey nedir? Ve bilim insanları püskürmeyi önceden nasıl anlar?",
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
        "display": "ABD Jeoloji Araştırmaları Kurumu, kısaca USGS'ye göre volkan; lavın, kaya parçalarının ve buharın yeryüzüne çıktığı bir açıklıktır.",
        "spoken": "A Be De Jeoloji Araştırmaları Kurumu, kısaca Yu Es Ci Es'e göre volkan; lavın, kaya parçalarının ve buharın yeryüzüne çıktığı bir açıklıktır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Önce iki kelimeyi ayıralım. Erimiş kaya yerin altındayken ona magma denir. Yüzeye çıktığında adı lav olur.",
        "spoken": "Önce iki kelimeyi ayıralım. Erimiş kaya yerin altındayken ona magma denir. Yüzeye çıktığında adı lav olur.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Magma, yerin çok derinlerinde oluşur. Çevresindeki katı kayadan daha hafiftir, yani daha az yoğundur. Bu yüzden yukarı doğru yükselir.",
        "spoken": "Magma, yerin çok derinlerinde oluşur. Çevresindeki katı kayadan daha hafiftir, yani daha az yoğundur. Bu yüzden yukarı doğru yükselir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Tıpkı suyun dibine bastırdığın bir mantarın yüzeye çıkması gibi.",
        "spoken": "Tıpkı suyun dibine bastırdığın bir mantarın yüzeye çıkması gibi.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Yükselen magma, volkanın içindeki bir odada toplanır: magma odası. Burada basınç giderek artar.",
        "spoken": "Yükselen magma, volkanın içindeki bir odada toplanır: magma odası. Burada basınç giderek artar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Peki magma nerelerde yükselir? NASA'ya göre yer kabuğu, tektonik levha denen parçalardan oluşur ve bu levhalar yavaşça hareket eder.",
        "spoken": "Peki magma nerelerde yükselir? Nasa'ya göre yer kabuğu, tektonik levha denen parçalardan oluşur ve bu levhalar yavaşça hareket eder.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Levhalar birbirinden uzaklaşırken aradan magma yükselir. Birbirine doğru ilerlerken ise kabuğun bir kısmı derine itilir, orada erir ve magma olarak yükselir.",
        "spoken": "Levhalar birbirinden uzaklaşırken aradan magma yükselir. Birbirine doğru ilerlerken ise kabuğun bir kısmı derine itilir, orada erir ve magma olarak yükselir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Üçüncü yol: sıcak noktalar. Hawaii'nin volkanları böyle bir sıcak noktanın üstünde oluşmuştur.",
        "spoken": "Üçüncü yol: sıcak noktalar. Havai'nin volkanları böyle bir sıcak noktanın üstünde oluşmuştur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Volkanların birçoğu Büyük Okyanus'un çevresinde dizilir. Bu kuşağın adı: Ateş Çemberi.",
        "spoken": "Volkanların birçoğu Büyük Okyanus'un çevresinde dizilir. Bu kuşağın adı: Ateş Çemberi.",
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
        "id": "l16",
        "display": "Şimdi asıl soru: volkanı patlatan nedir? Cevap: gaz!",
        "spoken": "Şimdi asıl soru: volkanı patlatan nedir? Cevap: gaz!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Britanya Jeoloji Araştırmaları Kurumu bunu bir gazoz şişesine benzetiyor: gaz sıvının içinde hapsolmuştur ve kaçmak ister.",
        "spoken": "Britanya Jeoloji Araştırmaları Kurumu bunu bir gazoz şişesine benzetiyor: gaz sıvının içinde hapsolmuştur ve kaçmak ister.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Magmanın içinde çok gaz hapsolursa basınç artar, artar, artar...",
        "spoken": "Magmanın içinde çok gaz hapsolursa basınç artar, artar, artar...",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "Ben gazoz içemem ama o basıncı bilirim. Güncelleme yüklerken ben de böyle oluyorum!",
        "spoken": "Ben gazoz içemem ama o basıncı bilirim. Güncelleme yüklerken ben de böyle oluyorum!",
        "factIds": []
      },
      {
        "id": "l20",
        "display": "Burada önemli bir kelime var: viskozite. Viskozitesi düşük sıvı akıcıdır; yüksek olan ise bal gibi yapışkan ve ağırdır.",
        "spoken": "Burada önemli bir kelime var: viskozite. Viskozitesi düşük sıvı akıcıdır; yüksek olan ise bal gibi yapışkan ve ağırdır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Magma akıcıysa gaz kolayca kaçar ve lav sakince akar. Buna efüzif püskürme denir.",
        "spoken": "Magma akıcıysa gaz kolayca kaçar ve lav sakince akar. Buna efüzif püskürme denir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l22",
        "display": "Magma yapışkansa gaz içeride sıkışır. Basınç birikir ve sonunda patlamalı bir püskürme olur.",
        "spoken": "Magma yapışkansa gaz içeride sıkışır. Basınç birikir ve sonunda patlamalı bir püskürme olur.",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l23",
        "display": "Yani püskürmenin sakin mi patlamalı mı olacağını en çok magmadaki gaz miktarı belirler.",
        "spoken": "Yani püskürmenin sakin mi patlamalı mı olacağını en çok magmadaki gaz miktarı belirler.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l24",
        "display": "Volkanın biçimi de magmaya bağlıdır. Akıcı lav uzağa yayılır ve yayvan bir kalkan volkan oluşturur; eğimi 10 dereceden azdır.",
        "spoken": "Volkanın biçimi de magmaya bağlıdır. Akıcı lav uzağa yayılır ve yayvan bir kalkan volkan oluşturur; eğimi on dereceden azdır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l25",
        "display": "Yapışkan magma ise dik yamaçlı bir stratovolkan kurar; eğimi yaklaşık 30–35 derecedir. Japonya'daki Fuji Dağı böyledir.",
        "spoken": "Yapışkan magma ise dik yamaçlı bir stratovolkan kurar; eğimi yaklaşık otuz ile otuz beş derecedir. Japonya'daki Fuji Dağı böyledir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l26",
        "display": "Püskürmede kül de çıkar. Kül, saç teli kalınlığında minik kaya parçalarıdır ve rüzgârla taşınır.",
        "spoken": "Püskürmede kül de çıkar. Kül, saç teli kalınlığında minik kaya parçalarıdır ve rüzgârla taşınır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "En tehlikelisi piroklastik akıştır: kaya parçaları ile gazın sıcak karışımı. Yamaçtan saatte 110 kilometre ya da daha hızlı iner.",
        "spoken": "En tehlikelisi piroklastik akıştır: kaya parçaları ile gazın sıcak karışımı. Yamaçtan saatte yüz on kilometre ya da daha hızlı iner.",
        "factIds": [
          "f14"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l28",
        "display": "Dünya'da 1500'den fazla etkin volkan var ve her yıl yaklaşık 50–70 tanesi püskürüyor.",
        "spoken": "Dünya'da bin beş yüzden fazla etkin volkan var ve her yıl yaklaşık elli ile yetmiş tanesi püskürüyor.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l29",
        "display": "Dünyanın en büyük etkin volkanı Hawaii'deki Mauna Loa'dır.",
        "spoken": "Dünyanın en büyük etkin volkanı Havai'deki Mauna Loa'dır.",
        "factIds": [
          "f16",
          "f5"
        ]
      },
      {
        "id": "l30",
        "display": "Bazalt lavın sıcaklığı 1100–1200 santigrat derecedir.",
        "spoken": "Bazalt lavın sıcaklığı bin yüz ile bin iki yüz santigrat derecedir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l31",
        "display": "Benim işlemcim bunun yanında buzdolabı sayılır!",
        "spoken": "Benim işlemcim bunun yanında buzdolabı sayılır!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "İyi haber: lav genellikle yavaş aktığı için doğrudan can kaybına nadiren yol açar.",
        "spoken": "İyi haber: lav genellikle yavaş aktığı için doğrudan can kaybına nadiren yol açar.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l33",
        "display": "Peki püskürme önceden anlaşılır mı? Volkanları inceleyen bilim insanlarına volkanolog denir.",
        "spoken": "Peki püskürme önceden anlaşılır mı? Volkanları inceleyen bilim insanlarına volkanolog denir.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l34",
        "display": "USGS'ye göre üç şey izlenir: depremler, yerdeki hareketler ve volkandan çıkan gazlar.",
        "spoken": "Yu Es Ci Es'e göre üç şey izlenir: depremler, yerdeki hareketler ve volkandan çıkan gazlar.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l35",
        "display": "Değişikliği erken fark etmek, insanlara hazırlanmak için zaman kazandırır.",
        "spoken": "Değişikliği erken fark etmek, insanlara hazırlanmak için zaman kazandırır.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l36",
        "display": "Volkanlar yeni kara da kurar: Surtsey adlı ada bir püskürmeyle doğdu.",
        "spoken": "Volkanlar yeni kara da kurar: Sürtsey adlı ada bir püskürmeyle doğdu.",
        "factIds": [
          "f19"
        ]
      },
      {
        "id": "l37",
        "display": "Şimdi sıra sende! Kapalı bir maden suyu şişesine bak: içinde neredeyse hiç kabarcık görünmüyor.",
        "spoken": "Şimdi sıra sende! Kapalı bir maden suyu şişesine bak: içinde neredeyse hiç kabarcık görünmüyor.",
        "factIds": []
      },
      {
        "id": "l38",
        "display": "Kapağı lavabonun üstünde, yavaşça aç. Kabarcıklar belirir: gaz kaçmaya çalışıyor! Tıpkı magmadaki gaz gibi.",
        "spoken": "Kapağı lavabonun üstünde, yavaşça aç. Kabarcıklar belirir: gaz kaçmaya çalışıyor! Tıpkı magmadaki gaz gibi.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l39",
        "display": "Bir uyarı: şişeyi çalkalama ve yüzüne doğru tutma.",
        "spoken": "Bir uyarı: şişeyi çalkalama ve yüzüne doğru tutma.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l40",
        "display": "Bunu biliyor muydun? Volkanların hepsi aynı değildir: yayvan kalkan volkanlar, dik stratovolkanlar ve en basit tür olan cüruf konileri vardır.",
        "spoken": "Bunu biliyor muydun? Volkanların hepsi aynı değildir: yayvan kalkan volkanlar, dik stratovolkanlar ve en basit tür olan cüruf konileri vardır.",
        "factIds": [
          "f9",
          "f10",
          "f11"
        ]
      },
      {
        "id": "l41",
        "display": "Hızlı soru! Erimiş kaya yerin altındayken adı nedir: magma mı, lav mı?",
        "spoken": "Hızlı soru! Erimiş kaya yerin altındayken adı nedir: magma mı, lav mı?",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l42",
        "display": "Düşün bakalım... Evet: magma!",
        "spoken": "Düşün bakalım... Evet: magma!",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l43",
        "display": "Yüzeye çıkınca adı lav olur. Ben yüzeye çıkınca yine Muma'yım!",
        "spoken": "Yüzeye çıkınca adı lav olur. Ben yüzeye çıkınca yine Muma'yım!",
        "factIds": []
      },
      {
        "id": "l44",
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
        "id": "l45",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l46",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l47",
        "display": "Abone olmayı ve zili açmayı unutma. Ben uçayım; burası ısınmaya başladı!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben uçayım; burası ısınmaya başladı!",
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
    "statement": "Volkanlar, lavın, tefranın (küçük kaya parçaları) ve buharın yeryüzüne püskürdüğü açıklıklardır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Erimiş kaya yerin altındayken magma, yüzeye aktığında lav adını alır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Magma yerin onlarca mil altında oluşur; çevresindeki katı kayadan hafiftir (daha az yoğundur) ve bu yüzden yükselir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Etkin bir volkanın içinde magmanın toplandığı bir oda vardır; magma odasında basınç artar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Magma, tektonik levhalar birbirinden uzaklaşırken yükselebilir; levhalar birbirine doğru ilerlerken kabuğun bir kısmı derine itilir, ısı ve basınç kabuğu eritir ve magma olarak yükselir; üçüncü yol sıcak noktalardır. Hawaii volkanları bir sıcak noktanın üstünde oluşur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Volkanların birçoğu Büyük Okyanus'un çevresinde, 'Ateş Çemberi' denen kuşakta yer alır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Magmada çok gaz hapsolursa basınç giderek artar; bu bir gazoz şişesine benzer: gaz sıvıda hapsolmuştur ve kaçmak ister.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Magmanın viskozitesi düşükse (akıcıysa) gaz kolayca kaçar; viskoz (yapışkan) magma yüzeye ulaştığında akamaz. Püskürmenin patlamalı mı efüzif mi olacağı büyük ölçüde magmadaki gaz miktarına bağlıdır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Kalkan volkanlar neredeyse tümüyle akıcı lav akıntılarından oluşur; eğimleri 10°'den azdır. Mauna Kea ve Mauna Loa kalkan volkandır.",
    "numbers": [
      "10"
    ]
  },
  {
    "id": "f10",
    "statement": "Çok viskoz magmanın püskürmesi, eğimi yaklaşık 30–35° olan dik yamaçlı volkanlar oluşturur; bileşik volkanlara stratovolkan da denir; Fuji Dağı bir örnektir.",
    "numbers": [
      "30",
      "35"
    ]
  },
  {
    "id": "f11",
    "statement": "Cüruf konileri en basit volkan türüdür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Kül, saç teli kalınlığında minik tefra parçalarıdır ve rüzgârla taşınabilir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bazalt lavlar tipik olarak 1100–1200°C sıcaklıkta püskürür.",
    "numbers": [
      "1100",
      "1200"
    ]
  },
  {
    "id": "f14",
    "statement": "Piroklastik akışlar, kaya parçaları ile gaz karışımından oluşan sıcak yoğunluk akıntılarıdır; volkanın yamaçlarından tipik olarak saatte 110 kilometre ya da daha hızlı iner.",
    "numbers": [
      "110"
    ]
  },
  {
    "id": "f15",
    "statement": "Dünya'da 1500'den fazla etkin volkan vardır; her yıl yaklaşık 50–70 volkan püskürür.",
    "numbers": [
      "1500",
      "50",
      "70"
    ]
  },
  {
    "id": "f16",
    "statement": "Mauna Loa dünyanın en büyük etkin volkanıdır.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "İzleme; depremler, yer hareketi ve volkanik gaz gibi birkaç tür gözlemi içermelidir; erken fark etmek insanlara hazırlanmak için en çok zamanı kazandırır.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Lav genellikle yavaş aktığı için doğrudan can kaybına yol açması nadirdir.",
    "numbers": []
  },
  {
    "id": "f19",
    "statement": "Surtsey püskürmesi yeni bir ada oluşturdu.",
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
