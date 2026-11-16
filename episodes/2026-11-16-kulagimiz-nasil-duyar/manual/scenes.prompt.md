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
        "display": "Bir arkadaşın adını fısıldıyor, sen hemen dönüp bakıyorsun. Bu kadar küçük bir sesi nasıl yakaladın?",
        "spoken": "Bir arkadaşın adını fısıldıyor, sen hemen dönüp bakıyorsun. Bu kadar küçük bir sesi nasıl yakaladın?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Ses kulağına nasıl girer? Ve beynin onu nasıl anlar?",
        "spoken": "Ses kulağına nasıl girer? Ve beynin onu nasıl anlar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir ses dalgasının peşinden kulağının içine giriyoruz!",
        "spoken": "Bugün bir ses dalgasının peşinden kulağının içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Ses nedir? Kulağın içinde neler olur? Ve kulaklarımızı nasıl koruruz?",
        "spoken": "Üç sorumuz var. Ses nedir? Kulağın içinde neler olur? Ve kulaklarımızı nasıl koruruz?",
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
        "display": "ABD Ulusal Park Servisi'ne göre ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler.",
        "spoken": "ABD Ulusal Park Servisi'ne göre ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Sesin iki önemli özelliği var. Frekans, dalganın saniyede kaç kez tekrarlandığıdır; sesi ince ya da kalın yapar.",
        "spoken": "Sesin iki önemli özelliği var. Frekans, dalganın saniyede kaç kez tekrarlandığıdır; sesi ince ya da kalın yapar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Genlik ise dalganın gücüdür; sesin yüksekliğini belirler. Desibel denen birimle ölçülür.",
        "spoken": "Genlik ise dalganın gücüdür; sesin yüksekliğini belirler. Desibel denen birimle ölçülür.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Normal işiten insanlar 20 ile 20.000 hertz arasındaki sesleri duyabilir.",
        "spoken": "Normal işiten insanlar yirmi ile yirmi bin hertz arasındaki sesleri duyabilir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Benim mikrofonum da bu aralığı duyuyor. Ama kulak memesi takmayı unutmuşlar!",
        "spoken": "Benim mikrofonum da bu aralığı duyuyor. Ama kulak memesi takmayı unutmuşlar!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Yolculuk dış kulakta başlar. KidsHealth'e göre dış kulak sesleri toplar ve kulak kanalına yönlendirir; ses dalgaları kanal boyunca kulak zarına ulaşır.",
        "spoken": "Yolculuk dış kulakta başlar. Kids Helt'e göre dış kulak sesleri toplar ve kulak kanalına yönlendirir; ses dalgaları kanal boyunca kulak zarına ulaşır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Kulak zarı ses dalgalarıyla titreşir ve titreşimi orta kulaktaki üç minik kemiğe iletir: çekiç, örs ve üzengi.",
        "spoken": "Kulak zarı ses dalgalarıyla titreşir ve titreşimi orta kulaktaki üç minik kemiğe iletir: çekiç, örs ve üzengi.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Üzengi, vücudundaki en küçük kemiktir!",
        "spoken": "Üzengi, vücudundaki en küçük kemiktir!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Bu kemikler titreşimi güçlendirir ve salyangoz biçimli, sıvı dolu bir yapıya gönderir: koklea.",
        "spoken": "Bu kemikler titreşimi güçlendirir ve salyangoz biçimli, sıvı dolu bir yapıya gönderir: koklea.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre kokleanın içinde tüy hücreleri denen duyu hücreleri vardır. Sıvıdaki dalgayla birlikte hareket ederler.",
        "spoken": "Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'ye göre kokleanın içinde tüy hücreleri denen duyu hücreleri vardır. Sıvıdaki dalgayla birlikte hareket ederler.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Kokleanın geniş ucundaki tüy hücreleri ince sesleri, merkeze yakın olanlar kalın sesleri algılar.",
        "spoken": "Kokleanın geniş ucundaki tüy hücreleri ince sesleri, merkeze yakın olanlar kalın sesleri algılar.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l17",
        "display": "Tüy hücreleri hareket edince içlerine kimyasallar akar ve bir elektrik sinyali oluşur. İşitme siniri bu sinyali beyne taşır; beyin de onu tanıdığımız bir sese dönüştürür.",
        "spoken": "Tüy hücreleri hareket edince içlerine kimyasallar akar ve bir elektrik sinyali oluşur. İşitme siniri bu sinyali beyne taşır; beyin de onu tanıdığımız bir sese dönüştürür.",
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
        "id": "l18",
        "display": "İşte kötü haber: NIH'ye göre insanın tüy hücreleri bir kez hasar görürse yeniden çıkmaz.",
        "spoken": "İşte kötü haber: En Ay Eyç'ye göre insanın tüy hücreleri bir kez hasar görürse yeniden çıkmaz.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Gürültünün yol açtığı işitme kaybının çoğu, bu hücrelerin hasar görüp ölmesinden kaynaklanır.",
        "spoken": "Gürültünün yol açtığı işitme kaybının çoğu, bu hücrelerin hasar görüp ölmesinden kaynaklanır.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "70 desibel ve altındaki sesler uzun süre dinlense bile genellikle zarar vermez. Ama 85 desibel ve üstüne uzun ya da sık sık maruz kalmak işitmeye zarar verebilir.",
        "spoken": "Yetmiş desibel ve altındaki sesler uzun süre dinlense bile genellikle zarar vermez. Ama seksen beş desibel ve üstüne uzun ya da sık sık maruz kalmak işitmeye zarar verebilir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Karşılaştırma için: normal konuşma 60–70, sirenler 110–129, havai fişek gösterisi ise 140–160 desibele kadar çıkabilir.",
        "spoken": "Karşılaştırma için: normal konuşma altmış ile yetmiş, sirenler yüz on ile yüz yirmi dokuz, havai fişek gösterisi ise yüz kırk ile yüz altmış desibele kadar çıkabilir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Ses ne kadar yüksekse, hasar o kadar çabuk oluşur.",
        "spoken": "Ses ne kadar yüksekse, hasar o kadar çabuk oluşur.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l23",
        "display": "Korunmak kolay: kulaklıkla dinlerken sesi kıs. Gürültülü bir yerde kulak tıkacı kullan. Gürültüyü azaltamıyorsan ondan uzaklaş.",
        "spoken": "Korunmak kolay: kulaklıkla dinlerken sesi kıs. Gürültülü bir yerde kulak tıkacı kullan. Gürültüyü azaltamıyorsan ondan uzaklaş.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Kulağın bir görevi daha var: dengeni korur. İç kulaktaki yarım daire kanalları, başının ne zaman döndüğünü beynine bildirir.",
        "spoken": "Kulağın bir görevi daha var: dengeni korur. İç kulaktaki yarım daire kanalları, başının ne zaman döndüğünü beynine bildirir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l25",
        "display": "Ben dönerken dengemi kaybetmem. Ama tekerleklerim kayarsa o başka!",
        "spoken": "Ben dönerken dengemi kaybetmem. Ama tekerleklerim kayarsa o başka!",
        "factIds": []
      },
      {
        "id": "l26",
        "display": "Şimdi sıra sende! Elini boğazına koy ve uzun bir ses çıkar. Hissettiğin titreşim, sesin kaynağıdır.",
        "spoken": "Şimdi sıra sende! Elini boğazına koy ve uzun bir ses çıkar. Hissettiğin titreşim, sesin kaynağıdır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l27",
        "display": "Sonra önce ince, sonra kalın bir ses çıkar. Titreşim nasıl değişiyor?",
        "spoken": "Sonra önce ince, sonra kalın bir ses çıkar. Titreşim nasıl değişiyor?",
        "factIds": [
          "f2"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l28",
        "display": "Bunu biliyor muydun? Gök gürültüsü 120 desibeli aşabilir; bu, kulakta acı hissettirecek kadar yüksek bir sestir.",
        "spoken": "Bunu biliyor muydun? Gök gürültüsü yüz yirmi desibeli aşabilir; bu, kulakta acı hissettirecek kadar yüksek bir sestir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l29",
        "display": "Hızlı soru! Vücudun en küçük kemiği hangisi?",
        "spoken": "Hızlı soru! Vücudun en küçük kemiği hangisi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l30",
        "display": "Düşün bakalım... Evet: kulağındaki üzengi kemiği!",
        "spoken": "Düşün bakalım... Evet: kulağındaki üzengi kemiği!",
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
        "display": "Abone olmayı ve zili açmayı unutma. Bu videoyu da çok yüksek sesle izleme!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bu videoyu da çok yüksek sesle izleme!",
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
    "statement": "Ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler; işitme, havadaki ses dalgalarını elektrik sinyallerine dönüştüren karmaşık adımlara dayanır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Frekans (perde), ses basınç dalgasının saniyede kaç kez tekrarlandığıdır; genlik, ses dalgalarının göreli gücüdür ve yükseklik olarak algılanır; desibel (dB) ile ölçülür.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Normal işiten insanlar 20 Hz ile 20.000 Hz arasındaki sesleri duyabilir.",
    "numbers": [
      "20",
      "20.000"
    ]
  },
  {
    "id": "f4",
    "statement": "Dış kulağın görevi sesleri toplayıp kulak kanalına yönlendirmektir; ses dalgaları kulak kanalından kulak zarına ulaşır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Kulak zarı gelen ses dalgalarıyla titreşir ve bu titreşimleri orta kulaktaki üç minik kemiğe gönderir: çekiç, örs ve üzengi; üzengi vücudun en küçük kemiğidir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Orta kulaktaki kemikler ses titreşimlerini güçlendirir ve salyangoz biçimli kokleaya gönderir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Baziler zarın üstündeki duyu hücreleri olan tüy hücreleri dalgayla hareket eder; salyangozun geniş ucundaki tüy hücreleri tiz sesleri, merkeze yakın olanlar pes sesleri algılar; hücrelere kimyasallar akar ve elektrik sinyali oluşur; işitme siniri bu sinyali beyne taşır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Kuş ve amfibilerin tersine insan tüy hücreleri yeniden çıkmaz; gürültüye bağlı işitme kaybının çoğu bu hücrelerin hasar görüp ölmesinden kaynaklanır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "70 dBA ve altındaki sesler uzun süre dinlense bile işitme kaybına yol açma olasılığı düşüktür; 85 dBA ve üstündeki seslere uzun ya da tekrarlı maruz kalmak işitme kaybına yol açabilir; ses ne kadar yüksekse hasar o kadar çabuk oluşur.",
    "numbers": [
      "70",
      "85"
    ]
  },
  {
    "id": "f10",
    "statement": "Normal konuşma 60–70 dBA, sirenler 110–129 dBA, havai fişek gösterisi 140–160 dBA düzeyindedir.",
    "numbers": [
      "60",
      "70",
      "110",
      "129",
      "140",
      "160"
    ]
  },
  {
    "id": "f11",
    "statement": "Telefonların, oyunların ve televizyonun sesi kısılmalı; gürültülü bir etkinlikte kulak tıkacı takılmalı; gürültü azaltılamıyorsa ondan uzaklaşılmalı.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Kulağın dengeye yardım eden bölümüne vestibüler sistem denir; yarım daire kanalları, birbirine aşağı yukarı dik açılarla dizilmiş üç sıvı dolu kanaldır ve başın ne zaman döndüğünü beyne bildirir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Gök gürültüsü 120 desibeli aşabilir; bu, insan kulağında acıya yol açacak kadar yüksektir.",
    "numbers": [
      "120"
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
