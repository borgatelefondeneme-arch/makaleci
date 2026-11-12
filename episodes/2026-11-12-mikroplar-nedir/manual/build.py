"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:mikroplar-nedir"
K1 = "Nemours KidsHealth — Fighting Germs"; K2 = "Nemours KidsHealth — Immune System"; C1 = "CDC — About Handwashing"; N1 = "NHS — How to wash your hands"
G1 = "NIH (NHGRI) — Genetics Glossary: Bacteria"; G2 = "NIH (NHGRI) — Genetics Glossary: Virus"; A1 = "CDC — About Antimicrobial Resistance"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Fighting Germs", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/germs.html"},
    {"id": "k2", "title": "Immune System", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/immune.html"},
    {"id": "k3", "title": "About Handwashing", "publisher": "CDC", "url": "https://www.cdc.gov/clean-hands/about/index.html"},
    {"id": "k4", "title": "How to wash your hands", "publisher": "NHS", "url": "https://www.nhs.uk/live-well/healthy-body/best-way-to-wash-your-hands/"},
    {"id": "k5", "title": "Genetics Glossary: Bacteria", "publisher": "NIH", "url": "https://www.genome.gov/genetics-glossary/Bacteria"},
    {"id": "k6", "title": "Genetics Glossary: Virus", "publisher": "NIH", "url": "https://www.genome.gov/genetics-glossary/Virus"},
    {"id": "k7", "title": "About Antimicrobial Resistance", "publisher": "CDC", "url": "https://www.cdc.gov/antimicrobial-resistance/about/index.html"}],
  "facts": [
    F(1, "'Mikrop' sözcüğü hastalığa yol açabilen mikroskobik bakterileri, virüsleri, mantarları ve protozoaları anlatır.", "The term \"germs\" refers to the microscopic bacteria, viruses, fungi, and protozoa that can cause disease.", K1),
    F(2, "Mikropların çoğu zararsızdır, hatta insanlara yararlıdır; enfeksiyona yol açanlara patojen denir.", "Pathogens are germs that cause infections. Most germs are harmless and even helpful to people.", A1),
    F(3, "Bakteriler küçük, tek hücreli canlılardır; insan vücudu bakteriyle doludur ve insan hücresinden daha çok bakteri hücresi içerdiği tahmin edilir; vücuttaki bakterilerin çoğu zararsız, bazıları yararlıdır; görece az sayıda tür hastalık yapar.", "Bacteria are small single-celled organisms. / The human body is full of bacteria, and in fact is estimated to contain more bacterial cells than human cells. / Most bacteria in the body are harmless, and some are even helpful. / A relatively small number of species cause disease.", G1),
    F(4, "Bakteriler küre, çubuk ya da sarmal biçiminde olabilir; sindirim sistemimizdeki bakteriler vücudumuzun normal çalışması için gereklidir.", "They can be spheres, they can be rods, or they can be spirals. / in our digestive system, in the gut, we have bacteria that are very necessary to help our bodies function in a normal way.", G1),
    F(5, "Virüs, bir protein kılıfla çevrili bir nükleik asit (DNA ya da RNA) parçasından oluşan bulaşıcı bir mikroptur; tek başına çoğalamaz, hücreleri enfekte edip konak hücrenin parçalarıyla kendini kopyalar; çoğu zaman bu sırada konak hücreyi öldürür.", "A virus is an infectious microbe consisting of a segment of nucleic acid (either DNA or RNA) surrounded by a protein coat. / A virus cannot replicate alone; instead, it must infect cells and use components of the host cell to make copies of itself. / Often, a virus ends up killing the host cell in the process", G2),
    F(6, "Mikropların çoğu hapşırık ve öksürükle havadan ya da ter ve tükürük gibi vücut sıvılarıyla yayılır; yıkanmamış ellerle göze, buruna ve ağza dokunmak, ellere hapşırıp başkalarının ellerine ya da ortak eşyalara dokunmak mikropları yayar.", "Most germs spread through the air in sneezes or coughs or through body fluids like sweat, saliva (spit), / Touch your eyes, nose, and mouth with unwashed hands / Blow your nose, cough, or sneeze into hands and then touch other people's hands or common objects", K1 + "; " + C1),
    F(7, "Bağışıklık sistemi vücudun enfeksiyonlara karşı savunmasıdır; deri, mikropların vücuda girmesini engelleyen bir engel görevi görür.", "The immune system is the body's defense against infections. / For example, the skin acts as a barrier to block germs from entering the body.", K2),
    F(8, "Akyuvarlar (lökositler) bağışıklıkta önemli rol oynar: fagositler istilacı canlıları yer; lenfositler vücudun istilacıları hatırlamasına ve yok etmesine yardım eder; T hücreleri asker gibidir; B lenfositleri antikor yapar.", "White blood cells, also called leukocytes (pronounced: LOO-kuh-sytes), play an important role in the immune system. / phagocytes (pronounced: FAH-guh-sytes), chew up invading organisms. / lymphocytes (pronounced: LIM-fuh-sytes), help the body remember the invaders and destroy them. / T cells are like the soldiers / B lymphocytes are triggered to make antibodies", K2),
    F(9, "Antikorlar yapıldıktan sonra aynı mikropla yeniden savaşmak gerekirse diye genellikle vücutta kalır; bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.", "After they're made, antibodies usually stay in our bodies in case we have to fight the same germ again. / That's why someone who gets sick with a disease, like chickenpox, usually won't get sick from it again.", K2),
    F(10, "Aşılar hastalığa yol açan mikrobun ölü ya da zayıflatılmış hâlini (ya da parçalarını) içerir; bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar yapar.", "Vaccines contain either a dead or a weakened germ (or parts of it) that causes a particular disease. / When someone gets a vaccine, their immune system acts as if there's a real infection. / It makes antibodies that recognize parts of that germ.", K1),
    F(11, "Antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez; antimikrobiyal direnç, mikropların kendilerini öldürmek için tasarlanan ilaçları yenme yeteneği kazanmasıdır; bu, vücudun antibiyotiğe dirençli olduğu anlamına gelmez.", "Antibiotics and antifungals do not work on viruses, such as colds and the flu. / Antimicrobial resistance (AR) happens when germs develop the ability to defeat the drugs designed to kill them. / It does NOT mean your body is resistant to antibiotics or antifungals.", A1),
    F(12, "Elleri temiz akan suyla ıslat, sabunla köpürt, en az 20 saniye ov (Doğum Günü şarkısını baştan sona iki kez), temiz suyla durula ve temiz havluyla kurula. Çoğu durumda mikroplardan kurtulmanın en iyi yolu sabun ve suyla yıkamaktır.", "Wet your hands with clean, running water (warm or cold), turn off the tap, and apply soap. / Scrub your hands for at least 20 seconds. Need a timer? Hum the \"Happy Birthday\" song from beginning to end twice. / Rinse your hands well under clean, running water. / Washing hands with soap and water is the best way to get rid of germs in most situations.", C1, ["20"]),
    F(13, "Burnu sildikten, öksürdükten ya da hapşırdıktan sonra, yemek hazırlamadan önce ve sonra, tuvaletten sonra eller yıkanmalıdır; el yıkamak solunum ve ishal enfeksiyonlarının yayılmasını önleyebilir.", "After blowing your nose, coughing, or sneezing / Before and after preparing food / After using the toilet / Washing hands can keep you healthy and prevent the spread of respiratory and diarrheal infections.", C1),
    F(14, "Hapşırırken ya da öksürürken ağzını ve burnunu mendille kapat ve mendili at; mendil yoksa eline değil dirseğine hapşır.", "If you sneeze or cough, cover your mouth and nose with a tissue, and then throw it out. / If you don't have a tissue, sneeze or cough into your elbow, not your hands.", K1),
]}
e = Ep(); L = e.L
KH = "Kids Helt"; CD = "Si Di Si"; EN = "En Ay Eyç"
e.sec("hook", [
    L("Şu an ellerinde, gözle göremeyeceğin kadar küçük canlılar var. Bazıları dost, bazıları düşman!", [1, 2]),
    L("Bu küçük canlılar kim? Ve vücudun düşmanları nasıl tanıyıp yeniyor?"),
    L("Bugün mikroskobun altına bakıyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Mikrop nedir? Vücudumuz kendini nasıl savunur? Ve mikroplardan nasıl korunuruz?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre mikrop dediğimiz şey; bakteriler, virüsler, mantarlar ve protozoalar gibi mikroskobik canlılardır.", [1], f"{KH}'e göre mikrop dediğimiz şey; bakteriler, virüsler, mantarlar ve protozoalar gibi mikroskobik canlılardır."),
    L("İyi haber: CDC'ye göre mikropların çoğu zararsızdır, hatta işimize yarar. Hastalık yapanlara patojen denir.", [2], f"İyi haber: {CD}'ye göre mikropların çoğu zararsızdır, hatta işimize yarar. Hastalık yapanlara patojen denir."),
    L("Bakterilerle başlayalım. Bakteriler tek hücreli, minicik canlılardır. Küre, çubuk ya da sarmal biçiminde olabilirler.", [3, 4]),
    L("Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre vücudumuzda, kendi hücrelerimizden daha çok bakteri hücresi olduğu tahmin ediliyor!", [3], f"Amerikan Ulusal Sağlık Enstitüleri, {EN}'ye göre vücudumuzda, kendi hücrelerimizden daha çok bakteri hücresi olduğu tahmin ediliyor!"),
    L("Yani sen hiçbir zaman yalnız değilsin. Ben de değilim: içimde bir sürü kablo var!"),
    L("Bu bakterilerin çoğu zararsızdır. Bağırsağımızdakiler ise vücudumuzun normal çalışması için gereklidir. Yalnızca az sayıda tür hastalık yapar.", [3, 4]),
    L("Virüsler ise çok farklıdır. Bir protein kılıfın içinde, DNA ya da RNA denen genetik bilgiden oluşurlar.", [5]),
    L("Virüsler tek başına çoğalamaz. Bir hücreye girer, o hücrenin parçalarını kullanarak kendini kopyalar ve çoğu zaman hücreye zarar verir.", [5]),
])
e.sec("finding", [
    L("Mikroplar nasıl yayılır? Çoğu, hapşırık ve öksürükle havaya karışır ya da tükürük gibi vücut sıvılarıyla geçer.", [6]),
    L("Yıkanmamış ellerle gözüne, burnuna, ağzına dokunmak da onlara kapı açar.", [6]),
    L("Ama vücudun güçlü bir ordusu var: bağışıklık sistemi. İlk kalesi derindir; mikropların içeri girmesini engeller.", [7]),
    L("Mikrop yine de içeri sızarsa akyuvarlar devreye girer. Fagosit denen akyuvarlar, istilacıları adeta yutar.", [8]),
    L("Lenfositler ise düşmanı hatırlamaya ve yok etmeye yardım eder. T hücreleri birer asker gibidir.", [8]),
    L("B hücreleri antikor denen özel proteinler üretir. Antikorlar, aynı mikropla yeniden karşılaşırsak diye vücutta kalır.", [8, 9]),
    L("Bu yüzden suçiçeği geçiren biri genellikle bir daha ondan hastalanmaz.", [9]),
    L("Vücudunun bir hafıza kartı var. Benimki ise bazen dolup taşıyor!"),
])
e.sec("importance", [
    L("Aşılar da bu hafızadan yararlanır. Aşı, mikrobun ölü ya da zayıflatılmış hâlini ya da bir parçasını içerir.", [10]),
    L("Bağışıklık sistemi gerçek bir enfeksiyon varmış gibi davranır ve o mikrobu tanıyan antikorlar üretir. Böylece asıl mikrop geldiğinde hazırdır.", [10]),
    L("Peki antibiyotik? CDC'ye göre antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez.", [11], f"Peki antibiyotik? {CD}'ye göre antibiyotikler soğuk algınlığı ve grip gibi virüslere etki etmez."),
    L("Üstelik bazı mikroplar zamanla onları öldürmek için yapılan ilaçları yenmeyi öğrenebilir. Buna antimikrobiyal direnç denir. Dirençli olan vücudumuz değil, mikroptur.", [11]),
    L("En güçlü silahımız ise çok basit: sabun ve su! CDC'ye göre çoğu durumda mikroplardan kurtulmanın en iyi yolu budur.", [12], f"En güçlü silahımız ise çok basit: sabun ve su! {CD}'ye göre çoğu durumda mikroplardan kurtulmanın en iyi yolu budur."),
    L("Ellerini ıslat, sabunla köpürt ve en az 20 saniye ov. Süreyi tutturmak için Doğum Günü şarkısını baştan sona iki kez söyleyebilirsin.", [12], "Ellerini ıslat, sabunla köpürt ve en az yirmi saniye ov. Süreyi tutturmak için Doğum Günü şarkısını baştan sona iki kez söyleyebilirsin."),
    L("Sonra temiz suyla durula ve temiz bir havluyla kurula.", [12]),
    L("Ne zaman? Tuvaletten sonra, yemekten önce, burnunu sildikten, öksürdükten ya da hapşırdıktan sonra.", [13]),
    L("Hapşırırken mendil kullan ve mendili at. Mendil yoksa eline değil, dirseğine hapşır!", [14]),
    L("Ben dirseğime hapşıramam. Ama vidalarım gıcırdayınca dirseğimi kapatıyorum!"),
    L("Şimdi sıra sende! Bir aile büyüğünle birlikte el yıkama dedektifliği yap: bir hafta boyunca evde elleri ne zaman yıkadığınızı bir tabloya not edin.", [13]),
    L("Hafta sonunda bakın: hangi durumlarda yıkamayı unutmuşsunuz?"),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? El yıkamak, solunum yolu ve ishal enfeksiyonlarının yayılmasını önlemeye yardım edebilir.", [13]),
    L("Hızlı soru! Antibiyotikler virüslere etki eder mi?", [11]),
    L("Düşün bakalım... Hayır! Antibiyotikler virüslere etki etmez.", [11]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Şimdi ellerini yıkamaya!"),
])
S = e.S
S(3, {"type": "hook", "question": "Mikroplar nedir?", "emoji": "🦠"}, ["🔬", "🧼", "🫧", "🧫"], ["", "DOST MU, DÜŞMAN MI?", "MİKROSKOBUN ALTINA!"], fx="sparkle")
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Mikrop nedir?", "Vücudumuz kendini nasıl savunur?", "Mikroplardan nasıl korunuruz?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Mikrop ailesi", "emoji": "🔬", "chips": [{"label": "Bakteriler", "emoji": "🦠"}, {"label": "Virüsler", "emoji": "🧬"}, {"label": "Mantarlar", "emoji": "🍄"}, {"label": "Protozoalar", "emoji": "💧"}]}, ["🧫", "✨"], ["MİKROSKOBİK", "ÇOĞU ZARARSIZ ✅"])
S(3, {"type": "comparison", "title": "Bakteriler", "left": {"title": "Nedir? 🦠", "items": ["Tek hücreli canlılar", "Küre, çubuk, sarmal"]}, "right": {"title": "Nerede? 🧍", "items": ["Vücudumuzda bol bol", "Kendi hücrelerimizden fazla olabilir"]}}, ["🔬", "🔌"], ["TEK HÜCRE", "BAKTERİ ÇOK!", "KABLOLARIM 🔌"])
S(1, {"type": "meter", "title": "Bakterilerin çoğu", "label": "Zararsız", "emoji": "🦠", "phases": [{"label": "Çoğu zararsız ya da yararlı", "level": 0.9, "emoji": "✅"}, {"label": "Az sayıda tür hastalık yapar", "level": 0.1, "emoji": "⚠️"}], "note": NOTE}, ["🍽️", "💪"], ["BAĞIRSAK DOSTLARI"])
S(2, {"type": "diagram", "title": "Virüs nasıl çoğalır?", "layout": "flow", "nodes": [{"label": "Protein kılıf + DNA/RNA", "emoji": "🧬"}, {"label": "Hücreye girer", "emoji": "🚪"}, {"label": "Hücrenin parçalarıyla kopyalar", "emoji": "📋"}, {"label": "Hücre zarar görür", "emoji": "💥"}]}, ["🦠", "🔬"], ["VİRÜS", "TEK BAŞINA ÇOĞALAMAZ"])
S(2, {"type": "spotlight", "title": "Mikroplar nasıl yayılır?", "emoji": "🤧", "chips": [{"label": "Hapşırık ve öksürük", "emoji": "🤧"}, {"label": "Tükürük, ter", "emoji": "💧"}, {"label": "Yıkanmamış eller", "emoji": "✋"}, {"label": "Göz, burun, ağız", "emoji": "👃"}]}, ["🫧", "🦠"], ["HAPŞIRIK!", "ELLER ✋"])
S(1, {"type": "big-number", "value": "Deri", "label": "Bağışıklığın ilk kalesi", "sub": "Mikropların içeri girmesini engeller", "icon": "🛡️"}, ["🏰", "🦠"], ["İLK KALE 🛡️"])
S(3, {"type": "diagram", "title": "Akyuvar ordusu", "layout": "flow", "nodes": [{"label": "Fagosit: yutar", "emoji": "🍽️"}, {"label": "Lenfosit: hatırlar", "emoji": "🧠"}, {"label": "T hücresi: asker", "emoji": "💂"}, {"label": "B hücresi: antikor yapar", "emoji": "🎯"}]}, ["🦠", "⚔️"], ["FAGOSİT", "T HÜCRESİ 💂", "ANTİKOR 🎯"])
S(2, {"type": "spotlight", "title": "Vücudun hafızası", "emoji": "🧠", "chips": [{"label": "Antikorlar vücutta kalır", "emoji": "🎯"}, {"label": "Aynı mikrop gelirse hazır", "emoji": "✅"}, {"label": "Suçiçeği örneği", "emoji": "🔴"}]}, ["💾", "🤖"], ["HAFIZA KARTI 💾", "BENİMKİ DOLU 😅"])
S(2, {"type": "diagram", "title": "Aşı nasıl çalışır?", "layout": "flow", "nodes": [{"label": "Ölü ya da zayıf mikrop", "emoji": "💉"}, {"label": "Bağışıklık sistemi tepki verir", "emoji": "⚔️"}, {"label": "Antikor üretilir", "emoji": "🎯"}, {"label": "Asıl mikroba hazır", "emoji": "🛡️"}]}, ["🧬", "✅"], ["AŞI", "HAZIRLIK 🛡️"])
S(2, {"type": "comparison", "title": "Antibiyotikler", "left": {"title": "Etki etmez ❌", "items": ["Virüsler", "Soğuk algınlığı, grip"]}, "right": {"title": "Direnç ⚠️", "items": ["Mikroplar ilacı yenmeyi öğrenebilir", "Dirençli olan vücut değil, mikrop"]}}, ["💊", "🦠"], ["VİRÜSE ETKİ ETMEZ", "DİRENÇ ⚠️"])
S(3, {"type": "stages", "title": "El yıkama", "rows": [{"label": "Islat", "emoji": "💧"}, {"label": "Sabunla köpürt", "emoji": "🧼"}, {"label": "En az 20 saniye ov", "emoji": "⏱️"}, {"label": "Durula ve kurula", "emoji": "🧻"}], "path": [0, 1, 1, 2, 2, 2, 3, 3], "highlightRow": 2, "note": "Şematik çizim."}, [], ["SABUN + SU 🧼", "20 SANİYE ⏱️", "DURULA, KURULA"])
S(2, {"type": "bullets", "title": "Ne zaman yıka?", "items": ["Tuvaletten sonra", "Yemekten önce", "Burnunu sildikten, öksürdükten, hapşırdıktan sonra", "Mendil yoksa dirseğine hapşır!"]}, ["🚽", "🍎"], ["NE ZAMAN?", "DİRSEĞE HAPŞIR 💪"])
S(1, {"type": "big-number", "value": "Dirsek", "label": "Mendil yoksa buraya hapşır", "sub": "Muma'nın dirseği gıcırdıyor!", "icon": "💪"}, ["🤧", "🔩"], ["GICIRT 🔩"])
S(2, {"type": "spotlight", "title": "Sen de dene: el yıkama dedektifi", "emoji": "🕵️", "chips": [{"label": "Bir aile büyüğünle", "emoji": "👨‍👩‍👧"}, {"label": "Bir hafta not tut", "emoji": "📓"}, {"label": "Ne zaman unuttunuz?", "emoji": "🔎"}]}, ["🧼", "✏️"], ["DEDEKTİFLİK 🕵️", "TABLOYA BAK"])
S(1, {"type": "big-number", "value": "El yıkamak", "label": "Solunum ve ishal enfeksiyonlarının yayılmasını önleyebilir", "sub": "CDC", "icon": "🧼"}, ["🫧", "💧"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Antibiyotikler virüslere etki eder mi?", "emoji": "🤔"}, ["💊", "🦠"], ["HIZLI SORU!", "HAYIR ❌"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 21, "videoTitle": "Mikroplar nedir?", "paperTitleTr": "Mikroplar nedir?",
  "theme": {"backdrop": "micro", "actors": [{"kind": "swarm", "emoji": "🦠", "size": 90}, {"kind": "chase", "emoji": "🧼", "emoji2": "🦠", "every": 18, "size": 100}]},
  "takeaways": ["Mikropların çoğu zararsızdır; bakteriler ve virüsler çok farklıdır", "Deri, akyuvarlar ve antikorlar bizi korur; aşılar hafızayı eğitir", "Sabun ve suyla en az 20 saniye el yıkamak en iyi korunmadır"],
  "description": "Ellerimizdeki görünmez canlılar kim? Bu bölümde bakterileri, virüsleri ve öteki mikropları; mikropların nasıl yayıldığını; derinin, akyuvarların, T ve B hücrelerinin ve antikorların bizi nasıl koruduğunu; aşıların nasıl çalıştığını ve antibiyotiklerin neden virüslere etki etmediğini keşfediyoruz. Sonunda el yıkama dedektifliği etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Mikrop", "meaning": "Gözle görülemeyecek kadar küçük canlı; bakteri, virüs, mantar ya da protozoa."},
    {"term": "Bakteri", "meaning": "Tek hücreli, minicik canlı; çoğu zararsızdır."},
    {"term": "Virüs", "meaning": "Protein kılıf içinde genetik bilgi taşıyan, ancak bir hücrenin içinde çoğalabilen mikrop."},
    {"term": "Patojen", "meaning": "Hastalığa yol açan mikrop."},
    {"term": "Bağışıklık sistemi", "meaning": "Vücudu enfeksiyonlara karşı koruyan savunma sistemi."},
    {"term": "Akyuvar", "meaning": "Bağışıklık sisteminde görevli kan hücresi."},
    {"term": "Antikor", "meaning": "Belirli bir mikrobu tanıyan ve onunla savaşan özel protein."},
    {"term": "Aşı", "meaning": "Bağışıklık sistemini bir mikroba karşı önceden hazırlayan uygulama."},
    {"term": "Antibiyotik", "meaning": "Bakterilere karşı kullanılan ilaç; virüslere etki etmez."}],
  "song": e.song("Görünmez Dünya", [("🦠", "Bakteri"), ("🧬", "Virüs"), ("🛡️", "Akyuvar"), ("🎯", "Antikor"), ("🧼", "Sabun")],
    ["Gözle görülmez minik canlılar", "Bakteri, virüs, mantar, protozoa", "Çoğu zararsız, bazısı dosttur", "Az bir kısmı hasta eder bizi"],
    ["Sabunla köpürt, yirmi saniye ov!", "İki kez söyle Doğum Günü şarkısını", "Deri bir kale, akyuvar asker", "Antikor hatırlar, vücut kazanır"],
    ["Virüs çoğalamaz kendi başına", "Hücreye girer, kopyalar kendini", "Aşı öğretir düşmanı önceden", "Antibiyotik virüse işlemez"],
    ["Sabunla köpürt, yirmi saniye ov!", "İki kez söyle Doğum Günü şarkısını", "Mendil yoksa dirseğine hapşır", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "chase", "emoji": "🧼", "emoji2": "🦠", "every": 6, "size": 230}, {"kind": "swarm", "emoji": "🫧"}, {"kind": "hop", "emoji": "🛡️"}, {"kind": "hop", "emoji": "💪"}, {"kind": "hop", "emoji": "🧼"}])}
e.write(D, facts, script)
