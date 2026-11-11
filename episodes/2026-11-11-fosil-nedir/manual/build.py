"""Manuel sağlayıcı yanıtları (Claude API anahtarı yokken): olgular, senaryo, sahne planı.
Çalıştırma: python3 <bu dosya>"""
import json, os
D = os.path.dirname(__file__)
PID = "topic:fosil-nedir"
NPS = "U.S. National Park Service — What is a Fossil?"
NPS2 = "U.S. National Park Service — How Fossils Form"
NPS4 = "U.S. National Park Service — Visit Park Fossils"
BGS = "British Geological Survey — Fossils"
NG = "National Geographic Education — Fossil"
NHM = "Natural History Museum — How are dinosaur fossils formed?"
NHM2 = "Natural History Museum — What is a fossil?"
NHM3 = "Natural History Museum — What is a coprolite?"
NHM4 = "Natural History Museum — Fossil hunting: How to find fossils on the beach"

def F(i, st, q, loc, nums=()):
    return {"id": f"f{i}", "kind": "number" if nums else "claim", "statement": st, "numbers": list(nums), "quote": q, "location": loc}

facts = {
    "paperId": PID, "basis": "full_text", "institutions": [],
    "sources": [
        {"id": "k1", "title": "What is a Fossil?", "publisher": "Ulusal Park Servisi", "url": "https://www.nps.gov/subjects/fossils/what-is-a-fossil.htm"},
        {"id": "k2", "title": "How Fossils Form", "publisher": "Ulusal Park Servisi", "url": "https://www.nps.gov/subjects/fossils/how-fossils-form.htm"},
        {"id": "k3", "title": "Visit Park Fossils", "publisher": "Ulusal Park Servisi", "url": "https://www.nps.gov/subjects/fossils/fossil-parks.htm"},
        {"id": "k4", "title": "Fossils", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": "https://www.bgs.ac.uk/discovering-geology/fossils-and-geological-time/fossils/"},
        {"id": "k5", "title": "Fossil", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/fossil/"},
        {"id": "k6", "title": "How are dinosaur fossils formed?", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/how-are-fossils-formed.html"},
        {"id": "k7", "title": "What is a fossil?", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/what-is-a-fossil.html"},
        {"id": "k8", "title": "What is a coprolite?", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/what-is-a-coprolite.html"},
        {"id": "k9", "title": "Fossil hunting: How to find fossils on the beach", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/how-to-find-fossils-on-the-beach.html"},
    ],
    "facts": [
        F(1, "Fosil, çok eski canlıların korunmuş kalıntısı ya da kalıntı izidir.", "Fossils are the preserved remains, or traces of remains, of ancient organisms.", NG),
        F(2, "Fosil kelimesi Latince 'fossilis'ten gelir; 'kazılıp çıkarılmış' demektir.", "The word fossil is derived from the Latin fossilis meaning ‘unearthed’.", BGS),
        F(3, "Korunmuş kalıntılar 10.000 yıldan yaşlıysa fosil sayılır; fosiller tipik olarak 10.000 yıldan eskidir.", "Preserved remains are defined as fossils if they are older than 10,000 years old. / Fossils also include any preserved trace of life that is typically more than 10 000 years old.", NG + "; " + BGS, ["10.000"]),
        F(4, "Vücut fosilleri kemik, diş, deri, kabuk, odun ve yaprakları kapsar.", "Body fossils include bones, teeth, skin, shells, wood, and leaves.", NPS),
        F(5, "İz fosilleri, canlının yaşarken yaptığı etkinlikten kalır: ayak izleri, yuva tünelleri, koprolitler gibi.", "Trace fossils result from activity of an organism while it is alive. / Trace fossils include footprints, tracks, burrows, trails, coprolites, root traces,", NPS),
        F(6, "İz fosilleri, başka türlü bilinemeyecek davranış bilgilerini ortaya çıkarır.", "trace fossils reveal information about behavior that would not otherwise be known.", NPS),
        F(7, "Koprolit, milyonlarca yıl önce yaşamış hayvanların fosilleşmiş dışkısıdır; bir iz fosilidir.", "Coprolites are the fossilised faeces of animals that lived millions of years ago. / They’re trace fossils, meaning not of the animal’s actual body.", NHM3),
        F(8, "Koprolitte kemik parçaları varsa hayvan etçildi; tohum, yaprak kalıntısı, polen ya da kabuk varsa bitki yiyordu.", "If there are bone fragments, the animal was a carnivore. / Seeds, leaf remains, pollen or bark found in a coprolite suggest that the animal it came from ate plants.", NHM3),
        F(9, "Hayvan ölür; deri ve kas gibi yumuşak kısımlar çürümeye başlar; tamamen yok olmadan çamur, kum ya da siltle örtülür; çoğu zaman yalnızca kemikler ve dişler kalır.", "The animal dies. / Soft parts of the animal's body, including skin and muscles, start to rot away. / Before the body disappears completely, it is buried by sediment - usually mud, sand or silt. / Often at this point only the bones and teeth remain.", NHM),
        F(10, "Hızlı gömülme fosilleşme için gereklidir; ölümden kısa süre sonra tortuyla örtülmek kalıntıyı çürümekten ve aşınmaktan korur.", "Rapid burial by sediments that were previously suspended in water is required for fossilisation to occur. / Burial by sediment soon after an organism dies prevents the remains from decomposition, weathering", BGS + "; " + NPS2),
        F(11, "Üstüne çok sayıda tortu katmanı birikir; bunlar zamanla tortul kayaya dönüşür.", "Many more layers of sediment build up on top. / Eventually, they turn into sedimentary rock.", NHM),
        F(12, "Su kemiklere ve dişlere sızar, geride mineral bırakarak onları taşa çevirir; permineralizasyon, organik maddedeki minik gözeneklerin dolmasıdır.", "While this is happening, water seeps into the bones and teeth, turning them to stone as it leaves behind minerals. / Permineralization is the infilling of tiny pores in organic material.", NHM + "; " + NPS),
        F(13, "Bu süreç binlerce, hatta milyonlarca yıl sürebilir.", "This process can take thousands or even millions of years.", NHM),
        F(14, "Yeraltı suyu gömülü kemiği ya da kabuğu çözerse onun biçiminde bir boşluk (kalıp) kalır; mineralli su bu boşluğu doldurursa aynı biçimde bir fosil (döküm) oluşur.", "Sometimes ground water dissolves the buried bone or shell, leaving behind a bone- or shell-shaped hole / If water rich in minerals fills this space, crystals can form and create a fossil in the shape / it may leave behind a space in the shape of the original material called a mould. / A cast is a positive impression of the original material formed by contact with the mould.", NHM + "; " + BGS),
        F(15, "Ağaçların yapışkan reçinesi fosilleşebilir (kehribar); kehribar karınca, sinek gibi narin canlıların bedenlerini koruyabilir.", "Sometimes, however, the sticky resin of a tree can become fossilized. / Amber can preserve the bodies of many delicate, soft-bodied organisms, such as ants, flies, and mosquitoes.", NG),
        F(16, "Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu tamamen çürür ve geriye bir şey kalmaz.", "A specific set of circumstances and conditions are needed for fossilisation to occur, so it is actually a very rare event. / Most things that die rot away completely, leaving nothing behind.", NHM),
        F(17, "Fosilleşme, iskelet, diş, kabuk gibi sert parçaları olan canlılarda daha sık görülür; solucan gibi yumuşak gövdeli canlılar nadiren fosilleşir.", "Fossilization more commonly occurs in organisms with hard, bony body parts, such as skeletons, teeth, or shells. / Soft-bodied organisms, such as worms, are rarely fossilized, because soft parts quickly decompose or are eaten.", NG),
        F(18, "Bulunan fosillerin neredeyse tamamı, yaklaşık %99'u, kabuklular ve köpek balıkları gibi deniz hayvanlarına aittir.", "Nearly all fossils we find - around 99% - are from marine animals such as shellfish and sharks.", NHM, ["99"]),
        F(19, "Fosiller, oluşma biçimleri nedeniyle tortul kayalarda bulunur.", "Because of how they form, fossils occur in sedimentary rocks.", NHM),
        F(20, "Rüzgâr, yağmur, buz, sıcaklık ve nehirlerin yol açtığı aşınma kayaları parçalar; fosiller yavaş yavaş yüzeye çıkar.", "Weathering and erosion from wind, rain, ice, heat and rivers break rocks apart / It can take millions of years, but gradually fossils become exposed at the surface where we can find them.", NHM),
        F(21, "Deniz hayvanlarının fosilleri Everest'in tepesinde bulunabilir; Himalayaları oluşturan kayalar bir zamanlar okyanusun dibindeydi.", "This is why fossils of marine animals can be found at the top of Mount Everest. / the rocks that became the Himalayas were at the bottom of the ocean.", NHM + "; " + NG),
        F(22, "Paleontologlar fosilleri inceleyen kişilerdir; fosiller türlerin nasıl yaşadığını ve Dünya'nın nasıl değiştiğini öğrenmeye yardım eder.", "Paleontologists are people who study fossils. / Studying fossils helps them learn about when and how different species lived millions of years ago. / Sometimes, fossils tell scientists how the Earth has changed.", NG),
        F(23, "En eski fosiller neredeyse 4 milyar yaşındadır ve okyanusta yaşamış bakterilerin izleridir.", "The oldest fossils are almost 4 billion years old and are traces of ocean-dwelling bacteria.", NG, ["4"]),
        F(24, "ABD Ulusal Park Sistemi'nin bütün birimlerinde fosil toplamak yasaktır; tek bir fosil, bütün bir türün var olduğunun tek kanıtı olabilir.", "collecting fossils for recreational, commercial, or educational use is prohibited in all units of the National Park System / A single fossil may be the only evidence of the existence of an entire species.", NPS4),
        F(25, "Bazı yerlerde bakılabilir ama hiçbir şey toplanamaz; önemli olabilecek bir fosil görülürse bir müzeye bildirilmesi önerilir.", "In some places you can look but mustn’t collect anything. / If you spot a fossil that you think may be exciting or important, report it to a Museum", NHM4),
        F(26, "Köpek balığı dişleri, en bol bulunan omurgalı fosilleridir.", "Shark teeth are the most abundant vertebrate fossils.", NHM2),
    ],
}

n = 0
def L(text, f=(), spoken=None):
    global n; n += 1
    return {"id": f"l{n}", "display": text, "spoken": spoken or text, "factIds": [f"f{i}" for i in f]}

sections = [
    ("hook", [
        L("Elinde sıradan bir taş var. Ama üstünde, çok eski zamanlarda yaşamış bir canlının izi duruyor!"),
        L("Bir canlı nasıl olur da taşa dönüşür? Ve neden her canlı fosil olmaz?"),
        L("Bugün yerin altındaki bu dev arşivi açıyoruz!"),
    ]),
    ("context", [
        L("Baştan söyleyeyim: bende kemik yok, vida var. Ben fosil olmam; olsa olsa antika olurum!"),
        L("Üç sorumuz var. Fosil tam olarak nedir? Bir canlı nasıl fosilleşir? Ve fosiller bize ne anlatır?"),
        L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
    ]),
    ("method", [
        L("National Geographic'e göre fosil, çok eski zamanlarda yaşamış canlılardan korunarak kalmış kalıntı ya da izdir.", [1], "Neşınıl Ciyografik'e göre fosil, çok eski zamanlarda yaşamış canlılardan korunarak kalmış kalıntı ya da izdir."),
        L("Kelime Latinceden gelir. Britanya Jeoloji Araştırmaları Kurumu'na göre \"fossilis\", kazılıp çıkarılmış demektir.", [2], "Kelime Latinceden gelir. Britanya Jeoloji Araştırmaları Kurumu'na göre fosilis, kazılıp çıkarılmış demektir."),
        L("Peki ne kadar eski? Bir kalıntının fosil sayılması için genellikle 10.000 yıldan yaşlı olması gerekir.", [3], "Peki ne kadar eski? Bir kalıntının fosil sayılması için genellikle on bin yıldan yaşlı olması gerekir."),
        L("Benim garanti belgem bile o kadar dayanmaz!"),
        L("ABD Ulusal Park Servisi'ne göre fosiller iki büyük gruba ayrılır. Birincisi vücut fosili: canlının kendi parçasıdır. Kemik, diş, kabuk, odun ya da yaprak gibi.", [4, 5], "A Be De Ulusal Park Servisi'ne göre fosiller iki büyük gruba ayrılır. Birincisi vücut fosili: canlının kendi parçasıdır. Kemik, diş, kabuk, odun ya da yaprak gibi."),
        L("İkincisi iz fosili: canlının bedeni değil, yaşarken bıraktığı izdir. Ayak izi ya da yuva tüneli gibi.", [5]),
        L("İz fosilleri çok değerlidir; çünkü canlının davranışı hakkında başka türlü bilemeyeceğimiz şeyleri gösterir.", [6]),
        L("En ilginç iz fosilinin adı koprolit. Londra'daki Doğa Tarihi Müzesi'ne göre koprolit, fosilleşmiş hayvan dışkısıdır. Evet, yanlış duymadın: taşlaşmış kaka!", [7]),
        L("Gülme, çok işe yarar! İçinde kemik parçaları varsa o hayvan etçildi. Tohum ya da yaprak kalıntısı varsa bitki yiyordu.", [8]),
        L("Demek ki bilim insanı olmak, bazen gerçekten pis iştir!"),
    ]),
    ("finding", [
        L("Peki bir canlı nasıl fosilleşir? Doğa Tarihi Müzesi'nin anlattığı adımları sırayla izleyelim.", [9]),
        L("Birinci adım: canlı ölür. Deri ve kas gibi yumuşak kısımlar çürümeye başlar.", [9]),
        L("İkinci adım: tamamen yok olmadan önce çamur, kum ya da silt gibi tortularla örtülür. Çoğu zaman geriye yalnızca kemikler ve dişler kalır.", [9]),
        L("Burada hız önemlidir: çabucak gömülmek, kalıntıyı çürümekten ve aşınmaktan korur.", [10]),
        L("Üçüncü adım: üstüne kat kat yeni tortu birikir. Bu katmanlar zamanla tortul kayaya dönüşür.", [11]),
        L("Dördüncü adım: su, kemiklerin içine sızar ve geride mineral bırakır. Mineraller kemiğin minik gözeneklerini doldurur; kemik yavaş yavaş taşa dönüşür.", [12]),
        L("Bu olayın adı permineralizasyon. Kelime uzun ama anlamı basit: gözeneklerin mineralle dolması.", [12]),
        L("Ve sabır gerekir: bu süreç binlerce, hatta milyonlarca yıl sürebilir.", [13]),
        L("Bazen su kemiği tamamen çözer ve kayada onun biçiminde bir boşluk kalır. Buna kalıp denir. Boşluğu mineraller doldurursa döküm oluşur.", [14]),
        L("Bir yol daha var: kehribar. Ağaç reçinesi fosilleşir ve içine yapışan karınca, sinek gibi böcekleri saklar.", [15]),
    ]),
    ("importance", [
        L("Peki her canlı fosil olur mu? Hayır! Fosilleşme çok nadir bir olaydır; ölen canlıların çoğu çürür ve geriye hiçbir şey kalmaz.", [16]),
        L("Kemik, diş, kabuk gibi sert parçalar daha kolay fosilleşir. Solucan gibi yumuşak gövdeli canlılar ise nadiren fosil olur.", [17]),
        L("Yani fosil olmak çok zor bir sınav gibi. Üstelik sonuçların açıklanması çok, çok uzun sürüyor!"),
        L("Bulduğumuz fosillerin neredeyse tamamı, yaklaşık %99'u, deniz hayvanlarına aittir: kabuklular ve köpek balıkları gibi.", [18], "Bulduğumuz fosillerin neredeyse tamamı, yaklaşık yüzde doksan dokuzu, deniz hayvanlarına aittir: kabuklular ve köpek balıkları gibi."),
        L("Fosiller tortul kayaların içinde bulunur. Rüzgâr, yağmur ve buz kayaları aşındırdıkça fosiller yavaş yavaş yüzeye çıkar.", [19, 20]),
        L("Şaşırtıcı bir örnek: Everest'in tepesinde deniz hayvanlarının fosilleri bulunabilir! Çünkü o kayalar bir zamanlar okyanusun dibindeydi.", [21]),
        L("Fosilleri inceleyen bilim insanlarına paleontolog denir. Fosiller onlara canlıların nasıl yaşadığını ve Dünya'nın nasıl değiştiğini anlatır.", [22]),
        L("En eski fosiller neredeyse 4 milyar yaşında: okyanusta yaşamış bakterilerin izleri.", [23], "En eski fosiller neredeyse dört milyar yaşında: okyanusta yaşamış bakterilerin izleri."),
        L("Şimdi sıra sende! Oyun hamuruna bir deniz kabuğu ya da yaprak bastır ve yavaşça kaldır."),
        L("Hamurda kalan çukur bir kalıptır. Doğada böyle bir boşluğu mineraller doldurur ve döküm oluşur.", [14]),
        L("Dışarıda fosil görürsen kural basit: bak, fotoğrafını çek, yerinde bırak. Örneğin ABD'nin milli parklarında fosil toplamak yasaktır; çünkü tek bir fosil, bir türün tek kanıtı olabilir.", [24, 25], "Dışarıda fosil görürsen kural basit: bak, fotoğrafını çek, yerinde bırak. Örneğin A Be De'nin milli parklarında fosil toplamak yasaktır; çünkü tek bir fosil, bir türün tek kanıtı olabilir."),
        L("Önemli bir şey bulduğunu düşünürsen bir büyüğünle birlikte bir müzeye haber ver.", [25]),
    ]),
    ("limitations", [
        L("Bunu biliyor muydun? Omurgalı hayvan fosilleri arasında en bol bulunanı köpek balığı dişleridir.", [26]),
        L("Hızlı soru! Ayak izi, vücut fosili midir yoksa iz fosili mi?", [5]),
        L("Düşün bakalım... Evet: iz fosili!", [5]),
        L("Ben hiç ayak izi bırakamam. Çünkü yürümüyorum, uçuyorum!"),
        L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
    ]),
    ("summary", [
        L("İşte bugün öğrendiklerimiz!"),
        L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
        L("Abone olmayı ve zili açmayı unutma. Ben de uçayım; burada fazla durursam fosil olacağım!"),
    ]),
]
STYLE = ["cheerful educational pop song", "upbeat marching band rhythm", "adventurous explorer cartoon theme energy", "bright glockenspiel, snare drum, tuba, hand claps", "catchy sing-along melody", "120 BPM", "clear enthusiastic lead vocal in Turkish", "group vocals shouting along in the chorus", "major key"]
song = {
    "title": "Taşa Yazılan Hikâye",
    "style": STYLE,
    "negativeStyle": ["sad", "slow", "dark", "heavy distortion", "mumbled vocals", "long instrumental solo", "lullaby"],
    "cast": [{"emoji": "🦴", "name": "Kemik"}, {"emoji": "🐚", "name": "Kabuk"}, {"emoji": "🐾", "name": "Ayak izi"}, {"emoji": "🐜", "name": "Kehribar"}, {"emoji": "🦷", "name": "Diş"}],
    "sections": [
        {"tag": "Intro", "label": "Giriş", "direction": "snare drum roll, hand claps", "lines": ["Hey! Hey! Hey!"], "durationMs": 5000},
        {"tag": "Verse 1", "label": "Kıta", "lines": ["Çamurun altında saklı bir kemik", "Kat kat tortu birikir, kaya olur gider", "Su sızar içine, mineral bırakır", "Gözenekler dolar, kemik taşlaşır"], "durationMs": 15000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Fosil! Fosil! Taştaki iz!", "Geçmişi okuruz kayalardan biz", "Kemik, diş, kabuk; ayak izi, yuva", "Dünya'nın geçmişi saklı burada"], "durationMs": 13000},
        {"tag": "Verse 2", "label": "Kıta", "lines": ["Kehribarın içinde bir karınca durur", "Kalıp ve döküm, biçimi korur", "Koprolit söyler kim ne yemiş", "Paleontolog ipucunu çözmüş"], "durationMs": 15000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Fosil! Fosil! Taştaki iz!", "Geçmişi okuruz kayalardan biz", "Görürsen bak, yerinde bırak", "Muma'yla öğrendik, hey!"], "durationMs": 13000},
    ],
}
script = {
    "paperId": PID, "episodeNumber": 3, "videoTitle": "Fosil nedir?", "paperTitleTr": "Fosil nedir?",
    "sections": [{"id": s, "lines": ls} for s, ls in sections],
    "takeaways": ["Fosil: çok eski canlıların korunmuş kalıntısı ya da izi", "Gömülme ve mineraller kemiği yavaş yavaş taşa çevirir", "Fosilleşme nadirdir; fosiller Dünya'nın geçmişini anlatır"],
    "nextTeaser": "Yeni bir soru, yeni bir keşif seni bekliyor!",
    "description": "Bir canlı nasıl taşa dönüşür? Bu bölümde fosilin ne olduğunu, vücut fosili ile iz fosili arasındaki farkı, koproliti, fosilleşmenin adımlarını (gömülme, tortul kaya, permineralizasyon), kalıp ve dökümü, kehribarı keşfediyoruz. Fosilleşme neden nadirdir, fosiller neden en çok deniz hayvanlarına aittir, paleontologlar taşlardan ne öğrenir? Sonunda oyun hamuruyla kalıp deneyi ve konuyu özetleyen bir şarkı var.",
    "glossary": [
        {"term": "Fosil", "meaning": "Çok eski zamanlarda yaşamış bir canlıdan korunarak kalmış kalıntı ya da iz."},
        {"term": "İz fosili", "meaning": "Canlının bedeni değil, yaşarken bıraktığı iz: ayak izi, yuva tüneli, koprolit."},
        {"term": "Koprolit", "meaning": "Fosilleşmiş hayvan dışkısı."},
        {"term": "Tortu", "meaning": "Suyun, rüzgârın taşıyıp biriktirdiği çamur, kum, silt gibi ince malzeme."},
        {"term": "Silt", "meaning": "Kumdan ince, kilden iri taneli tortu."},
        {"term": "Tortul kaya", "meaning": "Üst üste biriken tortu katmanlarının zamanla dönüştüğü kaya."},
        {"term": "Mineral", "meaning": "Doğada kendiliğinden oluşan, kayaları meydana getiren katı madde."},
        {"term": "Permineralizasyon", "meaning": "Kemik gibi kalıntıların minik gözeneklerinin mineralle dolması."},
        {"term": "Kehribar", "meaning": "Fosilleşmiş ağaç reçinesi."},
        {"term": "Paleontolog", "meaning": "Fosilleri inceleyen bilim insanı."},
    ],
    "song": song,
}

allids = [l["id"] for s, ls in sections for l in ls]
by = {l["id"]: l for s, ls in sections for l in ls}
sec_of = {l["id"]: s for s, ls in sections for l in ls}
pos = 0
scenes = []
M = {"state": "talk", "x": 0.87, "y": 0.54, "scale": 1.15}  # yalnızca kapanışta geçerli
def S(k, visual, stickers=(), keywords=(), extra=()):
    """k satırlık sahne. stickers: kenarda süzülen simgeler; keywords: satır başına büyük anahtar kelime."""
    global pos
    li = allids[pos:pos + k]; pos += k
    sc = {"id": f"s{len(scenes)+1}", "section": sec_of[li[0]], "lineIds": li, "visual": visual, "mascot": M,
          "factIds": sorted({f for i in li for f in by[i]["factIds"]} | {f"f{e}" for e in extra}, key=lambda x: int(x[1:]))}
    if stickers: sc["stickers"] = list(stickers)
    if keywords: sc["keywords"] = (list(keywords) + [""] * k)[:k]
    scenes.append(sc)

NOTE = "Şematik çizim; ölçekli değildir."
S(3, {"type": "hook", "question": "Bir canlı nasıl taşa dönüşür?", "emoji": "🦴"}, ["🪨", "🐚", "⛏️", "🦕"], ["", "TAŞA DÖNÜŞMEK?", "ARŞİVİ AÇIYORUZ!"])
S(1, {"type": "spotlight", "title": "Robot fosil olur mu?", "emoji": "🤖", "chips": [{"label": "Kemik yok", "emoji": "🦴"}, {"label": "Vida var", "emoji": "🔩"}, {"label": "Olsa olsa antika!", "emoji": "🏺"}]}, ["⚙️", "🔧"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Fosil tam olarak nedir?", "Bir canlı nasıl fosilleşir?", "Fosiller bize ne anlatır?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Fosil nedir?", "emoji": "🦴", "chips": [{"label": "Çok eski canlılardan", "emoji": "🦕"}, {"label": "Korunmuş kalıntı ya da iz", "emoji": "🪨"}, {"label": "Latince: fossilis", "emoji": "📜"}, {"label": "Kazılıp çıkarılmış", "emoji": "⛏️"}]}, ["🐚", "🌿"], ["KALINTI YA DA İZ", "FOSSILIS ⛏️"])
S(2, {"type": "big-number", "value": "10.000", "unit": "yıl", "label": "Fosil sayılmanın yaş sınırı", "sub": "Genellikle bundan yaşlı olmalı", "icon": "⏳"}, ["🦣", "📅"], ["NE KADAR ESKİ?", "GARANTİ BİTTİ 😅"])
S(3, {"type": "comparison", "title": "İki büyük grup",
      "left": {"title": "Vücut fosili 🦴", "items": ["Canlının kendi parçası", "Kemik, diş, kabuk", "Odun, yaprak"]},
      "right": {"title": "İz fosili 🐾", "items": ["Yaşarken bıraktığı iz", "Ayak izi, yuva tüneli", "Davranışı gösterir"]}}, ["🦷", "🐚", "🍃"], ["VÜCUT FOSİLİ", "İZ FOSİLİ", "DAVRANIŞ İPUCU 🔎"])
S(3, {"type": "spotlight", "title": "Koprolit", "emoji": "💩", "chips": [{"label": "Fosilleşmiş dışkı", "emoji": "🪨"}, {"label": "Bir iz fosili", "emoji": "🐾"}, {"label": "Kemik parçası → etçil", "emoji": "🍖"}, {"label": "Tohum, yaprak → bitki yiyen", "emoji": "🌿"}]}, ["🔬", "🧤"], ["KOPROLİT", "NE YEMİŞ? 🍖🌿", "PİS İŞ 🧤"])
S(2, {"type": "diagram", "title": "Birinci adım: çürüme", "layout": "flow", "nodes": [{"label": "Canlı ölür", "emoji": "🦕"}, {"label": "Deri ve kas çürür", "emoji": "🍂"}, {"label": "Sert parçalar kalır", "emoji": "🦴"}]}, ["🌊", "⏳"], ["NASIL FOSİLLEŞİR?", "BİRİNCİ ADIM"], extra=[9])
S(2, {"type": "meter", "title": "İkinci adım: gömülme", "label": "Tortu örtüsü", "emoji": "🦴", "phases": [{"label": "Çamur, kum, silt örter", "level": 0.5, "emoji": "🟤"}, {"label": "Çabuk gömülmek korur", "level": 0.92, "emoji": "🛡️"}], "note": NOTE}, ["🌊", "🏖️"], ["İKİNCİ ADIM: TORTU", "HIZ ÖNEMLİ ⚡"])
S(1, {"type": "spotlight", "title": "Üçüncü adım: katmanlar", "emoji": "🪨", "chips": [{"label": "Kat kat yeni tortu", "emoji": "📚"}, {"label": "Zamanla tortul kaya", "emoji": "⛰️"}, {"label": "Kemik içinde saklı", "emoji": "🦴"}]}, ["🟤", "🟫"], ["TORTUL KAYA"])
S(2, {"type": "diagram", "title": "Dördüncü adım: permineralizasyon", "layout": "flow", "nodes": [{"label": "Su kemiğe sızar", "emoji": "💧"}, {"label": "Mineral bırakır", "emoji": "💎"}, {"label": "Gözenekler dolar", "emoji": "🧽"}, {"label": "Kemik taşlaşır", "emoji": "🪨"}]}, ["💧", "💎"], ["SU + MİNERAL", "PERMİNERALİZASYON"])
S(1, {"type": "big-number", "value": "Sabır!", "label": "Binlerce, hatta milyonlarca yıl sürebilir", "sub": "Doğa Tarihi Müzesi", "icon": "⏳"}, ["🐢", "📆"], ["MİLYONLARCA YIL"])
S(1, {"type": "comparison", "title": "Kalıp ve döküm",
      "left": {"title": "Kalıp 🕳️", "items": ["Su kemiği çözer", "Biçiminde boşluk kalır"]},
      "right": {"title": "Döküm 🪨", "items": ["Boşluğu mineraller doldurur", "Aynı biçimde taş oluşur"]}}, ["🐚", "💧"], ["KALIP → DÖKÜM"])
S(1, {"type": "spotlight", "title": "Kehribar", "emoji": "🐜", "chips": [{"label": "Ağaç reçinesi", "emoji": "🌲"}, {"label": "Fosilleşir", "emoji": "🟠"}, {"label": "Karınca, sinek saklanır", "emoji": "🪰"}]}, ["🌲", "🟠"], ["KEHRİBAR"])
S(3, {"type": "meter", "title": "Fosil olma şansı", "label": "Şans", "emoji": "🎯", "phases": [{"label": "Çoğu canlı çürür: çok nadir", "level": 0.06, "emoji": "🍂"}, {"label": "Sert parçalar: daha kolay", "level": 0.4, "emoji": "🦴"}, {"label": "Yumuşak gövde: nadiren", "level": 0.1, "emoji": "🪱"}], "note": NOTE}, ["🦷", "🐚"], ["ÇOK NADİR!", "SERT PARÇALAR 🦴", "ZOR SINAV 📝"])
S(1, {"type": "big-number", "value": "%99", "label": "Deniz hayvanlarına ait", "sub": "Bulunan fosillerin yaklaşık bu kadarı", "icon": "🌊"}, ["🐚", "🦈", "🐟"], ["DENİZ HAYVANLARI 🌊"])
S(2, {"type": "diagram", "title": "Fosiller nasıl ortaya çıkar?", "layout": "flow", "nodes": [{"label": "Tortul kaya", "emoji": "⛰️"}, {"label": "Rüzgâr, yağmur, buz aşındırır", "emoji": "🌧️"}, {"label": "Fosil yüzeye çıkar", "emoji": "🦴"}, {"label": "Everest'te deniz fosilleri!", "emoji": "🏔️"}]}, ["🌬️", "🐚"], ["AŞINMA", "EVEREST'TE DENİZ! 🏔️"])
S(2, {"type": "spotlight", "title": "Paleontolog", "emoji": "🧑‍🔬", "chips": [{"label": "Fosilleri inceler", "emoji": "🔎"}, {"label": "Canlılar nasıl yaşadı?", "emoji": "🦕"}, {"label": "Dünya nasıl değişti?", "emoji": "🌍"}, {"label": "En eski fosil: neredeyse 4 milyar yaşında", "emoji": "🦠"}]}, ["⛏️", "🖌️"], ["PALEONTOLOG", "BAKTERİ İZLERİ 🦠"])
S(2, {"type": "bullets", "title": "Sen de dene: kalıp çıkar 🔬", "items": ["Oyun hamurunu düzleştir", "Deniz kabuğu ya da yaprak bastır", "Yavaşça kaldır: çukur = kalıp", "Doğada boşluğu mineraller doldurur: döküm"]}, ["🐚", "🍃", "✋"], ["DENEY ZAMANI 🔬", "KALIP!"])
S(2, {"type": "spotlight", "title": "Fosil görürsen", "emoji": "📸", "chips": [{"label": "Bak", "emoji": "👀"}, {"label": "Fotoğrafını çek", "emoji": "📸"}, {"label": "Yerinde bırak", "emoji": "🚫"}, {"label": "Müzeye haber ver", "emoji": "🏛️"}]}, ["🏞️", "🧭"], ["YERİNDE BIRAK!", "MÜZEYE HABER 🏛️"])
S(1, {"type": "big-number", "value": "Köpek balığı dişi", "label": "Omurgalı fosilleri arasında en bol bulunanı", "sub": "Doğa Tarihi Müzesi", "icon": "🦈"}, ["🦷", "🌊"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Ayak izi: vücut fosili mi, iz fosili mi?", "emoji": "🐾"}, ["🦕", "🦴"], ["HIZLI SORU!", "İZ FOSİLİ ✅", ""])
S(1, {"type": "song"})
S(3, {"type": "outro"})
assert pos == len(allids), (pos, len(allids))
for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": scenes})):
    json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("satır:", len(allids), "sahne:", len(scenes), "kelime:", sum(len(l["spoken"].split()) for s, ls in sections for l in ls), "karakter:", sum(len(l["spoken"]) for s, ls in sections for l in ls))
