"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:magaralar-nasil-olusur"
SO = "National Park Service — Solution Caves"; SP = "National Park Service — Speleothems"; LA = "National Park Service — Lava Caves or Tubes"; SE = "National Park Service — Sea or Littoral Caves"; GL = "National Park Service — Glacier Ice Caves"; IX = "National Park Service — Caves and Karst"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Solution Caves", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/caves/solution-caves.htm"},
    {"id": "k2", "title": "Speleothems", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/caves/speleothems.htm"},
    {"id": "k3", "title": "Lava Caves or Tubes", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/caves/lava-caves-or-tubes.htm"},
    {"id": "k4", "title": "Sea or Littoral Caves", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/caves/sea-or-littoral-caves.htm"},
    {"id": "k5", "title": "Glacier Ice Caves", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/articles/000/glacier-ice-caves.htm"},
    {"id": "k6", "title": "Caves and Karst", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/subjects/caves/index.htm"}],
  "facts": [
    F(1, "Erime mağaraları en çok kireçtaşı, mermer ve dolomit gibi kayaçlarda bulunur.", "Solution caves are most often found in rock types such as limestone, marble, dolomite", SO),
    F(2, "Bu kayaçlar yağmur suyu asidik olduğu için çözünür; mağaraları oluşturan asit genellikle karbonik asittir; bu asit karbondioksit suda çözününce oluşur.", "The reason these rocks dissolve is because rainwater is acidic / When caves form the acid that makes them is usually carbonic acid. / This acid forms when carbon dioxide (made of one Carbon and two Oxygen atoms and known as CO2) dissolves in water.", SO),
    F(3, "Su tortuları ve çözünmüş kayayı aşağı taşıdıkça düdenler genişler.", "Sinkholes enlarge as water carries sediments and dissolved rock downward.", SO),
    F(4, "Karst, kireçtaşı ya da başka çözünebilir kayaçların bulunduğu bölgelerde oluşan bir yer şekli türüdür.", "Karst is a type of landscape and topography formed in areas with limestone or the other soluble rocks.", SO),
    F(5, "Jeologlara göre içinden dere akan mağara geçitleri yılda en fazla yaklaşık 1 milimetre büyüyebilir.", "Geologists have determined that cave passages with active streams can grow a maximum of about 1 mm per year.", SO, ["1"]),
    F(6, "Birçok mağara yüz binlerce, hatta milyonlarca yaşındadır.", "Many caves are hundreds of thousands or even millions of years old.", SO),
    F(7, "Mamut Mağarası 400 milden uzun ölçüsüyle Dünya'nın en uzun mağarasıdır.", "This is the longest cave on Earth at more than 400 miles.", SO, ["400"]),
    F(8, "Sarkıtlar genellikle kalsitten oluşur; tavandan sarkan buz saçaklarına ya da havuçlara benzerler; sarkıt kelimesi (stalaktit) Yunancada 'damla damla sızmak' demektir.", "Stalactites are usually composed of calcite, but they may consist of other minerals. / they resemble icicles or carrots hanging from cave ceilings. / the word stalactite is Greek for “oozing out in drops.”", SP),
    F(9, "Dikitler, yukarıdaki bir sarkıttan ya da tavandan damlayan suyun yerde biriktirdiği tümsek çökeltilerdir.", "Stalagmites are convex floor deposits built up by water dripping from an overhead stalactite", SP),
    F(10, "Bir dikit kendisini besleyen sarkıtla birleşince sütun oluşur; sütunlar bazen 20 metreyi aşan yükseklik ve çapa ulaşabilir.", "When a stalagmite grows together with its counterpart feeder stalactite, a new speleothem is formed: a column or pillar. / Columns can reach gigantic proportions, sometimes over 65 feet (20 m) in height and diameter.", SP, ["20"]),
    F(11, "Lav binlerce derece sıcaktır ve bir nehir gibi akabilir; erimiş lav geçip gidince geride lav tüpü denen boş bir tünel kalır.", "Lava is thousands of degrees hot and can flow like a river. / Once the molten lava has passed through, it leaves an empty tunnel called a lava cave, or more commonly, a lava tube.", LA),
    F(12, "Deniz mağaraları çoğunlukla dalgaların yol açtığı aşınmayla oluşur.", "Sea caves or littoral caves are formed primarily from erosion caused by waves.", SE),
    F(13, "Bazen bir buzulun kenarındaki erime, buzun içinde küçük mağaralar oluşturabilir; buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.", "Sometimes, melting at the margin of a glacier may cause small caves to form within the ice, / Glacier ice caves are cold, with icy water dripping from their roofs.", GL),
    F(14, "Lav mağaraları kireçtaşı mağaraları kadar canlı çeşitliliğine sahiptir, içlerinde birçok küçük ve sıra dışı hayvan yaşar; bazı yerlerde büyük yarasa tünekleri vardır.", "Lava caves are just as biologically diverse as limestone caves with many small, unusual animals inside. / In other locations, large bat roosts lie in the caves.", LA),
    F(15, "ABD milli parklarında 4.700'den fazla mağara vardır.", "This includes over 4,700 caves with at least four of these that extend for more than 135 miles", IX, ["4.700"]),
]}
e = Ep(); L = e.L
e.sec("hook", [
    L("Yerin altında, gün ışığının hiç ulaşmadığı dev salonlar var. Tavanlarından taş saçaklar sarkıyor. Bu salonları kim kazdı?", [8]),
    L("Cevap seni şaşırtabilir: Su! Hem de damla damla. Benim en korktuğum şey!", [2]),
    L("Bugün fenerimizi alıp bir mağaraya giriyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Su taşı nasıl oyar? Sarkıtlar ve dikitler nasıl oluşur? Ve başka hangi tür mağaralar vardır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Milli Parklar Servisi'ne göre mağaraların çoğu kireçtaşı, mermer ve dolomit gibi kayaçlarda oluşur. Bunlara erime mağarası denir.", [1]),
    L("Bu kayaçlar çözünür, çünkü yağmur suyu hafifçe asidiktir.", [2]),
    L("Havadaki karbondioksit suda çözünür ve karbonik asit oluşur. Mağaraları oyan asit genellikle budur.", [2]),
    L("Asitli su kayaçtaki çatlaklardan sızar ve kayayı çok yavaş çözer. Su, çözünen kayayı ve tortuları aşağı taşıdıkça düdenler genişler.", [2, 3]),
    L("Kireçtaşı gibi çözünebilir kayaçların olduğu bu tür bölgelere karst denir.", [4]),
])
e.sec("finding", [
    L("Peki bu iş ne kadar sürer? Jeologlara göre içinden dere akan bir mağara geçidi yılda en fazla yaklaşık 1 milimetre büyüyebilir.", [5], "Peki bu iş ne kadar sürer? Jeologlara göre içinden dere akan bir mağara geçidi yılda en fazla yaklaşık bir milimetre büyüyebilir."),
    L("Bu yüzden birçok mağara yüz binlerce, hatta milyonlarca yaşındadır!", [6]),
    L("Ben bir milimetre ilerlemek için bile acele ederim. Mağaralar ise hiç acele etmez!"),
    L("Mağarada tavandan aşağı sarkan taş saçaklara sarkıt denir. Buz saçaklarına ya da havuçlara benzerler.", [8]),
    L("Sarkıtlar genellikle kalsit denen mineralden oluşur. Adları Yunancada 'damla damla sızmak' anlamına gelen bir kelimeden gelir.", [8]),
    L("Sarkıttan yere damlayan su da yerde birikip yukarı doğru tümsekler yapar. Bunlara dikit denir.", [9]),
    L("Bir dikit sarkıtla birleşince sütun oluşur. Sütunlar bazen 20 metreyi aşan yüksekliğe ulaşabilir!", [10], "Bir dikit sarkıtla birleşince sütun oluşur. Sütunlar bazen yirmi metreyi aşan yüksekliğe ulaşabilir!"),
])
e.sec("importance", [
    L("Her mağara suyla çözünerek oluşmaz. Lav, binlerce derece sıcaktır ve bir nehir gibi akabilir.", [11]),
    L("Erimiş lav geçip gidince geride boş bir tünel kalır. Buna lav tüpü denir.", [11]),
    L("Deniz mağaraları ise dalgaların kayaları aşındırmasıyla oluşur. Dalgalar da benim gibi hiç yorulmaz!", [12]),
    L("Bir buzulun kenarındaki erime de buzun içinde küçük mağaralar açabilir. Buzul mağaraları soğuktur ve tavanlarından buzlu su damlar.", [13]),
    L("Mağaralar canlılarla da doludur. Lav mağaralarında birçok küçük, sıra dışı hayvan yaşar; bazılarında büyük yarasa tünekleri vardır.", [14]),
    L("Ben mağarada yaşayamam. Wi-fi çekmiyor!"),
    L("Şimdi sıra sende! Bir tabağa bir şeker küpü koy ve üstüne bir damlalıkla ya da kaşıkla damla damla su damlat.", [2]),
    L("Su, şekeri nasıl oyuyor? Yağmur suyu da kireçtaşını buna benzer biçimde, ama çok çok daha yavaş çözer.", [2, 5]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Milli Parklar Servisi'ne göre Dünya'nın en uzun mağarası Mamut Mağarası'dır: 400 milden uzun! Mil, ABD'de kullanılan bir uzunluk birimidir.", [7], "Bunu biliyor muydun? Milli Parklar Servisi'ne göre Dünya'nın en uzun mağarası Mamut Mağarası'dır: dört yüz milden uzun! Mil, ABD'de kullanılan bir uzunluk birimidir."),
    L("Hızlı soru! Tavandan aşağı sarkan taş saçaklara ne denir?", [8]),
    L("Düşün bakalım... Evet: sarkıt!", [8]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bir mağara gezisine gidersen rehberinin yanından ayrılma!"),
])
S = e.S
S(3, {"type": "hook", "question": "Mağaralar nasıl oluşur?", "emoji": "🕳️"}, ["🔦", "🦇"], ["YERİN ALTINDA", "SU!", "FENERLER HAZIR 🔦"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Su taşı nasıl oyar?", "Sarkıt ve dikit nasıl oluşur?", "Başka hangi mağaralar var?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "stages", "title": "Erime mağarası", "rows": [{"label": "Karbondioksit suda çözünür", "emoji": "💨"}, {"label": "Karbonik asit oluşur", "emoji": "🧪"}, {"label": "Kireçtaşı çözünür", "emoji": "🪨"}, {"label": "Boşluk büyür", "emoji": "🕳️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim."}, [], ["KİREÇTAŞI", "ASİDİK YAĞMUR", "KARBONİK ASİT"])
S(2, {"type": "spotlight", "title": "Karst", "emoji": "⛰️", "chips": [{"label": "Su çatlaklardan sızar", "emoji": "💧"}, {"label": "Düdenler genişler", "emoji": "🕳️"}, {"label": "Çözünebilir kayaç bölgesi", "emoji": "🪨"}]}, ["💧", "🪨"], ["DÜDEN", "KARST"], fx="dig")
S(3, {"type": "big-number", "value": "1 mm", "label": "Bir mağara geçidinin yılda en fazla büyümesi (yaklaşık)", "sub": "Milli Parklar Servisi", "icon": "🐌"}, ["🐌", "⏳"], ["YILDA 1 MM", "MİLYONLARCA YIL", "ACELE YOK 🐌"])
S(2, {"type": "meter", "title": "Sarkıt", "label": "Kalsit", "emoji": "💧", "phases": [{"label": "Buz saçağı gibi sarkar", "level": 0.5, "emoji": "🧊"}, {"label": "Damla damla büyür", "level": 0.75, "emoji": "💧"}], "note": NOTE}, ["🥕", "🧊"], ["SARKIT", "DAMLA DAMLA"])
S(2, {"type": "comparison", "title": "Dikit ve sütun", "left": {"title": "Dikit ⬆️", "items": ["Yere damlayan sudan", "Yukarı doğru büyür"]}, "right": {"title": "Sütun 🏛️", "items": ["Dikit + sarkıt birleşir", "20 metreyi aşabilir"]}}, ["🏛️", "💧"], ["DİKİT", "SÜTUN 🏛️"], fx="sparkle")
S(3, {"type": "diagram", "title": "Başka mağaralar", "layout": "flow", "nodes": [{"label": "Lav nehir gibi akar", "emoji": "🌋"}, {"label": "Lav tüpü kalır", "emoji": "🕳️"}, {"label": "Deniz mağarası: dalga aşındırır", "emoji": "🌊"}]}, ["🌋", "🌊"], ["LAV", "LAV TÜPÜ", "DENİZ MAĞARASI"])
S(1, {"type": "big-number", "value": "Buzul mağarası", "label": "Buzulun kenarındaki erime buzun içinde mağara açar", "sub": "Milli Parklar Servisi", "icon": "🧊"}, ["🧊", "❄️"], ["BUZUL MAĞARASI"])
S(2, {"type": "spotlight", "title": "Mağara sakinleri", "emoji": "🦇", "chips": [{"label": "Küçük, sıra dışı hayvanlar", "emoji": "🦗"}, {"label": "Yarasa tünekleri", "emoji": "🦇"}]}, ["🦇", "📶"], ["MAĞARA CANLILARI", "WI-FI YOK 📶"])
S(2, {"type": "bullets", "title": "Sen de dene: şeker mağarası", "items": ["Tabağa bir şeker küpü koy", "Damla damla su damlat", "Su şekeri nasıl oyuyor?", "Kireçtaşı çok daha yavaş çözünür"]}, ["🍬", "💧"], ["DENEY ZAMANI 🔬", "DAMLA DAMLA"])
S(1, {"type": "big-number", "value": "400 mil+", "label": "Mamut Mağarası: Dünya'nın en uzun mağarası", "sub": "Milli Parklar Servisi", "icon": "🦣"}, ["🦣", "🗺️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Tavandan sarkan taş saçaklara ne denir?", "emoji": "🤔"}, ["🥕", "🧊"], ["HIZLI SORU!", "SARKIT ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 41, "videoTitle": "Mağaralar nasıl oluşur?", "paperTitleTr": "Mağaralar nasıl oluşur?",
  "theme": {"backdrop": "underground", "actors": [{"kind": "fly", "emoji": "🦇", "every": 34}]},
  "takeaways": ["Asidik yağmur suyu kireçtaşını çok yavaş çözerek erime mağaralarını oyar", "Damlayan su sarkıtları, dikitleri ve sütunları oluşturur", "Lav tüpleri, deniz mağaraları ve buzul mağaraları da vardır"],
  "description": "Mağaralar nasıl oluşur? Bu bölümde karbonik asidin kireçtaşını nasıl çözdüğünü, düdenleri ve karst bölgelerini, mağaraların ne kadar yavaş büyüdüğünü, sarkıtları, dikitleri ve sütunları, lav tüplerini, deniz ve buzul mağaralarını ve mağara canlılarını keşfediyoruz. Sonunda şeker küpü deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kireçtaşı", "meaning": "Asitli suda yavaşça çözünebilen bir kayaç."},
    {"term": "Karbonik asit", "meaning": "Karbondioksitin suda çözünmesiyle oluşan zayıf asit."},
    {"term": "Karst", "meaning": "Çözünebilir kayaçların bulunduğu, mağara ve düdenlerle dolu bölge."},
    {"term": "Düden", "meaning": "Kayacın çözünmesiyle yerde açılan çukur."},
    {"term": "Sarkıt", "meaning": "Mağara tavanından aşağı sarkan taş saçak."},
    {"term": "Dikit", "meaning": "Damlayan suyun yerde biriktirdiği, yukarı doğru büyüyen taş."},
    {"term": "Lav tüpü", "meaning": "Akan lavın geride bıraktığı boş tünel."}],
  "song": e.song("Damla Damla", [("💧", "Damla"), ("🪨", "Kireçtaşı"), ("🕳️", "Mağara"), ("🏛️", "Sütun"), ("🦇", "Yarasa")],
    ["Yağmur düştü toprağa", "Karbondioksitle asit oldu", "Kireçtaşına sızdı yavaşça", "Taşı çözdü, boşluk açtı"],
    ["Damla damla, yıl be yıl!", "Su oyar, mağara büyür", "Sarkıt iner, dikit çıkar", "Birleşince sütun olur"],
    ["Lav akar, tünel bırakır", "Dalga döver, deniz mağarası", "Buzul erir, buz mağarası", "Yarasalar tavanda uyur"],
    ["Damla damla, yıl be yıl!", "Su oyar, mağara büyür", "Şekere su damlat, izle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🦇"}, {"kind": "hop", "emoji": "💧"}, {"kind": "dig", "emoji": "⛏️"}, {"kind": "hop", "emoji": "🔦"}])}
e.write(D, facts, script)
