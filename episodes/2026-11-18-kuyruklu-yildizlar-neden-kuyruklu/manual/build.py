"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kuyruklu-yildizlar-neden-kuyruklu"
SP = "NASA Space Place — What Is a Comet?"; NS = "NASA Science — Comets"; HA = "NASA Science — Comet 1P/Halley"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "What Is a Comet?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/comets/en/"},
    {"id": "k2", "title": "Comets", "publisher": "NASA", "url": "https://science.nasa.gov/solar-system/comets/"},
    {"id": "k3", "title": "1P/Halley", "publisher": "NASA", "url": "https://science.nasa.gov/solar-system/comets/1p-halley/"}],
  "facts": [
    F(1, "Kuyruklu yıldızlar Güneş'in çevresinde dolanan, toz ve buzdan yapılmış buzlu cisimlerdir; donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler.", "Comets are icy objects made of dust and ice that orbit the Sun. / Comets are cosmic snowballs of frozen gases, rock, and dust that orbit the Sun.", SP + "; " + NS),
    F(2, "Bu toz ve buz topu, yani çekirdek, genellikle 16 kilometreden küçüktür; aşağı yukarı küçük bir kasaba büyüklüğündedir.", "This ball of dust and ice is usually less than 10 miles (16 kilometers) across – about the size of a small town.", SP, ["16"]),
    F(3, "Kuyruklu yıldız Güneş'e yaklaşınca ısınmaya başlar ve sonunda buz gaza dönüşmeye başlar.", "But when a comet gets close to the Sun, it starts heating up. / Eventually, the ice begins to turn to gas.", SP),
    F(4, "Gaz ve toz, çekirdeğin çevresinde koma denen dev, bulanık bir bulut oluşturur.", "The gas and dust create a huge, fuzzy cloud around the nucleus called the coma.", SP),
    F(5, "Kuyruklu yıldızın Güneş'e yaklaştıkça uzayan iki kuyruğu vardır; biri beyaz görünür ve tozdan yapılmıştır, Güneş'ten uzağa geniş ve hafifçe kıvrılan bir yol çizer; iyon kuyruğu ise her zaman doğrudan Güneş'in tersine bakar.", "A comet has two tails that get longer the closer it gets to the Sun. / One looks white and is made of dust. / This dust tail traces a broad, gently curving path away from the Sun. / The ion tail always points directly away from the Sun.", SP),
    F(6, "Bazı kuyruklu yıldızlar Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda, bazıları Güneş Sistemi'nin dış kenarındaki küre biçimli Oort Bulutu'nda yaşar; Güneş'in çevresinde muhtemelen milyarlarca kuyruklu yıldız dolanır.", "Some exist in a wide disk beyond the orbit of Neptune called the Kuiper Belt. / Other comets live in the Oort Cloud, a huge, sphere-shaped region at the outer edge of the solar system. / There are likely billions of comets orbiting our Sun in the Kuiper Belt and even more distant Oort Cloud.", SP + "; " + NS),
    F(7, "Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için 250.000 yıldan fazla zaman harcar.", "The comet with the longest known orbit takes more than 250,000 years to make just one trip around the Sun!", SP, ["250.000"]),
    F(8, "Halley'in yörünge dönemi ortalama 76 Dünya yılıdır; en son 1986'da Dünya'nın göğünde görüldü ve 2061'de geri dönecek.", "Halley's orbit period is, on average, 76 Earth years. / Halley was last seen in Earth's skies in 1986 / It will return in 2061 on its regular 76-year journey around the Sun.", HA, ["76", "1986", "2061"]),
    F(9, "Halley her dönüşünde çekirdeğinden uzaya buz ve kaya püskürtür; bu döküntü her yıl iki zayıf meteor yağmuruna yol açar: Mayıs'ta Eta Akuaridler, Ekim'de Orionidler.", "Each time Halley returns to the inner solar system its nucleus sprays ice and rock into space. / This debris stream results in two weak meteor showers each year: the Eta Aquarids in May and the Orionids in October.", HA),
    F(10, "Rosetta, kuyruklu yıldızın çekirdeğine bir iniş aracı bıraktı ve iki yıl boyunca kuyruklu yıldızın çevresinde dolandı.", "Rosetta dropped a lander on the nucleus, then orbited the comet for two years.", SP),
    F(11, "NASA'nın Stardust görevi Wild 2 kuyruklu yıldızından örnek topladı; bu parçacıkların, yaşamın yapı taşı sayılan hidrokarbonlarca zengin olduğu bulundu.", "NASA’s Stardust mission collected samples from Comet Wild 2 / Scientists found those particles to be rich in hydrocarbons, which are chemicals we consider the “building blocks” of life.", SP),
]}
e = Ep(); L = e.L
e.sec("hook", [
    L("Gökyüzünde parlak bir baş ve arkasında upuzun bir kuyruk... Ama adında yıldız geçse de kuyruklu yıldız aslında bir yıldız değil!", [1]),
    L("Peki o zaman ne? Ve o kuyruk nereden çıkıyor?"),
    L("Bugün Güneş Sistemi'nin buzlu gezginlerinin peşine düşüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Kuyruklu yıldız neden yapılır? Kuyruğu nasıl oluşur? Ve nereden gelir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre kuyruklu yıldızlar, Güneş'in çevresinde dolanan, toz ve buzdan yapılmış cisimlerdir. Donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler.", [1], "Nasa'ya göre kuyruklu yıldızlar, Güneş'in çevresinde dolanan, toz ve buzdan yapılmış cisimlerdir. Donmuş gazlardan, kayadan ve tozdan oluşan kozmik kartopları gibidirler."),
    L("Kuyruklu yıldızın merkezine çekirdek denir. Çekirdek genellikle 16 kilometreden küçüktür, yani küçük bir kasaba büyüklüğünde.", [2], "Kuyruklu yıldızın merkezine çekirdek denir. Çekirdek genellikle on altı kilometreden küçüktür, yani küçük bir kasaba büyüklüğünde."),
    L("Bir kasaba büyüklüğünde kartopu! Ben olsam onunla kartopu savaşı yapmazdım.", [2]),
])
e.sec("finding", [
    L("Güneş'ten uzaktayken kuyruklu yıldız donmuş ve sessizdir. Ama Güneş'e yaklaşınca ısınmaya başlar.", [3]),
    L("Isındıkça buzu gaza dönüşmeye başlar. Gaz ve toz, çekirdeğin çevresinde koma denen dev, bulanık bir bulut oluşturur.", [3, 4]),
    L("İşte şimdi kuyruklar ortaya çıkar! Kuyruklu yıldızın iki kuyruğu vardır ve Güneş'e yaklaştıkça uzarlar.", [5]),
    L("Birincisi toz kuyruğudur. Beyaz görünür ve Güneş'ten uzağa doğru geniş, hafifçe kıvrılan bir yol çizer.", [5]),
    L("İkincisi iyon kuyruğudur. İyon kuyruğu her zaman doğrudan Güneş'in tersine bakar.", [5]),
    L("Yani kuyruk, kuyruklu yıldızın arkasında değil, Güneş'in tersinde durur. Benim cin kuyruğum ise hep arkamda, ona güvenebilirim!"),
])
e.sec("importance", [
    L("Peki kuyruklu yıldızlar nereden gelir? NASA'ya göre bazıları Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda yaşar.", [6], "Peki kuyruklu yıldızlar nereden gelir? Nasa'ya göre bazıları Neptün'ün yörüngesinin ötesindeki Kuiper Kuşağı'nda yaşar."),
    L("Bazıları ise Güneş Sistemi'nin dış kenarındaki küre biçimli Oort Bulutu'nda. Güneş'in çevresinde muhtemelen milyarlarca kuyruklu yıldız dolanıyor!", [6]),
    L("Bazılarının yolculuğu çok uzun sürer. Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için 250.000 yıldan fazla zaman harcar!", [7], "Bazılarının yolculuğu çok uzun sürer. Bilinen en uzun yörüngeli kuyruklu yıldız, Güneş'in çevresinde bir tur için iki yüz elli bin yıldan fazla zaman harcar!"),
    L("En ünlüsü Halley Kuyruklu Yıldızı'dır. Ortalama 76 yılda bir döner. En son 1986'da görüldü ve 2061'de geri gelecek.", [8], "En ünlüsü Halley Kuyruklu Yıldızı'dır. Ortalama yetmiş altı yılda bir döner. En son bin dokuz yüz seksen altıda görüldü ve iki bin altmış birde geri gelecek."),
    L("O zaman ben de burada olacağım. Robotlar yaşlanmaz, sadece güncellenir!"),
    L("Halley her dönüşünde uzaya buz ve kaya püskürtür. Bu döküntü her yıl iki meteor yağmuruna yol açar: Mayıs'ta Eta Akuaridler, Ekim'de Orionidler.", [9]),
    L("Bilim insanları kuyruklu yıldızları yakından da inceledi. Rosetta aracı bir kuyruklu yıldızın çekirdeğine iniş aracı bıraktı ve iki yıl onun çevresinde dolandı.", [10]),
    L("Şimdi sıra sende! Ekim'de Orionid meteor yağmuru zamanı, bir yetişkinle şehir ışıklarından uzak, karanlık bir yere git.", [9]),
    L("Sırt üstü uzan, gözlerin karanlığa alışsın ve gökyüzünü izle. Gördüğün her kayan ışığı say! Gündüz asla Güneş'e doğrudan bakma.", [9]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? NASA'nın Stardust görevi bir kuyruklu yıldızdan örnek topladı. Bu parçacıklar, yaşamın yapı taşı sayılan hidrokarbonlarca zengin çıktı!", [11], "Bunu biliyor muydun? Nasa'nın Stardust görevi bir kuyruklu yıldızdan örnek topladı. Bu parçacıklar, yaşamın yapı taşı sayılan hidrokarbonlarca zengin çıktı!"),
    L("Hızlı soru! İyon kuyruğu her zaman hangi yöne bakar?", [5]),
    L("Düşün bakalım... Evet: Güneş'in tam tersine!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Gökyüzüne bakmayı da!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kuyruklu yıldızlar neden kuyruklu?", "emoji": "☄️"}, ["✨", "🌌"], ["YILDIZ DEĞİL!", "KUYRUK NEREDEN?", "BUZLU GEZGİNLER"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kuyruklu yıldız neden yapılır?", "Kuyruğu nasıl oluşur?", "Nereden gelir?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Kozmik kartopu", "emoji": "☄️", "chips": [{"label": "Toz ve buz", "emoji": "🧊"}, {"label": "Kaya ve donmuş gaz", "emoji": "🪨"}, {"label": "Çekirdek: 16 km'den küçük", "emoji": "🏘️"}]}, ["🧊", "⛄"], ["KOZMİK KARTOPU", "ÇEKİRDEK", "KARTOPU SAVAŞI? ⛄"])
S(2, {"type": "meter", "title": "Güneş'e yaklaşınca", "label": "Isı", "emoji": "☀️", "phases": [{"label": "Isınmaya başlar", "level": 0.5, "emoji": "🌡️"}, {"label": "Buz gaza döner, koma oluşur", "level": 0.9, "emoji": "💨"}], "note": NOTE}, ["☀️", "💨"], ["ISINIR", "KOMA"])
S(3, {"type": "comparison", "title": "İki kuyruk", "left": {"title": "Toz kuyruğu 🤍", "items": ["Beyaz görünür", "Geniş, kıvrılan yol"]}, "right": {"title": "İyon kuyruğu 💙", "items": ["Her zaman Güneş'in tersine", "Güneş'e yaklaştıkça uzar"]}}, ["☄️", "☀️"], ["İKİ KUYRUK", "TOZ KUYRUĞU", "İYON KUYRUĞU"], fx="sparkle")
S(1, {"type": "big-number", "value": "Güneş'in tersine", "label": "Kuyruk arkada değil, Güneş'in tersinde durur", "sub": "NASA", "icon": "🧭"}, ["🧞", "☀️"], ["CİN KUYRUĞU 🧞"])
S(2, {"type": "stages", "title": "Kuyruklu yıldızların evi", "rows": [{"label": "Güneş", "emoji": "☀️"}, {"label": "Neptün", "emoji": "🔵"}, {"label": "Kuiper Kuşağı", "emoji": "🪐"}, {"label": "Oort Bulutu", "emoji": "🌫️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim; ölçekli değildir."}, [], ["KUİPER KUŞAĞI", "OORT BULUTU"])
S(1, {"type": "big-number", "value": "250.000 yıl", "label": "En uzun yörüngeli kuyruklu yıldızın bir turu (en az)", "sub": "NASA", "icon": "⏳"}, ["⏳", "🌌"], ["UZUN YOLCULUK"])
S(2, {"type": "comparison", "title": "Halley Kuyruklu Yıldızı", "left": {"title": "Geçmiş 👀", "items": ["1986: son görülme"]}, "right": {"title": "Gelecek 🎉", "items": ["2061: dönüş", "Ortalama 76 yılda bir"]}}, ["🔧", "☄️"], ["76 YIL", "GÜNCELLENEN MUMA 🔧"])
S(2, {"type": "diagram", "title": "Halley'in izleri", "layout": "flow", "nodes": [{"label": "Buz ve kaya püskürtür", "emoji": "💥"}, {"label": "Mayıs: Eta Akuaridler", "emoji": "🌠"}, {"label": "Ekim: Orionidler", "emoji": "🌠"}, {"label": "Rosetta: yakından inceleme", "emoji": "🛰️"}]}, ["🌠", "🛰️"], ["METEOR YAĞMURU", "ROSETTA 🛰️"], fx="meteor")
S(2, {"type": "bullets", "title": "Sen de dene: meteor say", "items": ["Ekim'de, bir yetişkinle", "Şehir ışıklarından uzak dur", "Sırt üstü uzan, gökyüzünü izle", "Gündüz Güneş'e asla bakma!"], "tone": "caution"}, ["🌠", "🌙"], ["DENEY ZAMANI 🔬", "GÜNEŞ'E BAKMA ⚠️"])
S(1, {"type": "spotlight", "title": "Stardust", "emoji": "🧪", "chips": [{"label": "Kuyruklu yıldızdan örnek", "emoji": "🛰️"}, {"label": "Hidrokarbonlarca zengin", "emoji": "🧬"}]}, ["🧪", "🛰️"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "İyon kuyruğu hangi yöne bakar?", "emoji": "🤔"}, ["☄️", "☀️"], ["HIZLI SORU!", "GÜNEŞ'İN TERSİNE ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 39, "videoTitle": "Kuyruklu yıldızlar neden kuyruklu?", "paperTitleTr": "Kuyruklu yıldızlar neden kuyruklu?",
  "theme": {"backdrop": "space", "actors": [{"kind": "fly", "emoji": "🛰️", "every": 34}]},
  "takeaways": ["Kuyruklu yıldızlar toz, kaya ve donmuş gazdan oluşan kozmik kartoplarıdır", "Güneş'e yaklaşınca buz gaza döner; koma ve Güneş'in tersine bakan iki kuyruk oluşur", "Kuiper Kuşağı ve Oort Bulutu'ndan gelirler; Halley 2061'de dönecek"],
  "description": "Kuyruklu yıldızlar neden yapılır, kuyrukları nasıl oluşur? Bu bölümde çekirdeği, komayı, toz ve iyon kuyruklarını, Kuiper Kuşağı ile Oort Bulutu'nu, Halley Kuyruklu Yıldızı'nı ve bıraktığı meteor yağmurlarını, Rosetta ve Stardust görevlerini keşfediyoruz. Sonunda güvenli bir meteor gözlemi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Çekirdek", "meaning": "Kuyruklu yıldızın toz ve buzdan oluşan katı merkezi."},
    {"term": "Koma", "meaning": "Çekirdeğin çevresinde gaz ve tozdan oluşan bulanık bulut."},
    {"term": "İyon kuyruğu", "meaning": "Her zaman Güneş'in tam tersine bakan gaz kuyruğu."},
    {"term": "Kuiper Kuşağı", "meaning": "Neptün'ün ötesinde, buzlu cisimlerin bulunduğu geniş disk."},
    {"term": "Oort Bulutu", "meaning": "Güneş Sistemi'nin dış kenarındaki küre biçimli buzlu cisimler bölgesi."},
    {"term": "Meteor yağmuru", "meaning": "Dünya bir kuyruklu yıldızın döküntüsünden geçerken gökte görülen kayan ışıklar."},
    {"term": "Yörünge", "meaning": "Bir cismin başka bir cismin çevresinde izlediği yol."}],
  "song": e.song("Buzlu Gezgin", [("☄️", "Kuyruklu yıldız"), ("🧊", "Buz"), ("☀️", "Güneş"), ("🌠", "Meteor"), ("🛰️", "Rosetta")],
    ["Uzaklarda donmuş bir kartopu", "Kuiper'den, Oort'tan yola çıkar", "Güneş'e yaklaşır, ısınır", "Buzu gaza döner, koma açılır"],
    ["Parla, buzlu gezgin, parla!", "İki kuyruk süzülür ardında", "Toz kuyruğu kıvrılır beyaz", "İyon kuyruğu Güneş'in tersinde"],
    ["Halley döner yıllar sonra", "Döküntüsü meteor olur", "Mayıs'ta, Ekim'de kayar gökten", "Rosetta indi, yakından baktı"],
    ["Parla, buzlu gezgin, parla!", "İki kuyruk süzülür ardında", "Karanlıkta uzan, meteor say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "☄️"}, {"kind": "orbit", "emoji": "🛰️"}, {"kind": "hop", "emoji": "🌠"}, {"kind": "hop", "emoji": "🧊"}])}
e.write(D, facts, script)
