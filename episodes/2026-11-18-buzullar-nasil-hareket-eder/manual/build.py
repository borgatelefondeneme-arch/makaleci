"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:buzullar-nasil-hareket-eder"
NO = "NSIDC — Glaciers"; NS = "NSIDC — Science of Glaciers"; NQ = "NSIDC — Glacier Quick Facts"; NG = "National Geographic Education — Glacier"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Glaciers", "publisher": "NSIDC", "url": "https://nsidc.org/learn/parts-cryosphere/glaciers"},
    {"id": "k2", "title": "Science of Glaciers", "publisher": "NSIDC", "url": "https://nsidc.org/learn/parts-cryosphere/glaciers/science-glaciers"},
    {"id": "k3", "title": "Glacier Quick Facts", "publisher": "NSIDC", "url": "https://nsidc.org/learn/parts-cryosphere/glaciers/glacier-quick-facts"},
    {"id": "k4", "title": "Glacier", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/glacier/"}],
  "facts": [
    F(1, "Buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.", "A glacier is an accumulation of ice and snow that slowly flows over land.", NO),
    F(2, "Buzullar karada oluşur ve yüzyıllar boyunca sıkışarak buza dönüşen yağmış kardan yapılır.", "Glaciers form on land, and they are made up of fallen snow that gets compressed into ice over many centuries.", NG),
    F(3, "Her yıl yeni kar katmanları öncekileri gömer ve sıkıştırır; yaklaşık bir yıl sonra kar, kar ile buzul buzu arasında bir ara hal olan firne dönüşür; çoğu buzul için bu süreç yüz yıldan uzun sürer.", "Each year, new layers of snow bury and compress the previous layers. / After about a year, the snow turns into firn—an intermediate state between snow and glacier ice. / For most glaciers, this process takes more than a hundred years.", NO),
    F(4, "Çok yaşlı buzul buzunda kristaller bir yetişkin yumruğu büyüklüğüne ulaşabilir.", "In very old glacier ice, crystals can reach the size of an adult fist.", NQ),
    F(5, "Buzul buzu çok yoğunlaşıp kabarcıklardan arınınca çoğu zaman mavi görünür; buz kırmızı ışığın küçük bir bölümünü soğurur.", "Glacial ice often appears blue when it has become very dense and free of bubbles. / Ice absorbs a small amount of red light.", NQ),
    F(6, "Buzul kendi ağırlığının basıncıyla dışarıya ve aşağıya doğru akmaya başlar; kalın bir buz katmanının ağırlığı, yani buz kütlesine etki eden yer çekimi buzulları akıtır.", "Under the pressure of its own weight, a glacier will begin to move, or flow, outwards and downwards. / The sheer weight of a thick layer of ice, or the force of gravity on the ice mass, causes glaciers to flow.", NS),
    F(7, "Buzullar buzun iç deformasyonuyla ve tabandaki kayaların ve tortuların üzerinde kayarak hareket eder; dik yamaçlardaki ince, soğuk buzulların hareketinin çoğu bu taban kaymasından gelebilir.", "Glaciers move by internal deformation of the ice, and by sliding over the rocks and sediments at the base. / This basal sliding may account for most of the movement of thin, cold glaciers on steep slopes.", NS),
    F(8, "Yarıklar buzul buzundaki çatlaklardır; buzulun hızlı aktığı yerlerde sürtünme bu dev çatlakları oluşturur.", "Crevasse are cracks in glacier ice. / At locations where a glacier flows rapidly, friction creates these giant cracks.", NS),
    F(9, "Buzullar ani atılımlar yaparak haftalarca, hatta aylarca günde birkaç metre ilerleyebilir; en hızlı atılım rekoru Pakistan'daki Kutiah Buzulu'nundur: 1953'te üç ayda 12 kilometreden fazla ilerledi, günde ortalama yaklaşık 112 metre.", "Glaciers may surge, racing forward several meters per day for weeks or even months. / The Kutiah Glacier in Pakistan holds the record for the fastest glacial surge. / In 1953, it raced more than 12 kilometers (7.5 miles) in three months, averaging about 112 meters (367 feet) per day.", NS + "; " + NQ, ["1953", "12", "112"]),
    F(10, "ABD Jeoloji Araştırmaları Kurumu'na göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde 68,7'sini depolar.", "Glaciers and ice caps store about 68.7 percent of the world's fresh water, according to the US Geological Survey.", NQ, ["68.7"]),
    F(11, "Dünyada yalnızca iki buz tabakası vardır: Antarktika ve Grönland buz tabakaları; ikisi birlikte Dünya'daki tatlı su buzunun yüzde 99'undan fazlasını içerir; buzul buzunun çoğu Antarktika'dadır.", "Currently, there are only two ice sheets on Earth: the Antarctic and Greenland Ice Sheets. / Together, the Antarctic and Greenland Ice Sheets contain more than 99 percent of the freshwater ice on Earth. / Most of the world’s glacier ice is in Antarctica.", NO, ["99"]),
    F(12, "Dünyadaki buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir.", "Most of the world’s glaciers exist in the polar regions, in areas like Greenland, the Canadian Arctic, and Antarctica.", NG),
    F(13, "Son 60 ila 100 yılda dünyadaki buzullar genel olarak geri çekildi; son birkaç on yılda buzullar giderek artan bir hızla küçülüyor, hatta yok oluyor.", "Over the past 60 to 100 years, glaciers worldwide have tended to retreat. / Indeed, glaciers worldwide have been shrinking—and even disappearing—at an accelerated rate for the past several decades.", NS + "; " + NG, ["60", "100"]),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"; NSs = "En Es Ay Di Si"
e.sec("hook", [
    L("Dağın tepesinde dev bir buz kütlesi var. Hiç kıpırdamıyor gibi görünüyor, ama aslında akıyor! Hem de bir nehir gibi, sadece çok çok yavaş.", [1]),
    L("Buz nasıl akar? Ve bu dev buzlar nereden gelir?"),
    L("Bugün buzulların soğuk ve sessiz yolculuğuna katılıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Buzul nasıl oluşur? Nasıl hareket eder? Ve neden önemlidir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Ulusal Kar ve Buz Veri Merkezi NSIDC'ye göre buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir.", [1], f"ABD Ulusal Kar ve Buz Veri Merkezi {NSs}'ye göre buzul, kara üzerinde yavaşça akan bir buz ve kar birikintisidir."),
    L("Her şey kar ile başlar. Her yıl yağan yeni kar katmanları, alttaki eski katmanları gömer ve sıkıştırır.", [3]),
    L("Yaklaşık bir yıl sonra kar, firn denen bir ara hale dönüşür: Artık kar değildir ama henüz buzul buzu da değildir.", [3]),
    L("Çoğu buzul için kardan buzul buzuna dönüşmek yüz yıldan uzun sürer!", [3]),
    L("Ben yüz yıl beklemeye dayanamam. Pilim çoktan biterdi!"),
])
e.sec("finding", [
    L("Buzul buzu çok yoğunlaşıp içindeki kabarcıklardan arınınca mavi görünür. Çünkü buz, kırmızı ışığın küçük bir bölümünü soğurur.", [5]),
    L("Çok yaşlı buzul buzunda buz kristalleri bir yetişkinin yumruğu kadar büyüyebilir!", [4]),
    L("Peki buzul neden akar? Cevap: Kendi ağırlığı! Kalın bir buz katmanı o kadar ağırdır ki yer çekimi onu dışarıya ve aşağıya doğru akıtır.", [6]),
    L("Buzul iki yolla hareket eder. Birincisi, buzun kendi içinde yavaşça şekil değiştirmesidir. Buna iç deformasyon denir.", [7]),
    L("İkincisi, tabandaki kayaların ve tortuların üzerinde kaymasıdır. Dik yamaçlardaki ince buzulların hareketinin çoğu bu kaymadan gelebilir.", [7]),
    L("Buzulun hızlı aktığı yerlerde sürtünme dev çatlaklar açar. Bunlara yarık denir.", [8]),
])
e.sec("importance", [
    L("Buzullar genelde yavaştır, ama bazen ani atılımlar yapar ve haftalarca günde birkaç metre ilerler.", [9]),
    L("Rekor, Pakistan'daki Kutiah Buzulu'nda: 1953'te üç ayda 12 kilometreden fazla ilerledi. Günde ortalama yaklaşık 112 metre!", [9], "Rekor, Pakistan'daki Kutiah Buzulu'nda: bin dokuz yüz elli üçte üç ayda on iki kilometreden fazla ilerledi. Günde ortalama yaklaşık yüz on iki metre!"),
    L("Buzul olsam ben de bir gün koşuya çıkardım. Ama sonra yüz yıl dinlenirdim!"),
    L("Buzullar dev su depolarıdır. NSIDC'ye göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde 68,7'sini depolar.", [10], f"Buzullar dev su depolarıdır. {NSs}'ye göre buzullar ve buz takkeleri dünyadaki tatlı suyun yaklaşık yüzde altmış sekiz virgül yedisini depolar."),
    L("Buzulların çoğu Grönland, Kanada Arktiği ve Antarktika gibi kutup bölgelerindedir. Buzul buzunun çoğu ise Antarktika'dadır.", [11, 12]),
    L("Ama buzullar küçülüyor. Son 60 ila 100 yılda dünyadaki buzullar genel olarak geri çekildi.", [13], "Ama buzullar küçülüyor. Son altmış ila yüz yılda dünyadaki buzullar genel olarak geri çekildi."),
    L("Şimdi sıra sende! Eldivenlerini giy ve bir avuç kar ya da dondurucudaki karlanmış buzdan al.", [3]),
    L("Onu ellerinle iyice sıkıştır. Kar topu sertleşip buza benziyor mu? Buzulun ilk adımı da böyle bir sıkışmadır!", [3]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Dünyada yalnızca iki buz tabakası var: Antarktika ve Grönland. İkisi birlikte Dünya'daki tatlı su buzunun yüzde 99'undan fazlasını içerir!", [11], "Bunu biliyor muydun? Dünyada yalnızca iki buz tabakası var: Antarktika ve Grönland. İkisi birlikte Dünya'daki tatlı su buzunun yüzde doksan dokuzundan fazlasını içerir!"),
    L("Hızlı soru! Kar ile buzul buzu arasındaki ara hale ne denir?", [3]),
    L("Düşün bakalım... Evet: firn!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Sıcak bir şeyler iç, görüşürüz!"),
])
S = e.S
S(3, {"type": "hook", "question": "Buzullar nasıl hareket eder?", "emoji": "🏔️"}, ["❄️", "🧊"], ["BUZ AKAR!", "NEREDEN GELİR?", "SESSİZ YOLCULUK"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Buzul nasıl oluşur?", "Nasıl hareket eder?", "Neden önemlidir?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "stages", "title": "Kardan buzula", "rows": [{"label": "Kar yağar", "emoji": "🌨️"}, {"label": "Katmanlar sıkışır", "emoji": "🥞"}, {"label": "Firn", "emoji": "🧂"}, {"label": "Buzul buzu", "emoji": "🧊"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim."}, [], ["BUZUL", "SIKIŞMA", "FİRN"])
S(2, {"type": "big-number", "value": "Yüz yıldan fazla", "label": "Çoğu buzulda kardan buzul buzuna dönüşüm süresi", "sub": "NSIDC", "icon": "⏳"}, ["⏳", "🔋"], ["YÜZYILLAR", "PİL BİTER 🔋"])
S(2, {"type": "spotlight", "title": "Mavi buz", "emoji": "🧊", "chips": [{"label": "Yoğun ve kabarcıksız", "emoji": "💎"}, {"label": "Kırmızı ışığı biraz soğurur", "emoji": "🔴"}, {"label": "Yumruk kadar kristaller", "emoji": "✊"}]}, ["💎", "✊"], ["MAVİ BUZ", "DEV KRİSTALLER"], fx="sparkle")
S(3, {"type": "diagram", "title": "Buzul nasıl akar?", "layout": "flow", "nodes": [{"label": "Ağırlık ve yer çekimi", "emoji": "⬇️"}, {"label": "İç deformasyon", "emoji": "🌀"}, {"label": "Tabanda kayma", "emoji": "🛷"}]}, ["⬇️", "🛷"], ["KENDİ AĞIRLIĞI", "İÇ DEFORMASYON", "TABAN KAYMASI"])
S(1, {"type": "spotlight", "title": "Yarık", "emoji": "⚠️", "chips": [{"label": "Buzul buzunda dev çatlak", "emoji": "🧊"}, {"label": "Hızlı akışta sürtünme açar", "emoji": "⚡"}]}, ["🧊", "⚠️"], ["YARIK ⚠️"])
S(3, {"type": "big-number", "value": "Günde 112 metre", "label": "Kutiah Buzulu, 1953: üç ayda 12 km'den fazla", "sub": "NSIDC", "icon": "🏃"}, ["🏃", "🏔️"], ["ANİ ATILIM", "REKOR!", "KOŞAN BUZUL 🏃"])
S(2, {"type": "meter", "title": "Tatlı su deposu", "label": "Tatlı su", "emoji": "💧", "phases": [{"label": "Buzul ve buz takkeleri: %68,7", "level": 0.687, "emoji": "🧊"}, {"label": "Çoğu kutup bölgelerinde", "level": 0.7, "emoji": "🧭"}], "note": "Şematik çizim."}, ["💧", "🧭"], ["%68,7", "ANTARKTİKA"])
S(1, {"type": "comparison", "title": "Buzullar küçülüyor", "left": {"title": "Son 60–100 yıl", "items": ["Genel olarak geri çekildi"]}, "right": {"title": "Son on yıllar", "items": ["Giderek hızlanan küçülme"]}}, ["🌡️", "📉"], ["GERİ ÇEKİLME"])
S(2, {"type": "bullets", "title": "Sen de dene: mini buzul", "items": ["Eldiven giy", "Bir avuç kar ya da karlanmış buz al", "Ellerinle iyice sıkıştır", "Sertleşip buza benziyor mu?"]}, ["🧤", "❄️"], ["DENEY ZAMANI 🔬", "SIKIŞMA!"])
S(1, {"type": "big-number", "value": "%99+", "label": "Antarktika ve Grönland'daki tatlı su buzu payı", "sub": "NSIDC", "icon": "🧊"}, ["🐧", "🧊"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Kar ile buzul buzu arasındaki hal?", "emoji": "🤔"}, ["❄️", "🧊"], ["HIZLI SORU!", "FİRN ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 43, "videoTitle": "Buzullar nasıl hareket eder?", "paperTitleTr": "Buzullar nasıl hareket eder?",
  "theme": {"backdrop": "snow", "actors": [{"kind": "walk", "emoji": "🐧", "every": 32}]},
  "takeaways": ["Buzullar yüzyıllar boyunca sıkışan kardan oluşur; kar önce firne, sonra buza dönüşür", "Kendi ağırlıklarıyla iç deformasyon ve taban kaymasıyla akarlar", "Dünyadaki tatlı suyun büyük kısmını depolarlar ve küçülüyorlar"],
  "description": "Buz nasıl akar? Bu bölümde karın firne ve buzul buzuna dönüşmesini, buzul buzunun neden mavi göründüğünü, buzulların kendi ağırlıklarıyla nasıl hareket ettiğini, yarıkları, rekor kıran Kutiah Buzulu'nun ani atılımını, buzulların tatlı su deposu olmasını ve küçülmelerini keşfediyoruz. Sonunda mini buzul deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Buzul", "meaning": "Kara üzerinde yavaşça akan dev buz ve kar kütlesi."},
    {"term": "Firn", "meaning": "Kar ile buzul buzu arasındaki ara hal."},
    {"term": "İç deformasyon", "meaning": "Buzun kendi içinde yavaşça şekil değiştirerek akması."},
    {"term": "Yarık", "meaning": "Buzul buzunda açılan dev çatlak."},
    {"term": "Ani atılım", "meaning": "Bir buzulun kısa sürede çok hızlı ilerlemesi."},
    {"term": "Buz tabakası", "meaning": "Antarktika ve Grönland'ı örten dev buz kütlesi."}],
  "song": e.song("Yavaş Nehir", [("🏔️", "Buzul"), ("❄️", "Kar"), ("🧊", "Buz"), ("💧", "Tatlı su"), ("🐧", "Penguen")],
    ["Kar yağar katman katman", "Sıkışır, firne döner", "Yüzyıllar geçer sessizce", "Mavi buza dönüşür"],
    ["Ak, ak, yavaş nehir!", "Ağırlığınla kayar gidersin", "İçinden akar, tabanda kayarsın", "Yarıklar açılır yolunda"],
    ["Bazen koşar bir atılımla", "Tatlı suyu saklar içinde", "Antarktika, Grönland ev sahibi", "Son yıllarda hızla küçülür"],
    ["Ak, ak, yavaş nehir!", "Ağırlığınla kayar gidersin", "Karı sıkıştır, buzu gör", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "walk", "emoji": "🐧"}, {"kind": "hop", "emoji": "❄️"}, {"kind": "hop", "emoji": "🧊"}, {"kind": "walk", "emoji": "🐧"}])}
e.write(D, facts, script)
