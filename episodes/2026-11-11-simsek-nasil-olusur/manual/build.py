"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:simsek-nasil-olusur"
NB = "NOAA NSSL — Severe Weather 101: Lightning Basics"; NF = "NOAA NSSL — Severe Weather 101: Lightning FAQ"; NT = "NOAA NSSL — Severe Weather 101: Lightning Types"
NG = "National Geographic Education — Lightning"; WS = "U.S. National Weather Service — Understanding Lightning Science"; WI = "U.S. National Weather Service — Lightning Indoors"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Severe Weather 101: Lightning Basics", "publisher": "NSSL", "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/"},
    {"id": "k2", "title": "Severe Weather 101: Lightning FAQ", "publisher": "NSSL", "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/faq/"},
    {"id": "k3", "title": "Severe Weather 101: Lightning Types", "publisher": "NSSL", "url": "https://www.nssl.noaa.gov/education/svrwx101/lightning/types/"},
    {"id": "k4", "title": "Lightning", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/lightning/"},
    {"id": "k5", "title": "Understanding Lightning Science", "publisher": "Ulusal Hava Servisi", "url": "https://www.weather.gov/safety/lightning-science-overview"},
    {"id": "k6", "title": "Lightning Indoors", "publisher": "Ulusal Hava Servisi", "url": "https://www.weather.gov/safety/lightning-indoors"}],
  "facts": [
    F(1, "Şimşek, atmosferde bulutlar, hava ya da yer arasında oluşan dev bir elektrik kıvılcımıdır.", "Lightning is a giant spark of electricity in the atmosphere between clouds, the air, or the ground.", NB),
    F(2, "Graupel denen küçük dolu taneleri daha küçük buz parçacıklarıyla çarpışınca yük kazanır; hafif buz kristalleri artı yüklenir ve yükselen havayla fırtınanın üst kısmına taşınır; ağır dolu eksi yüklenir.", "small hail particles called graupel / When these graupel particles collide and bounce off of smaller ice particles, the graupel gains one sign of charge / The lighter ice crystals become positively charged and are carried upward into the upper part of the storm by rising air. / The heavier hail becomes negatively charged", NB + "; " + WS),
    F(3, "Fırtına bulutunun ortasındaki eksi yük, altındaki yerin artı yüklenmesine yol açar.", "The negative charge in the middle of thunderstorm cloud causes the ground underneath to become positively charged", WS),
    F(4, "Hava, artı ve eksi yükler arasında yalıtkan görevi görür; zıt yükler yeterince birikince havanın yalıtma kapasitesi çöker. Zıt yükler birbirini çeker.", "air acts as an insulator between the positive and negative charges in the cloud / When the opposite charges build up enough, this insulating capacity of the air breaks down / Since opposites attract, an upward streamer is sent out from the object about to be struck.", NB + "; " + NF),
    F(5, "Bulutun elektrik yükünü tam olarak nasıl biriktirdiği ve şimşeğin nasıl oluştuğu hâlâ tartışılıyor.", "there is still debate about exactly how a cloud builds up electrical charges, and how lightning forms", NB),
    F(6, "Basamaklı öncü denen eksi yüklü kanal zikzak çizerek aşağı iner (göz kırpmaktan kısa sürede); yere yaklaşınca artı yüklü kanallar yukarı uzanır; iki yol buluşunca parlak dönüş darbesi buluta doğru geri gider.", "a channel of negative charge, called a stepped leader, will zigzag downward in roughly 50-yard segments / As it nears the ground, the negatively charged stepped leader causes streamer channels of positive charge to reach upward / When these two paths meet, a return stroke zips back up to the sky. / This return stroke current of bright luminosity / shoots to the ground in less time than it takes to blink.", NT + "; " + NF),
    F(7, "Bulutun içinde kalan şimşekler, yere inenlerin kabaca 5 ila 10 katıdır.", "There are roughly 5 to 10 times as many flashes that remain in the cloud as there are flashes which travel to the ground", NT, ["5", "10"]),
    F(8, "Şimşek havayı kısa süreliğine Güneş'in yüzeyinden çok daha sıcak hale getirir; sıcaklık 28.000 santigrat dereceye ulaşabilir.", "heats the air briefly to around 50,000 degrees Fahrenheit, much hotter than the surface of the sun / It can reach 28,000 degrees Celsius (50,000 degrees Fahrenheit).", NB + "; " + NG, ["28.000"]),
    F(9, "Şimşek 100 milyon ile 1 milyar volt arasında olabilir.", "Lightning can have 100 million to 1 billion volts, and contains billions of watts.", NF, ["100", "1"]),
    F(10, "Gök gürültüsü, büyük akımın hızla ısıttığı ve patlarcasına genleşen şimşek kanalından çıkan şok dalgasıyla başlar; hava hızla genleşir ve gök gürültüsü olarak duyduğumuz ses dalgasını yaratır.", "Thunder starts as a shockwave from the explosively expanding lightning channel when a large current causes rapid heating. / This causes the air to expand rapidly and creates the sound wave we hear as thunder.", NF + "; " + WS),
    F(11, "Işık havada sesten kabaca bir milyon kat hızlı ilerler; bu yüzden şimşek gök gürültüsünden önce görülür.", "Because light travels through the air roughly a million times faster than sound does / Since light travels much, much, faster than sound, you'll see lightning before you hear thunder.", NB + "; " + NG),
    F(12, "Saniye sayısını 5'e bölmek şimşeğe olan uzaklığı mil olarak verir (3'e bölmek kilometre olarak).", "dividing the number of seconds by 5 gives the number of miles to the flash (while dividing by 3 gives the number of kilometers)", NB, ["5", "3"]),
    F(13, "Gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin; güvenli bir yere gir.", "If you hear thunder—even a distant rumble—you are already in danger of becoming a lightning victim. / If you hear thunder, the storm is nearby. Go inside a safe place.", WS + "; " + NG),
    F(14, "Güvenli sığınaklar elektrik ve su tesisatı olan binalar ya da camları kapalı, metal tavanlı araçlardır.", "Safe shelters are buildings with electricity and plumbing or metal-topped vehicles with the windows closed.", WI),
    F(15, "İçeride kablolu telefonlardan ve su tesisatından uzak durulmalıdır.", "Stay off corded phones. You can use cellular or cordless phones. / Avoid plumbing. Do not wash your hands, take a shower or wash dishes.", WI),
    F(16, "Açık alanlardan ve ağaç gibi yüksek nesnelerden uzak durulmalı; yüzülüyorsa havuzdan çıkılmalıdır.", "Stay away from open areas, like fields, and tall objects, like trees or telephone poles. / Since water is a great conductor of electricity, you should get out of a pool if you're swimming", NG),
    F(17, "Şimşek, halk arasındaki inanışın tersine aynı noktaya birden çok kez düşer.", "Lightning does hit the same spot (or almost the same spot) more than once, contrary to folk wisdom.", NF),
    F(18, "Ayaklarını halıya sürtüp metal kapı koluna dokununca hissedilen çarpma statik elektriktir; bu, fırtına bulutundaki olayın daha az tehlikeli bir halidir.", "Rub your feet on a carpet, then touch a metal doorknob. Do you feel a shock? That's static electricity. / a less-dangerous version of the negative charges in a thundercloud attracting the positive charge", NG),
    F(19, "New York'taki Empire State Binası'na her yıl yaklaşık 100 kez yıldırım düşer.", "Lightning strikes the iconic American Empire State Building in New York City about 100 times every year.", NG, ["100"]),
]}
e = Ep(); L = e.L
NS = "En Es Es El"; NGs = "Neşınıl Ciyografik"
e.sec("hook", [
    L("Gökyüzü bir anda aydınlanıyor. Birkaç saniye sonra da yeri göğü sarsan bir gürültü geliyor!"),
    L("Bu dev kıvılcım nasıl oluşuyor? Ve gürültü neden hep sonradan geliyor?"),
    L("Bugün bir fırtına bulutunun içine giriyoruz!"),
])
e.sec("context", [
    L("Elektriği severim, o benim yemeğim. Ama bu kadarı bana bile fazla!"),
    L("Üç sorumuz var. Bir bulut nasıl elektriklenir? Şimşek nasıl çakar? Ve gök gürültüsü nedir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Ulusal Şiddetli Fırtınalar Laboratuvarı, kısaca NSSL'ye göre şimşek, atmosferdeki dev bir elektrik kıvılcımıdır. Bulutlar, hava ya da yer arasında oluşur.", [1], f"A Be De Ulusal Şiddetli Fırtınalar Laboratuvarı, kısaca {NS}'e göre şimşek, atmosferdeki dev bir elektrik kıvılcımıdır. Bulutlar, hava ya da yer arasında oluşur."),
    L("Küçük bir örneğini sen de yaşadın. National Geographic'e göre ayaklarını halıya sürtüp metal kapı koluna dokununca hissettiğin çarpma, statik elektriktir.", [18], f"Küçük bir örneğini sen de yaşadın. {NGs}'e göre ayaklarını halıya sürtüp metal kapı koluna dokununca hissettiğin çarpma, statik elektriktir."),
    L("Fırtına bulutunun içinde graupel denen küçük dolu taneleri ve daha da küçük buz kristalleri vardır.", [2]),
    L("Bunlar birbirine çarptıkça elektrik yükü kazanır.", [2]),
    L("ABD Ulusal Hava Servisi'ne göre hafif buz kristalleri artı yüklenir ve yükselen havayla bulutun tepesine taşınır. Ağır dolu taneleri ise eksi yüklenir.", [2], "A Be De Ulusal Hava Servisi'ne göre hafif buz kristalleri artı yüklenir ve yükselen havayla bulutun tepesine taşınır. Ağır dolu taneleri ise eksi yüklenir."),
    L("Böylece bulut dev bir pile benzer: üstü artı, ortası eksi.", [2, 3]),
    L("Buluttaki eksi yük, altındaki yerin artı yüklenmesine yol açar.", [3]),
    L("Zıt yükler birbirini çeker. Ama aralarında hava var ve hava bir yalıtkandır: elektriği kolay geçirmez.", [4]),
])
e.sec("finding", [
    L("Yükler yeterince birikince havanın yalıtma gücü çöker. İşte o an şimşek çakar!", [4]),
    L("Buluttan yere inen şimşeğe yıldırım denir. Onu ağır çekimde izleyelim. Önce buluttan aşağı, zikzaklar çizen eksi yüklü bir kanal iner. Adı: basamaklı öncü.", [6]),
    L("Öncü yere yaklaşınca, yerden yukarı doğru artı yüklü kanallar uzanır.", [6]),
    L("İkisi buluştuğu anda parlak bir akım göğe doğru geri fırlar. Bizim gördüğümüz ışık budur: dönüş darbesi.", [6]),
    L("Öncünün yere inmesi, göz kırpmaktan bile kısa sürer.", [6]),
    L("Üstelik şimşeklerin çoğu yere hiç inmez: bulutun içinde kalanlar, yere inenlerin kabaca 5–10 katıdır.", [7], "Üstelik şimşeklerin çoğu yere hiç inmez: bulutun içinde kalanlar, yere inenlerin kabaca beş ile on katıdır."),
    L("Peki ne kadar güçlü? Bir şimşek 100 milyon ile 1 milyar volt arasında olabilir.", [9], "Peki ne kadar güçlü? Bir şimşek yüz milyon ile bir milyar volt arasında olabilir."),
    L("Benim şarj aletim bunun yanında oyuncak kalır!"),
    L("Şimşek, çevresindeki havayı bir anda 28.000 santigrat dereceye kadar ısıtabilir. Bu, Güneş'in yüzeyinden çok daha sıcaktır!", [8], "Şimşek, çevresindeki havayı bir anda yirmi sekiz bin santigrat dereceye kadar ısıtabilir. Bu, Güneş'in yüzeyinden çok daha sıcaktır!"),
    L("Bu kadar hızlı ısınan hava patlarcasına genleşir ve bir şok dalgası oluşturur. Bu dalga ses olarak yayılır: işte gök gürültüsü!", [10]),
])
e.sec("importance", [
    L("Peki neden önce ışığı görüp sonra sesi duyuyoruz? Çünkü ışık havada sesten kabaca bir milyon kat hızlı yol alır.", [11]),
    L("Bunu bir uzaklık ölçere çevirebilirsin. Şimşeği görünce saymaya başla, gürültüyü duyunca dur.", [12]),
    L("Saydığın saniyeyi 3'e böl: şimşek kabaca o kadar kilometre uzakta.", [12], "Saydığın saniyeyi üçe böl: şimşek kabaca o kadar kilometre uzakta."),
    L("Ben bu hesabı çok hızlı yaparım. Ne de olsa içimde bir hesap makinesi var!"),
    L("Yıldırım aynı yere iki kez düşmez derler. Bu doğru değil! Aynı yere birden çok kez düşebilir.", [17]),
    L("National Geographic'e göre New York'taki Empire State Binası'na her yıl yaklaşık 100 kez yıldırım düşer.", [19], f"{NGs}'e göre Nyu York'taki Empayır Steyt Binası'na her yıl yaklaşık yüz kez yıldırım düşer."),
    L("Şimdi güvenlik. Ulusal Hava Servisi'ne göre gök gürültüsünü duyuyorsan, uzaktan bile olsa, tehlikedesin demektir. Hemen güvenli bir yere gir.", [13]),
    L("Güvenli yer: elektrik ve su tesisatı olan bir bina ya da camları kapalı, metal tavanlı bir araç.", [14]),
    L("Dışarıdaysan açık alanlardan ve ağaç gibi yüksek şeylerden uzak dur. Yüzüyorsan sudan çık.", [16]),
    L("İçerideyken de kablolu telefonu kullanma ve musluklardan uzak dur.", [15]),
    L("Şimdi sıra sende! Bir sonraki fırtınada, evin içinden şimşeği izle ve saniyeleri say.", [12]),
    L("Sayı küçülüyorsa fırtına yaklaşıyor, büyüyorsa uzaklaşıyor demektir.", [12]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Bulutun tam olarak nasıl elektriklendiği ve şimşeğin nasıl başladığı, bilim insanları arasında hâlâ tartışılıyor.", [5]),
    L("Hızlı soru! Hangisi daha hızlı: ışık mı, ses mi?", [11]),
    L("Düşün bakalım... Evet: ışık!", [11]),
    L("Ben de hızlıyım ama. Özellikle şarjım biterken prize koşarken!"),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben prizime dönüyorum; küçük kıvılcımlar bana yeter!"),
])
S = e.S
S(3, {"type": "hook", "question": "Şimşek nasıl çakar?", "emoji": "⚡"}, ["⛈️", "🌩️", "🔊", "☔"], ["", "GÜRÜLTÜ NEDEN SONRA?", "BULUTUN İÇİNE!"])
S(1, {"type": "spotlight", "title": "Elektrik: robot yemeği", "emoji": "🤖", "chips": [{"label": "Severim", "emoji": "🔌"}, {"label": "Ama bu kadarı fazla!", "emoji": "⚡"}, {"label": "Küçük porsiyon lütfen", "emoji": "🔋"}]}, ["🔋", "😅"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Bir bulut nasıl elektriklenir?", "Şimşek nasıl çakar?", "Gök gürültüsü nedir?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Şimşek nedir?", "emoji": "⚡", "chips": [{"label": "Dev bir elektrik kıvılcımı", "emoji": "✨"}, {"label": "Bulutlar arasında", "emoji": "☁️"}, {"label": "Bulut ile hava arasında", "emoji": "🌬️"}, {"label": "Bulut ile yer arasında", "emoji": "🌍"}]}, ["⛈️", "🌩️"], ["DEV KIVILCIM ⚡"])
S(1, {"type": "diagram", "title": "Küçük örneği: statik elektrik", "layout": "flow", "nodes": [{"label": "Ayaklarını halıya sürt", "emoji": "🧦"}, {"label": "Metal kapı koluna dokun", "emoji": "🚪"}, {"label": "Çat! Statik elektrik", "emoji": "⚡"}]}, ["🧶", "✨"], ["STATİK ELEKTRİK"])
S(2, {"type": "spotlight", "title": "Fırtına bulutunun içinde", "emoji": "⛈️", "chips": [{"label": "Graupel: küçük dolu taneleri", "emoji": "⚪"}, {"label": "Buz kristalleri", "emoji": "❄️"}, {"label": "Çarpışırlar", "emoji": "💥"}, {"label": "Elektrik yükü kazanırlar", "emoji": "⚡"}]}, ["🧊", "🌬️"], ["GRAUPEL + BUZ", "ÇARPIŞMA → YÜK"])
S(2, {"type": "comparison", "title": "Bulut: dev bir pil", "left": {"title": "Üst kısım ➕", "items": ["Hafif buz kristalleri", "Artı yük", "Yükselen hava taşır"]}, "right": {"title": "Orta kısım ➖", "items": ["Ağır dolu taneleri", "Eksi yük"]}}, ["🔋", "☁️"], ["ARTI ➕ / EKSİ ➖", "DEV PİL 🔋"])
S(2, {"type": "diagram", "title": "Bulut ile yer arasında", "layout": "flow", "nodes": [{"label": "Bulut: eksi yük", "emoji": "➖"}, {"label": "Hava: yalıtkan", "emoji": "🧱"}, {"label": "Yer: artı yük", "emoji": "➕"}]}, ["☁️", "🌍"], ["YER ARTI YÜKLENİR", "HAVA = YALITKAN"])
S(1, {"type": "big-number", "value": "Çat!", "label": "Havanın yalıtma gücü çöker", "sub": "Yükler yeterince birikince", "icon": "⚡"}, ["⛈️", "💥"], ["ŞİMŞEK ÇAKAR!"])
S(3, {"type": "diagram", "title": "Yıldırım: ağır çekim", "layout": "flow", "nodes": [{"label": "Basamaklı öncü iner", "emoji": "⬇️"}, {"label": "Yerden artı kanallar uzanır", "emoji": "⬆️"}, {"label": "Buluşma", "emoji": "🤝"}, {"label": "Dönüş darbesi: parlak ışık", "emoji": "⚡"}]}, ["☁️", "🌍"], ["BASAMAKLI ÖNCÜ", "YERDEN YUKARI ⬆️", "DÖNÜŞ DARBESİ ⚡"])
S(2, {"type": "bullets", "title": "Göz açıp kapayıncaya kadar", "items": ["Öncünün inişi göz kırpmaktan kısa sürer", "Bulutta kalan şimşekler: yere inenlerin 5–10 katı"]}, ["👁️", "☁️"], ["GÖZ KIRPMADAN!", "ÇOĞU BULUTTA KALIR"])
S(2, {"type": "big-number", "value": "1 milyar", "unit": "volt", "label": "Bir şimşeğin gerilimi", "sub": "100 milyon ile 1 milyar volt arası", "icon": "🔌"}, ["🔋", "⚡"], ["NE KADAR GÜÇLÜ?", "ŞARJ ALETİM = OYUNCAK 😅"])
S(1, {"type": "spotlight", "title": "Güneş'in yüzeyinden sıcak!", "emoji": "🌡️", "chips": [{"label": "Hava 28.000 °C'ye kadar ısınabilir", "emoji": "🔥"}, {"label": "Güneş'in yüzeyinden çok daha sıcak", "emoji": "☀️"}]}, ["⚡", "🔥"], ["ÇOK SICAK! 🌡️"])
S(1, {"type": "diagram", "title": "Gök gürültüsü nasıl oluşur?", "layout": "flow", "nodes": [{"label": "Hava aniden ısınır", "emoji": "🔥"}, {"label": "Patlarcasına genleşir", "emoji": "💥"}, {"label": "Şok dalgası", "emoji": "〰️"}, {"label": "Ses: gök gürültüsü", "emoji": "🔊"}]}, ["⚡", "👂"], ["GÖK GÜRÜLTÜSÜ 🔊"])
S(1, {"type": "comparison", "title": "Işık mı, ses mi?", "left": {"title": "Işık ⚡", "items": ["Kabaca bir milyon kat hızlı", "Hemen görürsün"]}, "right": {"title": "Ses 🔊", "items": ["Çok daha yavaş", "Sonradan duyarsın"]}}, ["👁️", "👂"], ["IŞIK ÖNDE!"])
S(3, {"type": "big-number", "value": "÷ 3", "label": "Saniye ÷ 3 = kilometre", "sub": "Şimşeği gör, say; gürültüyü duyunca dur", "icon": "⏱️"}, ["⚡", "🔊", "🧮"], ["SAYMAYA BAŞLA ⏱️", "ÜÇE BÖL", "HESAP MAKİNESİ 🧮"])
S(2, {"type": "spotlight", "title": "Aynı yere iki kez?", "emoji": "🏙️", "chips": [{"label": "İnanış: iki kez düşmez", "emoji": "❌"}, {"label": "Gerçek: birden çok kez düşebilir", "emoji": "✅"}, {"label": "Empire State: yılda yaklaşık 100 kez", "emoji": "🏢"}]}, ["⚡", "🗽"], ["DOĞRU DEĞİL! ❌", "EMPIRE STATE 🏢"])
S(2, {"type": "bullets", "title": "Gök gürültüsünü duyunca", "items": ["Hemen güvenli bir yere gir", "Bina: elektrik ve su tesisatı olan", "Araç: metal tavanlı, camları kapalı"], "tone": "caution"}, ["🏠", "🚗"], ["İÇERİ GİR! 🏠", "GÜVENLİ YER"])
S(2, {"type": "comparison", "title": "Güvenlik kuralları", "left": {"title": "Dışarıda 🌳", "items": ["Açık alandan uzak dur", "Ağaçlardan uzak dur", "Sudan çık"]}, "right": {"title": "İçeride 🏠", "items": ["Kablolu telefonu kullanma", "Musluklardan uzak dur"]}}, ["⚠️", "🚿"], ["AĞAÇTAN UZAK 🌳", "MUSLUKTAN UZAK 🚿"])
S(2, {"type": "diagram", "title": "Sen de dene: fırtına ölçer", "layout": "flow", "nodes": [{"label": "Evin içinden izle", "emoji": "🏠"}, {"label": "Şimşek: saymaya başla", "emoji": "⚡"}, {"label": "Gürültü: dur", "emoji": "🔊"}, {"label": "Sayı küçülüyor mu?", "emoji": "📉"}]}, ["⏱️", "📓"], ["DENEY ZAMANI 🔬", "YAKLAŞIYOR MU?"])
S(1, {"type": "spotlight", "title": "Hâlâ araştırılıyor", "emoji": "🔬", "chips": [{"label": "Bulut tam olarak nasıl elektriklenir?", "emoji": "☁️"}, {"label": "Şimşek nasıl başlar?", "emoji": "⚡"}, {"label": "Bilim insanları tartışıyor", "emoji": "🧑‍🔬"}]}, ["❓", "📚"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Hangisi daha hızlı: ışık mı, ses mi?", "emoji": "🤔"}, ["⚡", "🔊"], ["HIZLI SORU!", "IŞIK ✅", ""])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 6, "videoTitle": "Şimşek nasıl oluşur?", "paperTitleTr": "Şimşek nasıl oluşur?",
  "takeaways": ["Bulutta çarpışan buz taneleri elektrik yükü biriktirir", "Havanın yalıtımı çökünce şimşek çakar; ısınan hava gürler", "Gök gürültüsünü duyunca güvenli bir yere girilir"],
  "description": "Şimşek nasıl çakar, gök gürültüsü neden sonradan gelir? Bu bölümde fırtına bulutunun nasıl elektriklendiğini, graupel ve buz kristallerini, basamaklı öncüyü ve dönüş darbesini; şimşeğin sıcaklığını ve gerilimini keşfediyoruz. Saniyeleri sayarak fırtınanın uzaklığı nasıl bulunur, yıldırımdan nasıl korunulur? Sonunda fırtına ölçer etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Statik elektrik", "meaning": "Bir cisimde biriken elektrik yükü; kapı koluna dokununca hissedilen küçük çarpma."},
    {"term": "Graupel", "meaning": "Fırtına bulutundaki küçük dolu taneleri."},
    {"term": "Elektrik yükü", "meaning": "Maddenin artı ya da eksi olabilen elektriksel özelliği; zıt yükler birbirini çeker."},
    {"term": "Yalıtkan", "meaning": "Elektriği kolay geçirmeyen madde."},
    {"term": "Yıldırım", "meaning": "Buluttan yere inen şimşek."},
    {"term": "Basamaklı öncü", "meaning": "Buluttan aşağı zikzak çizerek inen, eksi yüklü ilk kanal."},
    {"term": "Dönüş darbesi", "meaning": "Öncü ile yerden çıkan kanal buluşunca göğe doğru akan parlak akım."},
    {"term": "Şok dalgası", "meaning": "Havanın aniden genleşmesiyle oluşan güçlü basınç dalgası."}],
  "song": e.song("Bulutun Kıvılcımı", [("⛈️", "Bulut"), ("⚡", "Şimşek"), ("❄️", "Buz kristali"), ("🔊", "Gök gürültüsü"), ("🏠", "Güvenli yer")],
    ["Bulutun içinde buzlar çarpışır", "Hafifler yukarı artı taşır", "Ağır taneler eksiyle dolar", "Hava yalıtkan, arada durur"],
    ["Çat! Şimşek çakar, gök aydınlanır", "Hava genleşir, gürültü yayılır", "Önce ışık gelir, sonra ses", "Say saniyeyi, üçe böl, hesapla!"],
    ["Öncü iner zikzak çizerek", "Yerden kanal çıkar yükselerek", "Buluşunca döner parlak darbe", "Güneş'ten sıcak olur hava bile"],
    ["Çat! Şimşek çakar, gök aydınlanır", "Hava genleşir, gürültü yayılır", "Gürültüyü duyunca içeri gir", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
