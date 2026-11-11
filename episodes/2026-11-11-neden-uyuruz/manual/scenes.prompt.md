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
  - "source-card": künye kartı (yazar/kurum/dergi/DOI otomatik dolar) — künyenin okunduğu satırlar için zorunlu.
  - "big-number": tek çarpıcı sayı { value, unit?, label, sub? }. "value" makaledeki yazımla.
  - "bar-chart": 2–6 çubuk { title, unit?, bars: [{ label, value (sayı), display (ekranda yazılacak hali), highlight? }] }.
  - "line-chart": zaman/sıra içinde değişim { title, xLabel, yLabel, points: [...] }.
  - "comparison": iki şeyin yan yana kıyası { title, left: { title, value?, items[] }, right: {...} }.
  - "diagram": 2–5 adımlı süreç { title, layout: "flow" | "cycle", nodes: [{ label, emoji? }] } — yöntem anlatımı için ideal.
  - "analogy": benzetme { template: "scale" (alan kıyası) | "fill" (dolan kap) | "race" (yarış) | "zoom" (iç içe ölçek), title, a: { label, value, display? }, b: {...}, caption }. Benzetmede makalede olmayan sayı gösterme; "display" boş bırakılırsa sayı yazılmaz, yalnızca oran çizilir.
  - "quote-card": makaleden kısa alıntı { quote (Türkçe çeviri, en çok iki cümle), attribution }.
  - "bullets": 1–4 madde { title, items[], tone?: "neutral" | "caution" } — sınırlılıklar için "caution".
  - "outro": kapanış — son sahne, summary bölümünün tüm satırlarını kapsar.
- "mascot": karakter Zerre'nin bu sahnedeki hali { state: "idle" | "talk" | "point" | "think", x, y (0–1, ekran oranı, merkez), scale (0,5–1,6), pointAt? }.
  İçerik sol-ortadadır; Zerre genelde sağda durur (x≈0,86, y≈0,62, scale≈1). Geniş sahnelerde (bar-chart, line-chart, diagram, analogy, comparison) küçülüp köşeye çekilsin (x≈0,9, y≈0,72, scale≈0,7). "hook" sahnesinde solda ve büyük (x≈0,17, y≈0,5, scale≈1,6, state "think"). Bir sayıya ya da grafiğe dikkat çekerken "point" kullan ve "pointAt" ile hedefi ver. Sahneden sahneye konum ve boyut değişsin ki karakter ekranda gezsin.

<senaryo>
[
  {
    "id": "hook",
    "lines": [
      {
        "id": "l1",
        "display": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Bir anda sabah oldu.",
        "spoken": "Dün gece yatağa girdin, gözlerini kapadın ve... pat! Bir anda sabah oldu.",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Peki aradaki o saatlerde ne oldu? Vücudun düğmesine basılıp kapandı mı?",
        "spoken": "Peki aradaki o saatlerde ne oldu? Vücudun düğmesine basılıp kapandı mı?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Hiç de değil! Sen uyurken içeride koca bir gece vardiyası çalışıyor. Hadi, gizlice bakalım!",
        "spoken": "Hiç de değil! Sen uyurken içeride koca bir gece vardiyası çalışıyor. Hadi, gizlice bakalım!",
        "factIds": [
          "f1"
        ]
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Merhaba! Ben senin robot arkadaşınım. Gerçi ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!",
        "spoken": "Merhaba! Ben senin robot arkadaşınım. Gerçi ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Bir kere uyumayı denedim. Bir türlü kapanamadım. Meğer kapatma düğmem yokmuş!",
        "spoken": "Bir kere uyumayı denedim. Bir türlü kapanamadım. Meğer kapatma düğmem yokmuş!",
        "factIds": []
      },
      {
        "id": "l6",
        "display": "Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?",
        "spoken": "Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?",
        "factIds": []
      },
      {
        "id": "l7",
        "display": "Bugünkü bilgilerimiz sağlık kurumlarının sayfalarından geliyor: CDC, NIH ve Nemours KidsHealth.",
        "spoken": "Bugünkü bilgilerimiz sağlık kurumlarının sayfalarından geliyor: Si Di Si, En Ay Eyç ve Nemurs Kids Helt.",
        "factIds": []
      },
      {
        "id": "l8",
        "display": "Kaynakların bağlantıları videonun açıklamasında.",
        "spoken": "Kaynakların bağlantıları videonun açıklamasında.",
        "factIds": []
      }
    ]
  },
  {
    "id": "method",
    "lines": [
      {
        "id": "l9",
        "display": "Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?",
        "spoken": "Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır.",
        "spoken": "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!",
        "spoken": "Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Ana saati en çok ışık ve karanlık etkiler.",
        "spoken": "Ana saati en çok ışık ve karanlık etkiler.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.",
        "spoken": "Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Yani akşam esnemeye başladıysan suçlu belli: melatonin!",
        "spoken": "Yani akşam esnemeye başladıysan suçlu belli: melatonin!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Sabah olunca işler değişir. Vücudun, uyanmana yardım eden kortizol gibi hormonlar salgılar.",
        "spoken": "Sabah olunca işler değişir. Vücudun, uyanmana yardım eden kortizol gibi hormonlar salgılar.",
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
        "display": "Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. Tam tersine, vücudun beynini ve sağlığını korumak için çalışır.",
        "spoken": "Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. Tam tersine, vücudun beynini ve sağlığını korumak için çalışır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l17",
        "display": "Beynin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.",
        "spoken": "Beynin iki tür uyku arasında gidip gelir: Rem olmayan uyku ve Rem uykusu.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık 90 dakika sürer.",
        "spoken": "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık doksan dakika sürer.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "REM olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.",
        "spoken": "Rem olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Yani büyümek, biraz da yastık işi!",
        "spoken": "Yani büyümek, biraz da yastık işi!",
        "factIds": [
          "f9",
          "f15"
        ]
      },
      {
        "id": "l21",
        "display": "REM uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder.",
        "spoken": "Rem uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "En canlı rüyalarımızı da bu sırada görürüz.",
        "spoken": "En canlı rüyalarımızı da bu sırada görürüz.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "İlginç olan şu: REM uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!",
        "spoken": "İlginç olan şu: Rem uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l24",
        "display": "REM uykusu öğrenme ve hafıza için de önemlidir.",
        "spoken": "Rem uykusu öğrenme ve hafıza için de önemlidir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l25",
        "display": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "spoken": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l26",
        "display": "Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.",
        "spoken": "Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l27",
        "display": "Bu yüzden yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
        "spoken": "Bu yüzden yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l28",
        "display": "Yani uyku tembellik değil. Uyku, vücudunun en önemli işlerinden biri!",
        "spoken": "Yani uyku tembellik değil. Uyku, vücudunun en önemli işlerinden biri!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l29",
        "display": "Peki yeterince uyumazsak ne olur? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.",
        "spoken": "Peki yeterince uyumazsak ne olur? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l30",
        "display": "O zaman ne kadar uyumalıyız? 6–12 yaş arasındaysan günde 9–12 saat.",
        "spoken": "O zaman ne kadar uyumalıyız? Altı ile on iki yaş arasındaysan günde dokuz ile on iki saat.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l31",
        "display": "13–17 yaş arasındaysan 8–10 saat.",
        "spoken": "On üç ile on yedi yaş arasındaysan sekiz ile on saat.",
        "factIds": [
          "f19"
        ]
      },
      {
        "id": "l32",
        "display": "Kaç saat uyuduğunu merak mı ettin? Yattığın ve kalktığın saate bak, aradaki saatleri say.",
        "spoken": "Kaç saat uyuduğunu merak mı ettin? Yattığın ve kalktığın saate bak, aradaki saatleri say.",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l33",
        "display": "Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?",
        "spoken": "Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Bir: Her gün aynı saatte yat, aynı saatte kalk.",
        "spoken": "Bir: Her gün aynı saatte yat, aynı saatte kalk.",
        "factIds": [
          "f20"
        ]
      },
      {
        "id": "l35",
        "display": "İki: Yatmadan en az 30 dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.",
        "spoken": "İki: Yatmadan en az otuz dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.",
        "factIds": [
          "f21",
          "f22"
        ]
      },
      {
        "id": "l36",
        "display": "Üç: Odan sessiz, sakin ve serin olsun. Gün içinde de bol bol hareket et.",
        "spoken": "Üç: Odan sessiz, sakin ve serin olsun. Gün içinde de bol bol hareket et.",
        "factIds": [
          "f23",
          "f24"
        ]
      },
      {
        "id": "l37",
        "display": "Dört: Her sabah kendine sor: Bugün nasıl hissediyorum? Bir kâğıda not et, hafta sonunda karşılaştır.",
        "spoken": "Dört: Her sabah kendine sor: Bugün nasıl hissediyorum? Bir kâğıda not et, hafta sonunda karşılaştır.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l38",
        "display": "Bunu biliyor muydun? Vücut saatini yalnızca ışık etkilemez. Yemek, hareket ve sıcaklık da etkiler.",
        "spoken": "Bunu biliyor muydun? Vücut saatini yalnızca ışık etkilemez. Yemek, hareket ve sıcaklık da etkiler.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l39",
        "display": "Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?",
        "spoken": "Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l40",
        "display": "Düşün bakalım... Evet: REM uykusunda!",
        "spoken": "Düşün bakalım... Evet: Rem uykusunda!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l41",
        "display": "Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!",
        "spoken": "Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!",
        "factIds": []
      },
      {
        "id": "l42",
        "display": "Bir soru daha! Akşam olunca uykumuzu getiren hormonun adı neydi?",
        "spoken": "Bir soru daha! Akşam olunca uykumuzu getiren hormonun adı neydi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l43",
        "display": "Me-la-to-nin! Söylemesi bile insanın uykusunu getiriyor.",
        "spoken": "Melatonin! Söylemesi bile insanın uykusunu getiriyor.",
        "factIds": [
          "f5"
        ]
      }
    ]
  },
  {
    "id": "summary",
    "lines": [
      {
        "id": "l44",
        "display": "Bugün bunu öğrendik!",
        "spoken": "Bugün bunu öğrendik!",
        "factIds": []
      },
      {
        "id": "l45",
        "display": "Bir: İçimizde bir saat var. Akşam olunca melatonin uykumuzu getirir.",
        "spoken": "Bir: İçimizde bir saat var. Akşam olunca melatonin uykumuzu getirir.",
        "factIds": [
          "f2",
          "f5"
        ]
      },
      {
        "id": "l46",
        "display": "İki: Uyurken beynimiz çalışmaya devam eder. Uyku, öğrenmeye ve hafızaya yardım eder.",
        "spoken": "İki: Uyurken beynimiz çalışmaya devam eder. Uyku, öğrenmeye ve hafızaya yardım eder.",
        "factIds": [
          "f7",
          "f14"
        ]
      },
      {
        "id": "l47",
        "display": "Üç: Uyku büyümemize ve hastalıklardan korunmamıza yardım eder.",
        "spoken": "Üç: Uyku büyümemize ve hastalıklardan korunmamıza yardım eder.",
        "factIds": [
          "f15",
          "f16"
        ]
      },
      {
        "id": "l48",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l49",
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
    "statement": "Vücut saati (sirkadiyen ritim), bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.",
    "numbers": [
      "24"
    ]
  },
  {
    "id": "f3",
    "statement": "İnsanda ana saat beyindedir; büyük bir sinir hücresi grubudur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Vücut saatini en çok ışık ve karanlık etkiler; yemek, stres, hareket, sosyal çevre ve sıcaklık da etkiler.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Akşam ana saat beyne daha çok melatonin üretmesini söyler; bu uyku getirir. Melatonin bir hormondur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Sabah vücut, uyanmaya yardım eden kortizol gibi hormonlar salgılar.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Uyurken beyin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Okul çağında bir uyku döngüsü yaklaşık 90 dakika sürer.",
    "numbers": [
      "90"
    ]
  },
  {
    "id": "f9",
    "statement": "REM olmayan uykunun üçüncü aşamasında vücut, büyüme ve gelişme için gereken hormonları salgılar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "REM uykusunda gözler göz kapaklarının altında hızlı hareket eder.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "En canlı rüyalar REM uykusunda görülür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "REM uykusunda kollar ve bacaklar hareket ettirilemez.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "REM uykusu öğrenme ve hafıza için önemlidir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Çocuklarda ve gençlerde uyku, büyümeyi ve gelişmeyi de destekler.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz, sinirli ya da keyifsiz olabilir.",
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
    "statement": "Yatak odasının sessiz, rahatlatıcı ve serin olması önerilir.",
    "numbers": []
  },
  {
    "id": "f24",
    "statement": "Düzenli hareket etmek ve sağlıklı beslenmek daha iyi uykuya yardım eder.",
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
