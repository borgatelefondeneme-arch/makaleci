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
        "display": "Gökyüzünde dalgalanan yeşil ve mor ışık perdeleri... Bu muhteşem gösterinin arkasında dev bir mıknatıs var: Dünya'nın kendisi!",
        "spoken": "Gökyüzünde dalgalanan yeşil ve mor ışık perdeleri... Bu muhteşem gösterinin arkasında dev bir mıknatıs var: Dünya'nın kendisi!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l2",
        "display": "Mıknatıslar nasıl çeker? Ve Dünya nasıl mıknatıs olur?",
        "spoken": "Mıknatıslar nasıl çeker? Ve Dünya nasıl mıknatıs olur?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün görünmez bir kuvvetin izini sürüyoruz!",
        "spoken": "Bugün görünmez bir kuvvetin izini sürüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Mıknatısı mıknatıs yapan nedir? Dünya'nın manyetik alanı nereden gelir? Ve bu alan bizi neden korur?",
        "spoken": "Üç sorumuz var. Mıknatısı mıknatıs yapan nedir? Dünya'nın manyetik alanı nereden gelir? Ve bu alan bizi neden korur?",
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
        "display": "National Geographic'e göre manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir.",
        "spoken": "Neşınıl Ciyografik'e göre manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Her mıknatısın bir kuzey, bir de güney kutbu vardır. Zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.",
        "spoken": "Her mıknatısın bir kuzey, bir de güney kutbu vardır. Zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Mıknatısın çevresinde, kuvvetinin etkili olduğu görünmez bir bölge vardır. Buna manyetik alan denir.",
        "spoken": "Mıknatısın çevresinde, kuvvetinin etkili olduğu görünmez bir bölge vardır. Buna manyetik alan denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l9",
        "display": "Peki bu kuvvet nereden gelir? Atomlara bakmamız gerek. Elektronlar atomun çekirdeği çevresinde topaç gibi dönerek dolanır.",
        "spoken": "Peki bu kuvvet nereden gelir? Atomlara bakmamız gerek. Elektronlar atomun çekirdeği çevresinde topaç gibi dönerek dolanır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Bu hareket yüzünden her elektron, minicik bir mıknatıs gibi davranır.",
        "spoken": "Bu hareket yüzünden her elektron, minicik bir mıknatıs gibi davranır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Çoğu maddede elektronların yarısı bir yöne, yarısı öbür yöne döner. Manyetizmaları birbirini sıfırlar. Kâğıdın, kumaşın mıknatısa yapışmamasının nedeni bu.",
        "spoken": "Çoğu maddede elektronların yarısı bir yöne, yarısı öbür yöne döner. Manyetizmaları birbirini sıfırlar. Kâğıdın, kumaşın mıknatısa yapışmamasının nedeni bu.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Ama demirde, kobaltta ve nikelde elektronların çoğu aynı yöne döner. Minik mıknatıslar aynı tarafa bakınca güçlü bir mıknatıs ortaya çıkar.",
        "spoken": "Ama demirde, kobaltta ve nikelde elektronların çoğu aynı yöne döner. Minik mıknatıslar aynı tarafa bakınca güçlü bir mıknatıs ortaya çıkar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Ben de biraz demirden yapıldım. Buzdolabının yanından geçerken dikkatli olmam gerek!",
        "spoken": "Ben de biraz demirden yapıldım. Buzdolabının yanından geçerken dikkatli olmam gerek!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Elektrikle de mıknatıs yapabilirsin! Bir tel bobininden akım geçirince çevresinde manyetik alan oluşur.",
        "spoken": "Elektrikle de mıknatıs yapabilirsin! Bir tel bobininden akım geçirince çevresinde manyetik alan oluşur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Akımı kesince alan kaybolur. Buna elektromıknatıs denir: istediğinde açıp kapatabileceğin bir mıknatıs.",
        "spoken": "Akımı kesince alan kaybolur. Buna elektromıknatıs denir: istediğinde açıp kapatabileceğin bir mıknatıs.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Şimdi en büyük mıknatısa geçelim: Dünya! Britanya Jeoloji Araştırmaları Kurumu'na göre manyetik alanımız, Dünya'nın sıvı dış çekirdeğinde oluşur.",
        "spoken": "Şimdi en büyük mıknatısa geçelim: Dünya! Britanya Jeoloji Araştırmaları Kurumu'na göre manyetik alanımız, Dünya'nın sıvı dış çekirdeğinde oluşur.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Orada yavaşça hareket eden erimiş demirde elektrik akımları akar. Bu akımlar manyetik alanı üretir. Bu düzeneğe dinamo denir.",
        "spoken": "Orada yavaşça hareket eden erimiş demirde elektrik akımları akar. Bu akımlar manyetik alanı üretir. Bu düzeneğe dinamo denir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l18",
        "display": "Yani Dünya, içinde dev bir elektromıknatıs taşıyor!",
        "spoken": "Yani Dünya, içinde dev bir elektromıknatıs taşıyor!",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Bir şaşırtıcı ayrıntı: manyetik kutuplar, haritadaki Kuzey ve Güney Kutbu ile aynı yerde değildir.",
        "spoken": "Bir şaşırtıcı ayrıntı: manyetik kutuplar, haritadaki Kuzey ve Güney Kutbu ile aynı yerde değildir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l20",
        "display": "Üstelik yerinde de durmaz. ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre Kuzey Manyetik Kutbu, son ölçüme göre yılda yaklaşık 55 kilometre hızla ilerliyor.",
        "spoken": "Üstelik yerinde de durmaz. A Be De Ulusal Okyanus ve Atmosfer Dairesi, Noa'ya göre Kuzey Manyetik Kutbu, son ölçüme göre yılda yaklaşık elli beş kilometre hızla ilerliyor.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Hatta manyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirmiş: kuzey güney, güney kuzey olmuş! Bu değişim yavaş ve düzensiz olur.",
        "spoken": "Hatta manyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirmiş: kuzey güney, güney kuzey olmuş! Bu değişim yavaş ve düzensiz olur.",
        "factIds": [
          "f9"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l22",
        "display": "Bu manyetik alan bizi korur. Dünya'yı saran bu koruyucu bölgeye manyetosfer denir.",
        "spoken": "Bu manyetik alan bizi korur. Dünya'yı saran bu koruyucu bölgeye manyetosfer denir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "NASA'ya göre Güneş'ten saatte 1 milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır.",
        "spoken": "Nasa'ya göre Güneş'ten saatte bir milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Karşılaştırma için Mars'a bak: Mars, manyetosferini yaklaşık 4,2 milyar yıl önce kaybetmiş.",
        "spoken": "Karşılaştırma için Mars'a bak: Mars, manyetosferini yaklaşık dört virgül iki milyar yıl önce kaybetmiş.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Bazı parçacıklar yine de içeri sızar ve atmosferdeki gazlarla etkileşir. İşte o ışık perdeleri böyle oluşur!",
        "spoken": "Bazı parçacıklar yine de içeri sızar ve atmosferdeki gazlarla etkileşir. İşte o ışık perdeleri böyle oluşur!",
        "factIds": [
          "f10",
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Oksijen yeşil ve kırmızı, azot ise mavi ve mor ışık verir. Kuzey Kutbu yakınında bu gösteriye kuzey ışıkları denir.",
        "spoken": "Oksijen yeşil ve kırmızı, azot ise mavi ve mor ışık verir. Kuzey Kutbu yakınında bu gösteriye kuzey ışıkları denir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Pusula da bu alan sayesinde çalışır: iğnesi, Dünya'nın manyetik kutuplarıyla aynı hizaya gelir.",
        "spoken": "Pusula da bu alan sayesinde çalışır: iğnesi, Dünya'nın manyetik kutuplarıyla aynı hizaya gelir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Pusulanın hikâyesi eskidir. Eski Yunanlılar ve Çinliler, mıknatıs taşı denen doğal manyetik taşları biliyordu.",
        "spoken": "Pusulanın hikâyesi eskidir. Eski Yunanlılar ve Çinliler, mıknatıs taşı denen doğal manyetik taşları biliyordu.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l29",
        "display": "Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslamayı keşfetti. Pusulayla yön bulmaya dair en eski yazılar 11. yüzyıla ait.",
        "spoken": "Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslamayı keşfetti. Pusulayla yön bulmaya dair en eski yazılar on birinci yüzyıla ait.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l30",
        "display": "Bazı hayvanların içinde de pusula var gibi: güvercinler, arılar ve somon balıkları manyetik alanı algılayıp yön bulabilir. Bilim insanları bunu nasıl yaptıklarından emin değil.",
        "spoken": "Bazı hayvanların içinde de pusula var gibi: güvercinler, arılar ve somon balıkları manyetik alanı algılayıp yön bulabilir. Bilim insanları bunu nasıl yaptıklarından emin değil.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l31",
        "display": "Benim içimde GPS var. Ama güvercinlerin kini daha az pil yiyor!",
        "spoken": "Benim içimde GPS var. Ama güvercinlerin kini daha az pil yiyor!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Masaya bir buzdolabı mıknatısı koy. Ataş, alüminyum folyo, kâğıt ve bozuk para gibi eşyaları teker teker yaklaştır.",
        "spoken": "Şimdi sıra sende! Masaya bir buzdolabı mıknatısı koy. Ataş, alüminyum folyo, kâğıt ve bozuk para gibi eşyaları teker teker yaklaştır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l33",
        "display": "Hangileri yapışıyor, hangileri yapışmıyor? Bir tabloya yaz. Bir uyarı: mıknatısları telefonlardan ve bilgisayarlardan uzak tut; küçük mıknatısları asla ağzına alma.",
        "spoken": "Hangileri yapışıyor, hangileri yapışmıyor? Bir tabloya yaz. Bir uyarı: mıknatısları telefonlardan ve bilgisayarlardan uzak tut; küçük mıknatısları asla ağzına alma.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l34",
        "display": "Bunu biliyor muydun? Mart 1989'daki güçlü bir manyetik fırtına, Kanada'nın Quebec eyaletinde elektrik sistemini 9 saatten uzun süre kapattı.",
        "spoken": "Bunu biliyor muydun? Mart bin dokuz yüz seksen dokuzdaki güçlü bir manyetik fırtına, Kanada'nın Kebek eyaletinde elektrik sistemini dokuz saatten uzun süre kapattı.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l35",
        "display": "Hızlı soru! İki mıknatısın kuzey kutuplarını birbirine yaklaştırırsan ne olur?",
        "spoken": "Hızlı soru! İki mıknatısın kuzey kutuplarını birbirine yaklaştırırsan ne olur?",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l36",
        "display": "Düşün bakalım... Evet: birbirlerini iterler!",
        "spoken": "Düşün bakalım... Evet: birbirlerini iterler!",
        "factIds": [
          "f2"
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben de buzdolabından uzak durarak eve dönüyorum!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de buzdolabından uzak durarak eve dönüyorum!",
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
    "statement": "Manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir; elektrik yüklerinin hareketinden kaynaklanır; manyetik alan, mıknatısın çevresinde manyetik kuvvetin etkili olduğu bölgedir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Bütün mıknatısların kuzey ve güney kutbu vardır; zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Elektronlar topaç gibi dönerek atom çekirdeğinin çevresinde dolanır; bu hareket her elektronun mikroskobik bir mıknatıs gibi davranmasına yol açar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Demir, kobalt ve nikel gibi maddelerde elektronların çoğu aynı yönde döner; çoğu maddede eşit sayıda elektron zıt yönlerde döner ve manyetizmalarını birbirine sıfırlar; bu yüzden kumaş ya da kâğıt zayıf manyetik sayılır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bir tel bobininden elektrik geçince manyetik alan oluşur; akım kesilince bobinin çevresindeki alan kaybolur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Dünya'nın manyetik alanı, sıvı dış çekirdekte kendi kendini besleyen bir dinamo süreciyle oluşur; yavaş hareket eden erimiş demirde akan elektrik akımları manyetik alanı üretir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Jeomanyetik kutuplar Kuzey ve Güney Kutbu ile aynı değildir; mıknatısın kuzey ucu, güney manyetik yük taşıyan Kuzey Manyetik Kutbu'nu gösterir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Son ölçüme göre Kuzey Manyetik Kutbu yılda yaklaşık 55 kilometre hızla kuzey-kuzeybatıya doğru ilerliyor; Kanada Arktiği boyunca yavaşça sürükleniyor.",
    "numbers": [
      "55"
    ]
  },
  {
    "id": "f9",
    "statement": "Jeomanyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirdi; bu dönüşler yavaş ve düzensiz olur.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Manyetosfer, Güneş'ten saatte 1 milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır; Dünya'yı parçacıkların çoğundan korur.",
    "numbers": [
      "1"
    ]
  },
  {
    "id": "f11",
    "statement": "Mars, manyetosferini yaklaşık 4,2 milyar yıl önce kaybetmiş bir gezegendir.",
    "numbers": [
      "4.2"
    ]
  },
  {
    "id": "f12",
    "statement": "Parçacıklar atmosferdeki gazlarla etkileşir ve gökyüzünde güzel ışık gösterileri oluşur; oksijen yeşil ve kırmızı, azot mavi ve mor ışık verir; Kuzey Kutbu yakınında buna kuzey ışıkları denir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Pusulanın manyetik iğnesi Dünya'nın manyetik kutuplarıyla aynı hizaya gelir; insanlar yüzlerce yıldır yön bulmak için pusula kullanıyor.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Eski Yunanlılar ve Çinliler mıknatıs taşı denen doğal manyetik taşları biliyordu; Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslayabileceklerini keşfetti; pusulayla yön bulmaya ilişkin en eski yazılar 11. yüzyıla aittir.",
    "numbers": [
      "11"
    ]
  },
  {
    "id": "f15",
    "statement": "Güvercinler, arılar ve somonlar gibi bazı hayvanlar Dünya'nın manyetik alanını algılayıp yön bulmak için kullanabilir; bilim insanları bunu nasıl yaptıklarından emin değil.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Son zamanların en şiddetli manyetik fırtınası Mart 1989'da oldu; Kanada'nın Quebec eyaletinde elektrik iletim sistemi 9 saatten uzun süre kapandı.",
    "numbers": [
      "1989",
      "9"
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
