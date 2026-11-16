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
        "display": "Saçlarını uçuran, uçurtmanı göğe çıkaran, ağaçları sallayan bir güç var. Ama onu hiç göremiyorsun!",
        "spoken": "Saçlarını uçuran, uçurtmanı göğe çıkaran, ağaçları sallayan bir güç var. Ama onu hiç göremiyorsun!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Rüzgâr nereden gelir? Ve neden bazen hafif, bazen çok sert eser?",
        "spoken": "Rüzgâr nereden gelir? Ve neden bazen hafif, bazen çok sert eser?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün görünmez havanın izini sürüyoruz!",
        "spoken": "Bugün görünmez havanın izini sürüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Rüzgârı ne oluşturur? Neden belirli yönlerde eser? Ve rüzgârı nasıl ölçeriz?",
        "spoken": "Üç sorumuz var. Rüzgârı ne oluşturur? Neden belirli yönlerde eser? Ve rüzgârı nasıl ölçeriz?",
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
        "display": "National Geographic'e göre rüzgâr, Güneş'in Dünya'yı eşit olmayan biçimde ısıtmasıyla oluşan hava hareketidir.",
        "spoken": "Neşınıl Ciyografik'e göre rüzgâr, Güneş'in Dünya'yı eşit olmayan biçimde ısıtmasıyla oluşan hava hareketidir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Hava ısınınca yoğunluğu azalır ve yükselir. Yerinde alçak basınçlı bir bölge kalır.",
        "spoken": "Hava ısınınca yoğunluğu azalır ve yükselir. Yerinde alçak basınçlı bir bölge kalır.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l8",
        "display": "Rüzgâr ise genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere doğru eser. Hava, boşluğu doldurmak için koşar!",
        "spoken": "Rüzgâr ise genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere doğru eser. Hava, boşluğu doldurmak için koşar!",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Bu kadar koşuşturma bana da lazım. Ama ben rüzgârla değil, pille çalışıyorum!",
        "spoken": "Bu kadar koşuşturma bana da lazım. Ama ben rüzgârla değil, pille çalışıyorum!",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Bunu kıyıda her gün görebilirsin. NOAA'ya göre kara, gündüz ile gece arasında denizden çok daha fazla ısınıp soğur.",
        "spoken": "Bunu kıyıda her gün görebilirsin. Noa'ya göre kara, gündüz ile gece arasında denizden çok daha fazla ısınıp soğur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l11",
        "display": "Gündüz karadaki ılık hava yükselir; denizdeki serin hava karaya doğru akar. Buna deniz meltemi denir.",
        "spoken": "Gündüz karadaki ılık hava yükselir; denizdeki serin hava karaya doğru akar. Buna deniz meltemi denir.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l12",
        "display": "Gece ise kara denizden daha çok soğur ve rüzgâr tersine döner: kara meltemi.",
        "spoken": "Gece ise kara denizden daha çok soğur ve rüzgâr tersine döner: kara meltemi.",
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
        "id": "l13",
        "display": "Aynı şey bütün dünyada olur. Ekvator, dünyanın geri kalanından daha çok ısınır.",
        "spoken": "Aynı şey bütün dünyada olur. Ekvator, dünyanın geri kalanından daha çok ısınır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Ekvator'daki ılık hava yükselir ve kutuplara doğru gider. Daha serin, yoğun hava da yeryüzünde Ekvator'a doğru akıp onun yerini alır.",
        "spoken": "Ekvator'daki ılık hava yükselir ve kutuplara doğru gider. Daha serin, yoğun hava da yeryüzünde Ekvator'a doğru akıp onun yerini alır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l15",
        "display": "Ama Dünya döner! Bu dönüş, havanın yolunu saptırır. Buna Coriolis etkisi denir.",
        "spoken": "Ama Dünya döner! Bu dönüş, havanın yolunu saptırır. Buna Koryolis etkisi denir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Bu yüzden her yarım kürede tek büyük dolaşım yerine üç ayrı dolaşım oluşur.",
        "spoken": "Bu yüzden her yarım kürede tek büyük dolaşım yerine üç ayrı dolaşım oluşur.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Hâkim rüzgârlar da çoğunlukla doğu-batı yönünde eser. Tropiklerde doğudan esen güçlü rüzgârlara alize denir. Orta enlemlerde ise batı rüzgârları eser.",
        "spoken": "Hâkim rüzgârlar da çoğunlukla doğu-batı yönünde eser. Tropiklerde doğudan esen güçlü rüzgârlara alize denir. Orta enlemlerde ise batı rüzgârları eser.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Yukarılarda daha da hızlıları var: jet akımları. Bu güçlü rüzgârlar saatte 480 kilometreye kadar esebilir!",
        "spoken": "Yukarılarda daha da hızlıları var: jet akımları. Bu güçlü rüzgârlar saatte dört yüz seksen kilometreye kadar esebilir!",
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
        "id": "l19",
        "display": "Peki rüzgârı nasıl ölçeriz? Hızını anemometre ölçer. Yönünü ise rüzgâr gülü gösterir.",
        "spoken": "Peki rüzgârı nasıl ölçeriz? Hızını anemometre ölçer. Yönünü ise rüzgâr gülü gösterir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l20",
        "display": "Aletin yoksa gözlerin yeter! 1805'te Amiral Francis Beaufort, denizcilerin rüzgârı gözle tahmin etmesi için bir ölçek geliştirdi.",
        "spoken": "Aletin yoksa gözlerin yeter! Bin sekiz yüz beşte Amiral Frensis Bofort, denizcilerin rüzgârı gözle tahmin etmesi için bir ölçek geliştirdi.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l21",
        "display": "Ölçek 0'dan 12'ye kadar gider. 0'da hava sakindir ve duman dümdüz yükselir.",
        "spoken": "Ölçek sıfırdan on ikiye kadar gider. Sıfırda hava sakindir ve duman dümdüz yükselir.",
        "factIds": [
          "f11",
          "f12"
        ]
      },
      {
        "id": "l22",
        "display": "3'te yapraklar ve ince dallar sürekli kıpırdar, hafif bir bayrak açılır. 7'de bütün ağaçlar sallanır ve rüzgâra karşı yürümek zorlaşır.",
        "spoken": "Üçte yapraklar ve ince dallar sürekli kıpırdar, hafif bir bayrak açılır. Yedide bütün ağaçlar sallanır ve rüzgâra karşı yürümek zorlaşır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l23",
        "display": "10'da ise ağaçlar kökünden sökülebilir. Böyle havalarda dışarı çıkmamak gerekir.",
        "spoken": "Onda ise ağaçlar kökünden sökülebilir. Böyle havalarda dışarı çıkmamak gerekir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l24",
        "display": "Rüzgâr bir enerji kaynağıdır da. Rüzgâr türbinlerinin kanatlarını çevirir; kanatlar bir jeneratörü döndürür ve elektrik üretilir.",
        "spoken": "Rüzgâr bir enerji kaynağıdır da. Rüzgâr türbinlerinin kanatlarını çevirir; kanatlar bir jeneratörü döndürür ve elektrik üretilir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l25",
        "display": "Rüzgâr, doğrudan kirlilik yaratmayan, yenilenebilir bir kaynaktır. Yükseklerde daha hızlı estiği için türbin kuleleri uzun yapılır.",
        "spoken": "Rüzgâr, doğrudan kirlilik yaratmayan, yenilenebilir bir kaynaktır. Yükseklerde daha hızlı estiği için türbin kuleleri uzun yapılır.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Şimdi sıra sende! Bir hafta boyunca her gün pencereden dışarı bak: ağaçlar, yapraklar, bayraklar ne yapıyor?",
        "spoken": "Şimdi sıra sende! Bir hafta boyunca her gün pencereden dışarı bak: ağaçlar, yapraklar, bayraklar ne yapıyor?",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Beaufort ölçeğine göre o günün rüzgârına bir sayı ver ve tabloya yaz. En rüzgârlı gün hangisiydi?",
        "spoken": "Beaufort ölçeğine göre o günün rüzgârına bir sayı ver ve tabloya yaz. En rüzgârlı gün hangisiydi?",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l28",
        "display": "Bunu biliyor muydun? Rüzgârı göremez ya da tutamazsın, ama kuvvetini her zaman hissedebilirsin.",
        "spoken": "Bunu biliyor muydun? Rüzgârı göremez ya da tutamazsın, ama kuvvetini her zaman hissedebilirsin.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l29",
        "display": "Hızlı soru! Gündüz denizden karaya esen rüzgârın adı nedir?",
        "spoken": "Hızlı soru! Gündüz denizden karaya esen rüzgârın adı nedir?",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l30",
        "display": "Düşün bakalım... Evet: deniz meltemi!",
        "spoken": "Düşün bakalım... Evet: deniz meltemi!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l31",
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
        "id": "l32",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Abone olmayı ve zili açmayı unutma.",
        "spoken": "Abone olmayı ve zili açmayı unutma.",
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
    "statement": "Rüzgâr, Dünya'nın Güneş tarafından eşit olmayan biçimde ısıtılmasından kaynaklanan hava hareketidir; göremez ya da tutamazsın ama kuvvetini hissedebilirsin.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Atmosfer basıncındaki farklar rüzgârı oluşturur; rüzgâr genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere eser.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Hava ısındıkça yoğunluğu azalır ve 'termal alçak' denen zayıf bir alçak basınç bölgesi oluşur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Ekvator'da Güneş suyu ve karayı dünyanın geri kalanından daha çok ısıtır; ılık ekvator havası atmosferde yükselir ve kutuplara doğru gider; daha serin, yoğun hava yeryüzünde Ekvator'a doğru ilerleyip ısınan havanın yerini alır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Deniz meltemi gündüz, kara meltemi gece eser; gündüz ile gece arasındaki sıcaklık farkı karada denizdekinden çok daha büyüktür; gece kara sıcaklığı denizinkinin altına düşer.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Karadaki ılık hava yükselir ve sudaki serin hava karaya doğru ilerleyerek iç kesimlere esen bir meltem oluşturur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Dünya'nın dönmesi havanın doğuya doğru sapmasına yol açar; buna Coriolis etkisi denir; her yarım kürede tek büyük dolaşım yerine üç dolaşım vardır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Hâkim rüzgârlar genellikle kuzey-güney değil doğu-batı doğrultusunda eser; alize rüzgârları tropiklerde doğudan esen güçlü rüzgârlardır; batı rüzgârları orta enlemlerde batıdan eser.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Jet akımları üst atmosferde saatte 480 kilometreye kadar esebilen güçlü, hızlı rüzgârlardır.",
    "numbers": [
      "480"
    ]
  },
  {
    "id": "f10",
    "statement": "Anemometre rüzgâr hızını, rüzgâr gülü (yön göstergesi) rüzgârın yönünü ölçer.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Beaufort ölçeği 0'dan başlar ve 12'ye kadar gider; Amiral Sir Francis Beaufort ölçeği 1805'te denizcilerin rüzgârı gözle tahmin etmesine yardım etmek için geliştirdi.",
    "numbers": [
      "0",
      "12",
      "1805"
    ]
  },
  {
    "id": "f12",
    "statement": "Beaufort 0: sakin, duman dümdüz yükselir; 3: yapraklar ve küçük dallar sürekli hareket eder, hafif bayrağı açar; 7: bütün ağaçlar sallanır, rüzgâra karşı yürümek zorlaşır; 10: ağaçlar kökünden sökülür.",
    "numbers": [
      "0",
      "3",
      "7",
      "10"
    ]
  },
  {
    "id": "f13",
    "statement": "Rüzgâr, doğrudan kirlilik yaratmayan yenilenebilir bir kaynaktır; rüzgâr kanatları çevirince kanatlar bir jeneratörü döndürür ve elektrik üretir; rüzgâr hızı yükseklikle arttığı için daha uzun kuleler daha çok enerji yakalar.",
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
