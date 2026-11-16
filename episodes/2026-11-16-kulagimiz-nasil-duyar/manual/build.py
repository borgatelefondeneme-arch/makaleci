"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kulagimiz-nasil-duyar"
N1 = "NIH (NIDCD) — How Do We Hear?"; K1 = "Nemours KidsHealth — Ears"; N2 = "NIH (NIDCD) — Noise-Induced Hearing Loss"; N3 = "NIH (NIDCD) — Balance Disorders"; P1 = "U.S. National Park Service — Understanding Sound"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "How Do We Hear?", "publisher": "NIH", "url": "https://www.nidcd.nih.gov/health/how-do-we-hear"},
    {"id": "k2", "title": "Ears", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/ears.html"},
    {"id": "k3", "title": "Noise-Induced Hearing Loss", "publisher": "NIH", "url": "https://www.nidcd.nih.gov/health/noise-induced-hearing-loss"},
    {"id": "k4", "title": "Balance Disorders", "publisher": "NIH", "url": "https://www.nidcd.nih.gov/health/balance-disorders"},
    {"id": "k5", "title": "Understanding Sound", "publisher": "Ulusal Park Servisi", "url": "https://www.nps.gov/subjects/sound/understandingsound.htm"}],
  "facts": [
    F(1, "Ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler; işitme, havadaki ses dalgalarını elektrik sinyallerine dönüştüren karmaşık adımlara dayanır.", "Sound moves through a medium such as air or water as waves. / Hearing depends on a series of complex steps that change sound waves in the air into electrical signals.", P1 + "; " + N1),
    F(2, "Frekans (perde), ses basınç dalgasının saniyede kaç kez tekrarlandığıdır; genlik, ses dalgalarının göreli gücüdür ve yükseklik olarak algılanır; desibel (dB) ile ölçülür.", "Frequency, sometimes referred to as pitch, is the number of times per second that a sound pressure wave repeats itself. / Amplitude is the relative strength of sound waves (transmitted vibrations), which we perceive as loudness or volume. / Amplitude is measured in decibels (dB)", P1),
    F(3, "Normal işiten insanlar 20 Hz ile 20.000 Hz arasındaki sesleri duyabilir.", "Humans with normal hearing can hear sounds between 20 Hz and 20,000 Hz.", P1, ["20", "20.000"]),
    F(4, "Dış kulağın görevi sesleri toplayıp kulak kanalına yönlendirmektir; ses dalgaları kulak kanalından kulak zarına ulaşır.", "Its main job is to gather sounds and funnel them to the ear canal / Sound waves enter the outer ear and travel through a narrow passageway called the ear canal, which leads to the eardrum.", K1 + "; " + N1),
    F(5, "Kulak zarı gelen ses dalgalarıyla titreşir ve bu titreşimleri orta kulaktaki üç minik kemiğe gönderir: çekiç, örs ve üzengi; üzengi vücudun en küçük kemiğidir.", "The eardrum vibrates from the incoming sound waves and sends these vibrations to three tiny bones in the middle ear. / malleus (pronounced: MAH-lee-us) (\"hammer\") / incus (pronounced: IN-kus) (\"anvil\") / stapes (pronounced: STAY-peez) (\"stirrup\"), which is attached to the incus and is the smallest bone in the body", N1 + "; " + K1),
    F(6, "Orta kulaktaki kemikler ses titreşimlerini güçlendirir ve salyangoz biçimli kokleaya gönderir.", "The bones in the middle ear amplify, or increase, the sound vibrations and send them to the cochlea,", N1),
    F(7, "Baziler zarın üstündeki duyu hücreleri olan tüy hücreleri dalgayla hareket eder; salyangozun geniş ucundaki tüy hücreleri tiz sesleri, merkeze yakın olanlar pes sesleri algılar; hücrelere kimyasallar akar ve elektrik sinyali oluşur; işitme siniri bu sinyali beyne taşır.", "Hair cells—sensory cells sitting on top of the basilar membrane—ride the wave. / Hair cells near the wide end of the snail-shaped cochlea detect higher-pitched sounds / Those closer to the center detect lower-pitched sounds / chemicals rush into the cells, creating an electrical signal. / The auditory nerve carries this electrical signal to the brain", N1),
    F(8, "Kuş ve amfibilerin tersine insan tüy hücreleri yeniden çıkmaz; gürültüye bağlı işitme kaybının çoğu bu hücrelerin hasar görüp ölmesinden kaynaklanır.", "Unlike bird and amphibian hair cells, human hair cells don’t grow back. They are gone for good. / Most NIHL is caused by the damage and eventual death of these hair cells.", N2),
    F(9, "70 dBA ve altındaki sesler uzun süre dinlense bile işitme kaybına yol açma olasılığı düşüktür; 85 dBA ve üstündeki seslere uzun ya da tekrarlı maruz kalmak işitme kaybına yol açabilir; ses ne kadar yüksekse hasar o kadar çabuk oluşur.", "Sounds at or below 70 A-weighted decibels (dBA), even after long exposure, are unlikely to cause hearing loss. / long or repeated exposure to sounds at or above 85 dBA can cause hearing loss. / The louder the sound, the shorter the amount of time it takes for NIHL to happen.", N2, ["70", "85"]),
    F(10, "Normal konuşma 60–70 dBA, sirenler 110–129 dBA, havai fişek gösterisi 140–160 dBA düzeyindedir.", "Normal conversation 60-70 dBA / Sirens 110-129 dBA / Fireworks show 140-160 dBA", N2, ["60", "70", "110", "129", "140", "160"]),
    F(11, "Telefonların, oyunların ve televizyonun sesi kısılmalı; gürültülü bir etkinlikte kulak tıkacı takılmalı; gürültü azaltılamıyorsa ondan uzaklaşılmalı.", "Turn down the volume on phones, video games, TVs, and other devices, especially when listening with earbuds or headphones. / Wear earplugs or other protective devices when involved in a loud activity / If you can’t reduce the noise or protect yourself from it, move away from it.", K1 + "; " + N2),
    F(12, "Kulağın dengeye yardım eden bölümüne vestibüler sistem denir; yarım daire kanalları, birbirine aşağı yukarı dik açılarla dizilmiş üç sıvı dolu kanaldır ve başın ne zaman döndüğünü beyne bildirir.", "The part of the ear that assists in balance is known as the vestibular system, or the labyrinth, / The semicircular canals contain three fluid-filled ducts, which form loops arranged roughly at right angles to one another. / They tell your brain when your head rotates.", N3),
    F(13, "Gök gürültüsü 120 desibeli aşabilir; bu, insan kulağında acıya yol açacak kadar yüksektir.", "The crack of thunder can exceed 120 decibels, loud enough to cause pain to the human ear.", P1, ["120"]),
]}
e = Ep(); L = e.L
EN = "En Ay Eyç"; KH = "Kids Helt"
e.sec("hook", [
    L("Bir arkadaşın adını fısıldıyor, sen hemen dönüp bakıyorsun. Bu kadar küçük bir sesi nasıl yakaladın?"),
    L("Ses kulağına nasıl girer? Ve beynin onu nasıl anlar?"),
    L("Bugün bir ses dalgasının peşinden kulağının içine giriyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Ses nedir? Kulağın içinde neler olur? Ve kulaklarımızı nasıl koruruz?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("ABD Ulusal Park Servisi'ne göre ses, hava ya da su gibi bir ortamda dalgalar hâlinde ilerler.", [1]),
    L("Sesin iki önemli özelliği var. Frekans, dalganın saniyede kaç kez tekrarlandığıdır; sesi ince ya da kalın yapar.", [2]),
    L("Genlik ise dalganın gücüdür; sesin yüksekliğini belirler. Desibel denen birimle ölçülür.", [2]),
    L("Normal işiten insanlar 20 ile 20.000 hertz arasındaki sesleri duyabilir.", [3], "Normal işiten insanlar yirmi ile yirmi bin hertz arasındaki sesleri duyabilir."),
    L("Benim mikrofonum da bu aralığı duyuyor. Ama kulak memesi takmayı unutmuşlar!"),
])
e.sec("finding", [
    L("Yolculuk dış kulakta başlar. KidsHealth'e göre dış kulak sesleri toplar ve kulak kanalına yönlendirir; ses dalgaları kanal boyunca kulak zarına ulaşır.", [4], f"Yolculuk dış kulakta başlar. {KH}'e göre dış kulak sesleri toplar ve kulak kanalına yönlendirir; ses dalgaları kanal boyunca kulak zarına ulaşır."),
    L("Kulak zarı ses dalgalarıyla titreşir ve titreşimi orta kulaktaki üç minik kemiğe iletir: çekiç, örs ve üzengi.", [5]),
    L("Üzengi, vücudundaki en küçük kemiktir!", [5]),
    L("Bu kemikler titreşimi güçlendirir ve salyangoz biçimli, sıvı dolu bir yapıya gönderir: koklea.", [6]),
    L("Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre kokleanın içinde tüy hücreleri denen duyu hücreleri vardır. Sıvıdaki dalgayla birlikte hareket ederler.", [7], f"Amerikan Ulusal Sağlık Enstitüleri, {EN}'ye göre kokleanın içinde tüy hücreleri denen duyu hücreleri vardır. Sıvıdaki dalgayla birlikte hareket ederler."),
    L("Kokleanın geniş ucundaki tüy hücreleri ince sesleri, merkeze yakın olanlar kalın sesleri algılar.", [7]),
    L("Tüy hücreleri hareket edince içlerine kimyasallar akar ve bir elektrik sinyali oluşur. İşitme siniri bu sinyali beyne taşır; beyin de onu tanıdığımız bir sese dönüştürür.", [7]),
])
e.sec("importance", [
    L("İşte kötü haber: NIH'ye göre insanın tüy hücreleri bir kez hasar görürse yeniden çıkmaz.", [8], f"İşte kötü haber: {EN}'ye göre insanın tüy hücreleri bir kez hasar görürse yeniden çıkmaz."),
    L("Gürültünün yol açtığı işitme kaybının çoğu, bu hücrelerin hasar görüp ölmesinden kaynaklanır.", [8]),
    L("70 desibel ve altındaki sesler uzun süre dinlense bile genellikle zarar vermez. Ama 85 desibel ve üstüne uzun ya da sık sık maruz kalmak işitmeye zarar verebilir.", [9], "Yetmiş desibel ve altındaki sesler uzun süre dinlense bile genellikle zarar vermez. Ama seksen beş desibel ve üstüne uzun ya da sık sık maruz kalmak işitmeye zarar verebilir."),
    L("Karşılaştırma için: normal konuşma 60–70, sirenler 110–129, havai fişek gösterisi ise 140–160 desibele kadar çıkabilir.", [10], "Karşılaştırma için: normal konuşma altmış ile yetmiş, sirenler yüz on ile yüz yirmi dokuz, havai fişek gösterisi ise yüz kırk ile yüz altmış desibele kadar çıkabilir."),
    L("Ses ne kadar yüksekse, hasar o kadar çabuk oluşur.", [9]),
    L("Korunmak kolay: kulaklıkla dinlerken sesi kıs. Gürültülü bir yerde kulak tıkacı kullan. Gürültüyü azaltamıyorsan ondan uzaklaş.", [11]),
    L("Kulağın bir görevi daha var: dengeni korur. İç kulaktaki yarım daire kanalları, başının ne zaman döndüğünü beynine bildirir.", [12]),
    L("Ben dönerken dengemi kaybetmem. Ama tekerleklerim kayarsa o başka!"),
    L("Şimdi sıra sende! Elini boğazına koy ve uzun bir ses çıkar. Hissettiğin titreşim, sesin kaynağıdır.", [1]),
    L("Sonra önce ince, sonra kalın bir ses çıkar. Titreşim nasıl değişiyor?", [2]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Gök gürültüsü 120 desibeli aşabilir; bu, kulakta acı hissettirecek kadar yüksek bir sestir.", [13], "Bunu biliyor muydun? Gök gürültüsü yüz yirmi desibeli aşabilir; bu, kulakta acı hissettirecek kadar yüksek bir sestir."),
    L("Hızlı soru! Vücudun en küçük kemiği hangisi?", [5]),
    L("Düşün bakalım... Evet: kulağındaki üzengi kemiği!", [5]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bu videoyu da çok yüksek sesle izleme!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kulağımız nasıl duyar?", "emoji": "👂"}, ["🎵", "🔊"], ["", "SES NASIL GİRER?", "KULAĞIN İÇİNE!"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Ses nedir?", "Kulağın içinde neler olur?", "Kulaklarımızı nasıl koruruz?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "comparison", "title": "Sesin iki özelliği", "left": {"title": "Frekans 〰️", "items": ["Saniyedeki tekrar sayısı", "İnce ya da kalın"]}, "right": {"title": "Genlik 📶", "items": ["Dalganın gücü", "Desibelle ölçülür"]}}, ["🎵", "🔊"], ["SES DALGASI", "FREKANS", "DESİBEL"])
S(2, {"type": "big-number", "value": "20–20.000", "unit": "Hz", "label": "İnsanın duyabildiği frekanslar", "sub": "Ulusal Park Servisi", "icon": "👂"}, ["🎧", "🤖"], ["DUYMA ARALIĞI", "KULAK MEMESİ YOK 😅"])
S(3, {"type": "diagram", "title": "Dış ve orta kulak", "layout": "flow", "nodes": [{"label": "Dış kulak toplar", "emoji": "👂"}, {"label": "Kulak kanalı", "emoji": "➡️"}, {"label": "Kulak zarı titreşir", "emoji": "🥁"}, {"label": "Çekiç, örs, üzengi", "emoji": "🦴"}]}, ["🔊", "〰️"], ["KULAK KANALI", "KULAK ZARI 🥁", "EN KÜÇÜK KEMİK!"])
S(2, {"type": "spotlight", "title": "Koklea", "emoji": "🐌", "chips": [{"label": "Salyangoz biçimli", "emoji": "🐌"}, {"label": "Sıvı dolu", "emoji": "💧"}, {"label": "Tüy hücreleri", "emoji": "🌾"}]}, ["〰️", "🔬"], ["KOKLEA 🐌", "TÜY HÜCRELERİ"])
S(2, {"type": "stages", "title": "Titreşimden sinyale", "rows": [{"label": "Tüy hücreleri hareket eder", "emoji": "🌾"}, {"label": "Elektrik sinyali", "emoji": "⚡"}, {"label": "İşitme siniri", "emoji": "🧵"}, {"label": "Beyin: ses!", "emoji": "🧠"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 3, "note": "Şematik çizim."}, [], ["İNCE / KALIN", "SİNYAL → BEYİN 🧠"])
S(2, {"type": "meter", "title": "Tüy hücreleri", "label": "Sağlam hücre", "emoji": "🌾", "phases": [{"label": "Hasar görünce yeniden çıkmaz", "level": 0.55, "emoji": "⚠️"}, {"label": "Gürültü işitme kaybının çoğu buradan", "level": 0.3, "emoji": "🔊"}], "note": NOTE}, ["⚠️", "👂"], ["YENİDEN ÇIKMAZ ⚠️", "GÜRÜLTÜ"])
S(2, {"type": "bar-chart", "title": "Ne kadar yüksek? (dBA)", "unit": "dBA", "bars": [{"label": "Normal konuşma (en çok)", "value": 70, "display": "70"}, {"label": "Zarar sınırı", "value": 85, "display": "85", "highlight": True}, {"label": "Siren (en çok)", "value": 129, "display": "129"}, {"label": "Havai fişek (en çok)", "value": 160, "display": "160"}]}, ["🔊", "🎆"], ["85 VE ÜSTÜ ⚠️", "HAVAİ FİŞEK 🎆"])
S(2, {"type": "bullets", "title": "Kulaklarını koru", "items": ["Ses yüksekse hasar çabuk", "Kulaklıkta sesi kıs", "Gürültüde kulak tıkacı", "Uzaklaş"], "tone": "caution"}, ["🎧", "🛡️"], ["DAHA YÜKSEK = DAHA ÇABUK", "SESİ KIS 🎧"])
S(2, {"type": "spotlight", "title": "Denge", "emoji": "🎢", "chips": [{"label": "Vestibüler sistem", "emoji": "👂"}, {"label": "Üç yarım daire kanalı", "emoji": "➰"}, {"label": "Başın dönüşünü bildirir", "emoji": "🔄"}]}, ["⚖️", "🤖"], ["DENGE ⚖️", "TEKERLEKLERİM 😅"])
S(2, {"type": "diagram", "title": "Sen de dene: sesi hisset", "layout": "flow", "nodes": [{"label": "Elini boğazına koy", "emoji": "✋"}, {"label": "Uzun bir ses çıkar", "emoji": "🎵"}, {"label": "Titreşimi hisset", "emoji": "〰️"}, {"label": "İnce ve kalın: fark var mı?", "emoji": "🔎"}]}, ["🎤", "📓"], ["DENEY ZAMANI 🔬", "İNCE / KALIN"])
S(1, {"type": "big-number", "value": "120+", "unit": "dB", "label": "Gök gürültüsü: kulakta acıya yol açabilir", "sub": "Ulusal Park Servisi", "icon": "⛈️"}, ["⚡", "👂"], ["BUNU BİLİYOR MUYDUN?"], fx="flash")
S(2, {"type": "hook", "question": "Vücudun en küçük kemiği hangisi?", "emoji": "🤔"}, ["🦴", "👂"], ["HIZLI SORU!", "ÜZENGİ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 24, "videoTitle": "Kulağımız nasıl duyar?", "paperTitleTr": "Kulağımız nasıl duyar?",
  "theme": {"backdrop": "meadow", "actors": [{"kind": "fly", "emoji": "🐦", "every": 28}]},
  "takeaways": ["Ses dalgaları kulak zarını ve üç minik kemiği titreştirir", "Koklea'daki tüy hücreleri titreşimi elektrik sinyaline çevirir", "Tüy hücreleri yenilenmez: yüksek sesten korunmak gerekir"],
  "description": "Fısıltıyı bile nasıl duyarız? Bu bölümde sesin dalga olarak nasıl ilerlediğini, frekans ve desibeli; dış kulaktan kulak zarına, çekiç, örs ve üzengiye, oradan kokleaya ve tüy hücrelerine uzanan yolculuğu; işitme sinirinin sinyali beyne taşımasını keşfediyoruz. Tüy hücreleri neden korunmalı, kulaklarımızı nasıl koruruz, denge nasıl sağlanır? Sonunda sesi hisset etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Ses dalgası", "meaning": "Havada ya da suda titreşim olarak yayılan ses."},
    {"term": "Frekans", "meaning": "Ses dalgasının saniyede kaç kez tekrarlandığı; sesi ince ya da kalın yapar."},
    {"term": "Desibel", "meaning": "Sesin yüksekliğini ölçen birim."},
    {"term": "Kulak zarı", "meaning": "Ses dalgalarıyla titreşen ince zar."},
    {"term": "Koklea", "meaning": "İç kulakta, salyangoz biçimli, sıvı dolu işitme organı."},
    {"term": "Tüy hücreleri", "meaning": "Kokleada titreşimi elektrik sinyaline çeviren duyu hücreleri."},
    {"term": "İşitme siniri", "meaning": "İşitme sinyallerini beyne taşıyan sinir."},
    {"term": "Vestibüler sistem", "meaning": "İç kulakta dengeyi sağlayan bölüm."}],
  "song": e.song("Kulaktaki Yolculuk", [("👂", "Kulak"), ("🥁", "Kulak zarı"), ("🐌", "Koklea"), ("🧠", "Beyin"), ("🎧", "Kulaklık")],
    ["Ses dalga olur, havada yol alır", "Dış kulak toplar, kanala yollar", "Kulak zarı titrer, kemikler sallanır", "Çekiç, örs, üzengi sesi büyütür"],
    ["Duy, duy, dünyayı duy!", "Kokleada tüy hücreleri dans eder", "Titreşim sinyale, sinyal beyne", "Ses anlam kazanır bir anda"],
    ["İnce sesler bir uçta, kalınlar içeride", "Tüy hücreleri bir kez gider, gelmez", "Seksen beş desibel üstü dikkat", "Sesi kıs, kulağını koru"],
    ["Duy, duy, dünyayı duy!", "Kokleada tüy hücreleri dans eder", "Elini boğazına koy, titreşimi hisset", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "🎵"}, {"kind": "hop", "emoji": "🥁"}, {"kind": "hop", "emoji": "🎶"}, {"kind": "fly", "emoji": "🐦", "every": 8}])}
e.write(D, facts, script)
