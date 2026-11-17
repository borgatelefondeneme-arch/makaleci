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
        "display": "Yazın güneş akşam geç saatlere kadar batmaz. Kışın ise daha okuldan dönerken hava kararır. Neden?",
        "spoken": "Yazın güneş akşam geç saatlere kadar batmaz. Kışın ise daha okuldan dönerken hava kararır. Neden?",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l2",
        "display": "Ve neden bir yıl içinde dört mevsim yaşıyoruz?",
        "spoken": "Ve neden bir yıl içinde dört mevsim yaşıyoruz?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Dünya'mızın uzaydaki dansına bakıyoruz!",
        "spoken": "Bugün Dünya'mızın uzaydaki dansına bakıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Mevsimlere ne yol açar? Güneş'e yakınlık işe karışır mı? Ve günler neden uzayıp kısalır?",
        "spoken": "Üç sorumuz var. Mevsimlere ne yol açar? Güneş'e yakınlık işe karışır mı? Ve günler neden uzayıp kısalır?",
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
        "display": "NASA'ya göre mevsimlerin sırrı tek bir kelimede saklı: eğiklik. Dünya'nın ekseni dimdik durmaz, yana yatıktır.",
        "spoken": "Nasa'ya göre mevsimlerin sırrı tek bir kelimede saklı: eğiklik. Dünya'nın ekseni dimdik durmaz, yana yatıktır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Eksen, Dünya'nın kuzey ve güney kutuplarından geçen hayali çizgidir. Dünya bu çizginin çevresinde döner ve her gün bir tam tur atar.",
        "spoken": "Eksen, Dünya'nın kuzey ve güney kutuplarından geçen hayali çizgidir. Dünya bu çizginin çevresinde döner ve her gün bir tam tur atar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l8",
        "display": "Benim de bir eksenim var: başımı sağa sola çeviriyorum. Ama mevsim yapamıyorum, sadece baş dönmesi!",
        "spoken": "Benim de bir eksenim var: başımı sağa sola çeviriyorum. Ama mevsim yapamıyorum, sadece baş dönmesi!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Dünya bir yandan da Güneş'in çevresinde dolanır. Bu yolculuk boyunca eğik ekseni hep aynı yöne bakar.",
        "spoken": "Dünya bir yandan da Güneş'in çevresinde dolanır. Bu yolculuk boyunca eğik ekseni hep aynı yöne bakar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Bu yüzden yılın bir bölümünde Kuzey Yarım Küre Güneş'e doğru eğilir, diğer bölümünde Güneş'ten uzağa.",
        "spoken": "Bu yüzden yılın bir bölümünde Kuzey Yarım Küre Güneş'e doğru eğilir, diğer bölümünde Güneş'ten uzağa.",
        "factIds": [
          "f2",
          "f4",
          "f5"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Haziran civarında Kuzey Kutbu Güneş'e doğru eğiktir. Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir.",
        "spoken": "Haziran civarında Kuzey Kutbu Güneş'e doğru eğiktir. Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "İşte bu yüzden orada yaz olur. Türkiye de Kuzey Yarım Küre'de, bizde de yaz olur.",
        "spoken": "İşte bu yüzden orada yaz olur. Türkiye de Kuzey Yarım Küre'de, bizde de yaz olur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "National Geographic'e göre Güneş'e doğru eğik yarım küre daha fazla saat gün ışığı alır. Günler uzar!",
        "spoken": "Neşınıl Ciyogrefik'e göre Güneş'e doğru eğik yarım küre daha fazla saat gün ışığı alır. Günler uzar!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Aralık'ta ise Kuzey Yarım Küre Güneş'ten uzağa eğiktir. Daha az güneş ışığı ve daha az gün ışığı saati alır: kış gelir.",
        "spoken": "Aralık'ta ise Kuzey Yarım Küre Güneş'ten uzağa eğiktir. Daha az güneş ışığı ve daha az gün ışığı saati alır: kış gelir.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Peki Güney Yarım Küre? Orada mevsimler bizimkinin tersidir. Biz kışın üşürken Güney Yarım Küre'de yaz yaşanır.",
        "spoken": "Peki Güney Yarım Küre? Orada mevsimler bizimkinin tersidir. Biz kışın üşürken Güney Yarım Küre'de yaz yaşanır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Yani Aralık'ta orada biri plajda dondurma yiyebilir. Ben kışın sadece şarjımı yerim!",
        "spoken": "Yani Aralık'ta orada biri plajda dondurma yiyebilir. Ben kışın sadece şarjımı yerim!",
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
        "id": "l17",
        "display": "Pek çok kişi yazın sıcak olmasının nedeninin Dünya'nın Güneş'e yaklaşması olduğunu sanır.",
        "spoken": "Pek çok kişi yazın sıcak olmasının nedeninin Dünya'nın Güneş'e yaklaşması olduğunu sanır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Ama NASA'ya göre Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir.",
        "spoken": "Ama Nasa'ya göre Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Yani biz Güneş'e en yakınken kış yaşıyoruz! Demek ki mevsimlerin nedeni uzaklık değil, eğiklik.",
        "spoken": "Yani biz Güneş'e en yakınken kış yaşıyoruz! Demek ki mevsimlerin nedeni uzaklık değil, eğiklik.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Yılın dönüm noktaları da var. Yaz, 20 ya da 21 Haziran'daki yaz gündönümüyle başlar. Bu, yılın en uzun gündüzüdür.",
        "spoken": "Yılın dönüm noktaları da var. Yaz, yirmi ya da yirmi bir Haziran'daki yaz gündönümüyle başlar. Bu, yılın en uzun gündüzüdür.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Kış gündönümü ise gündüzün en kısa olduğu gündür.",
        "spoken": "Kış gündönümü ise gündüzün en kısa olduğu gündür.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l22",
        "display": "İlkbahar ve sonbahar ekinoksla başlar: gece ile gündüzün eşit olduğu günler. İlkbahar ekinoksu 20 ya da 21 Mart, sonbahar ekinoksu 22 ya da 23 Eylül'dedir.",
        "spoken": "İlkbahar ve sonbahar ekinoksla başlar: gece ile gündüzün eşit olduğu günler. İlkbahar ekinoksu yirmi ya da yirmi bir Mart, sonbahar ekinoksu yirmi iki ya da yirmi üç Eylül'dedir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Kuzeye gittikçe fark büyür. Haziran ortasında Finlandiya'nın Helsinki kentinde 18,5 saat gün ışığı olur.",
        "spoken": "Kuzeye gittikçe fark büyür. Haziran ortasında Finlandiya'nın Helsinki kentinde on sekiz buçuk saat gün ışığı olur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Yunanistan'ın Atina kentinde ise Haziran'da 14,5, Aralık'ta 9,5 saat gün ışığı vardır.",
        "spoken": "Yunanistan'ın Atina kentinde ise Haziran'da on dört buçuk, Aralık'ta dokuz buçuk saat gün ışığı vardır.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Şimdi sıra sende! Karanlık bir odada bir el fenerini bir kâğıda tam dik tut, sonra yana yatırarak tut.",
        "spoken": "Şimdi sıra sende! Karanlık bir odada bir el fenerini bir kâğıda tam dik tut, sonra yana yatırarak tut.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l26",
        "display": "Işık lekesi nasıl değişiyor? Hangisi daha küçük ve parlak? Güneş ışınlarının doğrudan gelmesi de buna benzer. Ama Güneş'e asla doğrudan bakma!",
        "spoken": "Işık lekesi nasıl değişiyor? Hangisi daha küçük ve parlak? Güneş ışınlarının doğrudan gelmesi de buna benzer. Ama Güneş'e asla doğrudan bakma!",
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
        "display": "Bunu biliyor muydun? Alaska'daki Barrow kentinde Mayıs ortasından Ağustos başına kadar gün boyu hava aydınlık kalır.",
        "spoken": "Bunu biliyor muydun? Alaska'daki Barrow kentinde Mayıs ortasından Ağustos başına kadar gün boyu hava aydınlık kalır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l28",
        "display": "Kasım ortasından Ocak'a kadar ise tam karanlık olur. Orada uyku saatini ayarlamak zor olmalı!",
        "spoken": "Kasım ortasından Ocak'a kadar ise tam karanlık olur. Orada uyku saatini ayarlamak zor olmalı!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l29",
        "display": "Hızlı soru! Mevsimlere ne yol açar: Güneş'e uzaklık mı, eksenin eğikliği mi?",
        "spoken": "Hızlı soru! Mevsimlere ne yol açar: Güneş'e uzaklık mı, eksenin eğikliği mi?",
        "factIds": [
          "f1",
          "f8"
        ]
      },
      {
        "id": "l30",
        "display": "Düşün bakalım... Evet: eksenin eğikliği!",
        "spoken": "Düşün bakalım... Evet: eksenin eğikliği!",
        "factIds": [
          "f1"
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
        "display": "Abone olmayı ve zili açmayı unutma. Hangi mevsimdeysen tadını çıkar!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Hangi mevsimdeysen tadını çıkar!",
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
    "statement": "Mevsimlere Dünya'nın eğik ekseni yol açar; Dünya'nın ekseni dimdik durmaz; Dünya yörünge düzlemine göre eksenine eğiktir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Dünya Güneş'in çevresinde dolanırken eğik ekseni hep aynı yöne bakar.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Dünya bu eksen çevresinde döner ve her gün bir tam tur atar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Kuzey Kutbu Güneş'e doğru eğikken (Haziran civarı) Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir ve orada yaz olur.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bir yarım küre Güneş'ten uzağa eğikken daha az güneş ışığı alır ve kış olur.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Güneş'e doğru eğik yarım küre daha fazla gün ışığı saati alır; Aralık'ta Güneş'ten uzağa eğik olan Kuzey Yarım Küre daha az gün ışığı saati alır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Kuzey Yarım Küre'deki mevsimler Güney Yarım Küre'dekilerin tersidir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Pek çok kişi yazın Dünya'nın Güneş'e daha yakın olduğunu sanır; oysa Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir; yani uzaklık mevsimlerin nedeni değildir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Yaz 20 ya da 21 Haziran'daki yaz gündönümüyle başlar; bu, yılın en çok gün ışığı olan günüdür; kış gündönümü en kısa gündüzün olduğu gündür.",
    "numbers": [
      "20",
      "21"
    ]
  },
  {
    "id": "f10",
    "statement": "İlkbahar ve sonbahar, gece ile gündüzün eşit olduğu ekinokslarla başlar; ilkbahar ekinoksu 20 ya da 21 Mart'ta, sonbahar ekinoksu 22 ya da 23 Eylül'dedir.",
    "numbers": [
      "20",
      "21",
      "22",
      "23"
    ]
  },
  {
    "id": "f11",
    "statement": "Helsinki'de Haziran ortasında 18,5 saat gün ışığı olur; Atina'da Haziran'da 14,5, Aralık'ta 9,5 saat gün ışığı vardır.",
    "numbers": [
      "18.5",
      "14.5",
      "9.5"
    ]
  },
  {
    "id": "f12",
    "statement": "Alaska'daki Barrow'da Mayıs ortasından Ağustos başına kadar gün boyu aydınlık olur; Kasım ortasından Ocak'a kadar ise tam karanlık hüküm sürer.",
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
