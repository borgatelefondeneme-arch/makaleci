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
        "display": "Ağzının içinde, vücudunun en sert maddesiyle kaplı bir alet takımı var!",
        "spoken": "Ağzının içinde, vücudunun en sert maddesiyle kaplı bir alet takımı var!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l2",
        "display": "Dişlerin nasıl bu kadar güçlü? Ve küçük bir şeker parçası onlara nasıl zarar verebilir?",
        "spoken": "Dişlerin nasıl bu kadar güçlü? Ve küçük bir şeker parçası onlara nasıl zarar verebilir?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün ağzının içine bir keşif yapıyoruz!",
        "spoken": "Bugün ağzının içine bir keşif yapıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Bir diş neyden yapılır? Hangi diş ne iş yapar? Ve çürük nasıl başlar?",
        "spoken": "Üç sorumuz var. Bir diş neyden yapılır? Hangi diş ne iş yapar? Ve çürük nasıl başlar?",
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
        "display": "KidsHealth'e göre ilk diş takımımız 20 süt dişinden oluşur. Onların yerini 32 kalıcı diş alır.",
        "spoken": "Kids Helt'e göre ilk diş takımımız yirmi süt dişinden oluşur. Onların yerini otuz iki kalıcı diş alır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Süt dişleri daha doğmadan gelişmeye başlar ve yaklaşık 6 yaşında düşmeye başlar.",
        "spoken": "Süt dişleri daha doğmadan gelişmeye başlar ve yaklaşık altı yaşında düşmeye başlar.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Benim dişim yok. Ama vidalarım da hiç düşmedi, o da bir başarı!",
        "spoken": "Benim dişim yok. Ama vidalarım da hiç düşmedi, o da bir başarı!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Bir diş dört dokudan yapılır: mine, dentin, öz ve sement.",
        "spoken": "Bir diş dört dokudan yapılır: mine, dentin, öz ve sement.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "En dışta mine vardır. Mine, vücudunun en sert dokusudur ve dişin görünen kısmı olan kronu örter.",
        "spoken": "En dışta mine vardır. Mine, vücudunun en sert dokusudur ve dişin görünen kısmı olan kronu örter.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l11",
        "display": "Minenin altında dentin bulunur: sarımsı, kemik kadar sert bir madde. Dişin büyük bölümünü o oluşturur.",
        "spoken": "Minenin altında dentin bulunur: sarımsı, kemik kadar sert bir madde. Dişin büyük bölümünü o oluşturur.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l12",
        "display": "En içte öz, yani pulpa vardır. Sinirler ve kan damarları buradadır; dişin sıcağı soğuğu hissetmesi buradan gelir.",
        "spoken": "En içte öz, yani pulpa vardır. Sinirler ve kan damarları buradadır; dişin sıcağı soğuğu hissetmesi buradan gelir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l13",
        "display": "Kökün dışını ise sement örter. Diş etinin altında kalır ve dişi çene kemiğinde sıkıca tutar.",
        "spoken": "Kökün dışını ise sement örter. Diş etinin altında kalır ve dişi çene kemiğinde sıkıca tutar.",
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
        "id": "l14",
        "display": "Peki hangi diş ne iş yapar? Öndeki keskin kenarlı dişlere kesici denir: ısırdığımızda besini keserler.",
        "spoken": "Peki hangi diş ne iş yapar? Öndeki keskin kenarlı dişlere kesici denir: ısırdığımızda besini keserler.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l15",
        "display": "Yanlarında sivri köpek dişleri durur.",
        "spoken": "Yanlarında sivri köpek dişleri durur.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l16",
        "display": "Arkada küçük azılar besini öğütüp ezer. En arkadaki azı dişleri ise girintili çıkıntılı yüzeyleriyle güçlü çiğnemeyi sağlar.",
        "spoken": "Arkada küçük azılar besini öğütüp ezer. En arkadaki azı dişleri ise girintili çıkıntılı yüzeyleriyle güçlü çiğnemeyi sağlar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l17",
        "display": "Yani ağzında bir makas, bir öğütücü ve bir değirmen var. Mutfak robotu gibisin!",
        "spoken": "Yani ağzında bir makas, bir öğütücü ve bir değirmen var. Mutfak robotu gibisin!",
        "factIds": [
          "f3",
          "f9"
        ]
      },
      {
        "id": "l18",
        "display": "İlk kalıcı azılar 5–7 yaş arasında çıkar; bunlara 6 yaş dişleri denir.",
        "spoken": "İlk kalıcı azılar beş ile yedi yaş arasında çıkar; bunlara altı yaş dişleri denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l19",
        "display": "İkinci kalıcı azılar 11–14 yaş arasında gelir; bunlar da 12 yaş dişleri. Üçüncü azılar ise yirmi yaş dişleridir.",
        "spoken": "İkinci kalıcı azılar on bir ile on dört yaş arasında gelir; bunlar da on iki yaş dişleri. Üçüncü azılar ise yirmi yaş dişleridir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l20",
        "display": "Dişler yalnızca yemek için değil: düzgün konuşmak için de onlara ihtiyacımız var.",
        "spoken": "Dişler yalnızca yemek için değil: düzgün konuşmak için de onlara ihtiyacımız var.",
        "factIds": [
          "f3"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l21",
        "display": "Şimdi çürüğe gelelim. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre ağzımızda yüzlerce farklı türde bakteri yaşar.",
        "spoken": "Şimdi çürüğe gelelim. Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'ye göre ağzımızda yüzlerce farklı türde bakteri yaşar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l22",
        "display": "Bazı bakteriler dişlerin üstünde plak denen yapışkan, renksiz bir tabaka oluşturur.",
        "spoken": "Bazı bakteriler dişlerin üstünde plak denen yapışkan, renksiz bir tabaka oluşturur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Bu bakteriler besinlerdeki şekeri kullanarak asit üretir. Asit de minenin sert yüzeyini aşındırmaya başlar.",
        "spoken": "Bu bakteriler besinlerdeki şekeri kullanarak asit üretir. Asit de minenin sert yüzeyini aşındırmaya başlar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Asit saldırıları tekrarlandıkça mine mineral kaybeder.",
        "spoken": "Asit saldırıları tekrarlandıkça mine mineral kaybeder.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l25",
        "display": "NIH bunu şöyle anlatıyor: gün boyunca ağzımızda bir halat çekme yarışı sürer.",
        "spoken": "En Ay Eyç bunu şöyle anlatıyor: gün boyunca ağzımızda bir halat çekme yarışı sürer.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l26",
        "display": "Bir tarafta şeker ve bakteriler. Öbür tarafta tükürük ve florür: mine, tükürükteki mineralleri ve diş macunundaki florürü kullanarak kendini onarabilir.",
        "spoken": "Bir tarafta şeker ve bakteriler. Öbür tarafta tükürük ve florür: mine, tükürükteki mineralleri ve diş macunundaki florürü kullanarak kendini onarabilir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Erken aşamada çürük durdurulabilir, hatta geri döndürülebilir.",
        "spoken": "Erken aşamada çürük durdurulabilir, hatta geri döndürülebilir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Ama bakteriler kazanırsa dişte oyuk oluşur. Bu kalıcı bir hasardır ve dişçinin dolguyla onarması gerekir.",
        "spoken": "Ama bakteriler kazanırsa dişte oyuk oluşur. Bu kalıcı bir hasardır ve dişçinin dolguyla onarması gerekir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l29",
        "display": "Halat çekmede hangi tarafı tuttuğunu biliyorsun, değil mi?",
        "spoken": "Halat çekmede hangi tarafı tuttuğunu biliyorsun, değil mi?",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Kazanmanın yolu basit: dişlerini günde iki kez, yaklaşık 2 dakika florürlü macunla fırçala. Dişlerinin arasını da günde bir kez diş ipiyle temizle.",
        "spoken": "Kazanmanın yolu basit: dişlerini günde iki kez, yaklaşık iki dakika florürlü macunla fırçala. Dişlerinin arasını da günde bir kez diş ipiyle temizle.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l31",
        "display": "Şekerli içecekleri ve yapışkan atıştırmalıkları sınırla; dişçine de düzenli git.",
        "spoken": "Şekerli içecekleri ve yapışkan atıştırmalıkları sınırla; dişçine de düzenli git.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! İki dakikalık bir şarkı seç ve dişlerini şarkı bitene kadar fırçala. Sonra aynada azı dişlerinin girintili yüzeyine bak.",
        "spoken": "Şimdi sıra sende! İki dakikalık bir şarkı seç ve dişlerini şarkı bitene kadar fırçala. Sonra aynada azı dişlerinin girintili yüzeyine bak.",
        "factIds": [
          "f15",
          "f9"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l33",
        "display": "Bunu biliyor muydun? Çocuklarda ve gençlerde çürüklerin çoğu arkadaki azı dişlerinde gelişir. Dişçiler bu dişlerin yüzeyini ince bir plastik kaplamayla koruyabilir.",
        "spoken": "Bunu biliyor muydun? Çocuklarda ve gençlerde çürüklerin çoğu arkadaki azı dişlerinde gelişir. Dişçiler bu dişlerin yüzeyini ince bir plastik kaplamayla koruyabilir.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l34",
        "display": "Bir de şu: uyurken tükürük akışı azalır. Bu yüzden yatmadan önce fırçalamak çok önemli!",
        "spoken": "Bir de şu: uyurken tükürük akışı azalır. Bu yüzden yatmadan önce fırçalamak çok önemli!",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l35",
        "display": "Hızlı soru! Vücudun en sert dokusu hangisidir?",
        "spoken": "Hızlı soru! Vücudun en sert dokusu hangisidir?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l36",
        "display": "Düşün bakalım... Evet: diş minesi!",
        "spoken": "Düşün bakalım... Evet: diş minesi!",
        "factIds": [
          "f5"
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
        "display": "Abone olmayı ve zili açmayı unutma. Bu akşam fırçalamayı da!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bu akşam fırçalamayı da!",
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
    "statement": "İlk diş takımı 20 süt dişidir; yerlerini 32 kalıcı diş alır. Süt dişleri doğumdan önce gelişmeye başlar ve çocuk yaklaşık 6 yaşındayken düşmeye başlar.",
    "numbers": [
      "20",
      "32",
      "6"
    ]
  },
  {
    "id": "f2",
    "statement": "İlk kalıcı azı dişleri ('6 yaş dişleri') 5–7 yaş arasında, ikinci kalıcı azılar ('12 yaş dişleri') 11–14 yaş arasında çıkar; üçüncü azılar yirmi yaş dişleridir.",
    "numbers": [
      "6",
      "5",
      "7",
      "12",
      "11",
      "14"
    ]
  },
  {
    "id": "f3",
    "statement": "Dişler konuşmak ve düzgün yemek için gereklidir; yerken dişlerimiz besini yutmaya hazırlamak için yırtar, keser ve öğütür.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "İnsan dişleri dört dokudan oluşur: öz (pulpa), dentin, mine ve sement.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Mine vücudun en sert dokusudur; dentini örter ve kronun en dış katmanını oluşturur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Dentin sert, sarı bir maddedir; dişin büyük bölümünü oluşturur ve kemik kadar serttir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Öz (pulpa) dişin en iç kısmıdır; bağ dokusu, sinirler ve kan damarlarından oluşur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Sement kökün dışını diş etinin altında örter ve dişi çene kemiğinde yerinde tutar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Kesici dişler ağzın önündeki keskin kenarlı dişlerdir ve ısırdığımızda besini keser; yanlarında sivri köpek dişleri bulunur; küçük azılar besini öğütüp ezer; azı dişleri güçlü çiğnemeyi sağlar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Diş çürüğü, besinlerdeki şekerleri kullanarak asit yapan bazı bakterilerin yol açtığı bir enfeksiyondur; asitler minenin sert dış yüzeyini aşındırmaya başlar; tekrarlanan asit saldırıları minenin mineral kaybetmesine yol açar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Plak, bakterilerden oluşan yapışkan, renksiz bir tabakadır; ağzımızda yüzlerce farklı türde bakteri yaşar.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Bu aşamada çürük durdurulabilir ya da geri döndürülebilir; mine tükürükteki mineralleri ve diş macunu gibi kaynaklardaki florürü kullanarak kendini onarabilir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Oyuk (kavite), dişçinin dolguyla onarması gereken kalıcı bir hasardır.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Gün boyunca ağzımızda bir halat çekme yarışı sürer.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Dişleri günde iki kez, yaklaşık 2 dakika florürlü diş macunuyla fırçalamak gerekir; dişler arası günde bir kez ip ile temizlenmelidir.",
    "numbers": [
      "2"
    ]
  },
  {
    "id": "f16",
    "statement": "Şeker, kurabiye, gazlı ve şekerli içecekler özel günlere saklanmalı; meyve suyu, şekerli atıştırmalıklar ve kuru meyve gibi yapışkan besinler sınırlanmalıdır; dişçiye düzenli gidilmelidir.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Fissür örtücüler, arka dişlerin (azıların) çiğneme yüzeylerine sürülen ince plastik kaplamalardır; çocuklarda ve gençlerde çürüklerin çoğu azı dişlerinde gelişir.",
    "numbers": []
  },
  {
    "id": "f18",
    "statement": "Uyku sırasında tükürük akışı azalır.",
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
