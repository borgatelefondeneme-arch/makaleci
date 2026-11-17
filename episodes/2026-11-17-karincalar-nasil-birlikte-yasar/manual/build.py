"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:karincalar-nasil-birlikte-yasar"
NG = "National Geographic — Ants"; AM = "Australian Museum — Ants: Family Formicidae"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Ants", "publisher": "National Geographic", "url": "https://www.nationalgeographic.com/animals/invertebrates/facts/ants"},
    {"id": "k2", "title": "Ants: Family Formicidae", "publisher": "Avustralya Müzesi", "url": "https://australian.museum/learn/animals/insects/ants-family-formicidae/"}],
  "facts": [
    F(1, "Karıncalar feromon denen koku kimyasalları salgılayarak iletişim kurar ve iş birliği yapar; bu kimyasallar diğerlerini tehlikeye karşı uyarabilir ya da onları umut veren bir besin kaynağına götürebilir.", "Ants communicate and cooperate by secreting pheromones, or scent chemicals, / that can alert others to danger or lead them to a promising food source.", NG),
    F(2, "Karıncalar hayvanlar âlemindeki en karmaşık kimyasal iletişime sahiptir; birlikte, tek bir böceğin yapamayacağı işleri başarırlar; başarılarının bir nedeni birbirleriyle iletişim kurabilmeleridir.", "They have the most complex form of chemical communication in the animal kingdom / together they accomplish tasks beyond any individual insect. / Their success, in part, is because of their ability to communicate with each other.", AM),
    F(3, "Koloni büyüklüğü türe göre birkaç bireyden on binlerce bireye kadar değişir; tek bir koloni yüz binlerce karınca barındırabilir.", "Colony sizes range from a few individuals to tens of thousands. / A single ant colony can contain hundreds of thousands of individual ants.", AM + "; " + NG),
    F(4, "Topluluğu bir ya da birden çok kraliçe yönetir; kraliçeler binlerce yumurta bırakır; genellikle yalnızca kraliçeler yumurtlar, işçiler üreyemez.", "Communities are headed by a queen or queens / Queens lay thousands of eggs to ensure the survival of the colony. / Workers are generally unable to reproduce, with only queens laying eggs.", NG + "; " + AM),
    F(5, "İşçi karıncalar hiç üremeyen dişilerdir; besin arar, kraliçenin yavrularına bakar, yuvada çalışır ve topluluğu korur.", "Worker ants, the most visible colony members, are females that never reproduce / but instead forage for food, care for the queen's offspring, work on the nest, and protect the community.", NG),
    F(6, "Kanatlı karıncalar çiftleşmek ve yeni koloniler kurmak için yuvadan ayrılır; yalnızca üreyebilen karıncaların kanadı vardır.", "Winged ants leave the nest to mate and found new colonies in late summer and spring, often after rain. / Only reproductives have wings,", AM),
    F(7, "Askerler rahatsızlığa karşı çıkar; ısırarak, asidik kimyasal fışkırtarak ya da sokarak tepki verebilir.", "Soldiers often confront the disturbance and may react by biting, squirting acidic chemicals or stinging.", AM),
    F(8, "Karıncalar yer altında, toprak tümseklerinde ya da ağaçlarda yuvalarda yaşar; yuvalarda yumurtalar, larvalar ve pupalar bulunur; bazı karıncalar yaprakları ipekle birleştirerek yuva yapar.", "that may be located underground, in ground-level mounds, or in trees. / Nests contain eggs, larvae and pupae and different types (or castes) of ants. / Some specialised ants construct nests by joining leaves with silk.", NG + "; " + AM),
    F(9, "Ordu karıncaları gibi bazı türlerin kalıcı yuvası yoktur.", "Some species, such as army ants, defy the norm and do not have permanent homes.", NG),
    F(10, "Bazı işçi karıncalar kendi vücut ağırlıklarının 50 katını taşıyabilir.", "Some workers can carry 50 times their own body weight.", NG, ["50"]),
    F(11, "Dünya'da 20 katrilyon karınca vardır; bu, insan başına 2,5 milyon karınca demektir.", "There are 20 quadrillion ants on Earth—that's 2.5 million ants for every human.", NG, ["20", "2.5"]),
    F(12, "Karıncalar dirsekli antenlerinden ve karın ile göğüs arasındaki ince 'bel'den tanınır; altı ince bacakları vardır.", "Ants can be identified by their elbowed antennae, and narrow \"waist\" between the abdomen and thorax. / Six slender legs.", NG + "; " + AM),
    F(13, "Türe göre gruplar halinde ya da tek başına besin ararlar; besin ararken çoğu zaman zikzak çizerler; bazı türler sıralar halinde, çoğu zaman yollar üzerinde koşar.", "Depending on the species they will forage in groups, or sometimes as individuals. / They often move in a zigzag motion searching for food items. / Some species of ants run in lines, often on paths.", AM),
    F(14, "Bir karınca türü yaralı karıncaları geride bırakmaz, iyileşebilecekleri yuvaya geri taşır.", "Instead of leaving the hurt ants behind, other ants will carry them back home where they can heal", NG),
    F(15, "Karıncalar sel sularından birbirine tutunup kümelenerek suyun yüzeyinde yüzerek kurtulabilir.", "They can also survive floods by clumping together to float on the water's surface.", NG),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Yere bir kırıntı düşür ve bekle. Bir süre sonra karıncalar gelir, hem de sıra sıra! Onlara kim haber verdi?", [1, 13]),
    L("Ne telefonları var ne de konuşabiliyorlar. Peki nasıl anlaşıyorlar?"),
    L("Bugün yerin altına, bir karınca kolonisine giriyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Karıncalar nasıl haberleşir? Kolonide kim ne iş yapar? Ve yuvaları nasıldır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre karıncalar feromon denen koku kimyasalları salgılayarak haberleşir.", [1], f"{NGs}'e göre karıncalar feromon denen koku kimyasalları salgılayarak haberleşir."),
    L("Feromonlar diğer karıncaları tehlikeye karşı uyarabilir ya da onları bir besin kaynağına götürebilir.", [1]),
    L("Yani karıncalar kokuyla mesajlaşır. Ben de mesaj atarım, ama benimkiler koku değil, bip bip!"),
    L("Avustralya Müzesi'ne göre karıncalar hayvanlar âlemindeki en karmaşık kimyasal iletişime sahiptir.", [2]),
    L("Birlikte, tek bir böceğin asla yapamayacağı işleri başarırlar.", [2]),
    L("Besin ararken türüne göre gruplar halinde ya da tek başına dolaşırlar. Çoğu zaman zikzak çizerler, bazı türler ise yollar üzerinde sıra halinde koşar.", [13]),
])
e.sec("finding", [
    L("Karıncalar koloni denen büyük topluluklarda yaşar. Bir koloni, türüne göre birkaç bireyden yüz binlerce karıncaya kadar büyüyebilir.", [3]),
    L("Koloniyi bir ya da birden çok kraliçe yönetir. Kraliçeler binlerce yumurta bırakır; genellikle yalnızca onlar yumurtlar.", [4]),
    L("En sık gördüğün karıncalar işçilerdir. İşçiler, hiç üremeyen dişi karıncalardır.", [5]),
    L("Besin ararlar, kraliçenin yavrularına bakarlar, yuvada çalışırlar ve topluluğu korurlar.", [5]),
    L("Ben de çok çalışkanım. Ama işçi karınca gibi değil; ben bir şarjla ancak bir video çekebiliyorum!"),
    L("Bazı türlerde askerler vardır. Askerler tehlikeye karşı ısırarak, asidik kimyasal fışkırtarak ya da sokarak karşılık verebilir.", [7]),
    L("Kanatlı karıncalar ise çiftleşmek ve yeni koloniler kurmak için yuvadan ayrılır. Kolonide yalnızca üreyebilenlerin kanadı vardır.", [6]),
])
e.sec("importance", [
    L("Peki yuvaları nerede? Yer altında, toprak tümseklerinde, hatta ağaçlarda olabilir.", [8]),
    L("Yuvanın içinde yumurtalar, larvalar ve pupalar bulunur. Bazı karıncalar yaprakları ipekle birleştirerek yuva yapar.", [8]),
    L("Ordu karıncaları gibi bazı türlerin ise kalıcı bir yuvası yoktur. Hep yoldalar, tıpkı benim gibi gezgin!", [9]),
    L("Karıncalar çok güçlüdür. National Geographic'e göre bazı işçiler kendi vücut ağırlıklarının 50 katını taşıyabilir!", [10], f"Karıncalar çok güçlüdür. {NGs}'e göre bazı işçiler kendi vücut ağırlıklarının elli katını taşıyabilir!"),
    L("Bir karınca türü, yaralı arkadaşlarını geride bırakmaz. Onları iyileşebilecekleri yuvaya geri taşır.", [14]),
    L("Sel geldiğinde ise karıncalar birbirine tutunup küme oluşturur ve suyun üstünde yüzerek kurtulabilir.", [15]),
    L("Şimdi sıra sende! Bir yetişkinle bahçede ya da parkta bir karınca yolu bul.", [13]),
    L("Yolun yakınına minicik bir ekmek kırıntısı bırak ve izle. Karıncalar kırıntıyı buluyor mu? Sıra halinde mi geliyorlar? Karıncalara dokunma; bazıları ısırabilir ya da sokabilir.", [1, 7, 13]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? National Geographic'e göre Dünya'da 20 katrilyon karınca var. Bu, insan başına 2,5 milyon karınca demek! Saymaya kalksam pilim biter!", [11], f"Bunu biliyor muydun? {NGs}'e göre Dünya'da yirmi katrilyon karınca var. Bu, insan başına iki buçuk milyon karınca demek! Saymaya kalksam pilim biter!"),
    L("Hızlı soru! Karıncaların haberleşmek için salgıladığı koku kimyasallarına ne denir?", [1]),
    L("Düşün bakalım... Evet: feromon!", [1]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bir dahaki sefere karıncaları görünce selam ver!"),
])
S = e.S
S(3, {"type": "hook", "question": "Karıncalar nasıl birlikte yaşar?", "emoji": "🐜"}, ["🍞", "🌿"], ["KİM HABER VERDİ?", "TELEFONSUZ", "KOLONİYE GİRİŞ"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Karıncalar nasıl haberleşir?", "Kolonide kim ne iş yapar?", "Yuvaları nasıldır?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "diagram", "title": "Koku mesajı", "layout": "flow", "nodes": [{"label": "Feromon salgılar", "emoji": "💨"}, {"label": "Diğerleri kokuyu alır", "emoji": "🐜"}, {"label": "Tehlike ya da besin!", "emoji": "🍞"}]}, ["📱", "🐜"], ["FEROMON", "KOKUYLA MESAJ", "BİP BİP 📱"])
S(3, {"type": "spotlight", "title": "Ekip işi", "emoji": "🤝", "chips": [{"label": "En karmaşık kimyasal iletişim", "emoji": "🧪"}, {"label": "Birlikte büyük işler", "emoji": "💪"}, {"label": "Zikzak ya da sıra halinde", "emoji": "〰️"}]}, ["🧪", "🐜"], ["KİMYASAL İLETİŞİM", "BİRLİKTE GÜÇLÜ", "ZİKZAK"])
S(2, {"type": "big-number", "value": "Yüz binlerce", "label": "Tek bir kolonide olabilecek karınca", "sub": "National Geographic", "icon": "🏘️"}, ["👑", "🥚"], ["KOLONİ", "KRALİÇE 👑"])
S(3, {"type": "comparison", "title": "Kolonide iş bölümü", "left": {"title": "Kraliçe 👑", "items": ["Binlerce yumurta bırakır", "Koloniyi yönetir"]}, "right": {"title": "İşçi 🐜", "items": ["Hiç üremeyen dişi", "Besin arar, yavrulara bakar", "Yuvada çalışır, korur"]}}, ["🔋", "🥚"], ["İŞÇİLER", "ÇOK İŞ!", "TEK ŞARJ 🔋"])
S(2, {"type": "spotlight", "title": "Diğer görevler", "emoji": "🛡️", "chips": [{"label": "Askerler: ısırır, sokar", "emoji": "⚔️"}, {"label": "Kanatlılar: yeni koloni", "emoji": "🪽"}]}, ["⚔️", "🪽"], ["ASKERLER", "KANATLI KARINCALAR"])
S(3, {"type": "stages", "title": "Yuva katları", "rows": [{"label": "Yer altı, tümsek ya da ağaç", "emoji": "🌳"}, {"label": "Yumurtalar", "emoji": "🥚"}, {"label": "Larvalar", "emoji": "🐛"}, {"label": "Pupalar", "emoji": "🫘"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 1, "note": "Şematik çizim."}, [], ["YUVA", "YAPRAK VE İPEK", "ORDU KARINCALARI"], fx="dig")
S(1, {"type": "big-number", "value": "50 kat", "label": "Bazı işçiler vücut ağırlığının bu kadarını taşır", "sub": "National Geographic", "icon": "🏋️"}, ["🏋️", "🍃"], ["SÜPER GÜÇ 💪"])
S(2, {"type": "diagram", "title": "Yardımlaşma", "layout": "flow", "nodes": [{"label": "Yaralıyı yuvaya taşır", "emoji": "🚑"}, {"label": "Selde küme olur", "emoji": "🌊"}, {"label": "Yüzerek kurtulur", "emoji": "🛟"}]}, ["🌊", "🤝"], ["YARALIYI BIRAKMAZ", "CANLI SAL 🛟"])
S(2, {"type": "bullets", "title": "Sen de dene: karınca yolu", "items": ["Bir yetişkinle karınca yolu bul", "Minicik bir kırıntı bırak", "Sıra halinde geliyorlar mı?", "Dokunma: ısırabilir, sokabilir"], "tone": "caution"}, ["🍞", "🔍"], ["DENEY ZAMANI 🔬", "DOKUNMA ⚠️"])
S(1, {"type": "big-number", "value": "20 katrilyon", "label": "Dünya'daki karınca sayısı (insan başına 2,5 milyon)", "sub": "National Geographic", "icon": "🌍"}, ["🌍", "🐜"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Karıncaların koku kimyasallarına ne denir?", "emoji": "🤔"}, ["💨", "🐜"], ["HIZLI SORU!", "FEROMON ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 33, "videoTitle": "Karıncalar nasıl birlikte yaşar?", "paperTitleTr": "Karıncalar nasıl birlikte yaşar?",
  "theme": {"backdrop": "underground", "actors": [{"kind": "walk", "emoji": "🐜", "every": 26}]},
  "takeaways": ["Karıncalar feromon denen koku kimyasallarıyla haberleşir", "Kolonide kraliçe yumurtlar, işçiler besin arar, yavrulara bakar ve yuvayı korur", "Yuvalar yer altında, tümseklerde ya da ağaçlarda olabilir"],
  "description": "Karıncalar telefonsuz nasıl haberleşir? Bu bölümde feromonları, kolonideki iş bölümünü (kraliçe, işçi, asker, kanatlı karıncalar), yuvaları, karıncaların gücünü ve yardımlaşmasını keşfediyoruz. Sonunda karınca yolu gözlemi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Feromon", "meaning": "Hayvanların birbirine mesaj vermek için salgıladığı koku kimyasalı."},
    {"term": "Koloni", "meaning": "Birlikte yaşayan ve iş bölümü yapan büyük karınca topluluğu."},
    {"term": "Kraliçe", "meaning": "Kolonide yumurta bırakan karınca."},
    {"term": "İşçi", "meaning": "Besin arayan, yavrulara bakan ve yuvada çalışan, üremeyen dişi karınca."},
    {"term": "Larva", "meaning": "Yumurtadan çıkan, henüz yetişkin olmamış böcek evresi."},
    {"term": "Pupa", "meaning": "Larva ile yetişkin arasındaki dönüşüm evresi."}],
  "song": e.song("Koku Yolu", [("🐜", "İşçi"), ("👑", "Kraliçe"), ("💨", "Feromon"), ("🥚", "Yumurta"), ("🏘️", "Koloni")],
    ["Bir kırıntı düştü yere", "Feromon yayıldı havaya", "Haber gitti yuvaya", "Sıra sıra geldi karıncalar"],
    ["Koku yolu, koku yolu!", "Birlikte güçlüyüz, koloni bu", "Kraliçe yumurtlar, işçi çalışır", "Toprağın altında bir şehir var"],
    ["Askerler korur yuvayı", "Kanatlılar kurar yeni koloni", "Elli kat yük taşır işçi", "Selde bile birlik olur"],
    ["Koku yolu, koku yolu!", "Birlikte güçlüyüz, koloni bu", "Kırıntı bırak, uzaktan izle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "walk", "emoji": "🐜"}, {"kind": "hop", "emoji": "👑"}, {"kind": "walk", "emoji": "🐜"}, {"kind": "hop", "emoji": "🍞"}])}
e.write(D, facts, script)
