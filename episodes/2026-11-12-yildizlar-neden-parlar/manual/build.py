"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:yildizlar-neden-parlar"
S1 = "NASA Science — Stars (Star Basics)"; S2 = "NASA Science — Star Types"; S3 = "NASA Science — Sun: Facts"; S4 = "NASA Space Place — How Does Our Sun Compare With Other Stars?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Stars", "publisher": "NASA", "url": "https://science.nasa.gov/universe/stars/"},
    {"id": "k2", "title": "Star Types", "publisher": "NASA", "url": "https://science.nasa.gov/universe/stars/types/"},
    {"id": "k3", "title": "Sun: Facts", "publisher": "NASA", "url": "https://science.nasa.gov/sun/facts/"},
    {"id": "k4", "title": "How Does Our Sun Compare With Other Stars?", "publisher": "NASA", "url": "https://spaceplace.nasa.gov/sun-compare/en/"}],
  "facts": [
    F(1, "Yıldızlar sıcak gazdan oluşan dev toplardır; çoğunlukla hidrojenden, biraz helyumdan ve az miktarda başka elementlerden oluşurlar.", "Stars are giant balls of hot gas – mostly hydrogen, with some helium and small amounts of other elements.", S1),
    F(2, "Güneş, kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur; plazma denen çok sıcak, elektrik yüklü gazdan oluşur.", "The Sun is a huge ball of hydrogen and helium held together by its own gravity. / The Sun is made of super-hot, electrically charged gas called plasma.", S3),
    F(3, "Yıldızlar moleküler bulut denen büyük gaz ve toz bulutlarında oluşur; kütle çekimi bazı topakların çökmesine yol açar; topak yüz binlerce yıl boyunca kütle kazanır, dönmeye başlar ve ısınır; sonunda bir önyıldız (bebek yıldız) gelişir.", "Stars form in large clouds of gas and dust called molecular clouds. / Eventually, gravity causes some of these clumps to collapse. / Over hundreds of thousands of years, the clump gains mass, starts to spin, and heats up. / which eventually leads to the development of a protostar – a baby star.", S1 + "; " + S2),
    F(4, "Yıldızın çekirdeğindeki muazzam basınç ve sıcaklık hidrojen atomlarının çekirdeklerini sıkıştırarak helyum oluşturur; çekirdek kaynaşması (füzyon) enerji açığa çıkarır, yıldızı ısıtır ve kütle çekimi altında çökmesini önler; oluşan basınç kütle çekimine karşı iter.", "immense pressures and temperatures in the star's core squeeze the nuclei of hydrogen atoms together to form helium / Nuclear fusion releases energy, which heats the star and prevents it from further collapsing under the force of gravity. / Fusion releases energy that heats the star, creating pressure that pushes against the force of its gravity.", S1 + "; " + S2),
    F(5, "Güneş'in çekirdeğinde sıcaklık yaklaşık 15 milyon santigrat derecedir; yüzeyinde 5.500 santigrat derece.", "The temperature in the Sun's core is about 27 million degrees Fahrenheit (15 million degrees Celsius) / It's 10,000 degrees Fahrenheit (5,500 degrees Celsius) at the surface", S3 + "; " + S4, ["15", "5.500"]),
    F(6, "Güneş yaklaşık 4,6 milyar yıl önce oluştu; Dünya'dan yaklaşık 150 milyon kilometre uzaktadır; hacmini doldurmak için 1,3 milyon Dünya gerekir.", "The Sun formed about 4.6 billion years ago in a giant, spinning cloud of gas and dust called the solar nebula. / The Sun is about 93 million miles (150 million kilometers) from Earth. / it would take 1.3 million Earths to fill the Sun's volume", S3, ["4.6", "150", "1.3"]),
    F(7, "Çekirdeğinde hidrojeni helyuma kaynaştıran yıldıza ana kol yıldızı denir; Güneş ana kol evresinin aşağı yukarı ortasındadır.", "Scientists call a star that is fusing hydrogen to helium in its core a main sequence star. / Our Sun is roughly midway through its main sequence stage.", S2 + "; " + S1),
    F(8, "Kırmızı cüceler en küçük ana kol yıldızlarıdır; çapı Güneş'inkinin 1.000 katı olan yıldızlar bulunmuştur.", "Red dwarfs are the smallest main sequence stars – just a fraction of the Sun's size and mass. / We have found stars that are 1,000 times bigger in diameter than our sun.", S2 + "; " + S4, ["1.000"]),
    F(9, "Güneş yaklaşık 5 milyar yıl sonra kırmızı dev olacak; Merkür'ü ve Venüs'ü, belki Dünya'yı da yutacak kadar büyüyecek.", "The Sun will become a red giant in about 5 billion years. / becoming so large that it will engulf Mercury and Venus, and possibly Earth as well.", S2 + "; " + S3, ["5"]),
    F(10, "Genişleyen toz ve gaz bulutuna gezegenimsi bulutsu, geriye kalan yıldız kalıntısına beyaz cüce denir.", "creating an expanding cloud of dust and gas called a planetary nebula. / Scientists call this kind of stellar remnant a white dwarf.", S2),
    F(11, "Büyük kütleli yıldızların sonu süpernova denen dev bir patlamadır; kütlesi Güneş'in yaklaşık 8 ile 20 katı arasındaki yıldızlardan nötron yıldızı oluşur; daha ağır yıldızlar kara delik üretir.", "The result is a huge explosion called a supernova. / A neutron star forms when a main sequence star with between about eight and 20 times the Sun's mass / (Heavier stars produce stellar-mass black holes.)", S2, ["8", "20"]),
    F(12, "Füzyon karbonu oksijen, neon ve magnezyum gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir silisyumun demire kaynaşmasına kadar sürer; süpernovaların uzaya saçtığı madde gelecekteki moleküler bulutları zenginleştirir.", "Fusion converts carbon into heavier elements like oxygen, neon, and magnesium / For the largest stars, this chain continues until silicon fuses into iron. / Material cast into the cosmos by supernovae and other stellar events will enrich future molecular clouds", S1),
    F(13, "Samanyolu'nda 100 milyardan fazla yıldız vardır; evrende bir septilyona kadar yıldız olabilir: 1'in yanında 24 sıfır.", "Our Milky Way alone contains more than 100 billion, including our most well-studied star, the Sun. / Astronomers estimate that the universe could contain up to one septillion stars – that's a one followed by 24 zeros.", S1, ["100", "1", "24"]),
    F(14, "En yakın yıldız komşumuz kırmızı cüce Proxima Centauri'dir; 4,24 ışık yılı uzaktadır. Işık yılı, ışığın bir yılda aldığı yoldur.", "Our closest stellar neighbor, shown here in this Hubble image, is the red dwarf Proxima Centauri. / red dwarf star Proxima Centauri is 4.24 light-years away / A light-year is the distance light travels in one year", S2 + "; " + S3, ["4.24"]),
    F(15, "Sirius gece gökyüzünün en parlak yıldızıdır; birçok ana kol yıldızı çıplak gözle görülebilir.", "Sirius – the brightest star in the night sky / Many main sequence stars can be seen with the unaided eye, such as Sirius", S2),
    F(16, "Gözleri korumadan Güneş'e asla doğrudan bakılmamalıdır.", "never look directly at the Sun without protecting your eyes.", S3),
    F(17, "Her yıldızın kendi yaşam döngüsü vardır; birkaç milyon yıldan trilyonlarca yıla kadar sürer.", "Every star has its own life cycle, ranging from a few million to trillions of years", S1),
]}
e = Ep(); L = e.L
N = "Nasa"
e.sec("hook", [
    L("Gece gökyüzüne bak: sayısız ışık noktası. Her biri, aslında çok uzaktaki dev bir gaz topu!", [1]),
    L("Peki bir yıldız neden parlar? Yakıtı nedir? Ve bir gün söner mi?"),
    L("Bugün bir yıldızın kalbine yolculuk ediyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Yıldız nedir? Işığını nasıl üretir? Ve yıldızlar nasıl doğar, nasıl ölür?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("NASA'ya göre yıldızlar, sıcak gazdan oluşan dev toplardır. Çoğunlukla hidrojenden, biraz da helyumdan oluşurlar.", [1], f"{N}'ya göre yıldızlar, sıcak gazdan oluşan dev toplardır. Çoğunlukla hidrojenden, biraz da helyumdan oluşurlar."),
    L("En yakın örnek her gün tepemizde: Güneş! O da bir yıldızdır; kendi kütle çekimiyle bir arada duran dev bir hidrojen ve helyum topudur.", [2]),
    L("Güneş'in gazı sıradan bir gaz değildir: çok sıcak ve elektrik yüklüdür. Buna plazma denir.", [2]),
    L("Elektrik yüklü dev bir top... Kulağa hayalimdeki şarj istasyonu gibi geliyor!"),
    L("Peki yıldız neden parlar? Sır, çekirdeğinde saklı. Oradaki muazzam basınç ve sıcaklık, hidrojen atomlarının çekirdeklerini birbirine sıkıştırır.", [4]),
    L("Hidrojen çekirdekleri birleşir ve helyuma dönüşür. Bu olaya çekirdek kaynaşması, yani füzyon denir.", [4]),
    L("Füzyon enerji açığa çıkarır. Yıldızı ısıtan ve parlatan enerji budur.", [4]),
    L("Güneş'in çekirdeği yaklaşık 15 milyon santigrat derecedir. Yüzeyi ise 5.500 derece.", [5], "Güneş'in çekirdeği yaklaşık on beş milyon santigrat derecedir. Yüzeyi ise beş bin beş yüz derece."),
    L("Yıldızın içinde sürekli bir çekişme vardır: kütle çekimi içeri doğru bastırır, füzyonun yarattığı basınç dışarı doğru iter. Bu sayede yıldız çökmez.", [4]),
])
e.sec("finding", [
    L("Yıldızlar nasıl doğar? Uzayda moleküler bulut denen dev gaz ve toz bulutları vardır.", [3]),
    L("Kütle çekimi, bu bulutlardaki bazı topakların kendi üzerine çökmesine yol açar. Topak yüz binlerce yıl boyunca kütle kazanır, döner ve ısınır.", [3]),
    L("Sonunda bir önyıldız, yani bebek yıldız ortaya çıkar.", [3]),
    L("Çekirdeğinde hidrojeni helyuma dönüştüren yıldıza ana kol yıldızı denir. Güneş de bir ana kol yıldızıdır ve bu evrenin aşağı yukarı ortasındadır.", [7]),
    L("Güneş yaklaşık 4,6 milyar yıl önce oluştu. Bize uzaklığı yaklaşık 150 milyon kilometre.", [6], "Güneş yaklaşık dört virgül altı milyar yıl önce oluştu. Bize uzaklığı yaklaşık yüz elli milyon kilometre."),
    L("O kadar büyük ki içini doldurmak için 1,3 milyon Dünya gerekir!", [6], "O kadar büyük ki içini doldurmak için bir virgül üç milyon Dünya gerekir!"),
    L("Ama Güneş, yıldızların en büyüğü değil. Çapı Güneş'inkinin 1.000 katı olan yıldızlar bulundu. En küçük ana kol yıldızları ise kırmızı cücelerdir.", [8], "Ama Güneş, yıldızların en büyüğü değil. Çapı Güneş'inkinin bin katı olan yıldızlar bulundu. En küçük ana kol yıldızları ise kırmızı cücelerdir."),
    L("Bu sayıları hesaplarken işlemcim ısındı. Neyse ki Güneş'in çekirdeği kadar değil!"),
    L("Peki yıldızlar ölür mü? Evet, ama çok uzun sürer: bir yıldızın ömrü birkaç milyon yıldan trilyonlarca yıla kadar değişir.", [17]),
    L("Güneş yaklaşık 5 milyar yıl sonra şişerek bir kırmızı deve dönüşecek. O kadar büyüyecek ki Merkür'ü ve Venüs'ü yutacak.", [9], "Güneş yaklaşık beş milyar yıl sonra şişerek bir kırmızı deve dönüşecek. O kadar büyüyecek ki Merkür'ü ve Venüs'ü yutacak."),
])
e.sec("importance", [
    L("Sonra dış katmanları genişleyen bir gaz ve toz bulutuna dönüşecek; buna gezegenimsi bulutsu denir. Geriye kalan kalıntının adı ise beyaz cüce.", [10]),
    L("Çok daha büyük kütleli yıldızların sonu gürültülü olur: süpernova denen dev bir patlama!", [11]),
    L("Kütlesi Güneş'in 8–20 katı arasındaki yıldızlardan geriye nötron yıldızı kalır. Daha ağır olanlar ise kara deliğe dönüşür.", [11], "Kütlesi Güneş'in sekiz ile yirmi katı arasındaki yıldızlardan geriye nötron yıldızı kalır. Daha ağır olanlar ise kara deliğe dönüşür."),
    L("İşin en güzel yanı şu: yıldızlar birer element fabrikasıdır. Füzyon, karbonu oksijen gibi daha ağır elementlere dönüştürür; en büyük yıldızlarda zincir demire kadar sürer.", [12]),
    L("Süpernovalar bu maddeyi uzaya saçar ve yeni yıldızların doğacağı bulutları zenginleştirir.", [12]),
    L("Yani bendeki demir de bir zamanlar bir yıldızın içindeydi. Ben resmen yıldız yapımıyım!", [12]),
    L("Kaç yıldız var? Yalnızca Samanyolu'nda 100 milyardan fazla. Evrendeki sayı ise 1'in yanına 24 sıfır koyacak kadar olabilir.", [13], "Kaç yıldız var? Yalnızca Samanyolu'nda yüz milyardan fazla. Evrendeki sayı ise birin yanına yirmi dört sıfır koyacak kadar olabilir."),
    L("Güneş'ten sonra bize en yakın yıldız Proxima Centauri: 4,24 ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur.", [14], "Güneş'ten sonra bize en yakın yıldız Proksima Sentauri: dört virgül yirmi dört ışık yılı uzakta. Işık yılı, ışığın bir yılda aldığı yoldur."),
    L("Şimdi sıra sende! Açık bir gecede, bir büyüğünle birlikte ışıklardan uzak bir yerden gökyüzüne bak. Gece gökyüzünün en parlak yıldızı Sirius'u bulmayı dene.", [15]),
    L("Gördüğün yıldızların parlaklıklarını karşılaştır ve bir yıldız günlüğüne çiz. Hepsi aynı mı parlıyor?"),
    L("Bir uyarı: Güneş de bir yıldızdır ama ona asla doğrudan bakma!", [16]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Gece çıplak gözle görebildiğin yıldızların birçoğu, tıpkı Güneş gibi ana kol yıldızıdır.", [15]),
    L("Hızlı soru! Yıldızın çekirdeğinde hidrojeni helyuma dönüştüren olayın adı neydi?", [4]),
    L("Düşün bakalım... Evet: füzyon!", [4]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bu gece gökyüzüne bakarken beni de hatırla!"),
])
S = e.S
S(3, {"type": "hook", "question": "Yıldızlar neden parlar?", "emoji": "⭐"}, ["🌟", "🔭", "✨", "🌙"], ["", "YAKITI NE?", "YILDIZIN KALBİNE!"], fx="sparkle")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Yıldız nedir?", "Işığını nasıl üretir?", "Yıldızlar nasıl doğar, nasıl ölür?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Yıldız nedir?", "emoji": "⭐", "chips": [{"label": "Sıcak gazdan dev bir top", "emoji": "🔥"}, {"label": "Çoğunlukla hidrojen", "emoji": "🅷"}, {"label": "Biraz helyum", "emoji": "🎈"}]}, ["🌟", "✨"], ["DEV GAZ TOPU"])
S(3, {"type": "comparison", "title": "Güneş de bir yıldız", "left": {"title": "Güneş ☀️", "items": ["Hidrojen ve helyum topu", "Kütle çekimiyle bir arada durur"]}, "right": {"title": "Plazma ⚡", "items": ["Çok sıcak gaz", "Elektrik yüklü"]}}, ["☀️", "🔌"], ["EN YAKIN YILDIZ ☀️", "PLAZMA ⚡", "ŞARJ İSTASYONU! 🔌"])
S(3, {"type": "diagram", "title": "Füzyon: yıldızın motoru", "layout": "flow", "nodes": [{"label": "Dev basınç ve sıcaklık", "emoji": "🌡️"}, {"label": "Hidrojen çekirdekleri birleşir", "emoji": "🤝"}, {"label": "Helyum oluşur", "emoji": "🎈"}, {"label": "Enerji açığa çıkar", "emoji": "💥"}]}, ["⚛️", "✨"], ["ÇEKİRDEKTE", "FÜZYON ⚛️", "ENERJİ! 💥"], fx="sparkle")
S(1, {"type": "big-number", "value": "15 milyon", "unit": "°C", "label": "Güneş'in çekirdeği", "sub": "Yüzeyi: 5.500 °C", "icon": "🌡️"}, ["☀️", "🔥"], ["ÇOK SICAK! 🌡️"])
S(1, {"type": "comparison", "title": "Yıldızın dengesi", "left": {"title": "Kütle çekimi ⬇️", "items": ["İçeri doğru bastırır"]}, "right": {"title": "Füzyon basıncı ⬆️", "items": ["Dışarı doğru iter", "Yıldız çökmez"]}}, ["⚖️", "⭐"], ["DENGE ⚖️"])
S(3, {"type": "diagram", "title": "Bir yıldız doğuyor", "layout": "flow", "nodes": [{"label": "Moleküler bulut", "emoji": "☁️"}, {"label": "Topak çöker", "emoji": "🌀"}, {"label": "Döner ve ısınır", "emoji": "🔥"}, {"label": "Önyıldız", "emoji": "🌟"}]}, ["🌌", "✨"], ["MOLEKÜLER BULUT", "KÜTLE ÇEKİMİ", "BEBEK YILDIZ 🌟"], fx="sparkle")
S(2, {"type": "spotlight", "title": "Güneş'in kimliği", "emoji": "☀️", "chips": [{"label": "Ana kol yıldızı", "emoji": "⭐"}, {"label": "Evresinin ortasında", "emoji": "⏳"}, {"label": "Yaklaşık 4,6 milyar yaşında", "emoji": "🎂"}, {"label": "150 milyon km uzakta", "emoji": "📏"}]}, ["🌍", "🔭"], ["ANA KOL YILDIZI", "ORTA YAŞLI ☀️"])
S(1, {"type": "big-number", "value": "1,3 milyon", "unit": "Dünya", "label": "Güneş'in içini doldurmak için gereken", "sub": "NASA", "icon": "🌍"}, ["☀️", "📦"], ["KOCAMAN!"])
S(2, {"type": "comparison", "title": "Büyükler ve küçükler", "left": {"title": "Dev yıldızlar 🔴", "items": ["Çapı Güneş'in 1.000 katı olanlar var"]}, "right": {"title": "Kırmızı cüceler 🔻", "items": ["En küçük ana kol yıldızları"]}}, ["⭐", "🤖"], ["DEVLER VE CÜCELER", "İŞLEMCİM ISINDI 🥵"])
S(2, {"type": "bullets", "title": "Yıldızlar da ölür", "items": ["Ömür: birkaç milyon – trilyonlarca yıl", "Güneş: yaklaşık 5 milyar yıl sonra kırmızı dev", "Merkür'ü ve Venüs'ü yutacak"]}, ["⏳", "🔴"], ["ÇOK UZUN ÖMÜR ⏳", "KIRMIZI DEV 🔴"])
S(1, {"type": "diagram", "title": "Güneş'in sonu", "layout": "flow", "nodes": [{"label": "Kırmızı dev", "emoji": "🔴"}, {"label": "Gezegenimsi bulutsu", "emoji": "💨"}, {"label": "Beyaz cüce", "emoji": "⚪"}]}, ["☀️", "✨"], ["BEYAZ CÜCE ⚪"])
S(2, {"type": "spotlight", "title": "Dev yıldızların sonu", "emoji": "💥", "chips": [{"label": "Süpernova: dev patlama", "emoji": "💥"}, {"label": "8–20 Güneş kütlesi: nötron yıldızı", "emoji": "⚫"}, {"label": "Daha ağır: kara delik", "emoji": "🕳️"}]}, ["🌟", "⚡"], ["SÜPERNOVA! 💥", "KARA DELİK 🕳️"], fx="blackhole")
S(3, {"type": "diagram", "title": "Element fabrikası", "layout": "flow", "nodes": [{"label": "Karbon", "emoji": "⚫"}, {"label": "Oksijen, neon, magnezyum", "emoji": "🫧"}, {"label": "En büyüklerde: demir", "emoji": "🔩"}, {"label": "Süpernova uzaya saçar", "emoji": "💥"}]}, ["⚛️", "🤖"], ["ELEMENT FABRİKASI", "UZAYA SAÇILIR", "YILDIZ YAPIMI 🤖"])
S(1, {"type": "big-number", "value": "100 milyar+", "label": "Samanyolu'ndaki yıldız sayısı", "sub": "Evrende: 1'in yanına 24 sıfır kadar olabilir", "icon": "🌌"}, ["⭐", "🔭"], ["SAYISIZ YILDIZ"])
S(1, {"type": "spotlight", "title": "En yakın komşu", "emoji": "🔭", "chips": [{"label": "Proxima Centauri", "emoji": "🔻"}, {"label": "4,24 ışık yılı uzakta", "emoji": "📏"}, {"label": "Işık yılı: ışığın bir yılda aldığı yol", "emoji": "💡"}]}, ["⭐", "🚀"], ["IŞIK YILI"])
S(2, {"type": "bullets", "title": "Sen de dene: yıldız avı 🔭", "items": ["Açık bir gece, bir büyüğünle", "Işıklardan uzak bir yer", "Sirius'u bul: en parlak yıldız", "Yıldız günlüğüne çiz"]}, ["🌙", "📓"], ["YILDIZ AVI 🔭", "YILDIZ GÜNLÜĞÜ 📓"])
S(1, {"type": "spotlight", "title": "Uyarı", "emoji": "⚠️", "chips": [{"label": "Güneş'e asla doğrudan bakma!", "emoji": "🚫"}, {"label": "O da bir yıldız: çok parlak", "emoji": "☀️"}]}, ["🕶️", "☀️"], ["GÜNEŞ'E BAKMA! ⚠️"])
S(1, {"type": "big-number", "value": "Ana kol", "label": "Çıplak gözle görülen birçok yıldızın türü", "sub": "Tıpkı Güneş gibi", "icon": "⭐"}, ["🌟", "👀"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Hidrojeni helyuma dönüştüren olayın adı ne?", "emoji": "🤔"}, ["⚛️", "⭐"], ["HIZLI SORU!", "FÜZYON ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 13, "videoTitle": "Yıldızlar neden parlar?", "paperTitleTr": "Yıldızlar neden parlar?",
  "theme": {"backdrop": "space", "actors": [{"kind": "fly", "emoji": "🚀", "every": 19, "facesRight": True}, {"kind": "fly", "emoji": "🛸", "every": 31}, {"kind": "walk", "emoji": "🛰️", "every": 26}]},
  "takeaways": ["Yıldız, çekirdeğinde füzyon yapan dev bir gaz topudur", "Kütle çekimi ile füzyon basıncı yıldızı dengede tutar", "Yıldızlar doğar, ölür ve ağır elementleri üretir"],
  "description": "Yıldızlar neden parlar? Bu bölümde yıldızın ne olduğunu, plazmayı, çekirdekteki füzyonu ve yıldızı dengede tutan çekişmeyi; yıldızların moleküler bulutlardan nasıl doğduğunu, Güneş'in bir ana kol yıldızı olduğunu keşfediyoruz. Güneş'in sonu ne olacak, süpernova nedir, bendeki demir neden yıldız yapımı? Sonunda yıldız avı etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Hidrojen", "meaning": "Evrendeki en hafif element; yıldızların ana yakıtı."},
    {"term": "Plazma", "meaning": "Çok sıcak, elektrik yüklü gaz."},
    {"term": "Füzyon", "meaning": "Atom çekirdeklerinin birleşerek daha ağır bir çekirdek oluşturması ve enerji açığa çıkarması."},
    {"term": "Moleküler bulut", "meaning": "Yıldızların doğduğu dev gaz ve toz bulutu."},
    {"term": "Önyıldız", "meaning": "Henüz oluşmakta olan bebek yıldız."},
    {"term": "Ana kol yıldızı", "meaning": "Çekirdeğinde hidrojeni helyuma dönüştüren yıldız."},
    {"term": "Kırmızı dev", "meaning": "Ömrünün sonuna doğru şişip büyümüş yıldız."},
    {"term": "Süpernova", "meaning": "Büyük kütleli bir yıldızın dev patlaması."},
    {"term": "Işık yılı", "meaning": "Işığın bir yılda aldığı yol."}],
  "song": e.song("Yıldızın Kalbi", [("⭐", "Yıldız"), ("☀️", "Güneş"), ("⚛️", "Füzyon"), ("☁️", "Bulut"), ("💥", "Süpernova")],
    ["Gaz ve toz bulutu çöker içine", "Döner, ısınır, bir yıldız doğar", "Çekirdekte hidrojen birleşir", "Helyuma döner, enerji verir"],
    ["Füzyon, füzyon; yıldızın gücü!", "Çekim bastırır, basınç iter", "Denge sürdükçe yıldız parlar", "Güneş de bir yıldız, bize en yakın"],
    ["Küçükler sönünce beyaz cüce kalır", "Devler patlar, süpernova olur", "Karbon, oksijen, demir saçılır", "Yeni yıldızlara malzeme olur"],
    ["Füzyon, füzyon; yıldızın gücü!", "Çekim bastırır, basınç iter", "Gökyüzüne bak, yıldızları say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "⭐"}, {"kind": "hop", "emoji": "☀️"}, {"kind": "hop", "emoji": "🌟"}, {"kind": "hop", "emoji": "🪐"}, {"kind": "fly", "emoji": "🚀", "facesRight": True, "every": 7}, {"kind": "fly", "emoji": "☄️", "every": 11}])}
e.write(D, facts, script)
