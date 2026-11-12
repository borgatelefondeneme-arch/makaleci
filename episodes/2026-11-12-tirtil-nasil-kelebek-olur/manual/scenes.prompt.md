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
        "display": "Minik bir tırtıl, birkaç hafta sonra kanatlanıp uçuyor. Üstelik bazı kelebekler binlerce kilometre uzağa göç ediyor!",
        "spoken": "Minik bir tırtıl, birkaç hafta sonra kanatlanıp uçuyor. Üstelik bazı kelebekler binlerce kilometre uzağa göç ediyor!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Bir tırtıl nasıl kanat çıkarır? Ve o kadar küçük bir kelebek nasıl bu kadar uzağa uçar?",
        "spoken": "Bir tırtıl nasıl kanat çıkarır? Ve o kadar küçük bir kelebek nasıl bu kadar uzağa uçar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün turuncu kanatlı bir yolcunun hikâyesini izliyoruz: monark kelebeği!",
        "spoken": "Bugün turuncu kanatlı bir yolcunun hikâyesini izliyoruz: monark kelebeği!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Bir kelebek hangi evrelerden geçer? Tırtılın vücudu nasıl korunur? Ve monarklar neden göç eder?",
        "spoken": "Üç sorumuz var. Bir kelebek hangi evrelerden geçer? Tırtılın vücudu nasıl korunur? Ve monarklar neden göç eder?",
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
        "display": "ABD Orman Servisi'ne göre monark kelebeğinin dört yaşam evresi vardır: yumurta, tırtıl, krizalit ve ergin kelebek.",
        "spoken": "A Be De Orman Servisi'ne göre monark kelebeğinin dört yaşam evresi vardır: yumurta, tırtıl, krizalit ve ergin kelebek.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bu dört evreli büyük değişime tam başkalaşım denir.",
        "spoken": "Bu dört evreli büyük değişime tam başkalaşım denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Ben de çok güncelleme aldım. Ama hiçbirinde kanat çıkmadı!",
        "spoken": "Ben de çok güncelleme aldım. Ama hiçbirinde kanat çıkmadı!",
        "factIds": []
      },
      {
        "id": "l9",
        "display": "Her şey bir yumurtayla başlar. Dişi monark, yumurtalarını süt otu denen bitkinin yapraklarının altına bırakır.",
        "spoken": "Her şey bir yumurtayla başlar. Dişi monark, yumurtalarını süt otu denen bitkinin yapraklarının altına bırakır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l10",
        "display": "Bir dişi ömrü boyunca 100 ile 300 arasında yumurta bırakır. Yumurtalar yaklaşık dört gün sonra açılır.",
        "spoken": "Bir dişi ömrü boyunca yüz ile üç yüz arasında yumurta bırakır. Yumurtalar yaklaşık dört gün sonra açılır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l11",
        "display": "Yumurtadan çıkan tırtılın ilk yemeği ne? Kendi yumurtasının kabuğu! Sonra süt otu yapraklarına geçer.",
        "spoken": "Yumurtadan çıkan tırtılın ilk yemeği ne? Kendi yumurtasının kabuğu! Sonra süt otu yapraklarına geçer.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Tırtıl yumurtadan çıktığında 1 santimetreden küçüktür. Yemeye yemeye yaklaşık 5 santimetreye kadar büyür.",
        "spoken": "Tırtıl yumurtadan çıktığında bir santimetreden küçüktür. Yemeye yemeye yaklaşık beş santimetreye kadar büyür.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Büyürken derisi dar gelir ve deri değiştirir. İki deri değiştirme arasındaki her evreye instar denir.",
        "spoken": "Büyürken derisi dar gelir ve deri değiştirir. İki deri değiştirme arasındaki her evreye instar denir.",
        "factIds": [
          "f4"
        ]
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l14",
        "display": "Yeterince büyüyen tırtıl, sert bir kılıfın içine girer. Bu evreye pupa ya da krizalit denir.",
        "spoken": "Yeterince büyüyen tırtıl, sert bir kılıfın içine girer. Bu evreye pupa ya da krizalit denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l15",
        "display": "Dışarıdan bakınca hiçbir şey olmuyor gibi görünür. Ama içeride, tırtılın vücudu kelebeğe dönüşmektedir.",
        "spoken": "Dışarıdan bakınca hiçbir şey olmuyor gibi görünür. Ama içeride, tırtılın vücudu kelebeğe dönüşmektedir.",
        "factIds": [
          "f1",
          "f5"
        ]
      },
      {
        "id": "l16",
        "display": "Orman Servisi'ne göre monark, en az beş günde pupadan ergin kelebeğe dönüşebilir.",
        "spoken": "Orman Servisi'ne göre monark, en az beş günde pupadan ergin kelebeğe dönüşebilir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Kelebeğin krizalitten çıkmasının da bilimsel bir adı var: eklozyon.",
        "spoken": "Kelebeğin krizalitten çıkmasının da bilimsel bir adı var: eklozyon.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l18",
        "display": "Ben de her sabah şarj istasyonumdan çıkıyorum. Ama kimse buna özel bir isim vermedi!",
        "spoken": "Ben de her sabah şarj istasyonumdan çıkıyorum. Ama kimse buna özel bir isim vermedi!",
        "factIds": []
      },
      {
        "id": "l19",
        "display": "Ergin kelebek artık çiğneyemez. Uzun, hortum gibi bir diliyle çiçeklerden nektar içer.",
        "spoken": "Ergin kelebek artık çiğneyemez. Uzun, hortum gibi bir diliyle çiçeklerden nektar içer.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l20",
        "display": "Kullanmadığı zaman bu esnek dil, minik bir sarmal gibi kıvrılır.",
        "spoken": "Kullanmadığı zaman bu esnek dil, minik bir sarmal gibi kıvrılır.",
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
        "id": "l21",
        "display": "Peki minik bir kelebek kendini nasıl korur? Hatırlarsan tırtıl süt otu yiyordu. Ulusal Park Servisi'ne göre süt otu zehirlidir.",
        "spoken": "Peki minik bir kelebek kendini nasıl korur? Hatırlarsan tırtıl süt otu yiyordu. Ulusal Park Servisi'ne göre süt otu zehirlidir.",
        "factIds": [
          "f2",
          "f7"
        ]
      },
      {
        "id": "l22",
        "display": "Bu zehir, tırtıl kelebeğe dönüştükten sonra bile vücudunda kalır. Monarkı yiyen hayvanlar çok hastalanır ve bir daha bu desenli kelebeğe dokunmaz.",
        "spoken": "Bu zehir, tırtıl kelebeğe dönüştükten sonra bile vücudunda kalır. Monarkı yiyen hayvanlar çok hastalanır ve bir daha bu desenli kelebeğe dokunmaz.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l23",
        "display": "Yani o parlak turuncu ve siyah desen bir uyarı işaretidir: Beni yeme!",
        "spoken": "Yani o parlak turuncu ve siyah desen bir uyarı işaretidir: Beni yeme!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l24",
        "display": "Şimdi büyük yolculuğa gelelim. Monark, kuşlar gibi gidip gelen bir göç yaptığı bilinen tek kelebektir.",
        "spoken": "Şimdi büyük yolculuğa gelelim. Monark, kuşlar gibi gidip gelen bir göç yaptığı bilinen tek kelebektir.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l25",
        "display": "Bir gramdan hafif bu kelebekler 2.000 ile 3.000 mil arasında uçar. Mil, kilometreden daha uzun bir uzunluk birimidir.",
        "spoken": "Bir gramdan hafif bu kelebekler iki bin ile üç bin mil arasında uçar. Mil, kilometreden daha uzun bir uzunluk birimidir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Günde 50–100 mil yol alabilirler. Kuzey Amerika'nın doğusundaki monarklar, kışı Meksika'daki 11–12 dağlık bölgede geçirir.",
        "spoken": "Günde elli ile yüz mil yol alabilirler. Kuzey Amerika'nın doğusundaki monarklar, kışı Meksika'daki on bir on iki dağlık bölgede geçirir.",
        "factIds": [
          "f9",
          "f10"
        ]
      },
      {
        "id": "l27",
        "display": "Orada tek bir ağaçta on binlerce monark kümelenebilir!",
        "spoken": "Orada tek bir ağaçta on binlerce monark kümelenebilir!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l28",
        "display": "İşin şaşırtıcı yanı: monarkların çoğu yalnızca birkaç hafta yaşar. Ama yaz sonunda doğan kuşak göç için doğar ve sekiz dokuz ay yaşayabilir.",
        "spoken": "İşin şaşırtıcı yanı: monarkların çoğu yalnızca birkaç hafta yaşar. Ama yaz sonunda doğan kuşak göç için doğar ve sekiz dokuz ay yaşayabilir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l29",
        "display": "Baharda kuzeye dönüş ise bir bayrak yarışına benzer: kuzeye ulaşmak 3–4 kuşak sürer. Her kuşak bir öncekinden biraz daha kuzeye gider.",
        "spoken": "Baharda kuzeye dönüş ise bir bayrak yarışına benzer: kuzeye ulaşmak üç dört kuşak sürer. Her kuşak bir öncekinden biraz daha kuzeye gider.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l30",
        "display": "Ama monarkların başı dertte. Yumurta bırakmak için süt otuna ihtiyaçları var; oysa süt otu çoğu zaman zararlı ot sanılıp yok ediliyor. Kışladıkları ormanlar da kesiliyor.",
        "spoken": "Ama monarkların başı dertte. Yumurta bırakmak için süt otuna ihtiyaçları var; oysa süt otu çoğu zaman zararlı ot sanılıp yok ediliyor. Kışladıkları ormanlar da kesiliyor.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l31",
        "display": "Şimdi sıra sende! Bahçende ya da parkta bir kelebek gözlem günlüğü tut. Gördüğün kelebeklerin renklerini ve hangi çiçeklere konduklarını not et.",
        "spoken": "Şimdi sıra sende! Bahçende ya da parkta bir kelebek gözlem günlüğü tut. Gördüğün kelebeklerin renklerini ve hangi çiçeklere konduklarını not et.",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Unutma: kelebeklere ve tırtıllara dokunma, yalnızca izle. Kanatları çok narindir.",
        "spoken": "Unutma: kelebeklere ve tırtıllara dokunma, yalnızca izle. Kanatları çok narindir.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l33",
        "display": "Hızlı soru! Tırtılın sert bir kılıf içinde kelebeğe dönüştüğü evrenin adı neydi?",
        "spoken": "Hızlı soru! Tırtılın sert bir kılıf içinde kelebeğe dönüştüğü evrenin adı neydi?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l34",
        "display": "Düşün bakalım... Evet: krizalit, yani pupa!",
        "spoken": "Düşün bakalım... Evet: krizalit, yani pupa!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l35",
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
        "id": "l36",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l38",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de göçmen kelebeklere yol gösterebilir miyim, bir bakayım!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de göçmen kelebeklere yol gösterebilir miyim, bir bakayım!",
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
    "statement": "Monark kelebeğinin dört ayrı yaşam evresi vardır: yumurta, larva (tırtıl), pupa (krizalit) ve ergin; bu dört evreli sürece tam başkalaşım denir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Dişi monarklar yumurtalarını zehirli süt otu yapraklarının alt yüzüne bırakır; bir dişi ömrü boyunca 100 ile 300 arasında yumurta bırakır; yumurtalar bırakıldıktan yaklaşık dört gün sonra açılır.",
    "numbers": [
      "100",
      "300"
    ]
  },
  {
    "id": "f3",
    "statement": "Tırtıl yumurtadan çıkınca kendi yumurtasını yer, sonra süt otu yapraklarıyla beslenmeye geçer.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Larvalar yumurtadan çıktığında 1 santimetreden küçüktür ve yaklaşık 5 santimetreye kadar büyür; larvanın deri değiştirmeleri arasındaki evrelere instar denir.",
    "numbers": [
      "1",
      "5"
    ]
  },
  {
    "id": "f5",
    "statement": "Monark, en az beş günde pupadan ergine dönüşebilir; kelebeğin pupadan çıkmasına eklozyon denir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Ergin kelebek uzun hortumunu açıp uzatarak çeşitli çiçeklerden nektar içer; kullanılmadığında bu esnek 'dil' yeniden sarmal biçiminde kıvrılır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Süt otunun zehirleri, tırtıl kelebeğe dönüştükten sonra bile monarkın vücudunda kalır; canlı desenleri bir uyarı işaretidir; monarkı yiyen hayvanlar çok hastalanır ve sonra bu desenli kelebekten uzak durur.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Monarkların çoğu yalnızca birkaç hafta yaşar; ama yaz sonu ve sonbahar başında çıkan kuşak farklıdır: göç için doğarlar ve sekiz dokuz ay yaşayabilirler.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Monark, kuşlar gibi iki yönlü göç yaptığı bilinen tek kelebektir; bazıları kışlık evlerine ulaşmak için 3.000 mile kadar uçar; günde 50–100 mil yol alabilirler.",
    "numbers": [
      "3.000",
      "50",
      "100"
    ]
  },
  {
    "id": "f10",
    "statement": "Kuzey Amerika'nın doğu monark topluluğu kışı Meksika'da aynı 11–12 dağlık bölgede geçirir; tek bir ağaçta on binlerce monark kümelenebilir.",
    "numbers": [
      "11",
      "12"
    ]
  },
  {
    "id": "f11",
    "statement": "Kuzey ABD'ye ve Kanada'ya ulaşmak 3–4 kuşak sürer; her yaz dört kuşağa kadar yetişir ve her kuşak bir öncekinden biraz daha kuzeye gider.",
    "numbers": [
      "3",
      "4"
    ]
  },
  {
    "id": "f12",
    "statement": "Monarkların yumurta bırakmak için süt otuna ihtiyacı vardır; ama süt otları çoğu zaman zararlı ot diye yok edilir; Meksika ve Kaliforniya'daki kışlak alanları ormansızlaşma yüzünden hızla küçülüyor.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bir gramdan hafif olan bu kelebekler 2.000 ile 3.000 mil arasında uçar.",
    "numbers": [
      "2.000",
      "3.000"
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
