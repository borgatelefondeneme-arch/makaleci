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
        "display": "Başına düşen bir yağmur damlası, kısa süre önce bir okyanusun yüzeyinde olabilirdi!",
        "spoken": "Başına düşen bir yağmur damlası, kısa süre önce bir okyanusun yüzeyinde olabilirdi!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l2",
        "display": "Su gökyüzüne nasıl çıkıyor? Ve bulut düşmezken yağmur neden düşüyor?",
        "spoken": "Su gökyüzüne nasıl çıkıyor? Ve bulut düşmezken yağmur neden düşüyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir su damlasının peşine takılıyoruz!",
        "spoken": "Bugün bir su damlasının peşine takılıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Su gökyüzüne nasıl çıkar? Bulut nasıl oluşur? Ve yağmur damlası nasıl düşer?",
        "spoken": "Üç sorumuz var. Su gökyüzüne nasıl çıkar? Bulut nasıl oluşur? Ve yağmur damlası nasıl düşer?",
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
        "display": "ABD Jeoloji Araştırmaları Kurumu USGS'ye göre su hiçbir zaman yerinde durmaz. Suyun Dünya'daki bu bitmeyen yolculuğuna su döngüsü denir.",
        "spoken": "A Be De Jeoloji Araştırmaları Kurumu, Yu Es Ci Es'e göre su hiçbir zaman yerinde durmaz. Suyun Dünya'daki bu bitmeyen yolculuğuna su döngüsü denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bu yolculuğun iki motoru var: Güneş'in enerjisi ve kütle çekimi.",
        "spoken": "Bu yolculuğun iki motoru var: Güneş'in enerjisi ve kütle çekimi.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "İlk adım buharlaşma: sıvı su, su buharı denen gaza dönüşür.",
        "spoken": "İlk adım buharlaşma: sıvı su, su buharı denen gaza dönüşür.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Atmosferdeki nemin yaklaşık %90'ı okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir.",
        "spoken": "Atmosferdeki nemin yaklaşık yüzde doksanı okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Gerisinin çoğu bitkilerden gelir: su, yapraklardan buharlaşır. Buna terleme denir.",
        "spoken": "Gerisinin çoğu bitkilerden gelir: su, yapraklardan buharlaşır. Buna terleme denir.",
        "factIds": [
          "f2",
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Buz ve kar da sıvılaşmadan doğrudan buhara dönüşebilir. Bunun adı süblimleşme.",
        "spoken": "Buz ve kar da sıvılaşmadan doğrudan buhara dönüşebilir. Bunun adı süblimleşme.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l12",
        "display": "İkinci adım yoğuşma. Su buharı taşıyan hava yükselir ve soğur.",
        "spoken": "İkinci adım yoğuşma. Su buharı taşıyan hava yükselir ve soğur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Su buharı, havadaki minik toz, tuz ve duman parçacıklarının üstünde minicik damlacıklara dönüşür. İşte bulut!",
        "spoken": "Su buharı, havadaki minik toz, tuz ve duman parçacıklarının üstünde minicik damlacıklara dönüşür. İşte bulut!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Yani her bulutun içinde biraz toz var. Temizlik robotu kuzenim bunu duymasın!",
        "spoken": "Yani her bulutun içinde biraz toz var. Temizlik robotu kuzenim bunu duymasın!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l15",
        "display": "Peki bulut neden düşmez? USGS'ye göre bir bulut tonlarca ağırlıkta olabilir. Ama onu oluşturan yükselen hava, bulutu havada tutar.",
        "spoken": "Peki bulut neden düşmez? Yu Es Ci Es'e göre bir bulut tonlarca ağırlıkta olabilir. Ama onu oluşturan yükselen hava, bulutu havada tutar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Bulut damlacıkları da yağış olarak düşemeyecek kadar küçüktür.",
        "spoken": "Bulut damlacıkları da yağış olarak düşemeyecek kadar küçüktür.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Yağmur için damlacıkların çarpışıp birleşmesi gerekir. Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir!",
        "spoken": "Yağmur için damlacıkların çarpışıp birleşmesi gerekir. Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l18",
        "display": "Damla yeterince büyüyünce, yükselen havayı yenip düşmeye başlar. Üçüncü adım: yağış.",
        "spoken": "Damla yeterince büyüyünce, yükselen havayı yenip düşmeye başlar. Üçüncü adım: yağış.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Yağış yalnızca yağmur değildir: kar, dolu ve sulu kar da birer yağıştır.",
        "spoken": "Yağış yalnızca yağmur değildir: kar, dolu ve sulu kar da birer yağıştır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Bir sürpriz: yağmur damlası gözyaşı biçiminde değildir! Yarıçapı 1 milimetreden küçük damlalar top gibi yuvarlaktır.",
        "spoken": "Bir sürpriz: yağmur damlası gözyaşı biçiminde değildir! Yarıçapı bir milimetreden küçük damlalar top gibi yuvarlaktır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l21",
        "display": "Çapı 2–3 milimetre olanların ise altı düzleşir; tıpkı bir hamburger ekmeği gibi.",
        "spoken": "Çapı iki üç milimetre olanların ise altı düzleşir; tıpkı bir hamburger ekmeği gibi.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l22",
        "display": "Gökten hamburger ekmeği yağıyor! Buna acıkmayan tek kişi ben olabilirim.",
        "spoken": "Gökten hamburger ekmeği yağıyor! Buna acıkmayan tek kişi ben olabilirim.",
        "factIds": []
      },
      {
        "id": "l23",
        "display": "Yere düşen su ne olur? Bir kısmı nehirlerle akar, bir kısmı toprağa süzülür ve yeraltı suyu olur.",
        "spoken": "Yere düşen su ne olur? Bir kısmı nehirlerle akar, bir kısmı toprağa süzülür ve yeraltı suyu olur.",
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
        "id": "l24",
        "display": "Yeraltı suyu, akifer denen yer altı katmanlarında akar; kaynaklardan, nehirlerden ya da doğrudan okyanusa geri döner.",
        "spoken": "Yeraltı suyu, akifer denen yer altı katmanlarında akar; kaynaklardan, nehirlerden ya da doğrudan okyanusa geri döner.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l25",
        "display": "Sonra her şey yeniden başlar: buharlaşma, yoğuşma, yağış.",
        "spoken": "Sonra her şey yeniden başlar: buharlaşma, yoğuşma, yağış.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l26",
        "display": "Bir su molekülü buharlaştıktan sonra havada yaklaşık 10 gün kalır.",
        "spoken": "Bir su molekülü buharlaştıktan sonra havada yaklaşık on gün kalır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l27",
        "display": "National Geographic'e göre bu döngü yaklaşık 3,8 milyar yıl önce başladı: soğuyan Dünya'ya yağmurlar yağdı ve okyanuslar oluştu.",
        "spoken": "Neşınıl Ciyografik'e göre bu döngü yaklaşık üç virgül sekiz milyar yıl önce başladı: soğuyan Dünya'ya yağmurlar yağdı ve okyanuslar oluştu.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Dünya'daki suyun yaklaşık %97'si okyanuslardadır. Tatlı su, toplamın yalnızca %2,5'i kadardır.",
        "spoken": "Dünya'daki suyun yaklaşık yüzde doksan yedisi okyanuslardadır. Tatlı su, toplamın yalnızca yüzde iki buçuğu kadardır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l29",
        "display": "Üstelik tatlı suyun yaklaşık %68'i donmuş hâldedir; yaklaşık %30'u da yer altındadır.",
        "spoken": "Üstelik tatlı suyun yaklaşık yüzde altmış sekizi donmuş hâldedir; yaklaşık yüzde otuzu da yer altındadır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l30",
        "display": "NOAA'ya göre su yaşam için vazgeçilmezdir; ama döngünün her aşamasında insanların kullanımına uygun değildir. Bu yüzden suyu boşa harcamamak gerekir.",
        "spoken": "Noa'ya göre su yaşam için vazgeçilmezdir; ama döngünün her aşamasında insanların kullanımına uygun değildir. Bu yüzden suyu boşa harcamamak gerekir.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l31",
        "display": "Ben bu konuda örnek bir vatandaşım: yıkanmam, silinirim!",
        "spoken": "Ben bu konuda örnek bir vatandaşım: yıkanmam, silinirim!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Bir kâseye biraz ılık su koy, üstünü streç filmle kapat ve güneşli bir pencerenin önüne bırak.",
        "spoken": "Şimdi sıra sende! Bir kâseye biraz ılık su koy, üstünü streç filmle kapat ve güneşli bir pencerenin önüne bırak.",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Bir süre sonra filmin altında damlacıklar görürsün: buharlaşma ve yoğuşma, kâsenin içinde!",
        "spoken": "Bir süre sonra filmin altında damlacıklar görürsün: buharlaşma ve yoğuşma, kâsenin içinde!",
        "factIds": [
          "f2",
          "f4"
        ]
      },
      {
        "id": "l34",
        "display": "Sıcak su kullanmak istersen mutlaka bir büyüğünden yardım iste.",
        "spoken": "Sıcak su kullanmak istersen mutlaka bir büyüğünden yardım iste.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l35",
        "display": "Bunu biliyor muydun? Atmosferde su buharı olarak bulunan su, Dünya'daki bütün suyun yalnızca %0,001'i kadardır.",
        "spoken": "Bunu biliyor muydun? Atmosferde su buharı olarak bulunan su, Dünya'daki bütün suyun yalnızca yüz binde biri kadardır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l36",
        "display": "Hızlı soru! Su buharının soğuyup minik damlacıklara dönüşmesine ne denir?",
        "spoken": "Hızlı soru! Su buharının soğuyup minik damlacıklara dönüşmesine ne denir?",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l37",
        "display": "Düşün bakalım... Evet: yoğuşma!",
        "spoken": "Düşün bakalım... Evet: yoğuşma!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l38",
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
        "id": "l39",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l40",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l41",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de şemsiyemi alıp gidiyorum; ıslanmak bana göre değil!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de şemsiyemi alıp gidiyorum; ıslanmak bana göre değil!",
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
    "statement": "Su döngüsü, suyun Dünya'da nerede olduğunu ve nasıl hareket ettiğini anlatır; su hiçbir zaman yerinde durmaz; suyun sürekli hareketini Güneş'in enerjisi ve kütle çekimi sağlar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Buharlaşma, sıvı suyu gaz hâlindeki suya (su buharına) çeviren süreçtir. Atmosferdeki nemin çoğu (yaklaşık %90) okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir; gerisi bitki terlemesinden ve çok az miktarda süblimleşmeden gelir.",
    "numbers": [
      "90"
    ]
  },
  {
    "id": "f3",
    "statement": "Terleme: sıvı su bitkilerin yapraklarından buharlaşır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Bulutlar, su buharı içeren hava yükselip soğuduğu için oluşur; su molekülleri havadaki minik toz, tuz ve duman parçacıklarıyla birleşir. Yoğuşma bulutların oluşumundan sorumludur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bulut damlacıkları yağış olarak düşemeyecek kadar küçüktür ama görünür bulutlar oluşturacak kadar büyüktür; bulutu oluşturan yükselen hava onu havada tutar; bir bulut tonlarca ağırlıkta olsa da düşmez.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir; yeterince çarpışma olur ve damlanın düşme hızı bulutun yükselen hava hızını aşarsa damla düşer.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Yarıçapı 1 milimetreden küçük yağmur damlaları top gibi küreseldir; yaklaşık 2–3 milimetre çapta alt kısım oldukça düzdür: hamburger ekmeği gibi.",
    "numbers": [
      "1",
      "2",
      "3"
    ]
  },
  {
    "id": "f8",
    "statement": "Yağış, bulutlardan yağmur, donan yağmur, sulu kar, kar ya da dolu biçiminde bırakılan sudur.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Su, süzülme ve yeraltı suyu beslenmesiyle toprağa girer; yeraltı suyu akiferlerde akar; nehirlere, okyanusa ve kaynaklara boşalarak yüzeye dönebilir. Suyun bir kısmı toprağa sızar ve yeraltı suyu olarak tutulur.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Buharlaşan bir su molekülü havada yaklaşık 10 gün kalır.",
    "numbers": [
      "10"
    ]
  },
  {
    "id": "f11",
    "statement": "Okyanuslar Dünya'daki suyun yaklaşık %97'sini tutar; tatlı su Dünya'daki suyun %2,5'idir; tatlı suyun yaklaşık %68'i donmuş hâldedir; yaklaşık %30'u yer altındadır.",
    "numbers": [
      "97",
      "2.5",
      "68",
      "30"
    ]
  },
  {
    "id": "f12",
    "statement": "Dünya'daki suyun çok küçük bir bölümü, yalnızca %0,001'i, atmosferde su buharı olarak bulunur.",
    "numbers": [
      "0.001"
    ]
  },
  {
    "id": "f13",
    "statement": "Dünya'nın su döngüsü yaklaşık 3,8 milyar yıl önce, soğuyan Dünya'ya yağmur yağıp okyanuslar oluştuğunda başladı.",
    "numbers": [
      "3.8"
    ]
  },
  {
    "id": "f14",
    "statement": "Su Dünya'daki yaşam için vazgeçilmezdir; su, döngünün her bölümünde insanların kullanımına uygun değildir.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Süblimleşmede buz ya da kar gibi katı su, sıvılaşmadan doğrudan su buharına dönüşebilir.",
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
