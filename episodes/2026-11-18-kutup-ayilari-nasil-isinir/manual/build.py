"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kutup-ayilari-nasil-isinir"
NG = "National Geographic — Polar Bear"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Polar Bear", "publisher": "National Geographic", "url": "https://www.nationalgeographic.com/animals/mammals/facts/polar-bear"}],
  "facts": [
    F(1, "Kutup ayıları Arktik buz örtülerinde dolaşır ve bölgenin kıyı sularında yüzer.", "Polar bears roam the Arctic ice sheets and swim in that region's coastal waters.", NG),
    F(2, "Kutup ayıları, ısıtan bir yağ katmanını örten kalın, yalıtkan bir kürke dayanır.", "depend on a thick coat of insulated fur, which covers a warming layer of fat.", NG),
    F(3, "Kutup ayılarının kürkünün altında siyah deri vardır; bu deri güneşin ısıtan ışınlarını daha iyi emer.", "But under their fur, polar bears have black skin—the better to soak in the sun's warming rays.", NG),
    F(4, "Ayının bembeyaz kürkü, çevredeki kar ve buzda kamuflaj sağlar.", "The bear's stark white coat provides camouflage in surrounding snow and ice.", NG),
    F(5, "Pençelerinin altında bile kürk büyür; bu, soğuk yüzeylere karşı korur ve buzda iyi tutunma sağlar.", "Fur even grows on the bottom of their paws, which protects against cold surfaces and provides a good grip on ice.", NG),
    F(6, "Kutup ayıları çok güçlü yüzücülerdir; kürek gibi kullandıkları büyük ön pençeleri hafifçe perdelidir; bazıları karadan yüzlerce mil uzakta yüzerken görülmüştür.", "They are very strong swimmers, and their large front paws, which they use to paddle, are slightly webbed. / Some polar bears have been seen swimming hundreds of miles from land", NG),
    F(7, "Bu güçlü avcılar genellikle fokları avlar; fokların nefes almak için yüzeye çıkabildiği, buzun kayıp çatladığı bölgeleri dolaşırlar; fırsat bulunca ölü balina gibi leşleri de yerler; etçildirler.", "These powerful predators typically prey on seals. / In search of this quarry they frequent areas of shifting, cracking ice where seals may surface to breathe air. / If the opportunity presents itself, polar bears will also consume carcasses, such as those of dead whales. / Diet: Carnivore", NG),
    F(8, "Kutup ayısının bilimsel adı Ursus maritimus'tur; bir memelidir.", "Scientific Name: Ursus maritimus / Type: Mammals", NG),
    F(9, "Dişiler derin kar yığınlarını kazarak in yapar; bu inler onları Arktik koşullarından korur ve yalıtır; kışın genellikle ikiz doğururlar.", "Females den by digging into deep snow drifts, which provide protection and insulation from the Arctic elements. / They give birth in winter, usually to twins.", NG),
    F(10, "Kutup ayılarının doğadaki ortalama ömrü 25 ile 30 yıldır.", "Average Life Span In The Wild: 25 to 30 years", NG, ["25", "30"]),
    F(11, "Kutup ayısı IUCN Kırmızı Listesi'nde 'hassas' olarak sınıflandırılır.", "IUCN Red List Status: Vulnerable", NG),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Buzlu bir denizde yüzmeyi düşün. Brrr! Bir dakika bile dayanamazsın, değil mi? Ama kutup ayıları buzlu sularda rahatça yüzer!", [1, 6]),
    L("Bu dev beyaz ayılar donmuş dünyada nasıl sıcak kalır?"),
    L("Bugün Arktik'e, kutup ayılarının evine gidiyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kutup ayıları nasıl ısınır? Buzda ve suda nasıl hareket eder? Ve ne yerler?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre kutup ayıları Arktik buz örtülerinde dolaşır ve kıyı sularında yüzer.", [1], f"{NGs}'e göre kutup ayıları Arktik buz örtülerinde dolaşır ve kıyı sularında yüzer."),
    L("Kutup ayısı bir memelidir. Bilimsel adı Ursus maritimus'tur.", [8], "Kutup ayısı bir memelidir. Bilimsel adı Ursus maritimus'tur."),
    L("Isınmanın ilk sırrı: kalın, yalıtkan bir kürk.", [2]),
    L("Yalıtkan demek, ısının kaçmasını zorlaştıran demek. Kürk, vücut ısısını içeride tutan bir mont gibidir.", [2]),
    L("İkinci sır kürkün altında saklı: kalın bir yağ katmanı. Bu yağ, ayıyı içeriden ısıtan ikinci bir kat gibidir.", [2]),
    L("Benim de iki katmanım var: metal kasam ve boyam. Ama ikisi de beni ısıtmıyor!"),
])
e.sec("finding", [
    L("Üçüncü sır daha da şaşırtıcı: Kutup ayısının kürkü beyaz ama derisi siyahtır!", [3]),
    L("National Geographic'e göre bu siyah deri, güneşin ısıtan ışınlarını daha iyi emer.", [3], f"{NGs}'e göre bu siyah deri, güneşin ısıtan ışınlarını daha iyi emer."),
    L("Peki kürk neden beyaz? Bembeyaz kürk, kar ve buzun arasında kamuflaj sağlar. Ayı çevresine karışır.", [4]),
    L("Ben kara karışamam. Gümüş rengim hemen göze batıyor!"),
    L("Dördüncü sır ayaklarında: Pençelerinin altında bile kürk vardır!", [5]),
    L("Bu kürk, ayının ayaklarını soğuk yüzeylere karşı korur ve buzda kaymadan yürümesini sağlar.", [5]),
])
e.sec("importance", [
    L("Kutup ayıları çok güçlü yüzücülerdir. Büyük ön pençelerini kürek gibi kullanırlar ve bu pençeler hafifçe perdelidir.", [6]),
    L("Bazı kutup ayıları karadan yüzlerce mil uzakta yüzerken görülmüştür!", [6]),
    L("Kutup ayıları etçildir ve genellikle fok avlar.", [7]),
    L("Fokların nefes almak için yüzeye çıkabildiği, buzun kayıp çatladığı yerlerde beklerler.", [7]),
    L("Fırsat bulurlarsa ölü balina gibi leşleri de yerler. Yani yemek seçmezler!", [7]),
    L("Yavrular kar altındaki sıcak inlerde doğar. Dişiler derin kar yığınlarını kazarak in yapar; bu in onları korur ve yalıtır.", [9]),
    L("Kışın genellikle ikiz doğururlar.", [9]),
    L("Şimdi sıra sende! Bir yetişkinle bir kaba buzlu su koy. Elini çok kısa bir süre suya sok ve soğuğu hisset.", [2]),
    L("Sonra elini bir poşete koy, poşetin etrafını bitkisel katı yağla dolu başka bir poşetle sar ve tekrar dene. Fark var mı? İşte yağ katmanı! Elini fazla bekletme.", [2]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? National Geographic'e göre kutup ayıları doğada ortalama 25 ile 30 yıl yaşar. Ve IUCN Kırmızı Listesi'nde 'hassas' tür olarak sınıflandırılırlar.", [10, 11], f"Bunu biliyor muydun? {NGs}'e göre kutup ayıları doğada ortalama yirmi beş ile otuz yıl yaşar. Ve Ay Yu Si En Kırmızı Listesi'nde hassas tür olarak sınıflandırılırlar."),
    L("Hızlı soru! Kutup ayısının kürkünün altındaki derisi ne renktir?", [3]),
    L("Düşün bakalım... Evet: siyah!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Sıkı giyin, görüşürüz!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kutup ayıları nasıl ısınır?", "emoji": "🐻‍❄️"}, ["🧊", "❄️"], ["BUZLU DENİZ", "NASIL ISINIR?", "ARKTİK"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kutup ayıları nasıl ısınır?", "Buzda ve suda nasıl hareket eder?", "Ne yerler?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Kutup ayısı", "emoji": "🐻‍❄️", "chips": [{"label": "Arktik buzunda dolaşır", "emoji": "🧊"}, {"label": "Kıyı sularında yüzer", "emoji": "🌊"}, {"label": "Memeli: Ursus maritimus", "emoji": "🔬"}]}, ["🧊", "🌊"], ["ARKTİK", "MEMELİ"])
S(3, {"type": "stages", "title": "Isı kalkanı", "rows": [{"label": "Kalın, yalıtkan kürk", "emoji": "🧥"}, {"label": "Isıyı içeride tutar", "emoji": "🔥"}, {"label": "Altında yağ katmanı", "emoji": "🧈"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 2, "note": "Şematik çizim."}, [], ["KÜRK", "YALITKAN", "YAĞ KATMANI"])
S(1, {"type": "big-number", "value": "İki kat", "label": "Kürk + yağ: ayıyı sıcak tutar", "sub": "National Geographic", "icon": "🧥"}, ["🤖", "🧥"], ["METAL KASA 🤖"])
S(3, {"type": "comparison", "title": "Beyaz kürk, siyah deri", "left": {"title": "Siyah deri ⚫", "items": ["Güneş ışınlarını emer"]}, "right": {"title": "Beyaz kürk ⚪", "items": ["Kar ve buzda kamuflaj"]}}, ["☀️", "❄️"], ["SİYAH DERİ!", "GÜNEŞİ EMER", "KAMUFLAJ"], fx="sparkle")
S(3, {"type": "spotlight", "title": "Kürklü pençeler", "emoji": "🐾", "chips": [{"label": "Pençe altında kürk", "emoji": "🐾"}, {"label": "Soğuğa karşı korur", "emoji": "🥶"}, {"label": "Buzda tutunma", "emoji": "⛸️"}]}, ["🐾", "🪩"], ["GÜMÜŞ MUMA 🪩", "KÜRKLÜ PENÇE", "KAYMAZ"])
S(2, {"type": "meter", "title": "Usta yüzücü", "label": "Yüzme", "emoji": "🏊", "phases": [{"label": "Ön pençeler kürek gibi", "level": 0.7, "emoji": "🚣"}, {"label": "Karadan yüzlerce mil uzakta", "level": 0.95, "emoji": "🌊"}], "note": NOTE}, ["🌊", "🚣"], ["PERDELİ PENÇE", "YÜZLERCE MİL"])
S(3, {"type": "diagram", "title": "Kutup ayısının sofrası", "layout": "flow", "nodes": [{"label": "Etçil: fok avlar", "emoji": "🦭"}, {"label": "Çatlayan buzda bekler", "emoji": "🧊"}, {"label": "Leş de yer", "emoji": "🐋"}]}, ["🦭", "🐋"], ["ETÇİL", "FOK AVI", "SEÇMEZ"])
S(2, {"type": "big-number", "value": "Genellikle ikiz", "label": "Kışın kar inlerinde doğan yavrular", "sub": "National Geographic", "icon": "🐻‍❄️"}, ["❄️", "🏠"], ["KAR İNİ", "İKİZLER"])
S(2, {"type": "bullets", "title": "Sen de dene: yağ eldiveni", "items": ["Bir yetişkinle buzlu su hazırla", "Elini kısa süre sok", "Yağ dolu poşetle sarıp tekrar dene", "Elini fazla bekletme!"], "tone": "caution"}, ["🧈", "🧊"], ["DENEY ZAMANI 🔬", "YAĞ KATMANI"])
S(1, {"type": "spotlight", "title": "Kutup ayısı bilgi kartı", "emoji": "📋", "chips": [{"label": "Doğada 25–30 yıl yaşar", "emoji": "⏳"}, {"label": "IUCN: hassas tür", "emoji": "⚠️"}]}, ["⏳", "⚠️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Kutup ayısının derisi ne renk?", "emoji": "🤔"}, ["⚫", "🐻‍❄️"], ["HIZLI SORU!", "SİYAH ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 44, "videoTitle": "Kutup ayıları nasıl ısınır?", "paperTitleTr": "Kutup ayıları nasıl ısınır?",
  "theme": {"backdrop": "aurora", "actors": [{"kind": "walk", "emoji": "🐻‍❄️", "every": 32}]},
  "takeaways": ["Kalın, yalıtkan kürk ve altındaki yağ katmanı kutup ayısını sıcak tutar", "Siyah deri güneşi emer, beyaz kürk kamuflaj sağlar, kürklü pençeler buzda tutunur", "Güçlü yüzücülerdir ve genellikle fok avlarlar"],
  "description": "Kutup ayıları donmuş Arktik'te nasıl sıcak kalır? Bu bölümde kalın ve yalıtkan kürkü, yağ katmanını, beyaz kürkün altındaki siyah deriyi, kürklü pençeleri, usta yüzücülüğü, fok avını ve kar inlerinde doğan yavruları keşfediyoruz. Sonunda yağ eldiveni deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Arktik", "meaning": "Dünya'nın kuzey kutbu çevresindeki soğuk bölge."},
    {"term": "Yalıtkan", "meaning": "Isının kaçmasını zorlaştıran."},
    {"term": "Kamuflaj", "meaning": "Bir canlının çevresine uyum sağlayarak gizlenmesi."},
    {"term": "Etçil", "meaning": "Başka hayvanların etiyle beslenen."},
    {"term": "Leş", "meaning": "Ölmüş bir hayvanın bedeni."},
    {"term": "Hassas tür", "meaning": "Nesli tehlike altına girebilecek durumdaki tür."}],
  "song": e.song("Beyaz Dev", [("🐻‍❄️", "Kutup ayısı"), ("🧊", "Buz"), ("🦭", "Fok"), ("🐾", "Pençe"), ("❄️", "Kar")],
    ["Arktik'te esen buz gibi rüzgâr", "Kalın kürk sarar her yanımı", "Altında yağ katmanı var", "Soğuk geçemez içime"],
    ["Beyaz dev, buzun kralı!", "Kürkün beyaz, derin siyah", "Güneşi emer, ısınırsın", "Karın içinde kaybolursun"],
    ["Pençelerin kürklü, kaymazsın", "Kürek gibi yüzersin denizde", "Buz çatlağında fok beklersin", "Kar ininde ikizler uyur"],
    ["Beyaz dev, buzun kralı!", "Kürkün beyaz, derin siyah", "Yağ eldivenini dene, hisset", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "walk", "emoji": "🐻‍❄️"}, {"kind": "swim", "emoji": "🦭"}, {"kind": "hop", "emoji": "❄️"}, {"kind": "hop", "emoji": "🧊"}])}
e.write(D, facts, script)
