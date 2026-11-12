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
        "display": "Bir çiçeğin üstünde vızıldayan küçük bir arı. Sence orada ne yapıyor?",
        "spoken": "Bir çiçeğin üstünde vızıldayan küçük bir arı. Sence orada ne yapıyor?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Yalnızca karnını doyurmuyor. Farkında olmadan senin sofrandaki meyvelerin de yolunu açıyor!",
        "spoken": "Yalnızca karnını doyurmuyor. Farkında olmadan senin sofrandaki meyvelerin de yolunu açıyor!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün bir arı kovanının içine giriyoruz!",
        "spoken": "Bugün bir arı kovanının içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kovanda kim ne iş yapar? Arılar çiçeklerde ne arar? Ve arılar olmasaydı ne olurdu?",
        "spoken": "Üç sorumuz var. Kovanda kim ne iş yapar? Arılar çiçeklerde ne arar? Ve arılar olmasaydı ne olurdu?",
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
        "display": "National Geographic'e göre bal arıları, koloni denen büyük topluluklar hâlinde yaşar. Her koloninin tek bir kraliçesi vardır.",
        "spoken": "Neşınıl Ciyografik'e göre bal arıları, koloni denen büyük topluluklar hâlinde yaşar. Her koloninin tek bir kraliçesi vardır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Kraliçenin işi yumurtlamaktır: kovanın yeni kuşağı onun yumurtalarından çıkar.",
        "spoken": "Kraliçenin işi yumurtlamaktır: kovanın yeni kuşağı onun yumurtalarından çıkar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l8",
        "display": "Kraliçe ayrıca ürettiği kimyasal maddelerle öteki arıların davranışını yönlendirir.",
        "spoken": "Kraliçe ayrıca ürettiği kimyasal maddelerle öteki arıların davranışını yönlendirir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Kimyasal mesajla yönetim! Bana da yazılım güncellemeleri böyle geliyor.",
        "spoken": "Kimyasal mesajla yönetim! Bana da yazılım güncellemeleri böyle geliyor.",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Dışarıda uçarken gördüğün arıların hepsi işçi arıdır ve hepsi dişidir.",
        "spoken": "Dışarıda uçarken gördüğün arıların hepsi işçi arıdır ve hepsi dişidir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "İşçilerin iş listesi uzundur: polen ve nektar toplar, peteği yapar, kovanı korur, temizler ve havalandırır.",
        "spoken": "İşçilerin iş listesi uzundur: polen ve nektar toplar, peteği yapar, kovanı korur, temizler ve havalandırır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l12",
        "display": "Üçüncü grup erkek arılardır. İlkbahar ve yaz boyunca kovanda birkaç yüz tane bulunurlar; kış gelince kovandan çıkarılırlar.",
        "spoken": "Üçüncü grup erkek arılardır. İlkbahar ve yaz boyunca kovanda birkaç yüz tane bulunurlar; kış gelince kovandan çıkarılırlar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Kışın koloni, depoladığı bal ve polenle yaşar. Arılar ısıyı korumak için top biçiminde kümelenir.",
        "spoken": "Kışın koloni, depoladığı bal ve polenle yaşar. Arılar ısıyı korumak için top biçiminde kümelenir.",
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
        "display": "Peki arılar çiçeklerde ne arar? ABD Jeoloji Araştırmaları Kurumu USGS'ye göre arılar hem nektarla hem polenle beslenir; ikisine de ihtiyaç duyar.",
        "spoken": "Peki arılar çiçeklerde ne arar? A Be De Jeoloji Araştırmaları Kurumu, Yu Es Ci Es'e göre arılar hem nektarla hem polenle beslenir; ikisine de ihtiyaç duyar.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Nektar, çiçeklerin şekerli sıvısıdır. Polen ise çiçek tozu.",
        "spoken": "Nektar, çiçeklerin şekerli sıvısıdır. Polen ise çiçek tozu.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "ABD Orman Servisi arılara şampiyon tozlaştırıcı diyor. Çünkü çiçekleri bile bile ziyaret ederler: polen ve nektar toplamak için.",
        "spoken": "A Be De Orman Servisi arılara şampiyon tozlaştırıcı diyor. Çünkü çiçekleri bile bile ziyaret ederler: polen ve nektar toplamak için.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Bir süper güçleri de var: arılar, bizim göremediğimiz morötesi ışığı algılayabilir.",
        "spoken": "Bir süper güçleri de var: arılar, bizim göremediğimiz morötesi ışığı algılayabilir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Ben morötesini göremem. Ama televizyon kumandasının ışığını görürüm; o da bir şey!",
        "spoken": "Ben morötesini göremem. Ama televizyon kumandasının ışığını görürüm; o da bir şey!",
        "factIds": []
      },
      {
        "id": "l19",
        "display": "Asıl büyük iş burada başlıyor. Birçok bitki, polenini bir çiçekten ötekine taşıyacak birine ihtiyaç duyar. Bu taşıma işine tozlaşma denir.",
        "spoken": "Asıl büyük iş burada başlıyor. Birçok bitki, polenini bir çiçekten ötekine taşıyacak birine ihtiyaç duyar. Bu taşıma işine tozlaşma denir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Arı çiçekten çiçeğe gezerken poleni de taşımış olur. Yani beslenirken bitkilere kuryelik yapar!",
        "spoken": "Arı çiçekten çiçeğe gezerken poleni de taşımış olur. Yani beslenirken bitkilere kuryelik yapar!",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Birleşmiş Milletler Gıda ve Tarım Örgütü FAO'ya göre çiçekli bitki türlerinin %80'inden fazlasını hayvanlar tozlaştırır; bunların çoğu böcektir.",
        "spoken": "Birleşmiş Milletler Gıda ve Tarım Örgütü, Fao'ya göre çiçekli bitki türlerinin yüzde seksenden fazlasını hayvanlar tozlaştırır; bunların çoğu böcektir.",
        "factIds": [
          "f8"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l22",
        "display": "Sofralarımız da buna bağlı: dünyanın en verimli tarım bitkilerinin dörtte üçü, en azından kısmen tozlaştırıcılara ihtiyaç duyar.",
        "spoken": "Sofralarımız da buna bağlı: dünyanın en verimli tarım bitkilerinin dörtte üçü, en azından kısmen tozlaştırıcılara ihtiyaç duyar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Dünyadaki tarımsal üretimin hacim olarak %35'i arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir.",
        "spoken": "Dünyadaki tarımsal üretimin hacim olarak yüzde otuz beşi arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l24",
        "display": "FAO'ya göre tozlaşma olmasaydı, ekosistemlerdeki pek çok tür ve süreç çökerdi.",
        "spoken": "Fao'ya göre tozlaşma olmasaydı, ekosistemlerdeki pek çok tür ve süreç çökerdi.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l25",
        "display": "Üstelik bal arısı tek değil: dünyada bilinen 20.000'den fazla arı türü var.",
        "spoken": "Üstelik bal arısı tek değil: dünyada bilinen yirmi binden fazla arı türü var.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l26",
        "display": "Ama arıların başı dertte. National Geographic'e göre bal arıları, koloni çöküşü bozukluğu denen bir sorun yüzünden kovanlardan kayboluyor. Bilim insanları nedeninden emin değil.",
        "spoken": "Ama arıların başı dertte. Neşınıl Ciyografik'e göre bal arıları, koloni çöküşü bozukluğu denen bir sorun yüzünden kovanlardan kayboluyor. Bilim insanları nedeninden emin değil.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Yaşam alanlarındaki ve iklimdeki değişiklikler, hastalık yapan mikroplar ve böcek ilaçları da arılar üzerinde baskı yaratıyor.",
        "spoken": "Yaşam alanlarındaki ve iklimdeki değişiklikler, hastalık yapan mikroplar ve böcek ilaçları da arılar üzerinde baskı yaratıyor.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Peki ne yapabiliriz? Arıların farklı çiçeklerden polen ve nektara ihtiyacı var. Bahçesi ya da balkonu olan herkes yardım edebilir.",
        "spoken": "Peki ne yapabiliriz? Arıların farklı çiçeklerden polen ve nektara ihtiyacı var. Bahçesi ya da balkonu olan herkes yardım edebilir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l29",
        "display": "Şimdi sıra sende! Balkonuna ya da bahçene birkaç farklı çiçek ek. Sonra uzaktan izle: hangi çiçeğe kaç arı geliyor?",
        "spoken": "Şimdi sıra sende! Balkonuna ya da bahçene birkaç farklı çiçek ek. Sonra uzaktan izle: hangi çiçeğe kaç arı geliyor?",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l30",
        "display": "Bir arı günlüğü tut: çiçeğin rengini ve gelen ziyaretçileri not et.",
        "spoken": "Bir arı günlüğü tut: çiçeğin rengini ve gelen ziyaretçileri not et.",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Bir uyarı: arılara dokunma ve onları kovalamaya çalışma. Yalnızca uzaktan izle.",
        "spoken": "Bir uyarı: arılara dokunma ve onları kovalamaya çalışma. Yalnızca uzaktan izle.",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Onlar çalışıyor. Mesaideki birini rahatsız etmek olmaz!",
        "spoken": "Onlar çalışıyor. Mesaideki birini rahatsız etmek olmaz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l33",
        "display": "Bunu biliyor muydun? USGS'ye göre neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarına önemli ölçüde destek olur.",
        "spoken": "Bunu biliyor muydun? Yu Es Ci Es'e göre neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarına önemli ölçüde destek olur.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l34",
        "display": "Hızlı soru! Kovanda yumurtlayan arı hangisidir?",
        "spoken": "Hızlı soru! Kovanda yumurtlayan arı hangisidir?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l35",
        "display": "Düşün bakalım... Evet: kraliçe arı!",
        "spoken": "Düşün bakalım... Evet: kraliçe arı!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l36",
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
        "id": "l37",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l38",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l39",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de bir çiçek ekmeye gidiyorum; robotlar da yardım edebilir!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de bir çiçek ekmeye gidiyorum; robotlar da yardım edebilir!",
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
    "statement": "Bal arıları, bütün kovanı yöneten tek bir kraliçesi olan koloniler hâlinde yaşar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "İşçi arıların hepsi dişidir ve kovanın dışında uçarken görülen arılar yalnızca onlardır; besin (polen ve nektar) toplar, peteği ve kovanı yapar, korur, temizler ve havayı dolaştırırlar.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Kraliçenin işi yumurtlamaktır; kovanın yeni kuşağı bu yumurtalardan çıkar. Kraliçe, öteki arıların davranışını yönlendiren kimyasallar üreterek kovanın etkinliklerini düzenler.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Erkek arılar üçüncü sınıftır; ilkbahar ve yaz boyunca her kovanda birkaç yüz erkek arı yaşar, kış aylarında kovandan çıkarılırlar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Arılar bütün kış depoladıkları bal ve polenle yaşar; ısıyı korumak için top biçiminde kümelenir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Arılar hem nektarla hem polenle beslenir ve ikisine de ihtiyaç duyar.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Arılar şampiyon tozlaştırıcılardır; polen ve nektar toplamak için çiçekleri bile bile ziyaret ederler; morötesi ışığı algılayabilirler.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Bütün çiçekli bitki türlerinin yüzde 80'inden fazlasını hayvanlar, çoğunlukla böcekler tozlaştırır. Kuzey Amerika bitki türlerinin yaklaşık yüzde 75'i poleninin taşınması için bir böceğe, çoğunlukla arılara ihtiyaç duyar.",
    "numbers": [
      "80",
      "75"
    ]
  },
  {
    "id": "f9",
    "statement": "Dünyanın en verimli tarım bitkilerinin 3/4'ü en azından kısmen tozlaştırıcılara bağlıdır; dünya tarımsal üretiminin (hacim olarak) %35'i arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir.",
    "numbers": [
      "3",
      "4",
      "35"
    ]
  },
  {
    "id": "f10",
    "statement": "Dünyada bilinen 20.000'den fazla arı türü vardır.",
    "numbers": [
      "20.000"
    ]
  },
  {
    "id": "f11",
    "statement": "Bal arıları, koloni çöküşü bozukluğu nedeniyle kovanlardan kayboluyor; bilim insanları bu çöküşe neyin yol açtığından emin değil.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Yaşam alanı ve iklimdeki değişiklikler ile hastalık etkenleri, böcek ilaçları ve yabancı türler arılar üzerinde baskı yaratır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Arılar çeşitli çiçeklerden polen ve nektara ihtiyaç duyar; bahçıvanların küçük yardımıyla birçok tür varlığını sürdürebilir; tozlaştırıcıların güvenli yaşam alanlarına ve besin kaynaklarına ihtiyacı vardır.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Tozlaşma hizmeti olmasaydı, bir ekosistemde işleyen pek çok tür ve süreç çökerdi.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarının etkinliğini önemli ölçüde tamamlar.",
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
