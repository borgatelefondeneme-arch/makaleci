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
        "display": "Şu an bu cümleyi duyuyor, anlıyor ve hatırlıyorsun. Bunu yapan, kafatasının içindeki organ: beynin!",
        "spoken": "Şu an bu cümleyi duyuyor, anlıyor ve hatırlıyorsun. Bunu yapan, kafatasının içindeki organ: beynin!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Beyin bu kadar işi nasıl yapar? Ve yeni bir şey öğrendiğinde içinde ne değişir?",
        "spoken": "Beyin bu kadar işi nasıl yapar? Ve yeni bir şey öğrendiğinde içinde ne değişir?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün beyninin içine, sinir hücrelerinin dünyasına gidiyoruz!",
        "spoken": "Bugün beyninin içine, sinir hücrelerinin dünyasına gidiyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Beynin bölümleri ne iş yapar? Sinir hücreleri nasıl haberleşir? Ve öğrendiğimizde ne olur?",
        "spoken": "Üç sorumuz var. Beynin bölümleri ne iş yapar? Sinir hücreleri nasıl haberleşir? Ve öğrendiğimizde ne olur?",
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
        "display": "KidsHealth'e göre beyin; ne düşündüğünü, ne hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.",
        "spoken": "Kids Helt'e göre beyin; ne düşündüğünü, ne hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bu değerli organı kafatası korur. Ayrıca zar katmanları ve özel bir sıvı onu yastık gibi sarar.",
        "spoken": "Bu değerli organı kafatası korur. Ayrıca zar katmanları ve özel bir sıvı onu yastık gibi sarar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "En büyük bölüm büyük beyindir. Sağ ve sol iki yarıya ayrılır; bunlara yarım küre denir.",
        "spoken": "En büyük bölüm büyük beyindir. Sağ ve sol iki yarıya ayrılır; bunlara yarım küre denir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Büyük beynin dört lobu vardır. Alnının arkasındaki alın lobu, karmaşık düşünmenin çoğunu yapar.",
        "spoken": "Büyük beynin dört lobu vardır. Alnının arkasındaki alın lobu, karmaşık düşünmenin çoğunu yapar.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Yan lob dokunma, tat ve sıcaklık bilgisini işler. Kulaklarına yakın şakak lobu, sesleri ve dili anlamanı sağlar.",
        "spoken": "Yan lob dokunma, tat ve sıcaklık bilgisini işler. Kulaklarına yakın şakak lobu, sesleri ve dili anlamanı sağlar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Başının arkasındaki art kafa lobu ise gözlerinden gelen görüntüleri işler.",
        "spoken": "Başının arkasındaki art kafa lobu ise gözlerinden gelen görüntüleri işler.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Beyincik dengeni ve hareketlerinin uyumunu sağlar. Beyin sapı ise nefes alma ve kalp atışı gibi otomatik işleri yönetir.",
        "spoken": "Beyincik dengeni ve hareketlerinin uyumunu sağlar. Beyin sapı ise nefes alma ve kalp atışı gibi otomatik işleri yönetir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Benim de bir işlemcim var. Ama dört lobu yok; olsa olsa dört düğmesi var!",
        "spoken": "Benim de bir işlemcim var. Ama dört lobu yok; olsa olsa dört düğmesi var!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Şimdi beynin yapı taşlarına bakalım. BrainFacts'e göre beynin temel çalışma birimi nörondur: bilgi iletmek için özelleşmiş bir hücre.",
        "spoken": "Şimdi beynin yapı taşlarına bakalım. Breyn Fekts'e göre beynin temel çalışma birimi nörondur: bilgi iletmek için özelleşmiş bir hücre.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Beyninde milyarlarca nöron var.",
        "spoken": "Beyninde milyarlarca nöron var.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l16",
        "display": "Bir nöronun hücre gövdesi, dendritleri ve bir aksonu vardır. Dendritler başka nöronlardan gelen mesajları alır.",
        "spoken": "Bir nöronun hücre gövdesi, dendritleri ve bir aksonu vardır. Dendritler başka nöronlardan gelen mesajları alır.",
        "factIds": [
          "f6",
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Akson mesajı bir elektrik uyarısı olarak iletir. Bazı aksonlar santimetrenin küçük bir parçası kadar kısa, bazıları bir metreye kadar uzundur.",
        "spoken": "Akson mesajı bir elektrik uyarısı olarak iletir. Bazı aksonlar santimetrenin küçük bir parçası kadar kısa, bazıları bir metreye kadar uzundur.",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Birçok akson, miyelin denen katmanlı bir kılıfla kaplıdır. Miyelin, elektrik sinyalini hızlandırır.",
        "spoken": "Birçok akson, miyelin denen katmanlı bir kılıfla kaplıdır. Miyelin, elektrik sinyalini hızlandırır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "İki nöronun buluştuğu temas noktasına sinaps denir. Mesaj burada bir nörondan ötekine geçer.",
        "spoken": "İki nöronun buluştuğu temas noktasına sinaps denir. Mesaj burada bir nörondan ötekine geçer.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l20",
        "display": "Yani beynin, elektrik ve kimyasalları birlikte kullanan dev bir haberleşme ağıdır.",
        "spoken": "Yani beynin, elektrik ve kimyasalları birlikte kullanan dev bir haberleşme ağıdır.",
        "factIds": [
          "f7"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l21",
        "display": "Peki öğrendiğinde ne olur? KidsHealth'e göre öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider.",
        "spoken": "Peki öğrendiğinde ne olur? Kids Helt'e göre öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Bu mesajlar beyninde yollar oluşturur ve bu yollar belleğin temelidir.",
        "spoken": "Bu mesajlar beyninde yollar oluşturur ve bu yollar belleğin temelidir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Bu yüzden yeni bir şey ilk başta çok dikkat ister, ama tekrar ettikçe kolaylaşır. Bisiklete binmeyi düşün!",
        "spoken": "Bu yüzden yeni bir şey ilk başta çok dikkat ister, ama tekrar ettikçe kolaylaşır. Bisiklete binmeyi düşün!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Birçok bilim insanı, beyni hep yeni şeyler öğrenmeye zorlamanın önemli olduğuna inanır. Böylece yeni bağlantılar kurulur.",
        "spoken": "Birçok bilim insanı, beyni hep yeni şeyler öğrenmeye zorlamanın önemli olduğuna inanır. Böylece yeni bağlantılar kurulur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Uyku da çok önemli. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "spoken": "Uyku da çok önemli. Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'ye göre uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Yeterince uyumazsan odaklanmak ve net düşünmek zorlaşabilir.",
        "spoken": "Yeterince uyumazsan odaklanmak ve net düşünmek zorlaşabilir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Ben uyumam, ama yeniden başlatınca ben de daha iyi düşünürüm!",
        "spoken": "Ben uyumam, ama yeniden başlatınca ben de daha iyi düşünürüm!",
        "factIds": []
      },
      {
        "id": "l28",
        "display": "Şimdi sıra sende! Hiç denemediğin bir şeyi seç: örneğin ayakkabı bağını yeni bir yöntemle bağlamak.",
        "spoken": "Şimdi sıra sende! Hiç denemediğin bir şeyi seç: örneğin ayakkabı bağını yeni bir yöntemle bağlamak.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l29",
        "display": "Bir hafta boyunca her gün dene ve kaç saniyede yaptığını not et. Süre kısalıyor mu? İşte beynindeki yol güçleniyor!",
        "spoken": "Bir hafta boyunca her gün dene ve kaç saniyede yaptığını not et. Süre kısalıyor mu? İşte beynindeki yol güçleniyor!",
        "factIds": [
          "f10"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l30",
        "display": "Bunu biliyor muydun? Beyninde, nöronlardan en az on kat fazla glia denen yardımcı hücre vardır.",
        "spoken": "Bunu biliyor muydun? Beyninde, nöronlardan en az on kat fazla glia denen yardımcı hücre vardır.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l31",
        "display": "Hızlı soru! İki nöronun buluştuğu temas noktasının adı neydi?",
        "spoken": "Hızlı soru! İki nöronun buluştuğu temas noktasının adı neydi?",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l32",
        "display": "Düşün bakalım... Evet: sinaps!",
        "spoken": "Düşün bakalım... Evet: sinaps!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l33",
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
        "id": "l34",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l36",
        "display": "Abone olmayı ve zili açmayı unutma. Bu gece de iyi uyu; beynin teşekkür edecek!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bu gece de iyi uyu; beynin teşekkür edecek!",
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
    "statement": "Beyin ne düşündüğünü ve hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Beyin ve omurilik kemikle korunur: beyin kafatası kemikleriyle; ayrıca meninks denen zar katmanları ve beyin omurilik sıvısıyla yastıklanır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Büyük beynin sağ ve sol yarısı vardır, bunlara yarım küre denir; dört lobu vardır: alın, yan, şakak ve art kafa lobu.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Alın lobu karmaşık düşünmenin çoğunu yapar; yan lob dokunma, tat ve sıcaklık bilgisini işler; şakak lobu sesleri ve dili anlamamızı sağlar; art kafa lobu gözlerden gelen görsel bilgiyi işler.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Beyincik denge, hareket ve koordinasyondan sorumludur; beyin sapı nefes alma, kalp atışı, kan basıncı ve yutma gibi otomatik işlevleri kontrol eder.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Nöron, beynin temel çalışma birimidir; bilgi iletmek için özelleşmiş bir hücredir; nöronların çoğunda hücre gövdesi, akson ve dendritler bulunur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Dendritler hücre gövdesinden uzanır ve diğer nöronlardan mesaj alır; akson elektrik uyarılarını iletir; sinapslar bir nöronun diğeriyle iletişim kurduğu temas noktalarıdır; nöronlar bilgiyi elektrokimyasal bir süreçle aktarır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Aksonların boyu santimetrenin küçük bir kesrinden yaklaşık bir metreye ya da daha fazlasına kadar değişebilir; birçok akson elektrik sinyallerinin iletimini hızlandıran katmanlı bir miyelin kılıfla kaplıdır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Beyinde milyarlarca nöron vardır; beyin, nörondan en az on kat fazla glia hücresi içerir.",
    "numbers": [
      "10"
    ]
  },
  {
    "id": "f10",
    "statement": "Büyüyüp öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider; bu yüzden araba sürmek ilk öğrenirken çok dikkat ister ama sonra kendiliğinden yapılır; beyinde dolaşan mesajlar belleğin temeli olan yollar oluşturur.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Birçok bilim insanı beyni yeni şeyler öğrenmeye ve yeni bağlantılar kurmaya zorlamanın önemli olduğuna inanır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder; yeterince ya da kaliteli uyumamak odaklanmayı ve net düşünmeyi zorlaştırabilir.",
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
