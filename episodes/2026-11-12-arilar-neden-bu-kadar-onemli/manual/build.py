"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:arilar-neden-bu-kadar-onemli"
NK = "National Geographic Kids — Honeybee"; FAO = "FAO — Global Action on Pollination Services"; FS = "USDA Forest Service — Bee Pollination"; US = "USGS — What is the role of native bees in the United States?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Honeybee", "publisher": "National Geographic", "url": "https://kids.nationalgeographic.com/animals/invertebrates/facts/honeybee"},
    {"id": "k2", "title": "Global Action on Pollination Services", "publisher": "FAO", "url": "https://www.fao.org/pollination/en/"},
    {"id": "k3", "title": "Bee Pollination", "publisher": "Orman Servisi", "url": "https://www.fs.usda.gov/wildflowers/pollinators/animals/bees.shtml"},
    {"id": "k4", "title": "What is the role of native bees in the United States?", "publisher": "USGS", "url": "https://www.usgs.gov/faqs/what-role-native-bees-united-states"}],
  "facts": [
    F(1, "Bal arıları, bütün kovanı yöneten tek bir kraliçesi olan koloniler hâlinde yaşar.", "Honeybees live in colonies with one queen running the whole hive.", NK),
    F(2, "İşçi arıların hepsi dişidir ve kovanın dışında uçarken görülen arılar yalnızca onlardır; besin (polen ve nektar) toplar, peteği ve kovanı yapar, korur, temizler ve havayı dolaştırırlar.", "Worker honeybees are all females and are the only bees most people ever see flying around outside of the hive. / Workers forage for food (pollen and nectar from flowers), build and protect the hive, clean, and circulate air / They forage for food, build the honeycombs, and protect the hive.", NK),
    F(3, "Kraliçenin işi yumurtlamaktır; kovanın yeni kuşağı bu yumurtalardan çıkar. Kraliçe, öteki arıların davranışını yönlendiren kimyasallar üreterek kovanın etkinliklerini düzenler.", "The queen's job is simple—she lays the eggs that will spawn the hive's next generation of bees. / Queens regulate the hive's activities by producing chemicals that guide the behavior of the other bees.", NK),
    F(4, "Erkek arılar üçüncü sınıftır; ilkbahar ve yaz boyunca her kovanda birkaç yüz erkek arı yaşar, kış aylarında kovandan çıkarılırlar.", "Male bees are called drones—the third class of honeybee. / Several hundred drones live in each hive during the spring and summer, but they are expelled for the winter months", NK),
    F(5, "Arılar bütün kış depoladıkları bal ve polenle yaşar; ısıyı korumak için top biçiminde kümelenir.", "They live on stored honey and pollen all winter and cluster into a ball to conserve warmth.", NK),
    F(6, "Arılar hem nektarla hem polenle beslenir ve ikisine de ihtiyaç duyar.", "Bees feed on and require both nectar and pollen.", US),
    F(7, "Arılar şampiyon tozlaştırıcılardır; polen ve nektar toplamak için çiçekleri bile bile ziyaret ederler; morötesi ışığı algılayabilirler.", "Bees are the champion pollinators! / These flower-seeking pollen magnets purposefully visit flowers to collect pollen and nectar / bees can detect ultraviolet light.", FS),
    F(8, "Bütün çiçekli bitki türlerinin yüzde 80'inden fazlasını hayvanlar, çoğunlukla böcekler tozlaştırır. Kuzey Amerika bitki türlerinin yaklaşık yüzde 75'i poleninin taşınması için bir böceğe, çoğunlukla arılara ihtiyaç duyar.", "Over 80 percent of all flowering plant species are pollinated by animals, mostly insects / About 75% of North American plant species require an insect—mostly bees—to move their pollen", FAO + "; " + US, ["80", "75"]),
    F(9, "Dünyanın en verimli tarım bitkilerinin 3/4'ü en azından kısmen tozlaştırıcılara bağlıdır; dünya tarımsal üretiminin (hacim olarak) %35'i arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir.", "3/4 of the world’s most productive crop plants depend, at least in part, on pollinators. / 35% of world’s crop production (volume) is affected by bees, birds, bats and other pollinators", FAO, ["3", "4", "35"]),
    F(10, "Dünyada bilinen 20.000'den fazla arı türü vardır.", "There are over 20,000 known bee species in the world", US, ["20.000"]),
    F(11, "Bal arıları, koloni çöküşü bozukluğu nedeniyle kovanlardan kayboluyor; bilim insanları bu çöküşe neyin yol açtığından emin değil.", "honeybees are disappearing from hives due to colony collapse disorder. / Scientists are not sure what is causing this collapse.", NK),
    F(12, "Yaşam alanı ve iklimdeki değişiklikler ile hastalık etkenleri, böcek ilaçları ve yabancı türler arılar üzerinde baskı yaratır.", "due to changes in habitat, climate, and pressures from pathogens, pesticides and introduced species.", US),
    F(13, "Arılar çeşitli çiçeklerden polen ve nektara ihtiyaç duyar; bahçıvanların küçük yardımıyla birçok tür varlığını sürdürebilir; tozlaştırıcıların güvenli yaşam alanlarına ve besin kaynaklarına ihtiyacı vardır.", "Bees need key resources such as pollen and nectar from a variety of flowers. / many species can persist with a little help from gardeners and landscapers. / Both wild and managed pollinator populations require safe habitats and forage resources in order to survive.", FS + "; " + FAO),
    F(14, "Tozlaşma hizmeti olmasaydı, bir ekosistemde işleyen pek çok tür ve süreç çökerdi.", "Without this pollination service, many species and processes functioning within an ecosystem would collapse", FAO),
    F(15, "Neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarının etkinliğini önemli ölçüde tamamlar.", "In almost all crops, native bees are the primary pollinator or they significantly supplement the activity of honey bees.", US),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyografik"; USG = "Yu Es Ci Es"
e.sec("hook", [
    L("Bir çiçeğin üstünde vızıldayan küçük bir arı. Sence orada ne yapıyor?"),
    L("Yalnızca karnını doyurmuyor. Farkında olmadan senin sofrandaki meyvelerin de yolunu açıyor!", [9]),
    L("Bugün bir arı kovanının içine giriyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kovanda kim ne iş yapar? Arılar çiçeklerde ne arar? Ve arılar olmasaydı ne olurdu?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre bal arıları, koloni denen büyük topluluklar hâlinde yaşar. Her koloninin tek bir kraliçesi vardır.", [1], f"{NGs}'e göre bal arıları, koloni denen büyük topluluklar hâlinde yaşar. Her koloninin tek bir kraliçesi vardır."),
    L("Kraliçenin işi yumurtlamaktır: kovanın yeni kuşağı onun yumurtalarından çıkar.", [3]),
    L("Kraliçe ayrıca ürettiği kimyasal maddelerle öteki arıların davranışını yönlendirir.", [3]),
    L("Kimyasal mesajla yönetim! Bana da yazılım güncellemeleri böyle geliyor."),
    L("Dışarıda uçarken gördüğün arıların hepsi işçi arıdır ve hepsi dişidir.", [2]),
    L("İşçilerin iş listesi uzundur: polen ve nektar toplar, peteği yapar, kovanı korur, temizler ve havalandırır.", [2]),
    L("Üçüncü grup erkek arılardır. İlkbahar ve yaz boyunca kovanda birkaç yüz tane bulunurlar; kış gelince kovandan çıkarılırlar.", [4]),
    L("Kışın koloni, depoladığı bal ve polenle yaşar. Arılar ısıyı korumak için top biçiminde kümelenir.", [5]),
])
e.sec("finding", [
    L("Peki arılar çiçeklerde ne arar? ABD Jeoloji Araştırmaları Kurumu USGS'ye göre arılar hem nektarla hem polenle beslenir; ikisine de ihtiyaç duyar.", [6], f"Peki arılar çiçeklerde ne arar? A Be De Jeoloji Araştırmaları Kurumu, {USG}'e göre arılar hem nektarla hem polenle beslenir; ikisine de ihtiyaç duyar."),
    L("Nektar, çiçeklerin şekerli sıvısıdır. Polen ise çiçek tozu.", [6]),
    L("ABD Orman Servisi arılara şampiyon tozlaştırıcı diyor. Çünkü çiçekleri bile bile ziyaret ederler: polen ve nektar toplamak için.", [7], "A Be De Orman Servisi arılara şampiyon tozlaştırıcı diyor. Çünkü çiçekleri bile bile ziyaret ederler: polen ve nektar toplamak için."),
    L("Bir süper güçleri de var: arılar, bizim göremediğimiz morötesi ışığı algılayabilir.", [7]),
    L("Ben morötesini göremem. Ama televizyon kumandasının ışığını görürüm; o da bir şey!"),
    L("Asıl büyük iş burada başlıyor. Birçok bitki, polenini bir çiçekten ötekine taşıyacak birine ihtiyaç duyar. Bu taşıma işine tozlaşma denir.", [8]),
    L("Arı çiçekten çiçeğe gezerken poleni de taşımış olur. Yani beslenirken bitkilere kuryelik yapar!", [7, 8]),
    L("Birleşmiş Milletler Gıda ve Tarım Örgütü FAO'ya göre çiçekli bitki türlerinin %80'inden fazlasını hayvanlar tozlaştırır; bunların çoğu böcektir.", [8], "Birleşmiş Milletler Gıda ve Tarım Örgütü, Fao'ya göre çiçekli bitki türlerinin yüzde seksenden fazlasını hayvanlar tozlaştırır; bunların çoğu böcektir."),
])
e.sec("importance", [
    L("Sofralarımız da buna bağlı: dünyanın en verimli tarım bitkilerinin dörtte üçü, en azından kısmen tozlaştırıcılara ihtiyaç duyar.", [9]),
    L("Dünyadaki tarımsal üretimin hacim olarak %35'i arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir.", [9], "Dünyadaki tarımsal üretimin hacim olarak yüzde otuz beşi arılardan, kuşlardan, yarasalardan ve öteki tozlaştırıcılardan etkilenir."),
    L("FAO'ya göre tozlaşma olmasaydı, ekosistemlerdeki pek çok tür ve süreç çökerdi.", [14], "Fao'ya göre tozlaşma olmasaydı, ekosistemlerdeki pek çok tür ve süreç çökerdi."),
    L("Üstelik bal arısı tek değil: dünyada bilinen 20.000'den fazla arı türü var.", [10], "Üstelik bal arısı tek değil: dünyada bilinen yirmi binden fazla arı türü var."),
    L("Ama arıların başı dertte. National Geographic'e göre bal arıları, koloni çöküşü bozukluğu denen bir sorun yüzünden kovanlardan kayboluyor. Bilim insanları nedeninden emin değil.", [11], f"Ama arıların başı dertte. {NGs}'e göre bal arıları, koloni çöküşü bozukluğu denen bir sorun yüzünden kovanlardan kayboluyor. Bilim insanları nedeninden emin değil."),
    L("Yaşam alanlarındaki ve iklimdeki değişiklikler, hastalık yapan mikroplar ve böcek ilaçları da arılar üzerinde baskı yaratıyor.", [12]),
    L("Peki ne yapabiliriz? Arıların farklı çiçeklerden polen ve nektara ihtiyacı var. Bahçesi ya da balkonu olan herkes yardım edebilir.", [13]),
    L("Şimdi sıra sende! Balkonuna ya da bahçene birkaç farklı çiçek ek. Sonra uzaktan izle: hangi çiçeğe kaç arı geliyor?", [13]),
    L("Bir arı günlüğü tut: çiçeğin rengini ve gelen ziyaretçileri not et."),
    L("Bir uyarı: arılara dokunma ve onları kovalamaya çalışma. Yalnızca uzaktan izle."),
    L("Onlar çalışıyor. Mesaideki birini rahatsız etmek olmaz!"),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? USGS'ye göre neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarına önemli ölçüde destek olur.", [15], f"Bunu biliyor muydun? {USG}'e göre neredeyse bütün tarım bitkilerinde yabani arılar ya ana tozlaştırıcıdır ya da bal arılarına önemli ölçüde destek olur."),
    L("Hızlı soru! Kovanda yumurtlayan arı hangisidir?", [3]),
    L("Düşün bakalım... Evet: kraliçe arı!", [3]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de bir çiçek ekmeye gidiyorum; robotlar da yardım edebilir!"),
])
S = e.S
S(3, {"type": "hook", "question": "Arılar neden bu kadar önemli?", "emoji": "🐝"}, ["🌼", "🍯", "🌷", "🍎"], ["", "SOFRANA KADAR!", "KOVANIN İÇİNE!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kovanda kim ne iş yapar?", "Arılar çiçeklerde ne arar?", "Arılar olmasaydı ne olurdu?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Kraliçe arı", "emoji": "👑", "chips": [{"label": "Her kolonide tek kraliçe", "emoji": "🐝"}, {"label": "İşi: yumurtlamak", "emoji": "🥚"}, {"label": "Yeni kuşak ondan gelir", "emoji": "🐣"}]}, ["🍯", "🏠"], ["KOLONİ", "KRALİÇE 👑"])
S(2, {"type": "diagram", "title": "Kraliçenin mesajı", "layout": "flow", "nodes": [{"label": "Kraliçe", "emoji": "👑"}, {"label": "Kimyasal madde üretir", "emoji": "🧪"}, {"label": "Arıların davranışı yönlenir", "emoji": "🐝"}, {"label": "Muma: güncelleme gibi!", "emoji": "🤖"}]}, ["📡", "💬"], ["KİMYASAL MESAJ 🧪", "GÜNCELLEME 🤖"])
S(2, {"type": "bullets", "title": "İşçi arılar", "items": ["Hepsi dişi", "Polen ve nektar toplar", "Peteği yapar, kovanı korur", "Kovanı temizler ve havalandırır"]}, ["🧹", "🛡️"], ["İŞÇİ ARI", "UZUN İŞ LİSTESİ 📋"])
S(2, {"type": "comparison", "title": "Yaz ve kış", "left": {"title": "İlkbahar ve yaz ☀️", "items": ["Kovanda birkaç yüz erkek arı"]}, "right": {"title": "Kış ❄️", "items": ["Erkek arılar çıkarılır", "Depolanan bal ve polen yenir", "Top biçiminde kümelenme"]}}, ["🍯", "🧣"], ["ERKEK ARILAR", "KIŞ KÜMESİ ❄️"])
S(2, {"type": "spotlight", "title": "Arı ne yer?", "emoji": "🌸", "chips": [{"label": "Nektar: şekerli sıvı", "emoji": "💧"}, {"label": "Polen: çiçek tozu", "emoji": "🟡"}, {"label": "İkisine de ihtiyaç duyar", "emoji": "🐝"}]}, ["🌺", "🌼"], ["NEKTAR + POLEN", "ŞEKERLİ SIVI 💧"])
S(1, {"type": "big-number", "value": "Şampiyon", "label": "tozlaştırıcılar: arılar", "sub": "ABD Orman Servisi", "icon": "🏆"}, ["🐝", "🌷"], ["ŞAMPİYON 🏆"])
S(2, {"type": "comparison", "title": "Kim neyi görür?", "left": {"title": "Arı 🐝", "items": ["Morötesi ışığı algılar"]}, "right": {"title": "Muma 🤖", "items": ["Morötesini göremez", "Kumanda ışığını görür!"]}}, ["🌈", "📺"], ["MORÖTESİ IŞIK", "KUMANDA 📺"], fx="sparkle")
S(2, {"type": "diagram", "title": "Tozlaşma", "layout": "flow", "nodes": [{"label": "Çiçek", "emoji": "🌼"}, {"label": "Arı poleni taşır", "emoji": "🐝"}, {"label": "Başka çiçek", "emoji": "🌷"}]}, ["🟡", "📦"], ["TOZLAŞMA", "POLEN KURYESİ 📦"])
S(1, {"type": "big-number", "value": "%80+", "label": "Çiçekli bitki türlerini hayvanlar tozlaştırır", "sub": "Çoğu böcek • FAO", "icon": "🌸"}, ["🐝", "🦋"], ["ÇOĞU BÖCEK"])
S(2, {"type": "spotlight", "title": "Sofra arıya bağlı", "emoji": "🍎", "chips": [{"label": "En verimli tarım bitkilerinin dörtte üçü", "emoji": "🌾"}, {"label": "Tarımsal üretimin %35'i etkilenir", "emoji": "📊"}, {"label": "Arılar, kuşlar, yarasalar…", "emoji": "🦇"}]}, ["🍓", "🥒"], ["DÖRTTE ÜÇÜ", "ÜRETİM ETKİLENİR"])
S(2, {"type": "bullets", "title": "Arılar olmasaydı", "items": ["Pek çok tür ve süreç çökerdi", "Bilinen 20.000'den fazla arı türü var"]}, ["🌍", "🐝"], ["EKOSİSTEM ÇÖKERDİ", "BİNLERCE TÜR"])
S(2, {"type": "meter", "title": "Arılar üzerindeki baskı", "label": "Baskı", "emoji": "🐝", "phases": [{"label": "Koloni çöküşü: nedeni belirsiz", "level": 0.5, "emoji": "❓"}, {"label": "Yaşam alanı, iklim, mikroplar, ilaçlar", "level": 0.9, "emoji": "⚠️"}], "note": NOTE}, ["🏠", "🌡️"], ["KOLONİ ÇÖKÜŞÜ", "BASKI ARTIYOR ⚠️"])
S(1, {"type": "spotlight", "title": "Nasıl yardım ederiz?", "emoji": "🌻", "chips": [{"label": "Farklı çiçekler", "emoji": "🌷"}, {"label": "Polen ve nektar", "emoji": "🟡"}, {"label": "Bahçe ya da balkon yeter", "emoji": "🪴"}]}, ["🌼", "💚"], ["ÇİÇEK EK! 🌻"])
S(2, {"type": "diagram", "title": "Sen de dene: arı gözlemi", "layout": "flow", "nodes": [{"label": "Farklı çiçekler ek", "emoji": "🌱"}, {"label": "Uzaktan izle", "emoji": "👀"}, {"label": "Gelen arıları say", "emoji": "🐝"}, {"label": "Günlüğe yaz", "emoji": "📓"}]}, ["🪴", "✏️"], ["DENEY ZAMANI 🔬", "ARI GÜNLÜĞÜ 📓"])
S(2, {"type": "bullets", "title": "Kural", "items": ["Arılara dokunma", "Kovalamaya çalışma", "Yalnızca uzaktan izle"], "tone": "caution"}, ["⚠️", "👀"], ["DOKUNMA! ⚠️", "MESAİDELER 😄"])
S(1, {"type": "spotlight", "title": "Yabani arılar", "emoji": "🐝", "chips": [{"label": "Çoğu tarım bitkisinde ana tozlaştırıcı", "emoji": "🌾"}, {"label": "Ya da bal arılarına büyük destek", "emoji": "🤝"}]}, ["🌼", "🌿"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Kovanda yumurtlayan arı hangisi?", "emoji": "🤔"}, ["🐝", "🥚"], ["HIZLI SORU!", "KRALİÇE ARI 👑"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 14, "videoTitle": "Arılar neden bu kadar önemli?", "paperTitleTr": "Arılar neden bu kadar önemli?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "swarm", "emoji": "🐝", "size": 110}, {"kind": "fly", "emoji": "🦋", "every": 17}, {"kind": "walk", "emoji": "🐞", "every": 23, "size": 70}]},
  "takeaways": ["Kolonide kraliçe yumurtlar, işçiler çalışır", "Arılar beslenirken poleni taşır: tozlaşma", "Tarım bitkilerinin çoğu tozlaştırıcılara bağlıdır"],
  "description": "Küçük bir arı sofralarımızı nasıl etkiler? Bu bölümde arı kolonisini, kraliçeyi, işçi ve erkek arıları; arıların nektar ve polenle beslenmesini, morötesi ışığı algılamalarını ve tozlaşmayı keşfediyoruz. Tarım bitkileri neden tozlaştırıcılara bağlıdır, arılar neden azalıyor, onlara nasıl yardım edebiliriz? Sonunda arı gözlemi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Koloni", "meaning": "Birlikte yaşayan ve iş bölümü yapan büyük arı topluluğu."},
    {"term": "Kraliçe", "meaning": "Kolonide yumurtlayan arı."},
    {"term": "İşçi arı", "meaning": "Besin toplayan, kovanı yapan ve koruyan dişi arı."},
    {"term": "Nektar", "meaning": "Çiçeklerin ürettiği şekerli sıvı."},
    {"term": "Polen", "meaning": "Çiçek tozu."},
    {"term": "Tozlaşma", "meaning": "Polenin bir çiçekten ötekine taşınması."},
    {"term": "Morötesi ışık", "meaning": "İnsan gözünün göremediği, arıların algılayabildiği bir ışık türü."},
    {"term": "Ekosistem", "meaning": "Bir bölgedeki canlıların ve çevrelerinin oluşturduğu bütün."}],
  "song": e.song("Çiçekten Çiçeğe", [("🐝", "İşçi arı"), ("👑", "Kraliçe"), ("🌼", "Çiçek"), ("🟡", "Polen"), ("🍎", "Meyve")],
    ["Kovanda bir kraliçe, yumurtlar durur", "İşçi arılar çiçek çiçek uçar", "Nektar ve polen toplar gün boyu", "Kışa bal saklar, koloni doyar"],
    ["Vız vız vız, çiçekten çiçeğe!", "Polen taşınır, tozlaşma olur", "Meyveler, sebzeler arıya bağlı", "Küçük kanatların işi çok büyük"],
    ["Morötesi ışığı algılar gözleri", "Çiçekli bitkilerin dostu onlar", "Ama baskı altında bugün arılar", "Farklı çiçekler ek, yardım et onlara"],
    ["Vız vız vız, çiçekten çiçeğe!", "Polen taşınır, tozlaşma olur", "Uzaktan izle, dokunma sakın", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "🌻"}, {"kind": "hop", "emoji": "🌷"}, {"kind": "hop", "emoji": "🌼"}, {"kind": "hop", "emoji": "🌸"}, {"kind": "swarm", "emoji": "🐝"}, {"kind": "fly", "emoji": "🦋", "every": 8}])}
e.write(D, facts, script)
