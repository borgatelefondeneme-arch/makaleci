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
        "display": "Koşuyorsun, zıplıyorsun, düşüp kalkıyorsun. Bütün bu yükü taşıyan şey içinde gizli: iskeletin!",
        "spoken": "Koşuyorsun, zıplıyorsun, düşüp kalkıyorsun. Bütün bu yükü taşıyan şey içinde gizli: iskeletin!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Kemikler nasıl bu kadar güçlü? Ve kırılınca nasıl kendi kendine iyileşir?",
        "spoken": "Kemikler nasıl bu kadar güçlü? Ve kırılınca nasıl kendi kendine iyileşir?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün kemiklerinin içine bakıyoruz!",
        "spoken": "Bugün kemiklerinin içine bakıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Kemikler ne işe yarar? Neyden yapılmıştır? Ve onları nasıl güçlü tutarız?",
        "spoken": "Üç sorumuz var. Kemikler ne işe yarar? Neyden yapılmıştır? Ve onları nasıl güçlü tutarız?",
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
        "display": "KidsHealth'e göre kemikler vücudumuza destek olur ve biçimini oluşturur.",
        "spoken": "Kids Helt'e göre kemikler vücudumuza destek olur ve biçimini oluşturur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Aynı zamanda bir kalkandır: kafatası beyni korur, kaburgalar ise kalbi ve akciğerleri saran bir kafes oluşturur.",
        "spoken": "Aynı zamanda bir kalkandır: kafatası beyni korur, kaburgalar ise kalbi ve akciğerleri saran bir kafes oluşturur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Kaslar kemikleri çeker ve biz hareket ederiz.",
        "spoken": "Kaslar kemikleri çeker ve biz hareket ederiz.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l9",
        "display": "Ama kemiklerin gizli görevleri de var. Kan hücrelerinin çoğu, kemiklerin içindeki yumuşak kemik iliğinde yapılır.",
        "spoken": "Ama kemiklerin gizli görevleri de var. Kan hücrelerinin çoğu, kemiklerin içindeki yumuşak kemik iliğinde yapılır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Kemikler bir de kalsiyum deposudur; vücudun başka yerlerinin ihtiyacı olunca kana kalsiyum verirler.",
        "spoken": "Kemikler bir de kalsiyum deposudur; vücudun başka yerlerinin ihtiyacı olunca kana kalsiyum verirler.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Benim iskeletim metal. Ama içinde kan hücresi üretmiyor; olsa olsa biraz pas!",
        "spoken": "Benim iskeletim metal. Ama içinde kan hücresi üretmiyor; olsa olsa biraz pas!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Peki kemik neden hem sert hem dayanıklı? Kolajen denen bir protein bir çatı kurar; kalsiyum fosfat denen mineral de onu sertleştirir.",
        "spoken": "Peki kemik neden hem sert hem dayanıklı? Kolajen denen bir protein bir çatı kurar; kalsiyum fosfat denen mineral de onu sertleştirir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Kemiğin dışında kompakt kemik vardır: katı ve serttir. İçinden kan damarları ve sinirler taşıyan kanallar geçer.",
        "spoken": "Kemiğin dışında kompakt kemik vardır: katı ve serttir. İçinden kan damarları ve sinirler taşıyan kanallar geçer.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "İçeride ise süngere benzeyen süngerimsi kemik bulunur.",
        "spoken": "İçeride ise süngere benzeyen süngerimsi kemik bulunur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l15",
        "display": "Kemik canlı bir dokudur ve vücut onu sürekli yeniler. Osteoblast denen hücreler yeni kemik yapar ve hasarı onarır.",
        "spoken": "Kemik canlı bir dokudur ve vücut onu sürekli yeniler. Osteoblast denen hücreler yeni kemik yapar ve hasarı onarır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Osteoklast denen hücreler ise eski kemiği yıkar ve biçimlendirir. Yıkan ve yapan iki ekip, kemiği hep yenileyen bir inşaat gibi.",
        "spoken": "Osteoklast denen hücreler ise eski kemiği yıkar ve biçimlendirir. Yıkan ve yapan iki ekip, kemiği hep yenileyen bir inşaat gibi.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Çocukların kemiklerinde büyüme plakları denen büyüme bölgeleri vardır. Boyunun uzaması buralarda olur.",
        "spoken": "Çocukların kemiklerinde büyüme plakları denen büyüme bölgeleri vardır. Boyunun uzaması buralarda olur.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l18",
        "display": "Kızlar daha erken olgunlaştığı için büyüme plakaları da daha erken sert kemiğe dönüşür.",
        "spoken": "Kızlar daha erken olgunlaştığı için büyüme plakaları da daha erken sert kemiğe dönüşür.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Kafatası da doğumda tek parça değildir: birbirine kaynayan kemik plakalardan oluşur.",
        "spoken": "Kafatası da doğumda tek parça değildir: birbirine kaynayan kemik plakalardan oluşur.",
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
        "id": "l20",
        "display": "İki kemiğin buluştuğu yere eklem denir. Eklemler sayesinde iskelet esnektir; onlar olmasa hareket edemezdik.",
        "spoken": "İki kemiğin buluştuğu yere eklem denir. Eklemler sayesinde iskelet esnektir; onlar olmasa hareket edemezdik.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l21",
        "display": "Kemikleri birbirine bağ denen lifli kayışlar bağlar. Kasları kemiğe ise kiriş denen ip gibi yapılar bağlar. Eklemleri de esnek kıkırdak korur.",
        "spoken": "Kemikleri birbirine bağ denen lifli kayışlar bağlar. Kasları kemiğe ise kiriş denen ip gibi yapılar bağlar. Eklemleri de esnek kıkırdak korur.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l22",
        "display": "Dizin ve dirseğin menteşe eklemdir: kapı menteşesi gibi tek yönde hareket eder.",
        "spoken": "Dizin ve dirseğin menteşe eklemdir: kapı menteşesi gibi tek yönde hareket eder.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l23",
        "display": "Kemikleri güçlü tutmanın yolu: kalsiyum, D vitamini ve hareket. İngiltere Ulusal Sağlık Servisi NHS'e göre vücut, deriye düşen güneş ışığıyla D vitamini üretir.",
        "spoken": "Kemikleri güçlü tutmanın yolu: kalsiyum, D vitamini ve hareket. İngiltere Ulusal Sağlık Servisi, En Eyç Es'e göre vücut, deriye düşen güneş ışığıyla D vitamini üretir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l24",
        "display": "D vitamini, vücuttaki kalsiyumun düzenlenmesine yardım eder.",
        "spoken": "D vitamini, vücuttaki kalsiyumun düzenlenmesine yardım eder.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l25",
        "display": "CDC'ye göre 6–17 yaş arasındakiler her gün en az 60 dakika hareket etmeli. Koşmak ve zıplamak gibi kemik güçlendiren etkinlikler de haftada en az 3 gün olmalı.",
        "spoken": "Si Di Si'ye göre altı ile on yedi yaş arasındakiler her gün en az altmış dakika hareket etmeli. Koşmak ve zıplamak gibi kemik güçlendiren etkinlikler de haftada en az üç gün olmalı.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l26",
        "display": "Kemik kırılırsa ne olur? KidsHealth'e göre kırık kemikler, özellikle çocuklarda, çok iyi iyileşir.",
        "spoken": "Kemik kırılırsa ne olur? Kids Helt'e göre kırık kemikler, özellikle çocuklarda, çok iyi iyileşir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Kırık uçlar arasında kallus denen yeni bir doku oluşur. Başta yumuşaktır, haftalar içinde sertleşir. Tam iyileşme birkaç ay sürebilir.",
        "spoken": "Kırık uçlar arasında kallus denen yeni bir doku oluşur. Başta yumuşaktır, haftalar içinde sertleşir. Tam iyileşme birkaç ay sürebilir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "Şimdi sıra sende! Kolunu bük ve aç; sonra bileğini döndür. Hangi eklem tek yönde, hangisi çok yönde hareket ediyor?",
        "spoken": "Şimdi sıra sende! Kolunu bük ve aç; sonra bileğini döndür. Hangi eklem tek yönde, hangisi çok yönde hareket ediyor?",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l29",
        "display": "Sonra bu hafta kaç gün koştuğunu ya da zıpladığını bir tabloya yaz. Haftada üç güne ulaşabilecek misin?",
        "spoken": "Sonra bu hafta kaç gün koştuğunu ya da zıpladığını bir tabloya yaz. Haftada üç güne ulaşabilecek misin?",
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
        "display": "Bunu biliyor muydun? Çocukların kemikleri daha yumuşak olduğu için, tamamen kırılmaktan çok bükülme eğilimindedir.",
        "spoken": "Bunu biliyor muydun? Çocukların kemikleri daha yumuşak olduğu için, tamamen kırılmaktan çok bükülme eğilimindedir.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l31",
        "display": "Hızlı soru! Yeni kemik yapan hücrelerin adı neydi?",
        "spoken": "Hızlı soru! Yeni kemik yapan hücrelerin adı neydi?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l32",
        "display": "Düşün bakalım... Evet: osteoblastlar!",
        "spoken": "Düşün bakalım... Evet: osteoblastlar!",
        "factIds": [
          "f5"
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
        "display": "Abone olmayı ve zili açmayı unutma. Ben de eklemlerimi yağlamaya gidiyorum!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de eklemlerimi yağlamaya gidiyorum!",
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
    "statement": "Kemikler vücudumuza destek olur ve biçimini oluşturur; kafatası beyni korur; kaburgalar kalbi ve akciğerleri barındıran bir kafes oluşturur; kaslar eklemleri çekerek hareket etmemizi sağlar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Kemikler kalsiyum depolar ve gerektiğinde bir kısmını kana verir; vücudun kan hücrelerinin çoğu kemiklerin içindeki yumuşak kemik iliğinde yapılır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Kemikler kolajen adlı bir proteinden yapılmış bir çatı ile kalsiyum fosfat adlı bir mineralden oluşur.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Kompakt kemik kemiğin katı, sert dış kısmıdır; içinden kan damarları ve sinirler taşıyan delikler ve kanallar geçer; süngere benzeyen süngerimsi kemik kompakt kemiğin içindedir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Vücut kemiklerin canlı dokusunu sürekli yeniler ve yeniden biçimlendirir; osteoblastlar yeni kemik yapar ve hasarı onarır; osteoklastlar kemiği yıkar ve biçimlendirir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Çocukların ve genç ergenlerin kemiklerinde büyüme plakları denen 'büyüme bölgeleri' vardır; kızlar daha erken olgunlaştığı için büyüme plakları daha erken sert kemiğe dönüşür.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Kafatasının kubbesi, doğum sırasında biraz hareket eden ve kafatası büyümesini tamamlayınca birbirine kaynayan kemik plakalardan oluşur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Eklemler iki kemiğin buluştuğu yerdir ve iskeleti esnek yapar; kemikler birbirine bağ denen uzun, lifli kayışlarla bağlanır; kıkırdak eklemlerde kemikleri destekleyen ve koruyan esnek bir maddedir; kaslar kemiğe kiriş denen ip gibi yapılarla bağlanır; menteşe eklemler dizde ve dirsekte olduğu gibi tek yönde hareket sağlar.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "D vitamini vücuttaki kalsiyum ve fosfat miktarını düzenler; vücut, açık havada deriye düşen doğrudan güneş ışığıyla D vitamini üretir; kalsiyum eksikliği çocuklarda raşitizme yol açabilir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "6–17 yaş arasındaki çocuk ve gençler her gün en az 60 dakika hareketli olmalıdır; zıplama ya da koşma gibi kemik güçlendiren etkinlikler haftada en az 3 gün yer almalıdır.",
    "numbers": [
      "6",
      "17",
      "60",
      "3"
    ]
  },
  {
    "id": "f11",
    "statement": "Kırık kemiklerin, özellikle çocuklarda, iyileşme yeteneği çok yüksektir; kırık uçları kallus denen yeni dokuyla birleşir; kallus başta yumuşaktır, sonraki haftalarda sertleşir; kırıkların çoğu alçı, atel ya da destekle tedavi edilir; tam iyileşme genellikle birkaç ay sürer; çocukların kemikleri daha yumuşak olduğu için tamamen kırılmaktan çok bükülür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Sardalya gibi kılçığıyla yenen balıklar kalsiyum kaynağıdır; kalsiyum kemikleri yapmaya ve dişleri sağlıklı tutmaya yardım eder.",
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
