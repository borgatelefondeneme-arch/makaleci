"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:volkanlar-nasil-patlar"
B1 = "British Geological Survey — Volcanoes"; B2 = "British Geological Survey — Types of volcano"; B3 = "British Geological Survey — Eruption styles"; B4 = "British Geological Survey — Volcanic hazards"
NG = "National Geographic Education — Volcanoes"; U1 = "USGS — About Volcanoes"; U2 = "USGS — Comprehensive monitoring provides timely warnings of volcano reawakening"; NASA = "NASA Space Place — What Is a Volcano?"
BGSU = "https://www.bgs.ac.uk/discovering-geology/earth-hazards/volcanoes/"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Volcanoes", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BGSU},
    {"id": "k2", "title": "Types of volcano", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BGSU + "how-volcanoes-form/"},
    {"id": "k3", "title": "Eruption styles", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BGSU + "eruption-styles/"},
    {"id": "k4", "title": "Volcanic hazards", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": BGSU + "volcanic-hazards/"},
    {"id": "k5", "title": "Volcanoes", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/volcanoes/"},
    {"id": "k6", "title": "About Volcanoes", "publisher": "USGS", "url": "https://www.usgs.gov/programs/VHP/about-volcanoes"},
    {"id": "k7", "title": "Comprehensive monitoring provides timely warnings of volcano reawakening", "publisher": "USGS", "url": "https://www.usgs.gov/programs/VHP/comprehensive-monitoring-provides-timely-warnings-volcano-reawakening"},
    {"id": "k8", "title": "What Is a Volcano?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/volcanoes2/en/"}],
  "facts": [
    F(1, "Volkanlar, lavın, tefranın (küçük kaya parçaları) ve buharın yeryüzüne püskürdüğü açıklıklardır.", "Volcanoes are openings, or vents where lava, tephra (small rocks), and steam erupt onto the Earth's surface.", U1),
    F(2, "Erimiş kaya yerin altındayken magma, yüzeye aktığında lav adını alır.", "\"lava\" when it's on the surface, \"magma\" when it's underground / Once it flows onto the surface the magma is known as lava.", NASA + "; " + NG),
    F(3, "Magma yerin onlarca mil altında oluşur; çevresindeki katı kayadan hafiftir (daha az yoğundur) ve bu yüzden yükselir.", "Originating many tens of miles beneath the ground, magma is lighter than surrounding solid rock. / Hot magma rises because it is less dense than the surrounding rock.", U1 + "; " + B2),
    F(4, "Etkin bir volkanın içinde magmanın toplandığı bir oda vardır; magma odasında basınç artar.", "Inside an active volcano is a chamber in which molten rock, called magma, collects. / Pressure builds up inside the magma chamber, causing the magma to move through channels in the rock", NG),
    F(5, "Magma, tektonik levhalar birbirinden uzaklaşırken yükselebilir; levhalar birbirine doğru ilerlerken kabuğun bir kısmı derine itilir, ısı ve basınç kabuğu eritir ve magma olarak yükselir; üçüncü yol sıcak noktalardır. Hawaii volkanları bir sıcak noktanın üstünde oluşur.", "Magma can rise when pieces of Earth's crust called tectonic plates slowly move away from each other. / When this happens, part of Earth's crust can be forced deep into its interior. / The high heat and pressure cause the crust to melt and rise as magma. / A final way that magma rises is over hot spots. / while Yellowstone and Hawaiian volcanoes form over a \"hot spot.\"", NASA + "; " + U1),
    F(6, "Volkanların birçoğu Büyük Okyanus'un çevresinde, 'Ateş Çemberi' denen kuşakta yer alır.", "Many of these are located around the Pacific Ocean in what is known as the \"Ring of Fire.\"", U1),
    F(7, "Magmada çok gaz hapsolursa basınç giderek artar; bu bir gazoz şişesine benzer: gaz sıvıda hapsolmuştur ve kaçmak ister.", "If a lot of gas is trapped within magma, pressure will build and build / It's a bit like a bottle of fizzy pop: gas is trapped in the liquid but if you shake the bottle the gas wants to escape.", B3),
    F(8, "Magmanın viskozitesi düşükse (akıcıysa) gaz kolayca kaçar; viskoz (yapışkan) magma yüzeye ulaştığında akamaz. Püskürmenin patlamalı mı efüzif mi olacağı büyük ölçüde magmadaki gaz miktarına bağlıdır.", "If a magma has low viscosity (it is runny), gas can escape easily / When the magma is viscous (or sticky), it can't flow when it reaches the surface / Whether an eruption is explosive or effusive largely depends upon the amount of gas in the magma.", B3),
    F(9, "Kalkan volkanlar neredeyse tümüyle akıcı lav akıntılarından oluşur; eğimleri 10°'den azdır. Mauna Kea ve Mauna Loa kalkan volkandır.", "Shield volcanoes are built almost entirely of fluid lava flows. / Shield volcanoes, on the other hand, have gentle slopes that are less than 10° / Mauna Kea and Mauna Loa are shield volcanoes.", U1 + "; " + B2, ["10"]),
    F(10, "Çok viskoz magmanın püskürmesi, eğimi yaklaşık 30–35° olan dik yamaçlı volkanlar oluşturur; bileşik volkanlara stratovolkan da denir; Fuji Dağı bir örnektir.", "tends to produce steep-sided volcanoes with slopes that are about 30–35° / Some of the Earth's grandest mountains are composite volcanoes—sometimes called stratovolcanoes. / Mount Fuji in Japan, Mount Cotopaxi in Ecuador, Mount Shasta in California", B2 + "; " + U1, ["30", "35"]),
    F(11, "Cüruf konileri en basit volkan türüdür.", "Cinder cones are the simplest type of volcano.", U1),
    F(12, "Kül, saç teli kalınlığında minik tefra parçalarıdır ve rüzgârla taşınabilir.", "Ash, tiny pieces of tephra the thickness of a strand of hair, may be carried by the wind", U1),
    F(13, "Bazalt lavlar tipik olarak 1100–1200°C sıcaklıkta püskürür.", "are typically erupted at temperatures of 1100–1200°C.", B4, ["1100", "1200"]),
    F(14, "Piroklastik akışlar, kaya parçaları ile gaz karışımından oluşan sıcak yoğunluk akıntılarıdır; volkanın yamaçlarından tipik olarak saatte 110 kilometre ya da daha hızlı iner.", "Pyroclastic flows are hot 'density currents' consisting of mixtures of rock debris and gas / They typically travel at 110 kilometres per hour or faster down the sides of the volcano.", B4, ["110"]),
    F(15, "Dünya'da 1500'den fazla etkin volkan vardır; her yıl yaklaşık 50–70 volkan püskürür.", "There are more than 1500 active volcanoes on Earth. / Around 50–70 volcanoes erupt every year.", B1, ["1500", "50", "70"]),
    F(16, "Mauna Loa dünyanın en büyük etkin volkanıdır.", "the world's largest active volcano, Mauna Loa", U1),
    F(17, "İzleme; depremler, yer hareketi ve volkanik gaz gibi birkaç tür gözlemi içermelidir; erken fark etmek insanlara hazırlanmak için en çok zamanı kazandırır.", "monitoring should include several types of observations (earthquakes, ground movement, volcanic gas / Early detection gives the maximum amount of time for people to prepare for an eruption.", U2),
    F(18, "Lav genellikle yavaş aktığı için doğrudan can kaybına yol açması nadirdir.", "In general, it is rare for lava to cause the direct loss of life, because it usually flows slowly", B4),
    F(19, "Surtsey püskürmesi yeni bir ada oluşturdu.", "This eruption formed a new island.", B3),
]}
e = Ep(); L = e.L
USG = "Yu Es Ci Es"
e.sec("hook", [
    L("Bir dağ düşün. İçinden, bin derecenin üstünde sıcaklıkta erimiş kaya fışkırıyor!", [13]),
    L("Bu kaya nereden geliyor? Ve neden bazı volkanlar sakince akarken bazıları patlıyor?"),
    L("Bugün bir volkanın içine iniyoruz!"),
])
e.sec("context", [
    L("Merak etme, ben sıcağa alışkınım. İşlemcim bazen fena ısınıyor!"),
    L("Üç sorumuz var. Magma nedir ve neden yükselir? Bir volkanı patlatan şey nedir? Ve bilim insanları püskürmeyi önceden nasıl anlar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Jeoloji Araştırmaları Kurumu, kısaca USGS'ye göre volkan; lavın, kaya parçalarının ve buharın yeryüzüne çıktığı bir açıklıktır.", [1], f"A Be De Jeoloji Araştırmaları Kurumu, kısaca {USG}'e göre volkan; lavın, kaya parçalarının ve buharın yeryüzüne çıktığı bir açıklıktır."),
    L("Önce iki kelimeyi ayıralım. Erimiş kaya yerin altındayken ona magma denir. Yüzeye çıktığında adı lav olur.", [2]),
    L("Magma, yerin çok derinlerinde oluşur. Çevresindeki katı kayadan daha hafiftir, yani daha az yoğundur. Bu yüzden yukarı doğru yükselir.", [3]),
    L("Tıpkı suyun dibine bastırdığın bir mantarın yüzeye çıkması gibi.", [3]),
    L("Yükselen magma, volkanın içindeki bir odada toplanır: magma odası. Burada basınç giderek artar.", [4]),
    L("Peki magma nerelerde yükselir? NASA'ya göre yer kabuğu, tektonik levha denen parçalardan oluşur ve bu levhalar yavaşça hareket eder.", [5], "Peki magma nerelerde yükselir? Nasa'ya göre yer kabuğu, tektonik levha denen parçalardan oluşur ve bu levhalar yavaşça hareket eder."),
    L("Levhalar birbirinden uzaklaşırken aradan magma yükselir. Birbirine doğru ilerlerken ise kabuğun bir kısmı derine itilir, orada erir ve magma olarak yükselir.", [5]),
    L("Üçüncü yol: sıcak noktalar. Hawaii'nin volkanları böyle bir sıcak noktanın üstünde oluşmuştur.", [5], "Üçüncü yol: sıcak noktalar. Havai'nin volkanları böyle bir sıcak noktanın üstünde oluşmuştur."),
    L("Volkanların birçoğu Büyük Okyanus'un çevresinde dizilir. Bu kuşağın adı: Ateş Çemberi.", [6]),
])
e.sec("finding", [
    L("Şimdi asıl soru: volkanı patlatan nedir? Cevap: gaz!", [7]),
    L("Britanya Jeoloji Araştırmaları Kurumu bunu bir gazoz şişesine benzetiyor: gaz sıvının içinde hapsolmuştur ve kaçmak ister.", [7]),
    L("Magmanın içinde çok gaz hapsolursa basınç artar, artar, artar...", [7]),
    L("Ben gazoz içemem ama o basıncı bilirim. Güncelleme yüklerken ben de böyle oluyorum!"),
    L("Burada önemli bir kelime var: viskozite. Viskozitesi düşük sıvı akıcıdır; yüksek olan ise bal gibi yapışkan ve ağırdır.", [8]),
    L("Magma akıcıysa gaz kolayca kaçar ve lav sakince akar. Buna efüzif püskürme denir.", [8]),
    L("Magma yapışkansa gaz içeride sıkışır. Basınç birikir ve sonunda patlamalı bir püskürme olur.", [7, 8]),
    L("Yani püskürmenin sakin mi patlamalı mı olacağını en çok magmadaki gaz miktarı belirler.", [8]),
    L("Volkanın biçimi de magmaya bağlıdır. Akıcı lav uzağa yayılır ve yayvan bir kalkan volkan oluşturur; eğimi 10 dereceden azdır.", [9], "Volkanın biçimi de magmaya bağlıdır. Akıcı lav uzağa yayılır ve yayvan bir kalkan volkan oluşturur; eğimi on dereceden azdır."),
    L("Yapışkan magma ise dik yamaçlı bir stratovolkan kurar; eğimi yaklaşık 30–35 derecedir. Japonya'daki Fuji Dağı böyledir.", [10], "Yapışkan magma ise dik yamaçlı bir stratovolkan kurar; eğimi yaklaşık otuz ile otuz beş derecedir. Japonya'daki Fuji Dağı böyledir."),
    L("Püskürmede kül de çıkar. Kül, saç teli kalınlığında minik kaya parçalarıdır ve rüzgârla taşınır.", [12]),
    L("En tehlikelisi piroklastik akıştır: kaya parçaları ile gazın sıcak karışımı. Yamaçtan saatte 110 kilometre ya da daha hızlı iner.", [14], "En tehlikelisi piroklastik akıştır: kaya parçaları ile gazın sıcak karışımı. Yamaçtan saatte yüz on kilometre ya da daha hızlı iner."),
])
e.sec("importance", [
    L("Dünya'da 1500'den fazla etkin volkan var ve her yıl yaklaşık 50–70 tanesi püskürüyor.", [15], "Dünya'da bin beş yüzden fazla etkin volkan var ve her yıl yaklaşık elli ile yetmiş tanesi püskürüyor."),
    L("Dünyanın en büyük etkin volkanı Hawaii'deki Mauna Loa'dır.", [16, 5], "Dünyanın en büyük etkin volkanı Havai'deki Mauna Loa'dır."),
    L("Bazalt lavın sıcaklığı 1100–1200 santigrat derecedir.", [13], "Bazalt lavın sıcaklığı bin yüz ile bin iki yüz santigrat derecedir."),
    L("Benim işlemcim bunun yanında buzdolabı sayılır!"),
    L("İyi haber: lav genellikle yavaş aktığı için doğrudan can kaybına nadiren yol açar.", [18]),
    L("Peki püskürme önceden anlaşılır mı? Volkanları inceleyen bilim insanlarına volkanolog denir.", [17]),
    L("USGS'ye göre üç şey izlenir: depremler, yerdeki hareketler ve volkandan çıkan gazlar.", [17], f"{USG}'e göre üç şey izlenir: depremler, yerdeki hareketler ve volkandan çıkan gazlar."),
    L("Değişikliği erken fark etmek, insanlara hazırlanmak için zaman kazandırır.", [17]),
    L("Volkanlar yeni kara da kurar: Surtsey adlı ada bir püskürmeyle doğdu.", [19], "Volkanlar yeni kara da kurar: Sürtsey adlı ada bir püskürmeyle doğdu."),
    L("Şimdi sıra sende! Kapalı bir maden suyu şişesine bak: içinde neredeyse hiç kabarcık görünmüyor."),
    L("Kapağı lavabonun üstünde, yavaşça aç. Kabarcıklar belirir: gaz kaçmaya çalışıyor! Tıpkı magmadaki gaz gibi.", [7]),
    L("Bir uyarı: şişeyi çalkalama ve yüzüne doğru tutma."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Volkanların hepsi aynı değildir: yayvan kalkan volkanlar, dik stratovolkanlar ve en basit tür olan cüruf konileri vardır.", [9, 10, 11]),
    L("Hızlı soru! Erimiş kaya yerin altındayken adı nedir: magma mı, lav mı?", [2]),
    L("Düşün bakalım... Evet: magma!", [2]),
    L("Yüzeye çıkınca adı lav olur. Ben yüzeye çıkınca yine Muma'yım!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben uçayım; burası ısınmaya başladı!"),
])
S = e.S
S(3, {"type": "hook", "question": "Bir volkanı patlatan nedir?", "emoji": "🌋"}, ["🔥", "🪨", "💨", "⛰️"], ["", "AKAR MI, PATLAR MI?", "VOLKANIN İÇİNE!"])
S(1, {"type": "spotlight", "title": "Sıcağa alışkın robot", "emoji": "🤖", "chips": [{"label": "İşlemci ısınıyor", "emoji": "🌡️"}, {"label": "Fan tam hız", "emoji": "🌀"}, {"label": "Lav kadar değil!", "emoji": "🔥"}]}, ["🧯", "⚙️"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Magma nedir ve neden yükselir?", "Bir volkanı patlatan şey nedir?", "Püskürme önceden nasıl anlaşılır?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Volkan nedir?", "emoji": "🌋", "chips": [{"label": "Yeryüzüne açılan açıklık", "emoji": "🕳️"}, {"label": "Lav", "emoji": "🔥"}, {"label": "Kaya parçaları", "emoji": "🪨"}, {"label": "Buhar", "emoji": "♨️"}]}, ["⛰️", "💨"], ["VOLKAN"])
S(1, {"type": "comparison", "title": "Magma mı, lav mı?", "left": {"title": "Magma ⬇️", "items": ["Erimiş kaya", "Yerin altında"]}, "right": {"title": "Lav ⬆️", "items": ["Erimiş kaya", "Yüzeyde"]}}, ["🔥", "🪨"], ["MAGMA ≠ LAV"])
S(3, {"type": "meter", "title": "Magma yükseliyor", "label": "Magma", "emoji": "🔥", "phases": [{"label": "Katı kayadan daha az yoğun", "level": 0.3, "emoji": "🪨"}, {"label": "Mantar gibi yükselir", "level": 0.6, "emoji": "⬆️"}, {"label": "Odada toplanır: basınç artar", "level": 0.95, "emoji": "💥"}], "note": NOTE}, ["🌍", "⛰️"], ["DAHA AZ YOĞUN", "YUKARI! ⬆️", "MAGMA ODASI"])
S(3, {"type": "diagram", "title": "Magma nerelerde yükselir?", "layout": "flow", "nodes": [{"label": "Tektonik levhalar hareket eder", "emoji": "🌍"}, {"label": "Uzaklaşan levhalar", "emoji": "↔️"}, {"label": "Yaklaşan levhalar: kabuk derine itilir", "emoji": "⤵️"}, {"label": "Sıcak nokta: Hawaii", "emoji": "🏝️"}]}, ["🗺️", "🔥"], ["TEKTONİK LEVHA", "UZAKLAŞ ↔️ YAKLAŞ", "SICAK NOKTA 🏝️"])
S(1, {"type": "big-number", "value": "Ateş Çemberi", "label": "Büyük Okyanus'un çevresindeki volkan kuşağı", "sub": "USGS", "icon": "🔥"}, ["🌊", "🌋"], ["ATEŞ ÇEMBERİ 🔥"])
S(2, {"type": "spotlight", "title": "Volkanı patlatan: gaz!", "emoji": "🥤", "chips": [{"label": "Gaz sıvıda hapsolur", "emoji": "🫧"}, {"label": "Kaçmak ister", "emoji": "💨"}, {"label": "Gazoz şişesi gibi", "emoji": "🍾"}]}, ["💥", "🫧"], ["CEVAP: GAZ!", "GAZOZ ŞİŞESİ 🥤"])
S(2, {"type": "meter", "title": "Basınç", "label": "Basınç", "emoji": "💨", "phases": [{"label": "Gaz hapsoldu: basınç artıyor", "level": 0.7, "emoji": "📈"}, {"label": "Güncelleme yükleniyor… 😅", "level": 0.98, "emoji": "🤖"}], "note": NOTE}, ["🫧", "⚠️"], ["ARTAR, ARTAR…", "BEN DE! 😅"])
S(3, {"type": "comparison", "title": "Viskozite", "left": {"title": "Akıcı magma 💧", "items": ["Düşük viskozite", "Gaz kolayca kaçar", "Efüzif: lav sakince akar"]}, "right": {"title": "Yapışkan magma 🍯", "items": ["Yüksek viskozite", "Gaz içeride sıkışır", "Patlamalı püskürme"]}}, ["🍯", "💧", "💥"], ["VİSKOZİTE", "EFÜZİF PÜSKÜRME", "PATLAMALI! 💥"])
S(1, {"type": "big-number", "value": "Gaz miktarı", "label": "Sakin mi, patlamalı mı? En çok bunu belirler", "sub": "Britanya Jeoloji Araştırmaları Kurumu", "icon": "🫧"}, ["💨", "🌋"], ["BELİRLEYEN: GAZ"])
S(2, {"type": "bar-chart", "title": "Yamaç eğimi", "unit": "°", "bars": [{"label": "Kalkan volkan", "value": 10, "display": "<10"}, {"label": "Stratovolkan", "value": 30, "display": "30–35", "highlight": True}]}, ["🛡️", "🗻"], ["KALKAN VOLKAN 🛡️", "STRATOVOLKAN 🗻"])
S(2, {"type": "spotlight", "title": "Püskürmede neler çıkar?", "emoji": "💥", "chips": [{"label": "Kül: saç teli kalınlığında kaya", "emoji": "🌫️"}, {"label": "Rüzgârla taşınır", "emoji": "🌬️"}, {"label": "Piroklastik akış: sıcak kaya + gaz", "emoji": "🔥"}, {"label": "Saatte 110 km ya da daha hızlı", "emoji": "⚡"}]}, ["🌋", "🪨"], ["KÜL", "PİROKLASTİK AKIŞ ⚠️"])
S(1, {"type": "big-number", "value": "1500+", "label": "Dünya'daki etkin volkan sayısı", "sub": "Her yıl yaklaşık 50–70 tanesi püskürür", "icon": "🌍"}, ["🌋", "🗺️"], ["ETKİN VOLKANLAR"])
S(1, {"type": "spotlight", "title": "Mauna Loa", "emoji": "🏝️", "chips": [{"label": "Hawaii'de", "emoji": "📍"}, {"label": "En büyük etkin volkan", "emoji": "🏆"}, {"label": "Bir kalkan volkan", "emoji": "🛡️"}]}, ["🌊", "🌋"], ["EN BÜYÜK 🏆"], extra=[9])
S(2, {"type": "big-number", "value": "1100–1200", "unit": "°C", "label": "Bazalt lavın sıcaklığı", "sub": "Britanya Jeoloji Araştırmaları Kurumu", "icon": "🌡️"}, ["🔥", "🧊"], ["BAZALT LAV", "İŞLEMCİM = BUZDOLABI 🧊"])
S(1, {"type": "bullets", "title": "İyi haber", "items": ["Lav genellikle yavaş akar", "Doğrudan can kaybına nadiren yol açar"]}, ["🐢", "🔥"], ["LAV YAVAŞTIR 🐢"])
S(3, {"type": "diagram", "title": "Volkanologlar neyi izler?", "layout": "flow", "nodes": [{"label": "Depremler", "emoji": "📈"}, {"label": "Yer hareketleri", "emoji": "📡"}, {"label": "Gazlar", "emoji": "💨"}, {"label": "Erken uyarı", "emoji": "⏰"}]}, ["🧑‍🔬", "🛰️"], ["VOLKANOLOG", "ÜÇ İPUCU", "ERKEN UYARI ⏰"])
S(1, {"type": "spotlight", "title": "Surtsey", "emoji": "🏝️", "chips": [{"label": "Bir püskürmeyle doğdu", "emoji": "🌋"}, {"label": "Yepyeni bir ada", "emoji": "✨"}, {"label": "Volkanlar kara da kurar", "emoji": "🧱"}]}, ["🌊", "🐦"], ["YENİ ADA! 🏝️"])
S(3, {"type": "bullets", "title": "Sen de dene: şişedeki gaz 🔬", "items": ["Kapalı şişeye bak: kabarcık yok gibi", "Kapağı lavabonun üstünde, yavaşça aç", "Kabarcıklar belirir: gaz kaçıyor!", "Çalkalama, yüzüne tutma ⚠️"]}, ["🫧", "🚰"], ["DENEY ZAMANI 🔬", "GAZ KAÇIYOR! 🫧", "ÇALKALAMA ⚠️"])
S(1, {"type": "spotlight", "title": "Volkan türleri", "emoji": "🌋", "chips": [{"label": "Kalkan volkan: yayvan", "emoji": "🛡️"}, {"label": "Stratovolkan: dik", "emoji": "🗻"}, {"label": "Cüruf konisi: en basit tür", "emoji": "🔺"}]}, ["⛰️", "🔥"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Yerin altındaki erimiş kaya: magma mı, lav mı?", "emoji": "🤔"}, ["🔥", "🌋"], ["HIZLI SORU!", "MAGMA ✅", ""])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 5, "videoTitle": "Volkanlar nasıl patlar?", "paperTitleTr": "Volkanlar nasıl patlar?",
  "takeaways": ["Magma katı kayadan daha az yoğundur, bu yüzden yükselir", "Püskürmeyi magmadaki gaz ve viskozite belirler", "Volkanologlar depremleri, yer hareketini ve gazları izler"],
  "description": "Bir volkanı patlatan nedir? Bu bölümde magma ile lav arasındaki farkı, magmanın neden yükseldiğini, tektonik levhaları ve sıcak noktaları; gazın ve viskozitenin püskürmeyi nasıl belirlediğini keşfediyoruz. Kalkan volkan ile stratovolkan arasındaki fark nedir, piroklastik akış nedir, volkanologlar püskürmeyi önceden nasıl anlar? Sonunda şişedeki gaz deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Magma", "meaning": "Yerin altındaki erimiş kaya. Yüzeye çıkınca lav adını alır."},
    {"term": "Magma odası", "meaning": "Volkanın içinde magmanın toplandığı boşluk."},
    {"term": "Tektonik levha", "meaning": "Yer kabuğunu oluşturan, yavaşça hareket eden dev parçalardan her biri."},
    {"term": "Viskozite", "meaning": "Bir sıvının akmaya karşı direnci; bal yüksek, su düşük viskozitelidir."},
    {"term": "Efüzif püskürme", "meaning": "Lavın patlamadan, sakince aktığı püskürme."},
    {"term": "Stratovolkan", "meaning": "Dik yamaçlı, katmanlı volkan."},
    {"term": "Piroklastik akış", "meaning": "Yamaçtan hızla inen, sıcak kaya parçaları ve gaz karışımı."},
    {"term": "Volkanolog", "meaning": "Volkanları inceleyen bilim insanı."}],
  "song": e.song("Dağın İçindeki Ateş", [("🌋", "Volkan"), ("🔥", "Magma"), ("🫧", "Gaz"), ("🌫️", "Kül"), ("📡", "Volkanolog")],
    ["Yerin derininde erimiş kaya", "Hafiftir taştan, yükselir yukarı", "Magma odasında toplanır durur", "İçindeki gaz basıncı kurar"],
    ["Magma yerde, lav yüzeyde!", "Gaz sıkışırsa dağ gürler", "Akıcıysa sakince akar", "Yapışkansa patlar, patlar!"],
    ["Levhalar ayrılır, magma çıkar", "Kalkan volkan yayvan, strato dik durur", "Kül rüzgârla uzağa uçar", "Volkanolog depremi, gazı ölçer"],
    ["Magma yerde, lav yüzeyde!", "Gaz sıkışırsa dağ gürler", "Bilim izler, erken uyarır", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
