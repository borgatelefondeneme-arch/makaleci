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
        "display": "Yağmur diniyor, Güneş çıkıyor ve gökyüzünde renkli, dev bir yay beliriyor!",
        "spoken": "Yağmur diniyor, Güneş çıkıyor ve gökyüzünde renkli, dev bir yay beliriyor!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Peki bu renkler nereden geliyor? Ve gökkuşağı neden hep yay biçiminde?",
        "spoken": "Peki bu renkler nereden geliyor? Ve gökkuşağı neden hep yay biçiminde?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir yağmur damlasının içine giriyoruz!",
        "spoken": "Bugün bir yağmur damlasının içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Gerçi ben damlanın içine giremem. Su ile robot pek iyi anlaşmaz!",
        "spoken": "Gerçi ben damlanın içine giremem. Su ile robot pek iyi anlaşmaz!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Beyaz ışığın içinde ne saklı? Bir damla ışığa ne yapar? Ve gökkuşağı neden yay biçimindedir?",
        "spoken": "Üç sorumuz var. Beyaz ışığın içinde ne saklı? Bir damla ışığa ne yapar? Ve gökkuşağı neden yay biçimindedir?",
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
        "display": "National Geographic'e göre gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.",
        "spoken": "Neşınıl Ciyografik'e göre gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "İlk sır Güneş ışığında. Bize beyaz görünür; ama beyaz ışık, gökkuşağının bütün renklerinin karışımıdır.",
        "spoken": "İlk sır Güneş ışığında. Bize beyaz görünür; ama beyaz ışık, gökkuşağının bütün renklerinin karışımıdır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "NASA'ya göre Isaac Newton bunu 1665'te bir deneyle gösterdi: cam bir prizma ışığı büker ve renklerine ayırır.",
        "spoken": "Nasa'ya göre Ayzek Nivtın bunu bin altı yüz altmış beşte bir deneyle gösterdi: cam bir prizma ışığı büker ve renklerine ayırır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l10",
        "display": "Her rengin dalga boyu farklıdır. Kırmızının dalga boyu en uzun, morunki en kısadır.",
        "spoken": "Her rengin dalga boyu farklıdır. Kırmızının dalga boyu en uzun, morunki en kısadır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Benim en sevdiğim renk mi? Şarj göstergemdeki yeşil!",
        "spoken": "Benim en sevdiğim renk mi? Şarj göstergemdeki yeşil!",
        "factIds": []
      },
      {
        "id": "l12",
        "display": "İkinci sır: kırılma. Kraliyet Meteoroloji Derneği'ne göre ışık, havadan daha yoğun bir ortama, örneğin suya girerken yön değiştirir.",
        "spoken": "İkinci sır: kırılma. Kraliyet Meteoroloji Derneği'ne göre ışık, havadan daha yoğun bir ortama, örneğin suya girerken yön değiştirir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Renkler suyun içinde farklı hızlarda ilerler. Bu yüzden her renk biraz farklı bir açıyla kırılır ve renkler birbirinden ayrılır.",
        "spoken": "Renkler suyun içinde farklı hızlarda ilerler. Bu yüzden her renk biraz farklı bir açıyla kırılır ve renkler birbirinden ayrılır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Yani her yağmur damlası minik bir prizma gibi çalışır.",
        "spoken": "Yani her yağmur damlası minik bir prizma gibi çalışır.",
        "factIds": [
          "f6",
          "f7"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l15",
        "display": "Şimdi tek bir damlayı izleyelim. Birinci adım: ışık damlaya girer ve kırılır.",
        "spoken": "Şimdi tek bir damlayı izleyelim. Birinci adım: ışık damlaya girer ve kırılır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "İkinci adım: damlanın arka yüzeyinden yansır. Tıpkı bir aynadan döner gibi.",
        "spoken": "İkinci adım: damlanın arka yüzeyinden yansır. Tıpkı bir aynadan döner gibi.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Üçüncü adım: damladan çıkarken bir kez daha kırılır. Artık renkler ayrılmıştır.",
        "spoken": "Üçüncü adım: damladan çıkarken bir kez daha kırılır. Artık renkler ayrılmıştır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Gökkuşağını görmek için iki koşul gerekir: Güneş arkanda olmalı, su damlacıkları ise önünde.",
        "spoken": "Gökkuşağını görmek için iki koşul gerekir: Güneş arkanda olmalı, su damlacıkları ise önünde.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Işık, damlalardan gözüne belirli bir açıyla döner: 42 derece.",
        "spoken": "Işık, damlalardan gözüne belirli bir açıyla döner: kırk iki derece.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Bu açıyı tutturan damlalar bir çemberin üzerinde dizilir. Çemberin merkezi, Güneş'in tam karşısındaki hayali noktadır. Adı: antisolar nokta.",
        "spoken": "Bu açıyı tutturan damlalar bir çemberin üzerinde dizilir. Çemberin merkezi, Güneş'in tam karşısındaki hayali noktadır. Adı: antisolar nokta.",
        "factIds": [
          "f9",
          "f10"
        ]
      },
      {
        "id": "l21",
        "display": "Evet, gökkuşağı aslında tam bir çemberdir! Yerdeyken yalnızca ufkun üstündeki kısmını görürüz. Uçaktakiler ise bazen çemberin tamamını görebilir.",
        "spoken": "Evet, gökkuşağı aslında tam bir çemberdir! Yerdeyken yalnızca ufkun üstündeki kısmını görürüz. Uçaktakiler ise bazen çemberin tamamını görebilir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Güneş ne kadar alçaktaysa yayın o kadar büyük bölümü görünür.",
        "spoken": "Güneş ne kadar alçaktaysa yayın o kadar büyük bölümü görünür.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l23",
        "display": "Bu yüzden gökkuşağının ucunda hazine arama. Çemberin ucu olmaz! Ben denedim, hâlâ dönüyorum.",
        "spoken": "Bu yüzden gökkuşağının ucunda hazine arama. Çemberin ucu olmaz! Ben denedim, hâlâ dönüyorum.",
        "factIds": [
          "f17"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l24",
        "display": "Renklerin sırası hep aynıdır: kırmızı yayın dışında, mor içindedir. Arada turuncu, sarı, yeşil, mavi ve çivit mavisi yer alır.",
        "spoken": "Renklerin sırası hep aynıdır: kırmızı yayın dışında, mor içindedir. Arada turuncu, sarı, yeşil, mavi ve çivit mavisi yer alır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l25",
        "display": "Ama keskin sınırlar yoktur: renkler kenarlarında üst üste biner. Hatta birçok bilim insanına göre çivit mavisi, maviden ayırt edilemeyecek kadar yakındır.",
        "spoken": "Ama keskin sınırlar yoktur: renkler kenarlarında üst üste biner. Hatta birçok bilim insanına göre çivit mavisi, maviden ayırt edilemeyecek kadar yakındır.",
        "factIds": [
          "f12",
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Bazen ilk yayın üstünde daha soluk, ikinci bir yay belirir. Buna çift gökkuşağı denir.",
        "spoken": "Bazen ilk yayın üstünde daha soluk, ikinci bir yay belirir. Buna çift gökkuşağı denir.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l27",
        "display": "Nedeni, ışığın damlanın içinde iki kez yansımasıdır. İkinci yayda renkler ters dizilir: kırmızı içte, mor dıştadır.",
        "spoken": "Nedeni, ışığın damlanın içinde iki kez yansımasıdır. İkinci yayda renkler ters dizilir: kırmızı içte, mor dıştadır.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l28",
        "display": "Gökkuşağı için yağmur şart değil: sis, deniz serpintisi ve şelale çevresinde de görülebilir. Ay ışığıyla oluşanına ay gökkuşağı denir.",
        "spoken": "Gökkuşağı için yağmur şart değil: sis, deniz serpintisi ve şelale çevresinde de görülebilir. Ay ışığıyla oluşanına ay gökkuşağı denir.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l29",
        "display": "En şaşırtıcısı şu: gökkuşağı, gökyüzünde belirli bir yerde durmaz. O bir optik yanılsamadır.",
        "spoken": "En şaşırtıcısı şu: gökkuşağı, gökyüzünde belirli bir yerde durmaz. O bir optik yanılsamadır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l30",
        "display": "Bu yüzden kimse aynı gökkuşağını görmez. Herkesin antisolar noktası farklıdır; yanındaki arkadaşın kendi gökkuşağına bakar.",
        "spoken": "Bu yüzden kimse aynı gökkuşağını görmez. Herkesin antisolar noktası farklıdır; yanındaki arkadaşın kendi gökkuşağına bakar.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l31",
        "display": "Yani gökkuşağı paylaşılmaz. Ama merak etme, herkese bir tane düşüyor!",
        "spoken": "Yani gökkuşağı paylaşılmaz. Ama merak etme, herkese bir tane düşüyor!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Güneşli bir günde sırtını Güneş'e dön ve bahçe hortumuyla önüne ince ince su püskürt.",
        "spoken": "Şimdi sıra sende! Güneşli bir günde sırtını Güneş'e dön ve bahçe hortumuyla önüne ince ince su püskürt.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l33",
        "display": "Damlacıkların içinde kendi gökkuşağını ara. Renklerin sırasını kontrol et: kırmızı dışta mı?",
        "spoken": "Damlacıkların içinde kendi gökkuşağını ara. Renklerin sırasını kontrol et: kırmızı dışta mı?",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l34",
        "display": "Bir uyarı: Güneş'e asla doğrudan bakma. Zaten gökkuşağı için ona sırtını dönmen gerekiyor!",
        "spoken": "Bir uyarı: Güneş'e asla doğrudan bakma. Zaten gökkuşağı için ona sırtını dönmen gerekiyor!",
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
        "id": "l35",
        "display": "Bunu biliyor muydun? İnsan gözü, ışığın yalnızca belirli dalga boylarını algılayabilir. Gökkuşağının renkleri, işte o görebildiğimiz ışıktır.",
        "spoken": "Bunu biliyor muydun? İnsan gözü, ışığın yalnızca belirli dalga boylarını algılayabilir. Gökkuşağının renkleri, işte o görebildiğimiz ışıktır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l36",
        "display": "Hızlı soru! Gökkuşağını görmek için Güneş nerede olmalı: önünde mi, arkanda mı?",
        "spoken": "Hızlı soru! Gökkuşağını görmek için Güneş nerede olmalı: önünde mi, arkanda mı?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l37",
        "display": "Düşün bakalım... Evet: arkanda!",
        "spoken": "Düşün bakalım... Evet: arkanda!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l38",
        "display": "Hortumu sen tut ama. Ben ıslanırsam gökkuşağı değil, kıvılcım görürüz!",
        "spoken": "Hortumu sen tut ama. Ben ıslanırsam gökkuşağı değil, kıvılcım görürüz!",
        "factIds": []
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben de gidip bir güzel kurulanayım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de gidip bir güzel kurulanayım!",
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
    "statement": "Gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Gökkuşağı bir optik yanılsamadır; gökyüzünde belirli bir noktada gerçekten bulunmaz.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Beyaz ışık, gökkuşağının bütün renklerinin karışımını gözümüzün algılama biçimidir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Kırmızı, görünür ışığın en uzun dalga boyuna; mor en kısa dalga boyuna sahiptir. İnsan gözü ışığın yalnızca belirli dalga boylarını algılar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Kırılma, Güneş ışığının havadan daha yoğun bir ortamdan geçerken yön değiştirmesidir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Güneş ışığının renkleri bir ortamda farklı hızlarda ilerler; her renk dalga boyuna göre biraz farklı açıyla kırılır. Isaac Newton 1665'te prizmanın görünür ışığı büktüğünü gösterdi.",
    "numbers": [
      "1665"
    ]
  },
  {
    "id": "f7",
    "statement": "Damlaya giren ışık kırılır, damlanın arkasından yansır ve çıkarken yeniden kırılır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Güneş genellikle gökkuşağını gören kişinin arkasındadır; su damlacıkları gözlemcinin önünde olmalıdır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Güneş ışığı izleyicinin önündeki damlalara belirli bir açıyla (42 derece) çarpar; birincil gökkuşağının merkezi, Güneş'in tam karşısındaki hayali antisolar noktadır.",
    "numbers": [
      "42"
    ]
  },
  {
    "id": "f10",
    "statement": "Gökkuşakları aslında tam çemberdir; yerdekiler yalnızca ufkun üstündeki damlalardan gelen ışığı görür; uçaktakiler bazen çemberin tamamını görebilir.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Güneş gökyüzünde ne kadar alçaksa gözlemci yayın o kadar büyük bölümünü görür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Renkler kırmızı, turuncu, sarı, yeşil, mavi, çivit mavisi ve mordur; kırmızı yayın dış kısmında, mor iç kısmında görünür. Birçok bilim insanına göre çivit mavisi maviye ayırt edilemeyecek kadar yakındır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Gökkuşağının renkleri kenarlarında üst üste biner.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Bazen birincil yayın üstünde soluk, ikincil bir gökkuşağı belirir; nedeni ışığın damlada iki kez yansımasıdır; bu yayda kırmızı içte, mor dıştadır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Gökkuşağı sis, deniz serpintisi ya da şelale çevresinde de görülebilir; ay gökkuşağı Ay'ın yansıttığı ışıkla oluşur.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Kimse aynı gökkuşağını görmez: her insanın antisolar noktası ve ufku farklıdır.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Gökkuşaklarının 'ucu' yoktur, çünkü çemberdirler.",
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
