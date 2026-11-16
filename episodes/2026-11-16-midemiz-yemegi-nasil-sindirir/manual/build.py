"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:midemiz-yemegi-nasil-sindirir"
KH = "Nemours KidsHealth — Your Digestive System"; NI = "NIDDK (NIH) — Your Digestive System & How It Works"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Your Digestive System", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/digestive-system.html"},
    {"id": "k2", "title": "Your Digestive System & How It Works", "publisher": "NIDDK", "url": "https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works"}],
  "facts": [
    F(1, "Besin yakıtımızdır; besin öğeleri hücrelere çalışmak için gereken enerjiyi ve maddeleri verir; ama önce vücudun emip kullanabileceği küçük parçalara sindirilmelidir.", "Food is our fuel, and its nutrients give our bodies' cells the energy and substances they need to work. / But before food can do that, it must be digested into small pieces the body can absorb and use.", KH),
    F(2, "Sindirim sistemi besin öğelerini vücudun emip enerji için kullanabileceği kadar küçük parçalara ayırır.", "Your digestive system breaks nutrients into parts small enough for your body to absorb and use for energy", NI),
    F(3, "Sindirim ağızda, besin mideye ulaşmadan çok önce başlar; dişler besini koparıp doğrar, tükürük onu ıslatır; tükürüğü tükürük bezleri yapar.", "Digestion begins in the mouth, well before food reaches the stomach. / As the teeth tear and chop the food, spit moistens it for easy swallowing. / Your salivary glands make saliva, a digestive juice", KH + "; " + NI),
    F(4, "Tükürükteki amilaz adlı sindirim enzimi bazı karbonhidratları parçalamaya başlar; tükürükteki enzim nişastaları parçalamaya başlar.", "A digestive enzyme in saliva called amylase (AH-meh-lace) starts to break down some of the carbohydrates / Saliva also has an enzyme that begins to break down starches in your food.", KH + "; " + NI),
    F(5, "Yemeği koklamak ya da düşünmek bile ağzı sulandırabilir; beyin tükürük bezlerine sinyal gönderir.", "Just by smelling that homemade apple pie or thinking about how delicious that ripe tomato is going to be / your brain sends a signal that causes your salivary glands to \"make your mouth water\" to prepare you to eat.", KH + "; " + NI),
    F(6, "Yutarken dil besini boğaza iter; epiglot denen küçük doku kapağı boğulmayı önlemek için soluk borusunun üstüne kapanır.", "When you swallow, your tongue pushes the food into your throat. / A small flap of tissue, called the epiglottis, folds over your windpipe to prevent choking", NI),
    F(7, "Peristalsis denen kas kasılma dalgaları besini yemek borusundan mideye iter.", "Waves of muscle contractions called peristalsis (per-uh-STALL-sus) force food down through the esophagus to the stomach.", KH),
    F(8, "Yemek borusunun sonundaki sfinkter genelde kapalı durur ve mide içeriğinin yemek borusuna geri akmasını engeller.", "This sphincter usually stays closed to keep what’s in your stomach from flowing back into your esophagus.", NI),
    F(9, "Mide kasları besini asit ve enzim içeren sindirim sıvılarıyla çalkalayıp karıştırır; mide duvarındaki bezler mide asidi ve enzim yapar; midedeki sindirim için asitli ortam gerekir.", "The stomach muscles churn and mix the food with digestive juices that have acids and enzymes / Glands in your stomach lining make stomach acid and enzymes that break down food. / An acidic environment is needed for the digestion that takes place in the stomach.", KH + "; " + NI),
    F(10, "Mide, kimus denen içeriğini yavaş yavaş ince bağırsağa boşaltır; midenin çıkışındaki ceviz büyüklüğündeki pilor kapağı kimusu midede tutar.", "The stomach slowly empties its contents, called chyme, into your small intestine. / A walnut-sized muscular valve at the outlet of the stomach called the pylorus (pie-LOR-us) keeps chyme in the stomach", NI + "; " + KH),
    F(11, "İnce bağırsağa uzunluğu yüzünden değil genişliği yüzünden ince denir; aslında kalın bağırsaktan çok daha uzundur.", "The small intestine is called small because of its width, not its length. It's actually much longer than the large intestine.", KH),
    F(12, "İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi villus ile kaplıdır; besinler villuslar aracılığıyla kana emilir; ince bağırsak duvarları suyu ve sindirilmiş besinleri kana emer.", "The inner wall of the small intestine is covered with millions of microscopic, finger-like projections called villi (VIH-lie). / The villi are the vehicles through which nutrients can be absorbed into the blood. / The walls of the small intestine absorb water and the digested nutrients into your bloodstream.", KH + "; " + NI),
    F(13, "İnce bağırsağın kasları besini pankreas, karaciğer ve bağırsaktan gelen sindirim sıvılarıyla karıştırır; karaciğer yağların sindirimine yardım eden safrayı yapar; safra kesesi safrayı öğünler arasında saklar; pankreas karbonhidrat, yağ ve proteinleri parçalayan enzimler yapar.", "The muscles of the small intestine mix food with digestive juices from the pancreas, liver, and intestine / Your liver makes a digestive juice called bile that helps digest fats and some vitamins. / Your gallbladder stores bile between meals. / Your pancreas makes a digestive juice that has enzymes that break down carbohydrates, fats, and proteins.", NI),
    F(14, "Kalın bağırsak suyu emer ve atığı sıvıdan katı dışkıya dönüştürür.", "The large intestine absorbs water and changes the waste from liquid into stool. / The large intestine's main job is to remove water from the undigested matter and form solid waste (poop) to be excreted.", NI + "; " + KH),
    F(15, "Kalın bağırsaktaki bakteriler kalan besin öğelerini parçalamaya yardım eder ve K vitamini yapar.", "Bacteria in your large intestine help break down remaining nutrients and make vitamin K.", NI),
    F(16, "Bir yetişkinin sindirim kanalı yaklaşık 9 metre uzunluğundadır.", "An adult's digestive tract is about 30 feet (about 9 meters) long.", KH, ["9"]),
    F(17, "Vücudun besini tamamen sindirmesi saatler sürer.", "It takes hours for our bodies to fully digest food.", KH),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; ND = "En Ay Di Di Key"
e.sec("hook", [
    L("Az önce bir dilim ekmek yedin. Peki o ekmek şimdi nerede ve ona ne oluyor?"),
    L("Yediğin her lokma, vücudunun içinde uzun bir yolculuğa çıkar.", [16]),
    L("Bugün bu yolculuğa biz de katılıyoruz: sindirim kanalının içine giriyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Sindirime neden ihtiyacımız var? Lokma hangi yollardan geçer? Ve vücut onu nasıl kullanır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre besin bizim yakıtımızdır. İçindeki besin öğeleri hücrelerimize enerji ve gereken maddeleri verir.", [1], f"{KHs}'e göre besin bizim yakıtımızdır. İçindeki besin öğeleri hücrelerimize enerji ve gereken maddeleri verir."),
    L("Ama önce vücudun emebileceği küçük parçalara ayrılması gerekir. İşte buna sindirim denir.", [1, 2]),
    L("Ben de yakıtla çalışırım, ama benimki bir priz. Hiç çiğnemem gerekmiyor!"),
    L("Sindirim midede değil, ağızda başlar. Dişlerin lokmayı koparır ve doğrar.", [3]),
    L("Tükürük bezlerinin yaptığı tükürük de lokmayı ıslatır; böylece kolayca yutulur.", [3]),
    L("Tükürükte amilaz denen bir sindirim enzimi vardır. Amilaz, nişasta gibi karbonhidratları parçalamaya başlar.", [4]),
    L("Yemeği koklamak, hatta düşünmek bile ağzını sulandırabilir. Çünkü beynin tükürük bezlerine sinyal gönderir.", [5]),
    L("Benim ağzım hiç sulanmaz. Sulansaydı kısa devre yapardım!"),
])
e.sec("finding", [
    L("Yutarken dilin lokmayı boğaza iter. NIDDK'ye göre bu sırada epiglot denen küçük bir doku kapağı soluk borunun üstüne kapanır; böylece boğulmayız.", [6], f"Yutarken dilin lokmayı boğaza iter. {ND}'ye göre bu sırada epiglot denen küçük bir doku kapağı soluk borunun üstüne kapanır; böylece boğulmayız."),
    L("Lokma sonra yemek borusuna girer. Yemek borusunun kasları dalga dalga kasılıp lokmayı aşağı iter. Bu dalgalara peristalsis denir.", [7]),
    L("Yemek borusunun sonunda sfinkter denen bir kas halka vardır. Genelde kapalı durur ve midedekilerin geri kaçmasını engeller.", [8]),
    L("Mide kaslı bir torbadır. Kasları lokmayı çalkalar ve sindirim sıvılarıyla karıştırır.", [9]),
    L("Mide duvarındaki bezler mide asidi ve enzimler yapar. KidsHealth'e göre midedeki sindirim için asitli bir ortam gerekir.", [9], f"Mide duvarındaki bezler mide asidi ve enzimler yapar. {KHs}'e göre midedeki sindirim için asitli bir ortam gerekir."),
    L("Lokma burada koyu bir lapaya dönüşür; buna kimus denir. Mide kimusu yavaş yavaş ince bağırsağa boşaltır.", [10]),
    L("Midenin çıkışında ceviz büyüklüğünde bir kas kapak vardır: pilor. Pilor, kimusu zamanı gelene kadar midede tutar.", [10]),
    L("Benim de bir kapağım var: pil kapağı. Ama o pilor değil, sadece pil yeri!"),
])
e.sec("importance", [
    L("Şimdi asıl iş başlıyor: ince bağırsak! Ona ince denmesinin nedeni genişliğidir, uzunluğu değil.", [11]),
    L("Aslında ince bağırsak, kalın bağırsaktan çok daha uzundur.", [11]),
    L("İnce bağırsağın kasları kimusu pankreastan, karaciğerden ve bağırsağın kendisinden gelen sindirim sıvılarıyla karıştırır.", [13]),
    L("Karaciğer safra denen bir sıvı yapar; safra yağların sindirimine yardım eder. Safra kesesi safrayı öğünler arasında saklar.", [13]),
    L("Pankreas ise karbonhidratları, yağları ve proteinleri parçalayan enzimler yapar.", [13]),
    L("İnce bağırsağın iç duvarı milyonlarca mikroskobik, parmak gibi çıkıntıyla kaplıdır. Bunlara villus denir.", [12]),
    L("Sindirilmiş besinler ve su, ince bağırsağın duvarından geçerek kana karışır. Villuslar bu işin taşıyıcılarıdır.", [12]),
    L("Villus kelimesini duyunca virüs sanma sakın. Villus dostumuz!"),
    L("Geriye kalanlar kalın bağırsağa gider. NIDDK'ye göre kalın bağırsak suyu emer ve atığı sıvıdan katıya, yani kakaya dönüştürür.", [14], f"Geriye kalanlar kalın bağırsağa gider. {ND}'ye göre kalın bağırsak suyu emer ve atığı sıvıdan katıya, yani kakaya dönüştürür."),
    L("Kalın bağırsaktaki bakteriler kalan besinleri parçalamaya yardım eder ve K vitamini yapar. İçinde sana yardım eden minik dostlar yaşıyor!", [15]),
    L("Bu yolculuk birkaç dakikada bitmez. KidsHealth'e göre besinin tamamen sindirilmesi saatler sürer.", [17], f"Bu yolculuk birkaç dakikada bitmez. {KHs}'e göre besinin tamamen sindirilmesi saatler sürer."),
    L("Şimdi sıra sende! Bir sonraki öğünde ilk lokmayı hemen yutma; yavaş yavaş, uzun uzun çiğne.", [3]),
    L("Lokmanın nasıl yumuşayıp ıslandığına dikkat et: tükürük ve amilaz iş başında! Ağzın doluyken konuşma ve gülme.", [3, 4]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? KidsHealth'e göre bir yetişkinin sindirim kanalı yaklaşık 9 metre uzunluğundadır!", [16], f"Bunu biliyor muydun? {KHs}'e göre bir yetişkinin sindirim kanalı yaklaşık dokuz metre uzunluğundadır!"),
    L("Benim kablolarım bu kadar uzun olsaydı, kesin düğüm olurdu!"),
    L("Hızlı soru! Besinleri kana geçiren, parmak gibi minik çıkıntıların adı neydi?", [12]),
    L("Düşün bakalım... Evet: villus!", [12]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Afiyet olsun!"),
])
S = e.S
S(3, {"type": "hook", "question": "Midemiz yemeği nasıl sindirir?", "emoji": "🍞"}, ["🍎", "🥕"], ["", "UZUN YOLCULUK", "SİNDİRİM KANALI"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Sindirime neden ihtiyacımız var?", "Lokma hangi yollardan geçer?", "Vücut onu nasıl kullanır?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Sindirim", "emoji": "🍽️", "chips": [{"label": "Besin = yakıt", "emoji": "⛽"}, {"label": "Hücrelere enerji", "emoji": "⚡"}, {"label": "Küçük parçalara ayır", "emoji": "✂️"}]}, ["🍎", "🔌"], ["YAKIT ⛽", "SİNDİRİM", "PRİZ 🔌"])
S(3, {"type": "diagram", "title": "Ağızda başlar", "layout": "flow", "nodes": [{"label": "Dişler doğrar", "emoji": "🦷"}, {"label": "Tükürük ıslatır", "emoji": "💧"}, {"label": "Amilaz nişastayı parçalar", "emoji": "✂️"}]}, ["🍞", "🦷"], ["DİŞLER 🦷", "TÜKÜRÜK", "AMİLAZ"])
S(2, {"type": "big-number", "value": "Sulanır!", "label": "Koku bile tükürük bezlerini çalıştırır", "sub": "KidsHealth · NIDDK", "icon": "👃"}, ["🥧", "🤖"], ["AĞZIN SULANDI MI?", "KISA DEVRE ⚡"])
S(3, {"type": "stages", "title": "Ağızdan mideye", "rows": [{"label": "Dil iter, epiglot kapanır", "emoji": "👅"}, {"label": "Yemek borusu: peristalsis", "emoji": "〰️"}, {"label": "Sfinkter kapanır", "emoji": "⭕"}, {"label": "Mide", "emoji": "🥣"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 1, "note": "Şematik çizim."}, [], ["EPİGLOT", "PERİSTALSİS 〰️", "SFİNKTER"])
S(3, {"type": "meter", "title": "Mide çalışıyor", "label": "Kimus", "emoji": "🥣", "phases": [{"label": "Kaslar çalkalar", "level": 0.5, "emoji": "🌀"}, {"label": "Asit ve enzimler", "level": 0.85, "emoji": "🧪"}, {"label": "Yavaşça ince bağırsağa", "level": 0.3, "emoji": "⬇️"}], "note": NOTE}, ["🧪", "🌀"], ["ÇALKALA!", "ASİTLİ ORTAM", "KİMUS"], fx="shake")
S(2, {"type": "spotlight", "title": "Pilor", "emoji": "🌰", "chips": [{"label": "Ceviz büyüklüğünde kas kapak", "emoji": "🚪"}, {"label": "Kimusu midede tutar", "emoji": "✋"}]}, ["🚪", "🔋"], ["PİLOR 🌰", "PİL YERİ 🔋"])
S(3, {"type": "comparison", "title": "İnce ve kalın bağırsak", "left": {"title": "İnce bağırsak 🐍", "items": ["Dar ama çok daha uzun", "Sindirim sıvılarıyla karıştırır"]}, "right": {"title": "Kalın bağırsak 🌭", "items": ["Daha geniş", "Daha kısa"]}}, ["📏", "🌀"], ["İNCE = DAR", "ÇOK UZUN", "KARIŞTIR"])
S(2, {"type": "spotlight", "title": "Yardımcı organlar", "emoji": "🧰", "chips": [{"label": "Karaciğer: safra", "emoji": "🟤"}, {"label": "Safra kesesi: saklar", "emoji": "👝"}, {"label": "Pankreas: enzimler", "emoji": "🧪"}]}, ["🧈", "🥩"], ["SAFRA", "PANKREAS"])
S(3, {"type": "diagram", "title": "Villuslar iş başında", "layout": "flow", "nodes": [{"label": "Milyonlarca villus", "emoji": "🖐️"}, {"label": "Besin ve su geçer", "emoji": "💧"}, {"label": "Kana karışır", "emoji": "🩸"}]}, ["🔬", "✨"], ["VİLLUS", "KANA GEÇER 🩸", "VİRÜS DEĞİL! 😄"], fx="sparkle")
S(2, {"type": "meter", "title": "Kalın bağırsak", "label": "Su", "emoji": "💧", "phases": [{"label": "Su emilir, atık katılaşır", "level": 0.35, "emoji": "🧽"}, {"label": "Bakteriler: K vitamini", "level": 0.2, "emoji": "🦠"}], "note": NOTE}, ["🦠", "💧"], ["SU EMİLİR", "MİNİK DOSTLAR 🦠"])
S(1, {"type": "big-number", "value": "Saatler", "label": "Besinin tamamen sindirilmesi bu kadar sürer", "sub": "KidsHealth", "icon": "⏳"}, ["⏰", "🍽️"], ["SABIR ⏳"])
S(2, {"type": "bullets", "title": "Sen de dene: yavaş çiğne", "items": ["İlk lokmayı hemen yutma", "Uzun uzun çiğne", "Yumuşamasını izle", "Ağzın doluyken konuşma"], "tone": "caution"}, ["🍞", "🦷"], ["DENEY ZAMANI 🔬", "AMİLAZ İŞ BAŞINDA"])
S(2, {"type": "big-number", "value": "9 metre", "label": "Bir yetişkinin sindirim kanalı yaklaşık bu uzunlukta", "sub": "KidsHealth", "icon": "📏"}, ["🔌", "🪢"], ["BUNU BİLİYOR MUYDUN?", "DÜĞÜM! 🪢"])
S(2, {"type": "hook", "question": "Besinleri kana geçiren çıkıntıların adı ne?", "emoji": "🤔"}, ["🖐️", "🔬"], ["HIZLI SORU!", "VİLLUS ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 28, "videoTitle": "Midemiz yemeği nasıl sindirir?", "paperTitleTr": "Midemiz yemeği nasıl sindirir?",
  "theme": {"backdrop": "gut", "actors": [{"kind": "swim", "emoji": "🦠", "every": 30}]},
  "takeaways": ["Sindirim ağızda başlar: dişler, tükürük ve amilaz", "Mide asit ve enzimlerle besini kimusa çevirir", "İnce bağırsakta villuslar besinleri kana geçirir"],
  "description": "Yediğimiz bir lokma vücudumuzda nereye gider? Bu bölümde ağızdaki tükürük ve amilazı, yutarken kapanan epiglotu, yemek borusundaki peristalsisi, midedeki asit ve enzimleri, pilor kapağını, ince bağırsaktaki villusları, karaciğer, safra kesesi ve pankreası, kalın bağırsaktaki bakterileri keşfediyoruz. Sonunda yavaş çiğneme etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Sindirim", "meaning": "Besinlerin vücudun emip kullanabileceği küçük parçalara ayrılması."},
    {"term": "Enzim", "meaning": "Besinleri parçalamaya yardım eden özel bir molekül; amilaz bunlardan biridir."},
    {"term": "Epiglot", "meaning": "Yutarken soluk borusunun üstüne kapanan küçük doku kapağı."},
    {"term": "Peristalsis", "meaning": "Besini ileri iten dalga dalga kas kasılmaları."},
    {"term": "Kimus", "meaning": "Midede sindirim sıvılarıyla karışıp koyu bir lapaya dönüşen besin."},
    {"term": "Pilor", "meaning": "Midenin çıkışındaki, kimusu midede tutan kas kapak."},
    {"term": "Villus", "meaning": "İnce bağırsağın iç duvarındaki, besinleri kana geçiren parmak gibi minik çıkıntılar."},
    {"term": "Safra", "meaning": "Karaciğerin yaptığı, yağların sindirimine yardım eden sıvı."}],
  "song": e.song("Lokmanın Yolculuğu", [("🍞", "Lokma"), ("🦷", "Dişler"), ("🧪", "Mide"), ("🖐️", "Villus"), ("🦠", "Bakteri")],
    ["Ağızda başlar bu macera", "Dişler doğrar, tükürük ıslatır", "Amilaz nişastayı parçalar", "Epiglot kapanır, yutarım"],
    ["Lokma lokma yolculuk var!", "Peristalsis dalga dalga", "Mide çalkalar, asit yardım eder", "İçimde bir fabrika çalışır"],
    ["Pilor kapısı bekletir", "İnce bağırsak uzun mu uzun", "Villuslar besini kana taşır", "Kalın bağırsak suyu toplar"],
    ["Lokma lokma yolculuk var!", "Peristalsis dalga dalga", "Yavaş çiğne, tadını çıkar", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "swim", "emoji": "🍞"}, {"kind": "hop", "emoji": "🍎"}, {"kind": "swim", "emoji": "🦠"}, {"kind": "hop", "emoji": "🥕"}])}
e.write(D, facts, script)
