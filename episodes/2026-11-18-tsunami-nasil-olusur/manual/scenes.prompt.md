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
        "display": "Okyanusun ortasında bir gemidesin. Altından bir dalga geçiyor ama fark etmiyorsun bile. Oysa o dalga, kıyıya varınca dev bir duvara dönüşebilir!",
        "spoken": "Okyanusun ortasında bir gemidesin. Altından bir dalga geçiyor ama fark etmiyorsun bile. Oysa o dalga, kıyıya varınca dev bir duvara dönüşebilir!",
        "factIds": [
          "f6",
          "f7"
        ]
      },
      {
        "id": "l2",
        "display": "Bu sessiz yolcu bir tsunami. Peki nasıl oluşur?",
        "spoken": "Bu sessiz yolcu bir tsunami. Peki nasıl oluşur?",
        "factIds": []
      },
      {
        "id": "l3",
        "display": "Bugün tsunaminin bilimini ve ondan nasıl korunacağımızı öğreniyoruz!",
        "spoken": "Bugün tsunaminin bilimini ve ondan nasıl korunacağımızı öğreniyoruz!",
        "factIds": []
      }
    ]
  },
  {
    "id": "context",
    "lines": [
      {
        "id": "l4",
        "display": "Üç sorumuz var. Tsunami neden oluşur? Kıyıya yaklaşınca neden büyür? Ve tehlike anında ne yapmalıyız?",
        "spoken": "Üç sorumuz var. Tsunami neden oluşur? Kıyıya yaklaşınca neden büyür? Ve tehlike anında ne yapmalıyız?",
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
        "display": "ABD Ulusal Okyanus ve Atmosfer İdaresi NOAA'ya göre tsunami, okyanus suyunun büyük ve ani biçimde yerinden oynamasıyla oluşan bir dizi son derece uzun dalgadır.",
        "spoken": "ABD Ulusal Okyanus ve Atmosfer İdaresi Noa'ya göre tsunami, okyanus suyunun büyük ve ani biçimde yerinden oynamasıyla oluşan bir dizi son derece uzun dalgadır.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l7",
        "display": "Bunun en sık nedeni, okyanus tabanının altında ya da yakınında olan bir depremdir.",
        "spoken": "Bunun en sık nedeni, okyanus tabanının altında ya da yakınında olan bir depremdir.",
        "factIds": [
          "f1"
        ]
      },
      {
        "id": "l8",
        "display": "Tsunamilerin çoğu, iki levhanın birbirine doğru yaklaştığı sınırlardaki depremlerden kaynaklanır. Heyelanlar ve volkanik etkinlik de tsunamiye yol açabilir.",
        "spoken": "Tsunamilerin çoğu, iki levhanın birbirine doğru yaklaştığı sınırlardaki depremlerden kaynaklanır. Heyelanlar ve volkanik etkinlik de tsunamiye yol açabilir.",
        "factIds": [
          "f3"
        ]
      },
      {
        "id": "l9",
        "display": "NOAA'ya göre 1900'den bu yana olası tsunamilerin yüzde 80'inden fazlası depremlerle oluştu.",
        "spoken": "Noa'ya göre bin dokuz yüzden bu yana olası tsunamilerin yüzde sekseninden fazlası depremlerle oluştu.",
        "factIds": [
          "f4"
        ]
      },
      {
        "id": "l10",
        "display": "Benim de sarsıntılarım olur, ama sadece fanım çalışınca. Neyse ki o tsunami yapmıyor!",
        "spoken": "Benim de sarsıntılarım olur, ama sadece fanım çalışınca. Neyse ki o tsunami yapmıyor!",
        "factIds": []
      }
    ]
  },
  {
    "id": "finding",
    "lines": [
      {
        "id": "l11",
        "display": "Sıradan dalgalar sadece yüzeyde oluşur. Tsunami ise okyanus tabanından yüzeyine kadar bütün su sütununu hareket ettirir.",
        "spoken": "Sıradan dalgalar sadece yüzeyde oluşur. Tsunami ise okyanus tabanından yüzeyine kadar bütün su sütununu hareket ettirir.",
        "factIds": [
          "f2"
        ]
      },
      {
        "id": "l12",
        "display": "Derin okyanusta bir tsunami jet uçağı kadar hızlı gidebilir! Ben o kadar hızlı gidemem, tekerleğim bile yok! Dalga boyu, yani bir tepeden ötekine uzaklık, yüzlerce mil olabilir.",
        "spoken": "Derin okyanusta bir tsunami jet uçağı kadar hızlı gidebilir! Ben o kadar hızlı gidemem, tekerleğim bile yok! Dalga boyu, yani bir tepeden ötekine uzaklık, yüzlerce mil olabilir.",
        "factIds": [
          "f5"
        ]
      },
      {
        "id": "l13",
        "display": "Ama derin suda tepesi çok alçaktır; okyanusun olağan dalgalanmasının çok az üstüne çıkar. Bu yüzden gemiler onu fark etmeyebilir.",
        "spoken": "Ama derin suda tepesi çok alçaktır; okyanusun olağan dalgalanmasının çok az üstüne çıkar. Bu yüzden gemiler onu fark etmeyebilir.",
        "factIds": [
          "f6"
        ]
      },
      {
        "id": "l14",
        "display": "Tsunami ancak karaya yaklaşınca tehlikeli olur. Kıyıya yakın sığ suya girince yavaşlar.",
        "spoken": "Tsunami ancak karaya yaklaşınca tehlikeli olur. Kıyıya yakın sığ suya girince yavaşlar.",
        "factIds": [
          "f6",
          "f7"
        ]
      },
      {
        "id": "l15",
        "display": "Yavaşlarken dalga boyu kısalır, yüksekliği artar ve akıntılar güçlenir. Arkadan gelen su öndekine yığılır gibi olur.",
        "spoken": "Yavaşlarken dalga boyu kısalır, yüksekliği artar ve akıntılar güçlenir. Arkadan gelen su öndekine yığılır gibi olur.",
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
        "id": "l16",
        "display": "Tsunamiden korunmanın ilk adımı doğanın uyarılarını tanımaktır. NOAA'ya göre güçlü ya da uzun bir deprem bir işarettir.",
        "spoken": "Tsunamiden korunmanın ilk adımı doğanın uyarılarını tanımaktır. Noa'ya göre güçlü ya da uzun bir deprem bir işarettir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l17",
        "display": "Okyanustan gelen tren ya da uçak sesine benzer yüksek bir uğultu da bir işarettir.",
        "spoken": "Okyanustan gelen tren ya da uçak sesine benzer yüksek bir uğultu da bir işarettir.",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l18",
        "display": "Ve denizin gelgitle ilgisi olmayan bir biçimde aniden yükselmesi ya da çekilmesi!",
        "spoken": "Ve denizin gelgitle ilgisi olmayan bir biçimde aniden yükselmesi ya da çekilmesi!",
        "factIds": [
          "f8"
        ]
      },
      {
        "id": "l19",
        "display": "Bu işaretleri görürsen resmi uyarıyı beklemeye vakit olmayabilir. Hemen yüksek bir yere ya da olabildiğince iç kesimlere git.",
        "spoken": "Bu işaretleri görürsen resmi uyarıyı beklemeye vakit olmayabilir. Hemen yüksek bir yere ya da olabildiğince iç kesimlere git.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l20",
        "display": "İlk dalga son ya da en büyük dalga olmayabilir. Yetkililer güvenli diyene kadar kıyıya dönme.",
        "spoken": "İlk dalga son ya da en büyük dalga olmayabilir. Yetkililer güvenli diyene kadar kıyıya dönme.",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l21",
        "display": "Bilim insanları da nöbette. DART denen şamandıralar deniz seviyesindeki küçük değişiklikleri algılar ve tsunami uyarı merkezlerine iletir.",
        "spoken": "Bilim insanları da nöbette. DART denen şamandıralar deniz seviyesindeki küçük değişiklikleri algılar ve tsunami uyarı merkezlerine iletir.",
        "factIds": [
          "f10"
        ]
      },
      {
        "id": "l22",
        "display": "Ben de nöbet tutarım. Ama genelde şarj aletimin başında!",
        "spoken": "Ben de nöbet tutarım. Ama genelde şarj aletimin başında!",
        "factIds": []
      },
      {
        "id": "l23",
        "display": "Şimdi sıra sende! Bir yetişkinle uzun bir tepsiye biraz su koy. Bir ucuna kitapla hafif bir yokuş yap: bu senin kıyın.",
        "spoken": "Şimdi sıra sende! Bir yetişkinle uzun bir tepsiye biraz su koy. Bir ucuna kitapla hafif bir yokuş yap: bu senin kıyın.",
        "factIds": [
          "f7"
        ]
      },
      {
        "id": "l24",
        "display": "Tepsinin diğer ucunu bir kez hafifçe kaldırıp bırak. Dalga yokuşa yaklaşınca nasıl değişiyor? Suyu taşırmamaya dikkat et; ıslak robot hiç hoş değil!",
        "spoken": "Tepsinin diğer ucunu bir kez hafifçe kaldırıp bırak. Dalga yokuşa yaklaşınca nasıl değişiyor? Suyu taşırmamaya dikkat et; ıslak robot hiç hoş değil!",
        "factIds": [
          "f7"
        ]
      }
    ]
  },
  {
    "id": "limitations",
    "lines": [
      {
        "id": "l25",
        "display": "Bunu biliyor muydun? 2004 Hint Okyanusu tsunamisi 17 ülkeyi etkiledi. NOAA'ya göre o günden bu yana tsunami uyarı sistemleri çok gelişti.",
        "spoken": "Bunu biliyor muydun? İki bin dört Hint Okyanusu tsunamisi on yedi ülkeyi etkiledi. Noa'ya göre o günden bu yana tsunami uyarı sistemleri çok gelişti.",
        "factIds": [
          "f11"
        ]
      },
      {
        "id": "l26",
        "display": "Hızlı soru! Deniz aniden çekilirse ne yapmalısın?",
        "spoken": "Hızlı soru! Deniz aniden çekilirse ne yapmalısın?",
        "factIds": [
          "f8",
          "f9"
        ]
      },
      {
        "id": "l27",
        "display": "Düşün bakalım... Evet: hemen yüksek bir yere gitmelisin!",
        "spoken": "Düşün bakalım... Evet: hemen yüksek bir yere gitmelisin!",
        "factIds": [
          "f9"
        ]
      },
      {
        "id": "l28",
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
        "id": "l29",
        "display": "İşte bugün öğrendiklerimiz!",
        "spoken": "İşte bugün öğrendiklerimiz!",
        "factIds": []
      },
      {
        "id": "l30",
        "display": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "spoken": "Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!",
        "factIds": []
      },
      {
        "id": "l31",
        "display": "Abone olmayı ve zili açmayı unutma. Tsunamiler seyrektir, ama hazırlıklı olmak her zaman akıllıcadır!",
        "spoken": "Abone olmayı ve zili açmayı unutma. Tsunamiler seyrektir, ama hazırlıklı olmak her zaman akıllıcadır!",
        "factIds": [
          "f12"
        ]
      }
    ]
  }
]
</senaryo>

<olgular>
[
  {
    "id": "f1",
    "statement": "Tsunami, okyanus suyunun büyük ve ani biçimde yerinden oynamasıyla oluşan bir dizi son derece uzun dalgadır; bu genellikle okyanus tabanının altında ya da yakınında olan bir depremin sonucudur.",
    "numbers": []
  },
  {
    "id": "f2",
    "statement": "Tsunamiler okyanus tabanından yüzeyine kadar tüm su sütunu boyunca hareket eder.",
    "numbers": []
  },
  {
    "id": "f3",
    "statement": "Tsunamilerin çoğu yakınlaşan levha sınırlarındaki depremlerden kaynaklanır; heyelanlar ve volkanik etkinlik de tsunamiye yol açabilir.",
    "numbers": []
  },
  {
    "id": "f4",
    "statement": "1900'den bu yana olası tsunamilerin yüzde 80'inden fazlası depremlerle oluştu.",
    "numbers": [
      "1900",
      "80"
    ]
  },
  {
    "id": "f5",
    "statement": "Derin okyanusta bir tsunami jet uçağı kadar hızlı hareket edebilir; dalga boyu, yani tepeden tepeye uzaklık, yüzlerce mil olabilir.",
    "numbers": []
  },
  {
    "id": "f6",
    "statement": "Derin suda dalganın tepesi okyanusun olağan dalgalanmasının çok az üstüne çıkar; tsunami ancak karaya yaklaşınca tehlikeli olur.",
    "numbers": []
  },
  {
    "id": "f7",
    "statement": "Tsunami kıyıya yakın sığ suya girince yavaşlar; dalga boyu kısalır, yüksekliği artar ve akıntılar güçlenir.",
    "numbers": []
  },
  {
    "id": "f8",
    "statement": "Doğal uyarı işaretleri arasında güçlü ya da uzun depremler, okyanustan gelen tren ya da uçak sesine benzer yüksek bir uğultu ve gelgitle ilgisi olmayan ani bir deniz yükselmesi ya da çekilmesi vardır.",
    "numbers": []
  },
  {
    "id": "f9",
    "statement": "Resmi uyarıyı beklemeye zaman olmayabilir; tahliye yolu görülmüyorsa yüksek bir yere ya da olabildiğince iç kesimlere gidilmeli; yetkililer güvenli diyene kadar tehlike bölgesinden uzak durulmalı; ilk dalga son, en büyük ya da en yıkıcı dalga olmayabilir.",
    "numbers": []
  },
  {
    "id": "f10",
    "statement": "DART şamandıraları deniz seviyesindeki küçük değişiklikleri algılayıp tsunami uyarı merkezlerine iletebilir; bilim insanları bir sonraki tsunaminin ne zaman ve nerede olacağını önceden kestiremez.",
    "numbers": []
  },
  {
    "id": "f11",
    "statement": "2004 Hint Okyanusu tsunamisi Güneydoğu ve Güney Asya'da 17 ülkeyi etkiledi; o zamandan bu yana tsunami uyarı yetenekleri çok gelişti.",
    "numbers": [
      "2004",
      "17"
    ]
  },
  {
    "id": "f12",
    "statement": "Tsunamiler Dünya'nın en seyrek görülen tehlikelerindendir; tsunaminin mevsimi yoktur ve her okyanus kıyısını her an vurabilir.",
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
