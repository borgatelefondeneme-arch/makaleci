"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:deprem-nasil-olur"
B1 = "British Geological Survey — Earthquakes"; B2 = "British Geological Survey — What causes earthquakes?"; B3 = "British Geological Survey — How are earthquakes detected, located and measured?"
NG = "National Geographic Education — Earthquakes"; U1 = "USGS — The Science of Earthquakes"; U2 = "USGS — Can you predict earthquakes?"; NASA = "NASA Space Place — What Is an Earthquake?"; RD = "Ready.gov Kids — Earthquakes"
BU = "https://www.bgs.ac.uk/discovering-geology/earth-hazards/earthquakes/"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Earthquakes", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BU},
    {"id": "k2", "title": "What causes earthquakes?", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BU + "what-causes-earthquakes/"},
    {"id": "k3", "title": "How are earthquakes detected, located and measured?", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BU + "how-are-earthquakes-detected/"},
    {"id": "k4", "title": "Earthquakes", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/earthquakes/"},
    {"id": "k5", "title": "The Science of Earthquakes", "publisher": "USGS", "url": "https://www.usgs.gov/programs/earthquake-hazards/science-earthquakes"},
    {"id": "k6", "title": "Can you predict earthquakes?", "publisher": "USGS", "url": "https://www.usgs.gov/faqs/can-you-predict-earthquakes"},
    {"id": "k7", "title": "What Is an Earthquake?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/earthquakes/en/"},
    {"id": "k8", "title": "Earthquakes", "publisher": "Ready.gov", "url": "https://www.ready.gov/kids/disaster-facts/earthquakes"}],
  "facts": [
    F(1, "Deprem, yer kabuğunda biriken gerinim enerjisinin aniden serbest kalmasıdır.", "An earthquake is the sudden release of strain energy in the Earth’s crust", B1),
    F(2, "Dünya'nın dört temel katmanı vardır: katı kabuk, sıcak ve neredeyse katı manto, sıvı dış çekirdek ve katı iç çekirdek.", "a solid crust, a hot, nearly solid mantle, a liquid outer core and a solid inner core. / The earth has four major layers: the inner core, outer core, mantle and crust", NASA + "; " + U1),
    F(3, "Dünya'nın en dış katmanı tektonik levha denen yaklaşık 15 büyük parçaya bölünmüştür; levhalar birbirine göre çok yavaş, tipik olarak yılda birkaç santimetre hareket eder.", "The Earth’s outermost layer is fragmented into about 15 major slabs called tectonic plates. / Tectonic plates move very slowly relative to each other, typically a few centimetres per year", B2, ["15"]),
    F(4, "Levhalar birbirine doğru hareket edebilir, birbirine sürtünerek kayabilir ya da birbirinden ayrılabilir.", "Continental and oceanic plates may move toward each other, scrape past each other, or pull apart", NG),
    F(5, "Sürtünme kayaları yerinde tutar ve gerilim birikir; fayın iki yanındaki kayalar yavaş yavaş biçim değiştirir; blokları kaydıracak enerji depolanır.", "Friction, however, holds the rocks in place, causing stresses to build. / Before an earthquake, the buildup of stress in the rocks on either side of a fault results in gradual deformation. / the energy that would normally cause the blocks to slide past one another is being stored up.", NG + "; " + B2 + "; " + U1),
    F(6, "Elastik geri sekme: kayalar özgün biçimine döner ama fayın iki yanında yer değiştirmiş olur.", "return to their original shape (elastic rebound) but are offset on either side of the fault.", B2),
    F(7, "Depremin başladığı noktaya odak ya da hiposantr denir ve kilometrelerce derinde olabilir; odağın tam üstündeki yüzey noktası merkez üssüdür.", "The point where an earthquake starts is termed the focus or hypocentre and may be many kilometres deep within the earth. / The point at the surface directly above the focus is called the earthquake epicentre.", B1),
    F(8, "Enerji, gölcükteki halkalar gibi her yöne yayılır.", "the energy spreads out in all directions like ripples on a pond.", B1),
    F(9, "P dalgaları ilerleme yönü boyunca sıkışma ve genleşmelerden oluşur; S dalgalarının hareketi ilerleme yönüne diktir; P dalgaları S dalgalarından hızlıdır. Tipik yer kabuğunda P 5–7 km/s, S 3–4 km/s hızla ilerler.", "P-waves are longitudinal waves that consist of a series of compressions and dilations along the direction of travel. / S-waves are transverse waves, whose motion is perpendicular to the direction of travel. / P waves are also faster than S waves / VP 5–7 km/s in typical Earth’s crust / VS 3–4 km/s in typical Earth’s crust", B3 + "; " + U1, ["5", "7", "3", "4"]),
    F(10, "P dalgaları şimşek, S dalgaları gök gürültüsü gibidir; P'nin S'den hızlı olması depremin nerede olduğunu bulmayı sağlar.", "P waves are like the lightning, and S waves are like the thunder. / P waves are also faster than S waves, and this fact is what allows us to tell where an earthquake was.", U1),
    F(11, "Sismograf ya da sismometre, sismogramı oluşturan ölçüm aletidir.", "A seismograph or seismometer is the measuring instrument that creates the seismogram.", B3),
    F(12, "Büyüklük ölçekleri logaritmiktir: büyüklükte bir birimlik artış, genlikte on katlık artışa karşılık gelir.", "Earthquake magnitude scales are logarithmic, i.e. a one unit increase in magnitude corresponds to a tenfold increase in amplitude.", B3),
    F(13, "Şiddet, depremin yol açtığı sarsıntının gücünün nitel ölçüsüdür ve normalde merkez üssünden uzaklaştıkça azalır; büyüklük ise uzaklıktan bağımsızdır.", "Intensity is a qualitative measure of the strength of shaking caused by an earthquake / normally decreases with distance from the epicentre / is independent of distance from the epicentre.", B3),
    F(14, "Dünya'da her gün yüzlerce deprem olur; ciddi hasar verebilecek büyüklükte olanlar yılda yaklaşık 100 tanedir.", "Hundreds of earthquakes occur on Earth everyday. / There are around 100 earthquakes each year of a size that could cause serious damage.", NG + "; " + B1, ["100"]),
    F(15, "Artçı sarsıntılar ana depremden sonra haftalarca, aylarca, hatta yıllarca sürebilir.", "aftershocks can continue for weeks, months, and even years after the mainshock!", U1),
    F(16, "Ne USGS ne de başka bilim insanları bugüne kadar büyük bir depremi önceden bildi; bir tahminin tarih ve saati, yeri ve büyüklüğü belirtmesi gerekir. Bilim insanları belirli bir fayda gelecekte yeniden deprem olacağını bilir.", "Neither the USGS nor any other scientists have ever predicted a major earthquake. / 1) the date and time, 2) the location, and 3) the magnitude. / On any particular fault, scientists know there will be another earthquake sometime in the future", U2 + "; " + U1),
    F(17, "Erken uyarı, deprem başladıktan sonra yapılan bir bildirimdir.", "Early warning is a notification that is issued after an earthquake starts.", U2),
    F(18, "Deprem anında: yere çök, sağlam bir masanın altına gir, sarsıntı bitene kadar tutun; camlardan ve devrilebilecek eşyalardan uzak dur; dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.", "DROP to the ground. / Take COVER under a sturdy table or other heavy furniture. / HOLD ON until the shaking stops. / STAY AWAY from windows, glass, lighting fixtures, or furniture that could fall, like bookcases. / Move away from buildings, streetlights, and wires.", RD),
    F(19, "Hızla tahliye gerekirse ihtiyaç duyulacak eşyalarla bir acil durum çantası hazırlanmalıdır.", "Build an emergency kit with items that you will need if you have to evacuate quickly.", RD),
    F(20, "Büyüklüğü 10 ya da daha fazla olan depremler olamaz.", "No, earthquakes of magnitude 10 or larger cannot happen.", U2, ["10"]),
]}
e = Ep(); L = e.L
USG = "Yu Es Ci Es"; NGs = "Neşınıl Ciyografik"
e.sec("hook", [
    L("Ayağının altındaki yer sapasağlam görünür. Ama aslında çok yavaş hareket eden dev parçalardan oluşur!", [3]),
    L("Peki yer neden bazen aniden sarsılır? Ve sarsıntı uzaklara nasıl yayılır?"),
    L("Bugün yerin derinlerine iniyoruz!"),
])
e.sec("context", [
    L("Ben de bazen titrerim. Ama o deprem değil, titreşim modum!"),
    L("Üç sorumuz var. Deprem neden olur? Deprem dalgaları nasıl yayılır? Ve deprem sırasında ne yapmalıyız?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre Dünya dört temel katmandan oluşur: katı kabuk, sıcak manto, sıvı dış çekirdek ve katı iç çekirdek.", [2], "Nasa'ya göre Dünya dört temel katmandan oluşur: katı kabuk, sıcak manto, sıvı dış çekirdek ve katı iç çekirdek."),
    L("Britanya Jeoloji Araştırmaları Kurumu'na göre en dıştaki katman tek parça değildir: yaklaşık 15 büyük parçaya bölünmüştür. Bunlara tektonik levha denir.", [3], "Britanya Jeoloji Araştırmaları Kurumu'na göre en dıştaki katman tek parça değildir: yaklaşık on beş büyük parçaya bölünmüştür. Bunlara tektonik levha denir."),
    L("Levhalar birbirine göre çok yavaş hareket eder: yılda yalnızca birkaç santimetre.", [3]),
    L("Benim yazılım güncellemelerim bile bundan hızlı. Çoğu zaman!"),
    L("National Geographic'e göre levhalar birbirine yaklaşabilir, birbirinden uzaklaşabilir ya da yan yana sürtünerek kayabilir.", [4], f"{NGs}'e göre levhalar birbirine yaklaşabilir, birbirinden uzaklaşabilir ya da yan yana sürtünerek kayabilir."),
    L("Kaya bloklarının birbirine göre kaydığı kırıklara fay denir.", [5]),
    L("Ama kayalar kolayca kaymaz. Sürtünme onları yerinde tutar ve kayalarda gerilim birikmeye başlar.", [5]),
    L("Gerilim biriktikçe kayalar yavaş yavaş biçim değiştirir. Tıpkı bükülen bir cetvel gibi enerji depolar.", [5]),
])
e.sec("finding", [
    L("Sonunda kayalar daha fazla dayanamaz ve fay aniden kayar. Biriken enerji bir anda serbest kalır. İşte deprem budur!", [1, 5]),
    L("Kayalar eski biçimine geri döner ama fayın iki yanı artık yer değiştirmiştir. Buna elastik geri sekme denir.", [6]),
    L("Depremin yerin içinde başladığı noktaya odak ya da hiposantr denir. Kilometrelerce derinde olabilir.", [7]),
    L("Odağın tam üstündeki yeryüzü noktası ise merkez üssüdür.", [7]),
    L("Enerji odaktan her yöne yayılır; tıpkı suya atılan taşın oluşturduğu halkalar gibi. Bu dalgalara sismik dalga denir.", [8]),
    L("İki ana türü var. P dalgaları kayayı ilerleme yönünde sıkıştırıp gevşetir. S dalgaları ise ilerleme yönüne dik sallar.", [9], "İki ana türü var. Pe dalgaları kayayı ilerleme yönünde sıkıştırıp gevşetir. Se dalgaları ise ilerleme yönüne dik sallar."),
    L("P dalgaları daha hızlıdır: yer kabuğunda saniyede 5–7 kilometre yol alır. S dalgaları ise saniyede 3–4 kilometre.", [9], "Pe dalgaları daha hızlıdır: yer kabuğunda saniyede beş ile yedi kilometre yol alır. Se dalgaları ise saniyede üç ile dört kilometre."),
    L("USGS bunu şöyle benzetiyor: P dalgası şimşek gibidir, S dalgası gök gürültüsü gibi. Önce biri gelir, sonra öteki.", [10], f"{USG} bunu şöyle benzetiyor: Pe dalgası şimşek gibidir, Se dalgası gök gürültüsü gibi. Önce biri gelir, sonra öteki."),
    L("P dalgasının daha hızlı olması, bilim insanlarının depremin nerede olduğunu bulmasını sağlar.", [10], "Pe dalgasının daha hızlı olması, bilim insanlarının depremin nerede olduğunu bulmasını sağlar."),
    L("Dalgaları ölçen alete sismometre denir. Çizdiği kayıt ise sismogramdır.", [11]),
])
e.sec("importance", [
    L("Depremin büyüklüğü bir sayıyla ifade edilir. Bu ölçek logaritmiktir: büyüklük bir birim artınca dalganın genliği, yani kayıttaki yüksekliği, on katına çıkar.", [12]),
    L("Büyüklük ile şiddet aynı şey değildir. Şiddet, sarsıntının bir yerde ne kadar güçlü olduğunu anlatır ve merkez üssünden uzaklaştıkça genellikle azalır.", [13]),
    L("Depremler sanıldığından çok daha sıktır: National Geographic'e göre Dünya'da her gün yüzlerce deprem olur.", [14], f"Depremler sanıldığından çok daha sıktır: {NGs}'e göre Dünya'da her gün yüzlerce deprem olur."),
    L("Ciddi hasar verebilecek büyüklükte olanlar ise yılda yaklaşık 100 tanedir.", [14], "Ciddi hasar verebilecek büyüklükte olanlar ise yılda yaklaşık yüz tanedir."),
    L("Büyük bir depremden sonra artçı sarsıntılar haftalarca, aylarca, hatta yıllarca sürebilir.", [15]),
    L("Peki deprem önceden bilinebilir mi? USGS'ye göre bugüne kadar hiçbir bilim insanı büyük bir depremin gününü, yerini ve büyüklüğünü önceden bilemedi.", [16], f"Peki deprem önceden bilinebilir mi? {USG}'e göre bugüne kadar hiçbir bilim insanı büyük bir depremin gününü, yerini ve büyüklüğünü önceden bilemedi."),
    L("Ama bilim insanları bir fayda gelecekte yeniden deprem olacağını bilir. Erken uyarı sistemleri de deprem başladıktan hemen sonra haber verir.", [16, 17]),
    L("Bu yüzden en iyi çözüm hazırlıklı olmaktır. Ready.gov'un önerdiği üç hareketi ezberle: Çök, Kapan, Tutun!", [18], "Bu yüzden en iyi çözüm hazırlıklı olmaktır. Redi nokta gav'ın önerdiği üç hareketi ezberle: Çök, Kapan, Tutun!"),
    L("Yere çök. Sağlam bir masanın altına gir. Sarsıntı bitene kadar tutun. Camlardan ve devrilebilecek eşyalardan uzak dur.", [18]),
    L("Dışarıdaysan binalardan, sokak lambalarından ve tellerden uzaklaş.", [18]),
    L("Şimdi sıra sende! Ailenle birlikte evde bir Çök, Kapan, Tutun tatbikatı yap ve bir acil durum çantası hazırla.", [18, 19]),
    L("Bir de deney: avuçlarını birbirine sıkıca bastır ve kaydırmaya çalış. Önce takılır, sonra aniden kayar. Fay da böyle davranır!", [5]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? USGS'ye göre büyüklüğü 10 ya da daha fazla olan bir deprem olamaz.", [20], f"Bunu biliyor muydun? {USG}'e göre büyüklüğü on ya da daha fazla olan bir deprem olamaz."),
    L("Hızlı soru! Hangi dalga daha hızlıdır: P mi, S mi?", [9], "Hızlı soru! Hangi dalga daha hızlıdır: Pe mi, Se mi?"),
    L("Düşün bakalım... Evet: P dalgası!", [9], "Düşün bakalım... Evet: Pe dalgası!"),
    L("Aklında şöyle kalsın: P, pistin şampiyonu. S, sonradan gelen!", [], "Aklında şöyle kalsın: Pe, pistin şampiyonu. Se, sonradan gelen!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de gidip acil durum çantama yedek pil koyayım!"),
])
S = e.S
S(3, {"type": "hook", "question": "Yer neden sarsılır?", "emoji": "🌍"}, ["🏔️", "〰️", "📈", "🧭"], ["", "NEDEN SARSILIR?", "YERİN DERİNLERİNE!"])
S(1, {"type": "spotlight", "title": "Titreşim modu", "emoji": "🤖", "chips": [{"label": "Ben de titrerim", "emoji": "📳"}, {"label": "Ama deprem değil!", "emoji": "😄"}, {"label": "Sessize alabilirsin", "emoji": "🔕"}]}, ["📳", "⚙️"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Deprem neden olur?", "Deprem dalgaları nasıl yayılır?", "Deprem sırasında ne yapmalıyız?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Dünya'nın katmanları", "emoji": "🌍", "chips": [{"label": "Katı kabuk", "emoji": "🪨"}, {"label": "Sıcak manto", "emoji": "🔥"}, {"label": "Sıvı dış çekirdek", "emoji": "💧"}, {"label": "Katı iç çekirdek", "emoji": "⚫"}]}, ["🧅", "🔬"], ["DÖRT KATMAN"])
S(3, {"type": "big-number", "value": "15", "label": "Yaklaşık bu kadar büyük tektonik levha", "sub": "Yılda yalnızca birkaç santimetre hareket ederler", "icon": "🧩"}, ["🌍", "🐌"], ["TEKTONİK LEVHA", "ÇOK YAVAŞ 🐌", "GÜNCELLEME DAHA HIZLI 😅"])
S(1, {"type": "diagram", "title": "Levhalar üç şekilde hareket eder", "layout": "flow", "nodes": [{"label": "Yaklaşır", "emoji": "🤜"}, {"label": "Uzaklaşır", "emoji": "↔️"}, {"label": "Yan yana kayar", "emoji": "↕️"}]}, ["🧩", "🌍"], ["ÜÇ HAREKET"])
S(3, {"type": "meter", "title": "Fayda gerilim birikiyor", "label": "Gerilim", "emoji": "🪨", "phases": [{"label": "Fay: kayaların kaydığı kırık", "level": 0.15, "emoji": "⚡"}, {"label": "Sürtünme tutar: gerilim birikir", "level": 0.55, "emoji": "✋"}, {"label": "Kayalar bükülür: enerji depolanır", "level": 0.92, "emoji": "📏"}], "note": NOTE}, ["⛰️", "🧱"], ["FAY", "SÜRTÜNME ✋", "ENERJİ DEPOLANIYOR"])
S(1, {"type": "big-number", "value": "Deprem!", "label": "Fay aniden kayar", "sub": "Biriken enerji bir anda serbest kalır", "icon": "💥"}, ["〰️", "🌍"], ["ENERJİ SERBEST!"])
S(1, {"type": "spotlight", "title": "Elastik geri sekme", "emoji": "↩️", "chips": [{"label": "Kayalar eski biçimine döner", "emoji": "📏"}, {"label": "Fayın iki yanı yer değiştirmiştir", "emoji": "↕️"}]}, ["🪨", "🧱"], ["GERİ SEKME ↩️"])
S(2, {"type": "comparison", "title": "Odak ve merkez üssü", "left": {"title": "Odak (hiposantr) ⬇️", "items": ["Depremin başladığı nokta", "Yerin içinde", "Kilometrelerce derinde olabilir"]}, "right": {"title": "Merkez üssü 📍", "items": ["Odağın tam üstü", "Yeryüzünde"]}}, ["🎯", "🗺️"], ["ODAK = HİPOSANTR", "MERKEZ ÜSSÜ 📍"])
S(1, {"type": "spotlight", "title": "Sismik dalgalar", "emoji": "🌊", "chips": [{"label": "Enerji her yöne yayılır", "emoji": "💫"}, {"label": "Sudaki halkalar gibi", "emoji": "🪨"}]}, ["〰️", "💧"], ["SİSMİK DALGA 〰️"])
S(2, {"type": "comparison", "title": "P ve S dalgaları", "left": {"title": "P dalgası 🥇", "items": ["Sıkıştırır ve gevşetir", "İlerleme yönünde", "Saniyede 5–7 km"]}, "right": {"title": "S dalgası 🥈", "items": ["İlerleme yönüne dik sallar", "Saniyede 3–4 km"]}}, ["〰️", "🏁"], ["P ve S", "P DAHA HIZLI 🥇"])
S(3, {"type": "diagram", "title": "Depremin yeri nasıl bulunur?", "layout": "flow", "nodes": [{"label": "Önce P: şimşek gibi", "emoji": "⚡"}, {"label": "Sonra S: gürültü gibi", "emoji": "🔊"}, {"label": "Hız farkı yeri gösterir", "emoji": "📍"}, {"label": "Sismometre ölçer", "emoji": "📈"}]}, ["⏱️", "🗺️"], ["ŞİMŞEK + GÜRÜLTÜ", "NEREDE? 📍", "SİSMOMETRE 📈"])
S(2, {"type": "spotlight", "title": "Büyüklük ve şiddet", "emoji": "📏", "chips": [{"label": "Büyüklük: logaritmik ölçek", "emoji": "🔢"}, {"label": "Bir birim artış = on kat genlik", "emoji": "📈"}, {"label": "Şiddet: bir yerde hissedilen sarsıntı", "emoji": "🏠"}, {"label": "Uzaklaştıkça genellikle azalır", "emoji": "↘️"}]}, ["📊", "🧮"], ["BÜYÜKLÜK: ON KAT", "ŞİDDET FARKLI"])
S(2, {"type": "big-number", "value": "Yüzlerce", "label": "deprem, her gün", "sub": "Ciddi hasar verebilecek olanlar: yılda yaklaşık 100", "icon": "🌍"}, ["📈", "🗓️"], ["HER GÜN!", "YILDA YAKLAŞIK YÜZ"])
S(1, {"type": "bullets", "title": "Artçı sarsıntılar", "items": ["Büyük depremden sonra gelir", "Haftalarca, aylarca, hatta yıllarca sürebilir"]}, ["〰️", "🗓️"], ["ARTÇILAR"])
S(2, {"type": "comparison", "title": "Deprem önceden bilinir mi?", "left": {"title": "Bilinemeyen ❌", "items": ["Günü ve saati", "Tam yeri", "Büyüklüğü"]}, "right": {"title": "Bilinen ✅", "items": ["Faylarda yine deprem olacağı", "Erken uyarı: başladıktan hemen sonra"]}}, ["🔮", "📡"], ["ÖNCEDEN BİLİNEMEZ", "ERKEN UYARI 📡"])
S(2, {"type": "diagram", "title": "Çök, Kapan, Tutun!", "layout": "flow", "nodes": [{"label": "ÇÖK: yere çök", "emoji": "⬇️"}, {"label": "KAPAN: sağlam masanın altına", "emoji": "🪑"}, {"label": "TUTUN: sarsıntı bitene kadar", "emoji": "✊"}, {"label": "Camlardan uzak dur", "emoji": "🪟"}]}, ["🛡️", "🏠"], ["HAZIRLIKLI OL!", "ÇÖK • KAPAN • TUTUN"])
S(1, {"type": "bullets", "title": "Dışarıdaysan", "items": ["Binalardan uzaklaş", "Sokak lambalarından uzaklaş", "Tellerden uzaklaş"], "tone": "caution"}, ["🏢", "💡"], ["AÇIK ALANA!"])
S(2, {"type": "spotlight", "title": "Sen de dene", "emoji": "🎒", "chips": [{"label": "Ailece tatbikat", "emoji": "👨‍👩‍👧"}, {"label": "Acil durum çantası", "emoji": "🎒"}, {"label": "Avuç deneyi: bastır ve kaydır", "emoji": "🤲"}, {"label": "Takılır… sonra aniden kayar!", "emoji": "💥"}]}, ["🔦", "📓"], ["TATBİKAT + ÇANTA 🎒", "AVUÇ DENEYİ 🤲"])
S(1, {"type": "big-number", "value": "10", "label": "Bu büyüklükte bir deprem olamaz", "sub": "USGS", "icon": "🚫"}, ["📏", "🌍"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Hangi dalga daha hızlı: P mi, S mi?", "emoji": "🤔"}, ["〰️", "🏁"], ["HIZLI SORU!", "P DALGASI ✅", "P: PİSTİN ŞAMPİYONU 🥇"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 7, "videoTitle": "Deprem nasıl olur?", "paperTitleTr": "Deprem nasıl olur?",
  "takeaways": ["Faylarda biriken gerilim aniden boşalınca deprem olur", "Enerji P ve S dalgalarıyla yayılır; sismometre ölçer", "Deprem önceden bilinemez: Çök, Kapan, Tutun!"],
  "description": "Yer neden sarsılır? Bu bölümde Dünya'nın katmanlarını, tektonik levhaları ve fayları; gerilimin nasıl biriktiğini ve aniden nasıl boşaldığını; odak ile merkez üssü arasındaki farkı, P ve S dalgalarını, sismometreyi, büyüklük ile şiddet arasındaki farkı keşfediyoruz. Deprem önceden bilinebilir mi, deprem anında ne yapmalıyız? Sonunda aile tatbikatı, avuç deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Tektonik levha", "meaning": "Dünya'nın en dış katmanını oluşturan, yavaşça hareket eden büyük parçalardan her biri."},
    {"term": "Fay", "meaning": "Kaya bloklarının birbirine göre kaydığı kırık."},
    {"term": "Gerilim", "meaning": "Kayaların üzerinde biriken, onları bükmeye ve kırmaya zorlayan kuvvet."},
    {"term": "Hiposantr", "meaning": "Depremin yerin içinde başladığı nokta; odak da denir."},
    {"term": "Merkez üssü", "meaning": "Odağın tam üstündeki yeryüzü noktası."},
    {"term": "Sismik dalga", "meaning": "Depremin enerjisini yerin içinde ve yüzeyinde taşıyan dalga."},
    {"term": "Sismometre", "meaning": "Yer sarsıntısını ölçen alet."},
    {"term": "Genlik", "meaning": "Bir dalganın yüksekliği."},
    {"term": "Artçı sarsıntı", "meaning": "Büyük bir depremden sonra aynı bölgede görülen depremler."}],
  "song": e.song("Yerin Altındaki Güç", [("🧩", "Levha"), ("🥇", "P dalgası"), ("🥈", "S dalgası"), ("📈", "Sismometre"), ("🎒", "Acil çanta")],
    ["Yer kabuğu parça parça, levha levha", "Yılda birkaç santim kayar usulca", "Sürtünme tutar, gerilim birikir", "Kayalar bükülür, enerji gizlenir"],
    ["Fay kayar, yer sarsılır!", "Dalgalar her yöne yayılır", "Önce P gelir, sonra S", "Sismometre yazar hepsini"],
    ["Odak derinde, üstünde merkez üssü", "Büyüklük bir artar, genlik on katı", "Günü bilinmez, hazırlık şart", "Çantanı hazırla, planını yap"],
    ["Fay kayar, yer sarsılır!", "Dalgalar her yöne yayılır", "Çök, kapan, tutun; sakin kal!", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
