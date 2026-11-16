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
        "display": "Az önce bir dilim ekmek yedin. Peki o ekmek şimdi nerede ve ona ne oluyor?",
        "spoken": "Az önce bir dilim ekmek yedin. Peki o ekmek şimdi nerede ve ona ne oluyor?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Yediğin her lokma, vücudunun içinde uzun bir yolculuğa çıkar.",
        "spoken": "Yediğin her lokma, vücudunun içinde uzun bir yolculuğa çıkar.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün bu yolculuğa biz de katılıyoruz: sindirim kanalının içine giriyoruz!",
        "spoken": "Bugün bu yolculuğa biz de katılıyoruz: sindirim kanalının içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Sindirime neden ihtiyacımız var? Lokma hangi yollardan geçer? Ve vücut onu nasıl kullanır?",
        "spoken": "Üç sorumuz var. Sindirime neden ihtiyacımız var? Lokma hangi yollardan geçer? Ve vücut onu nasıl kullanır?",
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
        "display": "KidsHealth'e göre besin bizim yakıtımızdır. İçindeki besin öğeleri hücrelerimize enerji ve gereken maddeleri verir.",
        "spoken": "Kids Helt'e göre besin bizim yakıtımızdır. İçindeki besin öğeleri hücrelerimize enerji ve gereken maddeleri verir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Ama önce vücudun emebileceği küçük parçalara ayrılması gerekir. İşte buna sindirim denir.",
        "spoken": "Ama önce vücudun emebileceği küçük parçalara ayrılması gerekir. İşte buna sindirim denir.",
        "factIds": [
          "f1",
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Ben de yakıtla çalışırım, ama benimki bir priz. Hiç çiğnemem gerekmiyor!",
        "spoken": "Ben de yakıtla çalışırım, ama benimki bir priz. Hiç çiğnemem gerekmiyor!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Sindirim midede değil, ağızda başlar. Dişlerin lokmayı koparır ve doğrar.",
        "spoken": "Sindirim midede değil, ağızda başlar. Dişlerin lokmayı koparır ve doğrar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Tükürük bezlerinin yaptığı tükürük de lokmayı ıslatır; böylece kolayca yutulur.",
        "spoken": "Tükürük bezlerinin yaptığı tükürük de lokmayı ıslatır; böylece kolayca yutulur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Tükürükte amilaz denen bir sindirim enzimi vardır. Amilaz, nişasta gibi karbonhidratları parçalamaya başlar.",
        "spoken": "Tükürükte amilaz denen bir sindirim enzimi vardır. Amilaz, nişasta gibi karbonhidratları parçalamaya başlar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Yemeği koklamak, hatta düşünmek bile ağzını sulandırabilir. Çünkü beynin tükürük bezlerine sinyal gönderir.",
        "spoken": "Yemeği koklamak, hatta düşünmek bile ağzını sulandırabilir. Çünkü beynin tükürük bezlerine sinyal gönderir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Benim ağzım hiç sulanmaz. Sulansaydı kısa devre yapardım!",
        "spoken": "Benim ağzım hiç sulanmaz. Sulansaydı kısa devre yapardım!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Yutarken dilin lokmayı boğaza iter. NIDDK'ye göre bu sırada epiglot denen küçük bir doku kapağı soluk borunun üstüne kapanır; böylece boğulmayız.",
        "spoken": "Yutarken dilin lokmayı boğaza iter. En Ay Di Di Key'ye göre bu sırada epiglot denen küçük bir doku kapağı soluk borunun üstüne kapanır; böylece boğulmayız.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Lokma sonra yemek borusuna girer. Yemek borusunun kasları dalga dalga kasılıp lokmayı aşağı iter. Bu dalgalara peristalsis denir.",
        "spoken": "Lokma sonra yemek borusuna girer. Yemek borusunun kasları dalga dalga kasılıp lokmayı aşağı iter. Bu dalgalara peristalsis denir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Yemek borusunun sonunda sfinkter denen bir kas halka vardır. Genelde kapalı durur ve midedekilerin geri kaçmasını engeller.",
        "spoken": "Yemek borusunun sonunda sfinkter denen bir kas halka vardır. Genelde kapalı durur ve midedekilerin geri kaçmasını engeller.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Mide kaslı bir torbadır. Kasları lokmayı çalkalar ve sindirim sıvılarıyla karıştırır.",
        "spoken": "Mide kaslı bir torbadır. Kasları lokmayı çalkalar ve sindirim sıvılarıyla karıştırır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l18",
        "display": "Mide duvarındaki bezler mide asidi ve enzimler yapar. KidsHealth'e göre midedeki sindirim için asitli bir ortam gerekir.",
        "spoken": "Mide duvarındaki bezler mide asidi ve enzimler yapar. Kids Helt'e göre midedeki sindirim için asitli bir ortam gerekir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l19",
        "display": "Lokma burada koyu bir lapaya dönüşür; buna kimus denir. Mide kimusu yavaş yavaş ince bağırsağa boşaltır.",
        "spoken": "Lokma burada koyu bir lapaya dönüşür; buna kimus denir. Mide kimusu yavaş yavaş ince bağırsağa boşaltır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l20",
        "display": "Midenin çıkışında ceviz büyüklüğünde bir kas kapak vardır: pilor. Pilor, kimusu zamanı gelene kadar midede tutar.",
        "spoken": "Midenin çıkışında ceviz büyüklüğünde bir kas kapak vardır: pilor. Pilor, kimusu zamanı gelene kadar midede tutar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l21",
        "display": "Benim de bir kapağım var: pil kapağı. Ama o pilor değil, sadece pil yeri!",
        "spoken": "Benim de bir kapağım var: pil kapağı. Ama o pilor değil, sadece pil yeri!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l22",
        "display": "Şimdi asıl iş başlıyor: ince bağırsak! Ona ince denmesinin nedeni genişliğidir, uzunluğu değil.",
        "spoken": "Şimdi asıl iş başlıyor: ince bağırsak! Ona ince denmesinin nedeni genişliğidir, uzunluğu değil.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Aslında ince bağırsak, kalın bağırsaktan çok daha uzundur.",
        "spoken": "Aslında ince bağırsak, kalın bağırsaktan çok daha uzundur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "İnce bağırsağın kasları kimusu pankreastan, karaciğerden ve bağırsağın kendisinden gelen sindirim sıvılarıyla karıştırır.",
        "spoken": "İnce bağırsağın kasları kimusu pankreastan, karaciğerden ve bağırsağın kendisinden gelen sindirim sıvılarıyla karıştırır.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l25",
        "display": "Karaciğer safra denen bir sıvı yapar; safra yağların sindirimine yardım eder. Safra kesesi safrayı öğünler arasında saklar.",
        "spoken": "Karaciğer safra denen bir sıvı yapar; safra yağların sindirimine yardım eder. Safra kesesi safrayı öğünler arasında saklar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Pankreas ise karbonhidratları, yağları ve proteinleri parçalayan enzimler yapar.",
        "spoken": "Pankreas ise karbonhidratları, yağları ve proteinleri parçalayan enzimler yapar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi çıkıntıyla kaplıdır. Bunlara villus denir.",
        "spoken": "İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi çıkıntıyla kaplıdır. Bunlara villus denir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Sindirilmiş besinler ve su, ince bağırsağın duvarından geçerek kana karışır. Villuslar bu işin taşıyıcılarıdır.",
        "spoken": "Sindirilmiş besinler ve su, ince bağırsağın duvarından geçerek kana karışır. Villuslar bu işin taşıyıcılarıdır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l29",
        "display": "Villus kelimesini duyunca virüs sanma sakın. Villus dostumuz!",
        "spoken": "Villus kelimesini duyunca virüs sanma sakın. Villus dostumuz!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Geriye kalanlar kalın bağırsağa gider. NIDDK'ye göre kalın bağırsak suyu emer ve atığı sıvıdan katıya, yani kakaya dönüştürür.",
        "spoken": "Geriye kalanlar kalın bağırsağa gider. En Ay Di Di Key'ye göre kalın bağırsak suyu emer ve atığı sıvıdan katıya, yani kakaya dönüştürür.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l31",
        "display": "Kalın bağırsaktaki bakteriler kalan besinleri parçalamaya yardım eder ve K vitamini yapar. İçinde sana yardım eden minik dostlar yaşıyor!",
        "spoken": "Kalın bağırsaktaki bakteriler kalan besinleri parçalamaya yardım eder ve K vitamini yapar. İçinde sana yardım eden minik dostlar yaşıyor!",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l32",
        "display": "Bu yolculuk birkaç dakikada bitmez. KidsHealth'e göre besinin tamamen sindirilmesi saatler sürer.",
        "spoken": "Bu yolculuk birkaç dakikada bitmez. Kids Helt'e göre besinin tamamen sindirilmesi saatler sürer.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l33",
        "display": "Şimdi sıra sende! Bir sonraki öğünde ilk lokmayı hemen yutma; yavaş yavaş, uzun uzun çiğne.",
        "spoken": "Şimdi sıra sende! Bir sonraki öğünde ilk lokmayı hemen yutma; yavaş yavaş, uzun uzun çiğne.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l34",
        "display": "Lokmanın nasıl yumuşayıp ıslandığına dikkat et: tükürük ve amilaz iş başında! Ağzın doluyken konuşma ve gülme.",
        "spoken": "Lokmanın nasıl yumuşayıp ıslandığına dikkat et: tükürük ve amilaz iş başında! Ağzın doluyken konuşma ve gülme.",
        "factIds": [
          "f3",
          "f4"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l35",
        "display": "Bunu biliyor muydun? KidsHealth'e göre bir yetişkinin sindirim kanalı yaklaşık 9 metre uzunluğundadır!",
        "spoken": "Bunu biliyor muydun? Kids Helt'e göre bir yetişkinin sindirim kanalı yaklaşık dokuz metre uzunluğundadır!",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l36",
        "display": "Benim kablolarım bu kadar uzun olsaydı, kesin düğüm olurdu!",
        "spoken": "Benim kablolarım bu kadar uzun olsaydı, kesin düğüm olurdu!",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "Hızlı soru! Besinleri kana geçiren, parmak gibi minik çıkıntıların adı neydi?",
        "spoken": "Hızlı soru! Besinleri kana geçiren, parmak gibi minik çıkıntıların adı neydi?",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l38",
        "display": "Düşün bakalım... Evet: villus!",
        "spoken": "Düşün bakalım... Evet: villus!",
        "factIds": [
          "f12"
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
        "display": "Abone olmayı ve zili açmayı unutma. Afiyet olsun!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Afiyet olsun!",
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
    "statement": "Besin yakıtımızdır; besin öğeleri hücrelere çalışmak için gereken enerjiyi ve maddeleri verir; ama önce vücudun emip kullanabileceği küçük parçalara sindirilmelidir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Sindirim sistemi besin öğelerini vücudun emip enerji için kullanabileceği kadar küçük parçalara ayırır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Sindirim ağızda, besin mideye ulaşmadan çok önce başlar; dişler besini koparıp doğrar, tükürük onu ıslatır; tükürüğü tükürük bezleri yapar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Tükürükteki amilaz adlı sindirim enzimi bazı karbonhidratları parçalamaya başlar; tükürükteki enzim nişastaları parçalamaya başlar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Yemeği koklamak ya da düşünmek bile ağzı sulandırabilir; beyin tükürük bezlerine sinyal gönderir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Yutarken dil besini boğaza iter; epiglot denen küçük doku kapağı boğulmayı önlemek için soluk borusunun üstüne kapanır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Peristalsis denen kas kasılma dalgaları besini yemek borusundan mideye iter.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Yemek borusunun sonundaki sfinkter genelde kapalı durur ve mide içeriğinin yemek borusuna geri akmasını engeller.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Mide kasları besini asit ve enzim içeren sindirim sıvılarıyla çalkalayıp karıştırır; mide duvarındaki bezler mide asidi ve enzim yapar; midedeki sindirim için asitli ortam gerekir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Mide, kimus denen içeriğini yavaş yavaş ince bağırsağa boşaltır; midenin çıkışındaki ceviz büyüklüğündeki pilor kapağı kimusu midede tutar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "İnce bağırsağa uzunluğu yüzünden değil genişliği yüzünden ince denir; aslında kalın bağırsaktan çok daha uzundur.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi villus ile kaplıdır; besinler villuslar aracılığıyla kana emilir; ince bağırsak duvarları suyu ve sindirilmiş besinleri kana emer.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "İnce bağırsağın kasları besini pankreas, karaciğer ve bağırsaktan gelen sindirim sıvılarıyla karıştırır; karaciğer yağların sindirimine yardım eden safrayı yapar; safra kesesi safrayı öğünler arasında saklar; pankreas karbonhidrat, yağ ve proteinleri parçalayan enzimler yapar.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Kalın bağırsak suyu emer ve atığı sıvıdan katı dışkıya dönüştürür.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Kalın bağırsaktaki bakteriler kalan besin öğelerini parçalamaya yardım eder ve K vitamini yapar.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Bir yetişkinin sindirim kanalı yaklaşık 9 metre uzunluğundadır.",
    "numbers": [
      "9"
    ]
  },
  {
    "id": "f17",
    "statement": "Vücudun besini tamamen sindirmesi saatler sürer.",
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
