"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:yarasalar-karanlikta-nasil-yol-bulur"
NP = "National Park Service — Echolocation"; NG = "National Geographic — Bats"; US = "USGS — Why are bats important?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Echolocation", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/bats/echolocation.htm"},
    {"id": "k2", "title": "Bats", "publisher": "National Geographic", "url": "https://www.nationalgeographic.com/animals/mammals/facts/bats"},
    {"id": "k3", "title": "Why are bats important?", "publisher": "USGS", "url": "https://www.usgs.gov/faqs/why-are-bats-important"}],
  "facts": [
    F(1, "Yarasalar yön bulmak ve böcek avlamak için ekolokasyon kullanır.", "Bats navigate and find insect prey using echolocation.", NP),
    F(2, "Yarasalar insanların duyabileceğinden yüksek frekansta, ultrason denen ses dalgaları üretir.", "They produce sound waves at frequencies above human hearing, called ultrasound.", NP),
    F(3, "Yarasaların çıkardığı ses dalgaları çevredeki cisimlere çarpıp geri döner; sesler, yarasanın kendi özgün çağrılarını tanımak için ince ayarlı kulaklarına ulaşır.", "The sound waves emitted by bats bounce off objects in their environment. / Then, the sounds return to the bats' ears, which are finely tuned to recognize their own unique calls.", NP),
    F(4, "Yarasalar bir cisme çarpıp geri dönen tiz bir ses çıkararak ekolokasyon yapar; bu yankı onlara cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler.", "They echolocate by making a high-pitched sound that travels until it hits an object and bounces back to them. / This echo tells them an object's size and how far away it is.", NG),
    F(5, "Benekli yarasanın sesi, iyi duyan insanlar tarafından belli belirsiz duyulabilir.", "The spotted bat (Euderma maculatum) is actually faintly audible to humans with good hearing.", NP),
    F(6, "Yarasaların bilimsel adı Chiroptera, Yunancada 'el kanat' demektir; yarasaların her biri ince bir deriyle bir sonrakine bağlı dört uzun parmağı ve bir başparmağı vardır.", "The scientific name for bats is Chiroptera, which is Greek for \"hand wing.\" / That's because bats have four long fingers and a thumb, each connected to the next by a thin layer of skin.", NG),
    F(7, "Yarasalar dünyada uçabilen tek memelilerdir.", "They are the only mammals in the world that can fly, and they are remarkably good at it.", NG),
    F(8, "Dünyada 1.300'den fazla yarasa türü vardır; bu onları kemirgenlerden sonra en yaygın ikinci memeli grubu yapar.", "There are more than 1,300 species of bats in the world, making them the second most common group of mammals after rodents.", NG, ["1.300"]),
    F(9, "Yarasaların çoğu güve gibi gece çıkan böcekleri yiyen mikro yarasalardır; mega yarasalar tropiklerde yaşar ve meyve, nektar ve polen yer; vampir yarasalar böcek yerine kanla beslenen tek mikro yarasa türüdür.", "Most bats are microbats, which eat insects like moths, that come out at night. / In contrast, megabats live in the tropics and eat fruit, nectar, and pollen. / Vampire bats are the only species of microbats that feed on blood rather than insects.", NG),
    F(10, "Böcek yiyen mikro yarasalar bir gecede milyonlarca böcek yer ve bitkiler için doğal bir zararlı kontrolü sağlar.", "Insect-eating microbats consume millions of bugs a night, acting as a natural pest control for plants.", NG),
    F(11, "Mango, muz ve avokado dahil 500'den fazla bitki türü tozlaşma için yarasalara bağlıdır; meyve yiyen yarasalar tohumları yayarak yağmur ormanlarının büyümesine yardım eder.", "In fact, more than 500 plant species, including mangoes, bananas, and avocados, depend on bats for pollination. / Finally, fruit-eating bats help disperse seeds so rainforests can grow", NG, ["500"]),
    F(12, "Yarasaların gözleri küçüktür ama görüşleri çok hassastır; bu, bizim zifiri karanlık sayacağımız koşullarda görmelerine yardım eder.", "Bats have small eyes with very sensitive vision, which helps them see in conditions we might consider pitch black.", US),
    F(13, "Bazı yarasalar kışın mağaralarda kış uykusuna yatar.", "For example, in the winter, some may hibernate in caves, and in the summer, they'll return to an attic.", NG),
    F(14, "Beyaz burun sendromu ilk kez 2007'de New York'ta bulundu ve kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtığı tahmin ediliyor.", "Since first discovered in 2007 in New York, white-nose syndrome has spread to 16 states, / The disease is estimated to have killed over five million hibernating bats.", US, ["2007"]),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Zifiri karanlık bir gece. Gözlerini kapatsan bile yolunu bulabilir misin? Yarasalar her gece bunu yapar, hem de uçarken!", [1]),
    L("Peki ışık olmadan nasıl görüyorlar?"),
    L("Bugün yarasaların gizli süper gücünü keşfediyoruz: sesle görmek!"),
])
e.sec("context", [
    L("Üç sorumuz var. Yarasalar karanlıkta nasıl yol bulur? Neden uçabilen tek memelilerdir? Ve doğa için neden bu kadar önemlidirler?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Milli Parklar Servisi'ne göre yarasalar yön bulmak ve böcek avlamak için ekolokasyon kullanır.", [1]),
    L("Ekolokasyon, sesle ve yankıyla yer bulmak demektir. Yarasa, insanların duyamayacağı kadar tiz sesler çıkarır. Bunlara ultrason denir.", [2]),
    L("Ses dalgaları çevredeki cisimlere çarpıp geri döner ve yarasanın kulaklarına ulaşır.", [3]),
    L("National Geographic'e göre bu yankı, yarasaya cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler.", [4], f"{NGs}'e göre bu yankı, yarasaya cismin büyüklüğünü ve ne kadar uzakta olduğunu söyler."),
    L("Kulakları da kendi özgün çağrılarını tanıyacak kadar ince ayarlıdır. Yani kalabalık bir mağarada bile kendi sesini ayırt eder!", [3]),
    L("Benim de bir sensörüm var. Ama ben duvarı ancak çarptıktan sonra fark ediyorum!"),
])
e.sec("finding", [
    L("Bir de şu var: Benekli yarasa denen bir türün sesini, iyi duyan insanlar belli belirsiz duyabilir.", [5]),
    L("Yarasalar kör de değildir. USGS'ye göre gözleri küçüktür ama görüşleri çok hassastır.", [12], "Yarasalar kör de değildir. Yu Es Ci Es'e göre gözleri küçüktür ama görüşleri çok hassastır."),
    L("Bu hassas gözler, bizim zifiri karanlık sandığımız yerlerde bile görmelerine yardım eder.", [12]),
    L("Yarasaların bilimsel adı Chiroptera'dır. Yunanca 'el kanat' demektir.", [6], "Yarasaların bilimsel adı Kiroptera'dır. Yunanca el kanat demektir."),
    L("Çünkü kanatları aslında bir eldir: Dört uzun parmak ve bir başparmak, ince bir deriyle birbirine bağlanmıştır.", [6]),
    L("Bu sayede yarasalar dünyada uçabilen tek memelilerdir!", [7]),
])
e.sec("importance", [
    L("National Geographic'e göre dünyada 1.300'den fazla yarasa türü var. Kemirgenlerden sonra en kalabalık ikinci memeli grubu!", [8], f"{NGs}'e göre dünyada bin üç yüzden fazla yarasa türü var. Kemirgenlerden sonra en kalabalık ikinci memeli grubu!"),
    L("Çoğu, gece çıkan güve gibi böcekleri yiyen mikro yarasalardır. Mega yarasalar ise tropiklerde yaşar; meyve, nektar ve polen yer.", [9]),
    L("Vampir yarasalar mı? Kanla beslenen tek mikro yarasa türü onlardır. Merak etme, ben vampir değilim; ben sadece elektrik içerim!", [9]),
    L("Böcek yiyen yarasalar bir gecede milyonlarca böcek yer. Bitkiler için doğal bir zararlı kontrolüdürler.", [10]),
    L("Ayrıca mango, muz ve avokado dahil 500'den fazla bitki türü tozlaşma için yarasalara bağlıdır.", [11], "Ayrıca mango, muz ve avokado dahil beş yüzden fazla bitki türü tozlaşma için yarasalara bağlıdır."),
    L("Meyve yiyen yarasalar tohumları yayar ve yağmur ormanlarının büyümesine yardım eder.", [11]),
    L("Şimdi sıra sende! Boş bir koridorda ya da büyük bir odada ellerini bir kez çırp ve sesi dinle.", [3]),
    L("Duvara yaklaşıp uzaklaşarak tekrar çırp. Yankı değişiyor mu? Ama gerçek bir yarasa görürsen asla dokunma, uzaktan izle!", [3, 4]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Bazı yarasalar kışın mağaralarda kış uykusuna yatar. Ne yazık ki 2007'de bulunan beyaz burun sendromu, kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtı.", [13, 14], "Bunu biliyor muydun? Bazı yarasalar kışın mağaralarda kış uykusuna yatar. Ne yazık ki iki bin yedide bulunan beyaz burun sendromu, kış uykusundaki beş milyondan fazla yarasanın ölümüne yol açtı."),
    L("Hızlı soru! Yarasaların sesle ve yankıyla yol bulmasına ne denir?", [1]),
    L("Düşün bakalım... Evet: ekolokasyon!", [1]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. İyi geceler, yarasalar!"),
])
S = e.S
S(3, {"type": "hook", "question": "Yarasalar karanlıkta nasıl yol bulur?", "emoji": "🦇"}, ["🌙", "🦋"], ["ZİFİRİ KARANLIK", "IŞIKSIZ GÖRMEK?", "SESLE GÖRMEK!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Karanlıkta nasıl yol bulur?", "Neden uçabilen tek memeli?", "Doğa için neden önemli?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "stages", "title": "Ekolokasyon", "rows": [{"label": "Yarasa ultrason çıkarır", "emoji": "🦇"}, {"label": "Ses cisme çarpar", "emoji": "🦋"}, {"label": "Yankı kulağa döner", "emoji": "👂"}, {"label": "Büyüklük ve uzaklık!", "emoji": "📏"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": "Şematik çizim."}, [], ["EKOLOKASYON", "ULTRASON", "YANKI"])
S(3, {"type": "spotlight", "title": "Yankının söyledikleri", "emoji": "👂", "chips": [{"label": "Cismin büyüklüğü", "emoji": "📐"}, {"label": "Ne kadar uzakta", "emoji": "📏"}, {"label": "Kendi sesini tanır", "emoji": "🎵"}]}, ["🦇", "🤖"], ["BÜYÜKLÜK • UZAKLIK", "KENDİ SESİ", "ÇARPAN MUMA 😅"], fx="sparkle")
S(3, {"type": "comparison", "title": "Yarasalar kör mü?", "left": {"title": "Yanlış 🙈", "items": ["Yarasalar kördür"]}, "right": {"title": "Doğru 👀", "items": ["Gözleri küçük ama hassas", "Zifiri karanlıkta da görür"]}}, ["👀", "🔊"], ["BENEKLİ YARASA", "KÖR DEĞİL!", "HASSAS GÖZLER"])
S(3, {"type": "diagram", "title": "El kanat", "layout": "flow", "nodes": [{"label": "Chiroptera: el kanat", "emoji": "🖐️"}, {"label": "Parmaklar arasında ince deri", "emoji": "🦇"}, {"label": "Uçabilen tek memeli", "emoji": "✈️"}]}, ["🖐️", "🦇"], ["CHIROPTERA", "DÖRT PARMAK + BAŞPARMAK", "TEK UÇAN MEMELİ"])
S(3, {"type": "spotlight", "title": "Yarasa sofrası", "emoji": "🍽️", "chips": [{"label": "Mikro yarasa: böcek", "emoji": "🦋"}, {"label": "Mega yarasa: meyve, nektar", "emoji": "🥭"}, {"label": "Vampir yarasa: kan", "emoji": "🩸"}]}, ["🔌", "🥭"], ["1.300+ TÜR", "MİKRO • MEGA", "ELEKTRİK İÇEN MUMA 🔌"])
S(3, {"type": "meter", "title": "Doğanın yardımcısı", "label": "Fayda", "emoji": "🌱", "phases": [{"label": "Gecede milyonlarca böcek", "level": 0.7, "emoji": "🦟"}, {"label": "500+ bitki tozlaşır", "level": 0.85, "emoji": "🍌"}, {"label": "Tohum yayar, orman büyür", "level": 0.95, "emoji": "🌳"}], "note": NOTE}, ["🍌", "🌳"], ["ZARARLI KONTROLÜ", "TOZLAŞMA", "YAĞMUR ORMANI"])
S(2, {"type": "bullets", "title": "Sen de dene: yankı avı", "items": ["Boş bir odada el çırp", "Yankıyı dinle", "Duvara yaklaş, tekrar çırp", "Gerçek yarasaya asla dokunma!"], "tone": "caution"}, ["👏", "🦇"], ["DENEY ZAMANI 🔬", "UZAKTAN İZLE ⚠️"])
S(1, {"type": "big-number", "value": "Beş milyondan fazla", "label": "Beyaz burun sendromundan ölen yarasa (tahmini)", "sub": "USGS", "icon": "🦇"}, ["🕳️", "❄️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Sesle ve yankıyla yol bulmaya ne denir?", "emoji": "🤔"}, ["🦇", "👂"], ["HIZLI SORU!", "EKOLOKASYON ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 40, "videoTitle": "Yarasalar karanlıkta nasıl yol bulur?", "paperTitleTr": "Yarasalar karanlıkta nasıl yol bulur?",
  "theme": {"backdrop": "night", "actors": [{"kind": "fly", "emoji": "🦇", "every": 30}]},
  "takeaways": ["Yarasalar ultrason çıkarır ve yankıyla cisimlerin büyüklüğünü ve uzaklığını anlar", "Kanatları parmaklar arasındaki deriden oluşur; uçabilen tek memelilerdir", "Böcek yer, bitkileri tozlaştırır ve tohum yayarlar"],
  "description": "Yarasalar zifiri karanlıkta nasıl yol bulur? Bu bölümde ekolokasyonu ve ultrasonu, yarasaların kör olmadığını, el kanat demek olan Chiroptera'yı, mikro ve mega yarasaları, böcek kontrolünü, tozlaşmayı ve tohum yaymayı keşfediyoruz. Sonunda yankı deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Ekolokasyon", "meaning": "Ses çıkarıp yankısını dinleyerek çevredeki cisimleri bulma."},
    {"term": "Ultrason", "meaning": "İnsanların duyamayacağı kadar tiz ses."},
    {"term": "Yankı", "meaning": "Bir cisme çarpıp geri dönen ses."},
    {"term": "Memeli", "meaning": "Yavrularını sütle besleyen hayvan."},
    {"term": "Tozlaşma", "meaning": "Polenin çiçekten çiçeğe taşınarak meyve oluşmasını sağlaması."},
    {"term": "Kış uykusu", "meaning": "Bazı hayvanların kışı çok az enerji harcayarak uyuyarak geçirmesi."}],
  "song": e.song("Sesle Gören", [("🦇", "Yarasa"), ("👂", "Kulak"), ("🌙", "Gece"), ("🦋", "Güve"), ("🍌", "Muz")],
    ["Gece çöktü, karanlık her yer", "Yarasa uçar, çağrısı tiz", "Ultrason gider, yankı döner", "Büyüklüğü, uzaklığı söyler"],
    ["Sesle gör, yankıyla bul!", "Ekolokasyon, işte sırrı bu", "Kör değil, gözleri hassas", "Gecenin pilotu, uçan memeli"],
    ["Parmaklar arasında ince deri", "El kanat diye seslenir bilim", "Böcek yer, polen taşır", "Muzlar, mangolar teşekkür eder"],
    ["Sesle gör, yankıyla bul!", "Ekolokasyon, işte sırrı bu", "Ellerini çırp, yankıyı dinle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🦇"}, {"kind": "fly", "emoji": "🦋"}, {"kind": "hop", "emoji": "🍌"}, {"kind": "hop", "emoji": "🌙"}])}
e.write(D, facts, script)
