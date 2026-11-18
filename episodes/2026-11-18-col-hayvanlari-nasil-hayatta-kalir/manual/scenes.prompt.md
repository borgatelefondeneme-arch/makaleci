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
        "display": "Kavurucu güneş, yağmur yok, gölge yok. Böyle bir yerde sen kaç saat dayanırdın? Ama çölde sayısız hayvan ve bitki yaşıyor!",
        "spoken": "Kavurucu güneş, yağmur yok, gölge yok. Böyle bir yerde sen kaç saat dayanırdın? Ama çölde sayısız hayvan ve bitki yaşıyor!",
        "factIds": [
          "f1",
          "f13"
        ]
      },
      {
        "id": "l2",
        "display": "Peki onlar susuzluğa ve sıcağa nasıl dayanıyor?",
        "spoken": "Peki onlar susuzluğa ve sıcağa nasıl dayanıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün çölün hayatta kalma ustalarıyla tanışıyoruz!",
        "spoken": "Bugün çölün hayatta kalma ustalarıyla tanışıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Çöl nedir? Hayvanlar sıcaktan ve susuzluktan nasıl korunur? Ve bitkiler suyu nasıl saklar?",
        "spoken": "Üç sorumuz var. Çöl nedir? Hayvanlar sıcaktan ve susuzluktan nasıl korunur? Ve bitkiler suyu nasıl saklar?",
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
        "display": "National Geographic'e göre çöl, çok az yağış alan bir bölgedir: yılda en fazla 25 santimetre yağış.",
        "spoken": "Neşınıl Ciyogrefik'e göre çöl, çok az yağış alan bir bölgedir: yılda en fazla yirmi beş santimetre yağış.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bazı çöllerde gündüz sıcaklığı 54 santigrat dereceye kadar çıkar! Ama her çöl sıcak değildir; Antarktika'nın neredeyse tamamı bir kutup çölüdür.",
        "spoken": "Bazı çöllerde gündüz sıcaklığı elli dört santigrat dereceye kadar çıkar! Ama her çöl sıcak değildir; Antarktika'nın neredeyse tamamı bir kutup çölüdür.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Çölde gece ile gündüz arasındaki fark da büyüktür. Chihuahua Çölü'nde gündüz 37 dereceyi aşabilir, gece ise sıfırın altına düşebilir.",
        "spoken": "Çölde gece ile gündüz arasındaki fark da büyüktür. Chihuahua Çölü'nde gündüz otuz yedi dereceyi aşabilir, gece ise sıfırın altına düşebilir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Neden? Çünkü çölde ısıyı tutan nem ve bulut azdır. Bu yüzden geceleri hızla soğur.",
        "spoken": "Neden? Çünkü çölde ısıyı tutan nem ve bulut azdır. Bu yüzden geceleri hızla soğur.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Gündüz kızar, gece donarım. Ben çölde kalsam ya erirdim ya da pilim donardı!",
        "spoken": "Gündüz kızar, gece donarım. Ben çölde kalsam ya erirdim ya da pilim donardı!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Çöl hayvanlarının ilk sırrı: gece çalışmak! Çoğu gececidir; sıcak gündüzleri uyuyarak geçirir, geceleri avlanır.",
        "spoken": "Çöl hayvanlarının ilk sırrı: gece çalışmak! Çoğu gececidir; sıcak gündüzleri uyuyarak geçirir, geceleri avlanır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Birçoğu da toprağa kazdığı serin yuvalarda sıcaktan saklanır.",
        "spoken": "Birçoğu da toprağa kazdığı serin yuvalarda sıcaktan saklanır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Milli Parklar Servisi'ne göre çöl şafakta hayatla dolar, öğleye doğru ise sessizleşir.",
        "spoken": "Milli Parklar Servisi'ne göre çöl şafakta hayatla dolar, öğleye doğru ise sessizleşir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l14",
        "display": "İkinci sır: suyu yiyecekten almak. Çöl tilkisinin böbrekleri, yediği besinden yeterince su tutar.",
        "spoken": "İkinci sır: suyu yiyecekten almak. Çöl tilkisinin böbrekleri, yediği besinden yeterince su tutar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l15",
        "display": "Yol koşucusu denen kuş da suyunu besininden alır.",
        "spoken": "Yol koşucusu denen kuş da suyunu besininden alır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Üçüncü sır: kulaklar! Çöl tavşanının uzun kulaklarında ısıyı dışarı veren kan damarları vardır. Kulakları bir radyatör gibidir!",
        "spoken": "Üçüncü sır: kulaklar! Çöl tavşanının uzun kulaklarında ısıyı dışarı veren kan damarları vardır. Kulakları bir radyatör gibidir!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l17",
        "display": "Benim de radyatörüm var: fan. Ama o kulaklarım kadar sevimli değil!",
        "spoken": "Benim de radyatörüm var: fan. Ama o kulaklarım kadar sevimli değil!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l18",
        "display": "Peki develer? Pek çok kişi deve hörgücünde su depolandığını sanır. Ama bu doğru değil: Hörgüç yağ depolar!",
        "spoken": "Peki develer? Pek çok kişi deve hörgücünde su depolandığını sanır. Ama bu doğru değil: Hörgüç yağ depolar!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "National Geographic'e göre tek hörgüçlü develer vücut ağırlıklarının yüzde 30'una kadarını zarar görmeden kaybedebilir.",
        "spoken": "Neşınıl Ciyogrefik'e göre tek hörgüçlü develer vücut ağırlıklarının yüzde otuzuna kadarını zarar görmeden kaybedebilir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Çöl kaplumbağası ise vücut ağırlığının yüzde 40'ına kadar suyu mesanesinde saklayabilir!",
        "spoken": "Çöl kaplumbağası ise vücut ağırlığının yüzde kırkına kadar suyu mesanesinde saklayabilir!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Bitkiler de usta. Kaktüslerin sığ ama geniş yayılan kökleri vardır; yağmur yağınca suyu hızla emer ve hücrelerinde saklarlar.",
        "spoken": "Bitkiler de usta. Kaktüslerin sığ ama geniş yayılan kökleri vardır; yağmur yağınca suyu hızla emer ve hücrelerinde saklarlar.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Büyük bir saguaro kaktüsü yüzlerce litre su tutabilen canlı bir depodur.",
        "spoken": "Büyük bir saguaro kaktüsü yüzlerce litre su tutabilen canlı bir depodur.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Mesquite ağacının kökleri ise yerin 61 metreden daha derinindeki suya ulaşabilir!",
        "spoken": "Meskit ağacının kökleri ise yerin altmış bir metreden daha derinindeki suya ulaşabilir!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Dikenler de bitkileri, onları yemek isteyen hayvanlardan korur.",
        "spoken": "Dikenler de bitkileri, onları yemek isteyen hayvanlardan korur.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Güneşli bir günde iki tabağa birer buz küpü koy. Birini güneşe bırak, diğerinin üstüne ters bir bardak kapat ve gölgeye koy.",
        "spoken": "Şimdi sıra sende! Güneşli bir günde iki tabağa birer buz küpü koy. Birini güneşe bırak, diğerinin üstüne ters bir bardak kapat ve gölgeye koy.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l26",
        "display": "Hangisi daha çabuk eriyor? Gölgedeki yuva, çöl hayvanlarının saklandığı serin yuvalar gibidir.",
        "spoken": "Hangisi daha çabuk eriyor? Gölgedeki yuva, çöl hayvanlarının saklandığı serin yuvalar gibidir.",
        "factIds": [
          "f4"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l27",
        "display": "Bunu biliyor muydun? Bazı çöller sıcak değil, buz gibidir: Antarktika'nın neredeyse tamamı bir kutup çölüdür!",
        "spoken": "Bunu biliyor muydun? Bazı çöller sıcak değil, buz gibidir: Antarktika'nın neredeyse tamamı bir kutup çölüdür!",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l28",
        "display": "Hızlı soru! Deve hörgücünde ne depolar?",
        "spoken": "Hızlı soru! Deve hörgücünde ne depolar?",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l29",
        "display": "Düşün bakalım... Evet: yağ, su değil!",
        "spoken": "Düşün bakalım... Evet: yağ, su değil!",
        "factIds": [
          "f7"
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
        "display": "Abone olmayı ve zili açmayı unutma. Bol su iç, serin kal!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bol su iç, serin kal!",
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
    "statement": "Çöller çok az yağış alan bölgelerdir; çöl, yılda en fazla 25 santimetre yağış alan kara parçasıdır.",
    "numbers": [
      "25"
    ]
  },
  {
    "id": "f2",
    "statement": "Bazı çöllerde gündüz sıcaklığı 54 santigrat dereceye kadar çıkar; bazı çöllerin kışları soğuktur ya da bütün yıl soğuktur; Antarktika'nın neredeyse tamamı bir kutup çölüdür.",
    "numbers": [
      "54"
    ]
  },
  {
    "id": "f3",
    "statement": "Chihuahua Çölü'nde gündüz sıcaklığı 37 santigrat dereceyi aşabilirken gece sıcaklığı donma noktası olan 0 derecenin altına düşebilir; çöller geceleri nem ve bulutların sağladığı yalıtım olmadığı için hızla soğur.",
    "numbers": [
      "37",
      "0"
    ]
  },
  {
    "id": "f4",
    "statement": "Çöl hayvanlarının çoğu gececidir; sıcak günleri uyuyarak geçirir, geceleri avlanır ve yiyecek arar; birçoğu sıcaktan yere kazdıkları serin yuvalarda korunur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Çöl tilkisinin böbrekleri yediği besinden yeterince su tutar; yol koşucusu kuşu suyunu besininden alır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Çöl tavşanının uzun kulaklarında ısı yayan kan damarları vardır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Develer hörgüçlerinde su depolamaz; hörgüç yağ depolar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Tek hörgüçlü develer vücut ağırlıklarının yüzde 30'una kadarını zarar görmeden kaybedebilir.",
    "numbers": [
      "30"
    ]
  },
  {
    "id": "f9",
    "statement": "Çöl kaplumbağası vücut ağırlığının yüzde 40'ına kadar suyu mesanesinde depolayabilir.",
    "numbers": [
      "40"
    ]
  },
  {
    "id": "f10",
    "statement": "Kaktüs gibi bazı çöl bitkilerinin sığ, geniş yayılan kökleri vardır; suyu hızla emip hücrelerinde depolarlar; büyük bir saguaro yüzlerce litre su tutabilen canlı bir depodur.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Mesquite ağacının kökleri yerin 61 metreden daha derinindeki suya ulaşabilir.",
    "numbers": [
      "61"
    ]
  },
  {
    "id": "f12",
    "statement": "Mesquite, saguaro ve birçok çöl bitkisinin onları otçul hayvanlardan koruyan dikenleri vardır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Çöl şafakta hayatla dolar, öğleye doğru hayvanlar sıcaktan korunmak için saklanınca sessizleşir.",
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
