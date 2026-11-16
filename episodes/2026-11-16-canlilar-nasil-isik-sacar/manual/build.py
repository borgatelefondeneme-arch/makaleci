"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:canlilar-nasil-isik-sacar"
NG = "National Geographic Education — Bioluminescence"; NP = "National Park Service (Great Smoky Mountains) — Fireflies"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Bioluminescence", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/bioluminescence/"},
    {"id": "k2", "title": "Fireflies", "publisher": "Milli Parklar Servisi", "url": "https://www.nps.gov/grsm/learn/nature/fireflies.htm"}],
  "facts": [
    F(1, "Biyolüminesans, canlıların vücutlarındaki kimyasal tepkimelerle saçtığı ışıktır.", "Bioluminescence is light emitted by living things through chemical reactions in their bodies.", NG),
    F(2, "Biyolüminesans ateşböceklerinin yanı sıra bazı mantarlarda, balıklarda, karideslerde, denizanalarında ve planktonlarda da görülür; bazıları karada yaşar.", "a natural process also seen in certain fungi, fish, shrimp, jellyfish, plankton / Some bioluminescent organisms, including fireflies and fungi, are found on land.", NP + "; " + NG),
    F(3, "Biyolüminesans lusiferin ve lusiferaz ya da fotoprotein gerektirir; ışığı asıl üreten bileşik lusiferindir; ateşböcekleri lusiferini oksijen ve lusiferaz enzimiyle karıştırır.", "requires two unique chemicals: luciferin and either luciferase or photoprotein / Luciferin is the compound that actually produces light. / fireflies mix the chemical luciferin with oxygen and the enzyme luciferase", NG + "; " + NP),
    F(4, "Fotoproteinler ışık yapmak için başka bir etkene, çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.", "need another agent, often an ion of the element calcium, to produce light", NG),
    F(5, "Soğuk ışık, ışığın yüzde 20'sinden azının ısı olarak yayılması demektir.", "Cold light means less than 20% of the light generates thermal radiation, or heat.", NG, ["20"]),
    F(6, "Akkor ampuller enerjilerinin yalnızca yaklaşık yüzde 10'unu ışık, yüzde 90'ını ısı olarak yayar; ateşböceğinin parıltısı neredeyse yüzde 100 ışıktır ve çok az ısı üretir.", "traditional incandescent bulbs emit only about 10% of their energy as light, with the remaining 90% as heat. / resulting in a 'cool' glow that boasts nearly 100% light / generate light with minimal heat", NP, ["10", "90", "100"]),
    F(7, "Işık saçan deniz canlıları arasında balıklar, bakteriler ve denizanaları vardır; dinoflagellatlar mavimsi yeşil parlar.", "These bioluminescent marine species include fish, bacteria, and jellies. / Dinoflagellates, for instance, bioluminesce in a bluish-green color.", NG),
    F(8, "Denizdeki biyolüminesansın çoğu görünür ışığın mavi-yeşil bölümündedir; bu renkler derin okyanusta daha kolay görülür.", "Most marine bioluminescence, for instance, is expressed in the blue-green part of the visible light spectrum. / These colors are more easily visible in the deep ocean.", NG),
    F(9, "Ateşböceği türlerinin çoğu yeşilimsi sarı ışık saçar, bazı türler mavi ya da beyaza yakın ışık saçar.", "Most species emit a greenish-yellow light, but some species showcase more of a blue or white hue.", NP),
    F(10, "Ateşböceğinin yanıp sönmesinin önemli bir amacı eş çekmektir; her türün kendine özgü bir yanıp sönme deseni vardır.", "The enchanting flash of a firefly serves a vital purpose: attracting a mate. / Each species of firefly possesses a unique flash pattern that plays a crucial role in their mating display.", NP),
    F(11, "Eşzamanlı ateşböceğinde 5 ile 8 arası belirgin parlamayı 8 saniyelik bir karanlık izler.", "a remarkable sequence of five to eight distinct flashes, followed by an eight-second pause of darkness", NP, ["5", "8"]),
    F(12, "Biyolüminesansı kullanan en ünlü avcı belki de avını cezbetmek için kullanan fener balığıdır.", "The most famous predator to use bioluminescence may be the anglerfish, which uses bioluminescence to lure prey.", NG),
    F(13, "Birçok deniz canlısı kendini korumak için karşı aydınlatma denen bir kamuflaj kullanır; baltabalıklarının ışık organları aşağı bakar, alttan çıkan ışığı yukarıdan gelen ışığa eşitler, böylece gölgelerini gizleyip aşağıdan bakan avcılara neredeyse görünmez olurlar.", "Many marine species use a technique called counterillumination to protect themselves. / Hatchetfish have light-producing organs that point downward. / They adjust the amount of light coming from their undersides to match the light coming from above. / they disguise their shadows and become virtually invisible to predators looking up.", NG),
    F(14, "Canlılar biyolüminesansı avlanmak, avcılara karşı korunmak ve eş bulmak için kullanır.", "Bioluminescence is used by living things to hunt prey, defend against predators, find mates", NG),
    F(15, "Birçok kalamar türü avcılarını ürkütmek için parlar; bazı böcek larvaları zehirli olduklarını avcılara bildirmek için ışık saçar.", "Many species of squid, for instance, flash to startle predators, such as fish. / light up to warn predators that they are toxic.", NG),
    F(16, "Tatlı su ortamlarına özgü ışık saçan canlı neredeyse yoktur.", "There are almost no bioluminescent organisms native to freshwater habitats.", NG),
    F(17, "Demiryolu solucanının başı kırmızı, gövdesi yeşil parlar.", "The head of the railroad worm glows red, while its body glows green.", NG),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Bir yaz gecesi çayırda minik ışıklar yanıp sönüyor. Bunlar lamba değil, ateşböcekleri!", [10]),
    L("Peki bir canlı, pil ya da kablo olmadan nasıl ışık yapar?"),
    L("Bugün ışık saçan canlıların sırrını çözüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Canlılar ışığı nasıl üretir? Bu ışık neden sıcak değildir? Ve neden ışık saçarlar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre canlıların vücutlarındaki kimyasal tepkimelerle saçtıkları ışığa biyolüminesans denir.", [1], f"{NGs}'e göre canlıların vücutlarındaki kimyasal tepkimelerle saçtıkları ışığa biyolüminesans denir."),
    L("ABD Milli Parklar Servisi'ne göre bunu yalnızca ateşböcekleri yapmaz; bazı mantarlar, balıklar, karidesler, denizanaları ve planktonlar da yapar.", [2]),
    L("Bu tepkimenin iki yıldızı var: lusiferin ve lusiferaz. Işığı asıl üreten bileşik lusiferindir.", [3]),
    L("Ateşböcekleri lusiferini oksijenle ve lusiferaz denen bir enzimle karıştırır. Sonuç: ışık!", [3]),
    L("Bazı canlılar lusiferaz yerine fotoprotein kullanır. Fotoproteinler ışık yapmak için çoğu zaman bir kalsiyum iyonuna ihtiyaç duyar.", [3, 4]),
    L("Benim de anten yıldızım parlıyor. Ama benimki tamamen pilden; içimde bir gram lusiferin yok!"),
])
e.sec("finding", [
    L("Bu ışığın şaşırtıcı bir özelliği var: Soğuk ışıktır.", [5]),
    L("National Geographic'e göre soğuk ışık, ışığın yüzde 20'sinden azının ısıya dönüşmesi demektir.", [5], f"{NGs}'e göre soğuk ışık, ışığın yüzde yirmisinden azının ısıya dönüşmesi demektir."),
    L("Eski tip akkor ampullerle karşılaştıralım. Milli Parklar Servisi'ne göre bu ampuller enerjilerinin yalnızca yüzde 10 kadarını ışığa çevirir; yüzde 90'ı ısı olur.", [6], "Eski tip akkor ampullerle karşılaştıralım. Milli Parklar Servisi'ne göre bu ampuller enerjilerinin yalnızca yüzde on kadarını ışığa çevirir; yüzde doksanı ısı olur."),
    L("Ateşböceğinin parıltısı ise neredeyse yüzde 100 ışıktır ve çok az ısı üretir.", [6], "Ateşböceğinin parıltısı ise neredeyse yüzde yüz ışıktır ve çok az ısı üretir."),
    L("Ben eski bir ampul olsaydım, kafam hep sıcacık olurdu. Neyse ki ben LED'liyim!"),
])
e.sec("importance", [
    L("Peki canlılar neden ışık saçar? National Geographic'e göre avlanmak, avcılara karşı korunmak ve eş bulmak için.", [14], f"Peki canlılar neden ışık saçar? {NGs}'e göre avlanmak, avcılara karşı korunmak ve eş bulmak için."),
    L("Ateşböceklerinde ışığın önemli bir görevi eş bulmaktır. Her türün kendine özgü bir yanıp sönme deseni vardır.", [10]),
    L("Örneğin eşzamanlı yanıp sönen bir türde, 5 ile 8 arası parlamayı 8 saniyelik bir karanlık izler.", [11], "Örneğin eşzamanlı yanıp sönen bir türde, beş ile sekiz arası parlamayı sekiz saniyelik bir karanlık izler."),
    L("Derin denizde ise fener balığı, ışığını avını cezbetmek için kullanır.", [12]),
    L("Baltabalığı gibi bazı balıklar karşı aydınlatma denen bir kamuflaj kullanır. Karınlarındaki ışık organları aşağıya bakar.", [13]),
    L("Alttan çıkan ışığı yukarıdan gelen ışığa eşitlerler. Böylece gölgeleri kaybolur ve aşağıdan bakan avcılara neredeyse görünmez olurlar.", [13]),
    L("Birçok kalamar türü avcılarını ürkütmek için parlar. Bazı böcek larvaları da zehirli olduklarını göstermek için ışık saçar.", [15]),
    L("Yani ışık; bir av tuzağı, bir görünmezlik pelerini ya da bir uyarı tabelası olabilir!", [12, 13, 15]),
    L("Denizdeki biyolüminesansın çoğu mavi-yeşil renktedir. Çünkü bu renkler derin okyanusta daha kolay görülür.", [8]),
    L("Ateşböceklerinin çoğu yeşilimsi sarı ışık saçar; bazı türlerinki ise maviye ya da beyaza kaçar.", [9]),
    L("Ben hangi renkte parlıyorum biliyor musun? Utanınca kıpkırmızı!"),
    L("Şimdi sıra sende! Yazın ateşböceklerinin yaşadığı bir yerdeysen, akşam karanlığında bir yetişkinle dışarı çık.", [10]),
    L("Işıkları dikkatle izle ve yanıp sönmeleri say. Hepsi aynı desende mi? Ateşböceklerini yakalama, yalnızca izle!", [10]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? National Geographic'e göre tatlı sulara özgü ışık saçan canlı neredeyse yoktur.", [16], f"Bunu biliyor muydun? {NGs}'e göre tatlı sulara özgü ışık saçan canlı neredeyse yoktur."),
    L("Bir de demiryolu solucanı var: başı kırmızı, gövdesi yeşil parlar. Yürüyen bir trafik ışığı gibi!", [17]),
    L("Hızlı soru! Işığı asıl üreten bileşiğin adı neydi?", [3]),
    L("Düşün bakalım... Evet: lusiferin!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Işığın hiç sönmesin!"),
])
S = e.S
S(3, {"type": "hook", "question": "Canlılar nasıl ışık saçar?", "emoji": "✨"}, ["🌙", "🌾"], ["ATEŞBÖCEKLERİ", "PİLSİZ IŞIK?", ""])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Canlılar ışığı nasıl üretir?", "Bu ışık neden sıcak değil?", "Neden ışık saçarlar?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Biyolüminesans", "emoji": "✨", "chips": [{"label": "Kimyasal tepkimeyle ışık", "emoji": "🧪"}, {"label": "Mantarlar", "emoji": "🍄"}, {"label": "Denizanaları", "emoji": "🪼"}, {"label": "Planktonlar", "emoji": "🦠"}]}, ["🌙", "🐟"], ["BİYOLÜMİNESANS", "KARADA DA DENİZDE DE", "LUSİFERİN"])
S(3, {"type": "diagram", "title": "Işık tarifi", "layout": "flow", "nodes": [{"label": "Lusiferin", "emoji": "🧪"}, {"label": "Oksijen", "emoji": "💨"}, {"label": "Lusiferaz enzimi", "emoji": "🔧"}, {"label": "Işık!", "emoji": "💡"}]}, ["✨", "🔋"], ["KARIŞTIR!", "FOTOPROTEİN", "PİLLİ MUMA 🔋"], fx="sparkle")
S(2, {"type": "big-number", "value": "%20", "label": "Soğuk ışıkta ısıya dönüşen pay bundan az", "sub": "National Geographic", "icon": "❄️"}, ["🌡️", "💡"], ["SOĞUK IŞIK ❄️", "ISI AZ"])
S(3, {"type": "bar-chart", "title": "Enerjinin ne kadarı ışık olur? (%)", "unit": "%", "bars": [{"label": "Akkor ampul: ışık", "value": 10, "display": "%10"}, {"label": "Akkor ampul: ısı", "value": 90, "display": "%90"}, {"label": "Ateşböceği: ışık", "value": 100, "display": "%100'e yakın", "highlight": True}]}, ["💡", "🔥"], ["AMPUL 🔥", "ATEŞBÖCEĞİ ✨", "LED'Lİ MUMA 😄"])
S(3, {"type": "meter", "title": "Ateşböceğinin ışık mesajı", "label": "Işık", "emoji": "✨", "phases": [{"label": "Eş bulmak için yanar", "level": 0.6, "emoji": "💌"}, {"label": "Her türün kendi deseni", "level": 0.8, "emoji": "🔦"}, {"label": "Parlamalar, sonra karanlık", "level": 0.1, "emoji": "🌑"}], "note": NOTE}, ["🌾", "🌙"], ["NEDEN PARLAR?", "EŞ BULMAK 💌", "DESEN"])
S(1, {"type": "big-number", "value": "Fener balığı", "label": "Işığıyla avını cezbeder", "sub": "National Geographic", "icon": "🎣"}, ["🐟", "🌊"], ["AV TUZAĞI 🎣"])
S(2, {"type": "stages", "title": "Karşı aydınlatma", "rows": [{"label": "Işık organı aşağı bakar", "emoji": "🐟"}, {"label": "Yukarıdaki ışığa eşitler", "emoji": "☀️"}, {"label": "Gölge kaybolur", "emoji": "👻"}, {"label": "Avcı göremez", "emoji": "🦈"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim."}, [], ["KAMUFLAJ", "GÖRÜNMEZ 👻"])
S(2, {"type": "comparison", "title": "Işığın işleri", "left": {"title": "Bulmak için 🔎", "items": ["Fener balığı: av", "Ateşböceği: eş"]}, "right": {"title": "Korunmak için 🛡️", "items": ["Baltabalığı: görünmez", "Kalamar: ürkütür", "Larvalar: uyarır"]}}, ["🦑", "🛡️"], ["ÜRKÜT! 🦑", "UYARI ⚠️"])
S(3, {"type": "spotlight", "title": "Işığın rengi", "emoji": "🎨", "chips": [{"label": "Deniz: mavi-yeşil", "emoji": "🌊"}, {"label": "Ateşböceği: yeşilimsi sarı", "emoji": "🟡"}, {"label": "Bazıları: mavi ya da beyaz", "emoji": "⚪"}]}, ["🌊", "😳"], ["MAVİ-YEŞİL", "YEŞİLİMSİ SARI", "KIPKIRMIZI 😳"])
S(2, {"type": "bullets", "title": "Sen de dene: ışıkları say", "items": ["Bir yetişkinle akşam dışarı çık", "Yanıp sönmeleri say", "Desenleri karşılaştır", "Yakalama, yalnızca izle"], "tone": "caution"}, ["🌙", "📓"], ["DENEY ZAMANI 🔬", "YALNIZCA İZLE 👀"])
S(2, {"type": "big-number", "value": "Neredeyse yok", "label": "Tatlı sulara özgü ışık saçan canlı", "sub": "National Geographic", "icon": "🏞️"}, ["🚦", "🪱"], ["BUNU BİLİYOR MUYDUN?", "TRAFİK IŞIĞI 🚦"])
S(2, {"type": "hook", "question": "Işığı asıl üreten bileşiğin adı ne?", "emoji": "🤔"}, ["🧪", "✨"], ["HIZLI SORU!", "LUSİFERİN ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 29, "videoTitle": "Canlılar nasıl ışık saçar?", "paperTitleTr": "Canlılar nasıl ışık saçar?",
  "theme": {"backdrop": "night", "actors": [{"kind": "fly", "emoji": "🦉", "every": 34}]},
  "takeaways": ["Canlılar ışığı lusiferinle yapılan kimyasal tepkimelerle üretir", "Bu ışık soğuktur: çok az ısı üretir", "Işık av, korunma ve eş bulma için kullanılır"],
  "description": "Ateşböcekleri, denizanaları, fener balıkları ve mantarlar nasıl ışık saçar? Bu bölümde biyolüminesansı; lusiferin, lusiferaz ve fotoproteinlerle yapılan kimyasal tepkimeyi, soğuk ışığı, ateşböceklerinin yanıp sönme desenlerini, fener balığının av tuzağını ve baltabalığının karşı aydınlatma kamuflajını keşfediyoruz. Sonunda ateşböceği gözlemi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Biyolüminesans", "meaning": "Canlıların vücutlarındaki kimyasal tepkimelerle ışık saçması."},
    {"term": "Lusiferin", "meaning": "Biyolüminesansta ışığı asıl üreten bileşik."},
    {"term": "Lusiferaz", "meaning": "Lusiferinin ışık saçan tepkimesine yardım eden enzim."},
    {"term": "Fotoprotein", "meaning": "Bazı canlılarda lusiferaz yerine ışık tepkimesinde görev alan protein."},
    {"term": "Soğuk ışık", "meaning": "Çok az ısı üreten ışık."},
    {"term": "Karşı aydınlatma", "meaning": "Bazı deniz canlılarının alttan ışık saçarak gölgelerini gizlediği kamuflaj."},
    {"term": "Kamuflaj", "meaning": "Bir canlının çevresine uyum sağlayarak gizlenmesi."}],
  "song": e.song("Gecenin Fenerleri", [("✨", "Işık"), ("🧪", "Lusiferin"), ("🐟", "Fener balığı"), ("🪼", "Denizanası"), ("🌙", "Gece")],
    ["Gece çöktü, çayır karanlık", "Ateşböceği yaktı fenerini", "Lusiferin, oksijen bir araya", "Lusiferaz karıştırır, parlar ışık"],
    ["Parla, parla, soğuk ışık!", "Isı yok, yalnızca parıltı", "Eşini çağırır kendi deseniyle", "Gecenin fenerleri yanar"],
    ["Derin denizde mavi-yeşil", "Fener balığı tuzak kurar", "Baltabalığı gölgesini siler", "Kalamar parlar, avcı kaçar"],
    ["Parla, parla, soğuk ışık!", "Isı yok, yalnızca parıltı", "Akşam çık, ışıkları say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "✨"}, {"kind": "swim", "emoji": "🐟"}, {"kind": "swim", "emoji": "🪼"}, {"kind": "hop", "emoji": "🍄"}])}
e.write(D, facts, script)
