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
        "display": "Şu an ellerinde, gözle göremeyeceğin kadar küçük canlılar var. Bazıları dost, bazıları düşman!",
        "spoken": "Şu an ellerinde, gözle göremeyeceğin kadar küçük canlılar var. Bazıları dost, bazıları düşman!",
        "factIds": [
          "f1",
          "f2"
        ]
      },
      {
        "id": "l2",
        "display": "Bu küçük canlılar kim? Ve vücudun düşmanları nasıl tanıyıp yeniyor?",
        "spoken": "Bu küçük canlılar kim? Ve vücudun düşmanları nasıl tanıyıp yeniyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün mikroskobun altına bakıyoruz!",
        "spoken": "Bugün mikroskobun altına bakıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Mikrop nedir? Vücudumuz kendini nasıl savunur? Ve mikroplardan nasıl korunuruz?",
        "spoken": "Üç sorumuz var. Mikrop nedir? Vücudumuz kendini nasıl savunur? Ve mikroplardan nasıl korunuruz?",
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
        "display": "KidsHealth'e göre mikrop dediğimiz şey; bakteriler, virüsler, mantarlar ve protozoalar gibi mikroskobik canlılardır.",
        "spoken": "Kids Helt'e göre mikrop dediğimiz şey; bakteriler, virüsler, mantarlar ve protozoalar gibi mikroskobik canlılardır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "İyi haber: CDC'ye göre mikropların çoğu zararsızdır, hatta işimize yarar. Hastalık yapanlara patojen denir.",
        "spoken": "İyi haber: Si Di Si'ye göre mikropların çoğu zararsızdır, hatta işimize yarar. Hastalık yapanlara patojen denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Bakterilerle başlayalım. Bakteriler tek hücreli, minicik canlılardır. Küre, çubuk ya da sarmal biçiminde olabilirler.",
        "spoken": "Bakterilerle başlayalım. Bakteriler tek hücreli, minicik canlılardır. Küre, çubuk ya da sarmal biçiminde olabilirler.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l9",
        "display": "Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre vücudumuzda, kendi hücrelerimizden daha çok bakteri hücresi olduğu tahmin ediliyor!",
        "spoken": "Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'ye göre vücudumuzda, kendi hücrelerimizden daha çok bakteri hücresi olduğu tahmin ediliyor!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Yani sen hiçbir zaman yalnız değilsin. Ben de değilim: içimde bir sürü kablo var!",
        "spoken": "Yani sen hiçbir zaman yalnız değilsin. Ben de değilim: içimde bir sürü kablo var!",
        "factIds": []
      },
      {
        "id": "l11",
        "display": "Bu bakterilerin çoğu zararsızdır. Bağırsağımızdakiler ise vücudumuzun normal çalışması için gereklidir. Yalnızca az sayıda tür hastalık yapar.",
        "spoken": "Bu bakterilerin çoğu zararsızdır. Bağırsağımızdakiler ise vücudumuzun normal çalışması için gereklidir. Yalnızca az sayıda tür hastalık yapar.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Virüsler ise çok farklıdır. Bir protein kılıfın içinde, DNA ya da RNA denen genetik bilgiden oluşurlar.",
        "spoken": "Virüsler ise çok farklıdır. Bir protein kılıfın içinde, DNA ya da RNA denen genetik bilgiden oluşurlar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Virüsler tek başına çoğalamaz. Bir hücreye girer, o hücrenin parçalarını kullanarak kendini kopyalar ve çoğu zaman hücreye zarar verir.",
        "spoken": "Virüsler tek başına çoğalamaz. Bir hücreye girer, o hücrenin parçalarını kullanarak kendini kopyalar ve çoğu zaman hücreye zarar verir.",
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
        "id": "l14",
        "display": "Mikroplar nasıl yayılır? Çoğu, hapşırık ve öksürükle havaya karışır ya da tükürük gibi vücut sıvılarıyla geçer.",
        "spoken": "Mikroplar nasıl yayılır? Çoğu, hapşırık ve öksürükle havaya karışır ya da tükürük gibi vücut sıvılarıyla geçer.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Yıkanmamış ellerle gözüne, burnuna, ağzına dokunmak da onlara kapı açar.",
        "spoken": "Yıkanmamış ellerle gözüne, burnuna, ağzına dokunmak da onlara kapı açar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Ama vücudun güçlü bir ordusu var: bağışıklık sistemi. İlk kalesi derindir; mikropların içeri girmesini engeller.",
        "spoken": "Ama vücudun güçlü bir ordusu var: bağışıklık sistemi. İlk kalesi derindir; mikropların içeri girmesini engeller.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Mikrop yine de içeri sızarsa akyuvarlar devreye girer. Fagosit denen akyuvarlar, istilacıları adeta yutar.",
        "spoken": "Mikrop yine de içeri sızarsa akyuvarlar devreye girer. Fagosit denen akyuvarlar, istilacıları adeta yutar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Lenfositler ise düşmanı hatırlamaya ve yok etmeye yardım eder. T hücreleri birer asker gibidir.",
        "spoken": "Lenfositler ise düşmanı hatırlamaya ve yok etmeye yardım eder. T hücreleri birer asker gibidir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "B hücreleri antikor denen özel proteinler üretir. Antikorlar, aynı mikropla yeniden karşılaşırsak diye vücutta kalır.",
        "spoken": "B hücreleri antikor denen özel proteinler üretir. Antikorlar, aynı mikropla yeniden karşılaşırsak diye vücutta kalır.",
        "factIds": [
          "f8",
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.",
        "spoken": "Bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Vücudunun bir hafıza kartı var. Benimki ise bazen dolup taşıyor!",
        "spoken": "Vücudunun bir hafıza kartı var. Benimki ise bazen dolup taşıyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l22",
        "display": "Aşılar da bu hafızadan yararlanır. Aşı, mikrobun ölü ya da zayıflatılmış hâlini ya da bir parçasını içerir.",
        "spoken": "Aşılar da bu hafızadan yararlanır. Aşı, mikrobun ölü ya da zayıflatılmış hâlini ya da bir parçasını içerir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar üretir. Böylece asıl mikrop geldiğinde hazırdır.",
        "spoken": "Bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar üretir. Böylece asıl mikrop geldiğinde hazırdır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Peki antibiyotik? CDC'ye göre antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez.",
        "spoken": "Peki antibiyotik? Si Di Si'ye göre antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Üstelik bazı mikroplar zamanla onları öldürmek için yapılan ilaçları yenmeyi öğrenebilir. Buna antimikrobiyal direnç denir. Dirençli olan vücudumuz değil, mikroptur.",
        "spoken": "Üstelik bazı mikroplar zamanla onları öldürmek için yapılan ilaçları yenmeyi öğrenebilir. Buna antimikrobiyal direnç denir. Dirençli olan vücudumuz değil, mikroptur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "En güçlü silahımız ise çok basit: sabun ve su! CDC'ye göre çoğu durumda mikroplardan kurtulmanın en iyi yolu budur.",
        "spoken": "En güçlü silahımız ise çok basit: sabun ve su! Si Di Si'ye göre çoğu durumda mikroplardan kurtulmanın en iyi yolu budur.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Ellerini ıslat, sabunla köpürt ve en az 20 saniye ov. Süreyi tutturmak için Doğum Günü şarkısını baştan sona iki kez söyleyebilirsin.",
        "spoken": "Ellerini ıslat, sabunla köpürt ve en az yirmi saniye ov. Süreyi tutturmak için Doğum Günü şarkısını baştan sona iki kez söyleyebilirsin.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Sonra temiz suyla durula ve temiz bir havluyla kurula.",
        "spoken": "Sonra temiz suyla durula ve temiz bir havluyla kurula.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l29",
        "display": "Ne zaman? Tuvaletten sonra, yemekten önce, burnunu sildikten, öksürdükten ya da hapşırdıktan sonra.",
        "spoken": "Ne zaman? Tuvaletten sonra, yemekten önce, burnunu sildikten, öksürdükten ya da hapşırdıktan sonra.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l30",
        "display": "Hapşırırken mendil kullan ve mendili at. Mendil yoksa eline değil, dirseğine hapşır!",
        "spoken": "Hapşırırken mendil kullan ve mendili at. Mendil yoksa eline değil, dirseğine hapşır!",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l31",
        "display": "Ben dirseğime hapşıramam. Ama vidalarım gıcırdayınca dirseğimi kapatıyorum!",
        "spoken": "Ben dirseğime hapşıramam. Ama vidalarım gıcırdayınca dirseğimi kapatıyorum!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Şimdi sıra sende! Bir aile büyüğünle birlikte el yıkama dedektifliği yap: bir hafta boyunca evde elleri ne zaman yıkadığınızı bir tabloya not edin.",
        "spoken": "Şimdi sıra sende! Bir aile büyüğünle birlikte el yıkama dedektifliği yap: bir hafta boyunca evde elleri ne zaman yıkadığınızı bir tabloya not edin.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l33",
        "display": "Hafta sonunda bakın: hangi durumlarda yıkamayı unutmuşsunuz?",
        "spoken": "Hafta sonunda bakın: hangi durumlarda yıkamayı unutmuşsunuz?",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l34",
        "display": "Bunu biliyor muydun? El yıkamak, solunum yolu ve ishal enfeksiyonlarının yayılmasını önlemeye yardım edebilir.",
        "spoken": "Bunu biliyor muydun? El yıkamak, solunum yolu ve ishal enfeksiyonlarının yayılmasını önlemeye yardım edebilir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l35",
        "display": "Hızlı soru! Antibiyotikler virüslere etki eder mi?",
        "spoken": "Hızlı soru! Antibiyotikler virüslere etki eder mi?",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l36",
        "display": "Düşün bakalım... Hayır! Antibiyotikler virüslere etki etmez.",
        "spoken": "Düşün bakalım... Hayır! Antibiyotikler virüslere etki etmez.",
        "factIds": [
          "f11"
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
        "display": "Abone olmayı ve zili açmayı unutma. Şimdi ellerini yıkamaya!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Şimdi ellerini yıkamaya!",
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
    "statement": "'Mikrop' sözcüğü hastalığa yol açabilen mikroskobik bakterileri, virüsleri, mantarları ve protozoaları anlatır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Mikropların çoğu zararsızdır, hatta insanlara yararlıdır; enfeksiyona yol açanlara patojen denir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Bakteriler küçük, tek hücreli canlılardır; insan vücudu bakteriyle doludur ve insan hücresinden daha çok bakteri hücresi içerdiği tahmin edilir; vücuttaki bakterilerin çoğu zararsız, bazıları yararlıdır; görece az sayıda tür hastalık yapar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Bakteriler küre, çubuk ya da sarmal biçiminde olabilir; sindirim sistemimizdeki bakteriler vücudumuzun normal çalışması için gereklidir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Virüs, bir protein kılıfla çevrili bir nükleik asit (DNA ya da RNA) parçasından oluşan bulaşıcı bir mikroptur; tek başına çoğalamaz, hücreleri enfekte edip konak hücrenin parçalarıyla kendini kopyalar; çoğu zaman bu sırada konak hücreyi öldürür.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Mikropların çoğu hapşırık ve öksürükle havadan ya da ter ve tükürük gibi vücut sıvılarıyla yayılır; yıkanmamış ellerle göze, buruna ve ağza dokunmak, ellere hapşırıp başkalarının ellerine ya da ortak eşyalara dokunmak mikropları yayar.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Bağışıklık sistemi vücudun enfeksiyonlara karşı savunmasıdır; deri, mikropların vücuda girmesini engelleyen bir engel görevi görür.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Akyuvarlar (lökositler) bağışıklıkta önemli rol oynar: fagositler istilacı canlıları yer; lenfositler vücudun istilacıları hatırlamasına ve yok etmesine yardım eder; T hücreleri asker gibidir; B lenfositleri antikor yapar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Antikorlar yapıldıktan sonra aynı mikropla yeniden savaşmak gerekirse diye genellikle vücutta kalır; bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Aşılar hastalığa yol açan mikrobun ölü ya da zayıflatılmış hâlini (ya da parçalarını) içerir; bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar yapar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez; antimikrobiyal direnç, mikropların kendilerini öldürmek için tasarlanan ilaçları yenme yeteneği kazanmasıdır; bu, vücudun antibiyotiğe dirençli olduğu anlamına gelmez.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Elleri temiz akan suyla ıslat, sabunla köpürt, en az 20 saniye ov (Doğum Günü şarkısını baştan sona iki kez), temiz suyla durula ve temiz havluyla kurula. Çoğu durumda mikroplardan kurtulmanın en iyi yolu sabun ve suyla yıkamaktır.",
    "numbers": [
      "20"
    ]
  },
  {
    "id": "f13",
    "statement": "Burnu sildikten, öksürdükten ya da hapşırdıktan sonra, yemek hazırlamadan önce ve sonra, tuvaletten sonra eller yıkanmalıdır; el yıkamak solunum ve ishal enfeksiyonlarının yayılmasını önleyebilir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Hapşırırken ya da öksürürken ağzını ve burnunu mendille kapat ve mendili at; mendil yoksa eline değil dirseğine hapşır.",
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
