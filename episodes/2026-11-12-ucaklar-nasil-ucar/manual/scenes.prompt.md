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
        "display": "Tonlarca ağırlıktaki bir uçak, bulutların üstünde süzülüyor. Altında yalnızca hava var!",
        "spoken": "Tonlarca ağırlıktaki bir uçak, bulutların üstünde süzülüyor. Altında yalnızca hava var!",
        "factIds": []
      },
      {
        "id": "l2",
        "display": "Smithsonian Müzesi'nin sorduğu gibi: Hava gibi hafif bir şey bütün o ağırlığı nasıl taşır?",
        "spoken": "Smitsonyın Müzesi'nin sorduğu gibi: Hava gibi hafif bir şey bütün o ağırlığı nasıl taşır?",
        "factIds": [
          "f16"
        ]
      },
      {
        "id": "l3",
        "display": "Bugün bir uçağın kanadına binip cevabı arıyoruz!",
        "spoken": "Bugün bir uçağın kanadına binip cevabı arıyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Bir uçağa hangi kuvvetler etki eder? Kanat uçağı nasıl kaldırır? Ve uçak nasıl ilerler, nasıl yön değiştirir?",
        "spoken": "Üç sorumuz var. Bir uçağa hangi kuvvetler etki eder? Kanat uçağı nasıl kaldırır? Ve uçak nasıl ilerler, nasıl yön değiştirir?",
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
        "display": "NASA'ya göre kuvvet, belirli bir yönde bir itme ya da çekmedir. Uçan bir uçağa dört kuvvet etki eder.",
        "spoken": "Nasa'ya göre kuvvet, belirli bir yönde bir itme ya da çekmedir. Uçan bir uçağa dört kuvvet etki eder.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Birincisi ağırlık: uçağı her zaman Dünya'nın merkezine doğru çeker.",
        "spoken": "Birincisi ağırlık: uçağı her zaman Dünya'nın merkezine doğru çeker.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l8",
        "display": "İkincisi kaldırma: ağırlığı yenmek için uçağın ürettiği, yukarı doğru kuvvet.",
        "spoken": "İkincisi kaldırma: ağırlığı yenmek için uçağın ürettiği, yukarı doğru kuvvet.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "Üçüncüsü sürükleme: hava, uçağın ilerlemesine direnir.",
        "spoken": "Üçüncüsü sürükleme: hava, uçağın ilerlemesine direnir.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Dördüncüsü itme: sürüklemeyi yenmek için motorların ürettiği, ileri doğru kuvvet.",
        "spoken": "Dördüncüsü itme: sürüklemeyi yenmek için motorların ürettiği, ileri doğru kuvvet.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l11",
        "display": "Bu dört kuvvet dengedeyse uçak sabit hızla yol alır. Dengede değilse, en büyük kuvvetin yönünde hızlanır.",
        "spoken": "Bu dört kuvvet dengedeyse uçak sabit hızla yol alır. Dengede değilse, en büyük kuvvetin yönünde hızlanır.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l12",
        "display": "Bende yalnızca bir kuvvet var: tembellik. O da beni koltuğa doğru çekiyor!",
        "spoken": "Bende yalnızca bir kuvvet var: tembellik. O da beni koltuğa doğru çekiyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l13",
        "display": "Şimdi en merak edilen kuvvet: kaldırma. NASA'ya göre kaldırma, hareket eden bir hava akışı katı bir cisim tarafından döndürüldüğünde oluşur.",
        "spoken": "Şimdi en merak edilen kuvvet: kaldırma. Nasa'ya göre kaldırma, hareket eden bir hava akışı katı bir cisim tarafından döndürüldüğünde oluşur.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Kanat havayı aşağı doğru yönlendirir. Newton'un etki-tepki yasasına göre hava da kanadı yukarı iter.",
        "spoken": "Kanat havayı aşağı doğru yönlendirir. Nivtın'un etki-tepki yasasına göre hava da kanadı yukarı iter.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l15",
        "display": "Bunu kanadın hem üst hem alt yüzeyi birlikte yapar. Bu yüzden kanadın altıyla üstü arasında bir basınç farkı oluşur.",
        "spoken": "Bunu kanadın hem üst hem alt yüzeyi birlikte yapar. Bu yüzden kanadın altıyla üstü arasında bir basınç farkı oluşur.",
        "factIds": [
          "f6",
          "f7"
        ]
      },
      {
        "id": "l16",
        "display": "Bir dikkat notu: kaldırmayla ilgili pek çok açıklama yanıltıcıdır. NASA'ya göre üst yüzeyin payını yok sayan açıklamalar yanlış bir kurama götürür.",
        "spoken": "Bir dikkat notu: kaldırmayla ilgili pek çok açıklama yanıltıcıdır. Nasa'ya göre üst yüzeyin payını yok sayan açıklamalar yanlış bir kurama götürür.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Kaldırma için hareket şarttır: kanat ile hava arasında hız farkı olmalıdır. Ve hava şarttır: akışkan yoksa kaldırma da yok!",
        "spoken": "Kaldırma için hareket şarttır: kanat ile hava arasında hız farkı olmalıdır. Ve hava şarttır: akışkan yoksa kaldırma da yok!",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l18",
        "display": "Kaldırmanın büyüklüğü uçağın biçimine, boyutuna ve hızına bağlıdır.",
        "spoken": "Kaldırmanın büyüklüğü uçağın biçimine, boyutuna ve hızına bağlıdır.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l19",
        "display": "Sürükleme ise uçağın biçimine bağlıdır. Pürüzsüz, cilalı bir yüzey, pürüzlü bir yüzeyden daha az sürtünür.",
        "spoken": "Sürükleme ise uçağın biçimine bağlıdır. Pürüzsüz, cilalı bir yüzey, pürüzlü bir yüzeyden daha az sürtünür.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "Ben her sabah cilalanıyorum. Ama uçmak için değil, parlamak için!",
        "spoken": "Ben her sabah cilalanıyorum. Ama uçmak için değil, parlamak için!",
        "factIds": []
      }
    ]
  },
  {
    "id": "importance",
    "lines": [
      {
        "id": "l21",
        "display": "Peki uçak nasıl ilerler? İtme kuvvetini motorlar üretir: pervaneler, jet motorları, hatta roketler.",
        "spoken": "Peki uçak nasıl ilerler? İtme kuvvetini motorlar üretir: pervaneler, jet motorları, hatta roketler.",
        "factIds": [
          "f10",
          "f11"
        ]
      },
      {
        "id": "l22",
        "display": "Jet motorunda sıcak gaz arkadan dışarı fırlar; itme ise uçağı öne doğru iter. Bu da yine etki-tepki yasası.",
        "spoken": "Jet motorunda sıcak gaz arkadan dışarı fırlar; itme ise uçağı öne doğru iter. Bu da yine etki-tepki yasası.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l23",
        "display": "Uçuşta uçak, ağırlık merkezi denen bir nokta çevresinde döner.",
        "spoken": "Uçuşta uçak, ağırlık merkezi denen bir nokta çevresinde döner.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l24",
        "display": "Kanatlardaki ve kuyruktaki hareketli yüzeyler uçağı üç yönde döndürür: yalpa, yunuslama ve sapma. Pilot da dengeyi korumak için kumandaları sürekli ayarlar.",
        "spoken": "Kanatlardaki ve kuyruktaki hareketli yüzeyler uçağı üç yönde döndürür: yalpa, yunuslama ve sapma. Pilot da dengeyi korumak için kumandaları sürekli ayarlar.",
        "factIds": [
          "f12"
        ]
      },
      {
        "id": "l25",
        "display": "Bütün bunlar nasıl başladı? 17 Aralık 1903'te Wright kardeşlerin motorlu uçağı Kitty Hawk'ta havalandı.",
        "spoken": "Bütün bunlar nasıl başladı? On yedi Aralık bin dokuz yüz üçte Rayt kardeşlerin motorlu uçağı Kiti Hok'ta havalandı.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l26",
        "display": "Pilot Orville'di. İlk uçuş yalnızca 12 saniye sürdü ve 36 metre gitti.",
        "spoken": "Pilot Orvil'di. İlk uçuş yalnızca on iki saniye sürdü ve otuz altı metre gitti.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l27",
        "display": "Aynı günün en iyi uçuşunda ise Wilbur 59 saniyede 255,6 metre yol aldı.",
        "spoken": "Aynı günün en iyi uçuşunda ise Vilbır elli dokuz saniyede iki yüz elli beş virgül altı metre yol aldı.",
        "factIds": [
          "f13"
        ]
      },
      {
        "id": "l28",
        "display": "Wright kardeşler pervaneleri dönen kanatlar gibi tasarladı. Uçağı yönlendirmek için de kanat uçlarını ters yönlere büktüler.",
        "spoken": "Rayt kardeşler pervaneleri dönen kanatlar gibi tasarladı. Uçağı yönlendirmek için de kanat uçlarını ters yönlere büktüler.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l29",
        "display": "Şimdi sıra sende! NASA'ya göre en bilinen planör örneği kâğıt uçaktır. Üç farklı kâğıt uçak katla: biri dar kanatlı, biri geniş kanatlı, biri kanat uçları bükülmüş.",
        "spoken": "Şimdi sıra sende! Nasa'ya göre en bilinen planör örneği kâğıt uçaktır. Üç farklı kâğıt uçak katla: biri dar kanatlı, biri geniş kanatlı, biri kanat uçları bükülmüş.",
        "factIds": [
          "f15"
        ]
      },
      {
        "id": "l30",
        "display": "Hepsini aynı güçle at ve ne kadar uçtuklarını ölç. Kanat biçimi uçuşu nasıl değiştiriyor?",
        "spoken": "Hepsini aynı güçle at ve ne kadar uçtuklarını ölç. Kanat biçimi uçuşu nasıl değiştiriyor?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l31",
        "display": "Uçaklarını insanlara doğru atma; geniş ve boş bir yerde dene.",
        "spoken": "Uçaklarını insanlara doğru atma; geniş ve boş bir yerde dene.",
        "factIds": []
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l32",
        "display": "Bunu biliyor muydun? Wright kardeşler de verimli bir kanat biçimi bulmak için çok uğraştı; doğru kanadı bulmak kolay değildi.",
        "spoken": "Bunu biliyor muydun? Wright kardeşler de verimli bir kanat biçimi bulmak için çok uğraştı; doğru kanadı bulmak kolay değildi.",
        "factIds": [
          "f14"
        ]
      },
      {
        "id": "l33",
        "display": "Hızlı soru! Uçağı yukarı doğru kaldıran kuvvetin adı neydi?",
        "spoken": "Hızlı soru! Uçağı yukarı doğru kaldıran kuvvetin adı neydi?",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l34",
        "display": "Düşün bakalım... Evet: kaldırma!",
        "spoken": "Düşün bakalım... Evet: kaldırma!",
        "factIds": [
          "f3"
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
        "display": "Abone olmayı ve zili açmayı unutma. Kâğıt uçağının ne kadar uçtuğunu da bize yaz!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Kâğıt uçağının ne kadar uçtuğunu da bize yaz!",
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
    "statement": "Kuvvet, belirli bir yönde bir itme ya da çekme olarak düşünülebilir.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Ağırlık her zaman Dünya'nın merkezine doğru yönelen bir kuvvettir; uçuşta uçak ağırlık merkezi denen nokta çevresinde döner.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Ağırlığı yenmek için uçaklar kaldırma denen karşıt bir kuvvet üretir; kaldırmanın büyüklüğü uçağın biçimine, boyutuna ve hızına bağlıdır.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "Hava uçağın hareketine direnir; bu direnç kuvvetine sürükleme denir. Sürüklemeyi yenmek için uçaklar bir itki sistemiyle itme kuvveti üretir.",
    "numbers": []
  },
  {
    "id": "f5",
    "statement": "Kuvvetler dengedeyse uçak sabit hızla yol alır; dengede değilse en büyük kuvvetin yönünde hızlanır.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Kaldırma, hareket eden bir gaz akışı katı bir cisim tarafından döndürüldüğünde oluşur; kaldırma Newton'un etki-tepki yasasına göre ters yönde üretilir; uçak kanadında hem üst hem alt yüzey akışın dönmesine katkıda bulunur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Kaldırma, cisim ile akışkan arasındaki hız farkıyla oluşur; kaldırma için cismin akışkanla temas etmesi gerekir: akışkan yoksa kaldırma da yok. Kaldıran kanadın üst ve alt yüzeyleri arasında basınç farkı vardır.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Kaldırmaya ilişkin açıklamaların birçoğu yanıltıcı ve yanlıştır; üst yüzeyin akışı döndürmedeki payını yok saymak yanlış bir kaldırma kuramına götürür.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Sürükleme, uçağın havadaki hareketine karşı koyan aerodinamik kuvvettir; uçağın biçimine bağlıdır (biçim sürüklemesi); pürüzsüz, cilalı bir yüzey pürüzlü bir yüzeyden daha az sürtünme üretir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "İtme, uçağı havada ilerleten kuvvettir; motorlarda bir itki sistemiyle üretilir; hızlandırılan gazın tersi yönünde oluşur: sıcak gaz arkadan çıkar, itme öne doğru iter (Newton'un etki-tepki yasası).",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "İtki sistemleri arasında pervane, türbin ya da jet motoru, ramjet ve roket vardır.",
    "numbers": []
  },
  {
    "id": "f12",
    "statement": "Uçağı yalpa, yunuslama ve sapma hareketlerinde aerodinamik yüzeyler denetler; pilot uçağı dengede tutmak için kumandaları sürekli ayarlar.",
    "numbers": []
  },
  {
    "id": "f13",
    "statement": "Wright kardeşlerin ilk motorlu uçağı 17 Aralık 1903'te Kitty Hawk'ta uçtu: 12 saniyelik uçuşta 36 metre yol aldı; pilotu Orville'di; günün en iyi uçuşunda Wilbur 59 saniyede 255,6 metre gitti.",
    "numbers": [
      "17",
      "1903",
      "12",
      "36",
      "59",
      "255.6"
    ]
  },
  {
    "id": "f14",
    "statement": "Wright kardeşler pervaneleri dönen kanatlar olarak tasarladı; kanat uçlarını ters yönlerde bükerek uçağı yönlendirdiler; verimli bir kanat kesiti geliştirmekle uğraştılar.",
    "numbers": []
  },
  {
    "id": "f15",
    "statement": "Kâğıt uçaklar en bilinen planör örneğidir.",
    "numbers": []
  },
  {
    "id": "f16",
    "statement": "Bir uçak nasıl havada kalır? Hava gibi hafif bir şey bütün o ağırlığı nasıl taşır?",
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
