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
        "display": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Sabah oldu. Peki aradaki saatlerde ne oldu?",
        "spoken": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Sabah oldu. Peki aradaki saatlerde ne oldu?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Vücudun kapanmadı. Tam tersine: beynin gece boyunca planlı bir program yürüttü.",
        "spoken": "Vücudun kapanmadı. Tam tersine: beynin gece boyunca planlı bir program yürüttü.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün o programı adım adım çözüyoruz!",
        "spoken": "Bugün o programı adım adım çözüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Ben uyumam, şarj olurum. Ama insan uykusu benim şarjımdan çok daha karmaşık!",
        "spoken": "Ben uyumam, şarj olurum. Ama insan uykusu benim şarjımdan çok daha karmaşık!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Vücudumuz uyku vaktini nasıl anlıyor? Uyurken beyinde hangi evreler yaşanıyor? Ve bu kadar uyumak neye yarıyor?",
        "spoken": "Üç sorumuz var. Vücudumuz uyku vaktini nasıl anlıyor? Uyurken beyinde hangi evreler yaşanıyor? Ve bu kadar uyumak neye yarıyor?",
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
        "display": "Uyku vaktini iki ayrı sistem birlikte belirler. Birincisi: biyolojik saat.",
        "spoken": "Uyku vaktini iki ayrı sistem birlikte belirler. Birincisi: biyolojik saat.",
        "factIds": []
      },
      {
        "id": "l8",
        "display": "Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır. Buna sirkadiyen ritim denir.",
        "spoken": "Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'e göre vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır. Buna sirkadiyen ritim denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Bu ritmi yöneten ana saat beynimizdedir. Adı biraz uzun: suprakiazmatik çekirdek. Kısaca SCN.",
        "spoken": "Bu ritmi yöneten ana saat beynimizdedir. Adı biraz uzun: suprakiazmatik çekirdek. Kısaca Es Si En.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "SCN, beynin hipotalamus adlı bölgesinde, görme sinirlerinin çaprazlaştığı noktanın hemen üstünde yer alır ve binlerce sinir hücresinden oluşur.",
        "spoken": "Es Si En, beynin hipotalamus adlı bölgesinde, görme sinirlerinin çaprazlaştığı noktanın hemen üstünde yer alır ve binlerce sinir hücresinden oluşur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Onu bir orkestra şefi gibi düşün: vücuttaki ritimlerin aynı tempoda çalmasını sağlar.",
        "spoken": "Onu bir orkestra şefi gibi düşün: vücuttaki ritimlerin aynı tempoda çalmasını sağlar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Şefin en önemli işareti ışıktır. Gözlerine gelen ışık, beynine şu mesajı yollar: Şu an gündüz!",
        "spoken": "Şefin en önemli işareti ışıktır. Gözlerine gelen ışık, beynine şu mesajı yollar: Şu an gündüz!",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l13",
        "display": "Güneş batınca beyin melatonin üretmeye başlar. Melatonin, uykuyu getiren bir hormondur. Kandaki miktarı akşam artar, sabaha karşı en yüksek düzeye çıkar.",
        "spoken": "Güneş batınca beyin melatonin üretmeye başlar. Melatonin, uykuyu getiren bir hormondur. Kandaki miktarı akşam artar, sabaha karşı en yüksek düzeye çıkar.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l14",
        "display": "İkinci sistem: uyku baskısı. Uyanık kaldığın her saat, beyninde adenozin adlı bir madde birikir.",
        "spoken": "İkinci sistem: uyku baskısı. Uyanık kaldığın her saat, beyninde adenozin adlı bir madde birikir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l15",
        "display": "Adenozin arttıkça uyuma ihtiyacın büyür. Uyuduğunda ise beyin bu maddeyi yeniden enerji molekülüne çevirir ve baskı ortadan kalkar.",
        "spoken": "Adenozin arttıkça uyuma ihtiyacın büyür. Uyuduğunda ise beyin bu maddeyi yeniden enerji molekülüne çevirir ve baskı ortadan kalkar.",
        "factIds": [
          "f8",
          "f9"
        ]
      },
      {
        "id": "l16",
        "display": "Yani gün sonunda esniyorsan tembel değilsin. Adenozin deposu doldu, o kadar!",
        "spoken": "Yani gün sonunda esniyorsan tembel değilsin. Adenozin deposu doldu, o kadar!",
        "factIds": [
          "f8"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l17",
        "display": "Peki uykuya dalınca ne olur? Sleep Foundation'a göre uyku dört evreden oluşur: üçü REM olmayan evre, biri REM.",
        "spoken": "Peki uykuya dalınca ne olur? Sliip Faundeyşın'a göre uyku dört evreden oluşur: üçü Rem olmayan evre, biri Rem.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l18",
        "display": "Bu evreler sırayla bir döngü oluşturur. Bir döngü ortalama 90 dakika sürer ve bir gecede 4–6 döngü yaşarız.",
        "spoken": "Bu evreler sırayla bir döngü oluşturur. Bir döngü ortalama doksan dakika sürer ve bir gecede dört ile altı döngü yaşarız.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l19",
        "display": "Üçüncü evreye derin uyku denir. Bu evre, vücudun toparlanması ve büyümesi için kritik sayılır.",
        "spoken": "Üçüncü evreye derin uyku denir. Bu evre, vücudun toparlanması ve büyümesi için kritik sayılır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l20",
        "display": "KidsHealth'e göre büyüme için gereken hormonlar da bu evrede salgılanır. Yani büyümek, biraz da yastık işi!",
        "spoken": "Kids Helt'e göre büyüme için gereken hormonlar da bu evrede salgılanır. Yani büyümek, biraz da yastık işi!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l21",
        "display": "Dördüncü evre REM uykusudur. REM, hızlı göz hareketi demektir: gözlerin kapalıdır ama hızla hareket eder.",
        "spoken": "Dördüncü evre Rem uykusudur. Rem, hızlı göz hareketi demektir: gözlerin kapalıdır ama hızla hareket eder.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l22",
        "display": "Bu evrede beyin etkinliği neredeyse uyanıkkenki düzeye çıkar. En canlı rüyalar da burada görülür.",
        "spoken": "Bu evrede beyin etkinliği neredeyse uyanıkkenki düzeye çıkar. En canlı rüyalar da burada görülür.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l23",
        "display": "Aynı anda kasların geçici olarak felç olur. Buna atoni denir. İyi ki öyle: yoksa rüyanda gol atarken yorgan havada uçardı!",
        "spoken": "Aynı anda kasların geçici olarak felç olur. Buna atoni denir. İyi ki öyle: yoksa rüyanda gol atarken yorgan havada uçardı!",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l24",
        "display": "REM uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir. Uyku, öğrendiklerinin uzun süreli anılara dönüşmesine yardım eder.",
        "spoken": "Rem uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir. Uyku, öğrendiklerinin uzun süreli anılara dönüşmesine yardım eder.",
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
        "id": "l25",
        "display": "Peki bunca saat uyumak neye yarıyor? Uyku, vücudun enerji tasarrufu yapmasını sağlar. Büyüme hormonu da dokuların büyümesine ve onarılmasına yardım eder.",
        "spoken": "Peki bunca saat uyumak neye yarıyor? Uyku, vücudun enerji tasarrufu yapmasını sağlar. Büyüme hormonu da dokuların büyümesine ve onarılmasına yardım eder.",
        "factIds": [
          "f15",
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Bağışıklık sistemin de güçlenir. NIH'ye göre uyurken bazı bağışıklık hücreleri daha çok çalışır; az uyuyanlar nezleye daha kolay yakalanabilir.",
        "spoken": "Bağışıklık sistemin de güçlenir. En Ay Eyç'e göre uyurken bazı bağışıklık hücreleri daha çok çalışır; az uyuyanlar nezleye daha kolay yakalanabilir.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l27",
        "display": "Yeterince uyumazsan dikkatini toplamak zorlaşır, keyfin de kaçabilir.",
        "spoken": "Yeterince uyumazsan dikkatini toplamak zorlaşır, keyfin de kaçabilir.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l28",
        "display": "CDC'ye göre 6–12 yaş arasındakilerin günde 9–12 saat, 13–17 yaş arasındakilerin 8–10 saat uyuması önerilir.",
        "spoken": "Si Di Si'ye göre altı ile on iki yaş arasındakilerin günde dokuz ile on iki saat, on üç ile on yedi yaş arasındakilerin sekiz ile on saat uyuması önerilir.",
        "factIds": [
          "f18",
          "f19"
        ]
      },
      {
        "id": "l29",
        "display": "Bir ayrıntı daha: birçok gencin daha geç yatıp daha geç kalkmak istemesi doğaldır. Bu, tembellik değildir.",
        "spoken": "Bir ayrıntı daha: birçok gencin daha geç yatıp daha geç kalkmak istemesi doğaldır. Bu, tembellik değildir.",
        "factIds": [
          "f23"
        ]
      },
      {
        "id": "l30",
        "display": "Şimdi sıra sende! Bir hafta boyunca uyku günlüğü tut.",
        "spoken": "Şimdi sıra sende! Bir hafta boyunca uyku günlüğü tut.",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Her gün aynı saatte yat ve kalk. Yatmadan en az 30 dakika önce ekranları kapat; çünkü cihazların ışığı biyolojik saati şaşırtabilir.",
        "spoken": "Her gün aynı saatte yat ve kalk. Yatmadan en az otuz dakika önce ekranları kapat; çünkü cihazların ışığı biyolojik saati şaşırtabilir.",
        "factIds": [
          "f20",
          "f21",
          "f22"
        ]
      },
      {
        "id": "l32",
        "display": "Her sabah kaç saat uyuduğunu ve kendini nasıl hissettiğini not et. Hafta sonunda verilerine bak: tıpkı bir bilim insanı gibi!",
        "spoken": "Her sabah kaç saat uyuduğunu ve kendini nasıl hissettiğini not et. Hafta sonunda verilerine bak: tıpkı bir bilim insanı gibi!",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l33",
        "display": "Bunu biliyor muydun? Kafein, adenozinin bağlandığı alıcıları kapatır. Kafeinli içeceklerin uykuyu kaçırmasının nedeni budur.",
        "spoken": "Bunu biliyor muydun? Kafein, adenozinin bağlandığı alıcıları kapatır. Kafeinli içeceklerin uykuyu kaçırmasının nedeni budur.",
        "factIds": [
          "f24"
        ]
      },
      {
        "id": "l34",
        "display": "Hızlı soru! Beynimizdeki ana saatin kısa adı neydi?",
        "spoken": "Hızlı soru! Beynimizdeki ana saatin kısa adı neydi?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l35",
        "display": "Düşün bakalım... Evet: SCN!",
        "spoken": "Düşün bakalım... Evet: Es Si En!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l36",
        "display": "Bende SCN yok. Ama çok güzel bir şarj göstergem var!",
        "spoken": "Bende Es Si En yok. Ama çok güzel bir şarj göstergem var!",
        "factIds": []
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!",
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
    "statement": "Uyurken vücut, beynin sağlıklı çalışmasını ve beden sağlığını desteklemek için çalışır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Sirkadiyen ritimler, bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.",
    "numbers": [
      "24"
    ]
  },
  {
    "id": "f3",
    "statement": "İnsanda ana saat beyindedir; suprakiazmatik çekirdek (SCN) adlı yapıyı oluşturan büyük bir sinir hücresi grubudur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "SCN, beynin hipotalamus bölgesinde, görme sinirlerinin çaprazlaştığı yerin hemen üstündedir; binlerce nörondan oluşur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Sirkadiyen ritimleri en çok ışık ve karanlık etkiler.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Gözlerle alınan ışık sinyalleri beyne gündüz olduğunu bildirir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Güneş batınca beyin uyku getiren melatonin hormonunu üretmeye başlar; kandaki melatonin akşam artar, sabaha karşı en yüksek düzeye çıkar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Uzun süre uyanık kaldıkça uyku ihtiyacı artar; bu ihtiyaç adenozin adlı bileşikle bağlantılıdır ve uyanıkken beyindeki adenozin düzeyi yükselir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Uyurken beyin adenozini yeniden ATP'ye (enerji molekülüne) çevirir ve uyku baskısı ortadan kalkar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Uyku dört evreden oluşur: üçü REM olmayan (N1, N2, N3), biri REM. Bir gecede dört ila altı döngü yaşanır; bir döngü ortalama 90 dakika sürer.",
    "numbers": [
      "90",
      "4",
      "6",
      "1",
      "2",
      "3"
    ]
  },
  {
    "id": "f11",
    "statement": "Üçüncü evre (N3) derin uykudur; vücudun toparlanması ve büyümesi için kritik sayılır, bağışıklık sistemini de destekleyebilir.",
    "numbers": [
      "3"
    ]
  },
  {
    "id": "f12",
    "statement": "Büyüme ve gelişme için gereken hormonlar REM olmayan uykunun üçüncü evresinde salgılanır; büyüme hormonu dokuların büyümesi ve onarılması için gereklidir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "REM uykusunda gözler kapalıyken hızla hareket eder; beyin etkinliği uyanıklık düzeyine yaklaşır; kaslar geçici olarak felç olur (atoni); en canlı rüyalar bu evrede görülür.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "REM uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir; uyku uzun süreli anıların oluşmasına yardım eder.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Uyku, vücudun enerji tasarrufu yapmasını sağlar.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz ya da keyifsiz olabilir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "6–12 yaş için önerilen günlük uyku 9–12 saattir.",
    "numbers": [
      "6",
      "12",
      "9"
    ]
  },
  {
    "id": "f19",
    "statement": "13–17 yaş için önerilen günlük uyku 8–10 saattir.",
    "numbers": [
      "13",
      "17",
      "8",
      "10"
    ]
  },
  {
    "id": "f20",
    "statement": "Her gün aynı saatte yatıp kalkmak daha iyi uykuya yardım eder.",
    "numbers": []
  },
  {
    "id": "f21",
    "statement": "Yatmadan en az 30 dakika önce elektronik cihazları kapatmak önerilir.",
    "numbers": [
      "30"
    ]
  },
  {
    "id": "f22",
    "statement": "Geceleri elektronik cihazların ışığı biyolojik saati şaşırtabilir.",
    "numbers": []
  },
  {
    "id": "f23",
    "statement": "Birçok gencin yetişkinlerden daha geç yatmayı ve sabah daha geç kalkmayı tercih etmesi doğaldır.",
    "numbers": []
  },
  {
    "id": "f24",
    "statement": "Kafein temel olarak adenozin alıcılarını kapatarak etki eder.",
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
