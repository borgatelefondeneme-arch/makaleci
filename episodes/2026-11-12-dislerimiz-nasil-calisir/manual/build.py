"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:dislerimiz-nasil-calisir"
KH = "Nemours KidsHealth — Mouth & Teeth"; NI = "NIH (NIDCR) — The Tooth Decay Process"; NH = "NHS — How to keep your teeth clean"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Mouth & Teeth", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/teeth.html"},
    {"id": "k2", "title": "The Tooth Decay Process: How to Reverse It and Avoid a Cavity", "publisher": "NIH", "url": "https://www.nidcr.nih.gov/health-info/tooth-decay/more-info/tooth-decay-process"},
    {"id": "k3", "title": "How to keep your teeth clean", "publisher": "NHS", "url": "https://www.nhs.uk/live-well/healthy-teeth-and-gums/how-to-keep-your-teeth-clean/"}],
  "facts": [
    F(1, "İlk diş takımı 20 süt dişidir; yerlerini 32 kalıcı diş alır. Süt dişleri doğumdan önce gelişmeye başlar ve çocuk yaklaşık 6 yaşındayken düşmeye başlar.", "The first set are 20 deciduous (pronounced: duh-SID-you-wus) teeth / They're replaced by a set of 32 permanent teeth, which are also called secondary or adult teeth. / They begin to develop before birth and begin to fall out when a child is around 6 years old.", KH, ["20", "32", "6"]),
    F(2, "İlk kalıcı azı dişleri ('6 yaş dişleri') 5–7 yaş arasında, ikinci kalıcı azılar ('12 yaş dişleri') 11–14 yaş arasında çıkar; üçüncü azılar yirmi yaş dişleridir.", "The first permanent molars called, \"6 year molars,\" come in between the ages of 5 and 7. / The second permanent molars, \"12 year molars,\" come in when a child is between 11 and 14 years old. / The third molars are the wisdom teeth.", NI + "; " + KH, ["6", "5", "7", "12", "11", "14"]),
    F(3, "Dişler konuşmak ve düzgün yemek için gereklidir; yerken dişlerimiz besini yutmaya hazırlamak için yırtar, keser ve öğütür.", "You need teeth to talk and eat properly. / When we eat, our teeth tear, cut, and grind food in preparation for swallowing.", KH),
    F(4, "İnsan dişleri dört dokudan oluşur: öz (pulpa), dentin, mine ve sement.", "Human teeth are made up of four different types of tissue: pulp, dentin, enamel, and cementum.", KH),
    F(5, "Mine vücudun en sert dokusudur; dentini örter ve kronun en dış katmanını oluşturur.", "Enamel, the hardest tissue in the body, covers the dentin and forms the outermost layer of the crown.", KH),
    F(6, "Dentin sert, sarı bir maddedir; dişin büyük bölümünü oluşturur ve kemik kadar serttir.", "A hard yellow substance, it makes up most of the tooth and is as hard as bone.", KH),
    F(7, "Öz (pulpa) dişin en iç kısmıdır; bağ dokusu, sinirler ve kan damarlarından oluşur.", "The pulp is the innermost portion of the tooth and consists of connective tissue, nerves, and blood vessels,", KH),
    F(8, "Sement kökün dışını diş etinin altında örter ve dişi çene kemiğinde yerinde tutar.", "A layer of cementum covers the outside of the root, under the gum line, and holds the tooth in place within the jawbone.", KH),
    F(9, "Kesici dişler ağzın önündeki keskin kenarlı dişlerdir ve ısırdığımızda besini keser; yanlarında sivri köpek dişleri bulunur; küçük azılar besini öğütüp ezer; azı dişleri güçlü çiğnemeyi sağlar.", "Incisors are the squarish, sharp-edged teeth in the front of the mouth that cut foods when we bite into them. / On either side of the incisors are the sharp canines. / Behind the canines are the premolars, or bicuspids, which grind and mash foods. / The molars, found behind the premolars, have points and grooves, and allow for vigorous chewing.", KH),
    F(10, "Diş çürüğü, besinlerdeki şekerleri kullanarak asit yapan bazı bakterilerin yol açtığı bir enfeksiyondur; asitler minenin sert dış yüzeyini aşındırmaya başlar; tekrarlanan asit saldırıları minenin mineral kaybetmesine yol açar.", "Tooth decay is the result of an infection with certain types of bacteria that use sugars in food to make acids. / These acids begin to eat away at the tooth's hard outer surface, or enamel. / the repeated cycles of acid attacks cause the enamel to continue to lose minerals.", NI),
    F(11, "Plak, bakterilerden oluşan yapışkan, renksiz bir tabakadır; ağzımızda yüzlerce farklı türde bakteri yaşar.", "a sticky, colorless film of bacteria / Hundreds of different types live on our teeth, gums, tongue, and other places in our mouths.", NI),
    F(12, "Bu aşamada çürük durdurulabilir ya da geri döndürülebilir; mine tükürükteki mineralleri ve diş macunu gibi kaynaklardaki florürü kullanarak kendini onarabilir.", "Tooth decay can be stopped or reversed at this point. / Enamel can repair itself by using minerals from saliva, and fluoride from toothpaste or other sources.", NI),
    F(13, "Oyuk (kavite), dişçinin dolguyla onarması gereken kalıcı bir hasardır.", "A cavity is permanent damage that a dentist has to repair with a filling.", NI),
    F(14, "Gün boyunca ağzımızda bir halat çekme yarışı sürer.", "Throughout the day, a tug-of-war takes place inside our mouths.", NI),
    F(15, "Dişleri günde iki kez, yaklaşık 2 dakika florürlü diş macunuyla fırçalamak gerekir; dişler arası günde bir kez ip ile temizlenmelidir.", "Brush your teeth with fluoride toothpaste twice a day for about 2 minutes to help keep your teeth and mouth healthy. / Brush your teeth twice a day for two minutes at a time. Floss the teeth once a day.", NH + "; " + KH, ["2"]),
    F(16, "Şeker, kurabiye, gazlı ve şekerli içecekler özel günlere saklanmalı; meyve suyu, şekerli atıştırmalıklar ve kuru meyve gibi yapışkan besinler sınırlanmalıdır; dişçiye düzenli gidilmelidir.", "Save candy, cookies, soda, and other sugary drinks for special occasions. / Limit juice, sugary snacks, and sticky foods like dried fruit. / Visit a dentist regularly for cleanings and an examination.", NI + "; " + KH),
    F(17, "Fissür örtücüler, arka dişlerin (azıların) çiğneme yüzeylerine sürülen ince plastik kaplamalardır; çocuklarda ve gençlerde çürüklerin çoğu azı dişlerinde gelişir.", "Sealants are thin, plastic coatings painted onto the chewing surfaces of the back teeth, or molars. / since most cavities in children and adolescents develop in the molars (the back teeth)", NI),
    F(18, "Uyku sırasında tükürük akışı azalır.", "Saliva flow decreases during sleep.", NI),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; EN = "En Ay Eyç"
e.sec("hook", [
    L("Ağzının içinde, vücudunun en sert maddesiyle kaplı bir alet takımı var!", [5]),
    L("Dişlerin nasıl bu kadar güçlü? Ve küçük bir şeker parçası onlara nasıl zarar verebilir?"),
    L("Bugün ağzının içine bir keşif yapıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Bir diş neyden yapılır? Hangi diş ne iş yapar? Ve çürük nasıl başlar?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre ilk diş takımımız 20 süt dişinden oluşur. Onların yerini 32 kalıcı diş alır.", [1], f"{KHs}'e göre ilk diş takımımız yirmi süt dişinden oluşur. Onların yerini otuz iki kalıcı diş alır."),
    L("Süt dişleri daha doğmadan gelişmeye başlar ve yaklaşık 6 yaşında düşmeye başlar.", [1], "Süt dişleri daha doğmadan gelişmeye başlar ve yaklaşık altı yaşında düşmeye başlar."),
    L("Benim dişim yok. Ama vidalarım da hiç düşmedi, o da bir başarı!"),
    L("Bir diş dört dokudan yapılır: mine, dentin, öz ve sement.", [4]),
    L("En dışta mine vardır. Mine, vücudunun en sert dokusudur ve dişin görünen kısmı olan kronu örter.", [5]),
    L("Minenin altında dentin bulunur: sarımsı, kemik kadar sert bir madde. Dişin büyük bölümünü o oluşturur.", [6]),
    L("En içte öz, yani pulpa vardır. Sinirler ve kan damarları buradadır; dişin sıcağı soğuğu hissetmesi buradan gelir.", [7]),
    L("Kökün dışını ise sement örter. Diş etinin altında kalır ve dişi çene kemiğinde sıkıca tutar.", [8]),
])
e.sec("finding", [
    L("Peki hangi diş ne iş yapar? Öndeki keskin kenarlı dişlere kesici denir: ısırdığımızda besini keserler.", [9]),
    L("Yanlarında sivri köpek dişleri durur.", [9]),
    L("Arkada küçük azılar besini öğütüp ezer. En arkadaki azı dişleri ise girintili çıkıntılı yüzeyleriyle güçlü çiğnemeyi sağlar.", [9]),
    L("Yani ağzında bir makas, bir öğütücü ve bir değirmen var. Mutfak robotu gibisin!", [3, 9]),
    L("İlk kalıcı azılar 5–7 yaş arasında çıkar; bunlara 6 yaş dişleri denir.", [2], "İlk kalıcı azılar beş ile yedi yaş arasında çıkar; bunlara altı yaş dişleri denir."),
    L("İkinci kalıcı azılar 11–14 yaş arasında gelir; bunlar da 12 yaş dişleri. Üçüncü azılar ise yirmi yaş dişleridir.", [2], "İkinci kalıcı azılar on bir ile on dört yaş arasında gelir; bunlar da on iki yaş dişleri. Üçüncü azılar ise yirmi yaş dişleridir."),
    L("Dişler yalnızca yemek için değil: düzgün konuşmak için de onlara ihtiyacımız var.", [3]),
])
e.sec("importance", [
    L("Şimdi çürüğe gelelim. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre ağzımızda yüzlerce farklı türde bakteri yaşar.", [11], f"Şimdi çürüğe gelelim. Amerikan Ulusal Sağlık Enstitüleri, {EN}'ye göre ağzımızda yüzlerce farklı türde bakteri yaşar."),
    L("Bazı bakteriler dişlerin üstünde plak denen yapışkan, renksiz bir tabaka oluşturur.", [11]),
    L("Bu bakteriler besinlerdeki şekeri kullanarak asit üretir. Asit de minenin sert yüzeyini aşındırmaya başlar.", [10]),
    L("Asit saldırıları tekrarlandıkça mine mineral kaybeder.", [10]),
    L("NIH bunu şöyle anlatıyor: gün boyunca ağzımızda bir halat çekme yarışı sürer.", [14], f"{EN} bunu şöyle anlatıyor: gün boyunca ağzımızda bir halat çekme yarışı sürer."),
    L("Bir tarafta şeker ve bakteriler. Öbür tarafta tükürük ve florür: mine, tükürükteki mineralleri ve diş macunundaki florürü kullanarak kendini onarabilir.", [12]),
    L("Erken aşamada çürük durdurulabilir, hatta geri döndürülebilir.", [12]),
    L("Ama bakteriler kazanırsa dişte oyuk oluşur. Bu kalıcı bir hasardır ve dişçinin dolguyla onarması gerekir.", [13]),
    L("Halat çekmede hangi tarafı tuttuğunu biliyorsun, değil mi?"),
    L("Kazanmanın yolu basit: dişlerini günde iki kez, yaklaşık 2 dakika florürlü macunla fırçala. Dişlerinin arasını da günde bir kez diş ipiyle temizle.", [15], "Kazanmanın yolu basit: dişlerini günde iki kez, yaklaşık iki dakika florürlü macunla fırçala. Dişlerinin arasını da günde bir kez diş ipiyle temizle."),
    L("Şekerli içecekleri ve yapışkan atıştırmalıkları sınırla; dişçine de düzenli git.", [16]),
    L("Şimdi sıra sende! İki dakikalık bir şarkı seç ve dişlerini şarkı bitene kadar fırçala. Sonra aynada azı dişlerinin girintili yüzeyine bak.", [15, 9]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Çocuklarda ve gençlerde çürüklerin çoğu arkadaki azı dişlerinde gelişir. Dişçiler bu dişlerin yüzeyini ince bir plastik kaplamayla koruyabilir.", [17]),
    L("Bir de şu: uyurken tükürük akışı azalır. Bu yüzden yatmadan önce fırçalamak çok önemli!", [18]),
    L("Hızlı soru! Vücudun en sert dokusu hangisidir?", [5]),
    L("Düşün bakalım... Evet: diş minesi!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bu akşam fırçalamayı da!"),
])
S = e.S
S(3, {"type": "hook", "question": "Dişlerimiz nasıl çalışır?", "emoji": "🦷"}, ["🪥", "😁", "🍎", "✨"], ["", "EN SERT DOKU!", "AĞZININ İÇİNE!"], fx="sparkle")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Bir diş neyden yapılır?", "Hangi diş ne iş yapar?", "Çürük nasıl başlar?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "comparison", "title": "İki diş takımı", "left": {"title": "Süt dişleri 🍼", "items": ["20 diş", "Doğumdan önce gelişir", "Yaklaşık 6 yaşında düşmeye başlar"]}, "right": {"title": "Kalıcı dişler 🦷", "items": ["32 diş"]}}, ["🦷", "🔩"], ["20 SÜT DİŞİ", "32 KALICI DİŞ", "VİDALARIM SAĞLAM 🔩"])
S(1, {"type": "spotlight", "title": "Dört doku", "emoji": "🦷", "chips": [{"label": "Mine", "emoji": "💎"}, {"label": "Dentin", "emoji": "🟡"}, {"label": "Öz (pulpa)", "emoji": "❤️"}, {"label": "Sement", "emoji": "🧱"}]}, ["🔬", "✨"], ["DÖRT DOKU"])
S(3, {"type": "stages", "title": "Dışarıdan içeriye bir diş", "rows": [{"label": "Mine: en sert doku", "emoji": "💎"}, {"label": "Dentin: kemik kadar sert", "emoji": "🟡"}, {"label": "Öz: sinirler ve damarlar", "emoji": "❤️"}], "path": [0, 0, 0, 1, 1, 1, 2, 2, 2], "highlightRow": 0, "note": NOTE}, [], ["MİNE 💎", "DENTİN", "ÖZ: SİNİRLER ❤️"])
S(1, {"type": "spotlight", "title": "Sement", "emoji": "🧱", "chips": [{"label": "Kökün dışını örter", "emoji": "🌱"}, {"label": "Diş etinin altında", "emoji": "🩷"}, {"label": "Dişi çene kemiğinde tutar", "emoji": "⚓"}]}, ["🦷", "🦴"], ["SEMENT ⚓"])
S(3, {"type": "diagram", "title": "Hangi diş ne iş yapar?", "layout": "flow", "nodes": [{"label": "Kesici: keser", "emoji": "✂️"}, {"label": "Köpek dişi: sivri", "emoji": "🔺"}, {"label": "Küçük azı: öğütür", "emoji": "⚙️"}, {"label": "Azı: güçlü çiğner", "emoji": "🪨"}]}, ["🍎", "🥕"], ["KESİCİ ✂️", "KÖPEK DİŞİ", "AZI DİŞİ ⚙️"])
S(1, {"type": "big-number", "value": "Mutfak robotu", "label": "Ağzında makas, öğütücü ve değirmen", "sub": "Keser, yırtar, öğütür", "icon": "🤖"}, ["✂️", "⚙️"], ["MUTFAK ROBOTU 😄"])
S(3, {"type": "comparison", "title": "Kalıcı azıların takvimi", "left": {"title": "6 yaş dişleri", "items": ["5–7 yaş arası"]}, "right": {"title": "12 yaş dişleri", "items": ["11–14 yaş arası", "Sonra: yirmi yaş dişleri"]}}, ["🗓️", "🦷"], ["6 YAŞ DİŞLERİ", "12 YAŞ DİŞLERİ", "KONUŞMAK İÇİN DE 🗣️"], extra=[3])
S(2, {"type": "spotlight", "title": "Ağızdaki misafirler", "emoji": "🦠", "chips": [{"label": "Yüzlerce bakteri türü", "emoji": "🦠"}, {"label": "Plak: yapışkan, renksiz tabaka", "emoji": "🫧"}]}, ["🔬", "🦷"], ["BAKTERİLER 🦠", "PLAK"])
S(2, {"type": "diagram", "title": "Çürük nasıl başlar?", "layout": "flow", "nodes": [{"label": "Şeker", "emoji": "🍬"}, {"label": "Bakteriler asit yapar", "emoji": "🦠"}, {"label": "Mine aşınır", "emoji": "💥"}, {"label": "Mineral kaybı", "emoji": "📉"}]}, ["🍭", "⚠️"], ["ŞEKER → ASİT", "MİNERAL KAYBI"], fx="shake")
S(3, {"type": "comparison", "title": "Ağızdaki halat çekme", "left": {"title": "Saldıranlar ⚔️", "items": ["Şeker", "Bakteriler", "Asit"]}, "right": {"title": "Savunanlar 🛡️", "items": ["Tükürükteki mineraller", "Florür", "Mine kendini onarır"]}}, ["🪢", "🦷"], ["HALAT ÇEKME 🪢", "TÜKÜRÜK + FLORÜR", "GERİ DÖNDÜRÜLEBİLİR ✅"])
S(2, {"type": "meter", "title": "Bakteriler kazanırsa", "label": "Hasar", "emoji": "🦷", "phases": [{"label": "Oyuk: kalıcı hasar", "level": 0.85, "emoji": "🕳️"}, {"label": "Dişçi dolguyla onarır", "level": 0.4, "emoji": "🩺"}], "note": NOTE}, ["🦠", "🪢"], ["OYUK 🕳️", "HANGİ TARAFTASIN?"])
S(2, {"type": "bullets", "title": "Kazanma planı", "items": ["Günde iki kez, yaklaşık 2 dakika fırçala", "Florürlü diş macunu", "Günde bir kez diş ipi", "Şekerliyi sınırla, dişçiye düzenli git"]}, ["🪥", "🧵"], ["GÜNDE İKİ KEZ 🪥", "ŞEKERİ SINIRLA 🍭"])
S(1, {"type": "diagram", "title": "Sen de dene: şarkılı fırçalama", "layout": "flow", "nodes": [{"label": "İki dakikalık şarkı seç", "emoji": "🎵"}, {"label": "Şarkı bitene kadar fırçala", "emoji": "🪥"}, {"label": "Aynada azılara bak", "emoji": "🪞"}]}, ["⏱️", "😁"], ["DENEY ZAMANI 🔬"])
S(2, {"type": "spotlight", "title": "Bunu biliyor muydun?", "emoji": "🛡️", "chips": [{"label": "Çürüklerin çoğu azı dişlerinde", "emoji": "🦷"}, {"label": "İnce plastik koruyucu kaplama", "emoji": "✨"}, {"label": "Uykuda tükürük azalır", "emoji": "😴"}, {"label": "Yatmadan önce fırçala!", "emoji": "🪥"}]}, ["🌙", "🦷"], ["AZI DİŞLERİ", "YATMADAN FIRÇALA 🌙"])
S(2, {"type": "hook", "question": "Vücudun en sert dokusu hangisi?", "emoji": "🤔"}, ["💎", "🦷"], ["HIZLI SORU!", "DİŞ MİNESİ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 17, "videoTitle": "Dişlerimiz nasıl çalışır?", "paperTitleTr": "Dişlerimiz nasıl çalışır?",
  "theme": {"backdrop": "mouth", "actors": [{"kind": "chase", "emoji": "🪥", "emoji2": "🦠", "every": 16, "size": 110}, {"kind": "swarm", "emoji": "🫧", "size": 70}]},
  "takeaways": ["Diş; mine, dentin, öz ve sementten oluşur", "Kesici keser, köpek dişi yırtar, azılar öğütür", "Şeker ve bakteriler asit yapar; fırçalama ve florür korur"],
  "description": "Ağzındaki alet takımı nasıl çalışır? Bu bölümde süt dişlerini ve kalıcı dişleri; minenin vücudun en sert dokusu olduğunu, dentini, özü ve sementi; kesici, köpek ve azı dişlerinin görevlerini keşfediyoruz. Çürük nasıl başlar, ağızdaki halat çekme yarışını nasıl kazanırız? Sonunda şarkılı fırçalama etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Mine", "meaning": "Dişin en dış katmanı; vücudun en sert dokusu."},
    {"term": "Dentin", "meaning": "Minenin altındaki, kemik kadar sert sarımsı doku."},
    {"term": "Öz (pulpa)", "meaning": "Dişin en iç kısmı; sinirler ve kan damarları burada bulunur."},
    {"term": "Sement", "meaning": "Kökü örten ve dişi çene kemiğinde tutan doku."},
    {"term": "Kron", "meaning": "Dişin diş etinin üstünde görünen kısmı."},
    {"term": "Plak", "meaning": "Dişlerin üstünde biriken, bakterilerden oluşan yapışkan tabaka."},
    {"term": "Florür", "meaning": "Mineyi güçlendiren ve çürüğü önlemeye yardım eden mineral."},
    {"term": "Oyuk (kavite)", "meaning": "Çürüğün dişte açtığı kalıcı delik."}],
  "song": e.song("Gülüşün Kalkanı", [("🦷", "Diş"), ("💎", "Mine"), ("🦠", "Bakteri"), ("🪥", "Fırça"), ("🧵", "Diş ipi")],
    ["En dışta mine, en sert doku", "Altında dentin, kemik kadar sağlam", "İçinde öz, sinirler orada", "Sement tutar kökü çenede"],
    ["Fırçala, fırçala; günde iki kez!", "Florürle mine kendini onarır", "Şeker gelir, bakteri asit yapar", "Halat çekmede sen kazanırsın!"],
    ["Kesici keser, köpek dişi sivri", "Azılar öğütür, çiğner her lokmayı", "Süt dişleri gider, kalıcılar gelir", "Bir ömür boyu seninle kalır"],
    ["Fırçala, fırçala; günde iki kez!", "Florürle mine kendini onarır", "Yatmadan önce unutma sakın", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "chase", "emoji": "🪥", "emoji2": "🦠", "every": 7, "size": 240}, {"kind": "hop", "emoji": "🦷"}, {"kind": "hop", "emoji": "😁"}, {"kind": "hop", "emoji": "🦷"}, {"kind": "swarm", "emoji": "🫧"}])}
e.write(D, facts, script)
