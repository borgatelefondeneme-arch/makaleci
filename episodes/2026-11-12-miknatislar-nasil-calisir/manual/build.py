"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:miknatislar-nasil-calisir"
NG = "National Geographic Education — Magnetism"; NM = "NASA Science — Earth's Magnetosphere"; SP = "NASA Space Place — What Is an Aurora?"
NC = "NOAA NCEI — Wandering of the Geomagnetic Poles"; BG = "British Geological Survey — An Overview of the Earth's Magnetic Field"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Magnetism", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/magnetism/"},
    {"id": "k2", "title": "Earth's Magnetosphere", "publisher": "NASA", "url": "https://science.nasa.gov/science-research/earth-science/earths-magnetosphere/"},
    {"id": "k3", "title": "What Is an Aurora?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/aurora/en/"},
    {"id": "k4", "title": "Wandering of the Geomagnetic Poles", "publisher": "NOAA", "url": "https://www.ncei.noaa.gov/products/wandering-geomagnetic-poles"},
    {"id": "k5", "title": "An Overview of the Earth's Magnetic Field", "publisher": "Britanya Jeoloji Araştırmaları Kurumu", "url": "https://geomag.bgs.ac.uk/education/earthmag.html"}],
  "facts": [
    F(1, "Manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir; elektrik yüklerinin hareketinden kaynaklanır; manyetik alan, mıknatısın çevresinde manyetik kuvvetin etkili olduğu bölgedir.", "Magnetism is the force exerted by magnets when they attract or repel each other / Magnetism is caused by the motion of electric charges. / The magnetic field is the area around a magnet that has magnetic force.", NG),
    F(2, "Bütün mıknatısların kuzey ve güney kutbu vardır; zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.", "All magnets have north and south poles. / Opposite poles are attracted to each other, while the same poles repel each other.", NG),
    F(3, "Elektronlar topaç gibi dönerek atom çekirdeğinin çevresinde dolanır; bu hareket her elektronun mikroskobik bir mıknatıs gibi davranmasına yol açar.", "Spinning like tops, the electrons circle the nucleus, or core, of an atom. / Their movement generates an electric current and causes each electron to act like a microscopic magnet.", NG),
    F(4, "Demir, kobalt ve nikel gibi maddelerde elektronların çoğu aynı yönde döner; çoğu maddede eşit sayıda elektron zıt yönlerde döner ve manyetizmalarını birbirine sıfırlar; bu yüzden kumaş ya da kâğıt zayıf manyetik sayılır.", "In substances such as iron, cobalt, and nickel, most of the electrons spin in the same direction. / In most substances, equal numbers of electrons spin in opposite directions, which cancels out their magnetism. / That is why materials such as cloth or paper are said to be weakly magnetic.", NG),
    F(5, "Bir tel bobininden elektrik geçince manyetik alan oluşur; akım kesilince bobinin çevresindeki alan kaybolur.", "When electricity runs through a coil of wire, it produces a magnetic field. / The field around the coil will disappear, however, as soon as the electric current is turned off.", NG),
    F(6, "Dünya'nın manyetik alanı, sıvı dış çekirdekte kendi kendini besleyen bir dinamo süreciyle oluşur; yavaş hareket eden erimiş demirde akan elektrik akımları manyetik alanı üretir.", "The Earth's magnetic field is generated in the fluid outer core by a self-exciting dynamo process. / Electrical currents flowing in the slowly moving molten iron generate the magnetic field.", BG),
    F(7, "Jeomanyetik kutuplar Kuzey ve Güney Kutbu ile aynı değildir; mıknatısın kuzey ucu, güney manyetik yük taşıyan Kuzey Manyetik Kutbu'nu gösterir.", "The geomagnetic poles are not the same as the North and South Poles. / The north end of a magnet points toward the North Magnetic Pole, which holds a south magnetic charge.", NG),
    F(8, "Son ölçüme göre Kuzey Manyetik Kutbu yılda yaklaşık 55 kilometre hızla kuzey-kuzeybatıya doğru ilerliyor; Kanada Arktiği boyunca yavaşça sürükleniyor.", "The most recent survey determined that the Pole is moving approximately north-northwest at 55km per year. / the North Magnetic Pole, which is slowly drifting across the Canadian Arctic", NC, ["55"]),
    F(9, "Jeomanyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirdi; bu dönüşler yavaş ve düzensiz olur.", "the geomagnetic poles have reversed—changed into the opposite kind of pole—hundreds of times since Earth formed. / These reversals occur slowly and irregularly", NG + "; " + BG),
    F(10, "Manyetosfer, Güneş'ten saatte 1 milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır; Dünya'yı parçacıkların çoğundan korur.", "It deflects most of the solar material sweeping towards us from our star at 1 million miles per hour or more. / The magnetosphere protects Earth from most of the particles, but some leak through it and become trapped.", NM + "; " + NG, ["1"]),
    F(11, "Mars, manyetosferini yaklaşık 4,2 milyar yıl önce kaybetmiş bir gezegendir.", "Compare Earth to Mars – a planet that lost its magnetosphere about 4.2 billion years ago.", NM, ["4.2"]),
    F(12, "Parçacıklar atmosferdeki gazlarla etkileşir ve gökyüzünde güzel ışık gösterileri oluşur; oksijen yeşil ve kırmızı, azot mavi ve mor ışık verir; Kuzey Kutbu yakınında buna kuzey ışıkları denir.", "There, the particles interact with gases in our atmosphere resulting in beautiful displays of light in the sky. / Oxygen gives off green and red light. Nitrogen glows blue and purple. / If you're near the North Pole, it is called an aurora borealis or northern lights.", SP),
    F(13, "Pusulanın manyetik iğnesi Dünya'nın manyetik kutuplarıyla aynı hizaya gelir; insanlar yüzlerce yıldır yön bulmak için pusula kullanıyor.", "The magnetic needle of a compass lines up with Earth’s magnetic poles. / For hundreds of years, people have used magnetic compasses to navigate using Earth’s magnetic field.", NG),
    F(14, "Eski Yunanlılar ve Çinliler mıknatıs taşı denen doğal manyetik taşları biliyordu; Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslayabileceklerini keşfetti; pusulayla yön bulmaya ilişkin en eski yazılar 11. yüzyıla aittir.", "The ancient Greeks and Chinese knew about naturally magnetic stones called \"lodestones.\" / The Chinese discovered that they could make a needle magnetic by stroking it against a lodestone / The earliest writings about compass navigation are credited to the Chinese and date from 11th century A.D.", NG + "; " + BG, ["11"]),
    F(15, "Güvercinler, arılar ve somonlar gibi bazı hayvanlar Dünya'nın manyetik alanını algılayıp yön bulmak için kullanabilir; bilim insanları bunu nasıl yaptıklarından emin değil.", "Some animals, such as pigeons, bees, and salmon, can detect Earth's magnetic field and use it to navigate. / Scientists aren't sure how they do this", NG),
    F(16, "Son zamanların en şiddetli manyetik fırtınası Mart 1989'da oldu; Kanada'nın Quebec eyaletinde elektrik iletim sistemi 9 saatten uzun süre kapandı.", "The most severe magnetic storm in recent times occurred in March 1989 / the power transmission system in Quebec, Canada, was shut down for over 9 hours.", BG, ["1989", "9"]),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyografik"; NO = "Noa"; N = "Nasa"
e.sec("hook", [
    L("Gökyüzünde dalgalanan yeşil ve mor ışık perdeleri... Bu muhteşem gösterinin arkasında dev bir mıknatıs var: Dünya'nın kendisi!", [12]),
    L("Mıknatıslar nasıl çeker? Ve Dünya nasıl mıknatıs olur?"),
    L("Bugün görünmez bir kuvvetin izini sürüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Mıknatısı mıknatıs yapan nedir? Dünya'nın manyetik alanı nereden gelir? Ve bu alan bizi neden korur?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir.", [1], f"{NGs}'e göre manyetizma, mıknatısların birbirini çektiğinde ya da ittiğinde uyguladığı kuvvettir."),
    L("Her mıknatısın bir kuzey, bir de güney kutbu vardır. Zıt kutuplar birbirini çeker, aynı kutuplar birbirini iter.", [2]),
    L("Mıknatısın çevresinde, kuvvetinin etkili olduğu görünmez bir bölge vardır. Buna manyetik alan denir.", [1]),
    L("Peki bu kuvvet nereden gelir? Atomlara bakmamız gerek. Elektronlar atomun çekirdeği çevresinde topaç gibi dönerek dolanır.", [3]),
    L("Bu hareket yüzünden her elektron, minicik bir mıknatıs gibi davranır.", [3]),
    L("Çoğu maddede elektronların yarısı bir yöne, yarısı öbür yöne döner. Manyetizmaları birbirini sıfırlar. Kâğıdın, kumaşın mıknatısa yapışmamasının nedeni bu.", [4]),
    L("Ama demirde, kobaltta ve nikelde elektronların çoğu aynı yöne döner. Minik mıknatıslar aynı tarafa bakınca güçlü bir mıknatıs ortaya çıkar.", [4]),
    L("Ben de biraz demirden yapıldım. Buzdolabının yanından geçerken dikkatli olmam gerek!"),
])
e.sec("finding", [
    L("Elektrikle de mıknatıs yapabilirsin! Bir tel bobininden akım geçirince çevresinde manyetik alan oluşur.", [5]),
    L("Akımı kesince alan kaybolur. Buna elektromıknatıs denir: istediğinde açıp kapatabileceğin bir mıknatıs.", [5]),
    L("Şimdi en büyük mıknatısa geçelim: Dünya! Britanya Jeoloji Araştırmaları Kurumu'na göre manyetik alanımız, Dünya'nın sıvı dış çekirdeğinde oluşur.", [6]),
    L("Orada yavaşça hareket eden erimiş demirde elektrik akımları akar. Bu akımlar manyetik alanı üretir. Bu düzeneğe dinamo denir.", [6]),
    L("Yani Dünya, içinde dev bir elektromıknatıs taşıyor!", [5, 6]),
    L("Bir şaşırtıcı ayrıntı: manyetik kutuplar, haritadaki Kuzey ve Güney Kutbu ile aynı yerde değildir.", [7]),
    L("Üstelik yerinde de durmaz. ABD Ulusal Okyanus ve Atmosfer Dairesi NOAA'ya göre Kuzey Manyetik Kutbu, son ölçüme göre yılda yaklaşık 55 kilometre hızla ilerliyor.", [8], f"Üstelik yerinde de durmaz. A Be De Ulusal Okyanus ve Atmosfer Dairesi, {NO}'ya göre Kuzey Manyetik Kutbu, son ölçüme göre yılda yaklaşık elli beş kilometre hızla ilerliyor."),
    L("Hatta manyetik kutuplar Dünya oluştuğundan beri yüzlerce kez yer değiştirmiş: kuzey güney, güney kuzey olmuş! Bu değişim yavaş ve düzensiz olur.", [9]),
])
e.sec("importance", [
    L("Bu manyetik alan bizi korur. Dünya'yı saran bu koruyucu bölgeye manyetosfer denir.", [10]),
    L("NASA'ya göre Güneş'ten saatte 1 milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır.", [10], f"{N}'ya göre Güneş'ten saatte bir milyon mil ya da daha hızlı gelen maddenin çoğunu saptırır."),
    L("Karşılaştırma için Mars'a bak: Mars, manyetosferini yaklaşık 4,2 milyar yıl önce kaybetmiş.", [11], "Karşılaştırma için Mars'a bak: Mars, manyetosferini yaklaşık dört virgül iki milyar yıl önce kaybetmiş."),
    L("Bazı parçacıklar yine de içeri sızar ve atmosferdeki gazlarla etkileşir. İşte o ışık perdeleri böyle oluşur!", [10, 12]),
    L("Oksijen yeşil ve kırmızı, azot ise mavi ve mor ışık verir. Kuzey Kutbu yakınında bu gösteriye kuzey ışıkları denir.", [12]),
    L("Pusula da bu alan sayesinde çalışır: iğnesi, Dünya'nın manyetik kutuplarıyla aynı hizaya gelir.", [13]),
    L("Pusulanın hikâyesi eskidir. Eski Yunanlılar ve Çinliler, mıknatıs taşı denen doğal manyetik taşları biliyordu.", [14]),
    L("Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslamayı keşfetti. Pusulayla yön bulmaya dair en eski yazılar 11. yüzyıla ait.", [14], "Çinliler bir iğneyi mıknatıs taşına sürterek mıknatıslamayı keşfetti. Pusulayla yön bulmaya dair en eski yazılar on birinci yüzyıla ait."),
    L("Bazı hayvanların içinde de pusula var gibi: güvercinler, arılar ve somon balıkları manyetik alanı algılayıp yön bulabilir. Bilim insanları bunu nasıl yaptıklarından emin değil.", [15]),
    L("Benim içimde GPS var. Ama güvercinlerin kini daha az pil yiyor!"),
    L("Şimdi sıra sende! Masaya bir buzdolabı mıknatısı koy. Ataş, alüminyum folyo, kâğıt ve bozuk para gibi eşyaları teker teker yaklaştır.", [4]),
    L("Hangileri yapışıyor, hangileri yapışmıyor? Bir tabloya yaz. Bir uyarı: mıknatısları telefonlardan ve bilgisayarlardan uzak tut; küçük mıknatısları asla ağzına alma."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Mart 1989'daki güçlü bir manyetik fırtına, Kanada'nın Quebec eyaletinde elektrik sistemini 9 saatten uzun süre kapattı.", [16], "Bunu biliyor muydun? Mart bin dokuz yüz seksen dokuzdaki güçlü bir manyetik fırtına, Kanada'nın Kebek eyaletinde elektrik sistemini dokuz saatten uzun süre kapattı."),
    L("Hızlı soru! İki mıknatısın kuzey kutuplarını birbirine yaklaştırırsan ne olur?", [2]),
    L("Düşün bakalım... Evet: birbirlerini iterler!", [2]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de buzdolabından uzak durarak eve dönüyorum!"),
])
S = e.S
S(3, {"type": "hook", "question": "Mıknatıslar nasıl çalışır?", "emoji": "🧲"}, ["🌌", "🧭", "🌍", "✨"], ["", "GÖRÜNMEZ KUVVET", "İZİNİ SÜRÜYORUZ!"], fx="sparkle")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Mıknatısı mıknatıs yapan nedir?", "Dünya'nın manyetik alanı nereden gelir?", "Bu alan bizi neden korur?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "comparison", "title": "Kutuplar", "left": {"title": "Zıt kutuplar 🧲", "items": ["Kuzey + güney", "Birbirini çeker"]}, "right": {"title": "Aynı kutuplar 🚫", "items": ["Kuzey + kuzey", "Birbirini iter"]}}, ["🔴", "🔵"], ["MANYETİZMA", "ÇEKER • İTER", "MANYETİK ALAN"])
S(2, {"type": "spotlight", "title": "Atomun içinde", "emoji": "⚛️", "chips": [{"label": "Elektronlar topaç gibi döner", "emoji": "🌀"}, {"label": "Her elektron: minik mıknatıs", "emoji": "🧲"}]}, ["🔬", "✨"], ["ELEKTRONLAR", "MİNİK MIKNATIS"])
S(3, {"type": "comparison", "title": "Neden bazıları yapışır?", "left": {"title": "Kâğıt, kumaş 📄", "items": ["Elektronlar zıt yönlerde döner", "Manyetizma sıfırlanır"]}, "right": {"title": "Demir, kobalt, nikel 🔩", "items": ["Elektronların çoğu aynı yöne döner", "Güçlü mıknatıs"]}}, ["📎", "🤖"], ["SIFIRLANIR", "AYNI YÖN = GÜÇ", "BUZDOLABI TEHLİKESİ 😅"])
S(2, {"type": "diagram", "title": "Elektromıknatıs", "layout": "flow", "nodes": [{"label": "Tel bobini", "emoji": "🌀"}, {"label": "Akım geçer", "emoji": "⚡"}, {"label": "Manyetik alan", "emoji": "🧲"}, {"label": "Akım kesilir: alan kaybolur", "emoji": "🔌"}]}, ["🔋", "💡"], ["ELEKTRİK → MIKNATIS", "AÇ / KAPAT 🔌"], fx="flash")
S(3, {"type": "stages", "title": "Dünya'nın dinamosu", "rows": [{"label": "Kabuk", "emoji": "🪨"}, {"label": "Manto", "emoji": "🔥"}, {"label": "Dış çekirdek", "emoji": "🌀"}], "path": [0, 1, 2, 2, 2, 2, 2], "highlightRow": 2, "note": NOTE}, [], ["DIŞ ÇEKİRDEK", "DİNAMO 🌀", "DEV ELEKTROMIKNATIS!"])
S(3, {"type": "spotlight", "title": "Gezgin kutuplar", "emoji": "🧭", "chips": [{"label": "Haritadaki kutuplarla aynı değil", "emoji": "🗺️"}, {"label": "Yılda yaklaşık 55 km ilerliyor", "emoji": "🚶"}, {"label": "Yüzlerce kez yer değiştirdi", "emoji": "🔄"}, {"label": "Yavaş ve düzensiz", "emoji": "🐢"}]}, ["🌍", "❄️"], ["AYNI YERDE DEĞİL", "KUTUP YÜRÜYOR 🚶", "TERS DÖNÜŞ 🔄"])
S(2, {"type": "meter", "title": "Manyetosfer: Dünya'nın kalkanı", "label": "Koruma", "emoji": "🛡️", "phases": [{"label": "Güneş'ten gelen hızlı madde", "level": 0.35, "emoji": "☀️"}, {"label": "Çoğu saptırılır", "level": 0.92, "emoji": "🛡️"}], "note": NOTE}, ["🌍", "☀️"], ["MANYETOSFER 🛡️", "SAPTIRIR"])
S(1, {"type": "big-number", "value": "4,2 milyar", "unit": "yıl önce", "label": "Mars manyetosferini kaybetti", "sub": "NASA", "icon": "🔴"}, ["🪐", "🌍"], ["MARS'IN KALKANI YOK"])
S(2, {"type": "spotlight", "title": "Kuzey ışıkları", "emoji": "🌌", "chips": [{"label": "Sızan parçacıklar gazlara çarpar", "emoji": "💥"}, {"label": "Oksijen: yeşil ve kırmızı", "emoji": "🟢"}, {"label": "Azot: mavi ve mor", "emoji": "🟣"}]}, ["✨", "❄️"], ["IŞIK GÖSTERİSİ ✨", "OKSİJEN • AZOT"], fx="sparkle")
S(1, {"type": "big-number", "value": "Pusula", "label": "İğnesi manyetik kutuplarla hizalanır", "sub": "National Geographic", "icon": "🧭"}, ["🗺️", "⛵"], ["PUSULA 🧭"])
S(2, {"type": "diagram", "title": "Pusulanın hikâyesi", "layout": "flow", "nodes": [{"label": "Mıknatıs taşı", "emoji": "🪨"}, {"label": "İğneyi sürt", "emoji": "🪡"}, {"label": "İğne mıknatıslanır", "emoji": "🧲"}, {"label": "11. yüzyıl yazıları", "emoji": "📜"}]}, ["⛵", "🌏"], ["MIKNATIS TAŞI", "EN ESKİ YAZILAR 📜"])
S(2, {"type": "spotlight", "title": "Canlı pusulalar", "emoji": "🕊️", "chips": [{"label": "Güvercinler", "emoji": "🕊️"}, {"label": "Arılar", "emoji": "🐝"}, {"label": "Somonlar", "emoji": "🐟"}, {"label": "Nasıl? Henüz bilinmiyor", "emoji": "❓"}]}, ["🧭", "🤖"], ["CANLI PUSULALAR", "PİL YEMİYOR 🔋"])
S(2, {"type": "bullets", "title": "Sen de dene: ne yapışır?", "items": ["Buzdolabı mıknatısını masaya koy", "Ataş, folyo, kâğıt, bozuk para yaklaştır", "Sonuçları tabloya yaz", "Mıknatısları telefondan uzak tut; ağza alma ⚠️"]}, ["📎", "📓"], ["DENEY ZAMANI 🔬", "GÜVENLİK ⚠️"])
S(1, {"type": "big-number", "value": "9+", "unit": "saat", "label": "Mart 1989 manyetik fırtınasında Quebec'te elektrik kesintisi", "sub": "Britanya Jeoloji Araştırmaları Kurumu", "icon": "⚡"}, ["🔌", "🌌"], ["BUNU BİLİYOR MUYDUN?"], fx="flash")
S(2, {"type": "hook", "question": "İki kuzey kutbu yaklaşırsa ne olur?", "emoji": "🤔"}, ["🧲", "🧲"], ["HIZLI SORU!", "İTERLER ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 18, "videoTitle": "Mıknatıslar nasıl çalışır?", "paperTitleTr": "Mıknatıslar nasıl çalışır?",
  "theme": {"backdrop": "aurora", "actors": [{"kind": "walk", "emoji": "🐧", "every": 18, "size": 96}, {"kind": "walk", "emoji": "🐻‍❄️", "every": 29}, {"kind": "fly", "emoji": "🕊️", "every": 23}]},
  "takeaways": ["Zıt kutuplar çeker, aynı kutuplar iter", "Dünya'nın manyetik alanı erimiş demir çekirdekten gelir", "Manyetosfer bizi korur; kuzey ışıklarını oluşturur"],
  "description": "Mıknatıslar nasıl çeker, Dünya nasıl mıknatıs olur? Bu bölümde manyetizmayı, kutupları, elektronların minik mıknatıslar gibi davranmasını ve elektromıknatısı; Dünya'nın sıvı dış çekirdeğindeki dinamoyu, gezgin manyetik kutupları ve manyetosferi keşfediyoruz. Kuzey ışıkları nasıl oluşur, pusula nasıl çalışır? Sonunda ne yapışır deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Manyetizma", "meaning": "Mıknatısların birbirini çekmesini ya da itmesini sağlayan kuvvet."},
    {"term": "Manyetik alan", "meaning": "Mıknatısın çevresinde kuvvetinin etkili olduğu bölge."},
    {"term": "Elektron", "meaning": "Atomun çekirdeği çevresinde dolanan eksi yüklü minik parçacık."},
    {"term": "Elektromıknatıs", "meaning": "Telden elektrik geçirilerek yapılan, açılıp kapatılabilen mıknatıs."},
    {"term": "Dış çekirdek", "meaning": "Dünya'nın merkezine yakın, erimiş demirden oluşan sıvı katman."},
    {"term": "Manyetosfer", "meaning": "Dünya'nın manyetik alanının oluşturduğu koruyucu bölge."},
    {"term": "Kuzey ışıkları", "meaning": "Güneş'ten gelen parçacıkların atmosferdeki gazlara çarpmasıyla oluşan ışık gösterisi."},
    {"term": "Pusula", "meaning": "İğnesi Dünya'nın manyetik kutuplarına dönen yön bulma aracı."}],
  "song": e.song("Görünmez Kuvvet", [("🧲", "Mıknatıs"), ("🌍", "Dünya"), ("🧭", "Pusula"), ("🌌", "Kuzey ışıkları"), ("🕊️", "Güvercin")],
    ["Elektronlar döner topaç gibi", "Her biri minicik bir mıknatıs", "Demirde aynı yöne dönerler", "Güçlenir kuvvet, çeker durur"],
    ["Kuzey güneyi çeker, aynılar iter!", "Görünmez bir alan sarar her yeri", "Dünya'nın kalbinde erimiş demir", "Dev bir mıknatıs, dinamo döner"],
    ["Manyetosfer kalkan olur bize", "Güneş'in fırtınasını saptırır", "Sızan parçacıklar gökte parlar", "Yeşil, mor ışıklar dans eder"],
    ["Kuzey güneyi çeker, aynılar iter!", "Görünmez bir alan sarar her yeri", "Pusulan şaşmaz, yolunu bulur", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "chase", "emoji": "🧲", "emoji2": "📎", "every": 7, "size": 230}, {"kind": "walk", "emoji": "🐧", "every": 9}, {"kind": "fly", "emoji": "🕊️", "every": 10}, {"kind": "hop", "emoji": "🧭"}, {"kind": "hop", "emoji": "🌍"}])}
e.write(D, facts, script)
