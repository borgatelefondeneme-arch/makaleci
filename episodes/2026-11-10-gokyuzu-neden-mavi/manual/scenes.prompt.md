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
  - "source-card": künye kartı (yazar/kurum/dergi/DOI otomatik dolar) — künyenin okunduğu satırlar için zorunlu.
  - "big-number": tek çarpıcı sayı { value, unit?, label, sub? }. "value" makaledeki yazımla.
  - "bar-chart": 2–6 çubuk { title, unit?, bars: [{ label, value (sayı), display (ekranda yazılacak hali), highlight? }] }.
  - "line-chart": zaman/sıra içinde değişim { title, xLabel, yLabel, points: [...] }.
  - "comparison": iki şeyin yan yana kıyası { title, left: { title, value?, items[] }, right: {...} }.
  - "diagram": 2–5 adımlı süreç { title, layout: "flow" | "cycle", nodes: [{ label, emoji? }] } — yöntem anlatımı için ideal.
  - "analogy": benzetme { template: "scale" (alan kıyası) | "fill" (dolan kap) | "race" (yarış) | "zoom" (iç içe ölçek), title, a: { label, value, display? }, b: {...}, caption }. Benzetmede makalede olmayan sayı gösterme; "display" boş bırakılırsa sayı yazılmaz, yalnızca oran çizilir.
  - "quote-card": makaleden kısa alıntı { quote (Türkçe çeviri, en çok iki cümle), attribution }.
  - "bullets": 1–4 madde { title, items[], tone?: "neutral" | "caution" } — sınırlılıklar için "caution".
  - "outro": kapanış — son sahne, summary bölümünün tüm satırlarını kapsar.
- "mascot": karakter Zerre'nin bu sahnedeki hali { state: "idle" | "talk" | "point" | "think", x, y (0–1, ekran oranı, merkez), scale (0,5–1,6), pointAt? }.
  İçerik sol-ortadadır; Zerre genelde sağda durur (x≈0,86, y≈0,62, scale≈1). Geniş sahnelerde (bar-chart, line-chart, diagram, analogy, comparison) küçülüp köşeye çekilsin (x≈0,9, y≈0,72, scale≈0,7). "hook" sahnesinde solda ve büyük (x≈0,17, y≈0,5, scale≈1,6, state "think"). Bir sayıya ya da grafiğe dikkat çekerken "point" kullan ve "pointAt" ile hedefi ver. Sahneden sahneye konum ve boyut değişsin ki karakter ekranda gezsin.

<senaryo>
[
  {
    "id": "hook",
    "lines": [
      {
        "id": "l1",
        "display": "Başını kaldır ve gökyüzüne bak. Masmavi, değil mi?",
        "spoken": "Başını kaldır ve gökyüzüne bak. Masmavi, değil mi?",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Peki neden yeşil değil? Ya da mor? Ya da pembe?",
        "spoken": "Peki neden yeşil değil? Ya da mor? Ya da pembe?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Gökyüzü neden başka bir renk değil de mavi? Hadi, bu sırrı birlikte çözelim!",
        "spoken": "Gökyüzü neden başka bir renk değil de mavi? Hadi, bu sırrı birlikte çözelim!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Merhaba! Ben senin robot arkadaşınım. Her gün, merak ettiğin bir soruyu birlikte araştırıyoruz.",
        "spoken": "Merhaba! Ben senin robot arkadaşınım. Her gün, merak ettiğin bir soruyu birlikte araştırıyoruz.",
        "factIds": []
      },
      {
        "id": "l5",
        "display": "Bugün üç şeyi merak ediyoruz. Gökyüzü neden mavi? Ufka doğru rengi neden açılıyor? Ve gün batımı neden kızıl?",
        "spoken": "Bugün üç şeyi merak ediyoruz. Gökyüzü neden mavi? Ufka doğru rengi neden açılıyor? Ve gün batımı neden kızıl?",
        "factIds": []
      },
      {
        "id": "l6",
        "display": "Bugünkü bilgilerimiz, uzay ajansı NASA'nın bilim sayfalarından geliyor: NASA Space Place ve NASA Science.",
        "spoken": "Bugünkü bilgilerimiz, uzay ajansı Nasa'nın bilim sayfalarından geliyor: Nasa Speys Pleys ve Nasa Sayıns.",
        "factIds": []
      },
      {
        "id": "l7",
        "display": "Kaynakların bağlantılarını videonun açıklamasında bulabilirsin.",
        "spoken": "Kaynakların bağlantılarını videonun açıklamasında bulabilirsin.",
        "factIds": []
      },
      {
        "id": "l8",
        "display": "Her şey Güneş'le başlıyor. Güneş bizden yaklaşık 150 milyon kilometre uzakta!",
        "spoken": "Her şey Güneş'le başlıyor. Güneş bizden yaklaşık yüz elli milyon kilometre uzakta!",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l9",
        "display": "Işığı bu upuzun yolu aşıp Dünya'mıza kadar geliyor.",
        "spoken": "Işığı bu upuzun yolu aşıp Dünya'mıza kadar geliyor.",
        "factIds": [
          "f14"
        ]
      }
    ]
  },
  {
    "id": "method",
    "lines": [
      {
        "id": "l10",
        "display": "Güneş ışığı gözümüze beyaz görünür. Ama aslında içinde gökkuşağının bütün renkleri saklıdır!",
        "spoken": "Güneş ışığı gözümüze beyaz görünür. Ama aslında içinde gökkuşağının bütün renkleri saklıdır!",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l11",
        "display": "Kırmızı, sarı, yeşil, mavi... Hepsi bir araya gelince ışık beyaz görünür.",
        "spoken": "Kırmızı, sarı, yeşil, mavi... Hepsi bir araya gelince ışık beyaz görünür.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l12",
        "display": "Gökkuşağına baktığında gördüğün o renklerin hepsi, Güneş ışığının içinde zaten vardır.",
        "spoken": "Gökkuşağına baktığında gördüğün o renklerin hepsi, Güneş ışığının içinde zaten vardır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l13",
        "display": "Işık, tıpkı denizdeki dalgalar gibi, dalga dalga yol alır.",
        "spoken": "Işık, tıpkı denizdeki dalgalar gibi, dalga dalga yol alır.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l14",
        "display": "Bir ip düşün. Ucundan yavaşça sallarsan uzun ve sakin dalgalar oluşur. Hızlı hızlı sallarsan kısa ve kıpır kıpır dalgalar!",
        "spoken": "Bir ip düşün. Ucundan yavaşça sallarsan uzun ve sakin dalgalar oluşur. Hızlı hızlı sallarsan kısa ve kıpır kıpır dalgalar!",
        "factIds": []
      },
      {
        "id": "l15",
        "display": "Işığın renkleri de böyledir. Bazı renkler uzun ve sakin dalgalarla, bazıları kısa ve kıpır kıpır dalgalarla ilerler.",
        "spoken": "Işığın renkleri de böyledir. Bazı renkler uzun ve sakin dalgalarla, bazıları kısa ve kıpır kıpır dalgalarla ilerler.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l16",
        "display": "Mavi ışığın dalgaları, kırmızı ışığın dalgalarından daha kısadır. Bunu aklında tut, çünkü birazdan çok işimize yarayacak!",
        "spoken": "Mavi ışığın dalgaları, kırmızı ışığın dalgalarından daha kısadır. Bunu aklında tut, çünkü birazdan çok işimize yarayacak!",
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
        "id": "l17",
        "display": "Şimdi işin sırrına geliyoruz. Dünya'mızın çevresi, atmosfer dediğimiz bir hava katmanıyla sarılıdır.",
        "spoken": "Şimdi işin sırrına geliyoruz. Dünya'mızın çevresi, atmosfer dediğimiz bir hava katmanıyla sarılıdır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l18",
        "display": "Güneş ışığı atmosfere girince havadaki gazlara ve minicik parçacıklara çarpar.",
        "spoken": "Güneş ışığı atmosfere girince havadaki gazlara ve minicik parçacıklara çarpar.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l19",
        "display": "Havayı göremeyiz ama içi gazlarla ve parçacıklarla doludur.",
        "spoken": "Havayı göremeyiz ama içi gazlarla ve parçacıklarla doludur.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l20",
        "display": "Çarpan ışık her yöne doğru saçılır. Tıpkı oradan oraya seken küçük toplar gibi!",
        "spoken": "Çarpan ışık her yöne doğru saçılır. Tıpkı oradan oraya seken küçük toplar gibi!",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l21",
        "display": "Ama bütün renkler aynı ölçüde saçılmaz.",
        "spoken": "Ama bütün renkler aynı ölçüde saçılmaz.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l22",
        "display": "Mavi ışık kısa ve küçük dalgalarla ilerlediği için diğer renklerden daha çok saçılır.",
        "spoken": "Mavi ışık kısa ve küçük dalgalarla ilerlediği için diğer renklerden daha çok saçılır.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l23",
        "display": "Her yana dağılan bu mavi ışık, gökyüzünün her köşesinden gözümüze ulaşır. İşte bu yüzden gökyüzünü mavi görürüz!",
        "spoken": "Her yana dağılan bu mavi ışık, gökyüzünün her köşesinden gözümüze ulaşır. İşte bu yüzden gökyüzünü mavi görürüz!",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l24",
        "display": "Yani mavi renk tek bir yerden gelmez. Gökyüzünün her yanından bize doğru saçılır.",
        "spoken": "Yani mavi renk tek bir yerden gelmez. Gökyüzünün her yanından bize doğru saçılır.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l25",
        "display": "Peki ufka doğru baktığında gökyüzünün renginin açıldığını hiç fark ettin mi?",
        "spoken": "Peki ufka doğru baktığında gökyüzünün renginin açıldığını hiç fark ettin mi?",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l26",
        "display": "Ufka yakın yerlerde gökyüzü açık maviye, hatta beyaza döner. Çünkü orada ışık o kadar çok saçılır ki renkler yeniden birbirine karışır.",
        "spoken": "Ufka yakın yerlerde gökyüzü açık maviye, hatta beyaza döner. Çünkü orada ışık o kadar çok saçılır ki renkler yeniden birbirine karışır.",
        "factIds": [
          "f7",
          "f8"
        ]
      },
      {
        "id": "l27",
        "display": "Akşam olunca gökyüzü bu kez kızıla boyanır. Neden mi?",
        "spoken": "Akşam olunca gökyüzü bu kez kızıla boyanır. Neden mi?",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l28",
        "display": "Güneş alçaldıkça ışığı bize ulaşmak için atmosferin içinde daha uzun bir yol kat eder.",
        "spoken": "Güneş alçaldıkça ışığı bize ulaşmak için atmosferin içinde daha uzun bir yol kat eder.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l29",
        "display": "Bu uzun yolda mavi ışık daha da çok saçılır. Kırmızılar ve sarılar ise dosdoğru gözümüze ulaşır.",
        "spoken": "Bu uzun yolda mavi ışık daha da çok saçılır. Kırmızılar ve sarılar ise dosdoğru gözümüze ulaşır.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l30",
        "display": "Gün batımının o güzel kızıl ve sarı renkleri işte böyle ortaya çıkar.",
        "spoken": "Gün batımının o güzel kızıl ve sarı renkleri işte böyle ortaya çıkar.",
        "factIds": [
          "f10"
        ]
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l31",
        "display": "Şimdi sıra sende! Küçük bir gökyüzü dedektifi olmaya ne dersin?",
        "spoken": "Şimdi sıra sende! Küçük bir gökyüzü dedektifi olmaya ne dersin?",
        "factIds": []
      },
      {
        "id": "l32",
        "display": "Dışarı çıktığında önce yukarıya, sonra ufka doğru bak. Renk nasıl değişiyor?",
        "spoken": "Dışarı çıktığında önce yukarıya, sonra ufka doğru bak. Renk nasıl değişiyor?",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l33",
        "display": "Akşam olunca da gün batımındaki renkleri izle ve gördüklerini bir kâğıda çiz.",
        "spoken": "Akşam olunca da gün batımındaki renkleri izle ve gördüklerini bir kâğıda çiz.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l34",
        "display": "Gözlemlerini ailenle ya da arkadaşlarınla paylaş. Bakalım onlar bu sırrı biliyor mu?",
        "spoken": "Gözlemlerini ailenle ya da arkadaşlarınla paylaş. Bakalım onlar bu sırrı biliyor mu?",
        "factIds": []
      },
      {
        "id": "l35",
        "display": "Yalnız unutma: Güneş'e asla doğrudan bakma. Gözlerin çok değerli!",
        "spoken": "Yalnız unutma: Güneş'e asla doğrudan bakma. Gözlerin çok değerli!",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l36",
        "display": "Bunu biliyor muydun? Her gezegenin gökyüzü mavi değildir!",
        "spoken": "Bunu biliyor muydun? Her gezegenin gökyüzü mavi değildir!",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l37",
        "display": "Mars'ın havası bizimkinden çok farklıdır. Çok incedir ve çoğunlukla karbondioksit gazından oluşur.",
        "spoken": "Mars'ın havası bizimkinden çok farklıdır. Çok incedir ve çoğunlukla karbondioksit gazından oluşur.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l38",
        "display": "Üstelik ince toz parçacıklarıyla doludur.",
        "spoken": "Üstelik ince toz parçacıklarıyla doludur.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l39",
        "display": "Bu yüzden Mars'ta gündüzleri gökyüzü turuncu ya da kızılımsı görünür.",
        "spoken": "Bu yüzden Mars'ta gündüzleri gökyüzü turuncu ya da kızılımsı görünür.",
        "factIds": [
          "f11",
          "f13"
        ]
      },
      {
        "id": "l40",
        "display": "Güneş batarken ise Güneş'in çevresi mavi-gri bir renge bürünür. Bizim gökyüzümüzden ne kadar farklı, değil mi?",
        "spoken": "Güneş batarken ise Güneş'in çevresi mavi-gri bir renge bürünür. Bizim gökyüzümüzden ne kadar farklı, değil mi?",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l41",
        "display": "Şimdi hızlı bir soru! Hangi renk ışık havada daha çok saçılır?",
        "spoken": "Şimdi hızlı bir soru! Hangi renk ışık havada daha çok saçılır?",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l42",
        "display": "Biraz düşün... Evet, bildin: Mavi!",
        "spoken": "Biraz düşün... Evet, bildin: Mavi!",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l43",
        "display": "Bir soru daha! Güneş ışığı gözümüze hangi renk görünür?",
        "spoken": "Bir soru daha! Güneş ışığı gözümüze hangi renk görünür?",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l44",
        "display": "Evet, beyaz! Ama içinde bütün renkler saklı.",
        "spoken": "Evet, beyaz! Ama içinde bütün renkler saklı.",
        "factIds": [
          "f1"
        ]
      }
    ]
  },
  {
    "id": "summary",
    "lines": [
      {
        "id": "l45",
        "display": "Bugün bunu öğrendik!",
        "spoken": "Bugün bunu öğrendik!",
        "factIds": []
      },
      {
        "id": "l46",
        "display": "Bir: Güneş ışığı beyaz görünür ama içinde gökkuşağının bütün renkleri vardır.",
        "spoken": "Bir: Güneş ışığı beyaz görünür ama içinde gökkuşağının bütün renkleri vardır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l47",
        "display": "İki: Hava, mavi ışığı diğer renklerden daha çok saçar. Gökyüzü bu yüzden mavidir.",
        "spoken": "İki: Hava, mavi ışığı diğer renklerden daha çok saçar. Gökyüzü bu yüzden mavidir.",
        "factIds": [
          "f5",
          "f6"
        ]
      },
      {
        "id": "l48",
        "display": "Üç: Gün batımında ışık daha uzun yol kat eder. Mavi saçılır, kırmızı ve sarı bize ulaşır.",
        "spoken": "Üç: Gün batımında ışık daha uzun yol kat eder. Mavi saçılır, kırmızı ve sarı bize ulaşır.",
        "factIds": [
          "f9",
          "f10"
        ]
      },
      {
        "id": "l49",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda senin sorunu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda senin sorunu araştırırız!",
        "factIds": []
      },
      {
        "id": "l50",
        "display": "Abone olmayı ve zili açmayı unutma. Merak etmeye devam!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Merak etmeye devam!",
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
    "statement": "Güneş ışığı beyaz görünür ama gökkuşağının bütün renklerinden oluşur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Işık enerjisi, okyanustaki enerji gibi dalgalar halinde yol alır.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Bazı ışık kısa ve kıpırtılı, bazı ışık uzun ve sakin dalgalarla ilerler.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Mavi ışığın dalgaları kırmızı ışığın dalgalarından kısadır.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Güneş ışığı atmosfere ulaşınca havadaki gazlar ve parçacıklar tarafından her yöne saçılır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Mavi ışık kısa ve küçük dalgalarla ilerlediği için diğer renklerden daha çok saçılır.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Ufka yaklaştıkça gökyüzü açık maviye ya da beyaza döner.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Çok fazla saçılma renkleri yeniden karıştırır; daha çok beyaz, daha az mavi görürüz.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Güneş alçaldıkça ışığı bize ulaşmak için atmosferin daha fazlasından geçer.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "Gün batımında mavi ışık daha da çok saçılır; kırmızılar ve sarılar doğrudan göze ulaşır.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "Mars'ta gündüz gökyüzü turuncu ya da kızılımsı görünür.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Mars'ta Güneş batarken Güneş'in çevresindeki gökyüzü mavi-gri bir ton alır.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Mars'ın atmosferi çok incedir, çoğunlukla karbondioksitten oluşur ve ince toz parçacıklarıyla doludur.",
    "numbers": []
  },
  {
    "id": "f14",
    "statement": "Güneş Dünya'dan yaklaşık 150 milyon kilometre uzaktadır.",
    "numbers": [
      "150"
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
