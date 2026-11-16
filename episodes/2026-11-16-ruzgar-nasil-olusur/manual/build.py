"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:ruzgar-nasil-olusur"
NG = "National Geographic Education — Wind"; GC = "NOAA JetStream — Global Atmospheric Circulations"; SB = "NOAA JetStream — The Sea Breeze"; BF = "U.S. National Weather Service (Miami) — Beaufort Wind Scale"; DOE = "U.S. Department of Energy — Explore a Wind Turbine"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Wind", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/wind/"},
    {"id": "k2", "title": "Global Atmospheric Circulations", "publisher": "NOAA", "url": "https://www.noaa.gov/jetstream/global/global-atmospheric-circulations"},
    {"id": "k3", "title": "The Sea Breeze", "publisher": "NOAA", "url": "https://www.noaa.gov/jetstream/ocean/sea-breeze"},
    {"id": "k4", "title": "Beaufort Wind Scale", "publisher": "Ulusal Hava Servisi", "url": "https://www.weather.gov/mfl/beaufort"},
    {"id": "k5", "title": "Explore a Wind Turbine - Text Version", "publisher": "ABD Enerji Bakanlığı", "url": "https://www.energy.gov/eere/wind/how-wind-turbine-works-text-version"}],
  "facts": [
    F(1, "Rüzgâr, Dünya'nın Güneş tarafından eşit olmayan biçimde ısıtılmasından kaynaklanan hava hareketidir; göremez ya da tutamazsın ama kuvvetini hissedebilirsin.", "Wind is the movement of air caused by the uneven heating of the Earth by the sun. / It does not have much substance—you cannot see it or hold it—but you can feel its force.", NG),
    F(2, "Atmosfer basıncındaki farklar rüzgârı oluşturur; rüzgâr genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere eser.", "Differences in atmospheric pressure generate winds. / Winds generally blow from high-pressure areas to low-pressure areas.", NG),
    F(3, "Hava ısındıkça yoğunluğu azalır ve 'termal alçak' denen zayıf bir alçak basınç bölgesi oluşur.", "As the air warms, its density decreases, creating a weak low-pressure area called a \"thermal low\"", SB),
    F(4, "Ekvator'da Güneş suyu ve karayı dünyanın geri kalanından daha çok ısıtır; ılık ekvator havası atmosferde yükselir ve kutuplara doğru gider; daha serin, yoğun hava yeryüzünde Ekvator'a doğru ilerleyip ısınan havanın yerini alır.", "At the Equator, the sun warms the water and land more than it does the rest of the globe. / Warm equatorial air rises higher into the atmosphere and migrates toward the poles. / cooler, denser air moves over Earth's surface toward the Equator to replace the heated air.", NG),
    F(5, "Deniz meltemi gündüz, kara meltemi gece eser; gündüz ile gece arasındaki sıcaklık farkı karada denizdekinden çok daha büyüktür; gece kara sıcaklığı denizinkinin altına düşer.", "While sea breezes occur during the day, land breezes occur at night. / temperature fluctuations between daytime and nighttime are much greater over land than over water. / At night, the land temperature falls to below that of the ocean, resulting in an increase in the air's density.", SB),
    F(6, "Karadaki ılık hava yükselir ve sudaki serin hava karaya doğru ilerleyerek iç kesimlere esen bir meltem oluşturur.", "Warm air above the land rises, and cooler air above the water moves in over the land, creating an inland breeze.", NG),
    F(7, "Dünya'nın dönmesi havanın doğuya doğru sapmasına yol açar; buna Coriolis etkisi denir; her yarım kürede tek büyük dolaşım yerine üç dolaşım vardır.", "The Earth's rotation results in an easterly-movement of air, called the Coriolis effect / Instead of one large circulation in each hemisphere, there are three circulations in each:", GC),
    F(8, "Hâkim rüzgârlar genellikle kuzey-güney değil doğu-batı doğrultusunda eser; alize rüzgârları tropiklerde doğudan esen güçlü rüzgârlardır; batı rüzgârları orta enlemlerde batıdan eser.", "Generally, prevailing winds blow east-west rather than north-south. / Trade winds are the powerful prevailing winds that blow from the east across the tropics. / Westerlies are prevailing winds that blow from the west at midlatitudes.", NG),
    F(9, "Jet akımları üst atmosferde saatte 480 kilometreye kadar esebilen güçlü, hızlı rüzgârlardır.", "These strong, fast winds in the upper atmosphere can blow 480 kph (298 mph).", NG, ["480"]),
    F(10, "Anemometre rüzgâr hızını, rüzgâr gülü (yön göstergesi) rüzgârın yönünü ölçer.", "a device that measures wind speed. / The wind vane measures wind direction", NG + "; " + DOE),
    F(11, "Beaufort ölçeği 0'dan başlar ve 12'ye kadar gider; Amiral Sir Francis Beaufort ölçeği 1805'te denizcilerin rüzgârı gözle tahmin etmesine yardım etmek için geliştirdi.", "The scale starts with 0 and goes to a force of 12. / He developed the scale in 1805 to help sailors estimate the winds via visual observations.", BF, ["0", "12", "1805"]),
    F(12, "Beaufort 0: sakin, duman dümdüz yükselir; 3: yapraklar ve küçük dallar sürekli hareket eder, hafif bayrağı açar; 7: bütün ağaçlar sallanır, rüzgâra karşı yürümek zorlaşır; 10: ağaçlar kökünden sökülür.", "Calm; smoke rises vertically. / Leaves and small twigs in constant motion; wind extends light flag. / Whole trees in motion; inconvenience felt when walking against the wind. / trees uprooted; considerable structural damage occurs.", BF, ["0", "3", "7", "10"]),
    F(13, "Rüzgâr, doğrudan kirlilik yaratmayan yenilenebilir bir kaynaktır; rüzgâr kanatları çevirince kanatlar bir jeneratörü döndürür ve elektrik üretir; rüzgâr hızı yükseklikle arttığı için daha uzun kuleler daha çok enerji yakalar.", "Wind is a renewable resource that does not directly cause pollution. / When the wind turns the blades, the blades turn a generator and create electricity. / Because wind speed increases with height, taller towers enable turbines to capture more energy", NG + "; " + DOE),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyografik"; NO = "Noa"
e.sec("hook", [
    L("Saçlarını uçuran, uçurtmanı göğe çıkaran, ağaçları sallayan bir güç var. Ama onu hiç göremiyorsun!", [1]),
    L("Rüzgâr nereden gelir? Ve neden bazen hafif, bazen çok sert eser?"),
    L("Bugün görünmez havanın izini sürüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Rüzgârı ne oluşturur? Neden belirli yönlerde eser? Ve rüzgârı nasıl ölçeriz?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre rüzgâr, Güneş'in Dünya'yı eşit olmayan biçimde ısıtmasıyla oluşan hava hareketidir.", [1], f"{NGs}'e göre rüzgâr, Güneş'in Dünya'yı eşit olmayan biçimde ısıtmasıyla oluşan hava hareketidir."),
    L("Hava ısınınca yoğunluğu azalır ve yükselir. Yerinde alçak basınçlı bir bölge kalır.", [3, 4]),
    L("Rüzgâr ise genellikle yüksek basınçlı bölgelerden alçak basınçlı bölgelere doğru eser. Hava, boşluğu doldurmak için koşar!", [2]),
    L("Bu kadar koşuşturma bana da lazım. Ama ben rüzgârla değil, pille çalışıyorum!"),
    L("Bunu kıyıda her gün görebilirsin. NOAA'ya göre kara, gündüz ile gece arasında denizden çok daha fazla ısınıp soğur.", [5], f"Bunu kıyıda her gün görebilirsin. {NO}'ya göre kara, gündüz ile gece arasında denizden çok daha fazla ısınıp soğur."),
    L("Gündüz karadaki ılık hava yükselir; denizdeki serin hava karaya doğru akar. Buna deniz meltemi denir.", [5, 6]),
    L("Gece ise kara denizden daha çok soğur ve rüzgâr tersine döner: kara meltemi.", [5]),
])
e.sec("finding", [
    L("Aynı şey bütün dünyada olur. Ekvator, dünyanın geri kalanından daha çok ısınır.", [4]),
    L("Ekvator'daki ılık hava yükselir ve kutuplara doğru gider. Daha serin, yoğun hava da yeryüzünde Ekvator'a doğru akıp onun yerini alır.", [4]),
    L("Ama Dünya döner! Bu dönüş, havanın yolunu saptırır. Buna Coriolis etkisi denir.", [7], "Ama Dünya döner! Bu dönüş, havanın yolunu saptırır. Buna Koryolis etkisi denir."),
    L("Bu yüzden her yarım kürede tek büyük dolaşım yerine üç ayrı dolaşım oluşur.", [7]),
    L("Hâkim rüzgârlar da çoğunlukla doğu-batı yönünde eser. Tropiklerde doğudan esen güçlü rüzgârlara alize denir. Orta enlemlerde ise batı rüzgârları eser.", [8]),
    L("Yukarılarda daha da hızlıları var: jet akımları. Bu güçlü rüzgârlar saatte 480 kilometreye kadar esebilir!", [9], "Yukarılarda daha da hızlıları var: jet akımları. Bu güçlü rüzgârlar saatte dört yüz seksen kilometreye kadar esebilir!"),
])
e.sec("importance", [
    L("Peki rüzgârı nasıl ölçeriz? Hızını anemometre ölçer. Yönünü ise rüzgâr gülü gösterir.", [10]),
    L("Aletin yoksa gözlerin yeter! 1805'te Amiral Francis Beaufort, denizcilerin rüzgârı gözle tahmin etmesi için bir ölçek geliştirdi.", [11], "Aletin yoksa gözlerin yeter! Bin sekiz yüz beşte Amiral Frensis Bofort, denizcilerin rüzgârı gözle tahmin etmesi için bir ölçek geliştirdi."),
    L("Ölçek 0'dan 12'ye kadar gider. 0'da hava sakindir ve duman dümdüz yükselir.", [11, 12], "Ölçek sıfırdan on ikiye kadar gider. Sıfırda hava sakindir ve duman dümdüz yükselir."),
    L("3'te yapraklar ve ince dallar sürekli kıpırdar, hafif bir bayrak açılır. 7'de bütün ağaçlar sallanır ve rüzgâra karşı yürümek zorlaşır.", [12], "Üçte yapraklar ve ince dallar sürekli kıpırdar, hafif bir bayrak açılır. Yedide bütün ağaçlar sallanır ve rüzgâra karşı yürümek zorlaşır."),
    L("10'da ise ağaçlar kökünden sökülebilir. Böyle havalarda dışarı çıkmamak gerekir.", [12], "Onda ise ağaçlar kökünden sökülebilir. Böyle havalarda dışarı çıkmamak gerekir."),
    L("Rüzgâr bir enerji kaynağıdır da. Rüzgâr türbinlerinin kanatlarını çevirir; kanatlar bir jeneratörü döndürür ve elektrik üretilir.", [13]),
    L("Rüzgâr, doğrudan kirlilik yaratmayan, yenilenebilir bir kaynaktır. Yükseklerde daha hızlı estiği için türbin kuleleri uzun yapılır.", [13]),
    L("Şimdi sıra sende! Bir hafta boyunca her gün pencereden dışarı bak: ağaçlar, yapraklar, bayraklar ne yapıyor?", [12]),
    L("Beaufort ölçeğine göre o günün rüzgârına bir sayı ver ve tabloya yaz. En rüzgârlı gün hangisiydi?", [11]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Rüzgârı göremez ya da tutamazsın, ama kuvvetini her zaman hissedebilirsin.", [1]),
    L("Hızlı soru! Gündüz denizden karaya esen rüzgârın adı nedir?", [5, 6]),
    L("Düşün bakalım... Evet: deniz meltemi!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma."),
])
S = e.S
S(3, {"type": "hook", "question": "Rüzgâr nasıl oluşur?", "emoji": "🌬️"}, ["🪁", "🍃"], ["", "BAZEN HAFİF, BAZEN SERT", "GÖRÜNMEZ HAVA!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Rüzgârı ne oluşturur?", "Neden belirli yönlerde eser?", "Rüzgârı nasıl ölçeriz?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "diagram", "title": "Rüzgâr nasıl başlar?", "layout": "flow", "nodes": [{"label": "Güneş eşit ısıtmaz", "emoji": "☀️"}, {"label": "Ilık hava yükselir", "emoji": "⬆️"}, {"label": "Alçak basınç", "emoji": "🔵"}, {"label": "Hava yüksekten alçağa akar", "emoji": "🌬️"}]}, ["🌡️", "🍃"], ["EŞİT OLMAYAN ISINMA", "ALÇAK BASINÇ", "YÜKSEKTEN ALÇAĞA"])
S(1, {"type": "big-number", "value": "Pil", "label": "Muma rüzgârla değil, pille çalışır", "sub": "Ama koşuşturmayı sever", "icon": "🔋"}, ["🤖", "🍃"], ["PİLLE ÇALIŞIRIM 😅"])
S(3, {"type": "comparison", "title": "Kıyıda meltemler", "left": {"title": "Gündüz ☀️", "items": ["Kara çabuk ısınır", "Deniz meltemi: denizden karaya"]}, "right": {"title": "Gece 🌙", "items": ["Kara daha çok soğur", "Kara meltemi: karadan denize"]}}, ["🌊", "🏖️"], ["KARA VE DENİZ", "DENİZ MELTEMİ", "KARA MELTEMİ"])
S(2, {"type": "diagram", "title": "Dünya çapında dolaşım", "layout": "cycle", "nodes": [{"label": "Ekvator: ılık hava yükselir", "emoji": "☀️"}, {"label": "Kutuplara gider", "emoji": "❄️"}, {"label": "Serin hava geri akar", "emoji": "🌬️"}]}, ["🌍", "🧭"], ["EKVATOR EN SICAK", "BÜYÜK DOLAŞIM 🔄"])
S(2, {"type": "spotlight", "title": "Dönen Dünya", "emoji": "🌍", "chips": [{"label": "Coriolis etkisi", "emoji": "🌀"}, {"label": "Havanın yolu sapar", "emoji": "↪️"}, {"label": "Her yarım kürede üç dolaşım", "emoji": "🔄"}]}, ["🧭", "🔄"], ["CORIOLIS 🌀", "ÜÇ DOLAŞIM"])
S(2, {"type": "comparison", "title": "Hâkim rüzgârlar ve jet akımları", "left": {"title": "Alçakta 🌴", "items": ["Alize: tropiklerde doğudan", "Batı rüzgârları: orta enlemler"]}, "right": {"title": "Yüksekte ✈️", "items": ["Jet akımları", "Saatte 480 km'ye kadar"]}}, ["🌬️", "✈️"], ["ALİZE RÜZGÂRLARI", "JET AKIMI ✈️"])
S(2, {"type": "spotlight", "title": "Rüzgârı ölçmek", "emoji": "📏", "chips": [{"label": "Anemometre: hız", "emoji": "🌀"}, {"label": "Rüzgâr gülü: yön", "emoji": "🧭"}]}, ["🌬️", "📐"], ["ANEMOMETRE • RÜZGÂR GÜLÜ", "1805: BEAUFORT"])
S(3, {"type": "stages", "title": "Beaufort ölçeği", "rows": [{"label": "0: duman dümdüz yükselir", "emoji": "💨"}, {"label": "3: yapraklar kıpırdar", "emoji": "🍃"}, {"label": "7: ağaçlar sallanır", "emoji": "🌳"}, {"label": "10: ağaçlar sökülür", "emoji": "⚠️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 1, "note": "Şematik çizim: ölçek 0'dan 12'ye kadar gider."}, [], ["0'DAN 12'YE", "AĞAÇLAR SALLANIR", "DIŞARI ÇIKMA ⚠️"])
S(2, {"type": "diagram", "title": "Rüzgârdan elektrik", "layout": "flow", "nodes": [{"label": "Rüzgâr", "emoji": "🌬️"}, {"label": "Kanatlar döner", "emoji": "🌀"}, {"label": "Jeneratör", "emoji": "⚙️"}, {"label": "Elektrik", "emoji": "💡"}]}, ["🔋", "🏭"], ["RÜZGÂR TÜRBİNİ", "YENİLENEBİLİR ♻️"])
S(2, {"type": "bullets", "title": "Sen de dene: rüzgâr gözlemcisi", "items": ["Bir hafta, her gün pencereden bak", "Ağaç, yaprak, bayrak ne yapıyor?", "Beaufort sayısı ver", "En rüzgârlı gün hangisi?"]}, ["📓", "🪟"], ["DENEY ZAMANI 🔬", "TABLO TUT 📓"])
S(1, {"type": "big-number", "value": "Görünmez", "label": "Ama kuvvetini hep hissedersin", "sub": "National Geographic", "icon": "🌬️"}, ["🍃", "🪁"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Gündüz denizden karaya esen rüzgârın adı ne?", "emoji": "🤔"}, ["🌊", "🏖️"], ["HIZLI SORU!", "DENİZ MELTEMİ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 26, "videoTitle": "Rüzgâr nasıl oluşur?", "paperTitleTr": "Rüzgâr nasıl oluşur?",
  "theme": {"backdrop": "sky", "actors": [{"kind": "fly", "emoji": "🪁", "every": 26}]},
  "takeaways": ["Rüzgâr, Güneş'in Dünya'yı eşit ısıtmamasından doğar", "Hava yüksek basınçtan alçak basınca akar; Dünya'nın dönüşü yolunu saptırır", "Rüzgâr anemometreyle ve Beaufort ölçeğiyle ölçülür"],
  "description": "Göremediğimiz rüzgâr nereden gelir? Bu bölümde Güneş'in Dünya'yı eşit ısıtmamasını, ısınan havanın yükselmesini ve basınç farklarını; deniz ve kara meltemlerini, Ekvator'dan kutuplara uzanan dolaşımı, Coriolis etkisini, alize rüzgârlarını ve jet akımlarını keşfediyoruz. Rüzgârı nasıl ölçeriz, Beaufort ölçeği nedir, rüzgârdan nasıl elektrik üretilir? Sonunda rüzgâr gözlemcisi etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Hava basıncı", "meaning": "Havanın bir yüzeye uyguladığı itme."},
    {"term": "Yoğunluk", "meaning": "Bir maddenin belirli bir hacimdeki kütlesi; ılık hava daha az yoğundur."},
    {"term": "Meltem", "meaning": "Kıyıda kara ile deniz arasında esen hafif rüzgâr."},
    {"term": "Coriolis etkisi", "meaning": "Dünya'nın dönmesinin rüzgârların yolunu saptırması."},
    {"term": "Alize", "meaning": "Tropiklerde doğudan esen düzenli, güçlü rüzgâr."},
    {"term": "Jet akımı", "meaning": "Atmosferin üst kısmında esen çok hızlı rüzgâr."},
    {"term": "Anemometre", "meaning": "Rüzgâr hızını ölçen alet."},
    {"term": "Beaufort ölçeği", "meaning": "Rüzgârın gücünü 0'dan 12'ye kadar gözle tahmin etmeye yarayan ölçek."}],
  "song": e.song("Görünmez Koşucu", [("☀️", "Güneş"), ("🌬️", "Rüzgâr"), ("🌊", "Deniz"), ("🌍", "Dünya"), ("🌀", "Türbin")],
    ["Güneş ısıtır ama eşit değil", "Ilık hava yükselir, yer boşalır", "Yüksek basınçtan alçağa doğru", "Hava koşar, rüzgâr olur"],
    ["Es rüzgâr, es, görünmez koşucu!", "Gündüz denizden, gece karadan", "Ekvator ısınır, kutuplar üşür", "Dünya döner, yollar sapar"],
    ["Alize doğudan, batı rüzgârı batıdan", "Jet akımı yükseklerde hızlı", "Beaufort sıfırdan on ikiye sayar", "Türbin döner, ışık yanar"],
    ["Es rüzgâr, es, görünmez koşucu!", "Gündüz denizden, gece karadan", "Pencereden bak, ağaçları say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "fly", "emoji": "🪁", "every": 7, "size": 220}, {"kind": "fly", "emoji": "🍃", "every": 6}, {"kind": "hop", "emoji": "🌀"}, {"kind": "hop", "emoji": "⛵"}])}
e.write(D, facts, script)
