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
        "display": "Gece gökyüzüne bak: sayısız ışık noktası. Her biri, aslında çok uzaktaki dev bir gaz topu!",
        "spoken": "Gece gökyüzüne bak: sayısız ışık noktası. Her biri, aslında çok uzaktaki dev bir gaz topu!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l2",
        "display": "Peki bir yıldız neden parlar? Yakıtı nedir? Ve bir gün söner mi?",
        "spoken": "Peki bir yıldız neden parlar? Yakıtı nedir? Ve bir gün söner mi?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün bir yıldızın kalbine yolculuk ediyoruz!",
        "spoken": "Bugün bir yıldızın kalbine yolculuk ediyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Yıldız nedir? Işığını nasıl üretir? Ve yıldızlar nasıl doğar, nasıl ölür?",
        "spoken": "Üç sorumuz var. Yıldız nedir? Işığını nasıl üretir? Ve yıldızlar nasıl doğar, nasıl ölür?",
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
        "display": "NASA'ya göre yıldızlar, sıcak gazdan oluşan dev toplardır. Çoğunlukla hidrojenden, biraz da helyumdan oluşurlar.",
        "spoken": "Nasa'ya göre yıldızlar, sıcak gazdan oluşan dev toplardır. Çoğunlukla hidrojenden, biraz da helyumdan oluşurlar.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "En yakın örnek her gün tepemizde: Güneş! O da bir yıldızdır; kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
        "spoken": "En yakın örnek her gün tepemizde: Güneş! O da bir yıldızdır; kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Güneş'in gazı sıradan bir gaz değildir: çok sıcak ve elektrik yüklüdür. Buna plazma denir.",
        "spoken": "Güneş'in gazı sıradan bir gaz değildir: çok sıcak ve elektrik yüklüdür. Buna plazma denir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Elektrik yüklü dev bir top... Kulağa hayalimdeki şarj istasyonu gibi geliyor!",
        "spoken": "Elektrik yüklü dev bir top... Kulağa hayalimdeki şarj istasyonu gibi geliyor!",
        "factIds": []
      },
      {
        "id": "l10",
        "display": "Peki yıldız neden parlar? Sır, çekirdeğinde saklı. Oradaki muazzam basınç ve sıcaklık, hidrojen atomlarının çekirdeklerini birbirine sıkıştırır.",
        "spoken": "Peki yıldız neden parlar? Sır, çekirdeğinde saklı. Oradaki muazzam basınç ve sıcaklık, hidrojen atomlarının çekirdeklerini birbirine sıkıştırır.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Hidrojen çekirdekleri birleşir ve helyuma dönüşür. Bu olaya çekirdek kaynaşması, yani füzyon denir.",
        "spoken": "Hidrojen çekirdekleri birleşir ve helyuma dönüşür. Bu olaya çekirdek kaynaşması, yani füzyon denir.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l12",
        "display": "Füzyon enerji açığa çıkarır. Yıldızı ısıtan ve parlatan enerji budur.",
        "spoken": "Füzyon enerji açığa çıkarır. Yıldızı ısıtan ve parlatan enerji budur.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l13",
        "display": "Güneş'in çekirdeği yaklaşık 15 milyon santigrat derecedir. Yüzeyi ise 5.500 derece.",
        "spoken": "Güneş'in çekirdeği yaklaşık on beş milyon santigrat derecedir. Yüzeyi ise beş bin beş yüz derece.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l14",
        "display": "Yıldızın içinde sürekli bir çekişme vardır: kütle çekimi içeri doğru bastırır, füzyonun yarattığı basınç dışarı doğru iter. Bu sayede yıldız çökmez.",
        "spoken": "Yıldızın içinde sürekli bir çekişme vardır: kütle çekimi içeri doğru bastırır, füzyonun yarattığı basınç dışarı doğru iter. Bu sayede yıldız çökmez.",
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
        "id": "l15",
        "display": "Yıldızlar nasıl doğar? Uzayda moleküler bulut denen dev gaz ve toz bulutları vardır.",
        "spoken": "Yıldızlar nasıl doğar? Uzayda moleküler bulut denen dev gaz ve toz bulutları vardır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l16",
        "display": "Kütle çekimi, bu bulutlardaki bazı topakların kendi üzerine çökmesine yol açar. Topak yüz binlerce yıl boyunca kütle kazanır, döner ve ısınır.",
        "spoken": "Kütle çekimi, bu bulutlardaki bazı topakların kendi üzerine çökmesine yol açar. Topak yüz binlerce yıl boyunca kütle kazanır, döner ve ısınır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l17",
        "display": "Sonunda bir önyıldız, yani bebek yıldız ortaya çıkar.",
        "spoken": "Sonunda bir önyıldız, yani bebek yıldız ortaya çıkar.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l18",
        "display": "Çekirdeğinde hidrojeni helyuma dönüştüren yıldıza ana kol yıldızı denir. Güneş de bir ana kol yıldızıdır ve bu evrenin aşağı yukarı ortasındadır.",
        "spoken": "Çekirdeğinde hidrojeni helyuma dönüştüren yıldıza ana kol yıldızı denir. Güneş de bir ana kol yıldızıdır ve bu evrenin aşağı yukarı ortasındadır.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l19",
        "display": "Güneş yaklaşık 4,6 milyar yıl önce oluştu. Bize uzaklığı yaklaşık 150 milyon kilometre.",
        "spoken": "Güneş yaklaşık dört virgül altı milyar yıl önce oluştu. Bize uzaklığı yaklaşık yüz elli milyon kilometre.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l20",
        "display": "O kadar büyük ki içini doldurmak için 1,3 milyon Dünya gerekir!",
        "spoken": "O kadar büyük ki içini doldurmak için bir virgül üç milyon Dünya gerekir!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l21",
        "display": "Ama Güneş, yıldızların en büyüğü değil. Çapı Güneş'inkinin 1.000 katı olan yıldızlar bulundu. En küçük ana kol yıldızları ise kırmızı cücelerdir.",
        "spoken": "Ama Güneş, yıldızların en büyüğü değil. Çapı Güneş'inkinin bin katı olan yıldızlar bulundu. En küçük ana kol yıldızları ise kırmızı cücelerdir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l22",
        "display": "Bu sayıları hesaplarken işlemcim ısındı. Neyse ki Güneş'in çekirdeği kadar değil!",
        "spoken": "Bu sayıları hesaplarken işlemcim ısındı. Neyse ki Güneş'in çekirdeği kadar değil!",
        "factIds": []
      },
      {
        "id": "l23",
        "display": "Peki yıldızlar ölür mü? Evet, ama çok uzun sürer: bir yıldızın ömrü birkaç milyon yıldan trilyonlarca yıla kadar değişir.",
        "spoken": "Peki yıldızlar ölür mü? Evet, ama çok uzun sürer: bir yıldızın ömrü birkaç milyon yıldan trilyonlarca yıla kadar değişir.",
        "factIds": [
          "f17"
        ]
      },
      {
        "id": "l24",
        "display": "Güneş yaklaşık 5 milyar yıl sonra şişerek bir kırmızı deve dönüşecek. O kadar büyüyecek ki Merkür'ü ve Venüs'ü yutacak.",
        "spoken": "Güneş yaklaşık beş milyar yıl sonra şişerek bir kırmızı deve dönüşecek. O kadar büyüyecek ki Merkür'ü ve Venüs'ü yutacak.",
        "factIds": [
          "f9"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l25",
        "display": "Sonra dış katmanları genişleyen bir gaz ve toz bulutuna dönüşecek; buna gezegenimsi bulutsu denir. Geriye kalan kalıntının adı ise beyaz cüce.",
        "spoken": "Sonra dış katmanları genişleyen bir gaz ve toz bulutuna dönüşecek; buna gezegenimsi bulutsu denir. Geriye kalan kalıntının adı ise beyaz cüce.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l26",
        "display": "Çok daha büyük kütleli yıldızların sonu gürültülü olur: süpernova denen dev bir patlama!",
        "spoken": "Çok daha büyük kütleli yıldızların sonu gürültülü olur: süpernova denen dev bir patlama!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l27",
        "display": "Kütlesi Güneş'in 8–20 katı arasındaki yıldızlardan geriye nötron yıldızı kalır. Daha ağır olanlar ise kara deliğe dönüşür.",
        "spoken": "Kütlesi Güneş'in sekiz ile yirmi katı arasındaki yıldızlardan geriye nötron yıldızı kalır. Daha ağır olanlar ise kara deliğe dönüşür.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l28",
        "display": "İşin en güzel yanı şu: yıldızlar birer element fabrikasıdır. Füzyon, karbonu oksijen gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir demire kadar sürer.",
        "spoken": "İşin en güzel yanı şu: yıldızlar birer element fabrikasıdır. Füzyon, karbonu oksijen gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir demire kadar sürer.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l29",
        "display": "Süpernovalar bu maddeyi uzaya saçar ve yeni yıldızların doğacağı bulutları zenginleştirir.",
        "spoken": "Süpernovalar bu maddeyi uzaya saçar ve yeni yıldızların doğacağı bulutları zenginleştirir.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l30",
        "display": "Yani bendeki demir de bir zamanlar bir yıldızın içindeydi. Ben resmen yıldız yapımıyım!",
        "spoken": "Yani bendeki demir de bir zamanlar bir yıldızın içindeydi. Ben resmen yıldız yapımıyım!",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l31",
        "display": "Kaç yıldız var? Yalnızca Samanyolu'nda 100 milyardan fazla. Evrendeki sayı ise 1'in yanına 24 sıfır koyacak kadar olabilir.",
        "spoken": "Kaç yıldız var? Yalnızca Samanyolu'nda yüz milyardan fazla. Evrendeki sayı ise birin yanına yirmi dört sıfır koyacak kadar olabilir.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l32",
        "display": "Güneş'ten sonra bize en yakın yıldız Proxima Centauri: 4,24 ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.",
        "spoken": "Güneş'ten sonra bize en yakın yıldız Proksima Sentauri: dört virgül yirmi dört ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l33",
        "display": "Şimdi sıra sende! Açık bir gecede, bir büyüğünle birlikte ışıklardan uzak bir yerden gökyüzüne bak. Gece gökyüzünün en parlak yıldızı Sirius'u bulmayı dene.",
        "spoken": "Şimdi sıra sende! Açık bir gecede, bir büyüğünle birlikte ışıklardan uzak bir yerden gökyüzüne bak. Gece gökyüzünün en parlak yıldızı Sirius'u bulmayı dene.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l34",
        "display": "Gördüğün yıldızların parlaklıklarını karşılaştır ve bir yıldız günlüğüne çiz. Hepsi aynı mı parlıyor?",
        "spoken": "Gördüğün yıldızların parlaklıklarını karşılaştır ve bir yıldız günlüğüne çiz. Hepsi aynı mı parlıyor?",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Bir uyarı: Güneş de bir yıldızdır ama ona asla doğrudan bakma!",
        "spoken": "Bir uyarı: Güneş de bir yıldızdır ama ona asla doğrudan bakma!",
        "factIds": [
          "f16"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l36",
        "display": "Bunu biliyor muydun? Gece çıplak gözle görebildiğin yıldızların birçoğu, tıpkı Güneş gibi ana kol yıldızıdır.",
        "spoken": "Bunu biliyor muydun? Gece çıplak gözle görebildiğin yıldızların birçoğu, tıpkı Güneş gibi ana kol yıldızıdır.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l37",
        "display": "Hızlı soru! Yıldızın çekirdeğinde hidrojeni helyuma dönüştüren olayın adı neydi?",
        "spoken": "Hızlı soru! Yıldızın çekirdeğinde hidrojeni helyuma dönüştüren olayın adı neydi?",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l38",
        "display": "Düşün bakalım... Evet: füzyon!",
        "spoken": "Düşün bakalım... Evet: füzyon!",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l39",
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
        "id": "l40",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l41",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l42",
        "display": "Abone olmayı ve zili açmayı unutma. Bu gece gökyüzüne bakarken beni de hatırla!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Bu gece gökyüzüne bakarken beni de hatırla!",
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
    "statement": "Yıldızlar sıcak gazdan oluşan dev toplardır; çoğunlukla hidrojenden, biraz helyumdan ve az miktarda başka elementlerden oluşurlar.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur; plazma denen çok sıcak, elektrik yüklü gazdan oluşur.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Yıldızlar moleküler bulut denen büyük gaz ve toz bulutlarında oluşur; kütle çekimi bazı topakların çökmesine yol açar; topak yüz binlerce yıl boyunca kütle kazanır, dönmeye başlar ve ısınır; sonunda bir önyıldız (bebek yıldız) gelişir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Yıldızın çekirdeğindeki muazzam basınç ve sıcaklık hidrojen atomlarının çekirdeklerini sıkıştırarak helyum oluşturur; çekirdek kaynaşması (füzyon) enerji açığa çıkarır, yıldızı ısıtır ve kütle çekimi altında çökmesini önler; oluşan basınç kütle çekimine karşı iter.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir; yüzeyinde 5.500 santigrat derece.",
    "numbers": [
      "15",
      "5.500"
    ]
  },
  {
    "id": "f6",
    "statement": "Güneş yaklaşık 4,6 milyar yıl önce oluştu; Dünya'dan yaklaşık 150 milyon kilometre uzaktadır; hacmini doldurmak için 1,3 milyon Dünya gerekir.",
    "numbers": [
      "4.6",
      "150",
      "1.3"
    ]
  },
  {
    "id": "f7",
    "statement": "Çekirdeğinde hidrojeni helyuma kaynaştıran yıldıza ana kol yıldızı denir; Güneş ana kol evresinin aşağı yukarı ortasındadır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Kırmızı cüceler en küçük ana kol yıldızlarıdır; çapı Güneş'inkinin 1.000 katı olan yıldızlar bulunmuştur.",
    "numbers": [
      "1.000"
    ]
  },
  {
    "id": "f9",
    "statement": "Güneş yaklaşık 5 milyar yıl sonra kırmızı dev olacak; Merkür'ü ve Venüs'ü, belki Dünya'yı da yutacak kadar büyüyecek.",
    "numbers": [
      "5"
    ]
  },
  {
    "id": "f10",
    "statement": "Genişleyen toz ve gaz bulutuna gezegenimsi bulutsu, geriye kalan yıldız kalıntısına beyaz cüce denir.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Büyük kütleli yıldızların sonu süpernova denen dev bir patlamadır; kütlesi Güneş'in yaklaşık 8 ile 20 katı arasındaki yıldızlardan nötron yıldızı oluşur; daha ağır yıldızlar kara delik üretir.",
    "numbers": [
      "8",
      "20"
    ]
  },
  {
    "id": "f12",
    "statement": "Füzyon karbonu oksijen, neon ve magnezyum gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir silisyumun demire kaynaşmasına kadar sürer; süpernovaların uzaya saçtığı madde gelecekteki moleküler bulutları zenginleştirir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Samanyolu'nda 100 milyardan fazla yıldız vardır; evrende bir septilyona kadar yıldız olabilir: 1'in yanında 24 sıfır.",
    "numbers": [
      "100",
      "1",
      "24"
    ]
  },
  {
    "id": "f14",
    "statement": "En yakın yıldız komşumuz kırmızı cüce Proxima Centauri'dir; 4,24 ışık yılı uzaktadır. Işık yılı, ışığın bir yılda aldığı yoldur.",
    "numbers": [
      "4.24"
    ]
  },
  {
    "id": "f15",
    "statement": "Sirius gece gökyüzünün en parlak yıldızıdır; birçok ana kol yıldızı çıplak gözle görülebilir.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Gözleri korumadan Güneş'e asla doğrudan bakılmamalıdır.",
    "numbers": []
  },
  {
    "id": "f17",
    "statement": "Her yıldızın kendi yaşam döngüsü vardır; birkaç milyon yıldan trilyonlarca yıla kadar sürer.",
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
