"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:gozumuz-nasil-gorur"
KH = "Nemours KidsHealth — Your Eyes"; NE = "National Eye Institute (NIH) — How the Eyes Work"; NC = "National Eye Institute (NIH) — Types of Color Vision Deficiency"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Your Eyes", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/eyes.html"},
    {"id": "k2", "title": "How the Eyes Work", "publisher": "Ulusal Göz Enstitüsü", "url": "https://www.nei.nih.gov/learn-about-eye-health/healthy-vision/how-eyes-work"},
    {"id": "k3", "title": "Types of Color Vision Deficiency", "publisher": "Ulusal Göz Enstitüsü", "url": "https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness/types-color-vision-deficiency"}],
  "facts": [
    F(1, "Göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukuru denen küçük bir oyukta durur.", "The eye is about as big as a ping-pong ball and sits in a little hollow area (the eye socket) in the skull.", KH),
    F(2, "Kornea, gözün renkli bölümünün önünde duran saydam bir kubbedir; ışığı kırarak gözün odaklanmasına yardım eder.", "The cornea (say: KOR-nee-uh), a transparent dome, sits in front of the colored part of the eye. / The cornea is shaped like a dome and bends light to help the eye focus.", KH + "; " + NE),
    F(3, "İris gözün renkli bölümüdür; göz bebeğinin ne kadar ışık alacağını denetler; ona bağlı kaslar biçimini değiştirir.", "The iris (say: EYE-riss) is the colorful part of the eye. / The iris (the colored part of the eye) controls how much light the pupil lets in. / The iris has muscles attached to it that change its shape.", KH + "; " + NE),
    F(4, "Göz bebekleri ışık yaklaşınca küçülür, ışık gidince genişler.", "The pupils will get smaller when the light shines near them and they'll open wider when the light is gone.", KH),
    F(5, "Mercek kornea ile birlikte ışığı retinaya doğru biçimde odaklar; yakına bakarken kalınlaşır, uzağa bakarken incelir.", "The lens works together with the cornea to focus light correctly on the retina. / When you look at things up close, the lens becomes thicker to focus the correct image onto the retina. / When you look at things far away, the lens becomes thinner.", NE + "; " + KH),
    F(6, "Retinada ışığa duyarlı milyonlarca hücre vardır; fotoreseptör denen özel hücreler ışığı elektrik sinyallerine çevirir.", "It holds millions of cells that are sensitive to light. / special cells called photoreceptors turn the light into electrical signals.", KH + "; " + NE),
    F(7, "Her gözde yaklaşık 120 milyon çubuk ve 7 milyon koni hücresi vardır.", "How about 120 million rods and 7 million cones — in each eye!", KH, ["120", "7"]),
    F(8, "Çubuklar siyah, beyaz ve gri tonlarında görür ve biçimi bildirir; renkleri ayırt edemez ama çok duyarlıdır, çok karanlıkta görmemizi sağlar.", "Rods see in black, white, and shades of gray and tell us the form or shape that something has. / Rods can't tell the difference between colors, but they are super-sensitive, allowing us to see when it's very dark.", KH),
    F(9, "Koniler rengi algılar ve iyi çalışmak için çubuklardan daha fazla ışığa ihtiyaç duyar; her koni türü kırmızı, yeşil ya da mavi renklerden birine duyarlıdır.", "Cones sense color and they need more light than rods to work well. / Each cone type is sensitive to one of three different colors — red, green, or blue", KH),
    F(10, "Elektrik sinyalleri retinadan görme siniri boyunca beyne gider; beyin sinyalleri gördüğümüz görüntülere çevirir; görme siniri gözü beyne bağlayan hızlı bir telefon hattı gibidir.", "These electrical signals travel from the retina through the optic nerve to the brain. / Then the brain turns the signals into the images you see. / The optic nerve serves as a high-speed telephone line connecting the eye to the brain.", NE + "; " + KH),
    F(11, "Göz kapağı dakikada birkaç kez açılıp kapanarak gözü temiz ve nemli tutar; her göz kırpışta üst kapaktan biraz gözyaşı gelir; gözlerin doğru çalışması için gözyaşı gerekir.", "The lid helps keep the eye clean and moist by opening and shutting several times a minute. / Every time you blink your eye, a tiny bit of tear fluid comes out of your upper eyelid. / Your eyes also need tears to work correctly.", KH + "; " + NE),
    F(12, "Renk görme bozukluğunun en yaygın türü kırmızı ile yeşili ayırt etmeyi zorlaştırır; tam renk görme bozukluğunda hiç renk görülmez.", "The most common type of color vision deficiency makes it hard to tell the difference between red and green. / If you have complete color vision deficiency, you can’t see colors at all.", NC),
    F(13, "Güneş gözlüğü takılmalıdır; fazla ışık gözlere zarar verebilir; parçacık ya da kimyasal sıçrayabilecek derslerde koruyucu gözlük takılmalıdır.", "Wear sunglasses. / Too much light can damage your eyes and cause vision problems later in life. / Wear protective goggles in classes where debris or chemicals could go flying", KH),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"
e.sec("hook", [
    L("Şu an bu ekrana bakıyorsun ve renkleri, harfleri, Muma'yı görüyorsun. Ama aslında görmek için gözün tek başına yetmez!", [10]),
    L("Işık gözüne nasıl girer, nasıl bir görüntüye dönüşür?"),
    L("Bugün göz küresinin içine yolculuk yapıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Işık göze nasıl girer? Göz onu nasıl odaklar? Ve görüntüyü kim oluşturur?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukurunda korunur.", [1], f"{KHs}'e göre göz yaklaşık bir pinpon topu büyüklüğündedir ve kafatasındaki göz çukurunda korunur."),
    L("Işığın ilk geçtiği yer korneadır: gözün önündeki saydam bir kubbe. Kornea ışığı kırarak odaklanmaya yardım eder.", [2]),
    L("Sonra iris gelir: gözünün renkli bölümü. İris, ortasındaki göz bebeğinden ne kadar ışık gireceğini denetler.", [3]),
    L("İrisin kasları onun biçimini değiştirir. Işık yaklaşınca göz bebeği küçülür, ışık gidince genişler.", [3, 4]),
    L("Benim gözlerim kamera. Göz bebeğim yok, ama bir objektif kapağım var. Bazen takmayı unutuyorum!"),
])
e.sec("finding", [
    L("Göz bebeğinden geçen ışık merceğe ulaşır. Ulusal Göz Enstitüsü'ne göre mercek, kornea ile birlikte ışığı retinaya odaklar.", [5]),
    L("Mercek esnektir: yakına bakarken kalınlaşır, uzağa bakarken incelir.", [5]),
    L("Retina, gözün arka duvarını kaplayan katmandır. İçinde ışığa duyarlı milyonlarca hücre vardır.", [6]),
    L("Bu hücrelere fotoreseptör denir. Fotoreseptörler ışığı elektrik sinyallerine çevirir.", [6]),
    L("İki türü vardır: çubuklar ve koniler. KidsHealth'e göre her gözde yaklaşık 120 milyon çubuk ve 7 milyon koni bulunur!", [7], f"İki türü vardır: çubuklar ve koniler. {KHs}'e göre her gözde yaklaşık yüz yirmi milyon çubuk ve yedi milyon koni bulunur!"),
    L("Çubuklar renkleri ayırt edemez; siyah, beyaz ve grinin tonlarını görür ve biçimleri bildirir.", [8]),
    L("Ama çok duyarlıdırlar. Çok karanlıkta görmeni çubuklar sağlar.", [8]),
    L("Koniler ise rengi algılar. İyi çalışmak için çubuklardan daha fazla ışığa ihtiyaç duyarlar.", [9]),
    L("Her koni türü üç renkten birine duyarlıdır: kırmızı, yeşil ya da mavi.", [9]),
    L("Ben de kırmızı, yeşil ve maviyi görürüm. Ama sadece ekranımı silince!"),
])
e.sec("importance", [
    L("Peki görüntü nerede oluşur? Elektrik sinyalleri retinadan görme siniri boyunca beyne gider.", [10]),
    L("KidsHealth'e göre görme siniri, gözü beyne bağlayan hızlı bir telefon hattı gibidir.", [10], f"{KHs}'e göre görme siniri, gözü beyne bağlayan hızlı bir telefon hattı gibidir."),
    L("Beyin bu sinyalleri gördüğün görüntülere çevirir. Yani aslında beyninle görürsün!", [10]),
    L("Gözlerin bakıma da ihtiyaç duyar. Göz kapağın dakikada birkaç kez açılıp kapanır ve gözü temiz ve nemli tutar.", [11]),
    L("Her göz kırpışında üst kapağından biraz gözyaşı gelir. Gözlerin doğru çalışması için gözyaşına ihtiyaç vardır.", [11]),
    L("Bazı insanlarda konilerin çalışması farklıdır. Ulusal Göz Enstitüsü'ne göre renk görme bozukluğunun en yaygın türü, kırmızı ile yeşili ayırt etmeyi zorlaştırır.", [12]),
    L("Şimdi sıra sende! Loş bir odada aynaya bak ve göz bebeğinin büyüklüğüne dikkat et.", [4]),
    L("Sonra odanın ışığını aç ve tekrar bak. Göz bebeğin küçüldü mü? Bunu iris yaptı! Gözüne asla el feneri ya da lazer tutma.", [3, 4]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? KidsHealth'e göre fazla ışık gözlerine zarar verebilir. Bu yüzden güneşli günlerde güneş gözlüğü tak.", [13], f"Bunu biliyor muydun? {KHs}'e göre fazla ışık gözlerine zarar verebilir. Bu yüzden güneşli günlerde güneş gözlüğü tak."),
    L("Hızlı soru! Karanlıkta görmemizi sağlayan fotoreseptörler hangileriydi?", [8]),
    L("Düşün bakalım... Evet: çubuklar!", [8]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Gözlerine iyi bak!"),
])
S = e.S
S(3, {"type": "hook", "question": "Gözümüz nasıl görür?", "emoji": "👁️"}, ["🌈", "🦋"], ["BEYNİNLE GÖRÜRSÜN?", "IŞIK → GÖRÜNTÜ", ""])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Işık göze nasıl girer?", "Göz onu nasıl odaklar?", "Görüntüyü kim oluşturur?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Gözün önü", "emoji": "👁️", "chips": [{"label": "Pinpon topu büyüklüğünde", "emoji": "🏓"}, {"label": "Kornea: saydam kubbe", "emoji": "🔍"}, {"label": "İris: renkli bölüm", "emoji": "🎨"}]}, ["🏓", "🔍"], ["GÖZ ÇUKURU", "KORNEA", "İRİS"])
S(2, {"type": "meter", "title": "Göz bebeği", "label": "Açıklık", "emoji": "⚫", "phases": [{"label": "Işık var: küçülür", "level": 0.25, "emoji": "☀️"}, {"label": "Işık gitti: genişler", "level": 0.85, "emoji": "🌙"}], "note": NOTE}, ["💡", "📷"], ["GÖZ BEBEĞİ", "OBJEKTİF KAPAĞI 📷"])
S(2, {"type": "comparison", "title": "Mercek odaklar", "left": {"title": "Yakına bak 📖", "items": ["Mercek kalınlaşır"]}, "right": {"title": "Uzağa bak 🏔️", "items": ["Mercek incelir"]}}, ["📖", "🏔️"], ["MERCEK + KORNEA", "ESNEK MERCEK"])
S(2, {"type": "diagram", "title": "Retinada", "layout": "flow", "nodes": [{"label": "Işık retinaya düşer", "emoji": "💡"}, {"label": "Fotoreseptörler", "emoji": "🔬"}, {"label": "Elektrik sinyali", "emoji": "⚡"}]}, ["🔬", "⚡"], ["RETİNA", "FOTORESEPTÖR"])
S(1, {"type": "bar-chart", "title": "Her gözde (milyon)", "unit": "milyon", "bars": [{"label": "Çubuk", "value": 120, "display": "120", "highlight": True}, {"label": "Koni", "value": 7, "display": "7"}]}, ["👁️", "🔢"], ["ÇUBUK VE KONİ"])
S(2, {"type": "spotlight", "title": "Çubuklar", "emoji": "🌑", "chips": [{"label": "Siyah, beyaz, gri", "emoji": "⚫"}, {"label": "Biçimleri bildirir", "emoji": "🔷"}, {"label": "Karanlıkta görür", "emoji": "🌙"}]}, ["🦉", "🌙"], ["RENK YOK", "KARANLIKTA GÖRME 🌙"])
S(3, {"type": "meter", "title": "Koniler", "label": "Işık", "emoji": "🌈", "phases": [{"label": "Rengi algılar", "level": 0.6, "emoji": "🎨"}, {"label": "Daha çok ışık ister", "level": 0.9, "emoji": "☀️"}, {"label": "Kırmızı, yeşil, mavi", "level": 0.75, "emoji": "🔴"}], "note": NOTE}, ["🔴", "🔵"], ["RENK", "ÇOK IŞIK", "KIRMIZI • YEŞİL • MAVİ"], fx="sparkle")
S(3, {"type": "stages", "title": "Gözden beyne", "rows": [{"label": "Retina sinyal üretir", "emoji": "⚡"}, {"label": "Görme siniri taşır", "emoji": "📞"}, {"label": "Beyin görüntüyü kurar", "emoji": "🧠"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 2, "note": "Şematik çizim."}, [], ["GÖRME SİNİRİ", "TELEFON HATTI 📞", "BEYİNLE GÖRMEK"])
S(2, {"type": "diagram", "title": "Göz bakımı", "layout": "cycle", "nodes": [{"label": "Göz kırp", "emoji": "😉"}, {"label": "Gözyaşı gelir", "emoji": "💧"}, {"label": "Göz temiz ve nemli", "emoji": "✨"}]}, ["💧", "😉"], ["GÖZ KIRP", "GÖZYAŞI 💧"])
S(1, {"type": "big-number", "value": "Kırmızı–yeşil", "label": "En yaygın renk görme bozukluğu bu renkleri karıştırır", "sub": "Ulusal Göz Enstitüsü", "icon": "🎨"}, ["🔴", "🟢"], ["RENK GÖRME"])
S(2, {"type": "bullets", "title": "Sen de dene: ayna deneyi", "items": ["Loş odada aynaya bak", "Göz bebeğine dikkat et", "Işığı aç, tekrar bak", "Gözüne fener ya da lazer tutma!"], "tone": "caution"}, ["🪞", "💡"], ["DENEY ZAMANI 🔬", "İRİS İŞ BAŞINDA"])
S(1, {"type": "spotlight", "title": "Gözünü koru", "emoji": "🕶️", "chips": [{"label": "Fazla ışık zarar verebilir", "emoji": "☀️"}, {"label": "Güneş gözlüğü tak", "emoji": "🕶️"}]}, ["☀️", "🥽"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Karanlıkta görmemizi hangi hücreler sağlar?", "emoji": "🤔"}, ["🌙", "👁️"], ["HIZLI SORU!", "ÇUBUKLAR ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 31, "videoTitle": "Gözümüz nasıl görür?", "paperTitleTr": "Gözümüz nasıl görür?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "fly", "emoji": "🦋", "every": 32}]},
  "takeaways": ["Kornea ve mercek ışığı retinaya odaklar, iris ışık miktarını ayarlar", "Retinadaki çubuklar karanlıkta, koniler renkte görmemizi sağlar", "Görüntüyü görme sinirinden gelen sinyallerle beyin kurar"],
  "description": "Gözümüz ışığı nasıl görüntüye çevirir? Bu bölümde korneayı, irisi ve göz bebeğini, odaklanan merceği, retinadaki çubuk ve koni hücrelerini, görme sinirini ve beynin görüntüyü nasıl kurduğunu keşfediyoruz. Göz kırpmanın ve gözyaşının görevini, renk görme bozukluğunu ve gözlerimizi nasıl koruyacağımızı öğreniyoruz. Sonunda ayna deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kornea", "meaning": "Gözün önündeki, ışığı kıran saydam kubbe."},
    {"term": "İris", "meaning": "Gözün renkli bölümü; göz bebeğine giren ışığı ayarlar."},
    {"term": "Göz bebeği", "meaning": "İrisin ortasındaki, ışığın girdiği açıklık."},
    {"term": "Mercek", "meaning": "Işığı retinaya odaklayan, kalınlığı değişebilen esnek yapı."},
    {"term": "Retina", "meaning": "Gözün arka duvarını kaplayan, ışığa duyarlı hücrelerin bulunduğu katman."},
    {"term": "Fotoreseptör", "meaning": "Işığı elektrik sinyaline çeviren hücre; çubuklar ve koniler."},
    {"term": "Görme siniri", "meaning": "Gözden beyne sinyal taşıyan sinir."}],
  "song": e.song("Işık Yolculuğu", [("👁️", "Göz"), ("🔍", "Kornea"), ("🎨", "İris"), ("🌈", "Koni"), ("🧠", "Beyin")],
    ["Işık geldi, kornea kırdı", "İris açtı göz bebeğini", "Mercek inceldi, mercek kalınlaştı", "Retinaya düştü görüntü"],
    ["Bak, bak, dünyaya bak!", "Çubuklar karanlıkta görür", "Koniler renkleri seçer", "Kırmızı, yeşil, mavi"],
    ["Fotoreseptör sinyal yapar", "Görme siniri hızla taşır", "Beyin kurar görüntüyü", "Göz kırp, gözyaşı gelsin"],
    ["Bak, bak, dünyaya bak!", "Çubuklar karanlıkta görür", "Güneşte gözlüğünü tak", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🦋"}, {"kind": "hop", "emoji": "👁️"}, {"kind": "hop", "emoji": "🌈"}, {"kind": "hop", "emoji": "🕶️"}])}
e.write(D, facts, script)
