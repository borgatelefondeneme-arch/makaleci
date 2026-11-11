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
        "display": "Ayağının altındaki yer sapasağlam görünür. Ama aslında çok yavaş hareket eden dev parçalardan oluşur!",
        "spoken": "Ayağının altındaki yer sapasağlam görünür. Ama aslında çok yavaş hareket eden dev parçalardan oluşur!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l2",
        "display": "Peki yer neden bazen aniden sarsılır? Ve sarsıntı uzaklara nasıl yayılır?",
        "spoken": "Peki yer neden bazen aniden sarsılır? Ve sarsıntı uzaklara nasıl yayılır?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün yerin derinlerine iniyoruz!",
        "spoken": "Bugün yerin derinlerine iniyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Ben de bazen titrerim. Ama o deprem değil, titreşim modum!",
        "spoken": "Ben de bazen titrerim. Ama o deprem değil, titreşim modum!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Deprem neden olur? Deprem dalgaları nasıl yayılır? Ve deprem sırasında ne yapmalıyız?",
        "spoken": "Üç sorumuz var. Deprem neden olur? Deprem dalgaları nasıl yayılır? Ve deprem sırasında ne yapmalıyız?",
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
        "display": "NASA'ya göre Dünya dört temel katmandan oluşur: katı kabuk, sıcak manto, sıvı dış çekirdek ve katı iç çekirdek.",
        "spoken": "Nasa'ya göre Dünya dört temel katmandan oluşur: katı kabuk, sıcak manto, sıvı dış çekirdek ve katı iç çekirdek.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Britanya Jeoloji Araştırmaları Kurumu'na göre en dıştaki katman tek parça değildir: yaklaşık 15 büyük parçaya bölünmüştür. Bunlara tektonik levha denir.",
        "spoken": "Britanya Jeoloji Araştırmaları Kurumu'na göre en dıştaki katman tek parça değildir: yaklaşık on beş büyük parçaya bölünmüştür. Bunlara tektonik levha denir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Levhalar birbirine göre çok yavaş hareket eder: yılda yalnızca birkaç santimetre.",
        "spoken": "Levhalar birbirine göre çok yavaş hareket eder: yılda yalnızca birkaç santimetre.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Benim yazılım güncellemelerim bile bundan hızlı. Çoğu zaman!",
        "spoken": "Benim yazılım güncellemelerim bile bundan hızlı. Çoğu zaman!",
        "factIds": []
      },
      {
        "id": "l11",
        "display": "National Geographic'e göre levhalar birbirine yaklaşabilir, birbirinden uzaklaşabilir ya da yan yana sürtünerek kayabilir.",
        "spoken": "Neşınıl Ciyografik'e göre levhalar birbirine yaklaşabilir, birbirinden uzaklaşabilir ya da yan yana sürtünerek kayabilir.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Kaya bloklarının birbirine göre kaydığı kırıklara fay denir.",
        "spoken": "Kaya bloklarının birbirine göre kaydığı kırıklara fay denir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Ama kayalar kolayca kaymaz. Sürtünme onları yerinde tutar ve kayalarda gerilim birikmeye başlar.",
        "spoken": "Ama kayalar kolayca kaymaz. Sürtünme onları yerinde tutar ve kayalarda gerilim birikmeye başlar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Gerilim biriktikçe kayalar yavaş yavaş biçim değiştirir. Tıpkı bükülen bir cetvel gibi enerji depolar.",
        "spoken": "Gerilim biriktikçe kayalar yavaş yavaş biçim değiştirir. Tıpkı bükülen bir cetvel gibi enerji depolar.",
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
        "id": "l15",
        "display": "Sonunda kayalar daha fazla dayanamaz ve fay aniden kayar. Biriken enerji bir anda serbest kalır. İşte deprem budur!",
        "spoken": "Sonunda kayalar daha fazla dayanamaz ve fay aniden kayar. Biriken enerji bir anda serbest kalır. İşte deprem budur!",
        "factIds": [
          "f1",
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Kayalar eski biçimine geri döner ama fayın iki yanı artık yer değiştirmiştir. Buna elastik geri sekme denir.",
        "spoken": "Kayalar eski biçimine geri döner ama fayın iki yanı artık yer değiştirmiştir. Buna elastik geri sekme denir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Depremin yerin içinde başladığı noktaya odak ya da hiposantr denir. Kilometrelerce derinde olabilir.",
        "spoken": "Depremin yerin içinde başladığı noktaya odak ya da hiposantr denir. Kilometrelerce derinde olabilir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Odağın tam üstündeki yeryüzü noktası ise merkez üssüdür.",
        "spoken": "Odağın tam üstündeki yeryüzü noktası ise merkez üssüdür.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "Enerji odaktan her yöne yayılır; tıpkı suya atılan taşın oluşturduğu halkalar gibi. Bu dalgalara sismik dalga denir.",
        "spoken": "Enerji odaktan her yöne yayılır; tıpkı suya atılan taşın oluşturduğu halkalar gibi. Bu dalgalara sismik dalga denir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "İki ana türü var. P dalgaları kayayı ilerleme yönünde sıkıştırıp gevşetir. S dalgaları ise ilerleme yönüne dik sallar.",
        "spoken": "İki ana türü var. Pe dalgaları kayayı ilerleme yönünde sıkıştırıp gevşetir. Se dalgaları ise ilerleme yönüne dik sallar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "P dalgaları daha hızlıdır: yer kabuğunda saniyede 5–7 kilometre yol alır. S dalgaları ise saniyede 3–4 kilometre.",
        "spoken": "Pe dalgaları daha hızlıdır: yer kabuğunda saniyede beş ile yedi kilometre yol alır. Se dalgaları ise saniyede üç ile dört kilometre.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "USGS bunu şöyle benzetiyor: P dalgası şimşek gibidir, S dalgası gök gürültüsü gibi. Önce biri gelir, sonra öteki.",
        "spoken": "Yu Es Ci Es bunu şöyle benzetiyor: Pe dalgası şimşek gibidir, Se dalgası gök gürültüsü gibi. Önce biri gelir, sonra öteki.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "P dalgasının daha hızlı olması, bilim insanlarının depremin nerede olduğunu bulmasını sağlar.",
        "spoken": "Pe dalgasının daha hızlı olması, bilim insanlarının depremin nerede olduğunu bulmasını sağlar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Dalgaları ölçen alete sismometre denir. Çizdiği kayıt ise sismogramdır.",
        "spoken": "Dalgaları ölçen alete sismometre denir. Çizdiği kayıt ise sismogramdır.",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l25",
        "display": "Depremin büyüklüğü bir sayıyla ifade edilir. Bu ölçek logaritmiktir: büyüklük bir birim artınca dalganın genliği, yani kayıttaki yüksekliği, on katına çıkar.",
        "spoken": "Depremin büyüklüğü bir sayıyla ifade edilir. Bu ölçek logaritmiktir: büyüklük bir birim artınca dalganın genliği, yani kayıttaki yüksekliği, on katına çıkar.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Büyüklük ile şiddet aynı şey değildir. Şiddet, sarsıntının bir yerde ne kadar güçlü olduğunu anlatır ve merkez üssünden uzaklaştıkça genellikle azalır.",
        "spoken": "Büyüklük ile şiddet aynı şey değildir. Şiddet, sarsıntının bir yerde ne kadar güçlü olduğunu anlatır ve merkez üssünden uzaklaştıkça genellikle azalır.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Depremler sanıldığından çok daha sıktır: National Geographic'e göre Dünya'da her gün yüzlerce deprem olur.",
        "spoken": "Depremler sanıldığından çok daha sıktır: Neşınıl Ciyografik'e göre Dünya'da her gün yüzlerce deprem olur.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l28",
        "display": "Ciddi hasar verebilecek büyüklükte olanlar ise yılda yaklaşık 100 tanedir.",
        "spoken": "Ciddi hasar verebilecek büyüklükte olanlar ise yılda yaklaşık yüz tanedir.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l29",
        "display": "Büyük bir depremden sonra artçı sarsıntılar haftalarca, aylarca, hatta yıllarca sürebilir.",
        "spoken": "Büyük bir depremden sonra artçı sarsıntılar haftalarca, aylarca, hatta yıllarca sürebilir.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l30",
        "display": "Peki deprem önceden bilinebilir mi? USGS'ye göre bugüne kadar hiçbir bilim insanı büyük bir depremin gününü, yerini ve büyüklüğünü önceden bilemedi.",
        "spoken": "Peki deprem önceden bilinebilir mi? Yu Es Ci Es'e göre bugüne kadar hiçbir bilim insanı büyük bir depremin gününü, yerini ve büyüklüğünü önceden bilemedi.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l31",
        "display": "Ama bilim insanları bir fayda gelecekte yeniden deprem olacağını bilir. Erken uyarı sistemleri de deprem başladıktan hemen sonra haber verir.",
        "spoken": "Ama bilim insanları bir fayda gelecekte yeniden deprem olacağını bilir. Erken uyarı sistemleri de deprem başladıktan hemen sonra haber verir.",
        "factIds": [
          "f16",
          "f17"
        ]
      },
      {
        "id": "l32",
        "display": "Bu yüzden en iyi çözüm hazırlıklı olmaktır. Ready.gov'un önerdiği üç hareketi ezberle: Çök, Kapan, Tutun!",
        "spoken": "Bu yüzden en iyi çözüm hazırlıklı olmaktır. Redi nokta gav'ın önerdiği üç hareketi ezberle: Çök, Kapan, Tutun!",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l33",
        "display": "Yere çök. Sağlam bir masanın altına gir. Sarsıntı bitene kadar tutun. Camlardan ve devrilebilecek eşyalardan uzak dur.",
        "spoken": "Yere çök. Sağlam bir masanın altına gir. Sarsıntı bitene kadar tutun. Camlardan ve devrilebilecek eşyalardan uzak dur.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l34",
        "display": "Dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.",
        "spoken": "Dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l35",
        "display": "Şimdi sıra sende! Ailenle birlikte evde bir Çök, Kapan, Tutun tatbikatı yap ve bir acil durum çantası hazırla.",
        "spoken": "Şimdi sıra sende! Ailenle birlikte evde bir Çök, Kapan, Tutun tatbikatı yap ve bir acil durum çantası hazırla.",
        "factIds": [
          "f18",
          "f19"
        ]
      },
      {
        "id": "l36",
        "display": "Bir de deney: avuçlarını birbirine sıkıca bastır ve kaydırmaya çalış. Önce takılır, sonra aniden kayar. Fay da böyle davranır!",
        "spoken": "Bir de deney: avuçlarını birbirine sıkıca bastır ve kaydırmaya çalış. Önce takılır, sonra aniden kayar. Fay da böyle davranır!",
        "factIds": [
          "f5"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l37",
        "display": "Bunu biliyor muydun? USGS'ye göre büyüklüğü 10 ya da daha fazla olan bir deprem olamaz.",
        "spoken": "Bunu biliyor muydun? Yu Es Ci Es'e göre büyüklüğü on ya da daha fazla olan bir deprem olamaz.",
        "factIds": [
          "f20"
        ]
      },
      {
        "id": "l38",
        "display": "Hızlı soru! Hangi dalga daha hızlıdır: P mi, S mi?",
        "spoken": "Hızlı soru! Hangi dalga daha hızlıdır: Pe mi, Se mi?",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l39",
        "display": "Düşün bakalım... Evet: P dalgası!",
        "spoken": "Düşün bakalım... Evet: Pe dalgası!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l40",
        "display": "Aklında şöyle kalsın: P, pistin şampiyonu. S, sonradan gelen!",
        "spoken": "Aklında şöyle kalsın: Pe, pistin şampiyonu. Se, sonradan gelen!",
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben de gidip acil durum çantama yedek pil koyayım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de gidip acil durum çantama yedek pil koyayım!",
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
    "statement": "Deprem, yer kabuğunda biriken gerinim enerjisinin aniden serbest kalmasıdır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Dünya'nın dört temel katmanı vardır: katı kabuk, sıcak ve neredeyse katı manto, sıvı dış çekirdek ve katı iç çekirdek.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Dünya'nın en dış katmanı tektonik levha denen yaklaşık 15 büyük parçaya bölünmüştür; levhalar birbirine göre çok yavaş, tipik olarak yılda birkaç santimetre hareket eder.",
    "numbers": [
      "15"
    ]
  },
  {
    "id": "f4",
    "statement": "Levhalar birbirine doğru hareket edebilir, birbirine sürtünerek kayabilir ya da birbirinden ayrılabilir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Sürtünme kayaları yerinde tutar ve gerilim birikir; fayın iki yanındaki kayalar yavaş yavaş biçim değiştirir; blokları kaydıracak enerji depolanır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Elastik geri sekme: kayalar özgün biçimine döner ama fayın iki yanında yer değiştirmiş olur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Depremin başladığı noktaya odak ya da hiposantr denir ve kilometrelerce derinde olabilir; odağın tam üstündeki yüzey noktası merkez üssüdür.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Enerji, gölcükteki halkalar gibi her yöne yayılır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "P dalgaları ilerleme yönü boyunca sıkışma ve genleşmelerden oluşur; S dalgalarının hareketi ilerleme yönüne diktir; P dalgaları S dalgalarından hızlıdır. Tipik yer kabuğunda P 5–7 km/s, S 3–4 km/s hızla ilerler.",
    "numbers": [
      "5",
      "7",
      "3",
      "4"
    ]
  },
  {
    "id": "f10",
    "statement": "P dalgaları şimşek, S dalgaları gök gürültüsü gibidir; P'nin S'den hızlı olması depremin nerede olduğunu bulmayı sağlar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Sismograf ya da sismometre, sismogramı oluşturan ölçüm aletidir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Büyüklük ölçekleri logaritmiktir: büyüklükte bir birimlik artış, genlikte on katlık artışa karşılık gelir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Şiddet, depremin yol açtığı sarsıntının gücünün nitel ölçüsüdür ve normalde merkez üssünden uzaklaştıkça azalır; büyüklük ise uzaklıktan bağımsızdır.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Dünya'da her gün yüzlerce deprem olur; ciddi hasar verebilecek büyüklükte olanlar yılda yaklaşık 100 tanedir.",
    "numbers": [
      "100"
    ]
  },
  {
    "id": "f15",
    "statement": "Artçı sarsıntılar ana depremden sonra haftalarca, aylarca, hatta yıllarca sürebilir.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Ne USGS ne de başka bilim insanları bugüne kadar büyük bir depremi önceden bildi; bir tahminin tarih ve saati, yeri ve büyüklüğü belirtmesi gerekir. Bilim insanları belirli bir fayda gelecekte yeniden deprem olacağını bilir.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Erken uyarı, deprem başladıktan sonra yapılan bir bildirimdir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Deprem anında: yere çök, sağlam bir masanın altına gir, sarsıntı bitene kadar tutun; camlardan ve devrilebilecek eşyalardan uzak dur; dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.",
    "numbers": []
  },
  {
    "id": "f19",
    "statement": "Hızla tahliye gerekirse ihtiyaç duyulacak eşyalarla bir acil durum çantası hazırlanmalıdır.",
    "numbers": []
  },
  {
    "id": "f20",
    "statement": "Büyüklüğü 10 ya da daha fazla olan depremler olamaz.",
    "numbers": [
      "10"
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
