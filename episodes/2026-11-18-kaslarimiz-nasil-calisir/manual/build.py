"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kaslarimiz-nasil-calisir"
KH = "Nemours KidsHealth — Bones, Muscles & Joints"; CC = "Cleveland Clinic — Muscle"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Bones, Muscles & Joints", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/muscles.html"},
    {"id": "k2", "title": "Muscle", "publisher": "Cleveland Clinic", "url": "https://my.clevelandclinic.org/health/body/21887-muscle"}],
  "facts": [
    F(1, "Vücudumuzda neredeyse sürekli kullandığımız 600'den fazla kas vardır.", "You have more than 600 muscles in your body that you use almost constantly.", CC, ["600"]),
    F(2, "İnsanlarda üç tür kas vardır: iskelet kası, düz kas ve kalp kası.", "Humans have three different kinds of muscle: / There are three types of muscle tissue in your body:", KH + "; " + CC),
    F(3, "İskelet kası bacaklarda, kollarda ve yüzde olduğu gibi kemiğe kordon gibi tendonlarla bağlıdır; hareketlerini kontrol edebildiğimiz için istemli kas denir.", "Skeletal muscle is attached by cord-like tendons to bone, such as in the legs, arms, and face. / known as voluntary muscles because you can control their movement", KH),
    F(4, "İskelet kasları hızlı ve güçlü kasılabilir ama çabuk yorulur.", "They can contract (shorten or tighten) quickly and powerfully, but they tire easily.", KH),
    F(5, "Düz kaslar istemsizdir; onları bilinçli olarak kontrol edemeyiz, sinir sistemi otomatik olarak kontrol eder; bazı organların içini kaplarlar.", "Smooth, or involuntary, muscle / We can't consciously control our smooth muscles; rather, they're controlled by the nervous system automatically / Smooth muscles are involuntary muscles that line the inside of some organs.", KH + "; " + CC),
    F(6, "Kalp kası kalpte bulunur; ritmik ve güçlü kasılmalarıyla kanı kalpten dışarı iter; kalp istemsiz bir kastır, kendiliğinden atar ve günde binlerce kez atar.", "Cardiac muscle is found in the heart. / Its rhythmic, powerful contractions force blood out of the heart as it beats. / Your heart is an involuntary muscle — it beats on its own without your input. / beats thousands of times a day to keep you alive.", KH + "; " + CC),
    F(7, "Kaslar vücut bölümlerini kasılıp gevşeyerek hareket ettirir; kaslar eklemleri çekerek hareket etmemizi sağlar.", "Muscles move body parts by contracting and then relaxing. / Muscles pull on the joints, allowing us to move.", KH),
    F(8, "Kaslar kemikleri çekebilir ama geri itemez; bu yüzden bükücü ve açıcı kaslar olarak çiftler halinde çalışır; üst kolun önündeki biseps bükücü, arkasındaki triseps açıcıdır.", "Muscles can pull bones, but they can't push them back to the original position. / So they work in pairs of flexors and extensors. / the biceps muscle, in the front of the upper arm, is a flexor / the triceps, at the back of the upper arm, is an extensor", KH),
    F(9, "Kaslar birbirine örülmüş binlerce küçük liften oluşur; bazı kas lifleri hızlı kasılır ve kısa enerji patlamaları kullanır.", "Your muscles are made of thousands of small fibers woven together. / Some muscle fibers contract quickly and use short bursts of energy (fast-twitch muscles).", CC),
    F(10, "Kasların hareketlerini beyin ve sinir sistemi düzenler ve kontrol eder.", "The movements your muscles make are coordinated and controlled by the brain and nervous system.", KH),
    F(11, "Hiç kıpırdamadan otururken bile vücudumuzdaki kaslar sürekli hareket eder.", "Even when we sit perfectly still, muscles throughout the body are constantly moving.", KH),
    F(12, "Egzersizden önce esneme ve ısınma kas sakatlıklarını önlemenin en iyi yoludur.", "Stretching and warming up before exercise or physical activity are the best ways to prevent muscle injuries.", CC),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; CCs = "Klivlınd Klinik"
e.sec("hook", [
    L("Şu an hiç kıpırdamadan oturuyor olabilirsin. Ama KidsHealth'e göre o sırada bile vücudundaki kaslar sürekli hareket ediyor!", [11], f"Şu an hiç kıpırdamadan oturuyor olabilirsin. Ama {KHs}'e göre o sırada bile vücudundaki kaslar sürekli hareket ediyor!"),
    L("Kalbin atıyor, gözlerin kırpıyor. Peki bunları kim yapıyor?", [6]),
    L("Bugün vücudunun motorlarına, yani kaslara bakıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kaç tür kasımız var? Kaslar nasıl kasılır? Ve neden çiftler halinde çalışırlar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Cleveland Clinic'e göre vücudunda 600'den fazla kas var ve onları neredeyse sürekli kullanıyorsun.", [1], f"{CCs}'e göre vücudunda altı yüzden fazla kas var ve onları neredeyse sürekli kullanıyorsun."),
    L("Benim de motorlarım var, ama sadece on iki tane. Yine de çok hareketliyim!"),
    L("Kasların üç türü vardır: iskelet kası, düz kas ve kalp kası.", [2]),
    L("İskelet kasları kemiklere tendon denen kordon gibi bağlarla tutunur. Kollarında, bacaklarında, yüzünde bulunurlar.", [3]),
    L("Onları sen kontrol edersin: gülümsemek de, zıplamak da senin elinde. Bu yüzden onlara istemli kas denir.", [3]),
    L("İskelet kasları hızlı ve güçlü kasılabilir ama çabuk yorulur.", [4]),
])
e.sec("finding", [
    L("Düz kaslar ise bazı organlarının içini kaplar. Onları bilinçli olarak kontrol edemezsin; sinir sistemi onları kendiliğinden yönetir.", [5]),
    L("Bu yüzden onlara istemsiz kas denir.", [5]),
    L("Üçüncü tür, kalp kasıdır. Kalp kası ritmik ve güçlü kasılmalarla kanı kalpten dışarı iter.", [6]),
    L("Kalbin de istemsiz bir kastır: senden izin almadan atar. Hem de günde binlerce kez!", [6]),
    L("Benim kalbim yok ama bir fanım var. O da senden izin almadan döner, bazen de vızıldar!"),
])
e.sec("importance", [
    L("Peki bir kas nasıl çalışır? Kaslar birbirine örülmüş binlerce küçük liften oluşur.", [9]),
    L("Lifler kasılınca kas kısalır, gevşeyince eski haline döner. Kaslar böylece eklemleri çekerek seni hareket ettirir.", [7]),
    L("Bazı kas lifleri çok hızlı kasılır ve kısa enerji patlamaları kullanır. Bir koşuya hızlı başlarken onları kullanırsın.", [9]),
    L("İşte işin sırrı: Kaslar kemikleri çekebilir ama geri itemez!", [8]),
    L("Bu yüzden çiftler halinde çalışırlar. Üst kolunun önündeki biseps kolunu büker, arkasındaki triseps ise açar.", [8]),
    L("Bütün bu hareketleri beynin ve sinir sistemin düzenler.", [10]),
    L("Şimdi sıra sende! Bir elini diğer kolunun üst kısmına, önüne koy. Sonra dirseğini yavaşça bük.", [8]),
    L("Biseps sertleşiyor mu? Şimdi elini kolunun arkasına koy ve kolunu düzelt: bu kez triseps çalışıyor!", [8]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Cleveland Clinic'e göre kas sakatlıklarını önlemenin en iyi yolu, egzersizden önce esnemek ve ısınmaktır.", [12], f"Bunu biliyor muydun? {CCs}'e göre kas sakatlıklarını önlemenin en iyi yolu, egzersizden önce esnemek ve ısınmaktır."),
    L("Hızlı soru! Kalp kası istemli mi, istemsiz mi?", [6]),
    L("Düşün bakalım... Evet: istemsiz!", [6]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Hadi kalk, biraz esne!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kaslarımız nasıl çalışır?", "emoji": "💪"}, ["🏃", "❤️"], ["HEP HAREKETTE", "KALP • GÖZ", "MOTORLAR"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kaç tür kasımız var?", "Kaslar nasıl kasılır?", "Neden çiftler halinde çalışırlar?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "big-number", "value": "600+", "label": "Vücudundaki kas sayısı", "sub": "Cleveland Clinic", "icon": "💪"}, ["💪", "🤖"], ["600'DEN FAZLA", "MOTORLU MUMA 🤖"])
S(1, {"type": "diagram", "title": "Üç tür kas", "layout": "flow", "nodes": [{"label": "İskelet kası", "emoji": "🦵"}, {"label": "Düz kas", "emoji": "🌀"}, {"label": "Kalp kası", "emoji": "❤️"}]}, ["🦵", "❤️"], ["ÜÇ TÜR"])
S(3, {"type": "spotlight", "title": "İskelet kası", "emoji": "🦵", "chips": [{"label": "Tendonla kemiğe bağlı", "emoji": "🦴"}, {"label": "İstemli: sen kontrol edersin", "emoji": "🎮"}, {"label": "Hızlı, güçlü ama çabuk yorulur", "emoji": "⚡"}]}, ["🦴", "🏋️"], ["TENDON", "İSTEMLİ", "ÇABUK YORULUR"])
S(3, {"type": "comparison", "title": "Düz kas ve kalp kası", "left": {"title": "Düz kas 🌀", "items": ["Organların içini kaplar", "İstemsiz"]}, "right": {"title": "Kalp kası ❤️", "items": ["Kanı dışarı iter", "Günde binlerce kez atar"]}}, ["🧠", "❤️"], ["DÜZ KAS", "İSTEMSİZ", "KALP KASI"])
S(2, {"type": "meter", "title": "Kalp", "label": "Kasılma", "emoji": "❤️", "phases": [{"label": "Senden izin almadan atar", "level": 0.85, "emoji": "💓"}, {"label": "Muma'nın fanı da döner", "level": 0.4, "emoji": "🌀"}], "note": NOTE}, ["💓", "🌀"], ["BİNLERCE ATIŞ", "FAN 🌀"], fx="shake")
S(3, {"type": "stages", "title": "Kas nasıl kasılır?", "rows": [{"label": "Binlerce lif", "emoji": "🧵"}, {"label": "Lifler kasılır: kas kısalır", "emoji": "↔️"}, {"label": "Eklem çekilir: hareket!", "emoji": "🦾"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 1, "note": "Şematik çizim."}, [], ["KAS LİFLERİ", "KASIL VE GEVŞE", "HIZLI LİFLER"])
S(3, {"type": "diagram", "title": "Kas çifti", "layout": "cycle", "nodes": [{"label": "Biseps kasılır: kol bükülür", "emoji": "💪"}, {"label": "Triseps kasılır: kol açılır", "emoji": "🦾"}]}, ["💪", "🧠"], ["ÇEKER, İTEMEZ!", "BİSEPS • TRİSEPS", "BEYİN YÖNETİR"])
S(2, {"type": "bullets", "title": "Sen de dene: kasını hisset", "items": ["Elini üst kolunun önüne koy", "Dirseğini bük: biseps sertleşir", "Elini kolunun arkasına koy", "Kolunu düzelt: triseps çalışır"]}, ["💪", "✋"], ["DENEY ZAMANI 🔬", "TRİSEPS İŞ BAŞINDA"])
S(1, {"type": "spotlight", "title": "Kaslarını koru", "emoji": "🤸", "chips": [{"label": "Önce esne", "emoji": "🧘"}, {"label": "Isın", "emoji": "🔥"}]}, ["🧘", "🏃"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Kalp kası istemli mi, istemsiz mi?", "emoji": "🤔"}, ["❤️", "💓"], ["HIZLI SORU!", "İSTEMSİZ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 37, "videoTitle": "Kaslarımız nasıl çalışır?", "paperTitleTr": "Kaslarımız nasıl çalışır?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "hop", "emoji": "🐇", "every": 30}]},
  "takeaways": ["Üç tür kasımız var: iskelet, düz ve kalp kası", "Kas lifleri kasılıp gevşeyerek eklemleri çeker", "Kaslar itemez, çeker; bu yüzden biseps ve triseps gibi çiftler halinde çalışır"],
  "description": "Kaslarımız bizi nasıl hareket ettirir? Bu bölümde vücudumuzdaki altı yüzden fazla kası, iskelet, düz ve kalp kasını, istemli ve istemsiz hareketleri, tendonları, kas liflerinin kasılmasını ve biseps ile trisepsin çift olarak çalışmasını keşfediyoruz. Sonunda kolundaki kasları hissetme etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "İskelet kası", "meaning": "Kemiklere bağlı, isteyerek hareket ettirdiğimiz kas."},
    {"term": "Düz kas", "meaning": "Bazı organların içini kaplayan, istemsiz çalışan kas."},
    {"term": "Kalp kası", "meaning": "Kalbi oluşturan, kendiliğinden kasılan kas."},
    {"term": "Tendon", "meaning": "Kası kemiğe bağlayan kordon gibi bağ."},
    {"term": "İstemli", "meaning": "İsteyerek kontrol edebildiğimiz."},
    {"term": "İstemsiz", "meaning": "Biz düşünmeden kendiliğinden çalışan."},
    {"term": "Kas lifi", "meaning": "Kası oluşturan, kasılabilen ince iplikler."}],
  "song": e.song("Çek ve Bırak", [("💪", "Biseps"), ("🦾", "Triseps"), ("❤️", "Kalp"), ("🦴", "Tendon"), ("🧠", "Beyin")],
    ["Altı yüzden fazla motor var", "Kemiklere tendonla bağlı", "İskelet kası benim emrimde", "Hızlı, güçlü, çabuk yorulur"],
    ["Çek ve bırak, kasıl ve gevşe!", "Biseps büker, triseps açar", "Kaslar iter mi? Hayır, çeker!", "Çift çift çalışır hepsi"],
    ["Düz kaslar kendi işini yapar", "Kalp atar, izin istemez", "Binlerce lif örülmüş birlikte", "Beynim yönetir her adımı"],
    ["Çek ve bırak, kasıl ve gevşe!", "Biseps büker, triseps açar", "Önce esne, sonra koş", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "🐇"}, {"kind": "hop", "emoji": "💪"}, {"kind": "hop", "emoji": "❤️"}, {"kind": "walk", "emoji": "🏃"}])}
e.write(D, facts, script)
