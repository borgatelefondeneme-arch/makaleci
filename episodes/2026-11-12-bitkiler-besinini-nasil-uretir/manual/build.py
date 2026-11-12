"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:bitkiler-besinini-nasil-uretir"
S1 = "National Geographic Education — Photosynthesis"; S2 = "National Geographic Education — Chlorophyll"; S3 = "NASA Science — Earth Observatory"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Photosynthesis", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/photosynthesis/"},
    {"id": "k2", "title": "Chlorophyll", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/chlorophyll/"},
    {"id": "k3", "title": "Earth Observatory", "publisher": "NASA", "url": "https://science.nasa.gov/earth/earth-observatory/"}],
  "facts": [
    F(1, "Fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.", "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar.", S1),
    F(2, "Bitkiler karbondioksiti ve suyu havadan ve topraktan alır.", "plants take in carbon dioxide (CO2) and water (H2O) from the air and soil.", S1),
    F(3, "Bitkiler Güneş ışığının enerjisini yakalayarak oksijen ve glikozda (bir şeker) depolanan kimyasal enerji üretir.", "capture energy from sunlight to produce oxygen (O2) and chemical energy stored in glucose (a sugar)", S1),
    F(4, "Bitki oksijeni havaya geri verir, enerjiyi glikoz moleküllerinde saklar.", "The plant then releases the oxygen back into the air, and stores energy within the glucose molecules.", S1),
    F(5, "Bitki hücresinin içinde Güneş ışığının enerjisini depolayan kloroplast adlı küçük organeller vardır; klorofil kloroplastlarda bulunur.", "Inside the plant cell are small organelles called chloroplasts, which store the energy of sunlight. / Chlorophyll is located in a plant’s chloroplasts, which are tiny structures in a plant’s cells.", S1 + "; " + S2),
    F(6, "Klorofil mavi ve kırmızı ışık dalgalarının enerjisini soğurur, yeşil ışık dalgalarını yansıtır; bitkilere yeşil rengini verir.", "chlorophyll absorbs energy from blue- and red-light waves, and reflects green-light waves / Chlorophyll gives plants their green color because it does not absorb the green wavelengths of white light.", S1 + "; " + S2),
    F(7, "Işığa bağımlı tepkime tilakoit zarında gerçekleşir ve sürekli Güneş ışığı gerektirir; su yükseltgenir (elektron kaybeder) ve oksijene dönüşür; ATP ve NADPH molekülleri oluşur.", "The light-dependent reaction takes place within the thylakoid membrane and requires a steady stream of sunlight / Within the plant cell, the water is oxidized, meaning it loses electrons / energy from the ATP and NADPH molecules", S1),
    F(8, "Işığa bağımlı olmayan aşama (Calvin döngüsü) stromada gerçekleşir; ATP ve NADPH moleküllerindeki enerji, karbondioksitten glikoz gibi karbonhidrat moleküllerini kurmak için kullanılır.", "The light-independent stage, also known as the Calvin cycle, takes place in the stroma / energy from the ATP and NADPH molecules is used to assemble carbohydrate molecules, like glucose, from carbon dioxide.", S1),
    F(9, "Bitkiler glikozu topraktan aldıkları besin maddeleriyle birlikte yeni yapraklar ve başka bitki bölümleri yapmak için kullanır.", "Plants use glucose together with nutrients taken from the soil to make new leaves and other plant parts.", S2),
    F(10, "Dünya'daki yaşamın çoğu fotosenteze bağlıdır; karadan denize her tür ekosistemde besin ağları fotosentezle başlar.", "Most life on Earth depends on photosynthesis. / Because food webs in every type of ecosystem, from terrestrial to marine, begin with photosynthesis", S1 + "; " + S2),
    F(11, "Fotosentezi bitkiler, algler ve bazı bakteri türleri yapar.", "The process is carried out by plants, algae, and some types of bacteria", S1),
    F(12, "Soluduğumuz oksijenin çoğu okyanustaki minik bitkilerden gelir.", "Did you know that most of the oxygen we breathe comes from tiny plants in the ocean?", S1),
    F(13, "Sonbaharda yeşil klorofil azaldıkça öteki pigmentler ortaya çıkar.", "As green chlorophyll fades from trees and plants each autumn, other pigments color Earth’s landscapes.", S3),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyografik"; AN = "A Te Pe ve En A De Pe Ha"
e.sec("hook", [
    L("Sen acıkınca mutfağa gidersin. Peki bir ağaç acıkınca ne yapar?"),
    L("Ne ağzı var ne midesi. Ama besinini kendi üretir; üstelik bunu ışıkla yapar!", [1]),
    L("Bugün bir yaprağın içine giriyoruz!"),
])
e.sec("context", [
    L("Ben de enerjimi kendim üretmek isterdim. Ama bende yaprak yok, yalnızca şarj girişi var!"),
    L("Üç sorumuz var. Bitki besinini neyle üretir? Yaprağın içinde neler olur? Ve bu olay bizim için neden hayati?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir.", [1], f"{NGs}'e göre fotosentez, bitkilerin Güneş ışığını, suyu ve karbondioksiti kullanarak oksijen ve şeker biçiminde enerji ürettiği süreçtir."),
    L("Malzemeler basit: bitki, havadan karbondioksit, topraktan su alır.", [2]),
    L("Güneş ışığının enerjisini yakalar ve iki şey üretir: oksijen ve glikoz. Glikoz bir şekerdir; enerjiyi kimyasal olarak depolar.", [3]),
    L("Bitki oksijeni havaya geri verir, enerjiyi ise glikoz moleküllerinde saklar.", [4]),
    L("Bütün bunlar nerede olur? Bitki hücrelerinin içindeki kloroplast adlı minik organellerde.", [5]),
    L("Kloroplastlarda klorofil adlı bir pigment, yani renk maddesi bulunur. Işığın enerjisini soğuran odur.", [5, 6]),
    L("Klorofil, ışığın mavi ve kırmızı dalgalarını soğurur; yeşil dalgaları ise yansıtır. Yapraklar bu yüzden yeşil görünür.", [6]),
    L("Yani bitkiler, kullanmadığı rengi bize yolluyor. Yeşil aslında artan renk!", [6]),
])
e.sec("finding", [
    L("Şimdi yaprağın içindeki fabrikaya girelim. Fotosentez iki aşamada gerçekleşir.", [7, 8]),
    L("Birinci aşama: ışığa bağımlı tepkimeler. Kloroplastın içindeki tilakoit zarında gerçekleşir ve sürekli Güneş ışığı ister.", [7]),
    L("Burada su molekülleri elektron kaybeder; buna yükseltgenme denir. Su, oksijene dönüşür.", [7]),
    L("Işığın enerjisi ise ATP ve NADPH adlı iki enerji taşıyıcı moleküle yüklenir.", [7], f"Işığın enerjisi ise {AN} adlı iki enerji taşıyıcı moleküle yüklenir."),
    L("Yani ATP, bitkinin şarjlı pili. Sonunda benim de anladığım bir şey!", [], "Yani A Te Pe, bitkinin şarjlı pili. Sonunda benim de anladığım bir şey!"),
    L("İkinci aşama: Calvin döngüsü. Işığa bağımlı değildir ve kloroplastın stroma adlı bölümünde gerçekleşir.", [8], "İkinci aşama: Kalvin döngüsü. Işığa bağımlı değildir ve kloroplastın stroma adlı bölümünde gerçekleşir."),
    L("Bu aşamada ATP ve NADPH'deki enerji kullanılır ve karbondioksitten glikoz gibi karbonhidrat molekülleri kurulur.", [8], f"Bu aşamada {AN}'daki enerji kullanılır ve karbondioksitten glikoz gibi karbonhidrat molekülleri kurulur."),
    L("Özetle: ışığın enerjisi önce pillere, sonra şekere aktarılır.", [7, 8]),
    L("Peki bitki glikozu ne yapar? Topraktan aldığı besin maddeleriyle birlikte yeni yapraklar ve başka bölümler üretir.", [9]),
])
e.sec("importance", [
    L("Bu olay yalnızca bitkiler için önemli değildir. National Geographic'e göre Dünya'daki yaşamın çoğu fotosenteze bağlıdır.", [10], f"Bu olay yalnızca bitkiler için önemli değildir. {NGs}'e göre Dünya'daki yaşamın çoğu fotosenteze bağlıdır."),
    L("Çünkü karadan denize, her ekosistemde besin ağları fotosentezle başlar. Bitkiyi yiyen de, onu yiyen de enerjisini en başta buradan alır.", [10]),
    L("Soluduğun oksijen de fotosentezin ürünüdür.", [1, 4]),
    L("Fotosentez yapanlar yalnızca bitkiler değildir: algler ve bazı bakteri türleri de yapar.", [11]),
    L("Peki sonbaharda yapraklar neden renk değiştirir? NASA'ya göre yeşil klorofil azalınca öteki pigmentler ortaya çıkar.", [13], "Peki sonbaharda yapraklar neden renk değiştirir? Nasa'ya göre yeşil klorofil azalınca öteki pigmentler ortaya çıkar."),
    L("Şimdi sıra sende! Aynı türden iki küçük saksı bitkisi al. Birini pencere önüne, ötekini karanlık bir dolaba koy."),
    L("İkisine de aynı miktarda su ver. Bir hafta boyunca her gün ikisini de gözle: renklerine ve yapraklarına bak."),
    L("Gözlemlerini bir tabloya yaz. Işık eksik kalınca bitkide ne değişiyor?"),
    L("Deney bitince dolaptaki bitkiyi yeniden ışığa çıkarmayı unutma!"),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? National Geographic'e göre soluduğumuz oksijenin çoğu, okyanustaki minik bitkilerden gelir.", [12], f"Bunu biliyor muydun? {NGs}'e göre soluduğumuz oksijenin çoğu, okyanustaki minik bitkilerden gelir."),
    L("Hızlı soru! Işığın enerjisini soğuran yeşil pigmentin adı neydi?", [6]),
    L("Düşün bakalım... Evet: klorofil!", [6]),
    L("Bende klorofil yok. Ama şarj ışığım yeşil yanıyor; o da bir şey!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de pencere önüne geçeyim; fotosentez yapamam ama güneşlenmeyi severim!"),
])
S = e.S
S(3, {"type": "hook", "question": "Bir ağaç acıkınca ne yapar?", "emoji": "🌳"}, ["🍃", "☀️", "💧", "🌱"], ["", "IŞIKLA BESİN!", "YAPRAĞIN İÇİNE!"], extra=[1])
S(1, {"type": "spotlight", "title": "Kendi enerjini üret", "emoji": "🤖", "chips": [{"label": "Yaprağım yok", "emoji": "🍃"}, {"label": "Şarj girişim var", "emoji": "🔌"}, {"label": "Bitkileri kıskandım!", "emoji": "😅"}]}, ["🔋", "🌿"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Bitki besinini neyle üretir?", "Yaprağın içinde neler olur?", "Bu olay bizim için neden hayati?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "diagram", "title": "Fotosentezin malzemeleri", "layout": "flow", "nodes": [{"label": "Güneş ışığı", "emoji": "☀️"}, {"label": "Su: topraktan", "emoji": "💧"}, {"label": "Karbondioksit: havadan", "emoji": "💨"}]}, ["🌱", "🧪"], ["FOTOSENTEZ", "ÜÇ MALZEME"])
S(2, {"type": "comparison", "title": "Fotosentezin ürünleri", "left": {"title": "Oksijen 🫧", "items": ["Havaya geri verilir"]}, "right": {"title": "Glikoz 🍬", "items": ["Bir şeker", "Enerjiyi depolar"]}}, ["🍃", "⚡"], ["OKSİJEN + GLİKOZ", "ENERJİ DEPOSU 🍬"])
S(3, {"type": "spotlight", "title": "Kloroplast", "emoji": "🌿", "chips": [{"label": "Hücredeki minik organel", "emoji": "🔬"}, {"label": "Klorofil: yeşil pigment", "emoji": "🟢"}, {"label": "Mavi ve kırmızıyı soğurur", "emoji": "🔵"}, {"label": "Yeşili yansıtır", "emoji": "🍃"}]}, ["☀️", "🔴"], ["KLOROPLAST", "KLOROFİL 🟢", "YEŞİLİ YANSITIR"])
S(1, {"type": "big-number", "value": "Yeşil", "label": "Bitkinin kullanmadığı renk", "sub": "Bu yüzden yapraklar yeşil görünür", "icon": "🍃"}, ["🟢", "😄"], ["ARTAN RENK 😄"])
S(1, {"type": "comparison", "title": "İki aşama", "left": {"title": "Işığa bağımlı tepkimeler ☀️", "items": ["Tilakoit zarında"]}, "right": {"title": "Calvin döngüsü 🔄", "items": ["Stromada"]}}, ["🏭", "🍃"], ["İKİ AŞAMA"])
S(3, {"type": "diagram", "title": "Birinci aşama: ışığa bağımlı tepkimeler", "layout": "flow", "nodes": [{"label": "Güneş ışığı", "emoji": "☀️"}, {"label": "Su elektron kaybeder", "emoji": "💧"}, {"label": "Oksijen çıkar", "emoji": "🫧"}, {"label": "ATP ve NADPH yüklenir", "emoji": "🔋"}]}, ["⚡", "🔬"], ["TİLAKOİT ZARI", "SU → OKSİJEN", "ATP + NADPH 🔋"])
S(1, {"type": "spotlight", "title": "ATP: şarjlı pil", "emoji": "🔋", "chips": [{"label": "Enerji taşıyan molekül", "emoji": "⚡"}, {"label": "Muma: bunu anladım!", "emoji": "🤖"}]}, ["🔌", "😄"], ["ŞARJLI PİL 🔋"])
S(2, {"type": "diagram", "title": "İkinci aşama: Calvin döngüsü", "layout": "cycle", "nodes": [{"label": "Karbondioksit", "emoji": "💨"}, {"label": "ATP ve NADPH enerjisi", "emoji": "🔋"}, {"label": "Glikoz", "emoji": "🍬"}]}, ["🔄", "🍃"], ["CALVIN DÖNGÜSÜ 🔄", "KARBONDİOKSİT → GLİKOZ"])
S(2, {"type": "bullets", "title": "Özet", "items": ["Işık enerjisi → ATP ve NADPH", "ATP ve NADPH → glikoz", "Glikoz + topraktaki besinler → yeni yapraklar"]}, ["📝", "🌱"], ["IŞIK → PİL → ŞEKER", "YENİ YAPRAKLAR 🌱"])
S(1, {"type": "big-number", "value": "Yaşamın çoğu", "label": "fotosenteze bağlı", "sub": "National Geographic", "icon": "🌍"}, ["🌳", "🐾"], ["HAYATİ!"])
S(2, {"type": "diagram", "title": "Besin ağı fotosentezle başlar", "layout": "flow", "nodes": [{"label": "Güneş", "emoji": "☀️"}, {"label": "Bitki", "emoji": "🌱"}, {"label": "Bitkiyi yiyen", "emoji": "🐛"}, {"label": "Onu yiyen", "emoji": "🐦"}]}, ["🕸️", "🫧"], ["BESİN AĞI", "OKSİJEN DE BURADAN 🫧"])
S(1, {"type": "spotlight", "title": "Kimler fotosentez yapar?", "emoji": "☀️", "chips": [{"label": "Bitkiler", "emoji": "🌳"}, {"label": "Algler", "emoji": "🌊"}, {"label": "Bazı bakteriler", "emoji": "🦠"}]}, ["🔬", "🍃"], ["YALNIZCA BİTKİLER DEĞİL"])
S(1, {"type": "comparison", "title": "Sonbaharda yapraklar", "left": {"title": "Yazın 🍃", "items": ["Klorofil bol", "Yapraklar yeşil"]}, "right": {"title": "Sonbaharda 🍂", "items": ["Klorofil azalır", "Öteki pigmentler görünür"]}}, ["🍁", "🍂"], ["SONBAHAR RENKLERİ 🍂"])
S(3, {"type": "bullets", "title": "Sen de dene: ışık deneyi 🔬", "items": ["Aynı türden iki saksı bitkisi", "Biri pencerede, biri karanlık dolapta", "İkisine de aynı miktarda su", "Bir hafta gözle ve tabloya yaz"]}, ["🪴", "📓", "💧"], ["DENEY ZAMANI 🔬", "HER GÜN GÖZLE 👀", "TABLO TUT 📓"])
S(1, {"type": "spotlight", "title": "Unutma!", "emoji": "🪴", "chips": [{"label": "Deney bitince bitkiyi ışığa çıkar", "emoji": "☀️"}, {"label": "Ona iyi bak", "emoji": "💚"}]}, ["🌱", "💧"], ["IŞIĞA ÇIKAR ☀️"])
S(1, {"type": "big-number", "value": "Okyanus", "label": "Soluduğumuz oksijenin çoğunun kaynağı", "sub": "Minik deniz bitkileri", "icon": "🌊"}, ["🫧", "🐟"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Işığı soğuran yeşil pigmentin adı ne?", "emoji": "🤔"}, ["🍃", "🟢"], ["HIZLI SORU!", "KLOROFİL ✅", "YEŞİL IŞIK 🟢"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 11, "videoTitle": "Bitkiler besinini nasıl üretir?", "paperTitleTr": "Bitkiler besinini nasıl üretir?",
  "takeaways": ["Bitkiler ışık, su ve karbondioksitten glikoz ve oksijen üretir", "Klorofil ışığı soğurur; fotosentez iki aşamada gerçekleşir", "Besin ağları ve soluduğumuz oksijen fotosenteze bağlıdır"],
  "description": "Bir ağaç acıkınca ne yapar? Bu bölümde fotosentezi; bitkilerin ışık, su ve karbondioksitten nasıl glikoz ve oksijen ürettiğini; kloroplastı, klorofili ve yaprakların neden yeşil göründüğünü; ışığa bağımlı tepkimeleri, ATP ile NADPH'yi ve Calvin döngüsünü keşfediyoruz. Fotosentez bizim için neden hayati, sonbaharda yapraklar neden renk değiştirir? Sonunda iki saksıyla ışık deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Fotosentez", "meaning": "Bitkilerin ışık, su ve karbondioksit kullanarak oksijen ve şeker üretmesi."},
    {"term": "Karbondioksit", "meaning": "Havada bulunan, bitkilerin fotosentezde kullandığı gaz."},
    {"term": "Glikoz", "meaning": "Enerjiyi depolayan bir şeker."},
    {"term": "Kloroplast", "meaning": "Bitki hücresinde fotosentezin gerçekleştiği minik organel."},
    {"term": "Klorofil", "meaning": "Işığın enerjisini soğuran ve bitkilere yeşil rengini veren pigment."},
    {"term": "Pigment", "meaning": "Renk veren madde."},
    {"term": "ATP", "meaning": "Hücrede enerji taşıyan molekül."},
    {"term": "Calvin döngüsü", "meaning": "Fotosentezin, karbondioksitten glikoz kurulan ikinci aşaması."},
    {"term": "Ekosistem", "meaning": "Bir bölgedeki canlıların ve çevrelerinin oluşturduğu bütün."}],
  "song": e.song("Işıktan Şeker", [("☀️", "Güneş"), ("💧", "Su"), ("🍃", "Klorofil"), ("🍬", "Glikoz"), ("🫧", "Oksijen")],
    ["Havadan karbondioksit, topraktan su", "Güneşin ışığı yaprağa konar", "Kloroplastta klorofil yakalar", "Mavi, kırmızı içeri; yeşil yansır"],
    ["Fotosentez! Işıktan şeker!", "Oksijen havaya, enerji glikoza", "Önce ışık pillere dolar", "Calvin döngüsü şekeri kurar"],
    ["Tilakoitte ışık, stromada döngü", "ATP taşır enerji yükünü", "Besin ağları burada başlar", "Algler, bakteriler de yapar"],
    ["Fotosentez! Işıktan şeker!", "Oksijen havaya, enerji glikoza", "Soluduğun oksijen onların işi", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
