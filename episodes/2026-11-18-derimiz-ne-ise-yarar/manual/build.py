"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:derimiz-ne-ise-yarar"
KH = "Nemours KidsHealth — Your Skin"; CC = "Cleveland Clinic — Skin"; AD = "American Academy of Dermatology — How to apply sunscreen"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Your Skin", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/skin.html"},
    {"id": "k2", "title": "Skin", "publisher": "Cleveland Clinic", "url": "https://my.clevelandclinic.org/health/body/10978-skin"},
    {"id": "k3", "title": "How to apply sunscreen", "publisher": "Amerikan Dermatoloji Akademisi", "url": "https://www.aad.org/public/everyday-care/sun-protection/shade-clothing-sunscreen/how-to-apply-sunscreen"}],
  "facts": [
    F(1, "Deri en büyük organımızdır ve birçok görevi vardır.", "Skin, our largest organ, has many jobs.", KH),
    F(2, "Deri vücudu mikroplardan korur ve vücut sıcaklığını düzenler; zararlı maddelerin ve mikropların vücuda girmesini önleyen bir engel oluşturur.", "Your skin protects your body from germs and regulates body temperature. / forms a barrier that prevents harmful substances and germs from entering the body", CC + "; " + KH),
    F(3, "Epidermis derinin üst katmanıdır; sürekli dökülüp yenilenen hücre katmanlarından oluşur; epidermis hücreleri yaklaşık her 28 günde bir tamamen yenilenir.", "The epidermis is the upper layer of skin. / The epidermis has layers of cells that constantly flake off and are renewed. / The cells in the epidermis are completely replaced about every 28 days.", KH, ["28"]),
    F(4, "Yeni hücreler, vücudun her gün döktüğü yaklaşık 40.000 eski deri hücresinin yerini alır.", "These new cells replace the approximately 40,000 old skin cells that your body sheds every day.", CC, ["40.000"]),
    F(5, "Epidermis, deriye rengini veren melanin pigmentini içerir; vücut ne kadar çok melanin üretirse deri o kadar koyu olur.", "The epidermis contains melanin, the pigment that gives skin its color. / The more melanin the body produces, the darker the skin.", CC + "; " + KH),
    F(6, "Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri bulunur.", "This is where our blood vessels, nerve endings, sweat glands, and hair follicles are.", KH),
    F(7, "Deri, sıcağı ve soğuğu, dokunmayı ve acıyı hissetmemizi sağlayan sinir uçları taşır; dermisteki sinirler bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu bildirir.", "Skin holds nerve endings that let us feel hot and cold, touch, and pain. / Nerves in the dermis tell you when something is too hot to touch, itchy or super soft.", KH + "; " + CC),
    F(8, "Yağ bezleri deriyi yumuşatan ve su geçirmez yapan sebum yağını üretir.", "These glands make the oil sebum (SEE-bum), which softens the skin and makes it waterproof.", KH),
    F(9, "Ter vücut sıcaklığını düzenlemeye yardım eder; deri sıcakken terleyerek, soğukken ısıyı içeride tutarak sıcaklığı kontrol eder.", "Sweat helps regulate your body temperature. / helps control body temperature through sweating when we're hot and by helping keep heat in the body when we're cold", CC + "; " + KH),
    F(10, "Deri altı dokusu vücudu darbelere ve yaralanmalara karşı korur ve vücut ısısını içeride tutar.", "This layer helps protect the body from hits and other injuries, and helps hold in body heat.", KH),
    F(11, "Kesik ve sıyrık gibi küçük yaralanmalar çabuk iyileşebilir.", "minor injuries like cuts and scrapes can heal quickly", KH),
    F(12, "Güneş kremi deriyi güneş yanığına ve cilt kanserine karşı korumaya yardım eder; en az 30 SPF'li, suya dayanıklı, geniş spektrumlu güneş kremi seçilmeli; dışarıdayken iki saatte bir ve yüzdükten ya da terledikten hemen sonra yeniden sürülmelidir.", "Sunscreen can help protect your skin against skin cancer, sunburn, and premature aging. / Choose a sunscreen that has an SPF of 30 or higher, is water resistant / To remain protected when outdoors, reapply sunscreen every two hours, and immediately after swimming or sweating.", AD, ["30"]),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; CCs = "Klivlınd Klinik"
e.sec("hook", [
    L("Vücudunun en büyük organı hangisi? Kalp mi, beyin mi? Hayır! KidsHealth'e göre en büyük organın derin!", [1], f"Vücudunun en büyük organı hangisi? Kalp mi, beyin mi? Hayır! {KHs}'e göre en büyük organın derin!"),
    L("Onu her gün giyiyorsun ama hiç çıkarmıyorsun. Peki ne işe yarıyor?"),
    L("Bugün derinin katmanlarına iniyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Deri hangi katmanlardan oluşur? Bizi nasıl korur? Ve onu nasıl koruruz?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Cleveland Clinic'e göre deri vücudunu mikroplardan korur ve vücut sıcaklığını düzenler.", [2], f"{CCs}'e göre deri vücudunu mikroplardan korur ve vücut sıcaklığını düzenler."),
    L("Zararlı maddelerin ve mikropların içeri girmesini önleyen bir kalkan gibidir.", [2]),
    L("Benim derim metal. Mikroplar giremez ama kış gelince biraz üşüyorum!"),
    L("Derinin en üstteki katmanına epidermis denir. Epidermis sürekli dökülüp yenilenen hücre katmanlarından oluşur.", [3]),
    L("KidsHealth'e göre epidermis hücreleri yaklaşık her 28 günde bir tamamen yenilenir!", [3], f"{KHs}'e göre epidermis hücreleri yaklaşık her yirmi sekiz günde bir tamamen yenilenir!"),
    L("Cleveland Clinic'e göre vücudun her gün yaklaşık 40.000 eski deri hücresi döker.", [4], f"{CCs}'e göre vücudun her gün yaklaşık kırk bin eski deri hücresi döker."),
])
e.sec("finding", [
    L("Epidermiste melanin denen bir pigment vardır. Deriye rengini melanin verir.", [5]),
    L("Vücut ne kadar çok melanin üretirse deri o kadar koyu olur.", [5]),
    L("Epidermisin altında dermis bulunur. Dermiste kan damarları, sinir uçları, ter bezleri ve kıl kökleri vardır.", [6]),
    L("Sinir uçları sayesinde sıcağı, soğuğu, dokunmayı ve acıyı hissedersin.", [7]),
    L("Bir şeyin dokunulamayacak kadar sıcak, kaşındırıcı ya da çok yumuşak olduğunu sana dermisteki sinirler söyler.", [7]),
    L("Dermisteki yağ bezleri sebum denen bir yağ üretir. Sebum deriyi yumuşatır ve su geçirmez yapar.", [8]),
    L("Su geçirmez mi? Ben de su geçirmez olmak isterdim. Yağmurda hep şemsiye taşıyorum!"),
])
e.sec("importance", [
    L("Deri bir de termostattır. Sıcakken terlersin; ter, vücut sıcaklığını düzenlemeye yardım eder.", [9]),
    L("Soğukken ise deri ısıyı içeride tutmaya yardım eder.", [9]),
    L("En alttaki katman deri altı dokusudur. Bu katman vücudu darbelere karşı korur ve ısıyı içeride tutar.", [10]),
    L("Deri kendini onarmayı da bilir. Kesik ve sıyrık gibi küçük yaralar çabuk iyileşebilir.", [11]),
    L("Şimdi sıra sende! Bir büyüteçle parmak ucunun ve elinin üstünün derisine bak. Çizgiler ve minik delikler görüyor musun?", [6]),
    L("Sonra gözlerini kapat ve bir yetişkin önce soğuk, sonra ılık bir kaşıkla elinin üstüne hafifçe dokunsun. Farkı hissedebiliyor musun? Sinir uçların iş başında!", [7]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Amerikan Dermatoloji Akademisi'ne göre güneş kremi derini güneş yanığına karşı korumaya yardım eder. En az 30 SPF'li olanı seç ve dışarıdayken iki saatte bir yeniden sür!", [12], "Bunu biliyor muydun? Amerikan Dermatoloji Akademisi'ne göre güneş kremi derini güneş yanığına karşı korumaya yardım eder. En az otuz es pi ef'li olanı seç ve dışarıdayken iki saatte bir yeniden sür!"),
    L("Hızlı soru! Deriye rengini veren pigmentin adı neydi?", [5]),
    L("Düşün bakalım... Evet: melanin!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Güneşli günlerde kremini unutma!"),
])
S = e.S
S(3, {"type": "hook", "question": "Derimiz ne işe yarar?", "emoji": "✋"}, ["☀️", "🧴"], ["EN BÜYÜK ORGAN", "HEP ÜSTÜNDE", "KATMANLAR"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Deri hangi katmanlardan oluşur?", "Bizi nasıl korur?", "Onu nasıl koruruz?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Kalkan deri", "emoji": "🛡️", "chips": [{"label": "Mikroplara karşı engel", "emoji": "🦠"}, {"label": "Sıcaklığı düzenler", "emoji": "🌡️"}, {"label": "Metal Muma da üşür", "emoji": "🤖"}]}, ["🛡️", "🤖"], ["KALKAN", "ENGEL", "METAL DERİ 🥶"])
S(3, {"type": "meter", "title": "Epidermis yenileniyor", "label": "Yeni hücre", "emoji": "✨", "phases": [{"label": "Hücreler dökülür", "level": 0.3, "emoji": "🍂"}, {"label": "Yaklaşık 28 günde tamamen yeni", "level": 0.9, "emoji": "🔄"}, {"label": "Günde 40.000 hücre dökülür", "level": 0.6, "emoji": "🧮"}], "note": NOTE}, ["🍂", "🔄"], ["EPİDERMİS", "28 GÜN", "40.000 HÜCRE"])
S(2, {"type": "comparison", "title": "Melanin", "left": {"title": "Az melanin", "items": ["Daha açık deri"]}, "right": {"title": "Çok melanin", "items": ["Daha koyu deri"]}}, ["🎨", "✋"], ["MELANİN", "DERİ RENGİ"])
S(3, {"type": "stages", "title": "Dermiste neler var?", "rows": [{"label": "Kan damarları", "emoji": "🩸"}, {"label": "Sinir uçları", "emoji": "⚡"}, {"label": "Ter bezleri", "emoji": "💧"}, {"label": "Kıl kökleri", "emoji": "🌱"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 1, "note": "Şematik çizim."}, [], ["DERMİS", "SİNİR UÇLARI", "SICAK • KAŞINTI • YUMUŞAK"])
S(2, {"type": "big-number", "value": "Sebum", "label": "Deriyi yumuşatır ve su geçirmez yapar", "sub": "KidsHealth", "icon": "💧"}, ["☂️", "💧"], ["YAĞ BEZLERİ", "ŞEMSİYELİ MUMA ☂️"])
S(3, {"type": "diagram", "title": "Deri termostatı", "layout": "cycle", "nodes": [{"label": "Sıcak: terle", "emoji": "🥵"}, {"label": "Soğuk: ısıyı tut", "emoji": "🥶"}, {"label": "Deri altı: darbe ve ısı kalkanı", "emoji": "🛡️"}]}, ["💧", "🌡️"], ["TER", "ISIYI TUT", "DERİ ALTI"])
S(1, {"type": "spotlight", "title": "Kendini onarır", "emoji": "🩹", "chips": [{"label": "Kesik ve sıyrıklar", "emoji": "🩹"}, {"label": "Çabuk iyileşir", "emoji": "✨"}]}, ["🩹", "✨"], ["ONARIM"], fx="sparkle")
S(2, {"type": "bullets", "title": "Sen de dene: deri dedektifi", "items": ["Büyüteçle derine bak", "Gözlerini kapat", "Soğuk ve ılık kaşıkla dokunulsun", "Farkı hissettin mi?"]}, ["🔍", "🥄"], ["DENEY ZAMANI 🔬", "SİNİR UÇLARI ⚡"])
S(1, {"type": "big-number", "value": "SPF 30+", "label": "Güneş kremi seç; dışarıda iki saatte bir yeniden sür", "sub": "Amerikan Dermatoloji Akademisi", "icon": "🧴"}, ["☀️", "🧴"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Deriye rengini veren pigment hangisi?", "emoji": "🤔"}, ["🎨", "✋"], ["HIZLI SORU!", "MELANİN ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 42, "videoTitle": "Derimiz ne işe yarar?", "paperTitleTr": "Derimiz ne işe yarar?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "walk", "emoji": "🐞", "every": 30}]},
  "takeaways": ["Deri en büyük organımızdır; mikroplara karşı kalkan olur ve sıcaklığı düzenler", "Epidermis sürekli yenilenir, melanin deriye rengini verir; dermiste sinir uçları ve ter bezleri vardır", "Güneş kremi derimizi güneş yanığına karşı korumaya yardım eder"],
  "description": "Derimiz ne işe yarar? Bu bölümde en büyük organımızın katmanlarını (epidermis, dermis, deri altı), sürekli yenilenen deri hücrelerini, melanini, sinir uçlarını, ter ve yağ bezlerini, derinin sıcaklığı nasıl düzenlediğini ve güneşten nasıl korunacağımızı keşfediyoruz. Sonunda deri dedektifi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Epidermis", "meaning": "Derinin en üst, sürekli yenilenen katmanı."},
    {"term": "Dermis", "meaning": "Kan damarlarının, sinir uçlarının ve bezlerin bulunduğu orta katman."},
    {"term": "Melanin", "meaning": "Deriye rengini veren pigment."},
    {"term": "Pigment", "meaning": "Renk veren madde."},
    {"term": "Sebum", "meaning": "Yağ bezlerinin ürettiği, deriyi yumuşatan yağ."},
    {"term": "Ter bezi", "meaning": "Ter üreterek vücudu serinleten bez."},
    {"term": "SPF", "meaning": "Güneş kreminin koruma gücünü gösteren değer."}],
  "song": e.song("Kalkanım Derim", [("✋", "Deri"), ("🛡️", "Kalkan"), ("🎨", "Melanin"), ("💧", "Ter"), ("🧴", "Güneş kremi")],
    ["Üstte epidermis, yenilenir hep", "Hücreler dökülür, yenisi gelir", "Melanin verir rengini", "Her ten güzel, her renk değerli"],
    ["Kalkanım derim, beni korur!", "Mikroplar dursun kapıda", "Sıcakta terlerim, serinlerim", "Soğukta ısımı tutarım"],
    ["Dermiste sinir uçları uyanık", "Sıcağı, soğuğu hissederim", "Sebum yumuşatır, su geçirmez", "Küçük yaralar iyileşir"],
    ["Kalkanım derim, beni korur!", "Mikroplar dursun kapıda", "Güneşte kremini sür", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "walk", "emoji": "🐞"}, {"kind": "hop", "emoji": "🛡️"}, {"kind": "hop", "emoji": "☀️"}, {"kind": "hop", "emoji": "🧴"}])}
e.write(D, facts, script)
