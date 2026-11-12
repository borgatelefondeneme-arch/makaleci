"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kara-delik-nedir"
S1 = "NASA Science — Black Holes"; S3 = "NASA Science — Black Hole Anatomy"; S4 = "NASA Science — Black Hole Types"; S5 = "NASA — What Is a Black Hole? (Grades 5-8)"; S7 = "NASA Science — First Image of a Black Hole"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Black Holes", "publisher": "NASA", "url": "https://science.nasa.gov/universe/black-holes/"},
    {"id": "k2", "title": "Black Hole Anatomy", "publisher": "NASA", "url": "https://science.nasa.gov/universe/black-holes/anatomy/"},
    {"id": "k3", "title": "Black Hole Types", "publisher": "NASA", "url": "https://science.nasa.gov/universe/black-holes/types/"},
    {"id": "k4", "title": "What Is a Black Hole? (Grades 5-8)", "publisher": "NASA", "url": "https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-a-black-hole-grades-5-8/"},
    {"id": "k5", "title": "First Image of a Black Hole", "publisher": "NASA", "url": "https://science.nasa.gov/resource/first-image-of-a-black-hole/"}],
  "facts": [
    F(1, "Kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir; güçlü kütle çekimi, maddenin çok küçük bir alana sıkışmasından kaynaklanır.", "A black hole is a region in space where the pulling force of gravity is so strong that light is not able to escape. / The strong gravity occurs because matter has been pressed into a tiny space.", S5),
    F(2, "Kara delikler aslında delik değildir; çok küçük alanlara sıkışmış dev madde yoğunlaşmalarıdır.", "These objects aren’t really holes. / They’re huge concentrations of matter packed into very tiny spaces.", S1),
    F(3, "Yıldız kütleli kara delikler, çok büyük kütleli bir yıldızın merkezi kendi üzerine çökünce oluşur; yıldız süpernova olarak patlar; kütlesi Güneş'in yaklaşık 20 katı ya da daha fazlaysa merkez yıldız kütleli bir kara deliğe çöker.", "Stellar black holes form when the center of a very massive star collapses in upon itself. / its core collapses, rebounds, and explodes as a supernova. / If it had around 20 times the Sun’s mass or more, the star’s core collapses into a stellar-mass black hole.", S5 + "; " + S4, ["20"]),
    F(4, "Güneş'in kütlesi kara deliğe çökmeye yetmez.", "The sun does not have enough mass to collapse into a black hole.", S5),
    F(5, "Olay ufku kara deliğin yüzeyi gibi düşünülebilir; onu geçen her şey, ışık bile, içeride kalmaya mahkûmdur. Bu sınırın içinde kaçış için gereken hız ışık hızını aşar; hiçbir şey ışıktan hızlı gidemez.", "We can think of the event horizon as the black hole’s surface. / So whatever passes into the event horizon is doomed to stay inside it – even light. / Inside this boundary, the velocity needed to escape the black hole exceeds the speed of light, which is as fast as anything can go.", S3),
    F(6, "Kara deliğin tam merkezinde maddenin sonsuz yoğunluğa ezildiği bir nokta (tekillik) vardır.", "the very center of a black hole contains a point where matter is crushed to infinite density.", S3),
    F(7, "Kara delikten gelen ışığın ana kaynağı birikim diskidir; gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışını yayar.", "The main light source from a black hole is a structure called an accretion disk. / the gas heats to very high temperatures and releases X-ray light in all directions.", S3 + "; " + S5),
    F(8, "Bazı kara deliklerden zıt yönlere fışkıran bir çift jet çıkar.", "a pair of jets that blast away from it in opposite directions.", S3),
    F(9, "Kara delikler kütlelerine göre üç gruba ayrılır: yıldız kütleli (Güneş'in birkaç katından yüzlerce katına), orta kütleli ve süper kütleli (Güneş'in yüz binlerce katından milyarlarca katına).", "divide black holes into three categories according to their mass / The masses of these newly born objects can range from a few to hundreds of times the Sun’s mass / These monster objects have hundreds of thousands to billions of times the Sun’s mass / These should range from around one hundred to hundreds of thousands of times the Sun’s mass", S4),
    F(10, "Bizim gökadamızın merkezindeki süper kütleli kara delik Sagittarius A*'dır; kütlesi Güneş'in 4 milyon katıdır.", "Our is called Sagittarius A* (pronounced ey-star), and it’s 4 million times the Sun’s mass.", S1, ["4"]),
    F(11, "Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için fiilen görünmezdir. Süper kütleli bir kara deliğin güçlü kütle çekimi, yıldızların çevresinde belirli bir biçimde dolanmasına yol açabilir.", "Black holes don’t emit or reflect light, making them effectively invisible to telescopes. / A supermassive black hole’s intense gravity can cause stars to orbit around it in a particular way.", S1),
    F(12, "Kara delikler uzay-zamanın dokusunda kütle çekim dalgaları denen dalgalanmalar yaratır.", "they create ripples in the fabric of space-time called gravitational waves.", S1),
    F(13, "Bilim insanları Olay Ufku Teleskobu ile M87 gökadasının merkezindeki kara deliğin görüntüsünü elde etti (2019); Dünya'dan yaklaşık 55 milyon ışık yılı uzaktadır.", "Using the Event Horizon Telescope, scientists obtained an image of the black hole at the center of the galaxy M87. / located about 55 million light years from Earth. (April 10, 2019)", S7, ["87", "55", "2019"]),
    F(14, "Spagettileşme, maddenin kara deliğe fazla yaklaşınca başına gelenleri anlatan gerçek bir terimdir: madde yatayda sıkışır, dikeyde uzar ve bir erişteye benzer.", "A real term that describes what happens when matter gets too close to a black hole. / It’s squeezed horizontally and stretched vertically, resembling a noodle.", S1),
    F(15, "Kara delikler kozmik elektrik süpürgesi değildir; başka maddeleri emmez. Yeterince uzaktan kütle çekim etkileri aynı kütledeki başka cisimlerinkiyle aynıdır.", "Cosmic vacuum cleaners. Black holes don’t suck in other matter. / From far enough away, their gravitational effects are just like those of other objects of the same mass.", S1),
    F(16, "Güneş'in yerini aynı kütlede bir kara delik alsaydı Dünya içine düşmezdi; gezegenler şimdi Güneş'in çevresinde dolandıkları gibi dolanmayı sürdürürdü.", "If a black hole with the same mass as the sun were to replace the sun, Earth would not fall in. / The planets would still orbit the black hole as they orbit the sun now.", S5),
    F(17, "Bilinen en yakın kara delik (Gaia BH1) yaklaşık 1.500 ışık yılı uzaktadır.", "The nearest known black hole, called Gaia BH1, is about 1,500 light-years away.", S1, ["1.500", "1"]),
    F(18, "Gözlenen en büyük kütleli kara delik TON 618'dir: Güneş'in 66 milyar katı kütlededir.", "The most massive black hole observed, TON 618, tips the scales at 66 billion times the Sun’s mass.", S1, ["618", "66"]),
]}
e = Ep(); L = e.L
N = "Nasa"
e.sec("hook", [
    L("Uzayda öyle bir yer düşün ki, içine giren hiçbir şey geri çıkamıyor. Işık bile!", [1]),
    L("Bu nasıl mümkün olabilir? Ve göremediğimiz bir şeyi bilim insanları nasıl buluyor?"),
    L("Bugün bir kara deliğe yaklaşıyoruz. Güvenli mesafeden tabii!"),
])
e.sec("context", [
    L("Ben fazla yaklaşmayacağım. Şarj kablom o kadar uzun değil!"),
    L("Üç sorumuz var. Kara delik nedir? Nasıl oluşur? Ve görünmez bir şey nasıl keşfedilir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir.", [1], f"{N}'ya göre kara delik, kütle çekiminin ışığın bile kaçamayacağı kadar güçlü olduğu bir uzay bölgesidir."),
    L("Adı seni yanıltmasın: kara delikler aslında delik değildir. Tam tersine, çok küçük bir alana sıkışmış dev miktarda maddedir.", [2]),
    L("Kütle çekimi neden bu kadar güçlü? Çünkü madde küçücük bir alana sıkışmıştır.", [1]),
    L("Peki nasıl oluşur? Her şey çok büyük kütleli bir yıldızla başlar. Yıldızın merkezi kendi üzerine çöker.", [3]),
    L("Yıldız, süpernova denen dev bir patlamayla dağılır.", [3]),
    L("Yıldızın kütlesi Güneş'inkinin yaklaşık 20 katı ya da daha fazlaysa, çöken merkez bir kara deliğe dönüşür.", [3], "Yıldızın kütlesi Güneş'inkinin yaklaşık yirmi katı ya da daha fazlaysa, çöken merkez bir kara deliğe dönüşür."),
    L("Güneş'imiz için endişelenme: onun kütlesi kara delik olmaya yetmez.", [4]),
    L("Oh! Güneş enerjisiyle şarj olan arkadaşlarım adına sevindim."),
])
e.sec("finding", [
    L("Şimdi bir kara deliğin bölümlerine bakalım. En önemli sınır olay ufkudur. Onu kara deliğin yüzeyi gibi düşünebilirsin.", [5]),
    L("Olay ufkunu geçen hiçbir şey geri dönemez. Çünkü oradan kaçmak için gereken hız, ışık hızından büyüktür ve hiçbir şey ışıktan hızlı gidemez.", [5]),
    L("Tam merkezde tekillik bulunur: maddenin sonsuz yoğunluğa kadar ezildiği nokta.", [6]),
    L("Kara deliğin çevresindeki gaz, birikim diski denen bir yapı oluşturur. Kara delikten gelen ışığın ana kaynağı bu disktir.", [7]),
    L("Gaz çok yüksek sıcaklıklara ısınır ve her yöne X ışınları yayar.", [7]),
    L("Bazı kara deliklerden zıt yönlere fışkıran bir çift jet de çıkar.", [8]),
    L("Kara delikler kütlelerine göre üç gruba ayrılır. Yıldız kütleli olanlar, Güneş'in birkaç katından yüzlerce katına kadar kütle taşır.", [9]),
    L("Süper kütleli kara delikler ise Güneş'in yüz binlerce katından milyarlarca katına kadar kütlelidir. Aradakilere orta kütleli denir.", [9]),
    L("Bizim gökadamız Samanyolu'nun merkezinde de bir tane var: Sagittarius A*. Kütlesi Güneş'in 4 milyon katı!", [10], "Bizim gökadamız Samanyolu'nun merkezinde de bir tane var: Sagitaryus A yıldız. Kütlesi Güneş'in dört milyon katı!"),
    L("Kara deliğe çok yaklaşan maddeye ne olur? Yatayda sıkışır, dikeyde uzar ve bir erişteye benzer. Bunun gerçek bir bilimsel adı var: spagettileşme!", [14]),
])
e.sec("importance", [
    L("Ben spagetti olmam ama. Olsa olsa tel şehriye!"),
    L("Peki ışık yaymayan bir şeyi nasıl buluruz? Kara delikler ışık yaymaz ve yansıtmaz; teleskoplar için neredeyse görünmezdir.", [11]),
    L("Ama çevreleri onları ele verir. Güçlü kütle çekimi, yakındaki yıldızların kendine özgü bir biçimde dolanmasına yol açar.", [11]),
    L("Birikim diskinin yaydığı X ışınları da bir ipucudur.", [7]),
    L("Kara delikler ayrıca uzay-zamanın dokusunda dalgalanmalar yaratır. Bunlara kütle çekim dalgaları denir.", [12]),
    L("2019'da büyük bir an yaşandı: Olay Ufku Teleskobu ile bir kara deliğin görüntüsü elde edildi.", [13], "İki bin on dokuzda büyük bir an yaşandı: Olay Ufku Teleskobu ile bir kara deliğin görüntüsü elde edildi."),
    L("Bu kara delik, M87 adlı gökadanın merkezinde, bizden yaklaşık 55 milyon ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.", [13], "Bu kara delik, Em seksen yedi adlı gökadanın merkezinde, bizden yaklaşık elli beş milyon ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur."),
    L("Şimdi bir yanlış inanışı düzeltelim: kara delikler uzayın elektrik süpürgesi değildir. Çevrelerindeki her şeyi içine çekmezler.", [15]),
    L("Yeterince uzaktan bakıldığında kütle çekimleri, aynı kütledeki başka bir cisminkiyle aynıdır.", [15]),
    L("NASA'nın örneği şöyle: Güneş'in yerine aynı kütlede bir kara delik koysaydık Dünya içine düşmezdi. Gezegenler dolanmaya devam ederdi.", [16], f"{N}'nın örneği şöyle: Güneş'in yerine aynı kütlede bir kara delik koysaydık Dünya içine düşmezdi. Gezegenler dolanmaya devam ederdi."),
    L("Üstelik bilinen en yakın kara delik bile yaklaşık 1.500 ışık yılı uzakta. Yani güvendeyiz!", [17], "Üstelik bilinen en yakın kara delik bile yaklaşık bin beş yüz ışık yılı uzakta. Yani güvendeyiz!"),
    L("Şimdi sıra sende! Esnek bir kumaşı gergin tut ve ortasına ağır bir top koy. Sonra kenardan bilyeler yuvarla."),
    L("Bilyelerin çukura doğru nasıl kıvrıldığını izle. Bu yalnızca bir model; ama büyük bir kütlenin çevresini nasıl etkilediğini hayal etmene yardım eder."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Gözlenen en büyük kütleli kara deliğin adı TON 618. Kütlesi Güneş'in 66 milyar katı!", [18], "Bunu biliyor muydun? Gözlenen en büyük kütleli kara deliğin adı Ton altı yüz on sekiz. Kütlesi Güneş'in altmış altı milyar katı!"),
    L("Hızlı soru! Güneş bir gün kara deliğe dönüşecek mi?", [4]),
    L("Düşün bakalım... Hayır! Kütlesi buna yetmez.", [4]),
    L("Ben de dönüşmem. Benim kütlem ancak bir okul çantasını doldurur!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben güvenli mesafeden uçuyorum; olay ufkuna uzaktan el sallarım!"),
])
S = e.S
S(3, {"type": "hook", "question": "Işığın bile kaçamadığı yer neresi?", "emoji": "⚫"}, ["⭐", "🔭", "🌌", "✨"], ["", "GÖRÜNMEZİ BULMAK?", "GÜVENLİ MESAFEDEN!"])
S(1, {"type": "spotlight", "title": "Güvenli mesafe", "emoji": "🤖", "chips": [{"label": "Fazla yaklaşmam", "emoji": "🚫"}, {"label": "Şarj kablom kısa", "emoji": "🔌"}, {"label": "Buradan anlatırım!", "emoji": "📣"}]}, ["🔌", "🌌"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kara delik nedir?", "Nasıl oluşur?", "Görünmez bir şey nasıl keşfedilir?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "spotlight", "title": "Kara delik nedir?", "emoji": "⚫", "chips": [{"label": "Çok güçlü kütle çekimi", "emoji": "🧲"}, {"label": "Işık bile kaçamaz", "emoji": "💡"}, {"label": "Delik değil: sıkışmış madde", "emoji": "🪨"}, {"label": "Küçücük alan, dev kütle", "emoji": "🤏"}]}, ["🌌", "✨"], ["IŞIK BİLE KAÇAMAZ", "DELİK DEĞİL!", "SIKIŞMIŞ MADDE"])
S(3, {"type": "diagram", "title": "Yıldız kütleli kara delik nasıl oluşur?", "layout": "flow", "nodes": [{"label": "Çok büyük kütleli yıldız", "emoji": "⭐"}, {"label": "Merkezi çöker", "emoji": "⬇️"}, {"label": "Süpernova", "emoji": "💥"}, {"label": "Güneş'in yaklaşık 20 katı ve üstü: kara delik", "emoji": "⚫"}]}, ["🌟", "🔭"], ["DEV YILDIZ ⭐", "SÜPERNOVA 💥", "KARA DELİK ⚫"])
S(2, {"type": "comparison", "title": "Ya Güneş?", "left": {"title": "Güneş ☀️", "items": ["Kütlesi yetmez", "Kara delik olmayacak"]}, "right": {"title": "Dev yıldız ⭐", "items": ["Güneş'in yaklaşık 20 katı ya da fazlası", "Merkezi kara deliğe çöker"]}}, ["☀️", "🔋"], ["GÜNEŞ GÜVENDE ☀️", "OH! 😅"], extra=[3])
S(3, {"type": "spotlight", "title": "Kara deliğin bölümleri", "emoji": "⚫", "chips": [{"label": "Olay ufku: yüzey gibi", "emoji": "⭕"}, {"label": "Geçen geri dönemez", "emoji": "🚫"}, {"label": "Kaçış hızı ışık hızından büyük", "emoji": "💡"}, {"label": "Tekillik: sonsuz yoğunluk", "emoji": "📍"}]}, ["🌌", "🚀"], ["OLAY UFKU", "GERİ DÖNÜŞ YOK", "TEKİLLİK"])
S(3, {"type": "diagram", "title": "Çevresinde neler var?", "layout": "flow", "nodes": [{"label": "Birikim diski: sıcak gaz", "emoji": "🌀"}, {"label": "X ışınları yayar", "emoji": "✨"}, {"label": "Zıt yönlere iki jet", "emoji": "🚀"}]}, ["🔥", "🛰️"], ["BİRİKİM DİSKİ 🌀", "X IŞINLARI", "JETLER 🚀"])
S(2, {"type": "bullets", "title": "Üç grup", "items": ["Yıldız kütleli: Güneş'in birkaç – yüzlerce katı", "Orta kütleli: aradakiler", "Süper kütleli: yüz binlerce – milyarlarca katı"]}, ["⚖️", "⭐"], ["YILDIZ KÜTLELİ", "SÜPER KÜTLELİ"])
S(1, {"type": "big-number", "value": "4 milyon", "unit": "Güneş kütlesi", "label": "Sagittarius A*", "sub": "Samanyolu'nun merkezindeki kara delik", "icon": "🌌"}, ["⭐", "🔭"], ["SAMANYOLU'NUN MERKEZİ"])
S(2, {"type": "spotlight", "title": "Spagettileşme", "emoji": "🍝", "chips": [{"label": "Yatayda sıkışır", "emoji": "↔️"}, {"label": "Dikeyde uzar", "emoji": "↕️"}, {"label": "Erişteye benzer", "emoji": "🍜"}, {"label": "Muma: tel şehriye!", "emoji": "🤖"}]}, ["🍴", "⚫"], ["SPAGETTİLEŞME 🍝", "TEL ŞEHRİYE 😄"])
S(2, {"type": "comparison", "title": "Görünmezi bulmak", "left": {"title": "Sorun 🙈", "items": ["Işık yaymaz", "Işık yansıtmaz"]}, "right": {"title": "İpucu 🔎", "items": ["Yakındaki yıldızların dolanışı"]}}, ["🔭", "⭐"], ["GÖRÜNMEZ!", "YILDIZLAR ELE VERİR ⭐"])
S(2, {"type": "diagram", "title": "Başka ipuçları", "layout": "flow", "nodes": [{"label": "Birikim diski", "emoji": "🌀"}, {"label": "X ışınları", "emoji": "🛰️"}, {"label": "Kütle çekim dalgaları", "emoji": "〰️"}]}, ["📡", "🌌"], ["X IŞINLARI 🛰️", "KÜTLE ÇEKİM DALGALARI"])
S(2, {"type": "big-number", "value": "55 milyon", "unit": "ışık yılı", "label": "Görüntüsü alınan kara deliğin uzaklığı", "sub": "M87 gökadası • 2019 • Olay Ufku Teleskobu", "icon": "📸"}, ["🔭", "🌌"], ["İLK GÖRÜNTÜ 📸", "IŞIK YILI"])
S(2, {"type": "spotlight", "title": "Elektrik süpürgesi değil!", "emoji": "🧹", "chips": [{"label": "Her şeyi içine çekmez", "emoji": "❌"}, {"label": "Uzaktan: aynı kütledeki cisim gibi", "emoji": "⚖️"}]}, ["🌌", "🪐"], ["YANLIŞ İNANIŞ ❌", "AYNI KÜTLE, AYNI ÇEKİM"])
S(1, {"type": "comparison", "title": "Güneş'in yerinde kara delik olsaydı", "left": {"title": "Koşul", "items": ["Güneş'le aynı kütlede"]}, "right": {"title": "Sonuç ✅", "items": ["Dünya içine düşmezdi", "Gezegenler dolanmaya devam ederdi"]}}, ["🌍", "🪐"], ["DÜNYA DÜŞMEZDİ"])
S(1, {"type": "big-number", "value": "1.500", "unit": "ışık yılı", "label": "Bilinen en yakın kara deliğin uzaklığı", "sub": "NASA", "icon": "📏"}, ["🌍", "✨"], ["GÜVENDEYİZ ✅"])
S(2, {"type": "bullets", "title": "Sen de dene: kumaş modeli 🔬", "items": ["Esnek kumaşı gergin tut", "Ortasına ağır bir top koy", "Kenardan bilyeler yuvarla", "Bilyeler nasıl kıvrılıyor?"]}, ["🧵", "🔮"], ["DENEY ZAMANI 🔬", "YALNIZCA BİR MODEL"])
S(1, {"type": "spotlight", "title": "TON 618", "emoji": "🏆", "chips": [{"label": "Gözlenen en büyük kütleli kara delik", "emoji": "⚫"}, {"label": "Güneş'in 66 milyar katı", "emoji": "☀️"}]}, ["🌌", "⚖️"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Güneş bir gün kara deliğe dönüşecek mi?", "emoji": "☀️"}, ["⚫", "⭐"], ["HIZLI SORU!", "HAYIR ✅", "BEN DE DÖNÜŞMEM 🎒"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 10, "videoTitle": "Kara delik nedir?", "paperTitleTr": "Kara delik nedir?",
  "takeaways": ["Kara delik delik değildir: çok küçük alana sıkışmış maddedir", "Olay ufkunu geçen hiçbir şey, ışık bile, geri dönemez", "Kara delikler çevrelerindeki yıldız, gaz ve ışınlardan bulunur"],
  "description": "Işığın bile kaçamadığı yer neresi? Bu bölümde kara deliğin ne olduğunu, dev yıldızların çöküşünü ve süpernovayı; olay ufkunu, tekilliği, birikim diskini ve jetleri; yıldız kütleli ve süper kütleli kara delikleri keşfediyoruz. Görünmeyen bir şey nasıl bulunur, spagettileşme nedir, kara delikler her şeyi yutar mı? Sonunda kumaş modeli etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kütle çekimi", "meaning": "Kütlesi olan cisimlerin birbirini çekmesi."},
    {"term": "Süpernova", "meaning": "Büyük kütleli bir yıldızın dev patlaması."},
    {"term": "Olay ufku", "meaning": "Kara deliğin çevresindeki sınır; onu geçen hiçbir şey geri dönemez."},
    {"term": "Tekillik", "meaning": "Kara deliğin merkezinde maddenin sonsuz yoğunluğa ezildiği nokta."},
    {"term": "Birikim diski", "meaning": "Kara deliğin çevresinde dönen, çok ısınmış gazdan oluşan yapı."},
    {"term": "X ışınları", "meaning": "Gözle görülmeyen, yüksek enerjili bir ışık türü."},
    {"term": "Gökada", "meaning": "Milyarlarca yıldızdan oluşan dev topluluk; bizimkinin adı Samanyolu."},
    {"term": "Işık yılı", "meaning": "Işığın bir yılda aldığı yol; uzaydaki uzaklıkları ölçmek için kullanılır."},
    {"term": "Spagettileşme", "meaning": "Kara deliğe çok yaklaşan maddenin uzayıp incelmesi."}],
  "song": e.song("Işığın Kaçamadığı Yer", [("⚫", "Kara delik"), ("⭐", "Dev yıldız"), ("💥", "Süpernova"), ("🌀", "Birikim diski"), ("🔭", "Teleskop")],
    ["Dev bir yıldızın merkezi çöker", "Süpernova patlar, gökyüzü titrer", "Madde sıkışır küçücük yere", "Çekim öyle güçlü, ışık bile gitmez"],
    ["Kara delik, kara delik; delik değil!", "Olay ufkunu geçen geri gelmez", "Merkezde tekillik, çevrede disk", "X ışınları parlar, ipucu verir"],
    ["Samanyolu'nun kalbinde bir dev var", "Dört milyon Güneş kadar ağır", "Yıldızların dansı onu ele verir", "Süpürge değil o, her şeyi çekmez"],
    ["Kara delik, kara delik; delik değil!", "Olay ufkunu geçen geri gelmez", "Güneş'imiz küçük, kara delik olmaz", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
