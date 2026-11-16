"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:gunes-sistemi-nde-hangi-gezegenler-var"
S1 = "NASA Science — Solar System Exploration"; S2 = "NASA Science — Solar System: Facts"; S3 = "NASA Science — About the Planets"; S4 = "NASA Science — What is a Planet?"
S5 = "NASA Science — Jupiter Facts"; S6 = "NASA Science — Saturn: Facts"; S7 = "NASA Science — Mars: Facts"; S8 = "NASA Science — Venus: Facts"; S9 = "NASA Science — Pluto: Facts"
U = "https://science.nasa.gov/"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Solar System Exploration", "publisher": "NASA", "url": U + "solar-system/"},
    {"id": "k2", "title": "Solar System: Facts", "publisher": "NASA", "url": U + "solar-system/solar-system-facts/"},
    {"id": "k3", "title": "About the Planets", "publisher": "NASA", "url": U + "solar-system/planets/"},
    {"id": "k4", "title": "What is a Planet?", "publisher": "NASA", "url": U + "solar-system/planets/what-is-a-planet/"},
    {"id": "k5", "title": "Jupiter Facts", "publisher": "NASA", "url": U + "jupiter/jupiter-facts/"},
    {"id": "k6", "title": "Saturn: Facts", "publisher": "NASA", "url": U + "saturn/facts/"},
    {"id": "k7", "title": "Mars: Facts", "publisher": "NASA", "url": U + "mars/facts/"},
    {"id": "k8", "title": "Venus: Facts", "publisher": "NASA", "url": U + "venus/venus-facts/"},
    {"id": "k9", "title": "Pluto: Facts", "publisher": "NASA", "url": U + "dwarf-planets/pluto/facts/"}],
  "facts": [
    F(1, "Güneş sistemimizde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ve asteroit vardır.", "Our solar system has one star, eight planets, five dwarf planets, hundreds of moons and thousands of comets and asteroids.", S2),
    F(2, "Güneş sistemimiz yaklaşık 4,6 milyar yıl önce yoğun bir yıldızlar arası gaz ve toz bulutundan oluştu; bulut çöküp dönen bir disk oluşturdu; Güneş mevcut maddenin %99'undan fazlasını topladı.", "Our solar system formed about 4.6 billion years ago from a dense cloud of interstellar gas and dust. / When this dust cloud collapsed, it formed a solar nebula – a spinning, swirling disk of material. / it eventually amassed more than 99% of the available matter.", S2, ["4.6", "99"]),
    F(3, "Sekiz gezegen: Merkür, Venüs, Dünya, Mars, Jüpiter, Satürn, Uranüs ve Neptün. İlk dördü katı yüzeyleri olduğu için karasal gezegenlerdir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.", "Our solar system has eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. / These inner planets also are known as terrestrial planets because they have solid surfaces. / Jupiter and Saturn are gas giants. Uranus and Neptune are ice giants.", S3),
    F(4, "Asteroit kuşağı, erken güneş sisteminden kalan parçalardan oluşur; Mars ile Jüpiter arasındadır; en büyük cismi cüce gezegen Ceres'tir.", "the asteroid belt is made of bits and pieces of the early solar system / Dwarf planet Ceres is the largest object in the asteroid belt between Mars and Jupiter", S2 + "; " + S3),
    F(5, "Bir cismin gezegen sayılması için bir yıldızın çevresinde dolanması, küre biçimini alacak kadar kütle çekimine sahip olması ve yörüngesinin çevresini benzer boyuttaki cisimlerden temizlemiş olması gerekir. Plüton 2006'da cüce gezegen olarak yeniden sınıflandırıldı; yörüngesini temizleyemedi.", "It must orbit a star (in our cosmic neighborhood, the Sun). / It must be big enough to have enough gravity to force it into a spherical shape. / its gravity has cleared away any other objects of a similar size near its orbit / Pluto was reclassified as a dwarf planet in 2006 / has not been able to clear its orbit of debris.", S4 + "; " + S9, ["2006"]),
    F(6, "Merkür Güneş'e en yakın ve en küçük gezegendir.", "Mercury is the planet nearest to the Sun, and the smallest planet in our solar system.", S3),
    F(7, "Venüs'ün kalın atmosferi ısıyı hapseder ve onu güneş sisteminin en sıcak gezegeni yapar; yüzey sıcaklığı kurşunu eritecek kadardır: yaklaşık 467 santigrat derece; atmosferi çoğunlukla karbondioksittir; Venüs çoğu gezegenin tersi yönde, yavaşça döner.", "Its thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system / about 872 degrees Fahrenheit (467 Celsius). / The atmosphere is mostly carbon dioxide / Venus spins slowly in the opposite direction from most planets.", S8, ["467"]),
    F(8, "Şimdiye kadar güneş sistemimizde yaşam bulduğumuz tek yer Dünya'dır; Dünya Güneş'ten üçüncü gezegendir.", "So far, Earth is the only place we've found life in our solar system. / Earth – our home planet – is the third planet from the Sun, and the fifth largest planet.", S1 + "; " + S3),
    F(9, "Mars'ın kırmızı görünmesinin nedeni kayalardaki demirin paslanmasıdır; güneş sisteminin en büyük yanardağı Olympus Mons Mars'tadır; Mars'ın iki küçük uydusu vardır: Phobos ve Deimos.", "The reason Mars looks reddish is due to oxidization — or rusting — of iron in the rocks / Mars is home to the largest volcano in the solar system, Olympus Mons. / Mars has two small moons, Phobos and Deimos", S7),
    F(10, "Jüpiter en büyük gezegendir; içi boş bir kabuk olsaydı içine 1.000 Dünya sığardı; Dünya bir üzüm olsaydı Jüpiter bir basketbol topu kadar olurdu; Büyük Kırmızı Leke, Dünya'dan büyük, yüzlerce yıldır süren dev bir fırtınadır; Jüpiter'in Uluslararası Astronomi Birliği'nin resmen tanıdığı 115 uydusu vardır.", "if it were a hollow shell, 1,000 Earths could fit inside. / If Earth were the size of a grape, Jupiter would be about as big as a basketball. / a giant storm bigger than Earth that has raged for hundreds of years. / Jupiter has 115 moons that are officially recognized", S5, ["1.000", "115"]),
    F(11, "Satürn'ün halkaları, toz gibi maddelerle kaplı milyarlarca küçük buz ve kaya parçasından oluşur; Satürn ortalama yoğunluğu sudan az olan tek gezegendir; Mart 2025 itibarıyla 274 doğrulanmış uydusu vardı.", "They are made of billions of small chunks of ice and rock coated with other materials such as dust. / Saturn is the only planet in our solar system with an average density that is less than water. / As of March 2025, Saturn had 274 confirmed moons", S6, ["2025", "274"]),
    F(12, "Uranüs Güneş'ten yedinci ve en büyük üçüncü gezegendir; Neptün sekizinci ve en uzak gezegendir.", "Uranus is the seventh planet from the Sun, and the third largest planet in our solar system. / Neptune is the eighth and most distant planet in our solar system.", S3),
    F(13, "Bir astronomik birim, Güneş ile Dünya arasındaki uzaklıktır: yaklaşık 150 milyon kilometre. Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a 13 dakikada, Jüpiter'e 43 dakikada, Satürn'e 80 dakikada ulaşır.", "One astronomical unit (or AU) is the distance from the Sun to Earth, or about 93 million miles (150 million kilometers). / about eight minutes for the Sun and Earth / it takes sunlight 13 minutes to travel from the Sun to Mars / 43 minutes to travel from the Sun to Jupiter / 80 minutes to travel from the Sun to Saturn", S2 + "; " + S8 + "; " + S7 + "; " + S5 + "; " + S6, ["150", "13", "43", "80"]),
]}
e = Ep(); L = e.L
N = "Nasa"
e.sec("hook", [
    L("Güneş'in çevresinde dönen sekiz dünya düşün: biri kurşunu eritecek kadar sıcak, biri bin Dünya'yı içine alacak kadar büyük!", [3, 7, 10]),
    L("Bu gezegenler nasıl oluştu? Ve onları birbirinden ne ayırıyor?"),
    L("Bugün Güneş Sistemi'nde bir tura çıkıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Güneş Sistemi nasıl oluştu? Bir cisme ne zaman gezegen denir? Ve her gezegeni özel yapan nedir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre Güneş Sistemi'nde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ile asteroit var.", [1], f"{N}'ya göre Güneş Sistemi'nde bir yıldız, sekiz gezegen, beş cüce gezegen, yüzlerce uydu ve binlerce kuyruklu yıldız ile asteroit var."),
    L("Hepsi yaklaşık 4,6 milyar yıl önce, yoğun bir gaz ve toz bulutundan oluştu. Bulut çöktü ve dönen bir diske dönüştü.", [2], "Hepsi yaklaşık dört virgül altı milyar yıl önce, yoğun bir gaz ve toz bulutundan oluştu. Bulut çöktü ve dönen bir diske dönüştü."),
    L("Merkezde Güneş doğdu ve maddenin %99'undan fazlasını topladı. Gezegenlere geriye kalanlar düştü.", [2], "Merkezde Güneş doğdu ve maddenin yüzde doksan dokuzundan fazlasını topladı. Gezegenlere geriye kalanlar düştü."),
    L("Peki bir cisme ne zaman gezegen denir? Üç şartı var: Güneş'in çevresinde dolanacak, kütle çekimi onu top gibi yuvarlak yapacak ve yörüngesinin çevresini temizlemiş olacak.", [5]),
    L("Plüton üçüncü şartı karşılayamadı; bu yüzden 2006'da cüce gezegen olarak yeniden sınıflandırıldı.", [5], "Plüton üçüncü şartı karşılayamadı; bu yüzden iki bin altıda cüce gezegen olarak yeniden sınıflandırıldı."),
    L("Plüton'a üzülme. Ben de hiçbir sınıfa sığmıyorum: ne insanım ne bilgisayar!"),
])
e.sec("finding", [
    L("Şimdi tura başlıyoruz. İlk dört gezegen karasal gezegenlerdir; çünkü katı yüzeyleri vardır.", [3]),
    L("Merkür, Güneş'e en yakın ve en küçük gezegen.", [6]),
    L("Venüs ise en sıcak gezegen: yüzeyi yaklaşık 467 santigrat derece! Kalın, çoğunlukla karbondioksitten oluşan atmosferi ısıyı hapseder.", [7], "Venüs ise en sıcak gezegen: yüzeyi yaklaşık dört yüz altmış yedi santigrat derece! Kalın, çoğunlukla karbondioksitten oluşan atmosferi ısıyı hapseder."),
    L("Üstelik Venüs, çoğu gezegenin tersi yönde ve çok yavaş döner.", [7]),
    L("Üçüncü sırada evimiz Dünya. Şimdiye kadar yaşam bulduğumuz tek yer burası.", [8]),
    L("Dördüncü sırada Mars. Kırmızı rengi, kayalarındaki demirin paslanmasından gelir. Güneş Sistemi'nin en büyük yanardağı Olympus Mons da Mars'ta.", [9], "Dördüncü sırada Mars. Kırmızı rengi, kayalarındaki demirin paslanmasından gelir. Güneş Sistemi'nin en büyük yanardağı Olimpus Mons da Mars'ta."),
    L("Paslanmak mı? Bu konuda Mars'la dertleşebilirim!"),
    L("Mars ile Jüpiter arasında asteroit kuşağı uzanır: erken Güneş Sistemi'nden kalan kaya parçaları. En büyüğü cüce gezegen Ceres'tir.", [4], "Mars ile Jüpiter arasında asteroit kuşağı uzanır: erken Güneş Sistemi'nden kalan kaya parçaları. En büyüğü cüce gezegen Seres'tir."),
])
e.sec("importance", [
    L("Sonra devler gelir. Jüpiter ve Satürn gaz devleri, Uranüs ve Neptün buz devleridir.", [3]),
    L("Jüpiter en büyük gezegen: içi boş olsaydı içine 1.000 Dünya sığardı. Dünya bir üzüm olsaydı, Jüpiter bir basketbol topu kadar olurdu.", [10], "Jüpiter en büyük gezegen: içi boş olsaydı içine bin Dünya sığardı. Dünya bir üzüm olsaydı, Jüpiter bir basketbol topu kadar olurdu."),
    L("Üzerindeki Büyük Kırmızı Leke, Dünya'dan büyük ve yüzlerce yıldır süren dev bir fırtınadır. Jüpiter'in resmen tanınan 115 uydusu var.", [10], "Üzerindeki Büyük Kırmızı Leke, Dünya'dan büyük ve yüzlerce yıldır süren dev bir fırtınadır. Jüpiter'in resmen tanınan yüz on beş uydusu var."),
    L("Satürn'ün ünlü halkaları milyarlarca küçük buz ve kaya parçasından oluşur.", [11]),
    L("Satürn, ortalama yoğunluğu sudan az olan tek gezegen. Ve Mart 2025 itibarıyla 274 uydusu doğrulanmıştı!", [11], "Satürn, ortalama yoğunluğu sudan az olan tek gezegen. Ve Mart iki bin yirmi beş itibarıyla iki yüz yetmiş dört uydusu doğrulanmıştı!"),
    L("Uranüs yedinci sırada; Neptün ise sekizinci ve Güneş'e en uzak gezegen.", [12]),
    L("Uzaklıkları anlamak için ışığa bakalım: Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a 13 dakikada, Jüpiter'e 43 dakikada, Satürn'e 80 dakikada ulaşır.", [13], "Uzaklıkları anlamak için ışığa bakalım: Güneş ışığı Dünya'ya yaklaşık sekiz dakikada, Mars'a on üç dakikada, Jüpiter'e kırk üç dakikada, Satürn'e seksen dakikada ulaşır."),
    L("Şimdi sıra sende! Sekiz kâğıda gezegenlerin adını yaz ve Güneş'ten uzaklık sırasına göre yere diz.", [3]),
    L("Sonra ilk dördün arasındaki adımlarla son dördün arasındaki adımları karşılaştır. Dış gezegenler ne kadar uzakta, gördün mü?", [13]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Güneş ile Dünya arasındaki uzaklığa bir astronomik birim denir: yaklaşık 150 milyon kilometre.", [13], "Bunu biliyor muydun? Güneş ile Dünya arasındaki uzaklığa bir astronomik birim denir: yaklaşık yüz elli milyon kilometre."),
    L("Hızlı soru! Güneş Sistemi'nin en sıcak gezegeni hangisi?", [7]),
    L("Düşün bakalım... Evet: Venüs! Güneş'e en yakın gezegen olmasa da.", [6, 7]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma."),
])
S = e.S
S(3, {"type": "hook", "question": "Güneş Sistemi'nde hangi gezegenler var?", "emoji": "🪐"}, ["☀️", "🌍"], ["", "SEKİZ DÜNYA", "TURA ÇIKIYORUZ!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Güneş Sistemi nasıl oluştu?", "Bir cisme ne zaman gezegen denir?", "Her gezegeni özel yapan nedir?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Güneş Sistemi", "emoji": "☀️", "chips": [{"label": "Bir yıldız", "emoji": "☀️"}, {"label": "Sekiz gezegen", "emoji": "🪐"}, {"label": "Beş cüce gezegen", "emoji": "⚪"}, {"label": "Yüzlerce uydu", "emoji": "🌙"}]}, ["🔭", "✨"], ["GÜNEŞ SİSTEMİ"])
S(2, {"type": "diagram", "title": "Nasıl oluştu?", "layout": "flow", "nodes": [{"label": "Gaz ve toz bulutu", "emoji": "☁️"}, {"label": "Çöker, dönen disk olur", "emoji": "🌀"}, {"label": "Güneş: maddenin %99'undan fazlası", "emoji": "☀️"}, {"label": "Geriye kalanlar: gezegenler", "emoji": "🪐"}]}, ["⏳", "🌌"], ["4,6 MİLYAR YIL", "GÜNEŞ DOĞDU ☀️"])
S(3, {"type": "bullets", "title": "Gezegen olmanın üç şartı", "items": ["Güneş'in çevresinde dolanmak", "Kütle çekimiyle yuvarlak olmak", "Yörüngesini temizlemiş olmak", "Plüton: 2006'dan beri cüce gezegen"]}, ["⚪", "🤖"], ["ÜÇ ŞART", "PLÜTON: CÜCE GEZEGEN", "SINIFA SIĞMIYORUM 😅"])
S(1, {"type": "spotlight", "title": "Karasal gezegenler", "emoji": "🪨", "chips": [{"label": "İlk dört gezegen", "emoji": "4️⃣"}, {"label": "Katı yüzey", "emoji": "🧱"}]}, ["🌍", "🔴"], ["KARASAL GEZEGENLER"])
S(3, {"type": "comparison", "title": "İlk iki gezegen", "left": {"title": "Merkür ☿️", "items": ["Güneş'e en yakın", "En küçük"]}, "right": {"title": "Venüs 🔥", "items": ["En sıcak: yaklaşık 467°C", "Kalın karbondioksit atmosfer", "Tersi yönde, yavaş döner"]}}, [], ["MERKÜR", "VENÜS 🔥", "TERS DÖNÜŞ 🔄"])
S(1, {"type": "big-number", "value": "Dünya", "label": "Şimdiye kadar yaşam bulunan tek yer", "sub": "Güneş'ten üçüncü gezegen", "icon": "🌍"}, ["🌱", "💧"], ["EVİMİZ 🌍"])
S(2, {"type": "spotlight", "title": "Kırmızı gezegen: Mars", "emoji": "🔴", "chips": [{"label": "Kırmızı: demir paslanması", "emoji": "🪨"}, {"label": "Olympus Mons: en büyük yanardağ", "emoji": "🌋"}, {"label": "İki küçük uydu", "emoji": "🌑"}]}, ["🤖", "🛰️"], ["MARS 🔴", "PAS KARDEŞİ 😅"])
S(1, {"type": "meter", "title": "Asteroit kuşağı", "label": "Kaya parçaları", "emoji": "☄️", "phases": [{"label": "Mars ile Jüpiter arasında", "level": 0.5, "emoji": "🪨"}, {"label": "En büyüğü: Ceres", "level": 0.85, "emoji": "⚪"}], "note": NOTE}, ["🪨", "🔭"], ["ASTEROİT KUŞAĞI"])
S(3, {"type": "comparison", "title": "Dev Jüpiter", "left": {"title": "Boyut 🏀", "items": ["İçine 1.000 Dünya sığar", "Dünya üzüm ise Jüpiter basketbol topu"]}, "right": {"title": "Özellikler 🌀", "items": ["Büyük Kırmızı Leke: dev fırtına", "115 resmî uydu"]}}, ["🍇", "🏀"], ["GAZ VE BUZ DEVLERİ", "1.000 DÜNYA!", "BÜYÜK KIRMIZI LEKE"])
S(2, {"type": "spotlight", "title": "Halkalı Satürn", "emoji": "🪐", "chips": [{"label": "Halkalar: buz ve kaya parçaları", "emoji": "🧊"}, {"label": "Yoğunluğu sudan az", "emoji": "💧"}, {"label": "274 uydu (Mart 2025)", "emoji": "🌙"}]}, ["✨", "🌌"], ["HALKALAR", "274 UYDU 🌙"])
S(2, {"type": "stages", "title": "Güneş ışığının yolculuğu", "rows": [{"label": "Dünya: yaklaşık sekiz dakika", "emoji": "🌍"}, {"label": "Mars: 13 dakika", "emoji": "🔴"}, {"label": "Jüpiter: 43 dakika", "emoji": "🟠"}, {"label": "Satürn: 80 dakika", "emoji": "🪐"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": "Şematik çizim."}, [], ["URANÜS • NEPTÜN", "IŞIĞIN YOLCULUĞU ☀️"])
S(2, {"type": "diagram", "title": "Sen de dene: gezegen sırası", "layout": "flow", "nodes": [{"label": "Sekiz kâğıt", "emoji": "📄"}, {"label": "Gezegen adlarını yaz", "emoji": "✏️"}, {"label": "Sırayla yere diz", "emoji": "👣"}, {"label": "Adımları karşılaştır", "emoji": "📏"}]}, ["🪐", "📓"], ["DENEY ZAMANI 🔬", "DIŞ GEZEGENLER UZAK"])
S(1, {"type": "big-number", "value": "150 milyon", "unit": "km", "label": "Bir astronomik birim: Güneş–Dünya uzaklığı", "sub": "NASA", "icon": "📏"}, ["☀️", "🌍"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "En sıcak gezegen hangisi?", "emoji": "🤔"}, ["🔥", "🪐"], ["HIZLI SORU!", "VENÜS ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 23, "videoTitle": "Güneş Sistemi'nde hangi gezegenler var?", "paperTitleTr": "Güneş Sistemi'nde hangi gezegenler var?",
  "theme": {"backdrop": "space", "actors": [{"kind": "fly", "emoji": "🛰️", "every": 30}]},
  "takeaways": ["Güneş Sistemi 4,6 milyar yıl önce bir gaz ve toz bulutundan oluştu", "Dört karasal gezegen, iki gaz devi, iki buz devi var", "Gezegen olmak için üç şart gerekir; Plüton cüce gezegendir"],
  "description": "Güneş'in çevresinde hangi dünyalar dönüyor? Bu bölümde Güneş Sistemi'nin nasıl oluştuğunu, bir cisme ne zaman gezegen dendiğini ve Plüton'un neden cüce gezegen olduğunu; Merkür'den Neptün'e sekiz gezegeni, asteroit kuşağını, Jüpiter'in Büyük Kırmızı Lekesi'ni ve Satürn'ün halkalarını keşfediyoruz. Sonunda gezegen sırası etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Gezegen", "meaning": "Güneş'in çevresinde dolanan, yuvarlak ve yörüngesini temizlemiş gök cismi."},
    {"term": "Cüce gezegen", "meaning": "Yuvarlak ama yörüngesini temizleyememiş gök cismi; örneğin Plüton."},
    {"term": "Yörünge", "meaning": "Bir gök cisminin başka birinin çevresinde izlediği yol."},
    {"term": "Karasal gezegen", "meaning": "Katı yüzeyi olan gezegen: Merkür, Venüs, Dünya, Mars."},
    {"term": "Gaz devi", "meaning": "Çoğunlukla gazdan oluşan dev gezegen: Jüpiter, Satürn."},
    {"term": "Atmosfer", "meaning": "Bir gezegeni saran gaz katmanı."},
    {"term": "Yoğunluk", "meaning": "Bir maddenin belirli bir hacimdeki kütlesi."},
    {"term": "Astronomik birim", "meaning": "Güneş ile Dünya arasındaki uzaklık; yaklaşık 150 milyon kilometre."}],
  "song": e.song("Sekiz Dünya", [("☀️", "Güneş"), ("🔴", "Mars"), ("🟠", "Jüpiter"), ("🪐", "Satürn"), ("🌍", "Dünya")],
    ["Gaz ve tozdan bir bulut çöktü", "Ortada Güneş, çevrede gezegenler", "Merkür küçük, Venüs en sıcak", "Dünya evimiz, Mars paslı kırmızı"],
    ["Sekiz dünya döner Güneş'in çevresinde!", "Dördü kayalık, dördü dev", "Asteroitler arada kuşak olur", "Plüton cüce, yine de bizden biri"],
    ["Jüpiter dev, fırtınası Dünya'dan büyük", "Satürn'ün halkası buz ve kaya", "Uranüs, Neptün uzaklarda buz devi", "Işık dakikalarca yol alır onlara"],
    ["Sekiz dünya döner Güneş'in çevresinde!", "Dördü kayalık, dördü dev", "Kâğıtları diz, adımları say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "orbit", "emoji": "🔴"}, {"kind": "orbit", "emoji": "🪐"}, {"kind": "orbit", "emoji": "🌍"}, {"kind": "fly", "emoji": "🚀", "every": 8, "facesRight": True}])}
e.write(D, facts, script)
