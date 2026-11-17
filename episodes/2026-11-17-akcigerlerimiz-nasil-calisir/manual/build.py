"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:akcigerlerimiz-nasil-calisir"
KH = "Nemours KidsHealth — Lungs & Respiratory System"; NH = "NIH (NHLBI) — How the Lungs Work: The Respiratory System"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Lungs & Respiratory System", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/lungs.html"},
    {"id": "k2", "title": "How the Lungs Work - The Respiratory System", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/lungs/respiratory-system"}],
  "facts": [
    F(1, "Solunum sistemi burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.", "The respiratory system includes the nose, mouth, throat, voice box, windpipe, lungs, and diaphragm.", KH),
    F(2, "Hava vücuda burundan ya da ağızdan girer; bunlar havayı nemlendirip ısıtır, çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.", "Air first enters your body through your nose or mouth, which moistens and warms the air since cold, dry air can irritate your lungs. / In the nostrils, air gets warmed and moistened.", NH + "; " + KH),
    F(3, "Burundaki silia denen minik tüyler tozu ve parçacıkları süzer; soluk borusu da silialarla kaplıdır ve bunlar yabancı parçacıkları hava yolundan dışarı süpürür.", "Tiny hairs in the nose called cilia (SIL-ee-uh) filter out dust and other particles. / The trachea is also lined with cilia, which sweep fluids and foreign particles out of the airway", KH),
    F(4, "Soluk borusu aşağıda sol ve sağ iki tüpe, bronşlara ayrılır; kıkırdak denen sert doku halkaları bronş tüplerini açık tutar.", "Further down, the trachea divides into two tubes (left and right) called bronchi (BRAHN-kye). / Rings of tough tissue, called cartilage, acts as a support to keep the bronchial tubes open.", KH + "; " + NH),
    F(5, "Akciğerlerin içinde bronşlar bronşiyol denen binlerce ince tüpe ayrılır.", "Inside your lungs, the bronchial tubes branch into thousands of thinner tubes called bronchioles.", NH),
    F(6, "Bronşiyoller alveol denen minik hava keseciği kümelerinde son bulur; akciğerlerde yaklaşık 150 milyon alveol vardır.", "The bronchioles end in clusters of tiny air sacs called alveoli. / Your lungs have about 150 million alveoli.", NH, ["150"]),
    F(7, "Her alveol kılcal damar denen minik kan damarlarından bir ağla sarılıdır.", "Each of these alveoli is made up of a mesh of tiny blood vessels called capillaries.", NH),
    F(8, "Oksijen alveollerden, alveol duvarlarını kaplayan kılcal damarlar yoluyla kana geçer; alyuvarlar oksijeni alıp vücut hücrelerine taşır.", "Oxygen moves from the alveoli to the blood through the capillaries (tiny blood vessels) lining the alveolar walls. / Red blood cells pick up the oxygen and deliver it to the body's cells.", KH),
    F(9, "Karbondioksit kandan alveollerin içindeki havaya geçer.", "Carbon dioxide moves from the blood into the air inside the alveoli.", NH),
    F(10, "Diyafram göğüs ile karın arasındaki bir kastır; nefes alırken karına doğru aşağı iner, nefes verirken yukarı çıkar ve göğüs duvarı kasları gevşer.", "The diaphragm (DYE-uh-fram) is a muscle between the chest and the abdomen / When you breathe in (inhalation), the diaphragm moves down toward the abdomen, / When you breathe out (exhalation), the diaphragm moves up and the chest wall muscles relax,", KH),
    F(11, "Sürfaktan, nefes alırken akciğerlerin daha kolay şişmesine yardım ederek nefes almak için gereken işi azaltır.", "Surfactant reduces the work it takes to breathe by helping the lungs inflate more easily when you breathe in.", NH),
    F(12, "Solunum sistemi sayesinde günde binlerce kez nefes alırız.", "We take thousands of breaths a day, thanks to the respiratory system.", KH),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; NI = "En Ay Eyç"
e.sec("hook", [
    L("Bu cümleyi dinlerken farkında olmadan birkaç kez nefes aldın. KidsHealth'e göre günde binlerce kez nefes alıyoruz!", [12], f"Bu cümleyi dinlerken farkında olmadan birkaç kez nefes aldın. {KHs}'e göre günde binlerce kez nefes alıyoruz!"),
    L("Peki içine çektiğin hava nereye gider? Ve vücudun onunla ne yapar?"),
    L("Bugün bir hava molekülü olup akciğerlerin içine yolculuk ediyoruz! Ben zaten havalı bir robotum, hazırım!"),
])
e.sec("context", [
    L("Üç sorumuz var. Hava hangi yollardan geçer? Oksijen kana nasıl karışır? Ve nefes almamızı hangi kas sağlar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Solunum sistemi; burun, ağız, boğaz, gırtlak, soluk borusu, akciğerler ve diyaframdan oluşur.", [1]),
    L("Hava önce burundan ya da ağızdan girer. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre burası havayı ısıtır ve nemlendirir.", [2], f"Hava önce burundan ya da ağızdan girer. Amerikan Ulusal Sağlık Enstitüleri, {NI}'ye göre burası havayı ısıtır ve nemlendirir."),
    L("Çünkü soğuk ve kuru hava akciğerleri tahriş edebilir.", [2]),
    L("Burnunda silia denen minik tüyler vardır. Silialar tozu ve parçacıkları süzer.", [3]),
    L("Soluk borusu da silialarla kaplıdır. Bu tüyler, yabancı parçacıkları süpürge gibi dışarı iter.", [3]),
    L("Benim de bir hava filtrem var. Ama ben onu ayda bir değiştiriyorum, sen ise kendi kendini temizliyorsun!"),
])
e.sec("finding", [
    L("Soluk borusu aşağıda ikiye ayrılır: sağ ve sol bronşlar. Kıkırdak denen sert halkalar bu tüpleri açık tutar.", [4]),
    L("Akciğerlerin içinde bronşlar binlerce ince tüpe ayrılır. Bunlara bronşiyol denir.", [5]),
    L("Ters dönmüş bir ağaç gibi: gövde soluk borusu, dallar bronşlar, ince dallar bronşiyoller.", [4, 5]),
    L("Her bronşiyolün ucunda minik hava kesecikleri vardır: alveoller.", [6]),
    L("NIH'ye göre akciğerlerinde yaklaşık 150 milyon alveol vardır!", [6], f"{NI}'ye göre akciğerlerinde yaklaşık yüz elli milyon alveol vardır!"),
    L("Her alveol, kılcal damar denen minik kan damarlarından bir ağla sarılıdır.", [7]),
])
e.sec("importance", [
    L("İşte büyük takas burada olur! Oksijen alveollerden kılcal damarlara, yani kana geçer.", [8]),
    L("Alyuvarlar oksijeni yakalar ve vücudundaki hücrelere taşır.", [8]),
    L("Karbondioksit ise ters yöne gider: kandan alveollerin içindeki havaya geçer. Sen de onu nefesle dışarı verirsin.", [9]),
    L("Ben karbondioksit vermem. Olsa olsa biraz sıcak hava üflerim, o da fanımdan!"),
    L("Peki havayı içeri ne çeker? Diyafram! Diyafram, göğüs ile karın arasındaki bir kastır.", [10]),
    L("Nefes alırken diyafram karnına doğru aşağı iner. Nefes verirken yukarı çıkar ve göğüs kasları gevşer.", [10]),
    L("Alveollerde sürfaktan denen bir madde de vardır. Sürfaktan, akciğerlerin daha kolay şişmesine yardım eder ve nefes almayı kolaylaştırır.", [11]),
    L("Şimdi sıra sende! Sırt üstü uzan ve bir elini karnına, diğerini göğsüne koy.", [10]),
    L("Yavaşça burnundan derin bir nefes al, sonra ver. Hangi elin daha çok hareket ediyor? Başın dönerse hemen normal nefese dön.", [10]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Her alveol bir kılcal damar ağıyla sarılıdır. Yani akciğerlerinde 150 milyon minik takas noktası var!", [6, 7], "Bunu biliyor muydun? Her alveol bir kılcal damar ağıyla sarılıdır. Yani akciğerlerinde yüz elli milyon minik takas noktası var!"),
    L("Benim bir tane bile yok. Ama şarj kablomda iki ucum var, sayılır mı?"),
    L("Hızlı soru! Nefes alırken aşağı inen kasın adı neydi?", [10]),
    L("Düşün bakalım... Evet: diyafram!", [10]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Derin bir nefes al, görüşürüz!"),
])
S = e.S
S(3, {"type": "hook", "question": "Akciğerlerimiz nasıl çalışır?", "emoji": "🫁"}, ["🎈", "💨"], ["BİNLERCE NEFES", "HAVA NEREYE GİDER?", ""])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Hava hangi yollardan geçer?", "Oksijen kana nasıl karışır?", "Nefesi hangi kas sağlar?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Solunum sistemi", "emoji": "🫁", "chips": [{"label": "Burun ve ağız", "emoji": "👃"}, {"label": "Soluk borusu", "emoji": "🌬️"}, {"label": "Akciğerler", "emoji": "🫁"}, {"label": "Diyafram", "emoji": "💪"}]}, ["💨", "🌡️"], ["SOLUNUM SİSTEMİ", "ISIT VE NEMLENDİR", "SOĞUK HAVA ❄️"])
S(3, {"type": "diagram", "title": "Hava temizliği", "layout": "flow", "nodes": [{"label": "Burun: silia süzer", "emoji": "👃"}, {"label": "Soluk borusu: silia süpürür", "emoji": "🧹"}, {"label": "Temiz hava içeri", "emoji": "✨"}]}, ["🧹", "🤖"], ["SİLİA", "SÜPÜRGE 🧹", "FİLTRE"])
S(3, {"type": "stages", "title": "Hava ağacı", "rows": [{"label": "Soluk borusu", "emoji": "🌬️"}, {"label": "Bronşlar: sağ ve sol", "emoji": "🌳"}, {"label": "Bronşiyoller", "emoji": "🌿"}, {"label": "Alveoller", "emoji": "🫧"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": "Şematik çizim."}, [], ["BRONŞLAR", "BRONŞİYOLLER", "TERS AĞAÇ 🌳"])
S(3, {"type": "big-number", "value": "150 milyon", "label": "Akciğerlerdeki alveol sayısı (yaklaşık)", "sub": "NIH", "icon": "🫧"}, ["🫧", "🩸"], ["ALVEOL", "150 MİLYON", "KILCAL DAMARLAR"], fx="sparkle")
S(2, {"type": "comparison", "title": "Alveolde takas", "left": {"title": "Kana geçer 🩸", "items": ["Oksijen", "Alyuvarlar hücrelere taşır"]}, "right": {"title": "Havaya geçer 💨", "items": ["Karbondioksit", "Nefesle dışarı"]}}, ["🩸", "💨"], ["OKSİJEN", "ALYUVARLAR"])
S(2, {"type": "meter", "title": "Takas devam ediyor", "label": "Gaz", "emoji": "💨", "phases": [{"label": "Karbondioksit havaya geçer", "level": 0.8, "emoji": "⬆️"}, {"label": "Nefes ver", "level": 0.15, "emoji": "😮‍💨"}], "note": NOTE}, ["💨", "🌀"], ["KARBONDİOKSİT", "FAN 🌀"])
S(3, {"type": "comparison", "title": "Diyafram", "left": {"title": "Nefes al 🫁", "items": ["Diyafram aşağı iner"]}, "right": {"title": "Nefes ver 😮‍💨", "items": ["Diyafram yukarı çıkar", "Göğüs kasları gevşer"]}}, ["💪", "🫧"], ["DİYAFRAM", "AŞAĞI • YUKARI", "SÜRFAKTAN"])
S(2, {"type": "bullets", "title": "Sen de dene: hangi el?", "items": ["Sırt üstü uzan", "Bir el karında, biri göğüste", "Yavaş ve derin nefes al", "Başın dönerse normal nefese dön"], "tone": "caution"}, ["✋", "🫁"], ["DENEY ZAMANI 🔬", "YAVAŞ VE DERİN"])
S(2, {"type": "spotlight", "title": "Minik takas noktaları", "emoji": "🫧", "chips": [{"label": "Her alveol kılcal ağla sarılı", "emoji": "🕸️"}, {"label": "150 milyon alveol", "emoji": "🔢"}]}, ["🔌", "🕸️"], ["BUNU BİLİYOR MUYDUN?", "ŞARJ KABLOSU 🔌"])
S(2, {"type": "hook", "question": "Nefes alırken aşağı inen kas hangisi?", "emoji": "🤔"}, ["💪", "🫁"], ["HIZLI SORU!", "DİYAFRAM ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 32, "videoTitle": "Akciğerlerimiz nasıl çalışır?", "paperTitleTr": "Akciğerlerimiz nasıl çalışır?",
  "theme": {"backdrop": "sky", "actors": [{"kind": "fly", "emoji": "🎈", "every": 32}]},
  "takeaways": ["Hava burun, soluk borusu, bronşlar ve bronşiyollerden alveollere gider", "Alveollerde oksijen kana, karbondioksit havaya geçer", "Diyafram aşağı inip yukarı çıkarak nefes almamızı sağlar"],
  "description": "Nefes aldığımızda hava nereye gider? Bu bölümde burun ve silialarla havanın temizlenmesini, soluk borusunu, bronşları ve bronşiyolleri, yaklaşık yüz elli milyon alveolü, oksijen ve karbondioksit takasını, diyaframı ve sürfaktanı keşfediyoruz. Sonunda karın ve göğüs nefes deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Silia", "meaning": "Burunda ve soluk borusunda tozu süzen, süpüren minik tüyler."},
    {"term": "Bronş", "meaning": "Soluk borusunun ayrıldığı sağ ve sol hava tüpleri."},
    {"term": "Bronşiyol", "meaning": "Bronşların akciğer içinde ayrıldığı çok ince hava tüpleri."},
    {"term": "Alveol", "meaning": "Bronşiyollerin ucundaki, gaz takasının olduğu minik hava kesecikleri."},
    {"term": "Kılcal damar", "meaning": "Alveolleri saran çok ince kan damarları."},
    {"term": "Diyafram", "meaning": "Göğüs ile karın arasında, nefes almayı sağlayan kas."},
    {"term": "Sürfaktan", "meaning": "Akciğerlerin kolay şişmesine yardım eden madde."}],
  "song": e.song("Nefes Ağacı", [("🫁", "Akciğer"), ("👃", "Burun"), ("🫧", "Alveol"), ("🩸", "Kan"), ("💪", "Diyafram")],
    ["Burundan girer serin hava", "Silialar süzer tozları", "Soluk borusu iner aşağı", "İkiye ayrılır bronşlarla"],
    ["Nefes al, nefes ver!", "Diyafram iner, diyafram çıkar", "Oksijen kana, karbondioksit dışarı", "İçimde bir ağaç yaşar"],
    ["Bronşiyoller dal dal ayrılır", "Alveoller minik keseler", "Kılcal damarlar sarar onları", "Alyuvarlar taşır oksijeni"],
    ["Nefes al, nefes ver!", "Diyafram iner, diyafram çıkar", "Elini karnına koy, hisset", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🎈"}, {"kind": "hop", "emoji": "🫁"}, {"kind": "hop", "emoji": "🫧"}, {"kind": "fly", "emoji": "🍃"}])}
e.write(D, facts, script)
