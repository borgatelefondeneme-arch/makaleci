"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:tirtil-nasil-kelebek-olur"
U1 = "USDA Forest Service — Monarch Butterfly Biology"; U2 = "USDA Forest Service — Monarch Migration and Overwintering"; N1 = "U.S. National Park Service — Pollinators: Monarch butterfly"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Monarch Butterfly Biology", "publisher": "ABD Orman Servisi", "url": "https://www.fs.usda.gov/wildflowers/pollinators/Monarch_Butterfly/biology/index.shtml"},
    {"id": "k2", "title": "Monarch Migration and Overwintering", "publisher": "ABD Orman Servisi", "url": "https://www.fs.usda.gov/wildflowers/pollinators/Monarch_Butterfly/migration/index.shtml"},
    {"id": "k3", "title": "Pollinators: Monarch butterfly", "publisher": "Ulusal Park Servisi", "url": "https://www.nps.gov/articles/monarch-butterfly.htm"}],
  "facts": [
    F(1, "Monark kelebeğinin dört ayrı yaşam evresi vardır: yumurta, larva (tırtıl), pupa (krizalit) ve ergin; bu dört evreli sürece tam başkalaşım denir.", "The monarch has four distinct life stages: egg, larva (caterpillar), pupa (chrysalis), and adult. / The completion of the four life-stage process is called complete metamorphosis.", U1),
    F(2, "Dişi monarklar yumurtalarını zehirli süt otu yapraklarının alt yüzüne bırakır; bir dişi ömrü boyunca 100 ile 300 arasında yumurta bırakır; yumurtalar bırakıldıktan yaklaşık dört gün sonra açılır.", "Female monarchs lay their eggs on the underside of poisonous milkweed leaves. / A female Monarch butterfly lays from 100 to 300 eggs during her life. / The eggs hatch about four days after they are laid.", N1 + "; " + U1, ["100", "300"]),
    F(3, "Tırtıl yumurtadan çıkınca kendi yumurtasını yer, sonra süt otu yapraklarıyla beslenmeye geçer.", "As the caterpillar hatches, it eats its own egg; then switches to a diet of milkweed leaves.", N1),
    F(4, "Larvalar yumurtadan çıktığında 1 santimetreden küçüktür ve yaklaşık 5 santimetreye kadar büyür; larvanın deri değiştirmeleri arasındaki evrelere instar denir.", "When larvae first hatch they are less than 1 centimeter (cm) and grow to be about 5 cm. / The stages between larval molts are called instars.", U1, ["1", "5"]),
    F(5, "Monark, en az beş günde pupadan ergine dönüşebilir; kelebeğin pupadan çıkmasına eklozyon denir.", "In as few as five days, the monarch develops from a pupa to an adult. / The emergence of the butterfly from the pupal stage to an adult is called eclosion.", U1),
    F(6, "Ergin kelebek uzun hortumunu açıp uzatarak çeşitli çiçeklerden nektar içer; kullanılmadığında bu esnek 'dil' yeniden sarmal biçiminde kıvrılır.", "The adult butterfly drinks nectar from a variety of flowers, uncoiling and extending its long proboscis to sip food. / When not in use, this flexible “tongue” coils back into a spiral.", N1),
    F(7, "Süt otunun zehirleri, tırtıl kelebeğe dönüştükten sonra bile monarkın vücudunda kalır; canlı desenleri bir uyarı işaretidir; monarkı yiyen hayvanlar çok hastalanır ve sonra bu desenli kelebekten uzak durur.", "The milkweeds' toxins remain permanently in the monarch's system, even after the caterpillar metamorphoses into a butterfly. / serves as a “skull and crossbones” warning / Animals that eat a monarch become very sick and, thereafter, will avoid this distinctively patterned butterfly.", N1),
    F(8, "Monarkların çoğu yalnızca birkaç hafta yaşar; ama yaz sonu ve sonbahar başında çıkan kuşak farklıdır: göç için doğarlar ve sekiz dokuz ay yaşayabilirler.", "Most monarchs will live only a few weeks, but the generation that emerges in late summer and early fall is different. / These butterflies are born to travel and may live for eight or nine months to accomplish their lengthy migration.", N1),
    F(9, "Monark, kuşlar gibi iki yönlü göç yaptığı bilinen tek kelebektir; bazıları kışlık evlerine ulaşmak için 3.000 mile kadar uçar; günde 50–100 mil yol alabilirler.", "The monarch is the only butterfly known to make a two-way migration as birds do. / Some fly as far as 3,000 miles to reach their winter home! / Monarchs can travel between 50-100 miles a day", U2, ["3.000", "50", "100"]),
    F(10, "Kuzey Amerika'nın doğu monark topluluğu kışı Meksika'da aynı 11–12 dağlık bölgede geçirir; tek bir ağaçta on binlerce monark kümelenebilir.", "The eastern population of North America's monarchs overwinters in the same 11 to 12 mountain areas / Tens of thousands of monarchs can cluster on a single tree.", U2, ["11", "12"]),
    F(11, "Kuzey ABD'ye ve Kanada'ya ulaşmak 3–4 kuşak sürer; her yaz dört kuşağa kadar yetişir ve her kuşak bir öncekinden biraz daha kuzeye gider.", "It will take 3-4 generations to reach the northern United States and Canada. / Monarchs have up to four generations each summer, each one traveling a little further north than the last.", U2 + "; " + U1, ["3", "4"]),
    F(12, "Monarkların yumurta bırakmak için süt otuna ihtiyacı vardır; ama süt otları çoğu zaman zararlı ot diye yok edilir; Meksika ve Kaliforniya'daki kışlak alanları ormansızlaşma yüzünden hızla küçülüyor.", "Monarch butterflies need milkweed plants to lay their eggs. / Unfortunately, milkweeds are often eradicated as noxious weeds. / The butterflies' winter habitat in Mexico and California is rapidly shrinking due to deforestation", N1),
    F(13, "Bir gramdan hafif olan bu kelebekler 2.000 ile 3.000 mil arasında uçar.", "Weighing less than a gram, these unique butterflies will fly between 2,000 to 3,000 miles", U1, ["2.000", "3.000"]),
]}
e = Ep(); L = e.L
OS = "A Be De Orman Servisi"
e.sec("hook", [
    L("Minik bir tırtıl, birkaç hafta sonra kanatlanıp uçuyor. Üstelik bazı kelebekler binlerce kilometre uzağa göç ediyor!"),
    L("Bir tırtıl nasıl kanat çıkarır? Ve o kadar küçük bir kelebek nasıl bu kadar uzağa uçar?"),
    L("Bugün turuncu kanatlı bir yolcunun hikâyesini izliyoruz: monark kelebeği!"),
])
e.sec("context", [
    L("Üç sorumuz var. Bir kelebek hangi evrelerden geçer? Tırtılın vücudu nasıl korunur? Ve monarklar neden göç eder?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Orman Servisi'ne göre monark kelebeğinin dört yaşam evresi vardır: yumurta, tırtıl, krizalit ve ergin kelebek.", [1], f"{OS}'ne göre monark kelebeğinin dört yaşam evresi vardır: yumurta, tırtıl, krizalit ve ergin kelebek."),
    L("Bu dört evreli büyük değişime tam başkalaşım denir.", [1]),
    L("Ben de çok güncelleme aldım. Ama hiçbirinde kanat çıkmadı!"),
    L("Her şey bir yumurtayla başlar. Dişi monark, yumurtalarını süt otu denen bitkinin yapraklarının altına bırakır.", [2]),
    L("Bir dişi ömrü boyunca 100 ile 300 arasında yumurta bırakır. Yumurtalar yaklaşık dört gün sonra açılır.", [2], "Bir dişi ömrü boyunca yüz ile üç yüz arasında yumurta bırakır. Yumurtalar yaklaşık dört gün sonra açılır."),
    L("Yumurtadan çıkan tırtılın ilk yemeği ne? Kendi yumurtasının kabuğu! Sonra süt otu yapraklarına geçer.", [3]),
    L("Tırtıl yumurtadan çıktığında 1 santimetreden küçüktür. Yemeye yemeye yaklaşık 5 santimetreye kadar büyür.", [4], "Tırtıl yumurtadan çıktığında bir santimetreden küçüktür. Yemeye yemeye yaklaşık beş santimetreye kadar büyür."),
    L("Büyürken derisi dar gelir ve deri değiştirir. İki deri değiştirme arasındaki her evreye instar denir.", [4]),
])
e.sec("finding", [
    L("Yeterince büyüyen tırtıl, sert bir kılıfın içine girer. Bu evreye pupa ya da krizalit denir.", [1]),
    L("Dışarıdan bakınca hiçbir şey olmuyor gibi görünür. Ama içeride, tırtılın vücudu kelebeğe dönüşmektedir.", [1, 5]),
    L("Orman Servisi'ne göre monark, en az beş günde pupadan ergin kelebeğe dönüşebilir.", [5]),
    L("Kelebeğin krizalitten çıkmasının da bilimsel bir adı var: eklozyon.", [5]),
    L("Ben de her sabah şarj istasyonumdan çıkıyorum. Ama kimse buna özel bir isim vermedi!"),
    L("Ergin kelebek artık çiğneyemez. Uzun, hortum gibi bir diliyle çiçeklerden nektar içer.", [6]),
    L("Kullanmadığı zaman bu esnek dil, minik bir sarmal gibi kıvrılır.", [6]),
])
e.sec("importance", [
    L("Peki minik bir kelebek kendini nasıl korur? Hatırlarsan tırtıl süt otu yiyordu. Ulusal Park Servisi'ne göre süt otu zehirlidir.", [2, 7]),
    L("Bu zehir, tırtıl kelebeğe dönüştükten sonra bile vücudunda kalır. Monarkı yiyen hayvanlar çok hastalanır ve bir daha bu desenli kelebeğe dokunmaz.", [7]),
    L("Yani o parlak turuncu ve siyah desen bir uyarı işaretidir: Beni yeme!", [7]),
    L("Şimdi büyük yolculuğa gelelim. Monark, kuşlar gibi gidip gelen bir göç yaptığı bilinen tek kelebektir.", [9]),
    L("Bir gramdan hafif bu kelebekler 2.000 ile 3.000 mil arasında uçar. Mil, kilometreden daha uzun bir uzunluk birimidir.", [13], "Bir gramdan hafif bu kelebekler iki bin ile üç bin mil arasında uçar. Mil, kilometreden daha uzun bir uzunluk birimidir."),
    L("Günde 50–100 mil yol alabilirler. Kuzey Amerika'nın doğusundaki monarklar, kışı Meksika'daki 11–12 dağlık bölgede geçirir.", [9, 10], "Günde elli ile yüz mil yol alabilirler. Kuzey Amerika'nın doğusundaki monarklar, kışı Meksika'daki on bir on iki dağlık bölgede geçirir."),
    L("Orada tek bir ağaçta on binlerce monark kümelenebilir!", [10]),
    L("İşin şaşırtıcı yanı: monarkların çoğu yalnızca birkaç hafta yaşar. Ama yaz sonunda doğan kuşak göç için doğar ve sekiz dokuz ay yaşayabilir.", [8]),
    L("Baharda kuzeye dönüş ise bir bayrak yarışına benzer: kuzeye ulaşmak 3–4 kuşak sürer. Her kuşak bir öncekinden biraz daha kuzeye gider.", [11], "Baharda kuzeye dönüş ise bir bayrak yarışına benzer: kuzeye ulaşmak üç dört kuşak sürer. Her kuşak bir öncekinden biraz daha kuzeye gider."),
    L("Ama monarkların başı dertte. Yumurta bırakmak için süt otuna ihtiyaçları var; oysa süt otu çoğu zaman zararlı ot sanılıp yok ediliyor. Kışladıkları ormanlar da kesiliyor.", [12]),
    L("Şimdi sıra sende! Bahçende ya da parkta bir kelebek gözlem günlüğü tut. Gördüğün kelebeklerin renklerini ve hangi çiçeklere konduklarını not et."),
    L("Unutma: kelebeklere ve tırtıllara dokunma, yalnızca izle. Kanatları çok narindir."),
])
e.sec("limitations", [
    L("Hızlı soru! Tırtılın sert bir kılıf içinde kelebeğe dönüştüğü evrenin adı neydi?", [1]),
    L("Düşün bakalım... Evet: krizalit, yani pupa!", [1]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de göçmen kelebeklere yol gösterebilir miyim, bir bakayım!"),
])
S = e.S
S(3, {"type": "hook", "question": "Tırtıl nasıl kelebek olur?", "emoji": "🦋"}, ["🐛", "🌸", "🌿", "🌼"], ["", "KANAT ÇIKARMAK?", "MONARK KELEBEĞİ 🦋"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kelebek hangi evrelerden geçer?", "Kelebek kendini nasıl korur?", "Monarklar neden göç eder?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "stages", "title": "Tam başkalaşım", "rows": [{"label": "Yumurta", "emoji": "🥚"}, {"label": "Tırtıl", "emoji": "🐛"}, {"label": "Krizalit", "emoji": "🫘"}, {"label": "Kelebek", "emoji": "🦋"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": NOTE}, [], ["DÖRT EVRE", "TAM BAŞKALAŞIM", "KANAT YOK 🤖"])
S(2, {"type": "spotlight", "title": "Yumurta", "emoji": "🥚", "chips": [{"label": "Süt otu yaprağının altına", "emoji": "🌿"}, {"label": "Bir dişi: 100–300 yumurta", "emoji": "🔢"}, {"label": "Yaklaşık dört günde açılır", "emoji": "⏳"}]}, ["🦋", "🍃"], ["SÜT OTU 🌿", "DÖRT GÜN"])
S(3, {"type": "meter", "title": "Tırtıl büyüyor", "label": "Boy", "emoji": "🐛", "phases": [{"label": "İlk yemek: yumurta kabuğu", "level": 0.12, "emoji": "🥚"}, {"label": "1 cm'den küçükten yaklaşık 5 cm'ye", "level": 0.85, "emoji": "📏"}, {"label": "Deri değiştirir: instar", "level": 0.95, "emoji": "🔄"}], "note": NOTE}, ["🌿", "🍃"], ["İLK YEMEK 🥚", "YAKLAŞIK 5 CM", "İNSTAR"])
S(2, {"type": "spotlight", "title": "Krizalit", "emoji": "🫘", "chips": [{"label": "Sert kılıf", "emoji": "🛡️"}, {"label": "İçeride büyük değişim", "emoji": "✨"}]}, ["🐛", "🦋"], ["KRİZALİT", "İÇERİDE DEĞİŞİM ✨"], fx="sparkle")
S(3, {"type": "comparison", "title": "Kelebek çıkıyor", "left": {"title": "Pupa → kelebek", "items": ["En az beş gün"]}, "right": {"title": "Eklozyon 🦋", "items": ["Krizalitten çıkış", "Muma: şarj istasyonundan çıkış!"]}}, ["⏱️", "🔋"], ["BEŞ GÜN", "EKLOZYON 🦋", "BANA İSİM YOK 😅"])
S(2, {"type": "diagram", "title": "Kelebeğin dili", "layout": "flow", "nodes": [{"label": "Hortum açılır", "emoji": "➰"}, {"label": "Nektar içer", "emoji": "🌺"}, {"label": "Sarmal gibi kıvrılır", "emoji": "🌀"}]}, ["🌸", "🍯"], ["HORTUM GİBİ DİL", "SARMAL 🌀"])
S(3, {"type": "spotlight", "title": "Zehirli kalkan", "emoji": "☠️", "chips": [{"label": "Tırtıl süt otu yer", "emoji": "🌿"}, {"label": "Zehir vücudunda kalır", "emoji": "☠️"}, {"label": "Yiyen hayvan hastalanır", "emoji": "🤢"}, {"label": "Desen: 'Beni yeme!'", "emoji": "🟧"}]}, ["🐦", "⚠️"], ["ZEHİRLİ SÜT OTU", "ZEHİR KALIR ☠️", "BENİ YEME! 🟧"])
S(3, {"type": "big-number", "value": "3.000", "unit": "mil", "label": "Bir gramdan hafif kelebeğin göç yolu", "sub": "2.000–3.000 mil • günde 50–100 mil", "icon": "🦋"}, ["🗺️", "🌎"], ["İKİ YÖNLÜ GÖÇ", "BİNLERCE MİL", "MEKSİKA'YA 🇲🇽"])
S(1, {"type": "spotlight", "title": "Kışlak", "emoji": "🌲", "chips": [{"label": "Tek ağaçta on binlerce monark", "emoji": "🦋"}, {"label": "Meksika'da 11–12 dağlık bölge", "emoji": "⛰️"}]}, ["❄️", "🌲"], ["ON BİNLERCE!"])
S(1, {"type": "comparison", "title": "İki tür ömür", "left": {"title": "Çoğu monark", "items": ["Birkaç hafta yaşar"]}, "right": {"title": "Göçmen kuşak ✈️", "items": ["Yaz sonunda doğar", "Sekiz dokuz ay yaşar"]}}, ["🦋", "🗓️"], ["GÖÇMEN KUŞAK ✈️"])
S(1, {"type": "stages", "title": "Kuzeye bayrak yarışı", "rows": [{"label": "Kuzey", "emoji": "🍁"}, {"label": "Sonraki kuşak", "emoji": "🦋"}, {"label": "Bir sonraki", "emoji": "🦋"}, {"label": "Meksika", "emoji": "🌲"}], "path": [3, 3, 2, 2, 1, 1, 0, 0], "highlightRow": 0, "note": "Şematik çizim: kuzeye ulaşmak 3–4 kuşak sürer."}, [], ["BAYRAK YARIŞI 🏃"])
S(1, {"type": "meter", "title": "Monarkların derdi", "label": "Tehlike", "emoji": "⚠️", "phases": [{"label": "Süt otu yok ediliyor", "level": 0.6, "emoji": "🌿"}, {"label": "Kışlak ormanları kesiliyor", "level": 0.9, "emoji": "🪓"}], "note": NOTE}, ["🌲", "🦋"], ["BAŞLARI DERTTE"])
S(2, {"type": "bullets", "title": "Sen de dene: kelebek günlüğü", "items": ["Bahçede ya da parkta gözle", "Renkleri ve çiçekleri not et", "Dokunma, yalnızca izle ⚠️"]}, ["📓", "🌼"], ["DENEY ZAMANI 🔬", "DOKUNMA ⚠️"])
S(2, {"type": "hook", "question": "Kelebeğe dönüşülen evrenin adı ne?", "emoji": "🤔"}, ["🐛", "🦋"], ["HIZLI SORU!", "KRİZALİT ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 19, "videoTitle": "Tırtıl nasıl kelebek olur?", "paperTitleTr": "Tırtıl nasıl kelebek olur?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "walk", "emoji": "🐛", "every": 30, "size": 84}, {"kind": "fly", "emoji": "🦋", "every": 11}, {"kind": "fly", "emoji": "🦋", "every": 17, "size": 80}]},
  "takeaways": ["Tam başkalaşım: yumurta, tırtıl, krizalit, kelebek", "Süt otu zehri monarkı avcılardan korur", "Monarklar kuşaklar boyunca binlerce mil göç eder"],
  "description": "Bir tırtıl nasıl kanat çıkarır? Bu bölümde monark kelebeğini izleyerek tam başkalaşımın dört evresini; süt otuna bırakılan yumurtaları, büyüyüp deri değiştiren tırtılı, krizaliti ve eklozyonu keşfediyoruz. Monarklar kendilerini nasıl korur, binlerce millik göçlerini nasıl başarır? Sonunda kelebek günlüğü etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Tam başkalaşım", "meaning": "Yumurta, larva, pupa ve ergin evrelerinden oluşan büyük değişim."},
    {"term": "Larva", "meaning": "Böceğin yumurtadan çıktıktan sonraki evresi; kelebekte tırtıl."},
    {"term": "Pupa (krizalit)", "meaning": "Tırtılın sert bir kılıf içinde kelebeğe dönüştüğü evre."},
    {"term": "İnstar", "meaning": "Tırtılın iki deri değiştirmesi arasındaki evre."},
    {"term": "Eklozyon", "meaning": "Kelebeğin krizalitten çıkması."},
    {"term": "Nektar", "meaning": "Çiçeklerin ürettiği şekerli sıvı."},
    {"term": "Göç", "meaning": "Hayvanların mevsime göre uzak bir yere gidip dönmesi."},
    {"term": "Süt otu", "meaning": "Monarkların yumurta bıraktığı zehirli bitki."}],
  "song": e.song("Kanatlı Yolculuk", [("🥚", "Yumurta"), ("🐛", "Tırtıl"), ("🫘", "Krizalit"), ("🦋", "Monark"), ("🌿", "Süt otu")],
    ["Süt otu yaprağında minik yumurta", "Tırtıl çıkar, kabuğunu yer", "Yer de yer, büyür de büyür", "Deri değiştirir, instar geçer"],
    ["Yumurta, tırtıl, krizalit, kelebek!", "Tam başkalaşım, büyük değişim", "Kılıfın içinde gizli bir iş", "Eklozyon olur, kanatlar açılır"],
    ["Süt otu zehri kalkanı olur", "Turuncu desen: beni yeme der", "Göçmen kuşak Meksika'ya uçar", "Kuşaklar boyu yolculuk sürer"],
    ["Yumurta, tırtıl, krizalit, kelebek!", "Tam başkalaşım, büyük değişim", "Dokunma, izle, not al günlüğe", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🦋", "every": 6, "size": 200}, {"kind": "fly", "emoji": "🦋", "every": 8}, {"kind": "walk", "emoji": "🐛", "every": 12}, {"kind": "hop", "emoji": "🌸"}, {"kind": "hop", "emoji": "🌼"}, {"kind": "hop", "emoji": "🌷"}])}
e.write(D, facts, script)
