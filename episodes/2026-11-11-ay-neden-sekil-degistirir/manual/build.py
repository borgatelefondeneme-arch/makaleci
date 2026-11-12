"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:ay-neden-sekil-degistirir"
S1 = "NASA Science — Moon Phases"; S2 = "NASA Space Place — What Are the Moon's Phases?"; S3 = "NASA Science — Moon Facts"; S4 = "NASA Science — Tidal Locking"; S6 = "NASA Science — The Moon & Eclipses"; S7 = "NASA Science — Tides"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Moon Phases", "publisher": "NASA", "url": "https://science.nasa.gov/moon/moon-phases/"},
    {"id": "k2", "title": "What Are the Moon's Phases?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/moon-phases/en/"},
    {"id": "k3", "title": "Moon Facts", "publisher": "NASA", "url": "https://science.nasa.gov/moon/facts/"},
    {"id": "k4", "title": "Tidal Locking", "publisher": "NASA", "url": "https://science.nasa.gov/moon/tidal-locking/"},
    {"id": "k5", "title": "The Moon & Eclipses", "publisher": "NASA", "url": "https://science.nasa.gov/moon/eclipses/"},
    {"id": "k6", "title": "Tides", "publisher": "NASA", "url": "https://science.nasa.gov/moon/tides/"}],
  "facts": [
    F(1, "Ay kendi ışığını üretmez; 'ay ışığı' aslında yansıyan Güneş ışığıdır.", "The Moon does not make its own light. \"Moonlight\" is actually reflected sunlight.", S1),
    F(2, "Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.", "The Moon is always half-lit by the Sun.", S1),
    F(3, "Ay Dünya'nın çevresinde dolandıkça farklı kısımları farklı zamanlarda Güneş ışığında ya da karanlıkta olur; bizim bakış açımızdan Ay'ın evrelerden geçmesinin nedeni budur. Ay'ın biçimi ay boyunca değişmez; değişen bizim görüşümüzdür.", "As the Moon orbits Earth, different parts are in sunlight or darkness at different times. / The changing illumination is why, from our perspective, the Moon goes through phases. / The shape of the Moon isn't changing throughout the month. However, our view of the Moon does change.", S3 + "; " + S2),
    F(4, "Sekiz evre sırayla: yeni ay, büyüyen hilal, ilk dördün, büyüyen şişkin ay, dolunay, küçülen şişkin ay, son dördün, küçülen hilal. Şişkin ay evresi yarım ay ile dolunay arasındadır.", "The eight lunar phases are, in order: new Moon, waxing crescent, first quarter, waxing gibbous, full Moon, waning gibbous, third quarter, and waning crescent. / Waxing means it is getting bigger. / Waning means it is getting smaller. / The waxing gibbous phase is between a half moon and full moon.", S1 + "; " + S2),
    F(5, "Ay'ın Dünya çevresindeki bir turu yaklaşık 27,3 gün sürer; bir yeni aydan ötekine ise yaklaşık 29,5 gün geçer.", "It takes about 27.3 days for the Moon to orbit Earth. / it takes about 29.5 days to go from one new moon to the next new moon.", S2, ["27.3", "29.5"]),
    F(6, "Fark, Dünya'nın da hareket etmesinden (Güneş'in çevresinde dolanmasından) kaynaklanır.", "Because Earth is moving as well – rotating on its axis as it orbits the Sun –", S3),
    F(7, "Ay bize sırtını hiç dönmez; eşinin çevresinde dönerken hep ona bakan bir dansçı gibidir.", "As a result, the Moon never turns its back to us, like a dancer circling ― but always facing ― its partner.", S4),
    F(8, "Dünya'dan hiç görmediğimiz yarıküreye (uzak yüz) 'karanlık yüz' denmesi yanıltıcıdır.", "Some people call the far side – the hemisphere we never see from Earth – the \"dark side\", but that's misleading.", S3),
    F(9, "Ay ortalama 384.400 kilometre uzaklıktadır.", "The Moon is an average of 238,855 miles (384,400 kilometers) away.", S3, ["384.400"]),
    F(10, "Ay'ın genişliği Dünya'nınkinin üçte birinden azdır.", "the Moon is less than a third of the width of Earth.", S3),
    F(11, "Ay büyük olasılıkla, birkaç milyar yıl önce Mars büyüklüğünde bir cismin Dünya'ya çarpmasından sonra oluştu.", "The Moon likely formed after a Mars-sized body collided with Earth several billion years ago.", S3),
    F(12, "Ay yılda yaklaşık 3,8 santimetre hızla yavaşça uzaklaşmaktadır.", "has been slowly drifting outward at the rate of about 1.5 inches (3.8 cm) per year.", S6, ["3.8"]),
    F(13, "Ay tutulmaları dolunay evresinde olur: Dünya tam olarak Ay ile Güneş arasına girince gölgesi Ay'ın yüzeyine düşer. Güneş tutulmaları yalnızca yeni ay evresinde, Ay Dünya ile Güneş arasındayken olur. Ay'ın yörüngesi Dünya'nın yörünge düzlemine göre yaklaşık 5 derece eğiktir.", "Lunar eclipses occur at the full Moon phase. / When Earth is positioned precisely between the Moon and Sun, Earth's shadow falls upon the surface of the Moon / Solar eclipses happen only at the new Moon phase, when the Moon is between Earth and the Sun. / The Moon's orbit is tilted about 5 degrees compared to the plane of Earth's orbit around the Sun.", S6, ["5"]),
    F(14, "Ay'ın kütle çekimi Dünya'daki gelgitlere yol açar; okyanuslar kabarır.", "The Moon's gravity drives Earth's tides / On Earth, the Moon's gravitational pull causes the oceans to bulge out on both the side closest to the Moon", S7),
    F(15, "Ay gündüz de sık sık soluk biçimde görülebilir; her gün biraz daha geç doğar; dolunay gün batımı sıralarında doğar.", "it's often visible during the day as a faint, pale presence. / Every day, the Moon rises a little bit later. / A full Moon rises around sunset and sets around sunrise.", S1),
    F(16, "Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.", "In our entire solar system, the only object that shines with its own light is the Sun.", S1),
]}
e = Ep(); L = e.L
e.sec("hook", [
    L("Bir gece gökyüzünde incecik bir hilal görürsün. Günler sonra aynı gökyüzünde kocaman, yusyuvarlak bir Ay!"),
    L("Ay gerçekten biçim mi değiştiriyor? Yoksa bizi yanıltan başka bir şey mi var?"),
    L("Bugün Ay'ın çevresinde bir tur atıyoruz!"),
])
e.sec("context", [
    L("Ay'a kadar uçmayı çok isterdim. Ama şarjım yarı yolda biter!"),
    L("Üç sorumuz var. Ay nasıl parlar? Neden her gece farklı görünür? Ve bize neden hep aynı yüzünü gösterir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre Ay kendi ışığını üretmez. Ay ışığı dediğimiz şey, aslında Ay'dan yansıyan Güneş ışığıdır.", [1], "Nasa'ya göre Ay kendi ışığını üretmez. Ay ışığı dediğimiz şey, aslında Ay'dan yansıyan Güneş ışığıdır."),
    L("Güneş sistemimizde kendi ışığıyla parlayan tek cisim Güneş'tir.", [16]),
    L("Ben ise kendi ışığımı üretirim. Gözlerim LED!", [], "Ben ise kendi ışığımı üretirim. Gözlerim led!"),
    L("İşin püf noktası şu: Ay'ın yarısı her zaman Güneş tarafından aydınlatılır.", [2]),
    L("Ay'ın biçimi ay boyunca hiç değişmez. Değişen, bizim ona bakış açımızdır.", [3]),
    L("Ay, Dünya'nın çevresinde bir yörüngede dolanır. Dolandıkça aydınlık yarısının bazen tamamını, bazen bir kısmını görürüz; bazen de hiç göremeyiz.", [3]),
    L("Bu farklı görünümlere Ay'ın evreleri denir.", [3, 4]),
    L("Peki Dünya'nın gölgesi? Evrelerin nedeni o değildir. Dünya'nın gölgesi Ay'a yalnızca Ay tutulmasında düşer.", [3, 13]),
])
e.sec("finding", [
    L("Sekiz evre var. İlki yeni ay: Ay, Dünya ile Güneş arasındadır ve aydınlık yüzü bize dönük değildir.", [4, 13]),
    L("Sonra incecik bir hilal belirir ve gece gece büyür.", [4]),
    L("Ardından ilk dördün gelir: Ay'ı yarım daire gibi görürüz.", [4]),
    L("Sonra şişkin ay: yarım ay ile dolunay arasındaki evre.", [4]),
    L("Ve dolunay! Aydınlık yüzün tamamı bize dönüktür.", [4]),
    L("Sonra her şey tersine döner: şişkin ay, son dördün, küçülen hilal ve yeniden yeni ay.", [4]),
    L("Bir yeni aydan ötekine kadar yaklaşık 29,5 gün geçer.", [5], "Bir yeni aydan ötekine kadar yaklaşık yirmi dokuz buçuk gün geçer."),
    L("İlginç olan şu: Ay, Dünya'nın çevresindeki bir turunu yaklaşık 27,3 günde tamamlar. Aradaki fark, Dünya'nın da bu sırada Güneş'in çevresinde ilerlemesinden kaynaklanır.", [5, 6], "İlginç olan şu: Ay, Dünya'nın çevresindeki bir turunu yaklaşık yirmi yedi virgül üç günde tamamlar. Aradaki fark, Dünya'nın da bu sırada Güneş'in çevresinde ilerlemesinden kaynaklanır."),
    L("Bir ipucu daha: dolunay, Güneş batarken doğar. Ay her gün biraz daha geç doğar ve gündüz gökyüzünde bile sık sık görülebilir.", [15]),
])
e.sec("importance", [
    L("Ay bize hep aynı yüzünü gösterir. NASA bunu, eşinin çevresinde dönerken yüzünü hep ona çeviren bir dansçıya benzetiyor.", [7], "Ay bize hep aynı yüzünü gösterir. Nasa bunu, eşinin çevresinde dönerken yüzünü hep ona çeviren bir dansçıya benzetiyor."),
    L("Ben de fotoğraflarda hep iyi tarafımı dönerim. Ay'dan öğrendim!"),
    L("Göremediğimiz yüze karanlık yüz denmesi ise yanıltıcıdır. Doğru adı uzak yüzdür; çünkü Ay'ın yarısı her zaman aydınlıktır.", [8, 2]),
    L("Ay tutulması dolunayda olur: Dünya tam olarak Güneş ile Ay'ın arasına girer ve gölgesi Ay'ın üstüne düşer.", [13]),
    L("Peki neden her dolunayda tutulma olmaz? Çünkü Ay'ın yörüngesi, Dünya'nın yörüngesine göre yaklaşık 5 derece eğiktir.", [13], "Peki neden her dolunayda tutulma olmaz? Çünkü Ay'ın yörüngesi, Dünya'nın yörüngesine göre yaklaşık beş derece eğiktir."),
    L("Ay yalnızca gökyüzünü süslemez. Kütle çekimi okyanusları kabartır: gelgitlerin nedeni budur.", [14]),
    L("Biraz da sayı: Ay bize ortalama 384.400 kilometre uzaklıktadır ve genişliği Dünya'nınkinin üçte birinden azdır.", [9, 10], "Biraz da sayı: Ay bize ortalama üç yüz seksen dört bin dört yüz kilometre uzaklıktadır ve genişliği Dünya'nınkinin üçte birinden azdır."),
    L("Nasıl oluştu? NASA'ya göre büyük olasılıkla, milyarlarca yıl önce Mars büyüklüğünde bir gök cismi Dünya'ya çarptıktan sonra.", [11], "Nasıl oluştu? Nasa'ya göre büyük olasılıkla, milyarlarca yıl önce Mars büyüklüğünde bir gök cismi Dünya'ya çarptıktan sonra."),
    L("Şimdi sıra sende! Karanlık bir odada masa lambasını yak: o Güneş olsun. Elindeki top Ay, sen de Dünya'sın."),
    L("Topu kolunu uzatarak tut ve olduğun yerde yavaşça dön. Topun aydınlık kısmının nasıl değiştiğine bak: hilal, dördün, dolunay!", [3]),
    L("İkinci görev: bir ay boyunca her akşam Ay'ı çiz. Böylece kendi Ay günlüğün olur."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Ay bizden yavaş yavaş uzaklaşıyor: yılda yaklaşık 3,8 santimetre.", [12], "Bunu biliyor muydun? Ay bizden yavaş yavaş uzaklaşıyor: yılda yaklaşık üç virgül sekiz santimetre."),
    L("Alınma, kişisel bir şey değil!"),
    L("Hızlı soru! Ay kendi ışığını üretir mi?", [1]),
    L("Düşün bakalım... Hayır! Güneş'in ışığını yansıtır.", [1]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de gözlerimi parlatmaya gidiyorum; bu gece dolunayla yarışacağım!"),
])
S = e.S
S(3, {"type": "hook", "question": "Ay gerçekten biçim mi değiştiriyor?", "emoji": "🌙"}, ["🌒", "🌕", "⭐", "🔭"], ["", "BİÇİM Mİ DEĞİŞİYOR?", "AY'IN ÇEVRESİNDE TUR!"])
S(1, {"type": "spotlight", "title": "Ay yolculuğu", "emoji": "🚀", "chips": [{"label": "Çok isterdim", "emoji": "🤖"}, {"label": "Şarj: yarı yolda biter", "emoji": "🪫"}, {"label": "Buradan anlatayım!", "emoji": "📣"}]}, ["🌙", "🔋"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Ay nasıl parlar?", "Neden her gece farklı görünür?", "Bize neden hep aynı yüzünü gösterir?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "diagram", "title": "Ay nasıl parlar?", "layout": "flow", "nodes": [{"label": "Güneş ışık üretir", "emoji": "☀️"}, {"label": "Işık Ay'a çarpar", "emoji": "🌕"}, {"label": "Yansır, bize ulaşır", "emoji": "👀"}, {"label": "Muma: LED gözler!", "emoji": "🤖"}]}, ["💡", "✨"], ["YANSIYAN IŞIK", "TEK IŞIK KAYNAĞI: GÜNEŞ", "LED 💡"])
S(2, {"type": "comparison", "title": "Ay'ın iki yarısı", "left": {"title": "Aydınlık yarı ☀️", "items": ["Güneş'e dönük", "Her zaman aydınlık"]}, "right": {"title": "Karanlık yarı 🌑", "items": ["Güneş'e arkası dönük"]}}, ["🌗", "☀️"], ["YARISI HEP AYDINLIK", "BİÇİM DEĞİŞMEZ!"])
S(3, {"type": "spotlight", "title": "Evreler neden olur?", "emoji": "🌍", "chips": [{"label": "Ay, Dünya'nın çevresinde dolanır", "emoji": "🔄"}, {"label": "Aydınlık yarının farklı kısmını görürüz", "emoji": "👀"}, {"label": "Bunlar Ay'ın evreleri", "emoji": "🌓"}, {"label": "Dünya'nın gölgesi değil!", "emoji": "🚫"}]}, ["🌙", "☀️"], ["YÖRÜNGE 🔄", "EVRELER", "GÖLGE DEĞİL! 🚫"])
S(3, {"type": "diagram", "title": "Büyüyen Ay", "layout": "flow", "nodes": [{"label": "Yeni ay", "emoji": "🌑"}, {"label": "Büyüyen hilal", "emoji": "🌒"}, {"label": "İlk dördün", "emoji": "🌓"}]}, ["⭐", "🔭"], ["YENİ AY 🌑", "HİLAL 🌒", "İLK DÖRDÜN 🌓"])
S(2, {"type": "spotlight", "title": "Dolunaya doğru", "emoji": "🌕", "chips": [{"label": "Şişkin ay: yarım ile dolunay arası", "emoji": "🌔"}, {"label": "Dolunay: aydınlık yüz bize dönük", "emoji": "🌕"}]}, ["🐺", "✨"], ["ŞİŞKİN AY 🌔", "DOLUNAY! 🌕"])
S(2, {"type": "stages", "title": "Bir ay boyunca görünen aydınlık kısım", "rows": [{"label": "Dolunay", "emoji": "🌕"}, {"label": "Şişkin ay", "emoji": "🌔"}, {"label": "Dördün", "emoji": "🌓"}, {"label": "Hilal", "emoji": "🌒"}, {"label": "Yeni ay", "emoji": "🌑"}], "path": [4, 3, 2, 1, 0, 1, 2, 3, 4], "highlightRow": 0, "note": "Şematik çizim: bir yeni aydan ötekine yaklaşık 29,5 gün."}, [], ["TERSİNE DÖNER 🔄", "29,5 GÜN"])
S(1, {"type": "comparison", "title": "İki farklı süre", "left": {"title": "27,3 gün", "items": ["Ay'ın Dünya çevresindeki bir turu"]}, "right": {"title": "29,5 gün", "items": ["Yeni aydan yeni aya", "Dünya da Güneş çevresinde ilerler"]}}, ["🗓️", "🌍"], ["NEDEN FARKLI?"])
S(1, {"type": "bullets", "title": "Gökyüzü ipuçları", "items": ["Dolunay, Güneş batarken doğar", "Ay her gün biraz daha geç doğar", "Gündüz de sık sık görülür"]}, ["🌅", "🔭"], ["GÜNDÜZ AY'I 🌤️"])
S(2, {"type": "spotlight", "title": "Hep aynı yüz", "emoji": "💃", "chips": [{"label": "Ay bize sırtını hiç dönmez", "emoji": "🌕"}, {"label": "Eşine hep yüzünü dönen dansçı gibi", "emoji": "🕺"}, {"label": "Muma: hep iyi tarafım!", "emoji": "📸"}]}, ["🌍", "🎶"], ["DANSÇI GİBİ 💃", "İYİ TARAFIM 📸"])
S(1, {"type": "comparison", "title": "Karanlık yüz mü?", "left": {"title": "Yanıltıcı ❌", "items": ["Karanlık yüz"]}, "right": {"title": "Doğrusu ✅", "items": ["Uzak yüz", "Ay'ın yarısı hep aydınlık"]}}, ["🌗", "🛰️"], ["UZAK YÜZ"])
S(2, {"type": "diagram", "title": "Ay tutulması", "layout": "flow", "nodes": [{"label": "Güneş", "emoji": "☀️"}, {"label": "Dünya araya girer", "emoji": "🌍"}, {"label": "Gölgesi Ay'a düşer", "emoji": "🌑"}, {"label": "Yörünge yaklaşık 5° eğik: her ay olmaz", "emoji": "📐"}]}, ["🌕", "🔭"], ["AY TUTULMASI", "EĞİK YÖRÜNGE 📐"])
S(1, {"type": "spotlight", "title": "Gelgit", "emoji": "🌊", "chips": [{"label": "Ay'ın kütle çekimi", "emoji": "🧲"}, {"label": "Okyanuslar kabarır", "emoji": "🌊"}]}, ["🌙", "🏖️"], ["GELGİT 🌊"])
S(1, {"type": "big-number", "value": "384.400", "unit": "km", "label": "Ay'ın ortalama uzaklığı", "sub": "Genişliği Dünya'nınkinin üçte birinden az", "icon": "📏"}, ["🌍", "🌙"], ["ÇOK UZAK!"])
S(1, {"type": "diagram", "title": "Ay nasıl oluştu? (büyük olasılıkla)", "layout": "flow", "nodes": [{"label": "Mars büyüklüğünde bir cisim", "emoji": "☄️"}, {"label": "Dünya'ya çarptı", "emoji": "💥"}, {"label": "Ay oluştu", "emoji": "🌕"}]}, ["🌍", "✨"], ["DEV ÇARPIŞMA 💥"])
S(3, {"type": "bullets", "title": "Sen de dene: odanda Ay evreleri 🔬", "items": ["Lamba = Güneş, top = Ay, sen = Dünya", "Topu kolunla uzat, yavaşça dön", "Aydınlık kısım nasıl değişiyor?", "Bir ay boyunca Ay günlüğü tut"]}, ["💡", "⚽", "📓"], ["DENEY ZAMANI 🔬", "YAVAŞÇA DÖN 🔄", "AY GÜNLÜĞÜ 📓"])
S(2, {"type": "big-number", "value": "3,8", "unit": "cm", "label": "Ay her yıl bu kadar uzaklaşıyor", "sub": "NASA", "icon": "👋"}, ["🌙", "📏"], ["BUNU BİLİYOR MUYDUN?", "KİŞİSEL DEĞİL 😄"])
S(2, {"type": "hook", "question": "Ay kendi ışığını üretir mi?", "emoji": "🤔"}, ["🌙", "☀️"], ["HIZLI SORU!", "HAYIR: YANSITIR ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 8, "videoTitle": "Ay neden şekil değiştirir?", "paperTitleTr": "Ay neden şekil değiştirir?",
  "takeaways": ["Ay kendi ışığını üretmez; Güneş ışığını yansıtır", "Evreler, aydınlık yarının ne kadarını gördüğümüze bağlıdır", "Ay bize hep aynı yüzünü gösterir; uzak yüz karanlık değildir"],
  "description": "Ay gerçekten biçim mi değiştiriyor? Bu bölümde Ay'ın nasıl parladığını, yörüngesini ve sekiz evresini; yeni aydan dolunaya neler olduğunu, bir evre döngüsünün neden 29,5 gün sürdüğünü keşfediyoruz. Ay bize neden hep aynı yüzünü gösterir, Ay tutulması nasıl olur, gelgitlerle Ay'ın ilgisi nedir? Sonunda lamba ve topla Ay evreleri deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Yörünge", "meaning": "Bir gök cisminin başka bir gök cisminin çevresinde izlediği yol."},
    {"term": "Evre", "meaning": "Ay'ın Dünya'dan görünen aydınlık kısmının aldığı biçimlerden her biri."},
    {"term": "Hilal", "meaning": "Ay'ın ince, yay biçiminde göründüğü evre."},
    {"term": "Dördün", "meaning": "Ay'ın yarım daire biçiminde göründüğü evre."},
    {"term": "Şişkin ay", "meaning": "Yarım ay ile dolunay arasındaki evre."},
    {"term": "Ay tutulması", "meaning": "Dünya'nın gölgesinin Ay'ın üstüne düşmesi."},
    {"term": "Kütle çekimi", "meaning": "Kütlesi olan cisimlerin birbirini çekmesi."},
    {"term": "Gelgit", "meaning": "Deniz seviyesinin gün içinde düzenli olarak yükselip alçalması."}],
  "song": e.song("Ay'ın Sekiz Yüzü", [("🌑", "Yeni ay"), ("🌒", "Hilal"), ("🌓", "Dördün"), ("🌕", "Dolunay"), ("🌍", "Dünya")],
    ["Ay kendi ışığını üretmez, bil", "Güneş'ten gelen ışığı yansıtır", "Yarısı her zaman aydınlıktır", "Değişen bizim bakış açımız"],
    ["Yeni ay, hilal, dördün, dolunay!", "Dünya'nın çevresinde döner Ay", "Biçimi aynı, görünen değişir", "Yirmi dokuz buçuk gün, baştan gelir"],
    ["Hep aynı yüzünü bize çevirir", "Uzak yüz de Güneş'i görür", "Dolunayda gölge düşerse tutulur", "Çekimiyle denizler kabarır durur"],
    ["Yeni ay, hilal, dördün, dolunay!", "Dünya'nın çevresinde döner Ay", "Lambayı yak, topu al, sen de dene", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
