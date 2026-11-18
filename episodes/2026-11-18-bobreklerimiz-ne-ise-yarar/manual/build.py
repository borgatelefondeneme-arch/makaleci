"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:bobreklerimiz-ne-ise-yarar"
KH = "Nemours KidsHealth — Urinary System & Kidneys"; NI = "NIDDK (NIH) — Your Kidneys & How They Work"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Urinary System & Kidneys", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/kidneys.html"},
    {"id": "k2", "title": "Your Kidneys & How They Work", "publisher": "NIDDK", "url": "https://www.niddk.nih.gov/health-information/kidney-disease/kidneys-how-they-work"}],
  "facts": [
    F(1, "Böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır; kaburgaların hemen altında, omurganın iki yanında birer tane bulunur.", "The kidneys are two bean-shaped organs, each about the size of a fist. / They are located just below the rib cage, one on each side of your spine.", NI),
    F(2, "İnsanların genellikle iki böbreği vardır ama tek böbrekle de normal, sağlıklı bir yaşam sürebilirler.", "People usually have two kidneys, but can live a normal, healthy life with just one.", KH),
    F(3, "Her böbrek, nefron denen yaklaşık bir milyon süzme biriminden oluşur; bu minik birimler zararlı maddeleri kandan uzaklaştırır.", "Each of your kidneys is made up of about a million filtering units called nephrons. / one million tiny filtering units in each kidney that remove the harmful substances from the blood.", NI + "; " + KH),
    F(4, "Sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer; atıkları ve fazla suyu ayırarak idrar yapar.", "Healthy kidneys filter about a half cup of blood every minute, removing wastes and extra water to make urine.", NI),
    F(5, "Vücut, ihtiyaç duymadığı atıklardan ve fazla sudan kurtulmak için idrar üretir.", "The body produces pee as a way to get rid of waste and extra water that it doesn't need.", KH),
    F(6, "Üreterler idrarı böbreklerden mesaneye taşıyan iki ince borudur; mesane tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir; üretra idrarı mesaneden vücut dışına taşıyan borudur.", "ureters: two thin tubes that take pee from the kidneys to the bladder / bladder: a sac that holds pee until it's time to go to the bathroom / urethra: the tube that carries urine from the bladder out of the body when you pee", KH),
    F(7, "Böbrekler su, tuz ve minerallerin sağlıklı dengesini korur; idrar da vücudun doğru miktarda su tutmasının bir yoludur.", "maintain a healthy balance of water, salts, and minerals / Pee also is a way for your body to keep the right amount of water.", NI + "; " + KH),
    F(8, "Böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.", "The kidneys also help regulate blood pressure, the level of salts in the blood,", KH),
    F(9, "Böbrekler kırmızı kan hücrelerinin üretimini denetleyen bir hormon yapar; böbreklerin yaptığı hormonlar kırmızı kan hücresi yapımına ve kemiklerin güçlü ve sağlıklı kalmasına yardım eder.", "making a hormone that controls the production of red blood cells. / make red blood cells / keep your bones strong and healthy", KH + "; " + NI),
    F(10, "Çok su içince daha çok idrara çıkılır ve idrar açık sarı olur.", "Did you ever notice that if you drink a lot, you pee more and the pee is pale yellow?", KH),
    F(11, "Böbrekleri ve idrar yollarını sağlıklı tutmak için yeterince su içilmeli, besleyici beslenilmeli ve bol egzersiz yapılmalıdır.", "Stay hydrated. / Eat a nutritious diet. / Get plenty of exercise.", KH),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; NIs = "En Ay Di Di Key"
e.sec("hook", [
    L("Vücudunda gece gündüz çalışan iki minik temizlik fabrikası var. Sen uyurken bile durmuyorlar!", [4]),
    L("Bu fabrikalar kanını temizliyor. Adları: böbrekler!"),
    L("Bugün böbreklerin içindeki minik süzgeçlere bakıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Böbrekler nerededir? Kanı nasıl süzer? Ve başka hangi işleri yapar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NIDDK'ye göre böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır.", [1], f"{NIs}'ye göre böbrekler, her biri yaklaşık bir yumruk büyüklüğünde, fasulye biçimli iki organdır."),
    L("Kaburgalarının hemen altında, omurganın iki yanında birer tane bulunur. Elini belinin biraz yukarısına, arkana koy: işte oradalar! Gıdıklanmak serbest!", [1]),
    L("İnsanların genellikle iki böbreği vardır, ama tek böbrekle de sağlıklı bir yaşam sürülebilir.", [2]),
    L("Benim böbreğim yok. Benim filtrem sadece toz tutuyor, o da haftada bir tıkanıyor!"),
])
e.sec("finding", [
    L("Her böbrekte nefron denen yaklaşık bir milyon minik süzme birimi vardır.", [3]),
    L("Nefronlar, zararlı maddeleri kandan ayıran süzgeçler gibidir. Mutfaktaki çay süzgeci bile bu kadar çalışkan değil!", [3]),
    L("NIDDK'ye göre sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer!", [4], f"{NIs}'ye göre sağlıklı böbrekler her dakika yaklaşık yarım bardak kanı süzer!"),
    L("Süzme sırasında atıklar ve fazla su ayrılır. Bunlardan idrar oluşur.", [4, 5]),
    L("İdrar, vücudun ihtiyaç duymadığı atıklardan ve fazla sudan kurtulma yoludur.", [5]),
    L("İdrar böbreklerden çıkar ve üreter denen iki ince borudan aşağı akar.", [6]),
    L("Sonra mesaneye gelir. Mesane, tuvalete gitme zamanı gelene kadar idrarı tutan bir kesedir.", [6]),
    L("Sonunda üretra denen boru, idrarı vücudun dışına taşır.", [6]),
])
e.sec("importance", [
    L("Böbreklerin başka işleri de var. Vücuttaki su, tuz ve minerallerin dengesini korurlar.", [7]),
    L("KidsHealth'e göre böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder.", [8], f"{KHs}'e göre böbrekler kan basıncını ve kandaki tuz düzeyini düzenlemeye de yardım eder."),
    L("Böbrekler hormon da yapar! Bu hormonlar kırmızı kan hücrelerinin yapımına ve kemiklerinin güçlü kalmasına yardım eder.", [9]),
    L("Hormon, vücutta bir yerden başka bir yere mesaj taşıyan kimyasal bir haberci gibidir.", [9]),
    L("Çok su içtiğinde daha sık tuvalete gidersin ve idrarın açık sarı olur. Böbreklerin fazla suyu dışarı atar.", [10]),
    L("Ben su içmem. İçsem kısa devre yaparım!"),
    L("Şimdi sıra sende! Bir gün boyunca içtiğin her bardak suyu bir kâğıda çizgiyle işaretle.", [11]),
    L("Akşam çizgileri say. Yeterince su içmiş misin? Böbreklerin sana teşekkür eder!", [11]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? KidsHealth'e göre böbreklerini sağlıklı tutmak için su içmek, besleyici yemekler yemek ve bol bol hareket etmek önemlidir.", [11], f"Bunu biliyor muydun? {KHs}'e göre böbreklerini sağlıklı tutmak için su içmek, besleyici yemekler yemek ve bol bol hareket etmek önemlidir."),
    L("Hızlı soru! Böbreklerdeki minik süzme birimlerine ne denir?", [3]),
    L("Düşün bakalım... Evet: nefron!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Şimdi git bir bardak su iç!"),
])
S = e.S
S(3, {"type": "hook", "question": "Böbreklerimiz ne işe yarar?", "emoji": "🫘"}, ["💧", "🏭"], ["TEMİZLİK FABRİKASI", "BÖBREKLER", "SÜZGEÇLER"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Böbrekler nerededir?", "Kanı nasıl süzer?", "Başka hangi işleri yapar?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Böbrekler", "emoji": "🫘", "chips": [{"label": "Fasulye biçimli", "emoji": "🫘"}, {"label": "Yumruk büyüklüğünde", "emoji": "✊"}, {"label": "Omurganın iki yanında", "emoji": "🦴"}]}, ["✊", "🦴"], ["FASULYE BİÇİMİ", "BELİNİN ÜSTÜ"])
S(2, {"type": "comparison", "title": "Bir mi, iki mi?", "left": {"title": "Genellikle 🫘🫘", "items": ["İki böbrek"]}, "right": {"title": "Tek böbrekle de 🫘", "items": ["Sağlıklı yaşam mümkün"]}}, ["🤖", "🧹"], ["İKİ BÖBREK", "TOZ FİLTRESİ 🧹"])
S(2, {"type": "big-number", "value": "Bir milyon", "label": "Her böbrekteki nefron sayısı (yaklaşık)", "sub": "NIDDK", "icon": "🔬"}, ["🔬", "🩸"], ["NEFRON", "SÜZGEÇ"])
S(3, {"type": "meter", "title": "Süzme", "label": "Süzülen kan", "emoji": "🩸", "phases": [{"label": "Her dakika yarım bardak kan", "level": 0.5, "emoji": "🥛"}, {"label": "Atık ve fazla su ayrılır", "level": 0.75, "emoji": "♻️"}, {"label": "İdrar oluşur", "level": 0.4, "emoji": "💧"}], "note": NOTE}, ["🥛", "♻️"], ["YARIM BARDAK", "ATIKLAR", "İDRAR"], fx="sparkle")
S(3, {"type": "stages", "title": "İdrarın yolu", "rows": [{"label": "Böbrek", "emoji": "🫘"}, {"label": "Üreterler", "emoji": "〰️"}, {"label": "Mesane", "emoji": "🎈"}, {"label": "Üretra", "emoji": "🚪"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim."}, [], ["ÜRETER", "MESANE", "ÜRETRA"])
S(2, {"type": "diagram", "title": "Denge ustası", "layout": "flow", "nodes": [{"label": "Su, tuz, mineral dengesi", "emoji": "⚖️"}, {"label": "Kan basıncı", "emoji": "🩺"}]}, ["⚖️", "🩺"], ["DENGE", "KAN BASINCI"])
S(2, {"type": "spotlight", "title": "Böbrek hormonları", "emoji": "📨", "chips": [{"label": "Kırmızı kan hücresi yapımı", "emoji": "🔴"}, {"label": "Güçlü kemikler", "emoji": "🦴"}, {"label": "Kimyasal haberci", "emoji": "📨"}]}, ["🔴", "🦴"], ["HORMON", "HABERCİ 📨"])
S(2, {"type": "big-number", "value": "Açık sarı", "label": "Çok su içince idrarın rengi", "sub": "KidsHealth", "icon": "💧"}, ["💧", "⚡"], ["SU İÇ!", "KISA DEVRE ⚡"])
S(2, {"type": "bullets", "title": "Sen de dene: su sayacı", "items": ["İçtiğin her bardağı işaretle", "Akşam çizgileri say", "Yeterince su içtin mi?"]}, ["📝", "🥛"], ["DENEY ZAMANI 🔬", "TEŞEKKÜRLER BÖBREKLER"])
S(1, {"type": "spotlight", "title": "Böbrek dostu alışkanlıklar", "emoji": "💪", "chips": [{"label": "Su iç", "emoji": "💧"}, {"label": "Besleyici ye", "emoji": "🥦"}, {"label": "Hareket et", "emoji": "🏃"}]}, ["🥦", "🏃"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Böbreklerdeki süzme birimlerine ne denir?", "emoji": "🤔"}, ["🔬", "🫘"], ["HIZLI SORU!", "NEFRON ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 47, "videoTitle": "Böbreklerimiz ne işe yarar?", "paperTitleTr": "Böbreklerimiz ne işe yarar?",
  "theme": {"backdrop": "gut", "actors": [{"kind": "swim", "emoji": "💧", "every": 32}]},
  "takeaways": ["Böbrekler omurganın iki yanında, yumruk büyüklüğünde iki organdır", "Her böbrekteki yaklaşık bir milyon nefron kanı süzer; atıklar ve fazla su idrar olur", "Böbrekler su ve tuz dengesini, kan basıncını korur ve hormon yapar"],
  "description": "Böbreklerimiz ne işe yarar? Bu bölümde böbreklerin yerini ve biçimini, kanı süzen nefronları, idrarın nasıl oluşup üreterlerden mesaneye ve üretraya gittiğini, böbreklerin su, tuz ve kan basıncı dengesindeki görevini ve yaptıkları hormonları keşfediyoruz. Sonunda su sayacı etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Böbrek", "meaning": "Kanı süzüp idrar yapan, fasulye biçimli organ."},
    {"term": "Nefron", "meaning": "Böbrekteki minik süzme birimi."},
    {"term": "İdrar", "meaning": "Böbreklerin atıklardan ve fazla sudan yaptığı sıvı."},
    {"term": "Üreter", "meaning": "İdrarı böbrekten mesaneye taşıyan ince boru."},
    {"term": "Mesane", "meaning": "İdrarı biriktiren kese."},
    {"term": "Üretra", "meaning": "İdrarı mesaneden vücut dışına taşıyan boru."},
    {"term": "Hormon", "meaning": "Vücutta mesaj taşıyan kimyasal haberci."}],
  "song": e.song("Minik Süzgeçler", [("🫘", "Böbrek"), ("🔬", "Nefron"), ("🩸", "Kan"), ("💧", "Su"), ("⚖️", "Denge")],
    ["İki fasulye belimin üstünde", "Gece gündüz çalışır durmadan", "Bir milyon nefron her birinde", "Kanı süzer, temizler"],
    ["Süz, süz, minik süzgeç!", "Atıklar dışarı, kan tertemiz", "Su, tuz, mineral dengede", "Böbreklerim iş başında"],
    ["Üreterden mesaneye", "Oradan da üretraya", "Hormon yapar, kemik güçlenir", "Kırmızı hücreler çoğalır"],
    ["Süz, süz, minik süzgeç!", "Atıklar dışarı, kan tertemiz", "Bir bardak su iç, işaretle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "swim", "emoji": "💧"}, {"kind": "hop", "emoji": "🫘"}, {"kind": "hop", "emoji": "🔬"}, {"kind": "swim", "emoji": "🩸"}])}
e.write(D, facts, script)
