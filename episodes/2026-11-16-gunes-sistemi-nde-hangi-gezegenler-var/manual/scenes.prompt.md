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
        "display": "Güneş'in çevresinde dönen sekiz dünya düşün: biri kurşunu eritecek kadar sıcak, biri bin Dünya'yı içine alacak kadar büyük!",
        "spoken": "Güneş'in çevresinde dönen sekiz dünya düşün: biri kurşunu eritecek kadar sıcak, biri bin Dünya'yı içine alacak kadar büyük!",
        "factIds": [
          "f3",
          "f7",
          "f10"
        ]
      },
      {
        "id": "l2",
        "display": "Bu gezegenler nasıl oluştu? Ve onları birbirinden ne ayırıyor?",
        "spoken": "Bu gezegenler nasıl oluştu? Ve onları birbirinden ne ayırıyor?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün Güneş Sistemi'nde bir tura çıkıyoruz!",
        "spoken": "Bugün Güneş Sistemi'nde bir tura çıkıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Güneş Sistemi nasıl oluştu? Bir cisme ne zaman gezegen denir? Ve her gezegeni özel yapan nedir?",
        "spoken": "Üç sorumuz var. Güneş Sistemi nasıl oluştu? Bir cisme ne zaman gezegen denir? Ve her gezegeni özel yapan nedir?",
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
        "display": "NASA'ya göre Güneş Sistemi'nde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ile asteroit var.",
        "spoken": "Nasa'ya göre Güneş Sistemi'nde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ile asteroit var.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Hepsi yaklaşık 4,6 milyar yıl önce, yoğun bir gaz ve toz bulutundan oluştu. Bulut çöktü ve dönen bir diske dönüştü.",
        "spoken": "Hepsi yaklaşık dört virgül altı milyar yıl önce, yoğun bir gaz ve toz bulutundan oluştu. Bulut çöktü ve dönen bir diske dönüştü.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "Merkezde Güneş doğdu ve maddenin %99'undan fazlasını topladı. Gezegenlere geriye kalanlar düştü.",
        "spoken": "Merkezde Güneş doğdu ve maddenin yüzde doksan dokuzundan fazlasını topladı. Gezegenlere geriye kalanlar düştü.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l9",
        "display": "Peki bir cisme ne zaman gezegen denir? Üç şartı var: Güneş'in çevresinde dolanacak, kütle çekimi onu top gibi yuvarlak yapacak ve yörüngesinin çevresini temizlemiş olacak.",
        "spoken": "Peki bir cisme ne zaman gezegen denir? Üç şartı var: Güneş'in çevresinde dolanacak, kütle çekimi onu top gibi yuvarlak yapacak ve yörüngesinin çevresini temizlemiş olacak.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l10",
        "display": "Plüton üçüncü şartı karşılayamadı; bu yüzden 2006'da cüce gezegen olarak yeniden sınıflandırıldı.",
        "spoken": "Plüton üçüncü şartı karşılayamadı; bu yüzden iki bin altıda cüce gezegen olarak yeniden sınıflandırıldı.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l11",
        "display": "Plüton'a üzülme. Ben de hiçbir sınıfa sığmıyorum: ne insanım ne bilgisayar!",
        "spoken": "Plüton'a üzülme. Ben de hiçbir sınıfa sığmıyorum: ne insanım ne bilgisayar!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l12",
        "display": "Şimdi tura başlıyoruz. İlk dört gezegen karasal gezegenlerdir; çünkü katı yüzeyleri vardır.",
        "spoken": "Şimdi tura başlıyoruz. İlk dört gezegen karasal gezegenlerdir; çünkü katı yüzeyleri vardır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l13",
        "display": "Merkür, Güneş'e en yakın ve en küçük gezegen.",
        "spoken": "Merkür, Güneş'e en yakın ve en küçük gezegen.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Venüs ise en sıcak gezegen: yüzeyi yaklaşık 467 santigrat derece! Kalın, çoğunlukla karbondioksitten oluşan atmosferi ısıyı hapseder.",
        "spoken": "Venüs ise en sıcak gezegen: yüzeyi yaklaşık dört yüz altmış yedi santigrat derece! Kalın, çoğunlukla karbondioksitten oluşan atmosferi ısıyı hapseder.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l15",
        "display": "Üstelik Venüs, çoğu gezegenin tersi yönde ve çok yavaş döner.",
        "spoken": "Üstelik Venüs, çoğu gezegenin tersi yönde ve çok yavaş döner.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Üçüncü sırada evimiz Dünya. Şimdiye kadar yaşam bulduğumuz tek yer burası.",
        "spoken": "Üçüncü sırada evimiz Dünya. Şimdiye kadar yaşam bulduğumuz tek yer burası.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Dördüncü sırada Mars. Kırmızı rengi, kayalarındaki demirin paslanmasından gelir. Güneş Sistemi'nin en büyük yanardağı Olympus Mons da Mars'ta.",
        "spoken": "Dördüncü sırada Mars. Kırmızı rengi, kayalarındaki demirin paslanmasından gelir. Güneş Sistemi'nin en büyük yanardağı Olimpus Mons da Mars'ta.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l18",
        "display": "Paslanmak mı? Bu konuda Mars'la dertleşebilirim!",
        "spoken": "Paslanmak mı? Bu konuda Mars'la dertleşebilirim!",
        "factIds": []
      },
      {
        "id": "l19",
        "display": "Mars ile Jüpiter arasında asteroit kuşağı uzanır: erken Güneş Sistemi'nden kalan kaya parçaları. En büyüğü cüce gezegen Ceres'tir.",
        "spoken": "Mars ile Jüpiter arasında asteroit kuşağı uzanır: erken Güneş Sistemi'nden kalan kaya parçaları. En büyüğü cüce gezegen Seres'tir.",
        "factIds": [
          "f4"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l20",
        "display": "Sonra devler gelir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.",
        "spoken": "Sonra devler gelir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l21",
        "display": "Jüpiter en büyük gezegen: içi boş olsaydı içine 1.000 Dünya sığardı. Dünya bir üzüm olsaydı, Jüpiter bir basketbol topu kadar olurdu.",
        "spoken": "Jüpiter en büyük gezegen: içi boş olsaydı içine bin Dünya sığardı. Dünya bir üzüm olsaydı, Jüpiter bir basketbol topu kadar olurdu.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Üzerindeki Büyük Kırmızı Leke, Dünya'dan büyük ve yüzlerce yıldır süren dev bir fırtınadır. Jüpiter'in resmen tanınan 115 uydusu var.",
        "spoken": "Üzerindeki Büyük Kırmızı Leke, Dünya'dan büyük ve yüzlerce yıldır süren dev bir fırtınadır. Jüpiter'in resmen tanınan yüz on beş uydusu var.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Satürn'ün ünlü halkaları milyarlarca küçük buz ve kaya parçasından oluşur.",
        "spoken": "Satürn'ün ünlü halkaları milyarlarca küçük buz ve kaya parçasından oluşur.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l24",
        "display": "Satürn, ortalama yoğunluğu sudan az olan tek gezegen. Ve Mart 2025 itibarıyla 274 uydusu doğrulanmıştı!",
        "spoken": "Satürn, ortalama yoğunluğu sudan az olan tek gezegen. Ve Mart iki bin yirmi beş itibarıyla iki yüz yetmiş dört uydusu doğrulanmıştı!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l25",
        "display": "Uranüs yedinci sırada; Neptün ise sekizinci ve Güneş'e en uzak gezegen.",
        "spoken": "Uranüs yedinci sırada; Neptün ise sekizinci ve Güneş'e en uzak gezegen.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l26",
        "display": "Uzaklıkları anlamak için ışığa bakalım: Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a 13 dakikada, Jüpiter'e 43 dakikada, Satürn'e 80 dakikada ulaşır.",
        "spoken": "Uzaklıkları anlamak için ışığa bakalım: Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a on üç dakikada, Jüpiter'e kırk üç dakikada, Satürn'e seksen dakikada ulaşır.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Şimdi sıra sende! Sekiz kâğıda gezegenlerin adını yaz ve Güneş'ten uzaklık sırasına göre yere diz.",
        "spoken": "Şimdi sıra sende! Sekiz kâğıda gezegenlerin adını yaz ve Güneş'ten uzaklık sırasına göre yere diz.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l28",
        "display": "Sonra ilk dördün arasındaki adımlarla son dördün arasındaki adımları karşılaştır. Dış gezegenler ne kadar uzakta, gördün mü?",
        "spoken": "Sonra ilk dördün arasındaki adımlarla son dördün arasındaki adımları karşılaştır. Dış gezegenler ne kadar uzakta, gördün mü?",
        "factIds": [
          "f13"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l29",
        "display": "Bunu biliyor muydun? Güneş ile Dünya arasındaki uzaklığa bir astronomik birim denir: yaklaşık 150 milyon kilometre.",
        "spoken": "Bunu biliyor muydun? Güneş ile Dünya arasındaki uzaklığa bir astronomik birim denir: yaklaşık yüz elli milyon kilometre.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l30",
        "display": "Hızlı soru! Güneş Sistemi'nin en sıcak gezegeni hangisi?",
        "spoken": "Hızlı soru! Güneş Sistemi'nin en sıcak gezegeni hangisi?",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l31",
        "display": "Düşün bakalım... Evet: Venüs! Güneş'e en yakın gezegen olmasa da.",
        "spoken": "Düşün bakalım... Evet: Venüs! Güneş'e en yakın gezegen olmasa da.",
        "factIds": [
          "f6",
          "f7"
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
        "display": "Abone olmayı ve zili açmayı unutma.",
        "spoken": "Abone olmayı ve zili açmayı unutma.",
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
    "statement": "Güneş sistemimizde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ve asteroit vardır.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Güneş sistemimiz yaklaşık 4,6 milyar yıl önce yoğun bir yıldızlar arası gaz ve toz bulutundan oluştu; bulut çöküp dönen bir disk oluşturdu; Güneş mevcut maddenin %99'undan fazlasını topladı.",
    "numbers": [
      "4.6",
      "99"
    ]
  },
  {
    "id": "f3",
    "statement": "Sekiz gezegen: Merkür, Venüs, Dünya, Mars, Jüpiter, Satürn, Uranüs ve Neptün. İlk dördü katı yüzeyleri olduğu için karasal gezegenlerdir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Asteroit kuşağı, erken güneş sisteminden kalan parçalardan oluşur; Mars ile Jüpiter arasındadır; en büyük cismi cüce gezegen Ceres'tir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Bir cismin gezegen sayılması için bir yıldızın çevresinde dolanması, küre biçimini alacak kadar kütle çekimine sahip olması ve yörüngesinin çevresini benzer boyuttaki cisimlerden temizlemiş olması gerekir. Plüton 2006'da cüce gezegen olarak yeniden sınıflandırıldı; yörüngesini temizleyemedi.",
    "numbers": [
      "2006"
    ]
  },
  {
    "id": "f6",
    "statement": "Merkür Güneş'e en yakın ve en küçük gezegendir.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Venüs'ün kalın atmosferi ısıyı hapseder ve onu güneş sisteminin en sıcak gezegeni yapar; yüzey sıcaklığı kurşunu eritecek kadardır: yaklaşık 467 santigrat derece; atmosferi çoğunlukla karbondioksittir; Venüs çoğu gezegenin tersi yönde, yavaşça döner.",
    "numbers": [
      "467"
    ]
  },
  {
    "id": "f8",
    "statement": "Şimdiye kadar güneş sistemimizde yaşam bulduğumuz tek yer Dünya'dır; Dünya Güneş'ten üçüncü gezegendir.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Mars'ın kırmızı görünmesinin nedeni kayalardaki demirin paslanmasıdır; güneş sisteminin en büyük yanardağı Olympus Mons Mars'tadır; Mars'ın iki küçük uydusu vardır: Phobos ve Deimos.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Jüpiter en büyük gezegendir; içi boş bir kabuk olsaydı içine 1.000 Dünya sığardı; Dünya bir üzüm olsaydı Jüpiter bir basketbol topu kadar olurdu; Büyük Kırmızı Leke, Dünya'dan büyük, yüzlerce yıldır süren dev bir fırtınadır; Jüpiter'in Uluslararası Astronomi Birliği'nin resmen tanıdığı 115 uydusu vardır.",
    "numbers": [
      "1.000",
      "115"
    ]
  },
  {
    "id": "f11",
    "statement": "Satürn'ün halkaları, toz gibi maddelerle kaplı milyarlarca küçük buz ve kaya parçasından oluşur; Satürn ortalama yoğunluğu sudan az olan tek gezegendir; Mart 2025 itibarıyla 274 doğrulanmış uydusu vardı.",
    "numbers": [
      "2025",
      "274"
    ]
  },
  {
    "id": "f12",
    "statement": "Uranüs Güneş'ten yedinci ve en büyük üçüncü gezegendir; Neptün sekizinci ve en uzak gezegendir.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Bir astronomik birim, Güneş ile Dünya arasındaki uzaklıktır: yaklaşık 150 milyon kilometre. Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a 13 dakikada, Jüpiter'e 43 dakikada, Satürn'e 80 dakikada ulaşır.",
    "numbers": [
      "150",
      "13",
      "43",
      "80"
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
