"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:mevsimler-nasil-olusur"
NA = "NASA Space Place — What Causes the Seasons?"; NG = "National Geographic Education — Season"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "What Causes the Seasons?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/seasons/en/"},
    {"id": "k2", "title": "Season", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/season/"}],
  "facts": [
    F(1, "Mevsimlere Dünya'nın eğik ekseni yol açar; Dünya'nın ekseni dimdik durmaz; Dünya yörünge düzlemine göre eksenine eğiktir.", "Earth's tilted axis causes the seasons. / Earth has seasons because its axis doesn't stand up straight. / Seasons occur because Earth is tilted on its axis relative to the orbital plane,", NA + "; " + NG),
    F(2, "Dünya Güneş'in çevresinde dolanırken eğik ekseni hep aynı yöne bakar.", "As Earth orbits the Sun, its tilted axis always points in the same direction.", NA),
    F(3, "Dünya bu eksen çevresinde döner ve her gün bir tam tur atar.", "Earth spins around this pole, making one complete turn each day.", NA),
    F(4, "Kuzey Kutbu Güneş'e doğru eğikken (Haziran civarı) Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir ve orada yaz olur.", "Sometimes it is the North Pole tilting toward the Sun (around June) / the Sun's rays hit that part of Earth more directly than at any other time of the year / So, when the North Pole tilts toward the Sun, it's summer in the Northern Hemisphere.", NA),
    F(5, "Bir yarım küre Güneş'ten uzağa eğikken daha az güneş ışığı alır ve kış olur.", "When it is pointing away, there is less sunlight, leading to winter.", NA),
    F(6, "Güneş'e doğru eğik yarım küre daha fazla gün ışığı saati alır; Aralık'ta Güneş'ten uzağa eğik olan Kuzey Yarım Küre daha az gün ışığı saati alır.", "This means it gets more hours of daylight. / In December, when the Northern Hemisphere is tilted away from the sun, it receives fewer hours of daylight.", NG),
    F(7, "Kuzey Yarım Küre'deki mevsimler Güney Yarım Küre'dekilerin tersidir.", "The seasons in the Northern Hemisphere are the opposite of those in the Southern Hemisphere. / As the poles are on opposite ends of Earth, they experience opposite timing for the seasons.", NG + "; " + NA),
    F(8, "Pek çok kişi yazın Dünya'nın Güneş'e daha yakın olduğunu sanır; oysa Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir; yani uzaklık mevsimlerin nedeni değildir.", "Many people believe that Earth is closer to the Sun in the summer and that is why it is hotter. / aphelion (when Earth is farthest from the Sun) occurs in July, and perihelion (when we are closest) occurs in January. / That just goes to prove that Earth's distance from the Sun is not the cause of the seasons.", NA),
    F(9, "Yaz 20 ya da 21 Haziran'daki yaz gündönümüyle başlar; bu, yılın en çok gün ışığı olan günüdür; kış gündönümü en kısa gündüzün olduğu gündür.", "Summer begins on June 20 or 21, the summer solstice, which has the most daylight of any day in the year. / This is the winter solstice, the day of the year with the shortest period of daylight.", NG, ["20", "21"]),
    F(10, "İlkbahar ve sonbahar, gece ile gündüzün eşit olduğu ekinokslarla başlar; ilkbahar ekinoksu 20 ya da 21 Mart'ta, sonbahar ekinoksu 22 ya da 23 Eylül'dedir.", "Spring and fall, or autumn, begin on equinoxes, days that have equal amounts of daylight and darkness. / The vernal, or spring, equinox falls on March 20 or 21, and the autumnal equinox is on September 22 or 23.", NG, ["20", "21", "22", "23"]),
    F(11, "Helsinki'de Haziran ortasında 18,5 saat gün ışığı olur; Atina'da Haziran'da 14,5, Aralık'ta 9,5 saat gün ışığı vardır.", "Helsinki, Finland, sees 18.5 hours of daylight in the middle of June. / It has 14.5 hours of daylight in June and 9.5 hours in December.", NG, ["18.5", "14.5", "9.5"]),
    F(12, "Alaska'daki Barrow'da Mayıs ortasından Ağustos başına kadar gün boyu aydınlık olur; Kasım ortasından Ocak'a kadar ise tam karanlık hüküm sürer.", "stays light all day long between mid-May and early August / in total darkness between mid-November and January", NG),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Yazın güneş akşam geç saatlere kadar batmaz. Kışın ise daha okuldan dönerken hava kararır. Neden?", [6]),
    L("Ve neden bir yıl içinde dört mevsim yaşıyoruz?"),
    L("Bugün Dünya'mızın uzaydaki dansına bakıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Mevsimlere ne yol açar? Güneş'e yakınlık işe karışır mı? Ve günler neden uzayıp kısalır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre mevsimlerin sırrı tek bir kelimede saklı: eğiklik. Dünya'nın ekseni dimdik durmaz, yana yatıktır.", [1], "Nasa'ya göre mevsimlerin sırrı tek bir kelimede saklı: eğiklik. Dünya'nın ekseni dimdik durmaz, yana yatıktır."),
    L("Eksen, Dünya'nın kuzey ve güney kutuplarından geçen hayali çizgidir. Dünya bu çizginin çevresinde döner ve her gün bir tam tur atar.", [3]),
    L("Benim de bir eksenim var: başımı sağa sola çeviriyorum. Ama mevsim yapamıyorum, sadece baş dönmesi!"),
    L("Dünya bir yandan da Güneş'in çevresinde dolanır. Bu yolculuk boyunca eğik ekseni hep aynı yöne bakar.", [2]),
    L("Bu yüzden yılın bir bölümünde Kuzey Yarım Küre Güneş'e doğru eğilir, diğer bölümünde Güneş'ten uzağa.", [2, 4, 5]),
])
e.sec("finding", [
    L("Haziran civarında Kuzey Kutbu Güneş'e doğru eğiktir. Güneş ışınları Kuzey Yarım Küre'ye yılın diğer zamanlarından daha doğrudan gelir.", [4]),
    L("İşte bu yüzden orada yaz olur. Türkiye de Kuzey Yarım Küre'de, bizde de yaz olur.", [4]),
    L("National Geographic'e göre Güneş'e doğru eğik yarım küre daha fazla saat gün ışığı alır. Günler uzar!", [6], f"{NGs}'e göre Güneş'e doğru eğik yarım küre daha fazla saat gün ışığı alır. Günler uzar!"),
    L("Aralık'ta ise Kuzey Yarım Küre Güneş'ten uzağa eğiktir. Daha az güneş ışığı ve daha az gün ışığı saati alır: kış gelir.", [5, 6]),
    L("Peki Güney Yarım Küre? Orada mevsimler bizimkinin tersidir. Biz kışın üşürken Güney Yarım Küre'de yaz yaşanır.", [7]),
    L("Yani Aralık'ta orada biri plajda dondurma yiyebilir. Ben kışın sadece şarjımı yerim!", [7]),
])
e.sec("importance", [
    L("Pek çok kişi yazın sıcak olmasının nedeninin Dünya'nın Güneş'e yaklaşması olduğunu sanır.", [8]),
    L("Ama NASA'ya göre Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir.", [8], "Ama Nasa'ya göre Dünya Güneş'e en yakın noktasına Ocak'ta, en uzak noktasına Temmuz'da gelir."),
    L("Yani biz Güneş'e en yakınken kış yaşıyoruz! Demek ki mevsimlerin nedeni uzaklık değil, eğiklik.", [8]),
    L("Yılın dönüm noktaları da var. Yaz, 20 ya da 21 Haziran'daki yaz gündönümüyle başlar. Bu, yılın en uzun gündüzüdür.", [9], "Yılın dönüm noktaları da var. Yaz, yirmi ya da yirmi bir Haziran'daki yaz gündönümüyle başlar. Bu, yılın en uzun gündüzüdür."),
    L("Kış gündönümü ise gündüzün en kısa olduğu gündür.", [9]),
    L("İlkbahar ve sonbahar ekinoksla başlar: gece ile gündüzün eşit olduğu günler. İlkbahar ekinoksu 20 ya da 21 Mart, sonbahar ekinoksu 22 ya da 23 Eylül'dedir.", [10], "İlkbahar ve sonbahar ekinoksla başlar: gece ile gündüzün eşit olduğu günler. İlkbahar ekinoksu yirmi ya da yirmi bir Mart, sonbahar ekinoksu yirmi iki ya da yirmi üç Eylül'dedir."),
    L("Kuzeye gittikçe fark büyür. Haziran ortasında Finlandiya'nın Helsinki kentinde 18,5 saat gün ışığı olur.", [11], "Kuzeye gittikçe fark büyür. Haziran ortasında Finlandiya'nın Helsinki kentinde on sekiz buçuk saat gün ışığı olur."),
    L("Yunanistan'ın Atina kentinde ise Haziran'da 14,5, Aralık'ta 9,5 saat gün ışığı vardır.", [11], "Yunanistan'ın Atina kentinde ise Haziran'da on dört buçuk, Aralık'ta dokuz buçuk saat gün ışığı vardır."),
    L("Şimdi sıra sende! Karanlık bir odada bir el fenerini bir kâğıda tam dik tut, sonra yana yatırarak tut.", [4]),
    L("Işık lekesi nasıl değişiyor? Hangisi daha küçük ve parlak? Güneş ışınlarının doğrudan gelmesi de buna benzer. Ama Güneş'e asla doğrudan bakma!", [4]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Alaska'daki Barrow kentinde Mayıs ortasından Ağustos başına kadar gün boyu hava aydınlık kalır.", [12]),
    L("Kasım ortasından Ocak'a kadar ise tam karanlık olur. Orada uyku saatini ayarlamak zor olmalı!", [12]),
    L("Hızlı soru! Mevsimlere ne yol açar: Güneş'e uzaklık mı, eksenin eğikliği mi?", [1, 8]),
    L("Düşün bakalım... Evet: eksenin eğikliği!", [1]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Hangi mevsimdeysen tadını çıkar!"),
])
S = e.S
S(3, {"type": "hook", "question": "Mevsimler nasıl oluşur?", "emoji": "🌍"}, ["☀️", "❄️"], ["UZUN GÜNLER", "DÖRT MEVSİM", ""])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Mevsimlere ne yol açar?", "Güneş'e yakınlık işe karışır mı?", "Günler neden uzayıp kısalır?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Eğik eksen", "emoji": "🌍", "chips": [{"label": "Eksen dimdik değil", "emoji": "📐"}, {"label": "Kutuplardan geçen hayali çizgi", "emoji": "📍"}, {"label": "Her gün bir tam tur", "emoji": "🔄"}]}, ["🔄", "🤖"], ["EĞİKLİK!", "EKSEN", "BAŞ DÖNMESİ 😵"])
S(2, {"type": "diagram", "title": "Güneş çevresinde yolculuk", "layout": "cycle", "nodes": [{"label": "Kuzey Güneş'e eğik", "emoji": "☀️"}, {"label": "Eksen hep aynı yöne", "emoji": "➡️"}, {"label": "Kuzey Güneş'ten uzak", "emoji": "❄️"}, {"label": "Eksen hep aynı yöne", "emoji": "➡️"}]}, ["🌍", "☀️"], ["DOLANMA", "HEP AYNI YÖN"])
S(3, {"type": "meter", "title": "Haziran: Kuzey Yarım Küre", "label": "Güneş ışığı", "emoji": "☀️", "phases": [{"label": "Işınlar daha doğrudan", "level": 0.75, "emoji": "🎯"}, {"label": "Yaz!", "level": 0.85, "emoji": "🏖️"}, {"label": "Daha çok gün ışığı saati", "level": 0.95, "emoji": "⏰"}], "note": NOTE}, ["🌻", "🏖️"], ["DOĞRUDAN IŞIK", "YAZ 🏖️", "UZUN GÜNLER"])
S(3, {"type": "comparison", "title": "Aralık'ta iki yarım küre", "left": {"title": "Kuzey ❄️", "items": ["Güneş'ten uzağa eğik", "Daha az gün ışığı", "Kış"]}, "right": {"title": "Güney ☀️", "items": ["Mevsimler tersine", "Yaz"]}}, ["🍦", "⛄"], ["KIŞ ❄️", "TERS MEVSİMLER", "ŞARJ YİYEN MUMA 🔋"])
S(3, {"type": "big-number", "value": "Ocak", "label": "Dünya Güneş'e en çok bu ayda yaklaşır", "sub": "NASA", "icon": "🌍"}, ["☀️", "🤔"], ["YANLIŞ İNANIŞ", "EN YAKIN: OCAK", "UZAKLIK DEĞİL!"], fx="sparkle")
S(3, {"type": "stages", "title": "Yılın dönüm noktaları", "rows": [{"label": "20 ya da 21 Mart: ilkbahar ekinoksu", "emoji": "🌱"}, {"label": "20 ya da 21 Haziran: yaz gündönümü", "emoji": "☀️"}, {"label": "22 ya da 23 Eylül: sonbahar ekinoksu", "emoji": "🍂"}, {"label": "Kış gündönümü: en kısa gündüz", "emoji": "❄️"}], "path": [1, 1, 3, 3, 0, 0, 2, 2], "highlightRow": 1, "note": "Şematik çizim."}, [], ["GÜNDÖNÜMÜ", "EN KISA GÜNDÜZ", "EKİNOKS"])
S(2, {"type": "bar-chart", "title": "Gün ışığı (saat)", "unit": "saat", "bars": [{"label": "Helsinki, Haziran ortası", "value": 18.5, "display": "18,5", "highlight": True}, {"label": "Atina, Haziran", "value": 14.5, "display": "14,5"}, {"label": "Atina, Aralık", "value": 9.5, "display": "9,5"}]}, ["🇫🇮", "🇬🇷"], ["KUZEYE GİTTİKÇE", "KISA KIŞ GÜNLERİ"])
S(2, {"type": "bullets", "title": "Sen de dene: el feneri", "items": ["Karanlık oda, el feneri, kâğıt", "Feneri dik tut, sonra yatır", "Işık lekesini karşılaştır", "Güneş'e asla doğrudan bakma!"], "tone": "caution"}, ["🔦", "📄"], ["DENEY ZAMANI 🔬", "GÜNEŞ'E BAKMA ⚠️"])
S(2, {"type": "spotlight", "title": "Barrow, Alaska", "emoji": "🧭", "chips": [{"label": "Mayıs–Ağustos: hep aydınlık", "emoji": "☀️"}, {"label": "Kasım–Ocak: tam karanlık", "emoji": "🌑"}]}, ["🌙", "😴"], ["BUNU BİLİYOR MUYDUN?", "UYKU SAATİ? 😴"])
S(2, {"type": "hook", "question": "Mevsimlere ne yol açar?", "emoji": "🤔"}, ["🌍", "📐"], ["HIZLI SORU!", "EĞİKLİK ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 30, "videoTitle": "Mevsimler nasıl oluşur?", "paperTitleTr": "Mevsimler nasıl oluşur?",
  "theme": {"backdrop": "space", "actors": [{"kind": "fly", "emoji": "☄️", "every": 34}]},
  "takeaways": ["Mevsimlere Dünya'nın eğik ekseni yol açar", "Güneş'e doğru eğik yarım kürede ışınlar doğrudan gelir, günler uzar", "Uzaklık neden değil: Dünya Güneş'e en çok Ocak'ta yaklaşır"],
  "description": "Neden dört mevsim yaşıyoruz? Yazın günler neden uzun, kışın neden kısa? Bu bölümde Dünya'nın eğik eksenini, Güneş çevresindeki yolculuğunu, gündönümlerini ve ekinoksları, iki yarım kürenin ters mevsimlerini ve 'Güneş'e yakınlık' yanılgısını keşfediyoruz. Sonunda el feneriyle güvenli bir deney ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Eksen", "meaning": "Dünya'nın kuzey ve güney kutuplarından geçen, çevresinde döndüğü hayali çizgi."},
    {"term": "Yörünge", "meaning": "Dünya'nın Güneş'in çevresinde izlediği yol."},
    {"term": "Yarım küre", "meaning": "Dünya'nın Ekvator'un kuzeyinde ya da güneyinde kalan yarısı."},
    {"term": "Gündönümü", "meaning": "Gündüzün yılın en uzun ya da en kısa olduğu gün."},
    {"term": "Ekinoks", "meaning": "Gece ile gündüzün eşit olduğu gün; ilkbahar ve sonbahar bununla başlar."}],
  "song": e.song("Eğik Dans", [("🌍", "Dünya"), ("☀️", "Güneş"), ("📐", "Eksen"), ("❄️", "Kış"), ("🌻", "Yaz")],
    ["Dünya döner, ekseni yatık", "Güneş'in çevresinde bir yolculuk", "Eksen hep aynı yöne bakar", "Bir yan ışıkta, bir yan karanlıkta"],
    ["Eğik dansla gelir mevsimler!", "Doğrudan ışık, uzun günler", "Uzaklık değil, eğiklik bu", "Kuzeyde kış, güneyde yaz"],
    ["Gündönümünde en uzun gündüz", "Ekinoksta gece gündüz eşit", "Ocak'ta Güneş'e en yakınız", "Yine de kar yağar bize"],
    ["Eğik dansla gelir mevsimler!", "Doğrudan ışık, uzun günler", "Feneri tut, ışığı izle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "orbit", "emoji": "🌍"}, {"kind": "hop", "emoji": "☀️"}, {"kind": "hop", "emoji": "❄️"}, {"kind": "hop", "emoji": "🌻"}])}
e.write(D, facts, script)
