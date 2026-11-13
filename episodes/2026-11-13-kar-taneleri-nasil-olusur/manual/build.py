"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kar-taneleri-nasil-olusur"
S1 = "NOAA — How do snowflakes form?"; S2 = "NOAA NSSL — Severe Weather 101: Winter Weather Types"; S3 = "NSIDC — Science of Snow"; S4 = "NSIDC — Quick Facts About Snow"; S5 = "Met Office — Snow"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "How do snowflakes form? Get the science behind snow", "publisher": "NOAA", "url": "https://www.noaa.gov/stories/how-do-snowflakes-form-get-science-behind-snow"},
    {"id": "k2", "title": "Severe Weather 101: Winter Weather Types", "publisher": "NSSL", "url": "https://www.nssl.noaa.gov/education/svrwx101/winter/types/"},
    {"id": "k3", "title": "Science of Snow", "publisher": "NSIDC", "url": "https://nsidc.org/learn/parts-cryosphere/snow/science-snow"},
    {"id": "k4", "title": "Quick Facts About Snow", "publisher": "NSIDC", "url": "https://nsidc.org/learn/parts-cryosphere/snow/quick-facts-about-snow"},
    {"id": "k5", "title": "Snow", "publisher": "Met Office", "url": "https://weather.metoffice.gov.uk/learn-about/weather/types-of-weather/snow"}],
  "facts": [
    F(1, "Bir kar tanesi, çok soğuk bir su damlacığı gökyüzünde bir polen ya da toz parçacığının üzerinde donunca oluşmaya başlar; su buharı ilk kristalin üzerinde donarak yeni kristaller kurar.", "A snowflake begins to form when an extremely cold water droplet freezes onto a pollen or dust particle in the sky. / water vapor freezes onto the primary crystal, building new crystals", S1),
    F(2, "Sıcaklık 0°C'nin altına düşünce su buharı sıvı evreye geçmeden doğrudan buza dönüşür.", "when temperatures drop below 0°C (32°F), water vapor condenses directly into ice without going through the liquid stage.", S4, ["0"]),
    F(3, "Kar taneleri bulutlardan düşen tek buz kristalleri ya da buz kristali kümeleridir; çok sayıda kar kristalinin birikimidir.", "Snowflakes are single ice crystals or clusters of ice crystals that fall from a cloud. / Snowflakes are accumulations of many snow crystals.", S3),
    F(4, "Kar tanelerinin biçimi, kristalin su moleküllerinin önceden belirlenmiş yerlere dizilmesindeki iç düzeni yansıtır; altıgen biçim her zaman korunur.", "reflect the internal order of the crystal's water molecules as they arrange themselves in predetermined spaces / Although the six-sided shape is always maintained", S1),
    F(5, "Kristalin biçimini en çok oluştuğu sıcaklık, daha az ölçüde de havanın nemi belirler; daha az soğukta uzun iğne gibi kristaller, çok daha soğukta çok yassı levha gibi kristaller görülür (kaynakta Fahrenhayt değerleriyle).", "it is the temperature at which a crystal forms — and to a lesser extent the humidity of the air / we see long needle-like crystals at 23 degrees F and very flat plate-like crystals at 5 degrees F.", S1),
    F(6, "Kar tanelerinin her biri gökyüzünden yere biraz farklı yollar izler; bu yüzden prizmalardan iğnelere, tanıdık dantel desenine kadar hepsi benzersiz görünme eğilimindedir.", "individual snowflakes all follow slightly different paths from the sky to the ground / they all tend to look unique, resembling everything from prisms and needles to the familiar lacy pattern.", S1),
    F(7, "Temiz kar görünür güneş ışığının çoğunu yansıtır ve beyaz görünür; aslında yarı saydamdır; kar tanesinin çok sayıdaki yüzü ışığı her yöne saçar.", "Clean snow, however, reflects most of the visible sunlight, creating a white appearance. / Snow appears white, but it is actually translucent. / The many sides of a snowflake scatter light, diffusing the color spectrum in many directions.", S3 + "; " + S4),
    F(8, "Kar, bir evin tavanındaki yalıtıma benzer iyi bir yalıtkandır; bir kar katmanının toplam hacminin çoğu havadır.", "snow is a good insulator, similar to the insulation in the ceiling of a house / most of the total volume of a snow layer is made up of air", S3),
    F(9, "Taze kar sesi bastırır, çünkü ses dalgalarını emer.", "Fresh snow cover dampens sound because it absorbs sound waves.", S4),
    F(10, "Kar tanelerinin çoğu 1,3 santimetreden küçüktür; çok daha büyükleri 5 santimetreye yaklaşabilir.", "Most snowflakes are less than 1.3 centimeters (0.5 inches) across. / nearing 5 centimeters (2 inches) across", S3, ["1.3", "5"]),
    F(11, "Sulu kar, kar taneleri ince bir ılık hava katmanından geçerken yalnızca kısmen eridiğinde oluşur; donan yağmur, kar taneleri daha ılık bir katmanda tamamen erir ve 0°C'deki ya da daha soğuk her şeye değer değmez yeniden donar.", "Sleet occurs when snowflakes only partially melt when they fall through a shallow layer of warm air. / Freezing rain occurs when snowflakes descend into a warmer layer of air and melt completely. / they instantly refreeze upon contact with anything that is at or below 0 degrees C", S2, ["0"]),
    F(12, "Graupel, yuvarlaklaşmış, opak, 2–5 milimetrelik kar taneciklerinden oluşur; bazen doluyla karıştırılır ama dokusu daha yumuşak ve ufalanır.", "Graupel consists of snowflakes that become rounded, opaque pellets ranging from 2 to 5 millimeters / Graupel is sometimes mistaken for hail, but tends to have a texture that is softer and more crumbly.", S3, ["2", "5"]),
    F(13, "Kar, atmosfer sıcaklığı donma noktasında ya da altındayken (0°C) oluşur; karın yağması için sıfırın altında olması gerektiği bir efsanedir.", "Snow forms when the atmospheric temperature is at or below freezing (0°C or 32°F). / It is a myth that it needs to be below zero to snow.", S3 + "; " + S5, ["0"]),
    F(14, "Kar taneleri bulutlardaki minik buz kristallerinin birbirine yapışmasıyla oluşur.", "Snow forms when tiny ice crystals in clouds stick together to become snowflakes.", S5),
    F(15, "Wilson Bentley, hobisi kar tanelerini fotoğraflamak olan bir çiftçiydi.", "Bentley was a farmer whose hobby was photographing snow flakes.", S1),
    F(16, "Küreme kar asla yenmemelidir; içinde kir ve magnezyum klorür gibi kimyasallar vardır; düşük rüzgâr soğuğuna maruz kalmak donmaya ya da hipotermiye yol açabilir.", "never eat plowed snow, which contains snow, dirt, and chemicals like magnesium chloride. / Exposure to low wind chill values can result in frostbite or hypothermia.", S4 + "; " + S3),
]}
e = Ep(); L = e.L
NO = "Noa"
e.sec("hook", [
    L("Gökyüzünden yavaşça süzülen beyaz taneler... Her birinin altı kolu var ve hepsi birbirinden farklı görünüyor!", [4, 6]),
    L("Bir kar tanesi nasıl oluşur? Ve neden hep altı köşelidir?"),
    L("Bugün bir bulutun içinde, buzdan bir sanat eserinin doğuşunu izliyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kar tanesi nasıl oluşur? Biçimini ne belirler? Ve kar neden beyazdır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre her şey bulutun içinde başlar: çok soğuk bir su damlacığı, havadaki bir polen ya da toz parçacığının üzerinde donar.", [1], f"A Be De Ulusal Okyanus ve Atmosfer Dairesi, {NO}'ya göre her şey bulutun içinde başlar: çok soğuk bir su damlacığı, havadaki bir polen ya da toz parçacığının üzerinde donar."),
    L("Yani her kar tanesinin kalbinde minicik bir toz zerresi var. Ben de tozlanırım ama kimse beni kar tanesi sanmaz!"),
    L("Sonra havadaki su buharı bu ilk kristalin üzerinde donar ve yeni kristaller ekler.", [1]),
    L("Sıcaklık 0 derecenin altına düşünce su buharı sıvı olmadan, doğrudan buza dönüşebilir.", [2], "Sıcaklık sıfır derecenin altına düşünce su buharı sıvı olmadan, doğrudan buza dönüşebilir."),
    L("Kar tanesi aslında çok sayıda kar kristalinin bir araya gelmesiyle oluşur.", [3]),
    L("Neden altı köşeli? NOAA'ya göre bu biçim, su moleküllerinin kristalin içinde belirli yerlere dizilmesinden gelir. Bu yüzden altıgen yapı her zaman korunur.", [4], f"Neden altı köşeli? {NO}'ya göre bu biçim, su moleküllerinin kristalin içinde belirli yerlere dizilmesinden gelir. Bu yüzden altıgen yapı her zaman korunur."),
])
e.sec("finding", [
    L("Peki biçimini ne belirler? En çok, kristalin oluştuğu sıcaklık; biraz da havanın nemi.", [5]),
    L("Örneğin hava donma noktasının biraz altındayken uzun iğneler, çok daha soğukken ise çok yassı levhalar oluşur.", [5]),
    L("Her kar tanesi yere inerken biraz farklı bir yoldan geçer. Farklı sıcaklıklar, farklı nem... Bu yüzden her biri benzersiz görünme eğilimindedir.", [6]),
    L("Prizmalar, iğneler ve o tanıdık dantel desenleri hep bu yolculuğun sonucu.", [6]),
    L("Kar tanelerinin çoğu 1,3 santimetreden küçüktür. Çok daha büyükleri 5 santimetreye yaklaşabilir.", [10], "Kar tanelerinin çoğu bir virgül üç santimetreden küçüktür. Çok daha büyükleri beş santimetreye yaklaşabilir."),
    L("Kar yağması için hava ne kadar soğuk olmalı? Ulusal Kar ve Buz Veri Merkezi NSIDC'ye göre kar, sıcaklık 0 derecede ya da altındayken oluşur.", [13], "Kar yağması için hava ne kadar soğuk olmalı? Ulusal Kar ve Buz Veri Merkezi, En Es Ay Di Si'ye göre kar, sıcaklık sıfır derecede ya da altındayken oluşur."),
    L("Hatta İngiltere Meteoroloji Ofisi'ne göre yerde sıcaklığın sıfırın altında olması gerektiği bir efsanedir.", [13]),
])
e.sec("importance", [
    L("Kar neden beyazdır? Aslında kar yarı saydamdır! Ama kar tanesinin sayısız yüzü ışığı her yöne saçar ve bize beyaz görünür.", [7]),
    L("Kar, iyi bir yalıtkandır; tıpkı evlerin tavanındaki yalıtım gibi. Çünkü bir kar katmanının büyük kısmı havadır.", [8]),
    L("Benim de yalıtımım var. Kablolarımın çevresinde, kardan değil plastikten!"),
    L("Karlı bir günde dışarısı neden sessizdir? Taze kar, ses dalgalarını emer.", [9]),
    L("Kışın gökten başka şeyler de düşer. Kar taneleri ılık bir hava katmanından geçerken kısmen eriyip yeniden donarsa sulu kar olur.", [11]),
    L("Tamamen erir ve yerdeki soğuk yüzeylere değer değmez donarsa buna donan yağmur denir.", [11]),
    L("Bir de graupel var: yuvarlaklaşmış, 2–5 milimetrelik kar tanecikleri. Doluya benzer ama daha yumuşaktır ve kolay ufalanır.", [12], "Bir de graupel var: yuvarlaklaşmış, iki ile beş milimetrelik kar tanecikleri. Doluya benzer ama daha yumuşaktır ve kolay ufalanır."),
    L("Şimdi sıra sende! Karlı bir günde koyu renkli bir kumaşı birkaç dakika dondurucuda soğut, sonra dışarı çıkıp üstüne düşen kar tanelerine büyüteçle bak."),
    L("Kaç köşe sayıyorsun? İğne mi, levha mı, dantel mi? Gördüklerini çiz."),
    L("Unutma: sıkı giyin, çok soğukta uzun süre kalma. Ve yol kenarındaki karı asla yeme; içinde kir ve kimyasallar olabilir.", [16]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Wilson Bentley adında bir çiftçinin hobisi, kar tanelerini fotoğraflamaktı.", [15]),
    L("Hızlı soru! Kar taneleri kaç köşelidir?", [4]),
    L("Düşün bakalım... Evet: altı!", [4]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de antenimdeki karı silkeleyip gidiyorum!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kar taneleri nasıl oluşur?", "emoji": "❄️"}, ["☃️", "🌨️", "🧣", "⛄"], ["", "NEDEN ALTI KÖŞE?", "BULUTUN İÇİNE!"], fx="sparkle")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kar tanesi nasıl oluşur?", "Biçimini ne belirler?", "Kar neden beyazdır?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "diagram", "title": "Bir kar tanesi doğuyor", "layout": "flow", "nodes": [{"label": "Polen ya da toz", "emoji": "🟤"}, {"label": "Çok soğuk damlacık donar", "emoji": "💧"}, {"label": "İlk kristal", "emoji": "❄️"}]}, ["☁️", "🤖"], ["TOZ ZERRESİ", "TOZLU MUMA 😅"])
S(3, {"type": "meter", "title": "Kristal büyüyor", "label": "Kristal", "emoji": "❄️", "phases": [{"label": "Su buharı üzerinde donar", "level": 0.4, "emoji": "♨️"}, {"label": "0°C altı: buhar doğrudan buza", "level": 0.7, "emoji": "🧊"}, {"label": "Çok sayıda kristal: kar tanesi", "level": 0.95, "emoji": "❄️"}], "note": NOTE}, ["☁️", "🌨️"], ["YENİ KRİSTALLER", "BUHAR → BUZ", "KAR TANESİ ❄️"])
S(1, {"type": "spotlight", "title": "Neden altı köşe?", "emoji": "❄️", "chips": [{"label": "Su molekülleri belirli yerlere dizilir", "emoji": "💧"}, {"label": "Altıgen yapı hep korunur", "emoji": "⬡"}]}, ["🔬", "✨"], ["ALTIGEN ⬡"])
S(2, {"type": "comparison", "title": "Biçimi sıcaklık belirler", "left": {"title": "Az soğuk 🌡️", "items": ["Uzun iğneler"]}, "right": {"title": "Çok soğuk 🥶", "items": ["Yassı levhalar"]}}, ["🌡️", "💧"], ["SICAKLIK + NEM", "İĞNE / LEVHA"])
S(2, {"type": "diagram", "title": "Benzersiz yolculuk", "layout": "flow", "nodes": [{"label": "Bulut", "emoji": "☁️"}, {"label": "Farklı sıcaklık", "emoji": "🌡️"}, {"label": "Farklı nem", "emoji": "💧"}, {"label": "Benzersiz desen", "emoji": "❄️"}]}, ["✨", "🎨"], ["FARKLI YOL", "PRİZMA • İĞNE • DANTEL"])
S(1, {"type": "big-number", "value": "1,3", "unit": "cm", "label": "Çoğu kar tanesi bundan küçük", "sub": "Büyükleri 5 santimetreye yaklaşabilir", "icon": "📏"}, ["❄️", "🔍"], ["KÜÇÜCÜK!"])
S(2, {"type": "spotlight", "title": "Ne kadar soğuk?", "emoji": "🌡️", "chips": [{"label": "0°C ya da altı", "emoji": "❄️"}, {"label": "'Sıfırın altı şart' bir efsane", "emoji": "❌"}]}, ["⛄", "🧤"], ["SIFIR DERECE", "EFSANE ❌"])
S(2, {"type": "comparison", "title": "Kar neden beyaz?", "left": {"title": "Aslında ❄️", "items": ["Yarı saydam"]}, "right": {"title": "Ama 🌈", "items": ["Sayısız yüz ışığı her yöne saçar", "Beyaz görünür"]}}, ["☀️", "✨"], ["IŞIK SAÇILIR", "KAR = YALITIM 🏠"], fx="sparkle", extra=[8])
S(2, {"type": "spotlight", "title": "Sessiz kar", "emoji": "🤫", "chips": [{"label": "Kar katmanı çoğunlukla hava", "emoji": "💨"}, {"label": "Taze kar sesi emer", "emoji": "🔇"}, {"label": "Muma: plastik yalıtım!", "emoji": "🔌"}]}, ["❄️", "🏔️"], ["PLASTİK YALITIM 🔌", "SESSİZLİK 🤫"], extra=[8])
S(3, {"type": "stages", "title": "Kışın gökten düşenler", "rows": [{"label": "Kar", "emoji": "❄️"}, {"label": "Sulu kar: kısmen erir", "emoji": "🌨️"}, {"label": "Donan yağmur: tamamen erir", "emoji": "🧊"}, {"label": "Graupel: 2–5 mm tanecik", "emoji": "⚪"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 0, "note": "Şematik çizim."}, [], ["SULU KAR", "DONAN YAĞMUR", "GRAUPEL"])
S(2, {"type": "diagram", "title": "Sen de dene: kar tanesi avı", "layout": "flow", "nodes": [{"label": "Koyu kumaşı soğut", "emoji": "🧣"}, {"label": "Kar tanelerini yakala", "emoji": "❄️"}, {"label": "Büyüteçle bak", "emoji": "🔍"}, {"label": "Köşeleri say, çiz", "emoji": "✏️"}]}, ["📓", "🧤"], ["DENEY ZAMANI 🔬", "KÖŞELERİ SAY"])
S(1, {"type": "bullets", "title": "Güvenlik", "items": ["Sıkı giyin, soğukta uzun kalma", "Yol kenarındaki karı asla yeme"], "tone": "caution"}, ["⚠️", "🧥"], ["GÜVENLİK ⚠️"])
S(1, {"type": "spotlight", "title": "Wilson Bentley", "emoji": "📷", "chips": [{"label": "Bir çiftçi", "emoji": "🧑‍🌾"}, {"label": "Hobisi: kar tanelerini fotoğraflamak", "emoji": "❄️"}]}, ["📸", "❄️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Kar taneleri kaç köşelidir?", "emoji": "🤔"}, ["❄️", "⬡"], ["HIZLI SORU!", "ALTI ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 22, "videoTitle": "Kar taneleri nasıl oluşur?", "paperTitleTr": "Kar taneleri nasıl oluşur?",
  "theme": {"backdrop": "snow", "actors": [{"kind": "walk", "emoji": "🦊", "every": 19, "size": 96}, {"kind": "hop", "emoji": "🐇", "size": 80}, {"kind": "fly", "emoji": "🐦", "every": 25}]},
  "takeaways": ["Kar tanesi bir toz zerresi çevresinde donan su ile başlar", "Biçimi sıcaklık ve nem belirler; altıgen yapı hep korunur", "Kar ışığı saçtığı için beyaz görünür, sesi emer ve yalıtır"],
  "description": "Gökten düşen kar taneleri nasıl oluşur, neden hep altı köşelidir? Bu bölümde bulutun içinde bir toz zerresi çevresinde başlayan kristal büyümesini, sıcaklık ve nemin kar tanesinin biçimini nasıl belirlediğini; karın neden beyaz göründüğünü, neden sessiz olduğunu ve nasıl yalıttığını; sulu kar, donan yağmur ve graupeli keşfediyoruz. Sonunda kar tanesi avı etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kristal", "meaning": "Molekülleri düzenli bir desenle dizilmiş katı madde."},
    {"term": "Su buharı", "meaning": "Suyun gaz hâli."},
    {"term": "Altıgen", "meaning": "Altı kenarı ve altı köşesi olan şekil."},
    {"term": "Nem", "meaning": "Havadaki su buharı miktarı."},
    {"term": "Yarı saydam", "meaning": "Işığın bir kısmını geçiren madde."},
    {"term": "Yalıtkan", "meaning": "Isıyı ya da elektriği kolay geçirmeyen madde."},
    {"term": "Sulu kar", "meaning": "Kısmen eriyip yeniden donan kar."},
    {"term": "Graupel", "meaning": "Yuvarlaklaşmış, yumuşak kar tanecikleri."}],
  "song": e.song("Buzdan Yıldızlar", [("❄️", "Kar tanesi"), ("☁️", "Bulut"), ("🌡️", "Sıcaklık"), ("⛄", "Kardan adam"), ("🔍", "Büyüteç")],
    ["Bulutta bir toz zerresi bekler", "Soğuk bir damla üstünde donar", "Buhar donar, kristal büyür", "Altı köşeli bir yıldız olur"],
    ["Kar tanesi, kar tanesi, süzül yere!", "Sıcaklık çizer her desenini", "İğne, levha, dantel gibi", "Hepsi kendi yolundan iner"],
    ["Işığı saçar, beyaz görünür", "Havayla dolu, sıcak tutar", "Sesleri emer, dünya susar", "Sulu kar, graupel de yağar"],
    ["Kar tanesi, kar tanesi, süzül yere!", "Sıcaklık çizer her desenini", "Büyüteci al, köşeleri say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "⛄"}, {"kind": "hop", "emoji": "❄️"}, {"kind": "hop", "emoji": "☃️"}, {"kind": "chase", "emoji": "🦊", "emoji2": "🐇", "every": 8, "size": 220}, {"kind": "swarm", "emoji": "❄️"}])}
e.write(D, facts, script)
