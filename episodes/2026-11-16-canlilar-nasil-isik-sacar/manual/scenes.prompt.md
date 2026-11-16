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
        "display": "Bir yaz gecesi çayırda minik ışıklar yanıp sönüyor. Bunlar lamba değil, ateşböcekleri!",
        "spoken": "Bir yaz gecesi çayırda minik ışıklar yanıp sönüyor. Bunlar lamba değil, ateşböcekleri!",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l2",
        "display": "Peki bir canlı, pil ya da kablo olmadan nasıl ışık yapar?",
        "spoken": "Peki bir canlı, pil ya da kablo olmadan nasıl ışık yapar?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün ışık saçan canlıların sırrını çözüyoruz!",
        "spoken": "Bugün ışık saçan canlıların sırrını çözüyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Canlılar ışığı nasıl üretir? Bu ışık neden sıcak değildir? Ve neden ışık saçarlar?",
        "spoken": "Üç sorumuz var. Canlılar ışığı nasıl üretir? Bu ışık neden sıcak değildir? Ve neden ışık saçarlar?",
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
        "display": "National Geographic'e göre canlıların vücutlarındaki kimyasal tepkimelerle saçtıkları ışığa biyolüminesans denir.",
        "spoken": "Neşınıl Ciyogrefik'e göre canlıların vücutlarındaki kimyasal tepkimelerle saçtıkları ışığa biyolüminesans denir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "ABD Milli Parklar Servisi'ne göre bunu yalnızca ateşböcekleri yapmaz; bazı mantarlar, balıklar, karidesler, denizanaları ve planktonlar da yapar.",
        "spoken": "ABD Milli Parklar Servisi'ne göre bunu yalnızca ateşböcekleri yapmaz; bazı mantarlar, balıklar, karidesler, denizanaları ve planktonlar da yapar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Bu tepkimenin iki yıldızı var: lusiferin ve lusiferaz. Işığı asıl üreten bileşik lusiferindir.",
        "spoken": "Bu tepkimenin iki yıldızı var: lusiferin ve lusiferaz. Işığı asıl üreten bileşik lusiferindir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Ateşböcekleri lusiferini oksijenle ve lusiferaz denen bir enzimle karıştırır. Sonuç: ışık!",
        "spoken": "Ateşböcekleri lusiferini oksijenle ve lusiferaz denen bir enzimle karıştırır. Sonuç: ışık!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l10",
        "display": "Bazı canlılar lusiferaz yerine fotoprotein kullanır. Fotoproteinler ışık yapmak için çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.",
        "spoken": "Bazı canlılar lusiferaz yerine fotoprotein kullanır. Fotoproteinler ışık yapmak için çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.",
        "factIds": [
          "f3",
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Benim de anten yıldızım parlıyor. Ama benimki tamamen pilden; içimde bir gram lusiferin yok!",
        "spoken": "Benim de anten yıldızım parlıyor. Ama benimki tamamen pilden; içimde bir gram lusiferin yok!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Bu ışığın şaşırtıcı bir özelliği var: Soğuk ışıktır.",
        "spoken": "Bu ışığın şaşırtıcı bir özelliği var: Soğuk ışıktır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "National Geographic'e göre soğuk ışık, ışığın yüzde 20'sinden azının ısıya dönüşmesi demektir.",
        "spoken": "Neşınıl Ciyogrefik'e göre soğuk ışık, ışığın yüzde yirmisinden azının ısıya dönüşmesi demektir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Eski tip akkor ampullerle karşılaştıralım. Milli Parklar Servisi'ne göre bu ampuller enerjilerinin yalnızca yüzde 10 kadarını ışığa çevirir; yüzde 90'ı ısı olur.",
        "spoken": "Eski tip akkor ampullerle karşılaştıralım. Milli Parklar Servisi'ne göre bu ampuller enerjilerinin yalnızca yüzde on kadarını ışığa çevirir; yüzde doksanı ısı olur.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Ateşböceğinin parıltısı ise neredeyse yüzde 100 ışıktır ve çok az ısı üretir.",
        "spoken": "Ateşböceğinin parıltısı ise neredeyse yüzde yüz ışıktır ve çok az ısı üretir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l16",
        "display": "Ben eski bir ampul olsaydım, kafam hep sıcacık olurdu. Neyse ki ben LED'liyim!",
        "spoken": "Ben eski bir ampul olsaydım, kafam hep sıcacık olurdu. Neyse ki ben LED'liyim!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l17",
        "display": "Peki canlılar neden ışık saçar? National Geographic'e göre avlanmak, avcılara karşı korunmak ve eş bulmak için.",
        "spoken": "Peki canlılar neden ışık saçar? Neşınıl Ciyogrefik'e göre avlanmak, avcılara karşı korunmak ve eş bulmak için.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l18",
        "display": "Ateşböceklerinde ışığın önemli bir görevi eş bulmaktır. Her türün kendine özgü bir yanıp sönme deseni vardır.",
        "spoken": "Ateşböceklerinde ışığın önemli bir görevi eş bulmaktır. Her türün kendine özgü bir yanıp sönme deseni vardır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l19",
        "display": "Örneğin eşzamanlı yanıp sönen bir türde, 5 ile 8 arası parlamayı 8 saniyelik bir karanlık izler.",
        "spoken": "Örneğin eşzamanlı yanıp sönen bir türde, beş ile sekiz arası parlamayı sekiz saniyelik bir karanlık izler.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l20",
        "display": "Derin denizde ise fener balığı, ışığını avını cezbetmek için kullanır.",
        "spoken": "Derin denizde ise fener balığı, ışığını avını cezbetmek için kullanır.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l21",
        "display": "Baltabalığı gibi bazı balıklar karşı aydınlatma denen bir kamuflaj kullanır. Karınlarındaki ışık organları aşağıya bakar.",
        "spoken": "Baltabalığı gibi bazı balıklar karşı aydınlatma denen bir kamuflaj kullanır. Karınlarındaki ışık organları aşağıya bakar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l22",
        "display": "Alttan çıkan ışığı yukarıdan gelen ışığa eşitlerler. Böylece gölgeleri kaybolur ve aşağıdan bakan avcılara neredeyse görünmez olurlar.",
        "spoken": "Alttan çıkan ışığı yukarıdan gelen ışığa eşitlerler. Böylece gölgeleri kaybolur ve aşağıdan bakan avcılara neredeyse görünmez olurlar.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l23",
        "display": "Birçok kalamar türü avcılarını ürkütmek için parlar. Bazı böcek larvaları da zehirli olduklarını göstermek için ışık saçar.",
        "spoken": "Birçok kalamar türü avcılarını ürkütmek için parlar. Bazı böcek larvaları da zehirli olduklarını göstermek için ışık saçar.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l24",
        "display": "Yani ışık; bir av tuzağı, bir görünmezlik pelerini ya da bir uyarı tabelası olabilir!",
        "spoken": "Yani ışık; bir av tuzağı, bir görünmezlik pelerini ya da bir uyarı tabelası olabilir!",
        "factIds": [
          "f12",
          "f13",
          "f15"
        ]
      },
      {
        "id": "l25",
        "display": "Denizdeki biyolüminesansın çoğu mavi-yeşil renktedir. Çünkü bu renkler derin okyanusta daha kolay görülür.",
        "spoken": "Denizdeki biyolüminesansın çoğu mavi-yeşil renktedir. Çünkü bu renkler derin okyanusta daha kolay görülür.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l26",
        "display": "Ateşböceklerinin çoğu yeşilimsi sarı ışık saçar; bazı türlerinki ise maviye ya da beyaza kaçar.",
        "spoken": "Ateşböceklerinin çoğu yeşilimsi sarı ışık saçar; bazı türlerinki ise maviye ya da beyaza kaçar.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l27",
        "display": "Ben hangi renkte parlıyorum biliyor musun? Utanınca kıpkırmızı!",
        "spoken": "Ben hangi renkte parlıyorum biliyor musun? Utanınca kıpkırmızı!",
        "factIds": []
      },
      {
        "id": "l28",
        "display": "Şimdi sıra sende! Yazın ateşböceklerinin yaşadığı bir yerdeysen, akşam karanlığında bir yetişkinle dışarı çık.",
        "spoken": "Şimdi sıra sende! Yazın ateşböceklerinin yaşadığı bir yerdeysen, akşam karanlığında bir yetişkinle dışarı çık.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l29",
        "display": "Işıkları dikkatle izle ve yanıp sönmeleri say. Hepsi aynı desende mi? Ateşböceklerini yakalama, yalnızca izle!",
        "spoken": "Işıkları dikkatle izle ve yanıp sönmeleri say. Hepsi aynı desende mi? Ateşböceklerini yakalama, yalnızca izle!",
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
        "display": "Bunu biliyor muydun? National Geographic'e göre tatlı sulara özgü ışık saçan canlı neredeyse yoktur.",
        "spoken": "Bunu biliyor muydun? Neşınıl Ciyogrefik'e göre tatlı sulara özgü ışık saçan canlı neredeyse yoktur.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l31",
        "display": "Bir de demiryolu solucanı var: başı kırmızı, gövdesi yeşil parlar. Yürüyen bir trafik ışığı gibi!",
        "spoken": "Bir de demiryolu solucanı var: başı kırmızı, gövdesi yeşil parlar. Yürüyen bir trafik ışığı gibi!",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l32",
        "display": "Hızlı soru! Işığı asıl üreten bileşiğin adı neydi?",
        "spoken": "Hızlı soru! Işığı asıl üreten bileşiğin adı neydi?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l33",
        "display": "Düşün bakalım... Evet: lusiferin!",
        "spoken": "Düşün bakalım... Evet: lusiferin!",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l34",
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
        "id": "l35",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l36",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l37",
        "display": "Abone olmayı ve zili açmayı unutma. Işığın hiç sönmesin!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Işığın hiç sönmesin!",
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
    "statement": "Biyolüminesans, canlıların vücutlarındaki kimyasal tepkimelerle saçtığı ışıktır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Biyolüminesans ateşböceklerinin yanı sıra bazı mantarlarda, balıklarda, karideslerde, denizanalarında ve planktonlarda da görülür; bazıları karada yaşar.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Biyolüminesans lusiferin ve lusiferaz ya da fotoprotein gerektirir; ışığı asıl üreten bileşik lusiferindir; ateşböcekleri lusiferini oksijen ve lusiferaz enzimiyle karıştırır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Fotoproteinler ışık yapmak için başka bir etkene, çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Soğuk ışık, ışığın yüzde 20'sinden azının ısı olarak yayılması demektir.",
    "numbers": [
      "20"
    ]
  },
  {
    "id": "f6",
    "statement": "Akkor ampuller enerjilerinin yalnızca yaklaşık yüzde 10'unu ışık, yüzde 90'ını ısı olarak yayar; ateşböceğinin parıltısı neredeyse yüzde 100 ışıktır ve çok az ısı üretir.",
    "numbers": [
      "10",
      "90",
      "100"
    ]
  },
  {
    "id": "f7",
    "statement": "Işık saçan deniz canlıları arasında balıklar, bakteriler ve denizanaları vardır; dinoflagellatlar mavimsi yeşil parlar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Denizdeki biyolüminesansın çoğu görünür ışığın mavi-yeşil bölümündedir; bu renkler derin okyanusta daha kolay görülür.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Ateşböceği türlerinin çoğu yeşilimsi sarı ışık saçar, bazı türler mavi ya da beyaza yakın ışık saçar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Ateşböceğinin yanıp sönmesinin önemli bir amacı eş çekmektir; her türün kendine özgü bir yanıp sönme deseni vardır.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Eşzamanlı ateşböceğinde 5 ile 8 arası belirgin parlamayı 8 saniyelik bir karanlık izler.",
    "numbers": [
      "5",
      "8"
    ]
  },
  {
    "id": "f12",
    "statement": "Biyolüminesansı kullanan en ünlü avcı belki de avını cezbetmek için kullanan fener balığıdır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Birçok deniz canlısı kendini korumak için karşı aydınlatma denen bir kamuflaj kullanır; baltabalıklarının ışık organları aşağı bakar, alttan çıkan ışığı yukarıdan gelen ışığa eşitler, böylece gölgelerini gizleyip aşağıdan bakan avcılara neredeyse görünmez olurlar.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Canlılar biyolüminesansı avlanmak, avcılara karşı korunmak ve eş bulmak için kullanır.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Birçok kalamar türü avcılarını ürkütmek için parlar; bazı böcek larvaları zehirli olduklarını avcılara bildirmek için ışık saçar.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Tatlı su ortamlarına özgü ışık saçan canlı neredeyse yoktur.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Demiryolu solucanının başı kırmızı, gövdesi yeşil parlar.",
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
