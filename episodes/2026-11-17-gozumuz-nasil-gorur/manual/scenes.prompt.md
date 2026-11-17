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
        "display": "Şu an bu ekrana bakıyorsun ve renkleri, harfleri, Muma'yı görüyorsun. Ama aslında görmek için gözün tek başına yetmez!",
        "spoken": "Şu an bu ekrana bakıyorsun ve renkleri, harfleri, Muma'yı görüyorsun. Ama aslında görmek için gözün tek başına yetmez!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l2",
        "display": "Işık gözüne nasıl girer, nasıl bir görüntüye dönüşür?",
        "spoken": "Işık gözüne nasıl girer, nasıl bir görüntüye dönüşür?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün göz küresinin içine yolculuk yapıyoruz!",
        "spoken": "Bugün göz küresinin içine yolculuk yapıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Işık göze nasıl girer? Göz onu nasıl odaklar? Ve görüntüyü kim oluşturur?",
        "spoken": "Üç sorumuz var. Işık göze nasıl girer? Göz onu nasıl odaklar? Ve görüntüyü kim oluşturur?",
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
        "display": "KidsHealth'e göre göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukurunda korunur.",
        "spoken": "Kids Helt'e göre göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukurunda korunur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Işığın ilk geçtiği yer korneadır: gözün önündeki saydam bir kubbe. Kornea ışığı kırarak odaklanmaya yardım eder.",
        "spoken": "Işığın ilk geçtiği yer korneadır: gözün önündeki saydam bir kubbe. Kornea ışığı kırarak odaklanmaya yardım eder.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Sonra iris gelir: gözünün renkli bölümü. İris, ortasındaki göz bebeğinden ne kadar ışık gireceğini denetler.",
        "spoken": "Sonra iris gelir: gözünün renkli bölümü. İris, ortasındaki göz bebeğinden ne kadar ışık gireceğini denetler.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "İrisin kasları onun biçimini değiştirir. Işık yaklaşınca göz bebeği küçülür, ışık gidince genişler.",
        "spoken": "İrisin kasları onun biçimini değiştirir. Işık yaklaşınca göz bebeği küçülür, ışık gidince genişler.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Benim gözlerim kamera. Göz bebeğim yok, ama bir objektif kapağım var. Bazen takmayı unutuyorum!",
        "spoken": "Benim gözlerim kamera. Göz bebeğim yok, ama bir objektif kapağım var. Bazen takmayı unutuyorum!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Göz bebeğinden geçen ışık merceğe ulaşır. Ulusal Göz Enstitüsü'ne göre mercek, kornea ile birlikte ışığı retinaya odaklar.",
        "spoken": "Göz bebeğinden geçen ışık merceğe ulaşır. Ulusal Göz Enstitüsü'ne göre mercek, kornea ile birlikte ışığı retinaya odaklar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Mercek esnektir: yakına bakarken kalınlaşır, uzağa bakarken incelir.",
        "spoken": "Mercek esnektir: yakına bakarken kalınlaşır, uzağa bakarken incelir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Retina, gözün arka duvarını kaplayan katmandır. İçinde ışığa duyarlı milyonlarca hücre vardır.",
        "spoken": "Retina, gözün arka duvarını kaplayan katmandır. İçinde ışığa duyarlı milyonlarca hücre vardır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Bu hücrelere fotoreseptör denir. Fotoreseptörler ışığı elektrik sinyallerine çevirir.",
        "spoken": "Bu hücrelere fotoreseptör denir. Fotoreseptörler ışığı elektrik sinyallerine çevirir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "İki türü vardır: çubuklar ve koniler. KidsHealth'e göre her gözde yaklaşık 120 milyon çubuk ve 7 milyon koni bulunur!",
        "spoken": "İki türü vardır: çubuklar ve koniler. Kids Helt'e göre her gözde yaklaşık yüz yirmi milyon çubuk ve yedi milyon koni bulunur!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Çubuklar renkleri ayırt edemez; siyah, beyaz ve grinin tonlarını görür ve biçimleri bildirir.",
        "spoken": "Çubuklar renkleri ayırt edemez; siyah, beyaz ve grinin tonlarını görür ve biçimleri bildirir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Ama çok duyarlıdırlar. Çok karanlıkta görmeni çubuklar sağlar.",
        "spoken": "Ama çok duyarlıdırlar. Çok karanlıkta görmeni çubuklar sağlar.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Koniler ise rengi algılar. İyi çalışmak için çubuklardan daha fazla ışığa ihtiyaç duyarlar.",
        "spoken": "Koniler ise rengi algılar. İyi çalışmak için çubuklardan daha fazla ışığa ihtiyaç duyarlar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l19",
        "display": "Her koni türü üç renkten birine duyarlıdır: kırmızı, yeşil ya da mavi.",
        "spoken": "Her koni türü üç renkten birine duyarlıdır: kırmızı, yeşil ya da mavi.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Ben de kırmızı, yeşil ve maviyi görürüm. Ama sadece ekranımı silince!",
        "spoken": "Ben de kırmızı, yeşil ve maviyi görürüm. Ama sadece ekranımı silince!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l21",
        "display": "Peki görüntü nerede oluşur? Elektrik sinyalleri retinadan görme siniri boyunca beyne gider.",
        "spoken": "Peki görüntü nerede oluşur? Elektrik sinyalleri retinadan görme siniri boyunca beyne gider.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "KidsHealth'e göre görme siniri, gözü beyne bağlayan hızlı bir telefon hattı gibidir.",
        "spoken": "Kids Helt'e göre görme siniri, gözü beyne bağlayan hızlı bir telefon hattı gibidir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Beyin bu sinyalleri gördüğün görüntülere çevirir. Yani aslında beyninle görürsün!",
        "spoken": "Beyin bu sinyalleri gördüğün görüntülere çevirir. Yani aslında beyninle görürsün!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l24",
        "display": "Gözlerin bakıma da ihtiyaç duyar. Göz kapağın dakikada birkaç kez açılıp kapanır ve gözü temiz ve nemli tutar.",
        "spoken": "Gözlerin bakıma da ihtiyaç duyar. Göz kapağın dakikada birkaç kez açılıp kapanır ve gözü temiz ve nemli tutar.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Her göz kırpışında üst kapağından biraz gözyaşı gelir. Gözlerin doğru çalışması için gözyaşına ihtiyaç vardır.",
        "spoken": "Her göz kırpışında üst kapağından biraz gözyaşı gelir. Gözlerin doğru çalışması için gözyaşına ihtiyaç vardır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "Bazı insanlarda konilerin çalışması farklıdır. Ulusal Göz Enstitüsü'ne göre renk görme bozukluğunun en yaygın türü, kırmızı ile yeşili ayırt etmeyi zorlaştırır.",
        "spoken": "Bazı insanlarda konilerin çalışması farklıdır. Ulusal Göz Enstitüsü'ne göre renk görme bozukluğunun en yaygın türü, kırmızı ile yeşili ayırt etmeyi zorlaştırır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l27",
        "display": "Şimdi sıra sende! Loş bir odada aynaya bak ve göz bebeğinin büyüklüğüne dikkat et.",
        "spoken": "Şimdi sıra sende! Loş bir odada aynaya bak ve göz bebeğinin büyüklüğüne dikkat et.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l28",
        "display": "Sonra odanın ışığını aç ve tekrar bak. Göz bebeğin küçüldü mü? Bunu iris yaptı! Gözüne asla el feneri ya da lazer tutma.",
        "spoken": "Sonra odanın ışığını aç ve tekrar bak. Göz bebeğin küçüldü mü? Bunu iris yaptı! Gözüne asla el feneri ya da lazer tutma.",
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
        "id": "l29",
        "display": "Bunu biliyor muydun? KidsHealth'e göre fazla ışık gözlerine zarar verebilir. Bu yüzden güneşli günlerde güneş gözlüğü tak.",
        "spoken": "Bunu biliyor muydun? Kids Helt'e göre fazla ışık gözlerine zarar verebilir. Bu yüzden güneşli günlerde güneş gözlüğü tak.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l30",
        "display": "Hızlı soru! Karanlıkta görmemizi sağlayan fotoreseptörler hangileriydi?",
        "spoken": "Hızlı soru! Karanlıkta görmemizi sağlayan fotoreseptörler hangileriydi?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l31",
        "display": "Düşün bakalım... Evet: çubuklar!",
        "spoken": "Düşün bakalım... Evet: çubuklar!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l32",
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
        "id": "l33",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Abone olmayı ve zili açmayı unutma. Gözlerine iyi bak!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Gözlerine iyi bak!",
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
    "statement": "Göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukuru denen küçük bir oyukta durur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Kornea, gözün renkli bölümünün önünde duran saydam bir kubbedir; ışığı kırarak gözün odaklanmasına yardım eder.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "İris gözün renkli bölümüdür; göz bebeğinin ne kadar ışık alacağını denetler; ona bağlı kaslar biçimini değiştirir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Göz bebekleri ışık yaklaşınca küçülür, ışık gidince genişler.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Mercek kornea ile birlikte ışığı retinaya doğru biçimde odaklar; yakına bakarken kalınlaşır, uzağa bakarken incelir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Retinada ışığa duyarlı milyonlarca hücre vardır; fotoreseptör denen özel hücreler ışığı elektrik sinyallerine çevirir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Her gözde yaklaşık 120 milyon çubuk ve 7 milyon koni hücresi vardır.",
    "numbers": [
      "120",
      "7"
    ]
  },
  {
    "id": "f8",
    "statement": "Çubuklar siyah, beyaz ve gri tonlarında görür ve biçimi bildirir; renkleri ayırt edemez ama çok duyarlıdır, çok karanlıkta görmemizi sağlar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Koniler rengi algılar ve iyi çalışmak için çubuklardan daha fazla ışığa ihtiyaç duyar; her koni türü kırmızı, yeşil ya da mavi renklerden birine duyarlıdır.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Elektrik sinyalleri retinadan görme siniri boyunca beyne gider; beyin sinyalleri gördüğümüz görüntülere çevirir; görme siniri gözü beyne bağlayan hızlı bir telefon hattı gibidir.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Göz kapağı dakikada birkaç kez açılıp kapanarak gözü temiz ve nemli tutar; her göz kırpışta üst kapaktan biraz gözyaşı gelir; gözlerin doğru çalışması için gözyaşı gerekir.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Renk görme bozukluğunun en yaygın türü kırmızı ile yeşili ayırt etmeyi zorlaştırır; tam renk görme bozukluğunda hiç renk görülmez.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Güneş gözlüğü takılmalıdır; fazla ışık gözlere zarar verebilir; parçacık ya da kimyasal sıçrayabilecek derslerde koruyucu gözlük takılmalıdır.",
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
