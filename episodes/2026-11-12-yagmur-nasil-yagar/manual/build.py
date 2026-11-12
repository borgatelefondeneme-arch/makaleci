"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:yagmur-nasil-yagar"
WC = "USGS Water Science School — Water cycle"; CO = "USGS Water Science School — Condensation and the Water Cycle"; PR = "USGS Water Science School — Precipitation and the Water Cycle"
EV = "USGS Water Science School — Evaporation and the Water Cycle"; HM = "USGS Water Science School — How Much Water is There on Earth?"
NG = "National Geographic Education — Water Cycle"; NO = "NOAA — The water cycle"
U = "https://www.usgs.gov/special-topics/water-science-school/science/"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Water cycle", "publisher": "USGS", "url": U + "water-cycle"},
    {"id": "k2", "title": "Condensation and the Water Cycle", "publisher": "USGS", "url": U + "condensation-and-water-cycle"},
    {"id": "k3", "title": "Precipitation and the Water Cycle", "publisher": "USGS", "url": U + "precipitation-and-water-cycle"},
    {"id": "k4", "title": "Evaporation and the Water Cycle", "publisher": "USGS", "url": U + "evaporation-and-water-cycle"},
    {"id": "k5", "title": "How Much Water is There on Earth?", "publisher": "USGS", "url": U + "how-much-water-there-earth"},
    {"id": "k6", "title": "Water Cycle", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/water-cycle/"},
    {"id": "k7", "title": "The water cycle", "publisher": "NOAA", "url": "https://www.noaa.gov/education/resource-collections/freshwater/water-cycle"}],
  "facts": [
    F(1, "Su döngüsü, suyun Dünya'da nerede olduğunu ve nasıl hareket ettiğini anlatır; su hiçbir zaman yerinde durmaz; suyun sürekli hareketini Güneş'in enerjisi ve kütle çekimi sağlar.", "The water cycle describes where water is on Earth and how it moves. / Water is never sitting still. / Energy from the sun and the force of gravity drive the continual movement of water between pools.", WC + "; " + HM),
    F(2, "Buharlaşma, sıvı suyu gaz hâlindeki suya (su buharına) çeviren süreçtir. Atmosferdeki nemin çoğu (yaklaşık %90) okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir; gerisi bitki terlemesinden ve çok az miktarda süblimleşmeden gelir.", "Evaporation is the process that changes liquid water to gaseous water (water vapor). / Most of the moisture in the atmosphere (about 90%) came from water evaporating from oceans, seas, lakes, and rivers. / The rest of the moisture in the atmosphere came from plant transpiration and (a very small amount) from sublimation.", EV, ["90"]),
    F(3, "Terleme: sıvı su bitkilerin yapraklarından buharlaşır.", "Liquid water evaporates from the leaves of plants in a process called transpiration.", NO),
    F(4, "Bulutlar, su buharı içeren hava yükselip soğuduğu için oluşur; su molekülleri havadaki minik toz, tuz ve duman parçacıklarıyla birleşir. Yoğuşma bulutların oluşumundan sorumludur.", "Clouds form in the atmosphere because air containing water vapor rises and cools. / water molecules will combine with tiny particles of dust, salt, and smoke in the air / Condensation is crucial to the water cycle because it is responsible for the formation of clouds.", CO),
    F(5, "Bulut damlacıkları yağış olarak düşemeyecek kadar küçüktür ama görünür bulutlar oluşturacak kadar büyüktür; bulutu oluşturan yükselen hava onu havada tutar; bir bulut tonlarca ağırlıkta olsa da düşmez.", "These droplets are way too small to fall as precipitation, but they are large enough to form visible clouds. / the rising air responsible for its formation keeps the cloud floating in the air / Even though a cloud weighs tons, it doesn’t fall on you", PR + "; " + CO),
    F(6, "Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir; yeterince çarpışma olur ve damlanın düşme hızı bulutun yükselen hava hızını aşarsa damla düşer.", "millions of cloud droplets are required to produce a single raindrop. / If enough collisions occur to produce a droplet with a fall velocity which exceeds the cloud updraft speed", PR),
    F(7, "Yarıçapı 1 milimetreden küçük yağmur damlaları top gibi küreseldir; yaklaşık 2–3 milimetre çapta alt kısım oldukça düzdür: hamburger ekmeği gibi.", "Small raindrops, those with a radius of less than 1 millimeter (mm), are spherical, like a round ball. / at about 2-3 mm in diameter the bottom is quite flat with an indention in the middle - much like a hamburger bun.", PR, ["1", "2", "3"]),
    F(8, "Yağış, bulutlardan yağmur, donan yağmur, sulu kar, kar ya da dolu biçiminde bırakılan sudur.", "Precipitation is water released from clouds in the form of rain, freezing rain, sleet, snow, or hail.", WC),
    F(9, "Su, süzülme ve yeraltı suyu beslenmesiyle toprağa girer; yeraltı suyu akiferlerde akar; nehirlere, okyanusa ve kaynaklara boşalarak yüzeye dönebilir. Suyun bir kısmı toprağa sızar ve yeraltı suyu olarak tutulur.", "Water moves into the ground through infiltration and groundwater recharge. / Underground, groundwater flows within aquifers. / Groundwater can return to the surface through natural discharge into rivers, the ocean, and from springs. / Some of it seeps into the soil where it is held underground as groundwater.", WC + "; " + NG),
    F(10, "Buharlaşan bir su molekülü havada yaklaşık 10 gün kalır.", "Once evaporated, a water molecule spends about 10 days in the air.", EV, ["10"]),
    F(11, "Okyanuslar Dünya'daki suyun yaklaşık %97'sini tutar; tatlı su Dünya'daki suyun %2,5'idir; tatlı suyun yaklaşık %68'i donmuş hâldedir; yaklaşık %30'u yer altındadır.", "The oceans hold about 97% of the water on Earth. / Freshwater makes up 2.5% of Earth’s water. / The water frozen in these pools accounts for approximately 68% of freshwater. / This liquid water is below ground and accounts for approximately 30% of freshwater.", NG + "; " + NO, ["97", "2.5", "68", "30"]),
    F(12, "Dünya'daki suyun çok küçük bir bölümü, yalnızca %0,001'i, atmosferde su buharı olarak bulunur.", "A tiny fraction—just 0.001%—exists in Earth’s atmosphere as water vapor.", NG, ["0.001"]),
    F(13, "Dünya'nın su döngüsü yaklaşık 3,8 milyar yıl önce, soğuyan Dünya'ya yağmur yağıp okyanuslar oluştuğunda başladı.", "Earth’s water cycle began about 3.8 billion years ago when rain fell on a cooling Earth, forming the oceans.", NG, ["3.8"]),
    F(14, "Su Dünya'daki yaşam için vazgeçilmezdir; su, döngünün her bölümünde insanların kullanımına uygun değildir.", "Water is essential to life on Earth. / Water isn’t available for people to use in every part of the cycle", NO),
    F(15, "Süblimleşmede buz ya da kar gibi katı su, sıvılaşmadan doğrudan su buharına dönüşebilir.", "In a process called sublimation, solid water, such as ice or snow, can transform directly into water vapor without first becoming a liquid.", NG),
]}
e = Ep(); L = e.L
USG = "Yu Es Ci Es"; NGs = "Neşınıl Ciyografik"
e.sec("hook", [
    L("Başına düşen bir yağmur damlası, kısa süre önce bir okyanusun yüzeyinde olabilirdi!", [10]),
    L("Su gökyüzüne nasıl çıkıyor? Ve bulut düşmezken yağmur neden düşüyor?"),
    L("Bugün bir su damlasının peşine takılıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Su gökyüzüne nasıl çıkar? Bulut nasıl oluşur? Ve yağmur damlası nasıl düşer?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Jeoloji Araştırmaları Kurumu USGS'ye göre su hiçbir zaman yerinde durmaz. Suyun Dünya'daki bu bitmeyen yolculuğuna su döngüsü denir.", [1], f"A Be De Jeoloji Araştırmaları Kurumu, {USG}'e göre su hiçbir zaman yerinde durmaz. Suyun Dünya'daki bu bitmeyen yolculuğuna su döngüsü denir."),
    L("Bu yolculuğun iki motoru var: Güneş'in enerjisi ve kütle çekimi.", [1]),
    L("İlk adım buharlaşma: sıvı su, su buharı denen gaza dönüşür.", [2]),
    L("Atmosferdeki nemin yaklaşık %90'ı okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir.", [2], "Atmosferdeki nemin yaklaşık yüzde doksanı okyanuslardan, denizlerden, göllerden ve nehirlerden buharlaşan sudan gelir."),
    L("Gerisinin çoğu bitkilerden gelir: su, yapraklardan buharlaşır. Buna terleme denir.", [2, 3]),
    L("Buz ve kar da sıvılaşmadan doğrudan buhara dönüşebilir. Bunun adı süblimleşme.", [15]),
    L("İkinci adım yoğuşma. Su buharı taşıyan hava yükselir ve soğur.", [4]),
    L("Su buharı, havadaki minik toz, tuz ve duman parçacıklarının üstünde minicik damlacıklara dönüşür. İşte bulut!", [4]),
    L("Yani her bulutun içinde biraz toz var. Temizlik robotu kuzenim bunu duymasın!"),
])
e.sec("finding", [
    L("Peki bulut neden düşmez? USGS'ye göre bir bulut tonlarca ağırlıkta olabilir. Ama onu oluşturan yükselen hava, bulutu havada tutar.", [5], f"Peki bulut neden düşmez? {USG}'e göre bir bulut tonlarca ağırlıkta olabilir. Ama onu oluşturan yükselen hava, bulutu havada tutar."),
    L("Bulut damlacıkları da yağış olarak düşemeyecek kadar küçüktür.", [5]),
    L("Yağmur için damlacıkların çarpışıp birleşmesi gerekir. Tek bir yağmur damlası için milyonlarca bulut damlacığı gerekir!", [6]),
    L("Damla yeterince büyüyünce, yükselen havayı yenip düşmeye başlar. Üçüncü adım: yağış.", [6]),
    L("Yağış yalnızca yağmur değildir: kar, dolu ve sulu kar da birer yağıştır.", [8]),
    L("Bir sürpriz: yağmur damlası gözyaşı biçiminde değildir! Yarıçapı 1 milimetreden küçük damlalar top gibi yuvarlaktır.", [7], "Bir sürpriz: yağmur damlası gözyaşı biçiminde değildir! Yarıçapı bir milimetreden küçük damlalar top gibi yuvarlaktır."),
    L("Çapı 2–3 milimetre olanların ise altı düzleşir; tıpkı bir hamburger ekmeği gibi.", [7], "Çapı iki üç milimetre olanların ise altı düzleşir; tıpkı bir hamburger ekmeği gibi."),
    L("Gökten hamburger ekmeği yağıyor! Buna acıkmayan tek kişi ben olabilirim."),
    L("Yere düşen su ne olur? Bir kısmı nehirlerle akar, bir kısmı toprağa süzülür ve yeraltı suyu olur.", [9]),
])
e.sec("importance", [
    L("Yeraltı suyu, akifer denen yer altı katmanlarında akar; kaynaklardan, nehirlerden ya da doğrudan okyanusa geri döner.", [9]),
    L("Sonra her şey yeniden başlar: buharlaşma, yoğuşma, yağış.", [1]),
    L("Bir su molekülü buharlaştıktan sonra havada yaklaşık 10 gün kalır.", [10], "Bir su molekülü buharlaştıktan sonra havada yaklaşık on gün kalır."),
    L("National Geographic'e göre bu döngü yaklaşık 3,8 milyar yıl önce başladı: soğuyan Dünya'ya yağmurlar yağdı ve okyanuslar oluştu.", [13], f"{NGs}'e göre bu döngü yaklaşık üç virgül sekiz milyar yıl önce başladı: soğuyan Dünya'ya yağmurlar yağdı ve okyanuslar oluştu."),
    L("Dünya'daki suyun yaklaşık %97'si okyanuslardadır. Tatlı su, toplamın yalnızca %2,5'i kadardır.", [11], "Dünya'daki suyun yaklaşık yüzde doksan yedisi okyanuslardadır. Tatlı su, toplamın yalnızca yüzde iki buçuğu kadardır."),
    L("Üstelik tatlı suyun yaklaşık %68'i donmuş hâldedir; yaklaşık %30'u da yer altındadır.", [11], "Üstelik tatlı suyun yaklaşık yüzde altmış sekizi donmuş hâldedir; yaklaşık yüzde otuzu da yer altındadır."),
    L("NOAA'ya göre su yaşam için vazgeçilmezdir; ama döngünün her aşamasında insanların kullanımına uygun değildir. Bu yüzden suyu boşa harcamamak gerekir.", [14], "Noa'ya göre su yaşam için vazgeçilmezdir; ama döngünün her aşamasında insanların kullanımına uygun değildir. Bu yüzden suyu boşa harcamamak gerekir."),
    L("Ben bu konuda örnek bir vatandaşım: yıkanmam, silinirim!"),
    L("Şimdi sıra sende! Bir kâseye biraz ılık su koy, üstünü streç filmle kapat ve güneşli bir pencerenin önüne bırak."),
    L("Bir süre sonra filmin altında damlacıklar görürsün: buharlaşma ve yoğuşma, kâsenin içinde!", [2, 4]),
    L("Sıcak su kullanmak istersen mutlaka bir büyüğünden yardım iste."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Atmosferde su buharı olarak bulunan su, Dünya'daki bütün suyun yalnızca %0,001'i kadardır.", [12], "Bunu biliyor muydun? Atmosferde su buharı olarak bulunan su, Dünya'daki bütün suyun yalnızca yüz binde biri kadardır."),
    L("Hızlı soru! Su buharının soğuyup minik damlacıklara dönüşmesine ne denir?", [4]),
    L("Düşün bakalım... Evet: yoğuşma!", [4]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de şemsiyemi alıp gidiyorum; ıslanmak bana göre değil!"),
])
S = e.S
S(3, {"type": "hook", "question": "Yağmur nasıl yağar?", "emoji": "🌧️"}, ["☔", "💧", "☁️", "🌊"], ["", "BULUT NEDEN DÜŞMEZ?", "DAMLANIN PEŞİNDE!"], fx="rain")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Su gökyüzüne nasıl çıkar?", "Bulut nasıl oluşur?", "Yağmur damlası nasıl düşer?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Su döngüsü", "emoji": "💧", "chips": [{"label": "Su hiç yerinde durmaz", "emoji": "🔄"}, {"label": "Motor: Güneş'in enerjisi", "emoji": "☀️"}, {"label": "Motor: kütle çekimi", "emoji": "⬇️"}]}, ["🌊", "☁️"], ["SU DÖNGÜSÜ 🔄", "İKİ MOTOR"])
S(3, {"type": "diagram", "title": "Birinci adım: buharlaşma", "layout": "flow", "nodes": [{"label": "Sıvı su", "emoji": "💧"}, {"label": "Su buharı", "emoji": "♨️"}, {"label": "Yaklaşık %90: okyanus, deniz, göl, nehir", "emoji": "🌊"}, {"label": "Bitkiler: terleme", "emoji": "🌿"}]}, ["☀️", "🌡️"], ["BUHARLAŞMA ♨️", "ÇOĞU DENİZLERDEN", "TERLEME 🌿"])
S(1, {"type": "big-number", "value": "Süblimleşme", "label": "Buz ve kar doğrudan buhara dönüşür", "sub": "Sıvılaşmadan!", "icon": "❄️"}, ["🧊", "♨️"], ["SÜBLİMLEŞME ❄️"])
S(3, {"type": "diagram", "title": "İkinci adım: yoğuşma", "layout": "flow", "nodes": [{"label": "Hava yükselir ve soğur", "emoji": "⬆️"}, {"label": "Toz, tuz, duman parçacıkları", "emoji": "🌫️"}, {"label": "Minicik damlacıklar", "emoji": "💧"}, {"label": "Bulut", "emoji": "☁️"}]}, ["🌬️", "🧹"], ["YOĞUŞMA", "İŞTE BULUT! ☁️", "TOZ VAR 🧹"])
S(2, {"type": "comparison", "title": "Bulut neden düşmez?", "left": {"title": "Bulut ☁️", "items": ["Tonlarca ağırlıkta olabilir", "Damlacıkları çok küçük"]}, "right": {"title": "Yükselen hava ⬆️", "items": ["Bulutu havada tutar"]}}, ["⚖️", "🎈"], ["TONLARCA AMA DÜŞMEZ", "ÇOK KÜÇÜK DAMLACIK"])
S(2, {"type": "meter", "title": "Damla büyüyor", "label": "Yağmur damlası", "emoji": "💧", "phases": [{"label": "Milyonlarca damlacık birleşir", "level": 0.6, "emoji": "🤝"}, {"label": "Büyür ve düşer: yağış", "level": 0.98, "emoji": "🌧️"}], "note": NOTE}, ["☁️", "☔"], ["MİLYONLARCA DAMLACIK", "YAĞIŞ! 🌧️"], fx="rain")
S(1, {"type": "spotlight", "title": "Yağış türleri", "emoji": "🌧️", "chips": [{"label": "Yağmur", "emoji": "💧"}, {"label": "Kar", "emoji": "❄️"}, {"label": "Dolu", "emoji": "⚪"}, {"label": "Sulu kar", "emoji": "🌨️"}]}, ["☃️", "☔"], ["YAĞIŞ TÜRLERİ"], fx="flash")
S(3, {"type": "comparison", "title": "Damlanın gerçek biçimi", "left": {"title": "Küçük damla ⚪", "items": ["Yarıçap 1 mm'den küçük", "Top gibi yuvarlak"]}, "right": {"title": "Büyük damla 🍔", "items": ["Çap 2–3 mm", "Altı düz", "Hamburger ekmeği gibi"]}}, ["💧", "🍔"], ["GÖZYAŞI DEĞİL!", "HAMBURGER EKMEĞİ 🍔", "ACIKMADIM 🤖"], fx="rain")
S(1, {"type": "diagram", "title": "Yere düşen su", "layout": "flow", "nodes": [{"label": "Yağış", "emoji": "🌧️"}, {"label": "Nehirlerle akar", "emoji": "🏞️"}, {"label": "Toprağa süzülür", "emoji": "⬇️"}, {"label": "Yeraltı suyu", "emoji": "💧"}]}, ["🌱", "🪨"], ["YERALTI SUYU"])
S(2, {"type": "spotlight", "title": "Döngü tamamlanıyor", "emoji": "🔄", "chips": [{"label": "Akifer: yer altı katmanı", "emoji": "🪨"}, {"label": "Kaynaklar ve nehirler", "emoji": "🏞️"}, {"label": "Okyanusa dönüş", "emoji": "🌊"}, {"label": "Yeniden: buharlaşma", "emoji": "♨️"}]}, ["💧", "☀️"], ["AKİFER", "YENİDEN BAŞLAR 🔄"])
S(1, {"type": "big-number", "value": "10", "unit": "gün", "label": "Bir su molekülünün havada kaldığı süre", "sub": "Yaklaşık • USGS", "icon": "☁️"}, ["💧", "🗓️"], ["HAVADA TATİL ☁️"])
S(1, {"type": "spotlight", "title": "Çok eski bir döngü", "emoji": "🌍", "chips": [{"label": "Yaklaşık 3,8 milyar yıl önce başladı", "emoji": "⏳"}, {"label": "Soğuyan Dünya'ya yağmur yağdı", "emoji": "🌧️"}, {"label": "Okyanuslar oluştu", "emoji": "🌊"}]}, ["🌋", "💧"], ["MİLYARLARCA YIL"])
S(2, {"type": "bar-chart", "title": "Dünya'nın suyu", "unit": "%", "bars": [{"label": "Okyanuslar", "value": 97, "display": "97"}, {"label": "Tatlı su", "value": 2.5, "display": "2,5", "highlight": True}]}, ["🌊", "🚰"], ["ÇOĞU TUZLU", "TATLI SU AZ"])
S(2, {"type": "bullets", "title": "Kullanılabilir su az", "items": ["Tatlı suyun yaklaşık %68'i donmuş", "Yaklaşık %30'u yer altında", "Suyu boşa harcama"]}, ["🧊", "🚿"], ["BOŞA HARCAMA 🚰", "SİLİNİRİM 🧽"], extra=[11])
S(2, {"type": "diagram", "title": "Sen de dene: kâsede su döngüsü", "layout": "flow", "nodes": [{"label": "Kâseye ılık su", "emoji": "🥣"}, {"label": "Streç filmle kapat", "emoji": "🎬"}, {"label": "Güneşli pencere", "emoji": "☀️"}, {"label": "Filmin altında damlacıklar", "emoji": "💧"}]}, ["🔬", "📓"], ["DENEY ZAMANI 🔬", "KÂSEDE BULUT ☁️"])
S(1, {"type": "bullets", "title": "Güvenlik", "items": ["Ilık su yeterli", "Sıcak su için bir büyüğünden yardım iste"], "tone": "caution"}, ["⚠️", "🫖"], ["BÜYÜĞÜNE SOR ⚠️"])
S(1, {"type": "big-number", "value": "%0,001", "label": "Dünya'daki suyun atmosferdeki payı", "sub": "National Geographic", "icon": "☁️"}, ["💧", "🌍"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Su buharının damlacığa dönüşmesine ne denir?", "emoji": "🤔"}, ["☁️", "💧"], ["HIZLI SORU!", "YOĞUŞMA ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 16, "videoTitle": "Yağmur nasıl yağar?", "paperTitleTr": "Yağmur nasıl yağar?",
  "theme": {"backdrop": "storm", "actors": [{"kind": "walk", "emoji": "🐌", "every": 34, "size": 80}, {"kind": "fly", "emoji": "🕊️", "every": 22}, {"kind": "walk", "emoji": "🦆", "every": 27}, {"kind": "hop", "emoji": "🐸", "size": 84}]},
  "takeaways": ["Su buharlaşır, yoğuşur ve yağış olarak geri döner", "Milyonlarca damlacık birleşince yağmur damlası düşer", "Dünya'daki suyun çok azı tatlı sudur"],
  "description": "Su gökyüzüne nasıl çıkar, bulut düşmezken yağmur neden düşer? Bu bölümde su döngüsünü; buharlaşmayı, terlemeyi, süblimleşmeyi ve yoğuşmayı; bulutların nasıl oluştuğunu, damlacıkların nasıl yağmur damlasına dönüştüğünü ve damlanın gerçek biçimini keşfediyoruz. Yere düşen su nereye gider, Dünya'daki suyun ne kadarı tatlı sudur? Sonunda kâsede su döngüsü deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Su döngüsü", "meaning": "Suyun yeryüzü, gökyüzü ve yer altı arasındaki bitmeyen yolculuğu."},
    {"term": "Buharlaşma", "meaning": "Sıvı suyun gaz hâline, yani su buharına dönüşmesi."},
    {"term": "Terleme", "meaning": "Suyun bitkilerin yapraklarından buharlaşması."},
    {"term": "Süblimleşme", "meaning": "Buzun ya da karın sıvılaşmadan doğrudan buhara dönüşmesi."},
    {"term": "Yoğuşma", "meaning": "Su buharının soğuyup minik su damlacıklarına dönüşmesi."},
    {"term": "Yağış", "meaning": "Bulutlardan yağmur, kar, dolu ya da sulu kar olarak düşen su."},
    {"term": "Yeraltı suyu", "meaning": "Toprağa süzülüp yer altında biriken su."},
    {"term": "Akifer", "meaning": "Yeraltı suyunu tutan ve ileten yer altı katmanı."}],
  "song": e.song("Damlanın Yolculuğu", [("💧", "Damla"), ("☀️", "Güneş"), ("☁️", "Bulut"), ("🌧️", "Yağış"), ("🌊", "Okyanus")],
    ["Güneş ısıtır, su buhar olur", "Yapraklardan da buharlaşır", "Yükselen hava soğur yukarıda", "Buhar yoğuşur toz zerresinde"],
    ["Buharlaş, yoğuş, yağ; döngü döner!", "Milyonlarca damlacık birleşir", "Büyüyen damla yere iner", "Nehirden denize, yeniden başlar"],
    ["Bulut tonlarca ama düşmez yere", "Yükselen hava tutar onu", "Damla yuvarlak, büyüğü yassı", "Toprağa süzülür, akiferde akar"],
    ["Buharlaş, yoğuş, yağ; döngü döner!", "Milyonlarca damlacık birleşir", "Tatlı su azdır, boşa harcama", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "💧"}, {"kind": "hop", "emoji": "☔"}, {"kind": "hop", "emoji": "🐸"}, {"kind": "hop", "emoji": "💧"}, {"kind": "fly", "emoji": "🕊️", "every": 9}, {"kind": "walk", "emoji": "🦆", "every": 11}])}
e.write(D, facts, script)
