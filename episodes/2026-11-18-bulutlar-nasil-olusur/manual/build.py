"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:bulutlar-nasil-olusur"
NG = "National Geographic Education — Cloud"; MO = "Met Office — Clouds"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Cloud", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/cloud/"},
    {"id": "k2", "title": "Clouds", "publisher": "Met Office", "url": "https://weather.metoffice.gov.uk/learn-about/weather/types-of-weather/clouds"}],
  "facts": [
    F(1, "Bulutlar, atmosferde toplanmış görünür minik su damlacıkları ya da buz kristalleridir.", "Clouds are visible accumulations of tiny water droplets or ice crystals in Earth’s atmosphere.", NG),
    F(2, "Su buharı görünmezdir ve havada her zaman çevremizdedir.", "Water vapour is invisible, and it is around us all the time in the air.", MO),
    F(3, "Bulutlar hava su buharıyla doygun hale gelince, yani havanın tutabileceğinden fazla su buharı olunca oluşur.", "Clouds form when air becomes saturated, or filled, with water vapor. / Clouds appear when there is too much water vapour for the air to hold.", NG + "; " + MO),
    F(4, "Hava yükselince soğur; sıcak hava soğuk havadan daha çok su buharı tutabilir, bu yüzden hava kütlesinin sıcaklığını düşürmek bir süngeri sıkmaya benzer.", "As a simple explanation, when air rises, it cools / Warm air can hold more water vapor than cold air, so lowering the temperature of an air mass is like squeezing a sponge.", MO + "; " + NG),
    F(5, "Su buharı yoğuşarak minik su damlacıklarına dönüşür ve bunlar küçük toz parçacıklarına tutunur; yoğuşma çekirdekleri, su buharının çevresinde yoğuştuğu mikroskobik kil, tuz ya da kirletici parçacıklarıdır.", "The water vapour (gas) then condenses to form tiny water droplets (liquid), / it forms lots of tiny little water droplets which cling to little bits of dust / microscopic bits of clay, salt, or solid pollutant around which water vapor condenses in clouds to form raindrops.", MO + "; " + NG),
    F(6, "Bu su damlacıklarının çapı yalnızca milimetrenin yüzde biri kadardır; o kadar küçüktürler ki havada asılı kalırlar.", "These droplets of water are only about a hundredth of a millimetre in diameter / These droplets are so small that they stay suspended in the air.", MO),
    F(7, "Bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus; stratus bulutları yatay ve katmanlıdır; kümülüs bulutları büyük ve topaklıdır ve 12.000 metre yüksekliğe kadar uzanabilir.", "This splits clouds into three main types - stratus, cumulus and cirrus. / Stratus clouds are horizontal and stratified, or layered. / Cumulus clouds are large and lumpy. / They can stretch vertically into the atmosphere up to 12,000 meters (39,000 feet) high.", MO + "; " + NG, ["12.000"]),
    F(8, "Kümülonimbus bulutlarına fırtına bulutu da denir; yağmur, gök gürültüsü ve şimşek üretirler.", "Cumulonimbus clouds are also called thunderheads. / Thunderheads produce rain, thunder, and lightning.", NG),
    F(9, "Bulutlar genellikle beyaz görünür çünkü içlerindeki minik su damlacıkları sıkı sıkıya dizilidir; yağmur yaklaşınca bulutlar kararır çünkü su buharı yağmur damlalarına dönüşerek topaklanır.", "Clouds usually appear white because the tiny water droplets inside them are tightly packed, / When it’s about to rain, clouds darken because the water vapor is clumping together into raindrops,", NG),
    F(10, "Bulutu oluşturan su ya da buz parçacıkları büyüyerek yağış olarak yere düşen daha büyük parçacıklara dönüşebilir.", "the water or ice particles that make up the cloud can grow into bigger particles that fall to Earth as precipitation.", NG),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"; MOs = "Met Ofis"
e.sec("hook", [
    L("Gökyüzüne bak: pamuk gibi bulutlar süzülüyor. Ama bir bulutun içi aslında su doludur. Peki nasıl düşmüyor?", [1, 6]),
    L("Ve o bulutlar nereden çıkıp geliyor?"),
    L("Bugün bir su damlacığıyla birlikte gökyüzüne yükseliyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Bulut neyden yapılır? Nasıl oluşur? Ve neden bazen beyaz, bazen karanlıktır?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre bulutlar, havada toplanmış minik su damlacıkları ya da buz kristalleridir.", [1], f"{NGs}'e göre bulutlar, havada toplanmış minik su damlacıkları ya da buz kristalleridir."),
    L("Her şey su buharıyla başlar. İngiltere'nin meteoroloji kurumu Met Office'e göre su buharı görünmezdir ve havada her zaman çevremizdedir.", [2], f"Her şey su buharıyla başlar. İngiltere'nin meteoroloji kurumu {MOs}'e göre su buharı görünmezdir ve havada her zaman çevremizdedir."),
    L("Ama hava ancak belli bir miktar su buharı tutabilir. Fazlası olunca, hava doygun hale gelir ve bulut oluşur.", [3]),
    L("Ben de doygunum. Ama sudan değil, bilgiden! Bir de biraz şarjdan.", []),
    L("Peki hava nasıl doygun hale gelir? Hava yükselince soğur.", [4]),
    L("Sıcak hava, soğuk havadan daha çok su buharı tutabilir. Hava soğuyunca sanki bir sünger sıkılmış gibi olur.", [4]),
])
e.sec("finding", [
    L("Sıkılan süngerden ne çıkar? Su! Su buharı yoğuşur, yani gazdan sıvıya döner ve minik su damlacıkları oluşur.", [5]),
    L("Bu damlacıklar havadaki minicik toz parçacıklarına tutunur. Bu parçacıklara yoğuşma çekirdeği denir: kil, tuz ya da kirletici zerreleri.", [5]),
    L("Bu damlacıklar çok ama çok küçüktür: çapları milimetrenin yüzde biri kadar.", [6]),
    L("O kadar küçüktürler ki havada asılı kalırlar. İşte bu yüzden bulut düşmez.", [6]),
    L("Ben de hafif olsam uçardım. Ama cin kuyruğum sayesinde zaten uçuyorum!"),
])
e.sec("importance", [
    L("Met Office'e göre bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus.", [7], f"{MOs}'e göre bulutlar üç ana türe ayrılır: stratus, kümülüs ve sirrus."),
    L("Stratus bulutları yatay ve katmanlıdır; gökyüzünü battaniye gibi örter.", [7]),
    L("Kümülüs bulutları büyük ve topaklıdır. National Geographic'e göre 12.000 metre yüksekliğe kadar uzanabilirler!", [7], f"Kümülüs bulutları büyük ve topaklıdır. {NGs}'e göre on iki bin metre yüksekliğe kadar uzanabilirler!"),
    L("Kümülonimbus bulutlarına fırtına bulutu da denir. Bunlar yağmur, gök gürültüsü ve şimşek üretir.", [8]),
    L("Bulutlar genellikle beyaz görünür, çünkü içlerindeki minik damlacıklar sıkı sıkıya dizilmiştir.", [9]),
    L("Yağmur yaklaşınca bulutlar kararır. Çünkü su buharı topaklanarak yağmur damlalarına dönüşmeye başlar.", [9]),
    L("Damlacıklar ya da buz parçacıkları büyür, büyür ve sonunda yağış olarak yere düşer.", [10]),
    L("Şimdi sıra sende! Buzdolabından soğuk bir bardak su al ve masaya koy.", [4]),
    L("Birkaç dakika bekle. Bardağın dışında damlacıklar beliriyor mu? Havadaki görünmez su buharı soğuk bardağa değince yoğuştu!", [2, 4, 5]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Bulut damlacıkları o kadar küçüktür ki havada asılı kalır. Ama birleşip büyüyünce yağmur olarak düşerler.", [6, 10]),
    L("Hızlı soru! Su buharının gazdan sıvıya dönmesine ne denir?", [5]),
    L("Düşün bakalım... Evet: yoğuşma!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bugün gökyüzüne bir bak, hangi bulutu görüyorsun?"),
])
S = e.S
S(3, {"type": "hook", "question": "Bulutlar nasıl oluşur?", "emoji": "☁️"}, ["💧", "🌤️"], ["PAMUK GİBİ", "NEREDEN GELİR?", "YUKARI!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Bulut neyden yapılır?", "Nasıl oluşur?", "Neden beyaz ya da karanlık?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Bulut", "emoji": "☁️", "chips": [{"label": "Minik su damlacıkları", "emoji": "💧"}, {"label": "ya da buz kristalleri", "emoji": "❄️"}, {"label": "Görünmez su buharı", "emoji": "👻"}]}, ["💧", "❄️"], ["DAMLACIK", "SU BUHARI", "DOYGUN HAVA"])
S(3, {"type": "meter", "title": "Hava ne kadar su tutar?", "label": "Su buharı", "emoji": "💧", "phases": [{"label": "Havada görünmez su buharı", "level": 0.45, "emoji": "👻"}, {"label": "Hava yükselir, soğur", "level": 0.8, "emoji": "⬆️"}, {"label": "Sünger sıkılır: doygun!", "level": 1.0, "emoji": "🧽"}], "note": NOTE}, ["🧽", "🌡️"], ["DOYGUNUM 😄", "YÜKSELİR VE SOĞUR", "SÜNGER"])
S(3, {"type": "stages", "title": "Bulutun doğuşu", "rows": [{"label": "Su buharı yoğuşur", "emoji": "💨"}, {"label": "Toz zerresine tutunur", "emoji": "🟤"}, {"label": "Minik damlacık", "emoji": "💧"}, {"label": "Havada asılı kalır", "emoji": "☁️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": "Şematik çizim."}, [], ["YOĞUŞMA", "YOĞUŞMA ÇEKİRDEĞİ", "MİNİCİK!"])
S(2, {"type": "big-number", "value": "Milimetrenin yüzde biri", "label": "Bir bulut damlacığının çapı", "sub": "Met Office", "icon": "💧"}, ["🔬", "🧞"], ["ASILI KALIR", "UÇAN MUMA 🧞"])
S(3, {"type": "comparison", "title": "Bulut türleri", "left": {"title": "Stratus 🌫️", "items": ["Yatay ve katmanlı", "Battaniye gibi örter"]}, "right": {"title": "Kümülüs ☁️", "items": ["Büyük ve topaklı", "12.000 metreye kadar"]}}, ["🌫️", "☁️"], ["ÜÇ TÜR", "STRATUS", "KÜMÜLÜS"])
S(1, {"type": "spotlight", "title": "Kümülonimbus", "emoji": "⛈️", "chips": [{"label": "Fırtına bulutu", "emoji": "🌩️"}, {"label": "Yağmur, gök gürültüsü, şimşek", "emoji": "⚡"}]}, ["⚡", "🌧️"], ["FIRTINA BULUTU ⛈️"], fx="flash")
S(3, {"type": "diagram", "title": "Beyazdan yağmura", "layout": "flow", "nodes": [{"label": "Sıkı dizilmiş damlacık: beyaz", "emoji": "☁️"}, {"label": "Topaklanır: kararır", "emoji": "🌥️"}, {"label": "Büyür ve düşer: yağış", "emoji": "🌧️"}]}, ["🌧️", "☂️"], ["BEYAZ", "KARARIR", "YAĞIŞ"], fx="rain")
S(2, {"type": "bullets", "title": "Sen de dene: soğuk bardak", "items": ["Buzdolabından soğuk bir bardak al", "Masaya koy, birkaç dakika bekle", "Dışında damlacık var mı?", "Yoğuşmayı gördün!"]}, ["🥛", "💧"], ["DENEY ZAMANI 🔬", "YOĞUŞMA!"])
S(1, {"type": "big-number", "value": "Asılı", "label": "Bulut damlacıkları büyüyene kadar havada kalır", "sub": "Met Office · National Geographic", "icon": "☁️"}, ["🌧️", "☁️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Gazdan sıvıya dönmeye ne denir?", "emoji": "🤔"}, ["💨", "💧"], ["HIZLI SORU!", "YOĞUŞMA ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 35, "videoTitle": "Bulutlar nasıl oluşur?", "paperTitleTr": "Bulutlar nasıl oluşur?",
  "theme": {"backdrop": "sky", "actors": [{"kind": "fly", "emoji": "🐦", "every": 30}]},
  "takeaways": ["Bulutlar minik su damlacıkları ya da buz kristallerinden oluşur", "Yükselen hava soğur, su buharı toz zerrelerine tutunarak yoğuşur", "Damlacıklar büyüyünce yağış olarak düşer"],
  "description": "Bulutlar neden düşmez, nasıl oluşur? Bu bölümde görünmez su buharını, yükselen ve soğuyan havayı, yoğuşmayı ve yoğuşma çekirdeklerini, stratus, kümülüs, sirrus ve kümülonimbus bulutlarını, bulutların neden beyaz ya da karanlık göründüğünü keşfediyoruz. Sonunda soğuk bardak deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Su buharı", "meaning": "Suyun gaz hali; görünmezdir."},
    {"term": "Doygun hava", "meaning": "Tutabileceği kadar su buharı taşıyan hava."},
    {"term": "Yoğuşma", "meaning": "Su buharının soğuyarak sıvı damlacıklara dönüşmesi."},
    {"term": "Yoğuşma çekirdeği", "meaning": "Su buharının çevresinde yoğuştuğu minik toz, tuz ya da kil zerresi."},
    {"term": "Kümülüs", "meaning": "Büyük, topaklı, pamuk gibi bulut."},
    {"term": "Stratus", "meaning": "Gökyüzünü katman halinde örten yatay bulut."},
    {"term": "Yağış", "meaning": "Buluttan yere düşen yağmur, kar ya da dolu."}],
  "song": e.song("Gökyüzü Pamuğu", [("☁️", "Bulut"), ("💧", "Damlacık"), ("🌡️", "Soğuk"), ("🟤", "Toz"), ("🌧️", "Yağmur")],
    ["Görünmez buhar yükselir", "Yükseldikçe soğur hava", "Sünger sıkılır, doyar gökyüzü", "Damlacık doğar bir toz zerresinde"],
    ["Süzül, süzül, bulut süzül!", "Minicik damlalar asılı kalır", "Yoğuşma yapar seni", "Gökyüzünün pamuğu sen"],
    ["Stratus örter battaniye gibi", "Kümülüs kabarır topak topak", "Fırtına bulutu şimşek çakar", "Kararınca yağmur başlar"],
    ["Süzül, süzül, bulut süzül!", "Minicik damlalar asılı kalır", "Soğuk bardağa bak, damlaları gör", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "☁️"}, {"kind": "hop", "emoji": "💧"}, {"kind": "fly", "emoji": "🐦"}, {"kind": "hop", "emoji": "🌧️"}])}
e.write(D, facts, script)
