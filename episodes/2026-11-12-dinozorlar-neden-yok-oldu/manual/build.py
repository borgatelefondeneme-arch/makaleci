"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:dinozorlar-neden-yok-oldu"
N1 = "Natural History Museum — How an asteroid ended the age of the dinosaurs"; N3 = "Natural History Museum — Why are birds the only surviving dinosaurs?"
NG = "National Geographic Education — Extinction"; NASA = "NASA Science — Asteroids"; US = "USGS — When did dinosaurs become extinct?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "How an asteroid ended the age of the dinosaurs", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/how-an-asteroid-caused-extinction-of-dinosaurs.html"},
    {"id": "k2", "title": "Why are birds the only surviving dinosaurs?", "publisher": "Doğa Tarihi Müzesi", "url": "https://www.nhm.ac.uk/discover/why-are-birds-the-only-surviving-dinosaurs.html"},
    {"id": "k3", "title": "Extinction", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/extinction/"},
    {"id": "k4", "title": "Asteroids", "publisher": "NASA", "url": "https://science.nasa.gov/solar-system/asteroids/"},
    {"id": "k5", "title": "When did dinosaurs become extinct?", "publisher": "USGS", "url": "https://www.usgs.gov/faqs/when-did-dinosaurs-become-extinct"}],
  "facts": [
    F(1, "66 milyon yıl önce dinozorlar çok kötü bir gün geçirdi; yok oluşun tarihi 66,0 milyon yıl öncedir.", "Sixty-six million years ago, dinosaurs had the ultimate bad day. / the date of the dinosaur extinction is 66.0 million years ago.", N1, ["66"]),
    F(2, "Dünya'daki hayvanların yaklaşık %75'i, dinozorlar dahil, aynı zamanda aniden yok oldu.", "Around 75% of Earth's animals, including dinosaurs, suddenly died out at the same point in time.", N1, ["75"]),
    F(3, "Asteroitler Güneş'in çevresinde dolanan büyük, kayalık cisimlerdir; Güneş sisteminin yaklaşık 4,6 milyar yıl önceki oluşumundan arta kalan parçalardır. Bu asteroidin 10–15 kilometre genişliğinde olduğu düşünülüyor.", "Asteroids are large, rocky objects that orbit the Sun. / rocky, airless remnants left over from the early formation of our solar system about 4.6 billion years ago. / The asteroid is thought to have been between 10 and 15 kilometres wide,", N1 + "; " + NASA, ["4.6", "10", "15"]),
    F(4, "Çarpma yeri Chicxulub krateri olarak bilinir ve merkezi Meksika'daki Yucatán Yarımadası'ndadır; krater 150 kilometre çapındadır.", "The impact site, known as the Chicxulub crater, is centred on the Yucatán Peninsula in Mexico. / the velocity of its collision caused the creation of a much larger crater, 150 kilometres in diameter.", N1, ["150"]),
    F(5, "Asteroit yüksek hızla çarptı ve fiilen buharlaştı; dev bir patlama dalgası ve sıcak dalgası yayıldı, atmosfere çok büyük miktarda madde savruldu.", "The asteroid hit at high velocity and effectively vaporised. / A huge blast wave and heatwave went out and it threw vast amounts of material up into the atmosphere.", N1),
    F(6, "Dev dalgalar Amerika kıtalarının bazı bölgelerini kapladı; büyük yangınların kanıtları da var.", "caused massive tidal waves to wash over parts of the American continents. / There's also evidence of substantial fires from that point in history.", N1),
    F(7, "Kurum bütün dünyaya yayıldı; Güneş'i tamamen kapatmadı ama yeryüzüne ulaşan ışığı azalttı ve bitki büyümesini etkiledi.", "It sent soot travelling all around the world. / It didn't completely block out the Sun, but it reduced the amount of light that reached the Earth's surface. / So it had an impact on plant growth.", N1),
    F(8, "Domino taşları gibi, bu durum besin zincirinin üst basamaklarını etkiledi ve ekosistemin çökmesine yol açtı.", "Like dominos, this had knock-on effects up the food chain, causing the ecosystem to collapse.", N1),
    F(9, "1980'de fizikçi Luis Walter Alvarez ve jeolog oğlu Walter, iridyumca zengin tarihsel bir kil tabakasının büyük bir asteroidin Dünya'ya çarpmasından kaynaklandığı kuramını yayımladı. İridyum Dünya'da bulunan en nadir metallerden biridir.", "In 1980, Nobel Prize-winning physicist Luis Walter Alvarez and his geologist son Walter published a theory / that a historic layer of iridium-rich clay was caused by a large asteroid colliding with Earth. / Iridium is one of the rarest metals found on Earth.", N1, ["1980"]),
    F(10, "Alvarez hipotezi başta tartışmalıydı ama bugün en yaygın kabul gören kuramdır; krater bulunmuştur ve yaşı kuş olmayan dinozorların yok oluşuyla tam olarak aynıdır.", "The Alvarez hypothesis was initially controversial, but it's now the most widely accepted theory / An asteroid impact is supported by really good evidence because we've identified the crater, / It's exactly the same age as the extinction of the non-bird dinosaurs, which can be tracked in the rock record all around the world.", N1),
    F(11, "Suç yalnızca asteroitte değildir: çarpışmadan önce Dünya bir iklim değişikliği dönemindeydi; bugünkü Hindistan'ın orta kesiminde iki milyon yıl boyunca çok büyük volkanik etkinlik sürdü; asteroit son, öldürücü darbeydi. Öldürme mekanizması hâlâ tartışılıyor.", "The blame can't solely rest on the asteroid. / Prior to its crash landing, Earth was experiencing a period of climate change. / In what's now central India, there was substantial volcanic activity / For two million years there was a huge amount of volcanic activity going on, / The asteroid was the final, killer blow. / There is a lot of discussion over the actual kill mechanism and how long that period lasted.", N1),
    F(12, "Ammonitler, bazı mikroskobik planktonlar, pterozorlar ve büyük deniz sürüngenleri yok oldu; ağırlığı 25 kilogramın üstündeki bütün kara hayvanları da yok oldu.", "Among them, ammonites, some microscopic plankton, pterosaurs and large marine reptiles all died out. / But all land animals weighing over 25 kilogrammes died out.", N1, ["25"]),
    F(13, "Bitkiler hayvanlardan daha az etkilendi; çünkü tohumları ve polenleri zor dönemlere daha uzun dayanabilir.", "plants were less affected than animals because their seeds and pollen can survive harsh periods for longer.", N1),
    F(14, "Hayatta kalanlar başlangıçta küçüktü; kuş olmayan bütün dinozorlar yok oldu ama dinozorlar kuşlar olarak hayatta kaldı.", "Initially the survivors were small, with birds the first to experience evolution to larger sizes. / All of the non-bird dinosaurs died out, but dinosaurs survived as birds.", N1),
    F(15, "Kuşlar teropod denen etçil bir dinozor grubundan evrildi; hayatta kalmalarında büyük olasılıkla küçük bedenleri, çok farklı besinler yiyebilmeleri ve uçabilmeleri etkili oldu; bugün en az 11.000 kuş türü vardır.", "Birds evolved from a group of meat-eating dinosaurs called theropods. / The answer probably lies in a combination of things: their small size, the fact they can eat a lot of different foods and their ability to fly. / Today there are at least 11,000 bird species.", N3, ["11.000"]),
    F(16, "Dinozorların yok oluşu memelilerin gelişip büyümesine olanak verdi.", "In the case of the Cretaceous extinction, the demise of the dinosaurs allowed mammals to thrive and grow larger.", NG),
    F(17, "NASA'nın bir birimi, Dünya için çarpma tehlikesi oluşturabilecek asteroit ve kuyrukluyıldızları bulma, izleme ve daha iyi anlama görevini yürütür.", "manages NASA's mission to find, track, and better understand asteroids and comets that could pose an impact hazard to Earth.", NASA),
    F(18, "Yaklaşık 66 milyon yıl önce, Kretase döneminin sonunda beşinci kitlesel yok oluş yaşandı.", "Finally, about 66 million years ago, at the end of the Cretaceous period came the fifth mass extinction.", NG, ["66"]),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyografik"
e.sec("hook", [
    L("Bir zamanlar bu gezegende dev dinozorlar dolaşıyordu. Sonra bir gün, her şey değişti."),
    L("Dinozorları ne yok etti? Ve bunu milyonlarca yıl sonra nasıl bilebiliyoruz?"),
    L("Bugün Dünya tarihinin en ünlü dedektiflik hikâyesini çözüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. O gün ne oldu? Bilim insanları bunu nereden biliyor? Ve kimler hayatta kaldı?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Londra'daki Doğa Tarihi Müzesi'ne göre 66 milyon yıl önce dinozorlar çok kötü bir gün geçirdi.", [1], "Londra'daki Doğa Tarihi Müzesi'ne göre altmış altı milyon yıl önce dinozorlar çok kötü bir gün geçirdi."),
    L("Dünya'daki hayvanların yaklaşık %75'i aynı dönemde yok oldu.", [2], "Dünya'daki hayvanların yaklaşık yüzde yetmiş beşi aynı dönemde yok oldu."),
    L("Bu kadar çok canlının birlikte yok olmasına kitlesel yok oluş denir. National Geographic'e göre bu, Dünya tarihindeki beşinci kitlesel yok oluştu.", [18], f"Bu kadar çok canlının birlikte yok olmasına kitlesel yok oluş denir. {NGs}'e göre bu, Dünya tarihindeki beşinci kitlesel yok oluştu."),
    L("Baş şüpheli: bir asteroit. Asteroitler, Güneş'in çevresinde dolanan kayalık gök cisimleridir.", [3]),
    L("NASA'ya göre Güneş sisteminin yaklaşık 4,6 milyar yıl önceki oluşumundan arta kalan parçalardır.", [3], "Nasa'ya göre Güneş sisteminin yaklaşık dört virgül altı milyar yıl önceki oluşumundan arta kalan parçalardır."),
    L("Bu asteroidin genişliği 10–15 kilometre arasındaydı ve bugünkü Meksika'da, Yucatán Yarımadası'na çarptı.", [3, 4], "Bu asteroidin genişliği on ile on beş kilometre arasındaydı ve bugünkü Meksika'da, Yukatan Yarımadası'na çarptı."),
    L("Çok yüksek hızla çarptı ve adeta buharlaştı. Geriye 150 kilometre çapında bir krater bıraktı: Chicxulub krateri.", [4, 5], "Çok yüksek hızla çarptı ve adeta buharlaştı. Geriye yüz elli kilometre çapında bir krater bıraktı: Çikşulub krateri."),
    L("Chicxulub. Söylemesi zor, biliyorum. Benim ses kartım bile iki kez denedi!", [], "Çik, şu, lub. Söylemesi zor, biliyorum. Benim ses kartım bile iki kez denedi!"),
])
e.sec("finding", [
    L("Çarpışma anında dev bir patlama dalgası ve sıcak dalgası yayıldı. Atmosfere çok büyük miktarda madde savruldu.", [5]),
    L("Dev dalgalar Amerika kıtalarının bazı bölgelerini kapladı. Büyük yangınlar çıktı.", [6]),
    L("Ama asıl felaket sonra geldi. Kurum bütün Dünya'ya yayıldı.", [7]),
    L("Güneş tamamen kapanmadı; ama yeryüzüne ulaşan ışık azaldı. Bu da bitkilerin büyümesini etkiledi.", [7]),
    L("Gerisi domino taşları gibiydi: etki, besin zincirinin basamaklarını birer birer devirdi ve ekosistem çöktü.", [8]),
    L("Peki bunu nereden biliyoruz? İpucu, kayaların arasındaki ince bir kil tabakasında saklı.", [9]),
    L("1980'de fizikçi Luis Alvarez ve jeolog oğlu Walter, iridyumca zengin bu kil tabakasının büyük bir asteroit çarpmasından kaynaklandığını öne sürdü.", [9], "Bin dokuz yüz seksende fizikçi Luis Alvares ve jeolog oğlu Voltır, iridyumca zengin bu kil tabakasının büyük bir asteroit çarpmasından kaynaklandığını öne sürdü."),
    L("İridyum, Dünya'da bulunan en nadir metallerden biridir.", [9]),
    L("Keşke ben de nadir bir metalden yapılmış olsaydım. Ama çoğum alüminyum!"),
    L("Başta bu fikir tartışmalıydı. Sonra krater bulundu: yaşı, yok oluşla tam olarak aynıydı!", [10]),
    L("Bugün bu, en yaygın kabul gören açıklamadır.", [10]),
])
e.sec("importance", [
    L("Ama suçlu yalnızca asteroit değil. Çarpışmadan önce de Dünya'nın iklimi değişiyordu.", [11]),
    L("Bugünkü Hindistan'ın orta kesiminde iki milyon yıl boyunca çok yoğun volkanik etkinlik yaşandı.", [11]),
    L("Müzeye göre asteroit, son ve öldürücü darbe oldu. Yok oluşun tam olarak nasıl işlediği ise hâlâ tartışılıyor.", [11]),
    L("Kimler yok oldu? Uçan sürüngenler pterozorlar, büyük deniz sürüngenleri ve ammonitler. Ağırlığı 25 kilogramı geçen bütün kara hayvanları da.", [12], "Kimler yok oldu? Uçan sürüngenler pterozorlar, büyük deniz sürüngenleri ve ammonitler. Ağırlığı yirmi beş kilogramı geçen bütün kara hayvanları da."),
    L("Ben o sınırın altındayım. Hafif olmanın iyi yanları da var!"),
    L("Peki kimler kurtuldu? Hayatta kalanlar küçüktü. Bitkiler de hayvanlardan daha az etkilendi; çünkü tohumları ve polenleri zor dönemlere daha uzun dayanabilir.", [13, 14]),
    L("Ve işte büyük sürpriz: dinozorların hepsi yok olmadı. Dinozorlar, kuşlar olarak hayatta kaldı!", [14]),
    L("Kuşlar, teropod denen etçil bir dinozor grubundan evrildi. Küçük olmaları, çok çeşitli besinler yiyebilmeleri ve uçabilmeleri büyük olasılıkla onlara yardım etti.", [15]),
    L("Bugün en az 11.000 kuş türü var. Yani penceredeki serçe, yaşayan bir dinozor!", [15], "Bugün en az on bir bin kuş türü var. Yani penceredeki serçe, yaşayan bir dinozor!"),
    L("Bir dahaki sefere bir güvercin görürsen selam ver. Sonuçta çok eski bir aileden geliyor!"),
    L("National Geographic'e göre dinozorların yok oluşu, memelilerin gelişip büyümesine olanak verdi.", [16], f"{NGs}'e göre dinozorların yok oluşu, memelilerin gelişip büyümesine olanak verdi."),
    L("Şimdi sıra sende! Dört domino taşı diz ve üzerlerine küçük kâğıtlarla şunları yaz: Güneş ışığı, bitki, otçul, etçil."),
    L("İlk taşı devir. Zincirin bir halkası bozulunca ötekilere ne oluyor? Ekosistemin çöküşü işte böyle işler.", [8]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? NASA'nın bir birimi, Dünya için tehlike oluşturabilecek asteroitleri bulmak ve izlemekle görevli.", [17], "Bunu biliyor muydun? Nasa'nın bir birimi, Dünya için tehlike oluşturabilecek asteroitleri bulmak ve izlemekle görevli."),
    L("Hızlı soru! Dinozorların bugün yaşayan temsilcileri hangi hayvanlar?", [14]),
    L("Düşün bakalım... Evet: kuşlar!", [14]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Arada bir gökyüzüne bakmayı da!"),
])
S = e.S
S(3, {"type": "hook", "question": "Dinozorları ne yok etti?", "emoji": "🦖"}, ["🦕", "☄️", "🌋", "🔍"], ["", "NASIL BİLİYORUZ?", "DEDEKTİFLİK ZAMANI 🔍"])
#S(1, {"type": "spotlight", "title": "Tanık değilim", "emoji": "🤖", "chips": [{"label": "Olay yerinde yoktum", "emoji": "🙅"}, {"label": "Daha üretilmemiştim", "emoji": "🏭"}, {"label": "İpuçlarını izleyeceğiz", "emoji": "🔍"}]}, ["🕵️", "🦴"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["O gün ne oldu?", "Bilim insanları bunu nereden biliyor?", "Kimler hayatta kaldı?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "big-number", "value": "66 milyon", "unit": "yıl önce", "label": "Dinozorların çok kötü günü", "sub": "Doğa Tarihi Müzesi", "icon": "🦖"}, ["📅", "🦕"], ["ÇOK KÖTÜ BİR GÜN"])
S(2, {"type": "spotlight", "title": "Kitlesel yok oluş", "emoji": "🦕", "chips": [{"label": "Hayvanların yaklaşık %75'i yok oldu", "emoji": "📉"}, {"label": "Çok sayıda canlı, birlikte", "emoji": "🐾"}, {"label": "Dünya tarihindeki beşincisi", "emoji": "🖐️"}]}, ["🦴", "🌍"], ["YAKLAŞIK DÖRTTE ÜÇÜ", "KİTLESEL YOK OLUŞ"])
S(2, {"type": "diagram", "title": "Baş şüpheli: asteroit", "layout": "flow", "nodes": [{"label": "Kayalık gök cismi", "emoji": "☄️"}, {"label": "Güneş'in çevresinde dolanır", "emoji": "☀️"}, {"label": "Yaklaşık 4,6 milyar yıllık kalıntı", "emoji": "🪨"}]}, ["🔭", "🌌"], ["ASTEROİT ☄️", "ÇOK ESKİ KALINTI"])
S(2, {"type": "comparison", "title": "Çarpışma", "left": {"title": "Asteroit ☄️", "items": ["10–15 km genişlik", "Çok yüksek hız", "Adeta buharlaştı"]}, "right": {"title": "Krater 🕳️", "items": ["Chicxulub", "Yucatán Yarımadası, Meksika", "150 km çap"]}}, ["💥", "🗺️"], ["MEKSİKA'YA ÇARPTI", "DEV KRATER 🕳️"])
S(1, {"type": "spotlight", "title": "Chicxulub", "emoji": "🗣️", "chips": [{"label": "Çik", "emoji": "1️⃣"}, {"label": "şu", "emoji": "2️⃣"}, {"label": "lub!", "emoji": "3️⃣"}]}, ["🎤", "😅"], ["ÇİK-ŞU-LUB 😅"])
S(2, {"type": "diagram", "title": "İlk anlar", "layout": "flow", "nodes": [{"label": "Patlama ve sıcak dalgası", "emoji": "💥"}, {"label": "Atmosfere savrulan madde", "emoji": "🌫️"}, {"label": "Dev dalgalar", "emoji": "🌊"}, {"label": "Yangınlar", "emoji": "🔥"}]}, ["☄️", "🌎"], ["PATLAMA DALGASI 💥", "DALGALAR + YANGIN"])
S(2, {"type": "meter", "title": "Yeryüzüne ulaşan ışık", "label": "Güneş ışığı", "emoji": "☀️", "phases": [{"label": "Kurum bütün Dünya'ya yayılır", "level": 0.6, "emoji": "🌫️"}, {"label": "Işık azalır: bitkiler etkilenir", "level": 0.22, "emoji": "🌿"}], "note": NOTE}, ["🌥️", "🥀"], ["KURUM 🌫️", "IŞIK AZALDI"])
S(1, {"type": "diagram", "title": "Domino etkisi", "layout": "flow", "nodes": [{"label": "Bitkiler", "emoji": "🌿"}, {"label": "Bitki yiyenler", "emoji": "🦕"}, {"label": "Et yiyenler", "emoji": "🦖"}, {"label": "Ekosistem çöker", "emoji": "📉"}]}, ["🁢", "⛓️"], ["DOMİNO ETKİSİ"])
S(2, {"type": "spotlight", "title": "İpucu: kil tabakası", "emoji": "🔍", "chips": [{"label": "İnce bir kil tabakası", "emoji": "🪨"}, {"label": "İridyumca zengin", "emoji": "✨"}, {"label": "1980: Alvarez baba ve oğul", "emoji": "👨‍🔬"}]}, ["🕵️", "🧪"], ["KİL TABAKASI", "ALVAREZ KURAMI"])
S(2, {"type": "big-number", "value": "İridyum", "label": "Dünya'daki en nadir metallerden biri", "sub": "Doğa Tarihi Müzesi", "icon": "💎"}, ["✨", "🤖"], ["İRİDYUM 💎", "BEN ALÜMİNYUMUM 😅"])
S(2, {"type": "comparison", "title": "Kanıtlar birleşiyor", "left": {"title": "Kil tabakası 🪨", "items": ["İridyumca zengin", "Kayalarda izlenebiliyor"]}, "right": {"title": "Krater 🕳️", "items": ["Bulundu", "Yaşı yok oluşla aynı"]}}, ["🧩", "✅"], ["KRATER BULUNDU!", "EN YAYGIN AÇIKLAMA ✅"])
S(3, {"type": "bullets", "title": "Tek suçlu asteroit değil", "items": ["İklim zaten değişiyordu", "Hindistan'da iki milyon yıl volkanik etkinlik", "Asteroit: son darbe", "Ayrıntılar hâlâ tartışılıyor"]}, ["🌋", "🌡️"], ["İKLİM DEĞİŞİYORDU", "VOLKANLAR 🌋", "SON DARBE ☄️"])
S(2, {"type": "spotlight", "title": "Kimler yok oldu?", "emoji": "🦴", "chips": [{"label": "Pterozorlar: uçan sürüngenler", "emoji": "🦅"}, {"label": "Büyük deniz sürüngenleri", "emoji": "🌊"}, {"label": "Ammonitler", "emoji": "🐚"}, {"label": "25 kg'dan ağır kara hayvanları", "emoji": "⚖️"}]}, ["🦕", "🤖"], ["YOK OLANLAR", "BEN HAFİFİM 😄"])
S(1, {"type": "comparison", "title": "Kimler kurtuldu?", "left": {"title": "Küçük hayvanlar 🐭", "items": ["Hayatta kalanlar küçüktü"]}, "right": {"title": "Bitkiler 🌱", "items": ["Tohum ve polen dayanıklı", "Daha az etkilendiler"]}}, ["🌰", "🐁"], ["KÜÇÜKLER KURTULDU"])
S(1, {"type": "big-number", "value": "Kuşlar", "label": "Yaşayan dinozorlar", "sub": "Dinozorlar kuşlar olarak hayatta kaldı", "icon": "🐦"}, ["🦖", "🪶"], ["BÜYÜK SÜRPRİZ! 🐦"])
S(3, {"type": "spotlight", "title": "Kuşlar neden başardı?", "emoji": "🐦", "chips": [{"label": "Teropodlardan evrildiler", "emoji": "🦖"}, {"label": "Küçük beden", "emoji": "🤏"}, {"label": "Çok çeşitli besin", "emoji": "🌰"}, {"label": "Uçabilme", "emoji": "🪽"}, {"label": "Bugün en az 11.000 tür", "emoji": "🌍"}]}, ["🪶", "🐤"], ["TEROPOD 🦖", "SERÇE = DİNOZOR!", "SELAM VER 🕊️"])
S(1, {"type": "bullets", "title": "Sıra memelilerde", "items": ["Dinozorlardan sonra geliştiler", "Zamanla büyüdüler"]}, ["🐭", "🐘"], ["MEMELİLER 🐭"])
S(2, {"type": "diagram", "title": "Sen de dene: domino besin zinciri", "layout": "flow", "nodes": [{"label": "Güneş ışığı", "emoji": "☀️"}, {"label": "Bitki", "emoji": "🌿"}, {"label": "Otçul", "emoji": "🦕"}, {"label": "Etçil", "emoji": "🦖"}]}, ["🁢", "📓"], ["DENEY ZAMANI 🔬", "İLK TAŞI DEVİR!"])
S(1, {"type": "spotlight", "title": "Gökyüzü nöbeti", "emoji": "🛰️", "chips": [{"label": "NASA asteroitleri bulur", "emoji": "🔭"}, {"label": "İzler", "emoji": "📡"}, {"label": "Tehlikeli olabilecekleri inceler", "emoji": "☄️"}]}, ["🌍", "🛡️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Dinozorların yaşayan temsilcileri kim?", "emoji": "🤔"}, ["🦖", "🐦"], ["HIZLI SORU!", "KUŞLAR ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 12, "videoTitle": "Dinozorlar neden yok oldu?", "paperTitleTr": "Dinozorlar neden yok oldu?",
  "takeaways": ["Dev bir asteroit çarptı; kurum ışığı azalttı, besin zinciri çöktü", "İridyumlu kil tabakası ve Chicxulub krateri bunun kanıtıdır", "Dinozorlar kuşlar olarak hâlâ yaşıyor"],
  "description": "Dinozorları ne yok etti ve bunu nereden biliyoruz? Bu bölümde 66 milyon yıl önceki asteroit çarpışmasını, Chicxulub kraterini, kurumun ışığı nasıl azalttığını ve besin zincirinin domino gibi nasıl çöktüğünü; iridyumlu kil tabakasını ve Alvarez kuramını; volkanların ve iklim değişikliğinin rolünü keşfediyoruz. Kimler yok oldu, kimler kurtuldu, kuşlar neden yaşayan dinozorlardır? Sonunda domino besin zinciri deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kitlesel yok oluş", "meaning": "Çok sayıda canlı türünün aynı dönemde yok olması."},
    {"term": "Asteroit", "meaning": "Güneş'in çevresinde dolanan kayalık gök cismi."},
    {"term": "Krater", "meaning": "Bir gök cisminin çarpmasıyla oluşan büyük çukur."},
    {"term": "İridyum", "meaning": "Dünya'da çok nadir bulunan bir metal."},
    {"term": "Besin zinciri", "meaning": "Canlıların birbirini besin olarak izlediği sıra: bitki, otçul, etçil."},
    {"term": "Ekosistem", "meaning": "Bir bölgedeki canlıların ve çevrelerinin oluşturduğu bütün."},
    {"term": "Pterozor", "meaning": "Dinozorlarla aynı dönemde yaşamış uçan sürüngen."},
    {"term": "Ammonit", "meaning": "Sarmal kabuklu, soyu tükenmiş deniz canlısı."},
    {"term": "Teropod", "meaning": "Kuşların da evrildiği, etçil dinozor grubu."}],
  "song": e.song("Dinozorların Son Günü", [("☄️", "Asteroit"), ("🦖", "Dinozor"), ("🌋", "Volkan"), ("🐦", "Kuş"), ("🐭", "Memeli")],
    ["Altmış altı milyon yıl önce bir gün", "Gökten bir asteroit düştü hızla", "Kurum yayıldı, ışık azaldı", "Bitkiler soldu, zincir koptu"],
    ["Domino, domino; zincir devrildi!", "Dev dinozorlar sahneden çekildi", "Kil tabakasında iridyum izi", "Krater bulundu, çözüldü gizi"],
    ["Volkanlar da iklimi değiştirdi", "Asteroit son darbeyi indirdi", "Küçükler dayandı, tohumlar bekledi", "Memeliler gelişti, büyüdü"],
    ["Domino, domino; zincir devrildi!", "Dev dinozorlar sahneden çekildi", "Ama bitmedi hikâye: kuşlar uçuyor!", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
