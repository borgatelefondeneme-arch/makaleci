"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:okyanusun-derinlerinde-ne-var"
S1 = "NOAA — How far does light travel in the ocean?"; S2 = "NOAA Ocean Exploration — How deep is the ocean?"; S3 = "NOAA Ocean Exploration — How much of the ocean has been explored?"
S4 = "NOAA Ocean Exploration — What is bioluminescence?"; S5 = "NOAA — What is a hydrothermal vent?"; S6 = "NOAA — How does pressure change with ocean depth?"
S7 = "National Geographic Education — Bioluminescence"; S8 = "NOAA — How much water is in the ocean?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "How far does light travel in the ocean?", "publisher": "NOAA", "url": "https://oceanservice.noaa.gov/facts/light_travel.html"},
    {"id": "k2", "title": "How deep is the ocean?", "publisher": "NOAA", "url": "https://oceanexplorer.noaa.gov/facts/ocean-depth.html"},
    {"id": "k3", "title": "How much of the ocean has been explored?", "publisher": "NOAA", "url": "https://oceanexplorer.noaa.gov/facts/explored.html"},
    {"id": "k4", "title": "What is bioluminescence?", "publisher": "NOAA", "url": "https://oceanexplorer.noaa.gov/facts/bioluminescence.html"},
    {"id": "k5", "title": "What is a hydrothermal vent?", "publisher": "NOAA", "url": "https://oceanservice.noaa.gov/facts/vents.html"},
    {"id": "k6", "title": "How does pressure change with ocean depth?", "publisher": "NOAA", "url": "https://oceanservice.noaa.gov/facts/pressure.html"},
    {"id": "k7", "title": "Bioluminescence", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/bioluminescence/"},
    {"id": "k8", "title": "How much water is in the ocean?", "publisher": "NOAA", "url": "https://oceanservice.noaa.gov/facts/oceanwater.html"}],
  "facts": [
    F(1, "Okyanus gezegenimizin yüzeyinin %70'inden fazlasını kaplar; Dünya'daki suyun yaklaşık %97'si okyanustadır.", "The ocean covers more than 70 percent of the surface of our planet. / About 97 percent of Earth's water is in the ocean.", S8, ["70", "97"]),
    F(2, "Okyanusun ortalama derinliği 3.682 metredir.", "The average depth of the ocean is 3,682 meters, or 12,080 feet.", S2, ["3.682"]),
    F(3, "Okyanusun üst 200 metresine öfotik, yani 'güneşli' bölge denir.", "The upper 200 meters of the ocean is called the euphotic, or \"sunlight,\" zone.", S1, ["200"]),
    F(4, "200–1.000 metre arası genellikle 'alacakaranlık' bölgesi olarak anılır; 200 metrenin ötesinde kayda değer ışık nadiren bulunur.", "is usually referred to as the \"twilight\" zone, but is officially the dysphotic zone / there is rarely any significant light beyond 200 meters", S1, ["200", "1.000"]),
    F(5, "Afotik bölge 1.000 metrenin altındadır; Güneş ışığı ulaşmaz, bölge karanlıktır.", "The aphotic zone exists in depths below 1,000 meters. / sunlight does not penetrate; the zone is bathed in darkness", S1, ["1.000"]),
    F(6, "200 metrenin ötesine o kadar az ışık ulaşır ki fotosentez artık mümkün olmaz.", "Such a minuscule amount of light penetrates beyond a depth of 200 meters that photosynthesis is no longer possible.", S1, ["200"]),
    F(7, "Her 33 fitte (10,06 metre) basınç bir atmosfer artar; deniz seviyesinde çevremizdeki hava bedenimize basınç uygular.", "For every 33 feet (10.06 meters) you go down, the pressure increases by one atmosphere. / At sea level, the air that surrounds us presses down on our bodies at 14.7 pounds per square inch.", S6, ["10.06"]),
    F(8, "Denizde ne kadar derine inilirse üstteki suyun aşağı doğru yaptığı basınç o kadar artar; balinalar bedenleri daha esnek olduğu için büyük basınç değişimlerine dayanabilir.", "The deeper you go under the sea, the greater the pressure of the water pushing down on you. / Whales, for instance, can withstand dramatic pressure changes because their bodies are more flexible.", S6),
    F(9, "Okyanusun en derin yeri 10.935 metredir; Büyük Okyanus'taki Mariana Çukuru'nda, Challenger Derinliği denen yerdedir.", "The deepest place in the ocean measures 10,935 meters (35,876 feet) / found in the Pacific Ocean's Mariana Trench, at a place called Challenger Deep", S2, ["10.935"]),
    F(10, "Biyolüminesans, bir canlının kimyasal tepkimeyle ürettiği ışıktır; okyanusta çok yaygındır; 200 ile 1.000 metre arasında yaşayan hayvanların %80'i biyolüminesanstır.", "Bioluminescence is light produced by an organism using a chemical reaction. / bioluminescence is very common in the ocean / 80 percent of the animals that live between 200 and 1,000 meters (656 and 3,280 feet) depth are bioluminescent", S4, ["200", "1.000", "80"]),
    F(11, "Biyolüminesans 'soğuk ışıktır': çok az ısı yayar. Işığı asıl üreten bileşik lusiferindir.", "Bioluminescence is a \"cold light.\" Cold light means less than 20% of the light generates thermal radiation, or heat. / Luciferin is the compound that actually produces light.", S7),
    F(12, "Canlılar biyolüminesansı av yakalamak, avcılardan korunmak ve eş bulmak için kullanır; yine de asıl amacı ya da işlevi tam olarak bilinmiyor.", "Bioluminescence is used by living things to hunt prey, defend against predators, find mates / we don't really know the main purpose or function of bioluminescence", S7 + "; " + S4),
    F(13, "Fener balığı avını çekmek için biyolüminesans kullanır; ipliğin ucundaki topu yakabilir.", "The most famous predator to use bioluminescence may be the anglerfish, which uses bioluminescence to lure prey. / On the end of the filament is a ball (called the esca) that the anglerfish can light up.", S7),
    F(14, "Vampir kalamar, avcıları ürkütüp şaşırtan ve oyalayan yapışkan, biyolüminesans bir salgı fırlatır.", "the vampire squid ejects sticky bioluminescent mucus, which can startle, confuse, and delay predators", S7),
    F(15, "Hidrotermal bacalar deniz suyunun magmayla karşılaştığı yerlerde oluşur; buradaki sıcak su, derinlikteki aşırı basınç nedeniyle kaynamaz; ilk kez 1977'de Galapagos Adaları yakınında keşfedildi ve çevrelerinde daha önce hiç görülmemiş çok sayıda canlı vardı.", "Hydrothermal vents form at locations where seawater meets magma. / Hot seawater in hydrothermal vents does not boil because of the extreme pressure at the depths / Scientists first discovered hydrothermal vents in 1977 while exploring an oceanic spreading ridge near the Galapagos Islands. / the hydrothermal vents were surrounded by large numbers of organisms that had never been seen before", S5, ["1977"]),
    F(16, "Nisan 2026 itibarıyla küresel deniz tabanının %28,7'sinin haritası çıkarılmıştı; kâşifler derin okyanus tabanının %0,001'inden azını görmüştür.", "As of April 2026, 28.7% of the global seafloor had been mapped / explorers have seen less than 0.001% of the deep ocean seafloor", S3, ["2026", "28.7", "0.001"]),
    F(17, "Derinler, uzaktan kumandalı araçlar gibi dalış araçlarıyla ve genellikle gemilere takılan sonarla incelenir.", "deploy submersibles, like remotely operated vehicles / usually mounted to ships, that can reveal the seafloor in greater detail", S3),
    F(18, "Bilim insanlarının tahminine göre okyanusta 700.000 ile 1 milyon arasında tür olabilir.", "Scientists estimate there may be between 700,000 and 1 million species in the ocean", S3, ["700.000", "1"]),
]}
e = Ep(); L = e.L
NO = "Noa"; NGs = "Neşınıl Ciyografik"
e.sec("hook", [
    L("Okyanus, gezegenimizin yüzeyinin %70'inden fazlasını kaplar. Ama derinlerini neredeyse hiç görmedik!", [1, 16], "Okyanus, gezegenimizin yüzeyinin yüzde yetmişinden fazlasını kaplar. Ama derinlerini neredeyse hiç görmedik!"),
    L("Güneş ışığının hiç ulaşmadığı o karanlıkta kimler yaşıyor? Ve kendi ışığını üreten canlılar gerçek mi?"),
    L("Bugün denizin dibine dalıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Okyanus ne kadar derin? Işık ve basınç derinlikle nasıl değişir? Ve karanlıkta canlılar nasıl yaşar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre Dünya'daki suyun yaklaşık %97'si okyanustadır.", [1], f"A Be De Ulusal Okyanus ve Atmosfer Dairesi, {NO}'ya göre Dünya'daki suyun yaklaşık yüzde doksan yedisi okyanustadır."),
    L("Okyanusun ortalama derinliği 3.682 metredir.", [2], "Okyanusun ortalama derinliği üç bin altı yüz seksen iki metredir."),
    L("En derin noktası Büyük Okyanus'taki Mariana Çukuru'ndadır. Challenger Derinliği denen bu yer 10.935 metre derinliktedir.", [9], "En derin noktası Büyük Okyanus'taki Mariana Çukuru'ndadır. Çelıncır Derinliği denen bu yer on bin dokuz yüz otuz beş metre derinliktedir."),
    L("Ben oraya inemem. Su geçirmezlik belgem yok!"),
    L("Derine indikçe iki şey hızla değişir: ışık ve basınç. Önce ışığa bakalım."),
    L("İlk 200 metreye güneşli bölge denir. Fotosentez yalnızca burada mümkündür; çünkü daha derine neredeyse hiç ışık ulaşmaz.", [3, 6], "İlk iki yüz metreye güneşli bölge denir. Fotosentez yalnızca burada mümkündür; çünkü daha derine neredeyse hiç ışık ulaşmaz."),
    L("200 ile 1.000 metre arası alacakaranlık bölgesidir. Burada kayda değer ışık nadiren bulunur.", [4], "İki yüz ile bin metre arası alacakaranlık bölgesidir. Burada kayda değer ışık nadiren bulunur."),
    L("1.000 metrenin altına ise Güneş ışığı hiç ulaşmaz. Burası zifiri karanlıktır.", [5], "Bin metrenin altına ise Güneş ışığı hiç ulaşmaz. Burası zifiri karanlıktır."),
])
e.sec("finding", [
    L("Şimdi basınç. Üstündeki su seni aşağı doğru iter; ne kadar derine inersen basınç o kadar artar.", [8]),
    L("NOAA'ya göre yaklaşık her on metrede basınç bir atmosfer daha artar. Bir atmosfer, deniz kıyısında havanın üstümüze yaptığı basınç kadardır.", [7], f"{NO}'ya göre yaklaşık her on metrede basınç bir atmosfer daha artar. Bir atmosfer, deniz kıyısında havanın üstümüze yaptığı basınç kadardır."),
    L("Peki canlılar buna nasıl dayanır? Örneğin balinaların bedenleri daha esnektir; bu sayede büyük basınç değişimlerine dayanabilirler.", [8]),
    L("Karanlığa gelince: derinlerdeki pek çok canlı kendi ışığını üretir! Buna biyolüminesans denir: bir canlının kimyasal tepkimeyle ışık üretmesi.", [10]),
    L("200 ile 1.000 metre arasında yaşayan hayvanların %80'i biyolüminesanstır.", [10], "İki yüz ile bin metre arasında yaşayan hayvanların yüzde sekseni biyolüminesanstır."),
    L("National Geographic'e göre bu ışığı üreten maddenin adı lusiferindir. Üstelik bu soğuk bir ışıktır: çok az ısı yayar.", [11], f"{NGs}'e göre bu ışığı üreten maddenin adı lusiferindir. Üstelik bu soğuk bir ışıktır: çok az ısı yayar."),
    L("Canlılar bu ışığı av yakalamak, düşmandan korunmak ve eş bulmak için kullanır.", [12]),
    L("En ünlüsü fener balığı: başından uzanan ipliğin ucundaki topu yakar ve avını kendine çeker.", [13]),
    L("Başında lamba taşıyan bir balık! Bence antenimdeki yıldızı kıskanmış."),
])
e.sec("importance", [
    L("Vampir kalamar ise tehlike anında yapışkan ve parlayan bir salgı fırlatır; düşmanını şaşırtıp oyalar.", [14]),
    L("Derinlerde bir sürpriz daha var: hidrotermal bacalar. Deniz suyunun magmayla karşılaştığı yerlerde oluşurlar.", [15]),
    L("Bu bacalardaki su çok sıcaktır; ama o derinlikteki aşırı basınç yüzünden kaynamaz.", [15]),
    L("Bilim insanları bu bacaları ilk kez 1977'de, Galapagos Adaları yakınında keşfetti. Çevrelerinde daha önce hiç görülmemiş pek çok canlı vardı.", [15], "Bilim insanları bu bacaları ilk kez bin dokuz yüz yetmiş yedide, Galapagos Adaları yakınında keşfetti. Çevrelerinde daha önce hiç görülmemiş pek çok canlı vardı."),
    L("Peki okyanusu ne kadar tanıyoruz? Nisan 2026 itibarıyla deniz tabanının yalnızca %28,7'sinin haritası çıkarılmıştı.", [16], "Peki okyanusu ne kadar tanıyoruz? Nisan iki bin yirmi altı itibarıyla deniz tabanının yalnızca yüzde yirmi sekiz virgül yedisinin haritası çıkarılmıştı."),
    L("Derin deniz tabanının gözle görülen kısmı ise %0,001'den az!", [16], "Derin deniz tabanının gözle görülen kısmı ise yüz binde birden az!"),
    L("Bilim insanları derinleri, gemilere takılan sonar cihazlarıyla ve uzaktan kumandalı araçlarla inceler.", [17]),
    L("Uzaktan kumandalı araçlar benim kuzenlerim sayılır. Aile toplantılarımız biraz ıslak geçiyor!"),
    L("Tahminlere göre okyanusta 700.000 ile 1 milyon arasında tür yaşıyor olabilir.", [18], "Tahminlere göre okyanusta yedi yüz bin ile bir milyon arasında tür yaşıyor olabilir."),
    L("Şimdi sıra sende! Büyük bir kâğıdı üçe böl: güneşli bölge, alacakaranlık bölgesi ve karanlık bölge."),
    L("Her bölgeye oraya uygun canlılar çiz. Karanlık bölgedekileri fosforlu kalemle boya; ışığı kapatınca kendi derin denizin parlasın!"),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? NOAA'ya göre biyolüminesansın asıl işlevinin ne olduğu hâlâ tam olarak bilinmiyor.", [12], f"Bunu biliyor muydun? {NO}'ya göre biyolüminesansın asıl işlevinin ne olduğu hâlâ tam olarak bilinmiyor."),
    L("Hızlı soru! Fotosentez okyanusun hangi bölgesinde yapılabilir?", [6]),
    L("Düşün bakalım... Evet: ilk 200 metredeki güneşli bölgede!", [3, 6], "Düşün bakalım... Evet: ilk iki yüz metredeki güneşli bölgede!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben yüzeyde kalıyorum; aşağıdaki kuzenlerime selam söyle!"),
])
S = e.S
S(3, {"type": "hook", "question": "Okyanusun derinlerinde ne var?", "emoji": "🌊"}, ["🐙", "🐟", "🦑", "🐚"], ["", "KARANLIKTA KİM VAR?", "DİBE DALIYORUZ!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Okyanus ne kadar derin?", "Işık ve basınç derinlikle nasıl değişir?", "Karanlıkta canlılar nasıl yaşar?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "big-number", "value": "%97", "label": "Dünya'daki suyun okyanustaki payı", "sub": "NOAA", "icon": "🌍"}, ["💧", "🌊"], ["SUYUN ÇOĞU BURADA"])
S(3, {"type": "comparison", "title": "Ne kadar derin?", "left": {"title": "Ortalama 🌊", "items": ["3.682 metre"]}, "right": {"title": "En derin nokta ⬇️", "items": ["10.935 metre", "Challenger Derinliği", "Mariana Çukuru"]}}, ["📏", "🤿"], ["ORTALAMA DERİNLİK", "MARİANA ÇUKURU", "BELGEM YOK 😅"])
S(1, {"type": "spotlight", "title": "Derine indikçe", "emoji": "🤿", "chips": [{"label": "Işık azalır", "emoji": "🔦"}, {"label": "Basınç artar", "emoji": "⬇️"}]}, ["🌊", "🫧"], ["IŞIK + BASINÇ"])
S(3, {"type": "stages", "title": "Okyanusun ışık bölgeleri", "rows": [{"label": "Güneşli bölge: ilk 200 m", "emoji": "☀️"}, {"label": "Alacakaranlık: 200–1.000 m", "emoji": "🌆"}, {"label": "Karanlık bölge: 1.000 m altı", "emoji": "🌑"}], "path": [0, 0, 0, 1, 1, 1, 2, 2, 2], "highlightRow": 0, "note": NOTE}, [], ["GÜNEŞLİ BÖLGE ☀️", "ALACAKARANLIK 🌆", "ZİFİRİ KARANLIK 🌑"])
S(3, {"type": "meter", "title": "Basınç", "label": "Basınç", "emoji": "🐋", "phases": [{"label": "Üstündeki su aşağı iter", "level": 0.3, "emoji": "⬇️"}, {"label": "Her on metrede bir atmosfer daha", "level": 0.65, "emoji": "📈"}, {"label": "Balinalar: esnek beden", "level": 0.9, "emoji": "🐋"}], "note": NOTE}, ["🤿", "🫧"], ["BASINÇ ARTAR", "BİR ATMOSFER DAHA", "ESNEK BEDEN 🐋"])
S(2, {"type": "spotlight", "title": "Biyolüminesans", "emoji": "✨", "chips": [{"label": "Canlının ürettiği ışık", "emoji": "💡"}, {"label": "Kimyasal tepkimeyle", "emoji": "🧪"}, {"label": "200–1.000 m arasındaki hayvanların %80'i", "emoji": "🐟"}]}, ["🪼", "🦑"], ["KENDİ IŞIĞI! ✨", "ÇOK YAYGIN"], fx="sparkle")
S(2, {"type": "diagram", "title": "Işık ne işe yarar?", "layout": "flow", "nodes": [{"label": "Lusiferin: ışığı üretir", "emoji": "🧪"}, {"label": "Av yakalamak", "emoji": "🎣"}, {"label": "Korunmak", "emoji": "🛡️"}, {"label": "Eş bulmak", "emoji": "💞"}]}, ["❄️", "💡"], ["LUSİFERİN • SOĞUK IŞIK", "ÜÇ İŞLEV"])
S(2, {"type": "big-number", "value": "Fener balığı", "label": "Ucundaki topu yakar, avını çeker", "sub": "National Geographic", "icon": "💡"}, ["🐟", "🎣"], ["FENER BALIĞI 🎣", "YILDIZIMI KISKANDI ⭐"], fx="sparkle")
S(1, {"type": "spotlight", "title": "Vampir kalamar", "emoji": "🦑", "chips": [{"label": "Yapışkan, parlayan salgı fırlatır", "emoji": "✨"}, {"label": "Düşmanı şaşırtır ve oyalar", "emoji": "😵"}]}, ["🌑", "🫧"], ["VAMPİR KALAMAR 🦑"])
S(3, {"type": "diagram", "title": "Hidrotermal bacalar", "layout": "flow", "nodes": [{"label": "Deniz suyu magmayla karşılaşır", "emoji": "🌋"}, {"label": "Çok sıcak su", "emoji": "♨️"}, {"label": "Basınç yüzünden kaynamaz", "emoji": "🚫"}, {"label": "1977: keşif ve yeni canlılar", "emoji": "🔎"}]}, ["🪸", "🦐"], ["HİDROTERMAL BACA", "KAYNAMAZ!", "GALAPAGOS YAKINI"], fx="erupt")
S(2, {"type": "big-number", "value": "%28,7", "label": "Deniz tabanının haritası çıkarılan kısmı", "sub": "Nisan 2026 • Görülen kısım: %0,001'den az", "icon": "🗺️"}, ["🧭", "🚢"], ["HARİTASI EKSİK", "NEREDEYSE HİÇ GÖRMEDİK"])
S(2, {"type": "comparison", "title": "Derinler nasıl incelenir?", "left": {"title": "Sonar 📡", "items": ["Gemilere takılır", "Tabanı ayrıntılı gösterir"]}, "right": {"title": "Uzaktan kumandalı araç 🤖", "items": ["Derine iner", "Muma'nın kuzenleri!"]}}, ["🚢", "🎮"], ["SONAR + ARAÇLAR", "KUZENLERİM 🤖"])
S(1, {"type": "big-number", "value": "1 milyon", "label": "türe kadar canlı yaşıyor olabilir", "sub": "Tahmin: 700.000 ile 1 milyon arası", "icon": "🐠"}, ["🐙", "🦈"], ["KALABALIK!"])
S(2, {"type": "bullets", "title": "Sen de dene: derin deniz posteri 🎨", "items": ["Kâğıdı üç bölgeye ayır", "Her bölgeye uygun canlılar çiz", "Karanlık bölgeyi fosforlu kalemle boya", "Işığı kapat: denizin parlasın!"]}, ["🖍️", "✨"], ["POSTER ZAMANI 🎨", "KARANLIKTA PARLAR ✨"])
S(1, {"type": "spotlight", "title": "Hâlâ bir sır", "emoji": "❓", "chips": [{"label": "Biyolüminesansın asıl işlevi ne?", "emoji": "✨"}, {"label": "Henüz tam olarak bilinmiyor", "emoji": "🔬"}]}, ["🪼", "📚"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Fotosentez hangi bölgede yapılabilir?", "emoji": "🤔"}, ["☀️", "🌿"], ["HIZLI SORU!", "GÜNEŞLİ BÖLGE ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 15, "videoTitle": "Okyanusun derinlerinde ne var?", "paperTitleTr": "Okyanusun derinlerinde ne var?",
  "theme": {"backdrop": "ocean", "actors": [{"kind": "swim", "emoji": "🐟", "every": 13}, {"kind": "swim", "emoji": "🐙", "every": 21}, {"kind": "swim", "emoji": "🦑", "every": 27}, {"kind": "swim", "emoji": "🐡", "every": 17, "size": 80}]},
  "takeaways": ["Derine indikçe ışık azalır, basınç artar", "Karanlıkta birçok canlı kendi ışığını üretir: biyolüminesans", "Deniz tabanının çoğunun haritası henüz çıkarılmadı"],
  "description": "Güneş ışığının ulaşmadığı derinlerde kimler yaşar? Bu bölümde okyanusun derinliğini, güneşli, alacakaranlık ve karanlık bölgeleri; derinlikle artan basıncı; biyolüminesansı, lusiferini, fener balığını ve vampir kalamarı; hidrotermal bacaları keşfediyoruz. Deniz tabanının ne kadarını tanıyoruz, derinler nasıl inceleniyor? Sonunda derin deniz posteri etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Fotosentez", "meaning": "Bitkilerin ve alglerin ışıkla besin üretmesi."},
    {"term": "Basınç", "meaning": "Bir yüzeye uygulanan itme kuvveti; suyun altında üstteki suyun ağırlığından doğar."},
    {"term": "Atmosfer", "meaning": "Burada bir basınç birimi: deniz kıyısında havanın yaptığı basınç kadar."},
    {"term": "Biyolüminesans", "meaning": "Bir canlının kimyasal tepkimeyle kendi ışığını üretmesi."},
    {"term": "Lusiferin", "meaning": "Biyolüminesansta ışığı üreten madde."},
    {"term": "Hidrotermal baca", "meaning": "Deniz tabanında, suyun magmayla karşılaşıp ısındığı yerlerde oluşan sıcak su çıkışı."},
    {"term": "Magma", "meaning": "Yerin altındaki erimiş kaya."},
    {"term": "Sonar", "meaning": "Ses dalgalarıyla deniz tabanını ölçen cihaz."}],
  "song": e.song("Derinlerin Işığı", [("🐟", "Fener balığı"), ("🦑", "Vampir kalamar"), ("🐋", "Balina"), ("✨", "Işık"), ("🌋", "Baca")],
    ["İlk iki yüz metre güneşle dolu", "Sonra alacakaranlık, ışık solar", "Bin metrenin altı zifiri karanlık", "Her on metrede basınç artar"],
    ["Dal dal dal, derinlere dal!", "Karanlıkta ışıklar yanar", "Biyolüminesans: canlının feneri", "Lusiferin parlar, soğuk ışık verir"],
    ["Fener balığı avını ışıkla çeker", "Vampir kalamar parlak salgı fırlatır", "Bacalarda su kaynamaz basınçtan", "Haritası çıkmamış nice yer var"],
    ["Dal dal dal, derinlere dal!", "Karanlıkta ışıklar yanar", "Keşfedilecek çok şey var daha", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "swim", "emoji": "🦈", "every": 8, "size": 260}, {"kind": "swim", "emoji": "🐙", "every": 10}, {"kind": "swim", "emoji": "🐢", "every": 12}, {"kind": "swarm", "emoji": "🐠"}, {"kind": "chase", "emoji": "🐋", "emoji2": "🦑", "every": 14, "size": 280}])}
e.write(D, facts, script)
