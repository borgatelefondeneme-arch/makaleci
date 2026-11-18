"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:gunes-nasil-parlar"
NS = "NASA Science — Sun: Facts"; SA = "NASA Space Place — All About the Sun"; SH = "NASA Space Place — Where Does the Sun's Energy Come From?"; SS = "NASA Science — Sunspots"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Sun: Facts", "publisher": "NASA", "url": "https://science.nasa.gov/sun/facts/"},
    {"id": "k2", "title": "All About the Sun", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/all-about-the-sun/en/"},
    {"id": "k3", "title": "Where Does the Sun's Energy Come From?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/sun-heat/en/"},
    {"id": "k4", "title": "Sunspots", "publisher": "NASA", "url": "https://science.nasa.gov/sun/sunspots/"}],
  "facts": [
    F(1, "Yıldız, sıcak ve parlayan bir gaz topudur.", "A star is a hot, glowing ball of gas.", SA),
    F(2, "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.", "The Sun is a huge ball of hydrogen and helium held together by its own gravity.", NS),
    F(3, "Çekirdekteki nükleer tepkimelerde hidrojen kaynaşarak helyuma dönüşür ve bu, Güneş'in ısısına ve ışığına güç verir; hidrojen atomları öyle bir kuvvetle çarpışır ki kelimenin tam anlamıyla kaynaşıp yeni bir element olan helyuma dönüşür.", "Nuclear reactions here – where hydrogen is fused to form helium – power the Sun's heat and light. / the hydrogen atoms collide with enough force that they literally meld into a new element—helium.", NS + "; " + SH),
    F(4, "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir.", "The temperature in the Sun's core is about 27 million degrees Fahrenheit (15 million degrees Celsius)", NS, ["15"]),
    F(5, "Güneş'in iç bölgeleri çekirdek, ışınım bölgesi ve konveksiyon bölgesidir; enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık 170.000 yıl sürer.", "The interior regions include the core, the radiative zone, and the convection zone. / taking about 170,000 years to get from the core to the top of the convection zone.", NS, ["170.000"]),
    F(6, "Konveksiyon bölgesinde büyük sıcak plazma kabarcıkları fotosfere doğru yükselir.", "large bubbles of hot plasma (a soup of ionized atoms) move upward toward the photosphere", NS),
    F(7, "Güneş'in yüzeyi denen bölüm fotosferdir; sıcaklığı yaklaşık 5.500 santigrat dereceye ulaşır.", "The part of the Sun commonly called its surface is the photosphere. / with temperatures reaching about 10,000 degrees Fahrenheit (5,500 degrees Celsius)", NS, ["5.500"]),
    F(8, "Güneş'in yüzeyinin üstünde ince kromosfer ve dev korona bulunur; korona 2 milyon santigrat dereceye ulaşır, fotosferden çok daha sıcaktır.", "Above the Sun's surface are its thin chromosphere and the huge corona (crown). / The corona reaches up to 3.5 million °F (2 million °C) – much, much hotter than the photosphere.", NS, ["2"]),
    F(9, "Madde koronadan ses üstü hızlarla ayrılınca güneş rüzgârı olur.", "Once material leaves the corona at supersonic speeds, it becomes the solar wind", NS),
    F(10, "Güneş lekeleri, manyetik alan çizgilerinin yoğunlaşmasıyla oluşan daha serin bölgelerdir; sayıları Güneş'in doğal 11 yıllık döngüsüyle artıp azalır.", "Sunspots are cooler regions on the Sun caused by a concentration of magnetic field lines. / The number of sunspots goes up and down as the Sun goes through its natural 11-year cycle.", SS, ["11"]),
    F(11, "Güneş patlamaları ve koronal kütle atımları, Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.", "The latter two are giant explosions of energy and particles that can reach Earth.", NS),
    F(12, "Güneş o kadar uzaktadır ki ışığının bize ulaşması yaklaşık 8 dakika 20 saniye sürer.", "The Sun is so far away that it takes light about 8 minutes and 20 seconds for it to get to us", SA, ["8", "20"]),
    F(13, "Güneş, Dünya'dan yaklaşık 100 kat, en büyük gezegen Jüpiter'den yaklaşık 10 kat daha geniştir; ama ortalama büyüklükte bir yıldızdır.", "The Sun is about 100 times wider than Earth and about 10 times wider than Jupiter, the biggest planet. / Our Sun is about 100 times wider than Earth, but it is just an average sized star.", NS + "; " + SA, ["100", "10"]),
    F(14, "Güneş yaklaşık 4,6 milyar yıl önce oluştu; ömrünün yarısından biraz daha azını geçirdi ve beyaz cüceye dönüşmeden önce yaklaşık 5 milyar yıl daha yaşayacak.", "The Sun formed about 4.6 billion years ago / Scientists predict the Sun is a little less than halfway through its lifetime / will last another 5 billion years or so before it becomes a white dwarf.", NS, ["4.6", "5"]),
    F(15, "Güneş'e çok özel koruyucu gözlük olmadan asla doğrudan bakılmamalıdır.", "you should never look directly at the Sun without very special protective eyewear.", SA),
]}
e = Ep(); L = e.L
e.sec("hook", [
    L("Sabah perdeyi açtığında yüzüne vuran o ışık, aslında yaklaşık 8 dakika 20 saniye önce Güneş'ten yola çıktı!", [12], "Sabah perdeyi açtığında yüzüne vuran o ışık, aslında yaklaşık sekiz dakika yirmi saniye önce Güneş'ten yola çıktı!"),
    L("Peki Güneş bu ışığı nasıl üretiyor? İçinde ateş mi yanıyor?"),
    L("Bugün en yakın yıldızımızın kalbine yolculuk ediyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Güneş neyden yapılmıştır? Işığını nasıl üretir? Ve içinde hangi katmanlar vardır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre yıldız, sıcak ve parlayan bir gaz topudur. Güneş de bir yıldızdır.", [1], "Nasa'ya göre yıldız, sıcak ve parlayan bir gaz topudur. Güneş de bir yıldızdır."),
    L("Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.", [2]),
    L("Güneş'te sıradan bir ateş yanmaz. Işığın sırrı çekirdekte saklı: nükleer kaynaşma, yani füzyon!", [3]),
    L("Çekirdekte hidrojen atomları öyle büyük bir kuvvetle çarpışır ki kaynaşıp yeni bir elemente, helyuma dönüşür.", [3]),
    L("Bu kaynaşma, Güneş'in ısısına ve ışığına güç verir. Çekirdekte sıcaklık yaklaşık 15 milyon santigrat derecedir!", [3, 4], "Bu kaynaşma, Güneş'in ısısına ve ışığına güç verir. Çekirdekte sıcaklık yaklaşık on beş milyon santigrat derecedir!"),
    L("Benim içimde de enerji var ama füzyon değil, sadece bir pil. Neyse ki ben de parlıyorum, en azından anten yıldızım!"),
])
e.sec("finding", [
    L("Güneş'in içi katmanlıdır: çekirdek, ışınım bölgesi ve konveksiyon bölgesi.", [5]),
    L("Enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık 170.000 yıl sürer!", [5], "Enerjinin çekirdekten konveksiyon bölgesinin tepesine ulaşması yaklaşık yüz yetmiş bin yıl sürer!"),
    L("Konveksiyon bölgesinde dev sıcak plazma kabarcıkları, kaynayan bir tencere gibi yukarı doğru yükselir.", [6]),
    L("Güneş'in yüzeyi dediğimiz bölüme fotosfer denir. Sıcaklığı yaklaşık 5.500 santigrat derecedir.", [7], "Güneş'in yüzeyi dediğimiz bölüme fotosfer denir. Sıcaklığı yaklaşık beş bin beş yüz santigrat derecedir."),
    L("Yüzeyin üstünde ince kromosfer ve dev korona vardır. İşin garibi, korona 2 milyon santigrat dereceye ulaşır; yani yüzeyden çok daha sıcaktır!", [8], "Yüzeyin üstünde ince kromosfer ve dev korona vardır. İşin garibi, korona iki milyon santigrat dereceye ulaşır; yani yüzeyden çok daha sıcaktır!"),
    L("Koronadan ses üstü hızlarla kaçan maddeye güneş rüzgârı denir.", [9]),
])
e.sec("importance", [
    L("Güneş'in yüzeyinde bazen daha karanlık lekeler görülür. Bunlar, manyetik alan çizgilerinin yoğunlaştığı daha serin bölgelerdir.", [10]),
    L("Güneş lekelerinin sayısı, Güneş'in doğal 11 yıllık döngüsüyle artıp azalır.", [10], "Güneş lekelerinin sayısı, Güneş'in doğal on bir yıllık döngüsüyle artıp azalır."),
    L("Güneş patlamaları ve koronal kütle atımları ise Dünya'ya ulaşabilen dev enerji ve parçacık patlamalarıdır.", [11]),
    L("Güneş, Dünya'dan yaklaşık 100 kat daha geniştir. Yine de evrende ortalama büyüklükte bir yıldızdır!", [13], "Güneş, Dünya'dan yaklaşık yüz kat daha geniştir. Yine de evrende ortalama büyüklükte bir yıldızdır!"),
    L("Güneş yaklaşık 4,6 milyar yıl önce oluştu. Ömrünün yarısını henüz doldurmadı ve yaklaşık 5 milyar yıl daha parlayacak.", [14], "Güneş yaklaşık dört virgül altı milyar yıl önce oluştu. Ömrünün yarısını henüz doldurmadı ve yaklaşık beş milyar yıl daha parlayacak."),
    L("Beş milyar yıl mı? Benim garantim sadece iki yıl!"),
    L("Şimdi sıra sende! İki beyaz karton al. Birine iğneyle küçük bir delik aç.", [15]),
    L("Güneşe sırtını dön, delikli kartonu tut ve ışığı diğer kartona düşür. Küçük bir Güneş görüntüsü göreceksin. Ama Güneş'e asla doğrudan bakma!", [15]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? NASA'ya göre Güneş, en büyük gezegen Jüpiter'den bile yaklaşık 10 kat daha geniştir!", [13], "Bunu biliyor muydun? Nasa'ya göre Güneş, en büyük gezegen Jüpiter'den bile yaklaşık on kat daha geniştir!"),
    L("Hızlı soru! Güneş'in çekirdeğinde hidrojen hangi elemente dönüşür?", [3]),
    L("Düşün bakalım... Evet: helyum!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Güneşli günler dilerim!"),
])
S = e.S
S(3, {"type": "hook", "question": "Güneş nasıl parlar?", "emoji": "☀️"}, ["🌅", "✨"], ["8 DAKİKA 20 SANİYE", "ATEŞ Mİ?", "YILDIZIN KALBİ"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Güneş neyden yapılmıştır?", "Işığını nasıl üretir?", "İçinde hangi katmanlar var?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Güneş bir yıldız", "emoji": "☀️", "chips": [{"label": "Sıcak, parlayan gaz topu", "emoji": "🔥"}, {"label": "Hidrojen ve helyum", "emoji": "🎈"}, {"label": "Kütle çekimiyle bir arada", "emoji": "🧲"}]}, ["⭐", "🎈"], ["YILDIZ", "HİDROJEN + HELYUM"])
S(2, {"type": "diagram", "title": "Füzyon", "layout": "flow", "nodes": [{"label": "Hidrojen atomları", "emoji": "⚪"}, {"label": "Büyük kuvvetle çarpışır", "emoji": "💥"}, {"label": "Helyum + ısı ve ışık", "emoji": "☀️"}]}, ["💥", "🔋"], ["FÜZYON", "KAYNAŞMA"], fx="sparkle")
S(2, {"type": "big-number", "value": "15 milyon °C", "label": "Güneş'in çekirdeğindeki sıcaklık (yaklaşık)", "sub": "NASA", "icon": "🔥"}, ["🔋", "⭐"], ["15 MİLYON °C", "PİLLİ MUMA 🔋"])
S(3, {"type": "stages", "title": "Güneş'in içi", "rows": [{"label": "Çekirdek", "emoji": "🔴"}, {"label": "Işınım bölgesi", "emoji": "🟠"}, {"label": "Konveksiyon bölgesi", "emoji": "🟡"}, {"label": "Fotosfer: yüzey", "emoji": "☀️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim; ölçekli değildir."}, [], ["KATMANLAR", "170.000 YIL", "PLAZMA KABARCIKLARI"])
S(3, {"type": "comparison", "title": "Yüzey ve korona", "left": {"title": "Fotosfer ☀️", "items": ["Güneş'in yüzeyi", "Yaklaşık 5.500 °C"]}, "right": {"title": "Korona 👑", "items": ["Yüzeyin üstünde", "2 milyon °C'ye kadar", "Güneş rüzgârı buradan kaçar"]}}, ["🌡️", "👑"], ["FOTOSFER", "KORONA 🔥", "GÜNEŞ RÜZGÂRI"])
S(3, {"type": "meter", "title": "Güneş lekeleri", "label": "Leke sayısı", "emoji": "⚫", "phases": [{"label": "Daha serin, manyetik bölgeler", "level": 0.4, "emoji": "🧲"}, {"label": "11 yıllık döngüyle artar, azalır", "level": 0.8, "emoji": "🔄"}, {"label": "Patlamalar Dünya'ya ulaşabilir", "level": 0.6, "emoji": "💥"}], "note": NOTE}, ["⚫", "💥"], ["GÜNEŞ LEKESİ", "11 YIL", "PATLAMALAR"])
S(3, {"type": "big-number", "value": "100 kat", "label": "Güneş, Dünya'dan bu kadar geniş (yaklaşık)", "sub": "NASA", "icon": "🌍"}, ["🌍", "🛡️"], ["100 KAT", "4,6 MİLYAR YIL", "GARANTİ? 😅"])
S(2, {"type": "bullets", "title": "Sen de dene: iğne deliği", "items": ["İki beyaz karton al", "Birine iğneyle delik aç", "Güneşe sırtını dön, ışığı düşür", "Güneş'e asla doğrudan bakma!"], "tone": "caution"}, ["📄", "📌"], ["DENEY ZAMANI 🔬", "GÜNEŞE BAKMA ⚠️"])
S(1, {"type": "big-number", "value": "10 kat", "label": "Güneş, Jüpiter'den bu kadar geniş (yaklaşık)", "sub": "NASA", "icon": "🪐"}, ["🪐", "☀️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Hidrojen hangi elemente dönüşür?", "emoji": "🤔"}, ["⚪", "☀️"], ["HIZLI SORU!", "HELYUM ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 45, "videoTitle": "Güneş nasıl parlar?", "paperTitleTr": "Güneş nasıl parlar?",
  "theme": {"backdrop": "space", "actors": [{"kind": "fly", "emoji": "🛰️", "every": 34}]},
  "takeaways": ["Güneş, hidrojen ve helyumdan oluşan bir yıldızdır", "Çekirdekte hidrojen kaynaşıp helyuma dönüşür; bu füzyon ısıyı ve ışığı üretir", "Güneş'in katmanları, lekeleri ve koronası vardır; ışığı bize yaklaşık 8 dakika 20 saniyede ulaşır"],
  "description": "Güneş nasıl parlar? Bu bölümde Güneş'in bir yıldız olduğunu, çekirdekteki nükleer füzyonu, çekirdek, ışınım ve konveksiyon bölgelerini, fotosferi, kromosferi ve koronayı, güneş rüzgârını, güneş lekelerini ve Güneş'in büyüklüğünü ve yaşını keşfediyoruz. Sonunda güvenli bir iğne deliği gözlemi ve konuyu özetleyen bir şarkı var. Güneş'e asla doğrudan bakmayın.",
  "glossary": [
    {"term": "Yıldız", "meaning": "Sıcak, parlayan dev bir gaz topu."},
    {"term": "Füzyon", "meaning": "Atomların kaynaşarak yeni bir element oluşturması ve enerji açığa çıkarması."},
    {"term": "Çekirdek", "meaning": "Güneş'in füzyonun gerçekleştiği en iç bölgesi."},
    {"term": "Fotosfer", "meaning": "Güneş'in yüzeyi denen, ışık saçan katmanı."},
    {"term": "Korona", "meaning": "Güneş'in yüzeyinin üstündeki çok sıcak dış katman."},
    {"term": "Güneş lekesi", "meaning": "Güneş yüzeyindeki daha serin, karanlık bölge."},
    {"term": "Plazma", "meaning": "Atomları elektrik yükü kazanmış çok sıcak gaz."}],
  "song": e.song("Yıldızımız", [("☀️", "Güneş"), ("⚪", "Hidrojen"), ("💥", "Füzyon"), ("👑", "Korona"), ("⚫", "Leke")],
    ["Çekirdekte çarpışır hidrojen", "Kaynaşır, helyum olur", "Füzyon yakar ışığını", "Isı yayılır her yöne"],
    ["Parla, parla, yıldızımız!", "Işığın sekiz dakikada gelir", "Hidrojen, helyum, dev bir top", "Sabahları uyandırırsın bizi"],
    ["Plazma kaynar, yükselir", "Fotosfer parlar yüzeyde", "Korona yakar daha da çok", "Lekeler gelir, lekeler gider"],
    ["Parla, parla, yıldızımız!", "Işığın sekiz dakikada gelir", "Kartonu del, görüntüyü yakala", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "orbit", "emoji": "🌍"}, {"kind": "hop", "emoji": "☀️"}, {"kind": "fly", "emoji": "🛰️"}, {"kind": "hop", "emoji": "⭐"}])}
e.write(D, facts, script)
