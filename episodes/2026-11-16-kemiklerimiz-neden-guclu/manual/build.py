"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kemiklerimiz-neden-guclu"
KK = "Nemours KidsHealth — Bones, Muscles & Joints"; KB = "Nemours KidsHealth — Broken Bones"; CDC = "CDC — Child Activity: An Overview"; NC = "NHS — Calcium"; ND = "NHS — Vitamin D"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Bones, Muscles & Joints", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/bones.html"},
    {"id": "k2", "title": "Broken Bones (Fractures)", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/broken-bones.html"},
    {"id": "k3", "title": "Child Activity: An Overview", "publisher": "CDC", "url": "https://www.cdc.gov/physical-activity-basics/guidelines/children.html"},
    {"id": "k4", "title": "Calcium", "publisher": "NHS", "url": "https://www.nhs.uk/conditions/vitamins-and-minerals/calcium/"},
    {"id": "k5", "title": "Vitamin D", "publisher": "NHS", "url": "https://www.nhs.uk/conditions/vitamins-and-minerals/vitamin-d/"}],
  "facts": [
    F(1, "Kemikler vücudumuza destek olur ve biçimini oluşturur; kafatası beyni korur; kaburgalar kalbi ve akciğerleri barındıran bir kafes oluşturur; kaslar eklemleri çekerek hareket etmemizi sağlar.", "Bones provide support for our bodies and help form our shape. / The skull protects the brain and forms the shape of the face. / The ribs form a cage that shelters the heart and lungs / Muscles pull on the joints, allowing us to move.", KK),
    F(2, "Kemikler kalsiyum depolar ve gerektiğinde bir kısmını kana verir; vücudun kan hücrelerinin çoğu kemiklerin içindeki yumuşak kemik iliğinde yapılır.", "Bones store calcium and release some into the bloodstream when it's needed by other parts of the body. / In this soft bone is where most of the body's blood cells are made.", KK),
    F(3, "Kemikler kolajen adlı bir proteinden yapılmış bir çatı ile kalsiyum fosfat adlı bir mineralden oluşur.", "Bones are made up of a framework of a protein called collagen with a mineral called calcium phosphate", KK),
    F(4, "Kompakt kemik kemiğin katı, sert dış kısmıdır; içinden kan damarları ve sinirler taşıyan delikler ve kanallar geçer; süngere benzeyen süngerimsi kemik kompakt kemiğin içindedir.", "Compact bone is the solid, hard outside part of the bone. / Holes and channels run through it, carrying blood vessels and nerves. / Cancellous (KAN-suh-lus) bone, which looks like a sponge, is inside compact bone.", KK),
    F(5, "Vücut kemiklerin canlı dokusunu sürekli yeniler ve yeniden biçimlendirir; osteoblastlar yeni kemik yapar ve hasarı onarır; osteoklastlar kemiği yıkar ve biçimlendirir.", "a body constantly renews and reshapes the bones' living tissue. / osteoblasts (AHS-tee-uh-blastz), which make new bone and help repair damage / osteoclasts (AHS-tee-o-klasts), which break down bone and help to sculpt and shape it", KK),
    F(6, "Çocukların ve genç ergenlerin kemiklerinde büyüme plakları denen 'büyüme bölgeleri' vardır; kızlar daha erken olgunlaştığı için büyüme plakları daha erken sert kemiğe dönüşür.", "The bones of kids and young teens are smaller than those of adults and contain \"growing zones\" called growth plates. / Because girls mature at an earlier age than boys, their growth plates change into hard bone at an earlier age.", KK),
    F(7, "Kafatasının kubbesi, doğum sırasında biraz hareket eden ve kafatası büyümesini tamamlayınca birbirine kaynayan kemik plakalardan oluşur.", "bony plates, which move slightly during birth and then fuse together as the skull finishes growing.", KK),
    F(8, "Eklemler iki kemiğin buluştuğu yerdir ve iskeleti esnek yapar; kemikler birbirine bağ denen uzun, lifli kayışlarla bağlanır; kıkırdak eklemlerde kemikleri destekleyen ve koruyan esnek bir maddedir; kaslar kemiğe kiriş denen ip gibi yapılarla bağlanır; menteşe eklemler dizde ve dirsekte olduğu gibi tek yönde hareket sağlar.", "Joints are where two bones meet. They make the skeleton flexible — without them, movement would be impossible. / Bones are fastened to other bones by long, fibrous straps called ligaments / Cartilage (KAR-tul-ij), a flexible, rubbery substance in our joints, supports bones and protects them / Skeletal muscle is attached by cord-like tendons to bone / Hinge joints allow movement in one direction, as seen in the knees and elbows.", KK),
    F(9, "D vitamini vücuttaki kalsiyum ve fosfat miktarını düzenler; vücut, açık havada deriye düşen doğrudan güneş ışığıyla D vitamini üretir; kalsiyum eksikliği çocuklarda raşitizme yol açabilir.", "Vitamin D helps regulate the amount of calcium and phosphate in the body. / The body creates vitamin D from direct sunlight on the skin when outdoors. / A lack of calcium could lead to a condition called rickets in children", ND + "; " + NC),
    F(10, "6–17 yaş arasındaki çocuk ve gençler her gün en az 60 dakika hareketli olmalıdır; zıplama ya da koşma gibi kemik güçlendiren etkinlikler haftada en az 3 gün yer almalıdır.", "Children and adolescents 6 to 17 need to be active for at least 60 minutes every day. / Includes activities such as jumping or running, at least 3 days a week.", CDC, ["6", "17", "60", "3"]),
    F(11, "Kırık kemiklerin, özellikle çocuklarda, iyileşme yeteneği çok yüksektir; kırık uçları kallus denen yeni dokuyla birleşir; kallus başta yumuşaktır, sonraki haftalarda sertleşir; kırıkların çoğu alçı, atel ya da destekle tedavi edilir; tam iyileşme genellikle birkaç ay sürer; çocukların kemikleri daha yumuşak olduğu için tamamen kırılmaktan çok bükülür.", "Broken bones have an amazing ability to heal, especially in children. / This is called a callus, and it joins the broken bones together. / It's soft at first, then gets harder and stronger over the following weeks. / Doctors treat most broken bones with a cast, splint, or brace. / Broken bones usually take a few months to heal completely. / Kids' bones are more likely to bend than break completely because they're softer.", KB),
    F(12, "Sardalya gibi kılçığıyla yenen balıklar kalsiyum kaynağıdır; kalsiyum kemikleri yapmaya ve dişleri sağlıklı tutmaya yardım eder.", "fish where you eat the bones – such as sardines and pilchards / helping build bones and keep teeth healthy", NC),
]}
e = Ep(); L = e.L
KH = "Kids Helt"; CD = "Si Di Si"
e.sec("hook", [
    L("Koşuyorsun, zıplıyorsun, düşüp kalkıyorsun. Bütün bu yükü taşıyan şey içinde gizli: iskeletin!", [1]),
    L("Kemikler nasıl bu kadar güçlü? Ve kırılınca nasıl kendi kendine iyileşir?"),
    L("Bugün kemiklerinin içine bakıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kemikler ne işe yarar? Neyden yapılmıştır? Ve onları nasıl güçlü tutarız?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre kemikler vücudumuza destek olur ve biçimini oluşturur.", [1], f"{KH}'e göre kemikler vücudumuza destek olur ve biçimini oluşturur."),
    L("Aynı zamanda bir kalkandır: kafatası beyni korur, kaburgalar ise kalbi ve akciğerleri saran bir kafes oluşturur.", [1]),
    L("Kaslar kemikleri çeker ve biz hareket ederiz.", [1]),
    L("Ama kemiklerin gizli görevleri de var. Kan hücrelerinin çoğu, kemiklerin içindeki yumuşak kemik iliğinde yapılır.", [2]),
    L("Kemikler bir de kalsiyum deposudur; vücudun başka yerlerinin ihtiyacı olunca kana kalsiyum verirler.", [2]),
    L("Benim iskeletim metal. Ama içinde kan hücresi üretmiyor; olsa olsa biraz pas!"),
])
e.sec("finding", [
    L("Peki kemik neden hem sert hem dayanıklı? Kolajen denen bir protein bir çatı kurar; kalsiyum fosfat denen mineral de onu sertleştirir.", [3]),
    L("Kemiğin dışında kompakt kemik vardır: katı ve serttir. İçinden kan damarları ve sinirler taşıyan kanallar geçer.", [4]),
    L("İçeride ise süngere benzeyen süngerimsi kemik bulunur.", [4]),
    L("Kemik canlı bir dokudur ve vücut onu sürekli yeniler. Osteoblast denen hücreler yeni kemik yapar ve hasarı onarır.", [5]),
    L("Osteoklast denen hücreler ise eski kemiği yıkar ve biçimlendirir. Yıkan ve yapan iki ekip, kemiği hep yenileyen bir inşaat gibi.", [5]),
    L("Çocukların kemiklerinde büyüme plakları denen büyüme bölgeleri vardır. Boyunun uzaması buralarda olur.", [6]),
    L("Kızlar daha erken olgunlaştığı için büyüme plakaları da daha erken sert kemiğe dönüşür.", [6]),
    L("Kafatası da doğumda tek parça değildir: birbirine kaynayan kemik plakalardan oluşur.", [7]),
])
e.sec("importance", [
    L("İki kemiğin buluştuğu yere eklem denir. Eklemler sayesinde iskelet esnektir; onlar olmasa hareket edemezdik.", [8]),
    L("Kemikleri birbirine bağ denen lifli kayışlar bağlar. Kasları kemiğe ise kiriş denen ip gibi yapılar bağlar. Eklemleri de esnek kıkırdak korur.", [8]),
    L("Dizin ve dirseğin menteşe eklemdir: kapı menteşesi gibi tek yönde hareket eder.", [8]),
    L("Kemikleri güçlü tutmanın yolu: kalsiyum, D vitamini ve hareket. İngiltere Ulusal Sağlık Servisi NHS'e göre vücut, deriye düşen güneş ışığıyla D vitamini üretir.", [9], "Kemikleri güçlü tutmanın yolu: kalsiyum, D vitamini ve hareket. İngiltere Ulusal Sağlık Servisi, En Eyç Es'e göre vücut, deriye düşen güneş ışığıyla D vitamini üretir."),
    L("D vitamini, vücuttaki kalsiyumun düzenlenmesine yardım eder.", [9]),
    L("CDC'ye göre 6–17 yaş arasındakiler her gün en az 60 dakika hareket etmeli. Koşmak ve zıplamak gibi kemik güçlendiren etkinlikler de haftada en az 3 gün olmalı.", [10], f"{CD}'ye göre altı ile on yedi yaş arasındakiler her gün en az altmış dakika hareket etmeli. Koşmak ve zıplamak gibi kemik güçlendiren etkinlikler de haftada en az üç gün olmalı."),
    L("Kemik kırılırsa ne olur? KidsHealth'e göre kırık kemikler, özellikle çocuklarda, çok iyi iyileşir.", [11], f"Kemik kırılırsa ne olur? {KH}'e göre kırık kemikler, özellikle çocuklarda, çok iyi iyileşir."),
    L("Kırık uçlar arasında kallus denen yeni bir doku oluşur. Başta yumuşaktır, haftalar içinde sertleşir. Tam iyileşme birkaç ay sürebilir.", [11]),
    L("Şimdi sıra sende! Kolunu bük ve aç; sonra bileğini döndür. Hangi eklem tek yönde, hangisi çok yönde hareket ediyor?", [8]),
    L("Sonra bu hafta kaç gün koştuğunu ya da zıpladığını bir tabloya yaz. Haftada üç güne ulaşabilecek misin?", [10]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Çocukların kemikleri daha yumuşak olduğu için, tamamen kırılmaktan çok bükülme eğilimindedir.", [11]),
    L("Hızlı soru! Yeni kemik yapan hücrelerin adı neydi?", [5]),
    L("Düşün bakalım... Evet: osteoblastlar!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de eklemlerimi yağlamaya gidiyorum!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kemiklerimiz neden güçlü?", "emoji": "🦴"}, ["🏃", "🤸"], ["", "KENDİ KENDİNE İYİLEŞİR!", "KEMİĞİN İÇİNE!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kemikler ne işe yarar?", "Neyden yapılmıştır?", "Onları nasıl güçlü tutarız?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "İskeletin görevleri", "emoji": "🦴", "chips": [{"label": "Destek ve biçim", "emoji": "🏛️"}, {"label": "Kafatası: beyni korur", "emoji": "🧠"}, {"label": "Kaburgalar: kalp ve akciğer", "emoji": "🫁"}, {"label": "Kaslarla hareket", "emoji": "💪"}]}, ["🛡️", "🏃"], ["DESTEK", "KALKAN 🛡️", "HAREKET"])
S(3, {"type": "comparison", "title": "Gizli görevler", "left": {"title": "Kemik iliği 🩸", "items": ["Kan hücrelerinin çoğu burada yapılır"]}, "right": {"title": "Kalsiyum deposu 🧱", "items": ["Gerekince kana kalsiyum verir"]}}, ["🩸", "🤖"], ["KEMİK İLİĞİ", "KALSİYUM DEPOSU", "METAL İSKELET 🤖"])
S(3, {"type": "stages", "title": "Bir kemiğin içi", "rows": [{"label": "Kolajen çatı + kalsiyum fosfat", "emoji": "🧱"}, {"label": "Kompakt kemik: sert dış", "emoji": "🪨"}, {"label": "Süngerimsi kemik: iç", "emoji": "🧽"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 0, "note": "Şematik çizim."}, [], ["KOLAJEN + MİNERAL", "KOMPAKT KEMİK", "SÜNGERİMSİ KEMİK"])
S(2, {"type": "comparison", "title": "Kemik hep yenilenir", "left": {"title": "Osteoblast 🔨", "items": ["Yeni kemik yapar", "Hasarı onarır"]}, "right": {"title": "Osteoklast 🧹", "items": ["Eski kemiği yıkar", "Biçimlendirir"]}}, ["🏗️", "🦴"], ["CANLI DOKU", "YIKAN VE YAPAN"])
S(3, {"type": "spotlight", "title": "Büyüme", "emoji": "📏", "chips": [{"label": "Büyüme plakaları", "emoji": "🌱"}, {"label": "Kızlarda daha erken kapanır", "emoji": "⏳"}, {"label": "Kafatası plakaları kaynaşır", "emoji": "🧩"}]}, ["📐", "🧒"], ["BÜYÜME PLAKASI", "ERKEN KAPANIR", "KAFATASI"])
S(3, {"type": "diagram", "title": "Eklemler ve bağlantılar", "layout": "flow", "nodes": [{"label": "Eklem: iki kemik buluşur", "emoji": "🦴"}, {"label": "Bağ: kemiği kemiğe", "emoji": "🎗️"}, {"label": "Kiriş: kası kemiğe", "emoji": "🪢"}, {"label": "Kıkırdak: korur", "emoji": "🛡️"}]}, ["🦵", "💪"], ["EKLEM", "BAĞ • KİRİŞ • KIKIRDAK", "MENTEŞE EKLEM 🚪"])
S(2, {"type": "meter", "title": "Güçlü kemik tarifi", "label": "Güç", "emoji": "🦴", "phases": [{"label": "Güneş ışığı: D vitamini", "level": 0.5, "emoji": "☀️"}, {"label": "D vitamini kalsiyumu düzenler", "level": 0.85, "emoji": "🥛"}], "note": NOTE}, ["☀️", "🐟"], ["D VİTAMİNİ ☀️", "KALSİYUM"])
S(1, {"type": "big-number", "value": "60", "unit": "dakika", "label": "Her gün hareket (6–17 yaş)", "sub": "Kemik güçlendiren etkinlik: haftada en az 3 gün", "icon": "🏃"}, ["⚽", "🤸"], ["HER GÜN HAREKET"])
S(2, {"type": "diagram", "title": "Kırık nasıl iyileşir?", "layout": "flow", "nodes": [{"label": "Kırık", "emoji": "💥"}, {"label": "Kallus oluşur", "emoji": "🩹"}, {"label": "Haftalarca sertleşir", "emoji": "🧱"}, {"label": "Birkaç ayda iyileşir", "emoji": "✅"}]}, ["🩼", "🦴"], ["ÇOK İYİ İYİLEŞİR", "KALLUS 🩹"])
S(2, {"type": "bullets", "title": "Sen de dene: eklem dedektifi", "items": ["Kolunu bük ve aç", "Bileğini döndür", "Hangisi tek yönde?", "Haftalık hareket tablosu tut"]}, ["📓", "🏃"], ["DENEY ZAMANI 🔬", "HAFTADA ÜÇ GÜN"])
S(1, {"type": "spotlight", "title": "Esnek çocuk kemikleri", "emoji": "🧒", "chips": [{"label": "Daha yumuşak", "emoji": "🌿"}, {"label": "Kırılmaktan çok bükülür", "emoji": "↪️"}]}, ["🦴", "🌱"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Yeni kemik yapan hücrelerin adı ne?", "emoji": "🤔"}, ["🦴", "🔨"], ["HIZLI SORU!", "OSTEOBLAST ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 25, "videoTitle": "Kemiklerimiz neden güçlü?", "paperTitleTr": "Kemiklerimiz neden güçlü?",
  "takeaways": ["İskelet destek olur, organları korur ve kaslarla hareket ettirir", "Kemik canlıdır: osteoblastlar yapar, osteoklastlar yıkar", "Kalsiyum, D vitamini ve hareket kemikleri güçlendirir"],
  "description": "Koşarken, zıplarken bütün yükü taşıyan iskeletimiz nasıl bu kadar güçlü? Bu bölümde kemiklerin görevlerini, kemik iliğini ve kalsiyum deposunu; kolajen ve kalsiyum fosfattan oluşan yapıyı, kompakt ve süngerimsi kemiği; osteoblast ve osteoklastları, büyüme plakalarını, eklemleri, bağları ve kirişleri keşfediyoruz. Kırık kemik nasıl iyileşir, kemikleri nasıl güçlü tutarız? Sonunda eklem dedektifi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "İskelet", "meaning": "Vücuttaki bütün kemiklerin oluşturduğu çatı."},
    {"term": "Kemik iliği", "meaning": "Kemiklerin içindeki, kan hücrelerinin yapıldığı yumuşak doku."},
    {"term": "Kolajen", "meaning": "Kemiğe esneklik veren protein."},
    {"term": "Osteoblast", "meaning": "Yeni kemik yapan hücre."},
    {"term": "Osteoklast", "meaning": "Eski kemiği yıkıp biçimlendiren hücre."},
    {"term": "Büyüme plakası", "meaning": "Çocukların kemiklerinde boy uzamasının olduğu bölge."},
    {"term": "Eklem", "meaning": "İki kemiğin buluştuğu yer."},
    {"term": "Kallus", "meaning": "Kırık kemiğin uçlarını birleştiren yeni doku."}],
  "song": e.song("İçimdeki Çatı", [("🦴", "Kemik"), ("💪", "Kas"), ("☀️", "D vitamini"), ("🥛", "Kalsiyum"), ("🏃", "Hareket")],
    ["Kafatası korur beyni sıkıca", "Kaburgalar kafes, kalbe kalkan", "Kaslar çeker, kemikler oynar", "İlikte kan hücreleri doğar"],
    ["Güçlü kemik, sağlam iskelet!", "Kolajen çatı, mineral sertlik", "Osteoblast yapar, osteoklast yıkar", "Kemiğim canlı, hep yenilenir"],
    ["Eklemde buluşur iki kemik", "Bağlar tutar, kiriş kası bağlar", "Kırılırsa kallus birleştirir", "Haftalar geçer, kemik iyileşir"],
    ["Güçlü kemik, sağlam iskelet!", "Kolajen çatı, mineral sertlik", "Güneşe çık, koş ve zıpla", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "🤸"}, {"kind": "hop", "emoji": "🦴"}, {"kind": "hop", "emoji": "⚽"}, {"kind": "chase", "emoji": "🐕", "emoji2": "🦴", "every": 8, "size": 210}])}
e.write(D, facts, script)
