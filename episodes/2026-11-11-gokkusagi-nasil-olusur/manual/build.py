"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:gokkusagi-nasil-olusur"
NG = "National Geographic Education — Rainbow"
RMS = "Royal Meteorological Society — How Are Rainbows Formed?"
NASA = "NASA Science — Visible Light"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Rainbow", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/rainbow/"},
    {"id": "k2", "title": "How Are Rainbows Formed?", "publisher": "Kraliyet Meteoroloji Derneği", "url": "https://www.rmets.org/metmatters/how-are-rainbows-formed"},
    {"id": "k3", "title": "Visible Light", "publisher": "NASA", "url": "https://science.nasa.gov/ems/09_visiblelight/"}],
  "facts": [
    F(1, "Gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.", "A rainbow is a multicolored arc made by light striking water droplets.", NG),
    F(2, "Gökkuşağı bir optik yanılsamadır; gökyüzünde belirli bir noktada gerçekten bulunmaz.", "A rainbow is an optical illusion—it does not actually exist in a specific spot in the sky.", NG),
    F(3, "Beyaz ışık, gökkuşağının bütün renklerinin karışımını gözümüzün algılama biçimidir.", "White light is how our eyes perceive all the colors of the rainbow mixed together.", NG),
    F(4, "Kırmızı, görünür ışığın en uzun dalga boyuna; mor en kısa dalga boyuna sahiptir. İnsan gözü ışığın yalnızca belirli dalga boylarını algılar.", "Red has the longest wavelength of visible light / Violet has the shortest wavelength / Typically, the human eye can detect wavelengths from 380 to 700 nanometers.", NG + "; " + NASA),
    F(5, "Kırılma, Güneş ışığının havadan daha yoğun bir ortamdan geçerken yön değiştirmesidir.", "Refraction occurs when the light from the sun changes direction when passing through a medium denser than air", RMS),
    F(6, "Güneş ışığının renkleri bir ortamda farklı hızlarda ilerler; her renk dalga boyuna göre biraz farklı açıyla kırılır. Isaac Newton 1665'te prizmanın görünür ışığı büktüğünü gösterdi.", "Sunlight is made of many different wavelengths, or colours, that travel at different speeds when passing through a medium. / Isaac Newton's experiment in 1665 showed that a prism bends visible light / each color refracts at a slightly different angle depending on the wavelength of the color.", RMS + "; " + NASA, ["1665"]),
    F(7, "Damlaya giren ışık kırılır, damlanın arkasından yansır ve çıkarken yeniden kırılır.", "Light entering a water droplet is refracted. It is then reflected by the back of the droplet. / As this reflected light leaves the droplet, it is refracted again, at multiple angles.", NG),
    F(8, "Güneş genellikle gökkuşağını gören kişinin arkasındadır; su damlacıkları gözlemcinin önünde olmalıdır.", "The sun or other source of light is usually behind the person seeing the rainbow. / Water droplets such as rain or fog must be in front of the observer.", NG + "; " + RMS),
    F(9, "Güneş ışığı izleyicinin önündeki damlalara belirli bir açıyla (42 derece) çarpar; birincil gökkuşağının merkezi, Güneş'in tam karşısındaki hayali antisolar noktadır.", "sunlight strikes raindrops in front of a viewer at a precise angle (42 degrees) / the center of a primary rainbow is the antisolar point, the imaginary point exactly opposite the sun.", NG, ["42"]),
    F(10, "Gökkuşakları aslında tam çemberdir; yerdekiler yalnızca ufkun üstündeki damlalardan gelen ışığı görür; uçaktakiler bazen çemberin tamamını görebilir.", "Rainbows are actually full circles. / Viewers in aircraft can sometimes see these circular rainbows. / Viewers on the ground can only see the light reflected by raindrops above the horizon.", NG),
    F(11, "Güneş gökyüzünde ne kadar alçaksa gözlemci yayın o kadar büyük bölümünü görür.", "The lower the sun in the sky, the more of an arc of a rainbow the observer will see", RMS),
    F(12, "Renkler kırmızı, turuncu, sarı, yeşil, mavi, çivit mavisi ve mordur; kırmızı yayın dış kısmında, mor iç kısmında görünür. Birçok bilim insanına göre çivit mavisi maviye ayırt edilemeyecek kadar yakındır.", "red, orange, yellow, green, blue, indigo, and violet / It usually appears on the outer part of a rainbow's arch. / it usually appears on the inner arch of the rainbow. / (Many scientists, however, think \"indigo\" is too close to blue to be truly distinguishable.)", NG),
    F(13, "Gökkuşağının renkleri kenarlarında üst üste biner.", "At their edges, the colors of a rainbow actually overlap.", NG),
    F(14, "Bazen birincil yayın üstünde soluk, ikincil bir gökkuşağı belirir; nedeni ışığın damlada iki kez yansımasıdır; bu yayda kırmızı içte, mor dıştadır.", "a faint, secondary rainbow appears above the primary one. / Double rainbows are caused by light being reflected twice inside the raindrop. / red is on the inner section of the arch, while violet is on the outside.", NG),
    F(15, "Gökkuşağı sis, deniz serpintisi ya da şelale çevresinde de görülebilir; ay gökkuşağı Ay'ın yansıttığı ışıkla oluşur.", "Rainbows can also be viewed around fog, sea spray, or waterfalls. / A moonbow, also called a lunar rainbow, is a rainbow produced by light reflected by the moon.", NG),
    F(16, "Kimse aynı gökkuşağını görmez: her insanın antisolar noktası ve ufku farklıdır.", "no one sees the same rainbow—each person has a different antisolar point, each person has a different horizon. / every rainbow is unique to the observer.", NG + "; " + RMS),
    F(17, "Gökkuşaklarının 'ucu' yoktur, çünkü çemberdirler.", "because no one sees the same rainbow and rainbows don't \"end\" (they're circles)", NG),
]}
e = Ep(); L = e.L
e.sec("hook", [
    L("Yağmur diniyor, Güneş çıkıyor ve gökyüzünde renkli, dev bir yay beliriyor!"),
    L("Peki bu renkler nereden geliyor? Ve gökkuşağı neden hep yay biçiminde?"),
    L("Bugün bir yağmur damlasının içine giriyoruz!"),
])
e.sec("context", [
    L("Gerçi ben damlanın içine giremem. Su ile robot pek iyi anlaşmaz!"),
    L("Üç sorumuz var. Beyaz ışığın içinde ne saklı? Bir damla ışığa ne yapar? Ve gökkuşağı neden yay biçimindedir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır.", [1], "Neşınıl Ciyografik'e göre gökkuşağı, ışığın su damlacıklarına çarpmasıyla oluşan çok renkli bir yaydır."),
    L("İlk sır Güneş ışığında. Bize beyaz görünür; ama beyaz ışık, gökkuşağının bütün renklerinin karışımıdır.", [3]),
    L("NASA'ya göre Isaac Newton bunu 1665'te bir deneyle gösterdi: cam bir prizma ışığı büker ve renklerine ayırır.", [6], "Nasa'ya göre Ayzek Nivtın bunu bin altı yüz altmış beşte bir deneyle gösterdi: cam bir prizma ışığı büker ve renklerine ayırır."),
    L("Her rengin dalga boyu farklıdır. Kırmızının dalga boyu en uzun, morunki en kısadır.", [4]),
    L("Benim en sevdiğim renk mi? Şarj göstergemdeki yeşil!"),
    L("İkinci sır: kırılma. Kraliyet Meteoroloji Derneği'ne göre ışık, havadan daha yoğun bir ortama, örneğin suya girerken yön değiştirir.", [5]),
    L("Renkler suyun içinde farklı hızlarda ilerler. Bu yüzden her renk biraz farklı bir açıyla kırılır ve renkler birbirinden ayrılır.", [6]),
    L("Yani her yağmur damlası minik bir prizma gibi çalışır.", [6, 7]),
])
e.sec("finding", [
    L("Şimdi tek bir damlayı izleyelim. Birinci adım: ışık damlaya girer ve kırılır.", [7]),
    L("İkinci adım: damlanın arka yüzeyinden yansır. Tıpkı bir aynadan döner gibi.", [7]),
    L("Üçüncü adım: damladan çıkarken bir kez daha kırılır. Artık renkler ayrılmıştır.", [7]),
    L("Gökkuşağını görmek için iki koşul gerekir: Güneş arkanda olmalı, su damlacıkları ise önünde.", [8]),
    L("Işık, damlalardan gözüne belirli bir açıyla döner: 42 derece.", [9], "Işık, damlalardan gözüne belirli bir açıyla döner: kırk iki derece."),
    L("Bu açıyı tutturan damlalar bir çemberin üzerinde dizilir. Çemberin merkezi, Güneş'in tam karşısındaki hayali noktadır. Adı: antisolar nokta.", [9, 10]),
    L("Evet, gökkuşağı aslında tam bir çemberdir! Yerdeyken yalnızca ufkun üstündeki kısmını görürüz. Uçaktakiler ise bazen çemberin tamamını görebilir.", [10]),
    L("Güneş ne kadar alçaktaysa yayın o kadar büyük bölümü görünür.", [11]),
    L("Bu yüzden gökkuşağının ucunda hazine arama. Çemberin ucu olmaz! Ben denedim, hâlâ dönüyorum.", [17]),
])
e.sec("importance", [
    L("Renklerin sırası hep aynıdır: kırmızı yayın dışında, mor içindedir. Arada turuncu, sarı, yeşil, mavi ve çivit mavisi yer alır.", [12]),
    L("Ama keskin sınırlar yoktur: renkler kenarlarında üst üste biner. Hatta birçok bilim insanına göre çivit mavisi, maviden ayırt edilemeyecek kadar yakındır.", [12, 13]),
    L("Bazen ilk yayın üstünde daha soluk, ikinci bir yay belirir. Buna çift gökkuşağı denir.", [14]),
    L("Nedeni, ışığın damlanın içinde iki kez yansımasıdır. İkinci yayda renkler ters dizilir: kırmızı içte, mor dıştadır.", [14]),
    L("Gökkuşağı için yağmur şart değil: sis, deniz serpintisi ve şelale çevresinde de görülebilir. Ay ışığıyla oluşanına ay gökkuşağı denir.", [15]),
    L("En şaşırtıcısı şu: gökkuşağı, gökyüzünde belirli bir yerde durmaz. O bir optik yanılsamadır.", [2]),
    L("Bu yüzden kimse aynı gökkuşağını görmez. Herkesin antisolar noktası farklıdır; yanındaki arkadaşın kendi gökkuşağına bakar.", [16]),
    L("Yani gökkuşağı paylaşılmaz. Ama merak etme, herkese bir tane düşüyor!"),
    L("Şimdi sıra sende! Güneşli bir günde sırtını Güneş'e dön ve bahçe hortumuyla önüne ince ince su püskürt.", [8]),
    L("Damlacıkların içinde kendi gökkuşağını ara. Renklerin sırasını kontrol et: kırmızı dışta mı?", [12]),
    L("Bir uyarı: Güneş'e asla doğrudan bakma. Zaten gökkuşağı için ona sırtını dönmen gerekiyor!", [8]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? İnsan gözü, ışığın yalnızca belirli dalga boylarını algılayabilir. Gökkuşağının renkleri, işte o görebildiğimiz ışıktır.", [4]),
    L("Hızlı soru! Gökkuşağını görmek için Güneş nerede olmalı: önünde mi, arkanda mı?", [8]),
    L("Düşün bakalım... Evet: arkanda!", [8]),
    L("Hortumu sen tut ama. Ben ıslanırsam gökkuşağı değil, kıvılcım görürüz!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de gidip bir güzel kurulanayım!"),
])
S = e.S
S(3, {"type": "hook", "question": "Gökkuşağının renkleri nereden gelir?", "emoji": "🌈"}, ["🌧️", "☀️", "💧", "☂️"], ["", "NEDEN YAY?", "DAMLANIN İÇİNE!"])
S(1, {"type": "spotlight", "title": "Su ve robot?", "emoji": "🤖", "chips": [{"label": "Damlaya giremem", "emoji": "💧"}, {"label": "Su + devre = kötü fikir", "emoji": "⚡"}, {"label": "Dışarıdan anlatırım!", "emoji": "📣"}]}, ["☂️", "🔧"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Beyaz ışığın içinde ne saklı?", "Bir damla ışığa ne yapar?", "Gökkuşağı neden yay biçimindedir?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Gökkuşağı nedir?", "emoji": "🌈", "chips": [{"label": "Işık", "emoji": "☀️"}, {"label": "Su damlacıkları", "emoji": "💧"}, {"label": "Çok renkli yay", "emoji": "🎨"}]}, ["🌦️", "✨"], ["IŞIK + DAMLA"])
S(2, {"type": "diagram", "title": "Newton'ın prizma deneyi (1665)", "layout": "flow", "nodes": [{"label": "Beyaz ışık", "emoji": "☀️"}, {"label": "Cam prizma", "emoji": "🔺"}, {"label": "Renkler ayrılır", "emoji": "🌈"}]}, ["💡", "🔬"], ["BEYAZ = BÜTÜN RENKLER", "PRİZMA 🔺"])
S(2, {"type": "comparison", "title": "Dalga boyu", "left": {"title": "Kırmızı 🔴", "items": ["En uzun dalga boyu"]}, "right": {"title": "Mor 🟣", "items": ["En kısa dalga boyu"]}}, ["〰️", "🎨"], ["DALGA BOYU", "FAVORİM: YEŞİL 🔋"])
S(3, {"type": "spotlight", "title": "Kırılma", "emoji": "💧", "chips": [{"label": "Daha yoğun ortam: su", "emoji": "🌊"}, {"label": "Işık yön değiştirir", "emoji": "↪️"}, {"label": "Her renk farklı açıyla kırılır", "emoji": "📐"}, {"label": "Damla = minik prizma", "emoji": "🔺"}]}, ["☀️", "🌧️"], ["KIRILMA", "RENKLER AYRILIR", "MİNİK PRİZMA 🔺"])
S(3, {"type": "diagram", "title": "Bir damlanın içinde", "layout": "flow", "nodes": [{"label": "Girer: kırılır", "emoji": "➡️"}, {"label": "Arkadan yansır", "emoji": "🪞"}, {"label": "Çıkar: yine kırılır", "emoji": "↩️"}, {"label": "Renkler ayrıldı", "emoji": "🌈"}]}, ["💧", "☀️"], ["BİR: KIRILMA", "İKİ: YANSIMA 🪞", "ÜÇ: YİNE KIRILMA"])
S(1, {"type": "comparison", "title": "İki koşul", "left": {"title": "Arkanda ☀️", "items": ["Güneş"]}, "right": {"title": "Önünde 💧", "items": ["Su damlacıkları"]}}, ["🧍", "🌧️"], ["GÜNEŞ ARKADA!"])
S(1, {"type": "big-number", "value": "42°", "label": "Işığın damladan gözüne dönüş açısı", "sub": "National Geographic", "icon": "📐"}, ["👁️", "💧"], ["BELİRLİ BİR AÇI"])
S(2, {"type": "spotlight", "title": "Aslında tam çember!", "emoji": "⭕", "chips": [{"label": "Merkez: antisolar nokta", "emoji": "🎯"}, {"label": "Güneş'in tam karşısı", "emoji": "☀️"}, {"label": "Yerden: ufkun üstü", "emoji": "🌄"}, {"label": "Uçaktan: tam çember", "emoji": "✈️"}]}, ["🌈", "🧭"], ["ANTİSOLAR NOKTA", "TAM ÇEMBER ⭕"])
S(2, {"type": "bullets", "title": "Yay ve çember", "items": ["Güneş alçaksa yayın daha büyük bölümü görünür", "Çemberin ucu olmaz: hazine arama! 🪙"]}, ["🌅", "🪙"], ["GÜNEŞ ALÇAKSA…", "UÇ YOK! 😅"])
S(2, {"type": "spotlight", "title": "Renk sırası", "emoji": "🌈", "chips": [{"label": "Dışta: kırmızı", "emoji": "🔴"}, {"label": "İçte: mor", "emoji": "🟣"}, {"label": "Sınırlar keskin değil", "emoji": "🎨"}, {"label": "Çivit mavisi ≈ mavi?", "emoji": "🔵"}]}, ["🟠", "🟡", "🟢"], ["KIRMIZI DIŞTA", "RENKLER ÜST ÜSTE"])
S(2, {"type": "comparison", "title": "Çift gökkuşağı", "left": {"title": "Birinci yay", "items": ["Tek yansıma", "Kırmızı dışta", "Daha parlak"]}, "right": {"title": "İkinci yay", "items": ["İki yansıma", "Kırmızı içte", "Daha soluk"]}}, ["🌈", "🌈"], ["ÇİFT GÖKKUŞAĞI", "RENKLER TERS! 🔄"])
S(1, {"type": "spotlight", "title": "Yağmur şart değil", "emoji": "💦", "chips": [{"label": "Sis", "emoji": "🌫️"}, {"label": "Deniz serpintisi", "emoji": "🌊"}, {"label": "Şelale", "emoji": "🏞️"}, {"label": "Ay gökkuşağı", "emoji": "🌙"}]}, ["⛲", "✨"], ["AY GÖKKUŞAĞI 🌙"])
S(3, {"type": "bullets", "title": "Kimse aynı gökkuşağını görmez", "items": ["Gökyüzünde belirli bir yerde durmaz", "Herkesin antisolar noktası farklıdır", "Herkese bir tane düşer! 😄"]}, ["👀", "🧑‍🤝‍🧑"], ["OPTİK YANILSAMA", "SENİNKİ SANA ÖZEL", "PAYLAŞILMAZ 😄"])
S(2, {"type": "diagram", "title": "Sen de dene: kendi gökkuşağın", "layout": "flow", "nodes": [{"label": "Sırtını Güneş'e dön", "emoji": "☀️"}, {"label": "Önüne ince su püskürt", "emoji": "🚿"}, {"label": "Damlacıklarda yayı ara", "emoji": "🌈"}, {"label": "Kırmızı dışta mı?", "emoji": "🔎"}]}, ["🌿", "💦"], ["DENEY ZAMANI 🔬", "SIRAYI KONTROL ET"])
S(1, {"type": "bullets", "title": "Güvenlik", "items": ["Güneş'e asla doğrudan bakma!", "Güneş hep arkanda kalsın"], "tone": "caution"}, ["⚠️", "🕶️"], ["GÜNEŞ'E BAKMA! ⚠️"])
S(1, {"type": "spotlight", "title": "Görünür ışık", "emoji": "👁️", "chips": [{"label": "Göz yalnızca belirli dalga boylarını algılar", "emoji": "〰️"}, {"label": "Gökkuşağı: görebildiğimiz ışık", "emoji": "🌈"}]}, ["💡", "✨"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Güneş nerede olmalı: önünde mi, arkanda mı?", "emoji": "☀️"}, ["🌈", "💧"], ["HIZLI SORU!", "ARKANDA ✅", ""])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 4, "videoTitle": "Gökkuşağı nasıl oluşur?", "paperTitleTr": "Gökkuşağı nasıl oluşur?",
  "takeaways": ["Beyaz ışık bütün renklerin karışımıdır", "Damlada kırılma, yansıma ve yine kırılma renkleri ayırır", "Gökkuşağı aslında bir çemberdir; herkes kendininkini görür"],
  "description": "Gökkuşağının renkleri nereden gelir? Bu bölümde beyaz ışığın içindeki renkleri, Newton'ın prizma deneyini, kırılmayı ve yansımayı; bir yağmur damlasının içinde ışığın izlediği yolu keşfediyoruz. Gökkuşağı neden yay biçimindedir, neden aslında tam bir çemberdir, çift gökkuşağında renkler neden ters dizilir? Sonunda bahçe hortumuyla gökkuşağı deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Prizma", "meaning": "Işığı büküp renklerine ayıran, saydam ve köşeli cisim."},
    {"term": "Dalga boyu", "meaning": "Işık dalgasının art arda gelen iki tepesi arasındaki uzaklık; her rengin dalga boyu farklıdır."},
    {"term": "Kırılma", "meaning": "Işığın bir ortamdan başka bir ortama geçerken yön değiştirmesi."},
    {"term": "Yansıma", "meaning": "Işığın bir yüzeye çarpıp geri dönmesi."},
    {"term": "Antisolar nokta", "meaning": "Gözlemciye göre Güneş'in tam karşısında kalan hayali nokta."},
    {"term": "Ufuk", "meaning": "Gökyüzü ile yerin birleşiyormuş gibi göründüğü çizgi."},
    {"term": "Optik yanılsama", "meaning": "Gördüğümüz şeyin, orada gerçekten duran bir nesne olmaması."},
    {"term": "Çivit mavisi", "meaning": "Mavi ile mor arasındaki koyu mavi ton."}],
  "song": e.song("Damladaki Renkler", [("☀️", "Güneş"), ("💧", "Damla"), ("🔺", "Prizma"), ("🌈", "Gökkuşağı"), ("👁️", "Göz")],
    ["Beyaz ışığın içinde renkler saklı", "Damlaya girer ışık, kırılır yolu", "Arkadan yansır, döner geri", "Çıkarken kırılır, ayrılır her biri"],
    ["Kırıl, yansı, kırıl; renkler açılır!", "Kırmızı dışta, mor en içte", "Güneş arkamda, damlalar önümde", "Kırk iki derece, renkler gökte"],
    ["Aslında tam çember, yarısı saklı", "İki kez yansırsa çift olur yayı", "İkinci yayda renkler ters durur", "Herkes kendi yayını görür"],
    ["Kırıl, yansı, kırıl; renkler açılır!", "Kırmızı dışta, mor en içte", "Sırtını Güneş'e dön, renklere bak", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
