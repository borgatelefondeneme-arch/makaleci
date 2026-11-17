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
        "display": "Yere bir kırıntı düşür ve bekle. Bir süre sonra karıncalar gelir, hem de sıra sıra! Onlara kim haber verdi?",
        "spoken": "Yere bir kırıntı düşür ve bekle. Bir süre sonra karıncalar gelir, hem de sıra sıra! Onlara kim haber verdi?",
        "factIds": [
          "f1",
          "f13"
        ]
      },
      {
        "id": "l2",
        "display": "Ne telefonları var ne de konuşabiliyorlar. Peki nasıl anlaşıyorlar?",
        "spoken": "Ne telefonları var ne de konuşabiliyorlar. Peki nasıl anlaşıyorlar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün yerin altına, bir karınca kolonisine giriyoruz!",
        "spoken": "Bugün yerin altına, bir karınca kolonisine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Karıncalar nasıl haberleşir? Kolonide kim ne iş yapar? Ve yuvaları nasıldır?",
        "spoken": "Üç sorumuz var. Karıncalar nasıl haberleşir? Kolonide kim ne iş yapar? Ve yuvaları nasıldır?",
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
        "display": "National Geographic'e göre karıncalar feromon denen koku kimyasalları salgılayarak haberleşir.",
        "spoken": "Neşınıl Ciyogrefik'e göre karıncalar feromon denen koku kimyasalları salgılayarak haberleşir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Feromonlar diğer karıncaları tehlikeye karşı uyarabilir ya da onları bir besin kaynağına götürebilir.",
        "spoken": "Feromonlar diğer karıncaları tehlikeye karşı uyarabilir ya da onları bir besin kaynağına götürebilir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Yani karıncalar kokuyla mesajlaşır. Ben de mesaj atarım, ama benimkiler koku değil, bip bip!",
        "spoken": "Yani karıncalar kokuyla mesajlaşır. Ben de mesaj atarım, ama benimkiler koku değil, bip bip!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Avustralya Müzesi'ne göre karıncalar hayvanlar âlemindeki en karmaşık kimyasal iletişime sahiptir.",
        "spoken": "Avustralya Müzesi'ne göre karıncalar hayvanlar âlemindeki en karmaşık kimyasal iletişime sahiptir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Birlikte, tek bir böceğin asla yapamayacağı işleri başarırlar.",
        "spoken": "Birlikte, tek bir böceğin asla yapamayacağı işleri başarırlar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Besin ararken türüne göre gruplar halinde ya da tek başına dolaşırlar. Çoğu zaman zikzak çizerler, bazı türler ise yollar üzerinde sıra halinde koşar.",
        "spoken": "Besin ararken türüne göre gruplar halinde ya da tek başına dolaşırlar. Çoğu zaman zikzak çizerler, bazı türler ise yollar üzerinde sıra halinde koşar.",
        "factIds": [
          "f13"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Karıncalar koloni denen büyük topluluklarda yaşar. Bir koloni, türüne göre birkaç bireyden yüz binlerce karıncaya kadar büyüyebilir.",
        "spoken": "Karıncalar koloni denen büyük topluluklarda yaşar. Bir koloni, türüne göre birkaç bireyden yüz binlerce karıncaya kadar büyüyebilir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Koloniyi bir ya da birden çok kraliçe yönetir. Kraliçeler binlerce yumurta bırakır; genellikle yalnızca onlar yumurtlar.",
        "spoken": "Koloniyi bir ya da birden çok kraliçe yönetir. Kraliçeler binlerce yumurta bırakır; genellikle yalnızca onlar yumurtlar.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "En sık gördüğün karıncalar işçilerdir. İşçiler, hiç üremeyen dişi karıncalardır.",
        "spoken": "En sık gördüğün karıncalar işçilerdir. İşçiler, hiç üremeyen dişi karıncalardır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Besin ararlar, kraliçenin yavrularına bakarlar, yuvada çalışırlar ve topluluğu korurlar.",
        "spoken": "Besin ararlar, kraliçenin yavrularına bakarlar, yuvada çalışırlar ve topluluğu korurlar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Ben de çok çalışkanım. Ama işçi karınca gibi değil; ben bir şarjla ancak bir video çekebiliyorum!",
        "spoken": "Ben de çok çalışkanım. Ama işçi karınca gibi değil; ben bir şarjla ancak bir video çekebiliyorum!",
        "factIds": []
      },
      {
        "id": "l17",
        "display": "Bazı türlerde askerler vardır. Askerler tehlikeye karşı ısırarak, asidik kimyasal fışkırtarak ya da sokarak karşılık verebilir.",
        "spoken": "Bazı türlerde askerler vardır. Askerler tehlikeye karşı ısırarak, asidik kimyasal fışkırtarak ya da sokarak karşılık verebilir.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Kanatlı karıncalar ise çiftleşmek ve yeni koloniler kurmak için yuvadan ayrılır. Kolonide yalnızca üreyebilenlerin kanadı vardır.",
        "spoken": "Kanatlı karıncalar ise çiftleşmek ve yeni koloniler kurmak için yuvadan ayrılır. Kolonide yalnızca üreyebilenlerin kanadı vardır.",
        "factIds": [
          "f6"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l19",
        "display": "Peki yuvaları nerede? Yer altında, toprak tümseklerinde, hatta ağaçlarda olabilir.",
        "spoken": "Peki yuvaları nerede? Yer altında, toprak tümseklerinde, hatta ağaçlarda olabilir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Yuvanın içinde yumurtalar, larvalar ve pupalar bulunur. Bazı karıncalar yaprakları ipekle birleştirerek yuva yapar.",
        "spoken": "Yuvanın içinde yumurtalar, larvalar ve pupalar bulunur. Bazı karıncalar yaprakları ipekle birleştirerek yuva yapar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Ordu karıncaları gibi bazı türlerin ise kalıcı bir yuvası yoktur. Hep yoldalar, tıpkı benim gibi gezgin!",
        "spoken": "Ordu karıncaları gibi bazı türlerin ise kalıcı bir yuvası yoktur. Hep yoldalar, tıpkı benim gibi gezgin!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "Karıncalar çok güçlüdür. National Geographic'e göre bazı işçiler kendi vücut ağırlıklarının 50 katını taşıyabilir!",
        "spoken": "Karıncalar çok güçlüdür. Neşınıl Ciyogrefik'e göre bazı işçiler kendi vücut ağırlıklarının elli katını taşıyabilir!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Bir karınca türü, yaralı arkadaşlarını geride bırakmaz. Onları iyileşebilecekleri yuvaya geri taşır.",
        "spoken": "Bir karınca türü, yaralı arkadaşlarını geride bırakmaz. Onları iyileşebilecekleri yuvaya geri taşır.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l24",
        "display": "Sel geldiğinde ise karıncalar birbirine tutunup küme oluşturur ve suyun üstünde yüzerek kurtulabilir.",
        "spoken": "Sel geldiğinde ise karıncalar birbirine tutunup küme oluşturur ve suyun üstünde yüzerek kurtulabilir.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Bir yetişkinle bahçede ya da parkta bir karınca yolu bul.",
        "spoken": "Şimdi sıra sende! Bir yetişkinle bahçede ya da parkta bir karınca yolu bul.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Yolun yakınına minicik bir ekmek kırıntısı bırak ve izle. Karıncalar kırıntıyı buluyor mu? Sıra halinde mi geliyorlar? Karıncalara dokunma; bazıları ısırabilir ya da sokabilir.",
        "spoken": "Yolun yakınına minicik bir ekmek kırıntısı bırak ve izle. Karıncalar kırıntıyı buluyor mu? Sıra halinde mi geliyorlar? Karıncalara dokunma; bazıları ısırabilir ya da sokabilir.",
        "factIds": [
          "f1",
          "f7",
          "f13"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l27",
        "display": "Bunu biliyor muydun? National Geographic'e göre Dünya'da 20 katrilyon karınca var. Bu, insan başına 2,5 milyon karınca demek! Saymaya kalksam pilim biter!",
        "spoken": "Bunu biliyor muydun? Neşınıl Ciyogrefik'e göre Dünya'da yirmi katrilyon karınca var. Bu, insan başına iki buçuk milyon karınca demek! Saymaya kalksam pilim biter!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Hızlı soru! Karıncaların haberleşmek için salgıladığı koku kimyasallarına ne denir?",
        "spoken": "Hızlı soru! Karıncaların haberleşmek için salgıladığı koku kimyasallarına ne denir?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l29",
        "display": "Düşün bakalım... Evet: feromon!",
        "spoken": "Düşün bakalım... Evet: feromon!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l30",
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
        "id": "l31",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l33",
        "display": "Abone olmayı ve zili açmayı unutma. Bir dahaki sefere karıncaları görünce selam ver!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bir dahaki sefere karıncaları görünce selam ver!",
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
    "statement": "Karıncalar feromon denen koku kimyasalları salgılayarak iletişim kurar ve iş birliği yapar; bu kimyasallar diğerlerini tehlikeye karşı uyarabilir ya da onları umut veren bir besin kaynağına götürebilir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Karıncalar hayvanlar âlemindeki en karmaşık kimyasal iletişime sahiptir; birlikte, tek bir böceğin yapamayacağı işleri başarırlar; başarılarının bir nedeni birbirleriyle iletişim kurabilmeleridir.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Koloni büyüklüğü türe göre birkaç bireyden on binlerce bireye kadar değişir; tek bir koloni yüz binlerce karınca barındırabilir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Topluluğu bir ya da birden çok kraliçe yönetir; kraliçeler binlerce yumurta bırakır; genellikle yalnızca kraliçeler yumurtlar, işçiler üreyemez.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "İşçi karıncalar hiç üremeyen dişilerdir; besin arar, kraliçenin yavrularına bakar, yuvada çalışır ve topluluğu korur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kanatlı karıncalar çiftleşmek ve yeni koloniler kurmak için yuvadan ayrılır; yalnızca üreyebilen karıncaların kanadı vardır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Askerler rahatsızlığa karşı çıkar; ısırarak, asidik kimyasal fışkırtarak ya da sokarak tepki verebilir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Karıncalar yer altında, toprak tümseklerinde ya da ağaçlarda yuvalarda yaşar; yuvalarda yumurtalar, larvalar ve pupalar bulunur; bazı karıncalar yaprakları ipekle birleştirerek yuva yapar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Ordu karıncaları gibi bazı türlerin kalıcı yuvası yoktur.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Bazı işçi karıncalar kendi vücut ağırlıklarının 50 katını taşıyabilir.",
    "numbers": [
      "50"
    ]
  },
  {
    "id": "f11",
    "statement": "Dünya'da 20 katrilyon karınca vardır; bu, insan başına 2,5 milyon karınca demektir.",
    "numbers": [
      "20",
      "2.5"
    ]
  },
  {
    "id": "f12",
    "statement": "Karıncalar dirsekli antenlerinden ve karın ile göğüs arasındaki ince 'bel'den tanınır; altı ince bacakları vardır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Türe göre gruplar halinde ya da tek başına besin ararlar; besin ararken çoğu zaman zikzak çizerler; bazı türler sıralar halinde, çoğu zaman yollar üzerinde koşar.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Bir karınca türü yaralı karıncaları geride bırakmaz, iyileşebilecekleri yuvaya geri taşır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Karıncalar sel sularından birbirine tutunup kümelenerek suyun yüzeyinde yüzerek kurtulabilir.",
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
