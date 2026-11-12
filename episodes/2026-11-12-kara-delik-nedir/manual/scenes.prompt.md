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
        "display": "Uzayda öyle bir yer düşün ki, içine giren hiçbir şey geri çıkamıyor. Işık bile!",
        "spoken": "Uzayda öyle bir yer düşün ki, içine giren hiçbir şey geri çıkamıyor. Işık bile!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Bu nasıl mümkün olabilir? Ve göremediğimiz bir şeyi bilim insanları nasıl buluyor?",
        "spoken": "Bu nasıl mümkün olabilir? Ve göremediğimiz bir şeyi bilim insanları nasıl buluyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir kara deliğe yaklaşıyoruz. Güvenli mesafeden tabii!",
        "spoken": "Bugün bir kara deliğe yaklaşıyoruz. Güvenli mesafeden tabii!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Ben fazla yaklaşmayacağım. Şarj kablom o kadar uzun değil!",
        "spoken": "Ben fazla yaklaşmayacağım. Şarj kablom o kadar uzun değil!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Kara delik nedir? Nasıl oluşur? Ve görünmez bir şey nasıl keşfedilir?",
        "spoken": "Üç sorumuz var. Kara delik nedir? Nasıl oluşur? Ve görünmez bir şey nasıl keşfedilir?",
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
        "display": "NASA'ya göre kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir.",
        "spoken": "Nasa'ya göre kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Adı seni yanıltmasın: kara delikler aslında delik değildir. Tam tersine, çok küçük bir alana sıkışmış dev miktarda maddedir.",
        "spoken": "Adı seni yanıltmasın: kara delikler aslında delik değildir. Tam tersine, çok küçük bir alana sıkışmış dev miktarda maddedir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Kütle çekimi neden bu kadar güçlü? Çünkü madde küçücük bir alana sıkışmıştır.",
        "spoken": "Kütle çekimi neden bu kadar güçlü? Çünkü madde küçücük bir alana sıkışmıştır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l10",
        "display": "Peki nasıl oluşur? Her şey çok büyük kütleli bir yıldızla başlar. Yıldızın merkezi kendi üzerine çöker.",
        "spoken": "Peki nasıl oluşur? Her şey çok büyük kütleli bir yıldızla başlar. Yıldızın merkezi kendi üzerine çöker.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l11",
        "display": "Yıldız, süpernova denen dev bir patlamayla dağılır.",
        "spoken": "Yıldız, süpernova denen dev bir patlamayla dağılır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Yıldızın kütlesi Güneş'inkinin yaklaşık 20 katı ya da daha fazlaysa, çöken merkez bir kara deliğe dönüşür.",
        "spoken": "Yıldızın kütlesi Güneş'inkinin yaklaşık yirmi katı ya da daha fazlaysa, çöken merkez bir kara deliğe dönüşür.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Güneş'imiz için endişelenme: onun kütlesi kara delik olmaya yetmez.",
        "spoken": "Güneş'imiz için endişelenme: onun kütlesi kara delik olmaya yetmez.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Oh! Güneş enerjisiyle şarj olan arkadaşlarım adına sevindim.",
        "spoken": "Oh! Güneş enerjisiyle şarj olan arkadaşlarım adına sevindim.",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l15",
        "display": "Şimdi bir kara deliğin bölümlerine bakalım. En önemli sınır olay ufkudur. Onu kara deliğin yüzeyi gibi düşünebilirsin.",
        "spoken": "Şimdi bir kara deliğin bölümlerine bakalım. En önemli sınır olay ufkudur. Onu kara deliğin yüzeyi gibi düşünebilirsin.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Olay ufkunu geçen hiçbir şey geri dönemez. Çünkü oradan kaçmak için gereken hız, ışık hızından büyüktür ve hiçbir şey ışıktan hızlı gidemez.",
        "spoken": "Olay ufkunu geçen hiçbir şey geri dönemez. Çünkü oradan kaçmak için gereken hız, ışık hızından büyüktür ve hiçbir şey ışıktan hızlı gidemez.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Tam merkezde tekillik bulunur: maddenin sonsuz yoğunluğa kadar ezildiği nokta.",
        "spoken": "Tam merkezde tekillik bulunur: maddenin sonsuz yoğunluğa kadar ezildiği nokta.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l18",
        "display": "Kara deliğin çevresindeki gaz, birikim diski denen bir yapı oluşturur. Kara delikten gelen ışığın ana kaynağı bu disktir.",
        "spoken": "Kara deliğin çevresindeki gaz, birikim diski denen bir yapı oluşturur. Kara delikten gelen ışığın ana kaynağı bu disktir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "Gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışınları yayar.",
        "spoken": "Gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışınları yayar.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l20",
        "display": "Bazı kara deliklerden zıt yönlere fışkıran bir çift jet de çıkar.",
        "spoken": "Bazı kara deliklerden zıt yönlere fışkıran bir çift jet de çıkar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Kara delikler kütlelerine göre üç gruba ayrılır. Yıldız kütleli olanlar, Güneş'in birkaç katından yüzlerce katına kadar kütle taşır.",
        "spoken": "Kara delikler kütlelerine göre üç gruba ayrılır. Yıldız kütleli olanlar, Güneş'in birkaç katından yüzlerce katına kadar kütle taşır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Süper kütleli kara delikler ise Güneş'in yüz binlerce katından milyarlarca katına kadar kütlelidir. Aradakilere orta kütleli denir.",
        "spoken": "Süper kütleli kara delikler ise Güneş'in yüz binlerce katından milyarlarca katına kadar kütlelidir. Aradakilere orta kütleli denir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Bizim gökadamız Samanyolu'nun merkezinde de bir tane var: Sagittarius A*. Kütlesi Güneş'in 4 milyon katı!",
        "spoken": "Bizim gökadamız Samanyolu'nun merkezinde de bir tane var: Sagitaryus A yıldız. Kütlesi Güneş'in dört milyon katı!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Kara deliğe çok yaklaşan maddeye ne olur? Yatayda sıkışır, dikeyde uzar ve bir erişteye benzer. Bunun gerçek bir bilimsel adı var: spagettileşme!",
        "spoken": "Kara deliğe çok yaklaşan maddeye ne olur? Yatayda sıkışır, dikeyde uzar ve bir erişteye benzer. Bunun gerçek bir bilimsel adı var: spagettileşme!",
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
        "display": "Ben spagetti olmam ama. Olsa olsa tel şehriye!",
        "spoken": "Ben spagetti olmam ama. Olsa olsa tel şehriye!",
        "factIds": []
      },
      {
        "id": "l26",
        "display": "Peki ışık yaymayan bir şeyi nasıl buluruz? Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için neredeyse görünmezdir.",
        "spoken": "Peki ışık yaymayan bir şeyi nasıl buluruz? Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için neredeyse görünmezdir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Ama çevreleri onları ele verir. Güçlü kütle çekimi, yakındaki yıldızların kendine özgü bir biçimde dolanmasına yol açar.",
        "spoken": "Ama çevreleri onları ele verir. Güçlü kütle çekimi, yakındaki yıldızların kendine özgü bir biçimde dolanmasına yol açar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Birikim diskinin yaydığı X ışınları da bir ipucudur.",
        "spoken": "Birikim diskinin yaydığı X ışınları da bir ipucudur.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l29",
        "display": "Kara delikler ayrıca uzay-zamanın dokusunda dalgalanmalar yaratır. Bunlara kütle çekim dalgaları denir.",
        "spoken": "Kara delikler ayrıca uzay-zamanın dokusunda dalgalanmalar yaratır. Bunlara kütle çekim dalgaları denir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l30",
        "display": "2019'da büyük bir an yaşandı: Olay Ufku Teleskobu ile bir kara deliğin görüntüsü elde edildi.",
        "spoken": "İki bin on dokuzda büyük bir an yaşandı: Olay Ufku Teleskobu ile bir kara deliğin görüntüsü elde edildi.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l31",
        "display": "Bu kara delik, M87 adlı gökadanın merkezinde, bizden yaklaşık 55 milyon ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.",
        "spoken": "Bu kara delik, Em seksen yedi adlı gökadanın merkezinde, bizden yaklaşık elli beş milyon ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l32",
        "display": "Şimdi bir yanlış inanışı düzeltelim: kara delikler uzayın elektrik süpürgesi değildir. Çevrelerindeki her şeyi içine çekmezler.",
        "spoken": "Şimdi bir yanlış inanışı düzeltelim: kara delikler uzayın elektrik süpürgesi değildir. Çevrelerindeki her şeyi içine çekmezler.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l33",
        "display": "Yeterince uzaktan bakıldığında kütle çekimleri, aynı kütledeki başka bir cisminkiyle aynıdır.",
        "spoken": "Yeterince uzaktan bakıldığında kütle çekimleri, aynı kütledeki başka bir cisminkiyle aynıdır.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l34",
        "display": "NASA'nın örneği şöyle: Güneş'in yerine aynı kütlede bir kara delik koysaydık Dünya içine düşmezdi. Gezegenler dolanmaya devam ederdi.",
        "spoken": "Nasa'nın örneği şöyle: Güneş'in yerine aynı kütlede bir kara delik koysaydık Dünya içine düşmezdi. Gezegenler dolanmaya devam ederdi.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l35",
        "display": "Üstelik bilinen en yakın kara delik bile yaklaşık 1.500 ışık yılı uzakta. Yani güvendeyiz!",
        "spoken": "Üstelik bilinen en yakın kara delik bile yaklaşık bin beş yüz ışık yılı uzakta. Yani güvendeyiz!",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l36",
        "display": "Şimdi sıra sende! Esnek bir kumaşı gergin tut ve ortasına ağır bir top koy. Sonra kenardan bilyeler yuvarla.",
        "spoken": "Şimdi sıra sende! Esnek bir kumaşı gergin tut ve ortasına ağır bir top koy. Sonra kenardan bilyeler yuvarla.",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "Bilyelerin çukura doğru nasıl kıvrıldığını izle. Bu yalnızca bir model; ama büyük bir kütlenin çevresini nasıl etkilediğini hayal etmene yardım eder.",
        "spoken": "Bilyelerin çukura doğru nasıl kıvrıldığını izle. Bu yalnızca bir model; ama büyük bir kütlenin çevresini nasıl etkilediğini hayal etmene yardım eder.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l38",
        "display": "Bunu biliyor muydun? Gözlenen en büyük kütleli kara deliğin adı TON 618. Kütlesi Güneş'in 66 milyar katı!",
        "spoken": "Bunu biliyor muydun? Gözlenen en büyük kütleli kara deliğin adı Ton altı yüz on sekiz. Kütlesi Güneş'in altmış altı milyar katı!",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l39",
        "display": "Hızlı soru! Güneş bir gün kara deliğe dönüşecek mi?",
        "spoken": "Hızlı soru! Güneş bir gün kara deliğe dönüşecek mi?",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l40",
        "display": "Düşün bakalım... Hayır! Kütlesi buna yetmez.",
        "spoken": "Düşün bakalım... Hayır! Kütlesi buna yetmez.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l41",
        "display": "Ben de dönüşmem. Benim kütlem ancak bir okul çantasını doldurur!",
        "spoken": "Ben de dönüşmem. Benim kütlem ancak bir okul çantasını doldurur!",
        "factIds": []
      },
      {
        "id": "l42",
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
        "id": "l43",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l44",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l45",
        "display": "Abone olmayı ve zili açmayı unutma. Ben güvenli mesafeden uçuyorum; olay ufkuna uzaktan el sallarım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben güvenli mesafeden uçuyorum; olay ufkuna uzaktan el sallarım!",
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
    "statement": "Kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir; güçlü kütle çekimi, maddenin çok küçük bir alana sıkışmasından kaynaklanır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Kara delikler aslında delik değildir; çok küçük alanlara sıkışmış dev madde yoğunlaşmalarıdır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Yıldız kütleli kara delikler, çok büyük kütleli bir yıldızın merkezi kendi üzerine çökünce oluşur; yıldız süpernova olarak patlar; kütlesi Güneş'in yaklaşık 20 katı ya da daha fazlaysa merkez yıldız kütleli bir kara deliğe çöker.",
    "numbers": [
      "20"
    ]
  },
  {
    "id": "f4",
    "statement": "Güneş'in kütlesi kara deliğe çökmeye yetmez.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Olay ufku kara deliğin yüzeyi gibi düşünülebilir; onu geçen her şey, ışık bile, içeride kalmaya mahkûmdur. Bu sınırın içinde kaçış için gereken hız ışık hızını aşar; hiçbir şey ışıktan hızlı gidemez.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kara deliğin tam merkezinde maddenin sonsuz yoğunluğa ezildiği bir nokta (tekillik) vardır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Kara delikten gelen ışığın ana kaynağı birikim diskidir; gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışını yayar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Bazı kara deliklerden zıt yönlere fışkıran bir çift jet çıkar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Kara delikler kütlelerine göre üç gruba ayrılır: yıldız kütleli (Güneş'in birkaç katından yüzlerce katına), orta kütleli ve süper kütleli (Güneş'in yüz binlerce katından milyarlarca katına).",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Bizim gökadamızın merkezindeki süper kütleli kara delik Sagittarius A*'dır; kütlesi Güneş'in 4 milyon katıdır.",
    "numbers": [
      "4"
    ]
  },
  {
    "id": "f11",
    "statement": "Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için fiilen görünmezdir. Süper kütleli bir kara deliğin güçlü kütle çekimi, yıldızların çevresinde belirli bir biçimde dolanmasına yol açabilir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Kara delikler uzay-zamanın dokusunda kütle çekim dalgaları denen dalgalanmalar yaratır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bilim insanları Olay Ufku Teleskobu ile M87 gökadasının merkezindeki kara deliğin görüntüsünü elde etti (2019); Dünya'dan yaklaşık 55 milyon ışık yılı uzaktadır.",
    "numbers": [
      "87",
      "55",
      "2019"
    ]
  },
  {
    "id": "f14",
    "statement": "Spagettileşme, maddenin kara deliğe fazla yaklaşınca başına gelenleri anlatan gerçek bir terimdir: madde yatayda sıkışır, dikeyde uzar ve bir erişteye benzer.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Kara delikler kozmik elektrik süpürgesi değildir; başka maddeleri emmez. Yeterince uzaktan kütle çekim etkileri aynı kütledeki başka cisimlerinkiyle aynıdır.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Güneş'in yerini aynı kütlede bir kara delik alsaydı Dünya içine düşmezdi; gezegenler şimdi Güneş'in çevresinde dolandıkları gibi dolanmayı sürdürürdü.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Bilinen en yakın kara delik (Gaia BH1) yaklaşık 1.500 ışık yılı uzaktadır.",
    "numbers": [
      "1.500",
      "1"
    ]
  },
  {
    "id": "f18",
    "statement": "Gözlenen en büyük kütleli kara delik TON 618'dir: Güneş'in 66 milyar katı kütlededir.",
    "numbers": [
      "618",
      "66"
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
