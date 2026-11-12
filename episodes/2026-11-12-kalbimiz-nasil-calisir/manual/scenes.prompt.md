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
        "display": "Şu an göğsünde, sen hiç düşünmeden çalışan bir pompa var. Dün gece sen uyurken de çalıştı!",
        "spoken": "Şu an göğsünde, sen hiç düşünmeden çalışan bir pompa var. Dün gece sen uyurken de çalıştı!",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l2",
        "display": "Yumruğun kadar bir kas, kanı bütün vücuduna nasıl ulaştırıyor?",
        "spoken": "Yumruğun kadar bir kas, kanı bütün vücuduna nasıl ulaştırıyor?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün kalbin içine giriyoruz!",
        "spoken": "Bugün kalbin içine giriyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Benim kalbim yok, pilim var. Yine de bu konuya kalbimi... yani pilimi koydum!",
        "spoken": "Benim kalbim yok, pilim var. Yine de bu konuya kalbimi... yani pilimi koydum!",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Üç sorumuz var. Kalbin içinde neler var? Kan vücutta hangi yolu izler? Ve kalbe atmasını kim söyler?",
        "spoken": "Üç sorumuz var. Kalbin içinde neler var? Kan vücutta hangi yolu izler? Ve kalbe atmasını kim söyler?",
        "factIds": []
      },
      {
        "id": "l6",
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
        "id": "l7",
        "display": "Britanya Kalp Vakfı'na göre kalp bir kastır. Yaklaşık yumruğun büyüklüğündedir ve göğsünün ortasında, hafifçe sola yatık durur.",
        "spoken": "Britanya Kalp Vakfı'na göre kalp bir kastır. Yaklaşık yumruğun büyüklüğündedir ve göğsünün ortasında, hafifçe sola yatık durur.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Görevi pompalamaktır. KidsHealth'e göre genellikle dakikada 60–100 kez atar.",
        "spoken": "Görevi pompalamaktır. Kids Helt'e göre genellikle dakikada altmış ile yüz kez atar.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Peki kan neden bu kadar önemli? Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre kan, organlarının çalışması için gereken oksijeni ve besinleri taşır.",
        "spoken": "Peki kan neden bu kadar önemli? Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'e göre kan, organlarının çalışması için gereken oksijeni ve besinleri taşır.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l10",
        "display": "Dönerken de karbondioksiti ve atıkları toplayıp götürür.",
        "spoken": "Dönerken de karbondioksiti ve atıkları toplayıp götürür.",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l11",
        "display": "Kalbin içinde dört odacık vardır. Üstteki ikisine kulakçık denir: kalbe gelen kanı karşılarlar.",
        "spoken": "Kalbin içinde dört odacık vardır. Üstteki ikisine kulakçık denir: kalbe gelen kanı karşılarlar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l12",
        "display": "Alttaki ikisine karıncık denir: kanı kalpten dışarı pompalarlar.",
        "spoken": "Alttaki ikisine karıncık denir: kanı kalpten dışarı pompalarlar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Kalbin sağ ve sol tarafı, septum adlı ince bir kas duvarla birbirinden ayrılır.",
        "spoken": "Kalbin sağ ve sol tarafı, septum adlı ince bir kas duvarla birbirinden ayrılır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l14",
        "display": "Kalpte dört de kapakçık bulunur. Her atışta açılıp kapanan kapılar gibidirler.",
        "spoken": "Kalpte dört de kapakçık bulunur. Her atışta açılıp kapanan kapılar gibidirler.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l15",
        "display": "Benim de kapağım var. Ama o pil kapağı!",
        "spoken": "Benim de kapağım var. Ama o pil kapağı!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l16",
        "display": "Şimdi kanın yolculuğunu izleyelim. Vücudu dolaşıp oksijeni azalmış kan, önce sağ kulakçığa gelir.",
        "spoken": "Şimdi kanın yolculuğunu izleyelim. Vücudu dolaşıp oksijeni azalmış kan, önce sağ kulakçığa gelir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l17",
        "display": "Oradan sağ karıncığa geçer. Sağ karıncık bu kanı akciğerlere pompalar.",
        "spoken": "Oradan sağ karıncığa geçer. Sağ karıncık bu kanı akciğerlere pompalar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l18",
        "display": "Akciğerlerde kan oksijen alır ve karbondioksit bırakır.",
        "spoken": "Akciğerlerde kan oksijen alır ve karbondioksit bırakır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l19",
        "display": "Kalpten akciğerlere gidip geri dönen bu kısa tura küçük dolaşım denir.",
        "spoken": "Kalpten akciğerlere gidip geri dönen bu kısa tura küçük dolaşım denir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l20",
        "display": "Oksijence zengin kan sol kulakçığa döner, oradan sol karıncığa geçer.",
        "spoken": "Oksijence zengin kan sol kulakçığa döner, oradan sol karıncığa geçer.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l21",
        "display": "Sol karıncık, sağdakinden biraz daha büyüktür ve kanı bütün vücuda pompalar.",
        "spoken": "Sol karıncık, sağdakinden biraz daha büyüktür ve kanı bütün vücuda pompalar.",
        "factIds": [
          "f7",
          "f19"
        ]
      },
      {
        "id": "l22",
        "display": "Kan kalpten aort adlı damarla çıkar. Aort, vücudun en büyük atardamarıdır. Bu uzun tura büyük dolaşım denir.",
        "spoken": "Kan kalpten aort adlı damarla çıkar. Aort, vücudun en büyük atardamarıdır. Bu uzun tura büyük dolaşım denir.",
        "factIds": [
          "f9",
          "f8"
        ]
      },
      {
        "id": "l23",
        "display": "Damarların üç türü var. Atardamarlar kanı kalpten uzağa taşır. Toplardamarlar kalbe geri getirir.",
        "spoken": "Damarların üç türü var. Atardamarlar kanı kalpten uzağa taşır. Toplardamarlar kalbe geri getirir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l24",
        "display": "Kılcal damarlar ise çok incedir: en küçük atardamarları en küçük toplardamarlara bağlar.",
        "spoken": "Kılcal damarlar ise çok incedir: en küçük atardamarları en küçük toplardamarlara bağlar.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l25",
        "display": "Peki o ünlü ses? Lub-dub! KidsHealth'e göre bu, kapakçıkların kapanma sesidir: önce bir grup kapanır, lub; sonra öteki grup, dub.",
        "spoken": "Peki o ünlü ses? Lab-dab! Kids Helt'e göre bu, kapakçıkların kapanma sesidir: önce bir grup kapanır, lab; sonra öteki grup, dab.",
        "factIds": [
          "f11"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l26",
        "display": "Kalbe atmasını kim söyler? Kendi içindeki küçük bir doku: sinüs düğümü. Sağ kulakçığın duvarında yer alır.",
        "spoken": "Kalbe atmasını kim söyler? Kendi içindeki küçük bir doku: sinüs düğümü. Sağ kulakçığın duvarında yer alır.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Sinüs düğümü bir elektrik sinyali gönderir ve kalp kası kasılır. Atışın hızını o belirlediği için ona kalbin doğal pili de denir.",
        "spoken": "Sinüs düğümü bir elektrik sinyali gönderir ve kalp kası kasılır. Atışın hızını o belirlediği için ona kalbin doğal pili de denir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Demek ki senin de bir pilin var. Kardeş sayılırız!",
        "spoken": "Demek ki senin de bir pilin var. Kardeş sayılırız!",
        "factIds": []
      },
      {
        "id": "l29",
        "display": "Britanya Kalp Vakfı'na göre kalbin her gün yaklaşık 100.000 kez atar.",
        "spoken": "Britanya Kalp Vakfı'na göre kalbin her gün yaklaşık yüz bin kez atar.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l30",
        "display": "Koşarken kalbin neden hızlanır? Çünkü kasların daha çok oksijene ihtiyaç duyar; kalp de daha hızlı pompalar.",
        "spoken": "Koşarken kalbin neden hızlanır? Çünkü kasların daha çok oksijene ihtiyaç duyar; kalp de daha hızlı pompalar.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l31",
        "display": "Kalbini korumak için CDC'nin önerisi şu: 6–17 yaş arasındakiler her gün en az 60 dakika hareket etmeli.",
        "spoken": "Kalbini korumak için Si Di Si'nin önerisi şu: altı ile on yedi yaş arasındakiler her gün en az altmış dakika hareket etmeli.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l32",
        "display": "Dengeli beslenmek ve sigaradan uzak durmak da kalbi korur.",
        "spoken": "Dengeli beslenmek ve sigaradan uzak durmak da kalbi korur.",
        "factIds": [
          "f18"
        ]
      },
      {
        "id": "l33",
        "display": "Şimdi sıra sende! İşaret ve orta parmağını bileğinin iç yüzüne, başparmağının hemen altına koy. Hissettiğin vuruşlar nabzındır.",
        "spoken": "Şimdi sıra sende! İşaret ve orta parmağını bileğinin iç yüzüne, başparmağının hemen altına koy. Hissettiğin vuruşlar nabzındır.",
        "factIds": []
      },
      {
        "id": "l34",
        "display": "Otuz saniye boyunca vuruşları say ve ikiyle çarp. Bu, kalbinin bir dakikadaki atış sayısıdır.",
        "spoken": "Otuz saniye boyunca vuruşları say ve ikiyle çarp. Bu, kalbinin bir dakikadaki atış sayısıdır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l35",
        "display": "Sonra yirmi kez zıpla ve yeniden say. Sayı arttı mı? Kasların oksijen istedi, kalbin hızlandı!",
        "spoken": "Sonra yirmi kez zıpla ve yeniden say. Sayı arttı mı? Kasların oksijen istedi, kalbin hızlandı!",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l36",
        "display": "Bir uyarı: kendini zorlama; yorulursan dinlen.",
        "spoken": "Bir uyarı: kendini zorlama; yorulursan dinlen.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l37",
        "display": "Bunu biliyor muydun? Kalp atarken elektrik sinyali önce kulakçıkları kasar. Böylece kalp düzenli ve eşgüdümlü bir ritimle çalışır.",
        "spoken": "Bunu biliyor muydun? Kalp atarken elektrik sinyali önce kulakçıkları kasar. Böylece kalp düzenli ve eşgüdümlü bir ritimle çalışır.",
        "factIds": [
          "f20"
        ]
      },
      {
        "id": "l38",
        "display": "Hızlı soru! Kanı akciğerlere hangi odacık pompalar: sağ karıncık mı, sol karıncık mı?",
        "spoken": "Hızlı soru! Kanı akciğerlere hangi odacık pompalar: sağ karıncık mı, sol karıncık mı?",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l39",
        "display": "Düşün bakalım... Evet: sağ karıncık!",
        "spoken": "Düşün bakalım... Evet: sağ karıncık!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l40",
        "display": "Sol karıncık ise bütün vücuda pompalar. Ağır işi o almış; ben olsam ek şarj isterdim!",
        "spoken": "Sol karıncık ise bütün vücuda pompalar. Ağır işi o almış; ben olsam ek şarj isterdim!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l41",
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
        "id": "l42",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l43",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l44",
        "display": "Abone olmayı ve zili açmayı unutma. Ben de pilimi şarja takayım; ne de olsa benim kalbim o!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Ben de pilimi şarja takayım; ne de olsa benim kalbim o!",
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
    "statement": "Kalp bir kastır; yaklaşık yumruk büyüklüğündedir; göğsün ortasında, hafifçe sola yatık durur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Kalp bir pompa olan organdır; genellikle dakikada yaklaşık 60–100 kez atar.",
    "numbers": [
      "60",
      "100"
    ]
  },
  {
    "id": "f3",
    "statement": "Kalbin dört odacığı vardır: üstteki iki kulakçık kalbe giren kanı alır; alttaki iki karıncık kanı kalpten dışarı pompalar.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "İki taraf, septum adlı ince kas duvarla ayrılır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Sağ kulakçık vücudun geri kalanından gelen oksijeni azalmış kanı alır; sağ karıncık bu kanı yeni oksijen alması için akciğerlere pompalar.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Akciğerlerde kan oksijen alır ve karbondioksit bırakır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Sol kulakçık akciğerlerden gelen oksijence zengin kanı alır ve sol karıncığa pompalar; sol karıncık bu kanı vücudun geri kalanına pompalar.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Akciğer (küçük) dolaşımı kalpten akciğerlere gidip dönen kısa bir halkadır; sistemik (büyük) dolaşım kanı kalpten vücudun bütün öteki bölümlerine taşır ve geri getirir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Aort en büyük atardamardır; kalpten oksijence zengin kanı taşıyarak çıkar.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Kalpte dört kapakçık vardır; her atışta açılıp kapanan kapılar gibi çalışırlar.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Kalp atışının ilk sesi (lub) kulakçık-karıncık kapakçıklarının, ikinci sesi (dub) öteki kapakçıkların kapanmasıyla oluşur.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Atardamarlar kanı kalpten uzağa, toplardamarlar kalbe geri taşır; kılcal damarlar çok küçük atardamarları çok küçük toplardamarlara bağlayan minik damarlardır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Sinüs düğümü sağ kulakçığın duvarındaki küçük bir doku alanıdır; atış hızını belirlediği için kalbin pili (pacemaker) denir; kalp kasının kasılmasını başlatan elektrik sinyalini gönderir.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Kalp her gün yaklaşık 100.000 kez atar.",
    "numbers": [
      "100.000"
    ]
  },
  {
    "id": "f15",
    "statement": "Egzersiz yaparken kalp daha hızlı pompalar; böylece kaslar daha çok oksijen alır.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Kan, organların çalışması için gereken oksijeni ve besinleri taşır; istenmeyen karbondioksiti ve atıkları da uzaklaştırır.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "6–17 yaş arasındaki çocuk ve gençlerin her gün en az 60 dakika hareketli olması gerekir.",
    "numbers": [
      "6",
      "17",
      "60"
    ]
  },
  {
    "id": "f18",
    "statement": "Dengeli, besleyici beslenmek ve sigara içmemek kalp sağlığını korur.",
    "numbers": []
  },
  {
    "id": "f19",
    "statement": "Sol karıncık sağ karıncıktan biraz daha büyüktür.",
    "numbers": []
  },
  {
    "id": "f20",
    "statement": "Elektrik uyarıları önce kulakçıkları kasar; elektrik sinyalleri kalbin düzenli ve eşgüdümlü atmasını sağlar.",
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
