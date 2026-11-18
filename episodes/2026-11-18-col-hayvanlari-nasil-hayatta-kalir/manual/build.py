"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:col-hayvanlari-nasil-hayatta-kalir"
NG = "National Geographic Education — Desert"; NC = "National Geographic — Dromedary Camel"; NP = "National Park Service — Deserts"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Desert", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/desert/"},
    {"id": "k2", "title": "Dromedary Camel", "publisher": "National Geographic", "url": "https://www.nationalgeographic.com/animals/mammals/facts/dromedary-camel"},
    {"id": "k3", "title": "Deserts", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/deserts/index.htm"}],
  "facts": [
    F(1, "Çöller çok az yağış alan bölgelerdir; çöl, yılda en fazla 25 santimetre yağış alan kara parçasıdır.", "Deserts are areas that receive very little precipitation. / area of land that receives no more than 25 centimeters (10 inches) of precipitation a year.", NG, ["25"]),
    F(2, "Bazı çöllerde gündüz sıcaklığı 54 santigrat dereceye kadar çıkar; bazı çöllerin kışları soğuktur ya da bütün yıl soğuktur; Antarktika'nın neredeyse tamamı bir kutup çölüdür.", "Although some deserts are very hot, with daytime temperatures as high as 54°C (130°F) / other deserts have cold winters or are cold year-round. / Almost the entire continent of Antarctica is a polar desert, experiencing little precipitation.", NG, ["54"]),
    F(3, "Chihuahua Çölü'nde gündüz sıcaklığı 37 santigrat dereceyi aşabilirken gece sıcaklığı donma noktası olan 0 derecenin altına düşebilir; çöller geceleri nem ve bulutların sağladığı yalıtım olmadığı için hızla soğur.", "Daytime temperatures in the Chihuahua can climb beyond 37°C (100°F), / while nighttime temperatures can dip below freezing (0°C or 32°F). / At night, these areas cool quickly because they lack the insulation provided by humidity and clouds.", NG, ["37", "0"]),
    F(4, "Çöl hayvanlarının çoğu gececidir; sıcak günleri uyuyarak geçirir, geceleri avlanır ve yiyecek arar; birçoğu sıcaktan yere kazdıkları serin yuvalarda korunur.", "Most xerocoles are nocturnal. / They sleep through the hot days and do their hunting and foraging at night. / Many escape the heat in cool burrows they dig in the ground.", NG),
    F(5, "Çöl tilkisinin böbrekleri yediği besinden yeterince su tutar; yol koşucusu kuşu suyunu besininden alır.", "Their kidneys retain enough water from the food they eat. / The roadrunner, native to the deserts of North America, obtains water from its food.", NG),
    F(6, "Çöl tavşanının uzun kulaklarında ısı yayan kan damarları vardır.", "For example, a jackrabbit’s long ears contain blood vessels that release heat.", NG),
    F(7, "Develer hörgüçlerinde su depolamaz; hörgüç yağ depolar.", "The animals do not store water in their humps, as people once believed. / The hump stores up to 80 pounds of fat", NC),
    F(8, "Tek hörgüçlü develer vücut ağırlıklarının yüzde 30'una kadarını zarar görmeden kaybedebilir.", "dromedary camels can lose up to 30% of their body weight without harm.", NG, ["30"]),
    F(9, "Çöl kaplumbağası vücut ağırlığının yüzde 40'ına kadar suyu mesanesinde depolayabilir.", "can store up to 40% of its body weight in water within its bladder", NG, ["40"]),
    F(10, "Kaktüs gibi bazı çöl bitkilerinin sığ, geniş yayılan kökleri vardır; suyu hızla emip hücrelerinde depolarlar; büyük bir saguaro yüzlerce litre su tutabilen canlı bir depodur.", "Some desert plants, such as cactuses, have shallow, wide-spreading root systems. / The plants soak up water quickly and store it in their cells. / A large saguaro is a living storage tower that can hold hundreds of liters of water.", NG),
    F(11, "Mesquite ağacının kökleri yerin 61 metreden daha derinindeki suya ulaşabilir.", "The roots of a mesquite tree, for example, can reach water more than 61 meters (200 feet) underground.", NG, ["61"]),
    F(12, "Mesquite, saguaro ve birçok çöl bitkisinin onları otçul hayvanlardan koruyan dikenleri vardır.", "Mesquites, saguaros and many other desert plants also have thorns or spines to protect them from grazing animals.", NG),
    F(13, "Çöl şafakta hayatla dolar, öğleye doğru hayvanlar sıcaktan korunmak için saklanınca sessizleşir.", "the desert teems with life at dawn and quiets by noon, as animals take shelter from the heat.", NP),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Kavurucu güneş, yağmur yok, gölge yok. Böyle bir yerde sen kaç saat dayanırdın? Ama çölde sayısız hayvan ve bitki yaşıyor!", [1, 13]),
    L("Peki onlar susuzluğa ve sıcağa nasıl dayanıyor?"),
    L("Bugün çölün hayatta kalma ustalarıyla tanışıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Çöl nedir? Hayvanlar sıcaktan ve susuzluktan nasıl korunur? Ve bitkiler suyu nasıl saklar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre çöl, çok az yağış alan bir bölgedir: yılda en fazla 25 santimetre yağış.", [1], f"{NGs}'e göre çöl, çok az yağış alan bir bölgedir: yılda en fazla yirmi beş santimetre yağış."),
    L("Bazı çöllerde gündüz sıcaklığı 54 santigrat dereceye kadar çıkar! Ama her çöl sıcak değildir; Antarktika'nın neredeyse tamamı bir kutup çölüdür.", [2], "Bazı çöllerde gündüz sıcaklığı elli dört santigrat dereceye kadar çıkar! Ama her çöl sıcak değildir; Antarktika'nın neredeyse tamamı bir kutup çölüdür."),
    L("Çölde gece ile gündüz arasındaki fark da büyüktür. Chihuahua Çölü'nde gündüz 37 dereceyi aşabilir, gece ise sıfırın altına düşebilir.", [3], "Çölde gece ile gündüz arasındaki fark da büyüktür. Chihuahua Çölü'nde gündüz otuz yedi dereceyi aşabilir, gece ise sıfırın altına düşebilir."),
    L("Neden? Çünkü çölde ısıyı tutan nem ve bulut azdır. Bu yüzden geceleri hızla soğur.", [3]),
    L("Gündüz kızar, gece donarım. Ben çölde kalsam ya erirdim ya da pilim donardı!"),
])
e.sec("finding", [
    L("Çöl hayvanlarının ilk sırrı: gece çalışmak! Çoğu gececidir; sıcak gündüzleri uyuyarak geçirir, geceleri avlanır.", [4]),
    L("Birçoğu da toprağa kazdığı serin yuvalarda sıcaktan saklanır.", [4]),
    L("Milli Parklar Servisi'ne göre çöl şafakta hayatla dolar, öğleye doğru ise sessizleşir.", [13]),
    L("İkinci sır: suyu yiyecekten almak. Çöl tilkisinin böbrekleri, yediği besinden yeterince su tutar.", [5]),
    L("Yol koşucusu denen kuş da suyunu besininden alır.", [5]),
    L("Üçüncü sır: kulaklar! Çöl tavşanının uzun kulaklarında ısıyı dışarı veren kan damarları vardır. Kulakları bir radyatör gibidir!", [6]),
    L("Benim de radyatörüm var: fan. Ama o kulaklarım kadar sevimli değil!"),
])
e.sec("importance", [
    L("Peki develer? Pek çok kişi deve hörgücünde su depolandığını sanır. Ama bu doğru değil: Hörgüç yağ depolar!", [7]),
    L("National Geographic'e göre tek hörgüçlü develer vücut ağırlıklarının yüzde 30'una kadarını zarar görmeden kaybedebilir.", [8], f"{NGs}'e göre tek hörgüçlü develer vücut ağırlıklarının yüzde otuzuna kadarını zarar görmeden kaybedebilir."),
    L("Çöl kaplumbağası ise vücut ağırlığının yüzde 40'ına kadar suyu mesanesinde saklayabilir!", [9], "Çöl kaplumbağası ise vücut ağırlığının yüzde kırkına kadar suyu mesanesinde saklayabilir!"),
    L("Bitkiler de usta. Kaktüslerin sığ ama geniş yayılan kökleri vardır; yağmur yağınca suyu hızla emer ve hücrelerinde saklarlar.", [10]),
    L("Büyük bir saguaro kaktüsü yüzlerce litre su tutabilen canlı bir depodur.", [10]),
    L("Mesquite ağacının kökleri ise yerin 61 metreden daha derinindeki suya ulaşabilir!", [11], "Meskit ağacının kökleri ise yerin altmış bir metreden daha derinindeki suya ulaşabilir!"),
    L("Dikenler de bitkileri, onları yemek isteyen hayvanlardan korur.", [12]),
    L("Şimdi sıra sende! Güneşli bir günde iki tabağa birer buz küpü koy. Birini güneşe bırak, diğerinin üstüne ters bir bardak kapat ve gölgeye koy.", [4]),
    L("Hangisi daha çabuk eriyor? Gölgedeki yuva, çöl hayvanlarının saklandığı serin yuvalar gibidir.", [4]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Bazı çöller sıcak değil, buz gibidir: Antarktika'nın neredeyse tamamı bir kutup çölüdür!", [2]),
    L("Hızlı soru! Deve hörgücünde ne depolar?", [7]),
    L("Düşün bakalım... Evet: yağ, su değil!", [7]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bol su iç, serin kal!"),
])
S = e.S
S(3, {"type": "hook", "question": "Çöl hayvanları nasıl hayatta kalır?", "emoji": "🐪"}, ["☀️", "🌵"], ["KAVURUCU SICAK", "SUSUZLUK", "HAYATTA KALMA"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Çöl nedir?", "Hayvanlar nasıl korunur?", "Bitkiler suyu nasıl saklar?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "big-number", "value": "25 cm", "label": "Bir çölün bir yılda aldığı en fazla yağış", "sub": "National Geographic", "icon": "🌧️"}, ["🌧️", "🧊"], ["AZ YAĞIŞ", "SICAK • SOĞUK ÇÖL"])
S(3, {"type": "comparison", "title": "Chihuahua Çölü'nde bir gün", "left": {"title": "Gündüz ☀️", "items": ["37 °C'yi aşabilir"]}, "right": {"title": "Gece 🌙", "items": ["0 °C'nin altına düşebilir", "Nem ve bulut yok: hızla soğur"]}}, ["🌡️", "🔋"], ["GECE • GÜNDÜZ", "HIZLA SOĞUR", "DONAN PİL 🥶"])
S(3, {"type": "spotlight", "title": "Gececiler", "emoji": "🌙", "chips": [{"label": "Gündüz uyur", "emoji": "😴"}, {"label": "Gece avlanır", "emoji": "🌙"}, {"label": "Serin yuvalar", "emoji": "🕳️"}]}, ["🌙", "🦉"], ["GECECİ", "YUVA", "ŞAFAK • ÖĞLE"])
S(2, {"type": "diagram", "title": "Suyu yiyecekten almak", "layout": "flow", "nodes": [{"label": "Besin ye", "emoji": "🦗"}, {"label": "Böbrekler suyu tutar", "emoji": "🫘"}, {"label": "Susuz yaşa", "emoji": "🦊"}]}, ["🦊", "🐦"], ["ÇÖL TİLKİSİ", "YOL KOŞUCUSU"])
S(2, {"type": "meter", "title": "Radyatör kulaklar", "label": "Isı", "emoji": "🐇", "phases": [{"label": "Uzun kulaklarda kan damarları", "level": 0.8, "emoji": "👂"}, {"label": "Isı dışarı verilir", "level": 0.35, "emoji": "🌬️"}], "note": NOTE}, ["🐇", "🌀"], ["RADYATÖR KULAKLAR", "FANLI MUMA 🌀"], fx="sparkle")
S(3, {"type": "bar-chart", "title": "Vücut ağırlığının yüzdesi", "unit": "%", "bars": [{"label": "Deve: zarar görmeden kaybeder", "value": 30, "display": "%30"}, {"label": "Kaplumbağa: su olarak saklar", "value": 40, "display": "%40", "highlight": True}]}, ["🐪", "🐢"], ["HÖRGÜÇ = YAĞ", "%30", "%40"])
S(2, {"type": "stages", "title": "Kaktüsün su planı", "rows": [{"label": "Sığ, geniş kökler", "emoji": "🌱"}, {"label": "Suyu hızla emer", "emoji": "💧"}, {"label": "Hücrelerde saklar", "emoji": "🌵"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 2, "note": "Şematik çizim."}, [], ["KAKTÜS", "SAGUARO"])
S(2, {"type": "big-number", "value": "61 m+", "label": "Mesquite kökleri bu derinlikteki suya ulaşabilir", "sub": "National Geographic", "icon": "🌳"}, ["🌳", "🌵"], ["DERİN KÖKLER", "DİKENLER"])
S(2, {"type": "bullets", "title": "Sen de dene: buz yarışı", "items": ["İki tabağa birer buz koy", "Biri güneşte kalsın", "Diğerine bardak kapat, gölgeye koy", "Hangisi daha çabuk eriyor?"]}, ["🧊", "☀️"], ["DENEY ZAMANI 🔬", "SERİN YUVA"])
S(1, {"type": "spotlight", "title": "Buz çölü", "emoji": "🧊", "chips": [{"label": "Antarktika: kutup çölü", "emoji": "🐧"}, {"label": "Az yağış alır", "emoji": "🌧️"}]}, ["🐧", "❄️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Deve hörgücünde ne depolar?", "emoji": "🤔"}, ["🐪", "💧"], ["HIZLI SORU!", "YAĞ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 48, "videoTitle": "Çöl hayvanları nasıl hayatta kalır?", "paperTitleTr": "Çöl hayvanları nasıl hayatta kalır?",
  "theme": {"backdrop": "desert", "actors": [{"kind": "walk", "emoji": "🐪", "every": 34}, {"kind": "hop", "emoji": "🦎", "every": 40}]},
  "takeaways": ["Çöl, yılda en fazla 25 santimetre yağış alan bölgedir; sıcak da soğuk da olabilir", "Hayvanlar gece çalışır, yuvalarda saklanır, suyu besinden alır ve ısıyı kulaklarından verir", "Deve hörgücü yağ depolar; kaktüsler suyu hücrelerinde saklar"],
  "description": "Çöl hayvanları sıcağa ve susuzluğa nasıl dayanır? Bu bölümde çölün ne olduğunu, gece ile gündüz arasındaki büyük sıcaklık farkını, gececi hayvanları ve serin yuvaları, suyu besinden alan çöl tilkisini, radyatör gibi kulaklı çöl tavşanını, deve hörgücünün sırrını, su saklayan kaplumbağayı ve kaktüsleri keşfediyoruz. Sonunda buz yarışı deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Çöl", "meaning": "Yılda çok az yağış alan bölge."},
    {"term": "Kutup çölü", "meaning": "Çok soğuk ve az yağış alan çöl; Antarktika gibi."},
    {"term": "Gececi", "meaning": "Gündüz dinlenip gece etkin olan hayvan."},
    {"term": "Yuva", "meaning": "Hayvanların toprağa kazdığı korunma yeri."},
    {"term": "Hörgüç", "meaning": "Devenin sırtındaki, yağ depolayan tümsek."},
    {"term": "Saguaro", "meaning": "Çok büyük boylara ulaşan, su depolayan bir kaktüs türü."}],
  "song": e.song("Çöl Ustaları", [("🐪", "Deve"), ("🦊", "Çöl tilkisi"), ("🐇", "Çöl tavşanı"), ("🐢", "Kaplumbağa"), ("🌵", "Kaktüs")],
    ["Güneş yakar, yağmur yağmaz", "Gündüz kavurur, gece dondurur", "Gececiler uyur gündüz boyu", "Serin yuvada saklanır"],
    ["Çölde usta, çölde güçlü!", "Su yok mu? Besinden alırız", "Kulaklar soğutur, yuvalar korur", "Hayat bulur kumun içinde"],
    ["Hörgüçte yağ var, su değil", "Kaplumbağa suyu saklar", "Kaktüs emer, depolar", "Derin kökler suyu bulur"],
    ["Çölde usta, çölde güçlü!", "Su yok mu? Besinden alırız", "Buzları yarıştır, gölgeyi gör", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "walk", "emoji": "🐪"}, {"kind": "hop", "emoji": "🦊"}, {"kind": "hop", "emoji": "🐇"}, {"kind": "walk", "emoji": "🐢"}])}
e.write(D, facts, script)
