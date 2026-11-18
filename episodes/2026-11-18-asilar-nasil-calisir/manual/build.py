"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:asilar-nasil-calisir"
WH = "World Health Organization — How do vaccines work?"; CD = "CDC — Explaining How Vaccines Work"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "How do vaccines work?", "publisher": "Dünya Sağlık Örgütü", "url": "https://www.who.int/news-room/feature-stories/detail/how-do-vaccines-work"},
    {"id": "k2", "title": "Explaining How Vaccines Work", "publisher": "CDC", "url": "https://www.cdc.gov/vaccines/basics/explaining-how-vaccines-work.html"}],
  "facts": [
    F(1, "Mikroplar hem çevremizde hem vücudumuzda, her yerdedir.", "Germs are all around us, both in our environment and in our bodies.", WH),
    F(2, "Patojen, vücutta hastalığa yol açabilen bir bakteri, virüs, parazit ya da mantardır.", "A pathogen is a bacterium, virus, parasite or fungus that can cause disease within the body.", WH),
    F(3, "Patojenin antikor oluşumuna yol açan parçasına antijen denir.", "The subpart of a pathogen that causes the formation of antibodies is called an antigen.", WH),
    F(4, "Antikorlar vücudun savunma sistemindeki askerler gibidir; her antikor tek bir belirli antijeni tanımak üzere eğitilmiştir.", "You can consider antibodies as the soldiers in your body’s defense system. / Each antibody, or soldier, in our system is trained to recognize one specific antigen.", WH),
    F(5, "Patojen antikorlarca yenildikten sonra da hayatta kalan hafıza hücreleri oluşur; aynı patojenle yeniden karşılaşınca antikor yanıtı ilk seferden çok daha hızlı ve etkili olur.", "memory cells, which remain alive even after the pathogen is defeated by the antibodies. / the antibody response is much faster and more effective than the first time around", WH),
    F(6, "Aşılar belirli bir organizmanın zayıflatılmış ya da etkisiz parçalarını (antijen) içerir; yeni aşılar antijenin kendisi yerine onu üretmenin planını (DNA ya da RNA) içerir.", "Vaccines contain weakened or inactive parts of a particular organism (antigen) / Newer vaccines contain the blueprint for producing antigens (DNA or RNA) rather than the antigen itself.", WH),
    F(7, "Aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir; vücudun, tam bir enfeksiyonun tehlikeleri olmadan kendini korumayı öğrenmesine yardım eder.", "Vaccines work by imitating an infection to engage the body’s natural defenses. / Vaccines help the body learn how to defend itself from disease without the dangers of a full-blown infection.", CD),
    F(8, "Akyuvarlar kemik iliğinde üretilir ama vücudun her yerine az sayıda dağılır.", "White blood cells are created in the bone marrow but dispersed throughout the body in low numbers", CD),
    F(9, "Bazı aşılar haftalar ya da aylar arayla birden çok doz gerektirir; bu, uzun ömürlü antikorların ve hafıza hücrelerinin gelişmesi için gerekebilir.", "Some vaccines require multiple doses, given weeks or months apart. / This is sometimes needed to allow for the production of long-lived antibodies and development of memory cells.", WH),
    F(10, "Bağışıklığın gelişmesi aşıdan sonra haftalar sürebilir.", "Because immunity can take weeks to develop after vaccination", CD),
    F(11, "Aşıya verilen bağışıklık yanıtı bir iki gün yorgunluk ve rahatsızlık yapabilir.", "The immune response to a vaccine might cause tiredness and discomfort for a day or two", CD),
    F(12, "Bir toplulukta çok kişi aşılanınca patojen yayılmakta zorlanır; buna sürü bağışıklığı denir; aşılanmak yalnızca kişinin kendisini değil, aşılanamayanları da korur.", "When a lot of people in a community are vaccinated, the pathogen has a hard time circulating / This is called herd immunity. / Vaccinating not only protects yourself but also protects those in the community who are unable to be vaccinated.", WH),
    F(13, "Çiçek hastalığının yok edildiği, küresel aşılama ve gözetim çalışmalarının ardından 1980'de Dünya Sağlık Örgütü tarafından onaylandı.", "certified by WHO in 1980 after global vaccination and surveillance efforts", WH, ["1980"]),
    F(14, "2000 ile 2023 arasında kızamık aşılamasının tahminen 60 milyon ölümü önlediği hesaplanıyor.", "Between 2000 and 2023, measles vaccination prevented an estimated 60 million deaths.", WH, ["2000", "2023", "60"]),
]}
e = Ep(); L = e.L
CDs = "Si Di Si"
e.sec("hook", [
    L("Dünya Sağlık Örgütü'ne göre mikroplar her yerde: çevremizde ve hatta vücudumuzda. Peki vücudun onlarla nasıl başa çıkar?", [1]),
    L("Hiç karşılaşmadığın bir hastalığa karşı önceden hazırlanmak mümkün mü?"),
    L("Bugün vücudunun savunma ordusunu ve aşıların onu nasıl eğittiğini keşfediyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Vücudun mikroplarla nasıl savaşır? Aşı içinde ne vardır? Ve aşı neden başkalarını da korur?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Hastalığa yol açabilen bakteri, virüs, parazit ya da mantarlara patojen denir.", [2]),
    L("Her patojenin üzerinde antijen denen bir parça vardır. Antijen, vücudunun 'Bu bir yabancı!' diye tanıdığı kimlik kartı gibidir.", [3]),
    L("Vücudun antijeni tanıyınca antikor üretir. Dünya Sağlık Örgütü'ne göre antikorlar savunma sisteminin askerleri gibidir.", [3, 4]),
    L("Her antikor tek bir antijeni tanımak üzere eğitilmiştir. Yani her askerin tek bir hedefi vardır!", [4]),
    L("Benim de bir savunma sistemim var: antivirüs programı. Ama o sadece bilgisayar virüslerini tanıyor!"),
])
e.sec("finding", [
    L("Savaş bitince bir şey daha olur: Hafıza hücreleri oluşur. Patojen yenildikten sonra da hayatta kalırlar.", [5]),
    L("Aynı patojen bir daha gelirse, antikor yanıtı ilk seferden çok daha hızlı ve etkili olur. Vücudun onu hatırlar!", [5]),
    L("İşte aşıların sırrı bu hafızada. Aşılar, belirli bir mikrobun zayıflatılmış ya da etkisiz parçalarını, yani antijenlerini içerir.", [6]),
    L("Bazı yeni aşılar ise antijenin kendisini değil, onu üretmenin planını taşır: DNA ya da RNA.", [6]),
    L("CDC'ye göre aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir.", [7], f"{CDs}'ye göre aşılar bir enfeksiyonu taklit ederek vücudun doğal savunmasını harekete geçirir."),
    L("Böylece vücudun, gerçek bir hastalığın tehlikeleri olmadan kendini korumayı öğrenir. Bir tatbikat gibi!", [7]),
    L("Ben de tatbikat yaparım: her sabah kendimi kapatıp açıyorum. Ama hâlâ kapatma düğmemi bulamadım!"),
])
e.sec("importance", [
    L("Bazı aşılar haftalar ya da aylar arayla birden çok doz gerektirir.", [9]),
    L("Bu, uzun ömürlü antikorların ve hafıza hücrelerinin gelişmesi için gerekebilir. Bağışıklığın gelişmesi de haftalar sürebilir.", [9, 10]),
    L("Aşıdan sonra bir iki gün biraz yorgun ya da rahatsız hissedebilirsin. CDC'ye göre bu, vücudunun bağışıklık yanıtıdır.", [11], f"Aşıdan sonra bir iki gün biraz yorgun ya da rahatsız hissedebilirsin. {CDs}'ye göre bu, vücudunun bağışıklık yanıtıdır."),
    L("Aşıların bir süper gücü daha var. Bir toplulukta çok kişi aşılanınca patojen yayılmakta zorlanır. Buna sürü bağışıklığı denir.", [12]),
    L("Böylece aşılanamayan insanlar da korunur. Aşı olmak sadece seni değil, çevreni de korur.", [12]),
    L("Şimdi sıra sende! Domino taşlarını sıraya diz ve ilkini devir. Hepsi birbirini devirir, değil mi?", [12]),
    L("Şimdi aralardan bazı taşları çıkar ve tekrar dene. Zincir duruyor mu? Sürü bağışıklığı da yayılmayı böyle durdurur!", [12]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Küresel aşılama çalışmalarından sonra, Dünya Sağlık Örgütü 1980'de çiçek hastalığının yok edildiğini onayladı!", [13], "Bunu biliyor muydun? Küresel aşılama çalışmalarından sonra, Dünya Sağlık Örgütü bin dokuz yüz sekseninde çiçek hastalığının yok edildiğini onayladı!"),
    L("Hızlı soru! Bir mikrobu hatırlayıp ikinci seferde hızlı yanıt veren hücrelere ne denir?", [5]),
    L("Düşün bakalım... Evet: hafıza hücreleri!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Sağlıkla kal!"),
])
S = e.S
S(3, {"type": "hook", "question": "Aşılar nasıl çalışır?", "emoji": "💉"}, ["🦠", "🛡️"], ["MİKROPLAR HER YERDE", "ÖNCEDEN HAZIRLIK?", "SAVUNMA ORDUSU"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Vücut mikroplarla nasıl savaşır?", "Aşının içinde ne var?", "Aşı neden başkalarını da korur?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Patojen", "emoji": "🦠", "chips": [{"label": "Bakteri", "emoji": "🦠"}, {"label": "Virüs", "emoji": "🧬"}, {"label": "Antijen: kimlik kartı", "emoji": "🪪"}]}, ["🦠", "🪪"], ["PATOJEN", "ANTİJEN 🪪"])
S(3, {"type": "diagram", "title": "Savunma başlıyor", "layout": "flow", "nodes": [{"label": "Antijen tanınır", "emoji": "🔍"}, {"label": "Antikor üretilir", "emoji": "🛡️"}, {"label": "Her antikor tek hedef", "emoji": "🎯"}]}, ["🛡️", "💻"], ["ANTİKOR = ASKER", "TEK HEDEF 🎯", "ANTİVİRÜS 💻"])
S(2, {"type": "comparison", "title": "Hafıza hücreleri", "left": {"title": "İlk karşılaşma 🐢", "items": ["Vücut tanımayı öğrenir"]}, "right": {"title": "İkinci karşılaşma ⚡", "items": ["Çok daha hızlı", "Çok daha etkili"]}}, ["🧠", "⚡"], ["HAFIZA HÜCRESİ", "HATIRLAR!"], fx="sparkle")
S(2, {"type": "spotlight", "title": "Aşının içinde", "emoji": "💉", "chips": [{"label": "Zayıflatılmış ya da etkisiz parçalar", "emoji": "🧩"}, {"label": "Ya da plan: DNA veya RNA", "emoji": "📜"}]}, ["🧩", "📜"], ["ANTİJEN", "DNA • RNA"])
S(3, {"type": "stages", "title": "Aşı tatbikatı", "rows": [{"label": "Aşı enfeksiyonu taklit eder", "emoji": "🎭"}, {"label": "Savunma harekete geçer", "emoji": "🛡️"}, {"label": "Vücut tehlikesizce öğrenir", "emoji": "🎓"}], "path": [0, 0, 1, 1, 2, 2], "highlightRow": 2, "note": "Şematik çizim."}, [], ["TAKLİT", "TATBİKAT", "KAPATMA DÜĞMESİ? 😅"])
S(3, {"type": "meter", "title": "Bağışıklık gelişiyor", "label": "Koruma", "emoji": "🛡️", "phases": [{"label": "Bazı aşılar birden çok doz", "level": 0.4, "emoji": "💉"}, {"label": "Haftalar içinde gelişir", "level": 0.75, "emoji": "📅"}, {"label": "Bir iki gün yorgunluk olabilir", "level": 0.8, "emoji": "😴"}], "note": NOTE}, ["📅", "😴"], ["DOZLAR", "HAFTALAR", "NORMAL BİR YANIT"])
S(2, {"type": "diagram", "title": "Sürü bağışıklığı", "layout": "flow", "nodes": [{"label": "Çok kişi aşılanır", "emoji": "👨‍👩‍👧‍👦"}, {"label": "Patojen yayılamaz", "emoji": "🚫"}, {"label": "Aşılanamayanlar da korunur", "emoji": "👶"}]}, ["👶", "🛡️"], ["SÜRÜ BAĞIŞIKLIĞI", "ÇEVRENİ KORU"])
S(2, {"type": "bullets", "title": "Sen de dene: domino zinciri", "items": ["Domino taşlarını sıraya diz", "İlkini devir, hepsi düşer", "Aradan bazı taşları çıkar", "Zincir duruyor mu?"]}, ["🁢", "🛑"], ["DENEY ZAMANI 🔬", "ZİNCİR DURDU!"])
S(1, {"type": "big-number", "value": "1980", "label": "Çiçek hastalığının yok edildiği onaylandı", "sub": "Dünya Sağlık Örgütü", "icon": "🌍"}, ["🌍", "💉"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Mikrobu hatırlayan hücrelere ne denir?", "emoji": "🤔"}, ["🧠", "🛡️"], ["HIZLI SORU!", "HAFIZA HÜCRELERİ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 38, "videoTitle": "Aşılar nasıl çalışır?", "paperTitleTr": "Aşılar nasıl çalışır?",
  "theme": {"backdrop": "micro", "actors": [{"kind": "swim", "emoji": "🦠", "every": 30}]},
  "takeaways": ["Antikorlar antijenleri tanıyıp patojenlerle savaşır, hafıza hücreleri onları hatırlar", "Aşılar zayıflatılmış ya da etkisiz antijenlerle vücudu tehlikesizce eğitir", "Çok kişi aşılanınca sürü bağışıklığı aşılanamayanları da korur"],
  "description": "Aşılar vücudumuzu hastalıklara karşı nasıl hazırlar? Bu bölümde patojenleri, antijenleri, antikorları ve hafıza hücrelerini; aşıların içinde ne olduğunu, neden bazen birden çok doz gerektiğini ve sürü bağışıklığını keşfediyoruz. Sonunda domino zinciri etkinliği ve konuyu özetleyen bir şarkı var. Sağlıkla ilgili kararlar için her zaman doktorunuza danışın.",
  "glossary": [
    {"term": "Patojen", "meaning": "Hastalığa yol açabilen bakteri, virüs, parazit ya da mantar."},
    {"term": "Antijen", "meaning": "Patojenin, vücudun tanıyıp antikor ürettiği parçası."},
    {"term": "Antikor", "meaning": "Belirli bir antijeni tanıyıp onunla savaşan savunma molekülü."},
    {"term": "Hafıza hücresi", "meaning": "Bir patojeni hatırlayıp ikinci karşılaşmada hızlı yanıt veren hücre."},
    {"term": "Aşı", "meaning": "Vücudu bir hastalığa karşı tehlikesizce eğiten hazırlık."},
    {"term": "Doz", "meaning": "Bir kerede verilen aşı ya da ilaç miktarı."},
    {"term": "Sürü bağışıklığı", "meaning": "Çok kişi aşılanınca hastalığın yayılamaması ve herkesin korunması."}],
  "song": e.song("Savunma Ordusu", [("🛡️", "Antikor"), ("🦠", "Patojen"), ("🪪", "Antijen"), ("🧠", "Hafıza"), ("💉", "Aşı")],
    ["Patojen geldi, kapıyı çaldı", "Antijen gösterdi kimliğini", "Antikor askerler hazır bekler", "Her biri tanır tek hedefini"],
    ["Hatırla, hatırla, hafıza hücresi!", "İkinci sefer daha hızlı", "Aşı bir tatbikat, tehlikesiz", "Vücudum öğrenir kendini korumayı"],
    ["Zayıf parçalar, ya da bir plan", "Bazen bir doz, bazen birkaç", "Çok kişi korununca zincir kopar", "Aşılanamayan da korunur"],
    ["Hatırla, hatırla, hafıza hücresi!", "İkinci sefer daha hızlı", "Domino diz, zinciri durdur", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "swim", "emoji": "🦠"}, {"kind": "hop", "emoji": "🛡️"}, {"kind": "hop", "emoji": "🧠"}, {"kind": "swim", "emoji": "🧬"}])}
e.write(D, facts, script)
