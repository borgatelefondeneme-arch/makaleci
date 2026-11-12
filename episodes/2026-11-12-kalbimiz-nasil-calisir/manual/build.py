"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kalbimiz-nasil-calisir"
KH = "Nemours KidsHealth — Heart & Circulatory System"; BHF = "British Heart Foundation — How your heart works"; NH = "NIH (NHLBI) — How the Heart Works"; CC = "Cleveland Clinic — Heart: Anatomy & Function"; CDC = "CDC — Child Activity: An Overview"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Heart & Circulatory System", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/heart.html"},
    {"id": "k2", "title": "How your heart works", "publisher": "Britanya Kalp Vakfı", "url": "https://www.bhf.org.uk/informationsupport/how-a-healthy-heart-works"},
    {"id": "k3", "title": "How the Heart Works", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/heart"},
    {"id": "k4", "title": "Heart: Anatomy & Function", "publisher": "Cleveland Clinic", "url": "https://my.clevelandclinic.org/health/body/21704-heart"},
    {"id": "k5", "title": "Child Activity: An Overview", "publisher": "CDC", "url": "https://www.cdc.gov/physical-activity-basics/guidelines/children.html"}],
  "facts": [
    F(1, "Kalp bir kastır; yaklaşık yumruk büyüklüğündedir; göğsün ortasında, hafifçe sola yatık durur.", "It’s a muscle, about the size of your fist, in the middle of your chest tilted slightly to the left.", BHF),
    F(2, "Kalp bir pompa olan organdır; genellikle dakikada yaklaşık 60–100 kez atar.", "The heart is an organ that’s a pump, usually beating about 60 to 100 times per minute.", KH, ["60", "100"]),
    F(3, "Kalbin dört odacığı vardır: üstteki iki kulakçık kalbe giren kanı alır; alttaki iki karıncık kanı kalpten dışarı pompalar.", "The heart has four chambers — two on the top and two on the bottom: / The two top chambers are the right atrium and the left atrium. They receive the blood entering the heart. / The two bottom chambers are the right ventricle and the left ventricle. These pump blood out of the heart.", KH),
    F(4, "İki taraf, septum adlı ince kas duvarla ayrılır.", "They are separated by a thin muscular wall called the septum.", BHF),
    F(5, "Sağ kulakçık vücudun geri kalanından gelen oksijeni azalmış kanı alır; sağ karıncık bu kanı yeni oksijen alması için akciğerlere pompalar.", "the right atrium receives blood low in oxygen from the rest of the body. / the right ventricle pumps the blood low in oxygen to the lungs to pick up a fresh supply of oxygen", BHF),
    F(6, "Akciğerlerde kan oksijen alır ve karbondioksit bırakır.", "At the lungs, the blood picks up oxygen and drops off carbon dioxide.", KH),
    F(7, "Sol kulakçık akciğerlerden gelen oksijence zengin kanı alır ve sol karıncığa pompalar; sol karıncık bu kanı vücudun geri kalanına pompalar.", "the left atrium receives blood high in oxygen from the lungs and pumps it to the left ventricle / the left ventricle pumps blood high in oxygen to the rest of the body.", BHF),
    F(8, "Akciğer (küçük) dolaşımı kalpten akciğerlere gidip dönen kısa bir halkadır; sistemik (büyük) dolaşım kanı kalpten vücudun bütün öteki bölümlerine taşır ve geri getirir.", "The pulmonary circulation is a short loop from the heart to the lungs and back again. / The systemic circulation carries blood from the heart to all the other parts of the body and back again.", KH),
    F(9, "Aort en büyük atardamardır; kalpten oksijence zengin kanı taşıyarak çıkar.", "The aorta is the largest artery, and it leaves the heart carrying the oxygen-rich blood.", KH),
    F(10, "Kalpte dört kapakçık vardır; her atışta açılıp kapanan kapılar gibi çalışırlar.", "They act like doors that open and close with every heartbeat. / There are 4 valves in your heart:", BHF),
    F(11, "Kalp atışının ilk sesi (lub) kulakçık-karıncık kapakçıklarının, ikinci sesi (dub) öteki kapakçıkların kapanmasıyla oluşur.", "During systole, the atrioventricular valves close, creating the first sound — the lub — of a heartbeat. / These valves closing is what creates the second sound — the dub — of a heartbeat.", KH),
    F(12, "Atardamarlar kanı kalpten uzağa, toplardamarlar kalbe geri taşır; kılcal damarlar çok küçük atardamarları çok küçük toplardamarlara bağlayan minik damarlardır.", "Arteries carry blood away from the heart, and veins carry blood back to the heart. / Capillaries are tiny blood vessels that connect very small arteries to very small veins.", KH),
    F(13, "Sinüs düğümü sağ kulakçığın duvarındaki küçük bir doku alanıdır; atış hızını belirlediği için kalbin pili (pacemaker) denir; kalp kasının kasılmasını başlatan elektrik sinyalini gönderir.", "The sinus node, or sinoatrial node, is a small area of tissue in the wall of the right atrium. / This node is called the pacemaker of the heart because it sets the rate of the heartbeat / It sends out an electrical signal to start the contracting (pumping) of the heart muscle.", KH),
    F(14, "Kalp her gün yaklaşık 100.000 kez atar.", "Each day, your heart beats around 100,000 times.", BHF, ["100.000"]),
    F(15, "Egzersiz yaparken kalp daha hızlı pompalar; böylece kaslar daha çok oksijen alır.", "But when you’re exercising, the heart pumps faster so that your muscles get more oxygen and can work harder.", KH),
    F(16, "Kan, organların çalışması için gereken oksijeni ve besinleri taşır; istenmeyen karbondioksiti ve atıkları da uzaklaştırır.", "Your blood carries the oxygen and nutrients that your organs need to work properly. / Your blood also carries away unwanted carbon dioxide and waste products.", NH + "; " + BHF),
    F(17, "6–17 yaş arasındaki çocuk ve gençlerin her gün en az 60 dakika hareketli olması gerekir.", "Children and adolescents 6 to 17 need to be active for at least 60 minutes every day.", CDC, ["6", "17", "60"]),
    F(18, "Dengeli, besleyici beslenmek ve sigara içmemek kalp sağlığını korur.", "eating a balanced, nutritious diet / Quit smoking and/or using tobacco products and avoid secondhand smoke.", KH + "; " + CC),
    F(19, "Sol karıncık sağ karıncıktan biraz daha büyüktür.", "The left ventricle is slightly larger than the right.", CC),
    F(20, "Elektrik uyarıları önce kulakçıkları kasar; elektrik sinyalleri kalbin düzenli ve eşgüdümlü atmasını sağlar.", "These electrical impulses make the atria contract first. / The electric signals make your heart beat in a regular, coordinated rhythm.", KH + "; " + BHF),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"
e.sec("hook", [
    L("Şu an göğsünde, sen hiç düşünmeden çalışan bir pompa var. Dün gece sen uyurken de çalıştı!", [2]),
    L("Yumruğun kadar bir kas, kanı bütün vücuduna nasıl ulaştırıyor?", [1]),
    L("Bugün kalbin içine giriyoruz!"),
])
e.sec("context", [
    L("Benim kalbim yok, pilim var. Yine de bu konuya kalbimi... yani pilimi koydum!"),
    L("Üç sorumuz var. Kalbin içinde neler var? Kan vücutta hangi yolu izler? Ve kalbe atmasını kim söyler?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("Britanya Kalp Vakfı'na göre kalp bir kastır. Yaklaşık yumruğun büyüklüğündedir ve göğsünün ortasında, hafifçe sola yatık durur.", [1]),
    L("Görevi pompalamaktır. KidsHealth'e göre genellikle dakikada 60–100 kez atar.", [2], f"Görevi pompalamaktır. {KHs}'e göre genellikle dakikada altmış ile yüz kez atar."),
    L("Peki kan neden bu kadar önemli? Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre kan, organlarının çalışması için gereken oksijeni ve besinleri taşır.", [16], "Peki kan neden bu kadar önemli? Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'e göre kan, organlarının çalışması için gereken oksijeni ve besinleri taşır."),
    L("Dönerken de karbondioksiti ve atıkları toplayıp götürür.", [16]),
    L("Kalbin içinde dört odacık vardır. Üstteki ikisine kulakçık denir: kalbe gelen kanı karşılarlar.", [3]),
    L("Alttaki ikisine karıncık denir: kanı kalpten dışarı pompalarlar.", [3]),
    L("Kalbin sağ ve sol tarafı, septum adlı ince bir kas duvarla birbirinden ayrılır.", [4]),
    L("Kalpte dört de kapakçık bulunur. Her atışta açılıp kapanan kapılar gibidirler.", [10]),
    L("Benim de kapağım var. Ama o pil kapağı!"),
])
e.sec("finding", [
    L("Şimdi kanın yolculuğunu izleyelim. Vücudu dolaşıp oksijeni azalmış kan, önce sağ kulakçığa gelir.", [5]),
    L("Oradan sağ karıncığa geçer. Sağ karıncık bu kanı akciğerlere pompalar.", [5]),
    L("Akciğerlerde kan oksijen alır ve karbondioksit bırakır.", [6]),
    L("Kalpten akciğerlere gidip geri dönen bu kısa tura küçük dolaşım denir.", [8]),
    L("Oksijence zengin kan sol kulakçığa döner, oradan sol karıncığa geçer.", [7]),
    L("Sol karıncık, sağdakinden biraz daha büyüktür ve kanı bütün vücuda pompalar.", [7, 19]),
    L("Kan kalpten aort adlı damarla çıkar. Aort, vücudun en büyük atardamarıdır. Bu uzun tura büyük dolaşım denir.", [9, 8]),
    L("Damarların üç türü var. Atardamarlar kanı kalpten uzağa taşır. Toplardamarlar kalbe geri getirir.", [12]),
    L("Kılcal damarlar ise çok incedir: en küçük atardamarları en küçük toplardamarlara bağlar.", [12]),
    L("Peki o ünlü ses? Lub-dub! KidsHealth'e göre bu, kapakçıkların kapanma sesidir: önce bir grup kapanır, lub; sonra öteki grup, dub.", [11], f"Peki o ünlü ses? Lab-dab! {KHs}'e göre bu, kapakçıkların kapanma sesidir: önce bir grup kapanır, lab; sonra öteki grup, dab."),
])
e.sec("importance", [
    L("Kalbe atmasını kim söyler? Kendi içindeki küçük bir doku: sinüs düğümü. Sağ kulakçığın duvarında yer alır.", [13]),
    L("Sinüs düğümü bir elektrik sinyali gönderir ve kalp kası kasılır. Atışın hızını o belirlediği için ona kalbin doğal pili de denir.", [13]),
    L("Demek ki senin de bir pilin var. Kardeş sayılırız!"),
    L("Britanya Kalp Vakfı'na göre kalbin her gün yaklaşık 100.000 kez atar.", [14], "Britanya Kalp Vakfı'na göre kalbin her gün yaklaşık yüz bin kez atar."),
    L("Koşarken kalbin neden hızlanır? Çünkü kasların daha çok oksijene ihtiyaç duyar; kalp de daha hızlı pompalar.", [15]),
    L("Kalbini korumak için CDC'nin önerisi şu: 6–17 yaş arasındakiler her gün en az 60 dakika hareket etmeli.", [17], "Kalbini korumak için Si Di Si'nin önerisi şu: altı ile on yedi yaş arasındakiler her gün en az altmış dakika hareket etmeli."),
    L("Dengeli beslenmek ve sigaradan uzak durmak da kalbi korur.", [18]),
    L("Şimdi sıra sende! İşaret ve orta parmağını bileğinin iç yüzüne, başparmağının hemen altına koy. Hissettiğin vuruşlar nabzındır."),
    L("Otuz saniye boyunca vuruşları say ve ikiyle çarp. Bu, kalbinin bir dakikadaki atış sayısıdır.", [2]),
    L("Sonra yirmi kez zıpla ve yeniden say. Sayı arttı mı? Kasların oksijen istedi, kalbin hızlandı!", [15]),
    L("Bir uyarı: kendini zorlama; yorulursan dinlen."),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Kalp atarken elektrik sinyali önce kulakçıkları kasar. Böylece kalp düzenli ve eşgüdümlü bir ritimle çalışır.", [20]),
    L("Hızlı soru! Kanı akciğerlere hangi odacık pompalar: sağ karıncık mı, sol karıncık mı?", [5]),
    L("Düşün bakalım... Evet: sağ karıncık!", [5]),
    L("Sol karıncık ise bütün vücuda pompalar. Ağır işi o almış; ben olsam ek şarj isterdim!", [7]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Ben de pilimi şarja takayım; ne de olsa benim kalbim o!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kalbimiz kanı nasıl pompalar?", "emoji": "❤️"}, ["💓", "🩸", "🫁", "🏃"], ["", "YUMRUK KADAR KAS", "KALBİN İÇİNE!"])
S(1, {"type": "spotlight", "title": "Kalp yerine pil", "emoji": "🤖", "chips": [{"label": "Kalbim yok", "emoji": "💔"}, {"label": "Pilim var", "emoji": "🔋"}, {"label": "Konuya pilimi koydum!", "emoji": "😄"}]}, ["🔋", "⚙️"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kalbin içinde neler var?", "Kan vücutta hangi yolu izler?", "Kalbe atmasını kim söyler?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(1, {"type": "spotlight", "title": "Kalp nedir?", "emoji": "❤️", "chips": [{"label": "Bir kas", "emoji": "💪"}, {"label": "Yumruğun kadar", "emoji": "✊"}, {"label": "Göğsün ortasında", "emoji": "📍"}, {"label": "Hafifçe sola yatık", "emoji": "↙️"}]}, ["🩺", "💓"], ["KALP = KAS 💪"])
S(1, {"type": "big-number", "value": "60–100", "label": "Dakikadaki atış sayısı", "sub": "KidsHealth", "icon": "💓"}, ["⏱️", "🩺"], ["POMPA!"])
S(2, {"type": "comparison", "title": "Kan ne taşır?", "left": {"title": "Götürür ➡️", "items": ["Oksijen", "Besinler"]}, "right": {"title": "Geri toplar ⬅️", "items": ["Karbondioksit", "Atıklar"]}}, ["🩸", "🍎"], ["OKSİJEN + BESİN", "ATIKLARI TOPLAR"])
S(3, {"type": "spotlight", "title": "Dört odacık", "emoji": "❤️", "chips": [{"label": "Üstte iki kulakçık: kanı karşılar", "emoji": "⬆️"}, {"label": "Altta iki karıncık: kanı pompalar", "emoji": "⬇️"}, {"label": "Septum: sağ ve solu ayıran duvar", "emoji": "🧱"}]}, ["🩺", "🔬"], ["KULAKÇIK", "KARINCIK", "SEPTUM 🧱"])
S(2, {"type": "bullets", "title": "Kapakçıklar", "items": ["Kalpte dört kapakçık var", "Her atışta açılıp kapanır", "Kapılar gibi çalışır 🚪"]}, ["🚪", "🔋"], ["KAPAKÇIK 🚪", "PİL KAPAĞI 😄"])
S(3, {"type": "diagram", "title": "Küçük dolaşım: akciğerlere", "layout": "flow", "nodes": [{"label": "Vücuttan gelen kan", "emoji": "🔵"}, {"label": "Sağ kulakçık", "emoji": "⬆️"}, {"label": "Sağ karıncık", "emoji": "⬇️"}, {"label": "Akciğerler: oksijen al", "emoji": "🫁"}]}, ["🩸", "💨"], ["SAĞ KULAKÇIK", "SAĞ KARINCIK → AKCİĞER", "OKSİJEN AL 🫁"])
S(1, {"type": "big-number", "value": "Küçük dolaşım", "label": "Kalp → akciğerler → kalp", "sub": "Kısa tur", "icon": "🫁"}, ["🔄", "💓"], ["KISA TUR 🔄"])
S(3, {"type": "diagram", "title": "Büyük dolaşım: bütün vücuda", "layout": "flow", "nodes": [{"label": "Sol kulakçık", "emoji": "⬆️"}, {"label": "Sol karıncık", "emoji": "💪"}, {"label": "Aort: en büyük atardamar", "emoji": "🔴"}, {"label": "Bütün vücut", "emoji": "🧍"}]}, ["🩸", "🏃"], ["SOL KULAKÇIK", "SOL KARINCIK 💪", "AORT → BÜYÜK DOLAŞIM"])
S(2, {"type": "comparison", "title": "Damar türleri", "left": {"title": "Atardamar 🔴", "items": ["Kanı kalpten uzağa taşır"]}, "right": {"title": "Toplardamar 🔵", "items": ["Kanı kalbe geri getirir", "Kılcal damarlar ikisini bağlar"]}}, ["🩸", "🔬"], ["ATAR / TOPLAR", "KILCAL DAMAR"])
S(1, {"type": "spotlight", "title": "Lub-dub!", "emoji": "🥁", "chips": [{"label": "Lub: bir grup kapakçık kapanır", "emoji": "🚪"}, {"label": "Dub: öteki grup kapanır", "emoji": "🚪"}]}, ["🩺", "🎵"], ["LUB-DUB 🥁"])
S(3, {"type": "diagram", "title": "Kalbin doğal pili", "layout": "flow", "nodes": [{"label": "Sinüs düğümü", "emoji": "⚡"}, {"label": "Elektrik sinyali", "emoji": "〰️"}, {"label": "Kalp kası kasılır", "emoji": "💓"}]}, ["🔋", "🤖"], ["SİNÜS DÜĞÜMÜ ⚡", "DOĞAL PİL 🔋", "KARDEŞİZ! 🤖"])
S(1, {"type": "big-number", "value": "100.000", "label": "Bir günde yaklaşık bu kadar atış", "sub": "Britanya Kalp Vakfı", "icon": "🗓️"}, ["💓", "⏱️"], ["HER GÜN!"])
S(1, {"type": "spotlight", "title": "Koşunca neden hızlanır?", "emoji": "🏃", "chips": [{"label": "Kaslar daha çok oksijen ister", "emoji": "💪"}, {"label": "Kalp daha hızlı pompalar", "emoji": "💓"}]}, ["👟", "🫁"], ["DAHA ÇOK OKSİJEN"])
S(2, {"type": "bullets", "title": "Kalbini koru", "items": ["Her gün en az 60 dakika hareket (6–17 yaş)", "Dengeli beslen", "Sigaradan uzak dur"]}, ["⚽", "🥗", "🚭"], ["HER GÜN HAREKET ⚽", "DENGELİ BESLEN 🥗"])
S(3, {"type": "diagram", "title": "Sen de dene: nabzını ölç", "layout": "flow", "nodes": [{"label": "İki parmak bileğe", "emoji": "✌️"}, {"label": "Otuz saniye say, ikiyle çarp", "emoji": "⏱️"}, {"label": "Yirmi kez zıpla", "emoji": "🤸"}, {"label": "Yeniden say: arttı mı?", "emoji": "📈"}]}, ["📓", "💓"], ["NABIZ ✌️", "SAY VE ÇARP ⏱️", "ZIPLA! 🤸"])
S(1, {"type": "bullets", "title": "Unutma", "items": ["Kendini zorlama", "Yorulursan dinlen"], "tone": "caution"}, ["⚠️", "💧"], ["ZORLAMA ⚠️"])
S(1, {"type": "spotlight", "title": "Atışın sırası", "emoji": "💓", "chips": [{"label": "Sinyal önce kulakçıkları kasar", "emoji": "⚡"}, {"label": "Düzenli, eşgüdümlü ritim", "emoji": "🎼"}]}, ["🥁", "〰️"], ["BUNU BİLİYOR MUYDUN?"])
S(3, {"type": "hook", "question": "Kanı akciğerlere hangi odacık pompalar?", "emoji": "🤔"}, ["🫁", "❤️"], ["HIZLI SORU!", "SAĞ KARINCIK ✅", "EK ŞARJ! 🔋"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 9, "videoTitle": "Kalbimiz nasıl çalışır?", "paperTitleTr": "Kalbimiz nasıl çalışır?",
  "takeaways": ["Kalp dört odacıklı bir kas pompasıdır", "Sağ taraf kanı akciğerlere, sol taraf bütün vücuda pompalar", "Sinüs düğümünün elektrik sinyali kalbi attırır"],
  "description": "Yumruk kadar bir kas, kanı bütün vücuda nasıl ulaştırır? Bu bölümde kalbin dört odacığını, kapakçıkları, küçük ve büyük dolaşımı; atardamar, toplardamar ve kılcal damarları; lub-dub sesinin nereden geldiğini ve kalbin doğal pili olan sinüs düğümünü keşfediyoruz. Koşunca kalbimiz neden hızlanır, kalbimizi nasıl koruruz? Sonunda nabız ölçme deneyi ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Kulakçık", "meaning": "Kalbin üstteki iki odacığından her biri; kalbe gelen kanı alır."},
    {"term": "Karıncık", "meaning": "Kalbin alttaki iki odacığından her biri; kanı kalpten dışarı pompalar."},
    {"term": "Septum", "meaning": "Kalbin sağ ve sol tarafını ayıran kas duvar."},
    {"term": "Kapakçık", "meaning": "Kalpte her atışta açılıp kapanan, kapı gibi çalışan yapı."},
    {"term": "Aort", "meaning": "Kalpten çıkan, vücudun en büyük atardamarı."},
    {"term": "Atardamar", "meaning": "Kanı kalpten uzağa taşıyan damar."},
    {"term": "Toplardamar", "meaning": "Kanı kalbe geri getiren damar."},
    {"term": "Kılcal damar", "meaning": "En küçük atardamarları en küçük toplardamarlara bağlayan çok ince damar."},
    {"term": "Sinüs düğümü", "meaning": "Sağ kulakçığın duvarında, kalbi attıran elektrik sinyalini başlatan doku."}],
  "song": e.song("Göğsümdeki Pompa", [("❤️", "Kalp"), ("🫁", "Akciğer"), ("🔴", "Atardamar"), ("🔵", "Toplardamar"), ("⚡", "Sinüs düğümü")],
    ["Yumruk kadar bir kas, göğsümde atar", "Dört odacığı var, kapakçıklar açılır", "Sağ taraf kanı akciğere yollar", "Kan oksijen alır, geri döner"],
    ["Lub-dub, lub-dub, durmadan atar!", "Kalbim kanı vücuda pompalar", "Atardamar götürür, toplardamar getirir", "Kılcal damarlar ikisini birleştirir"],
    ["Sol karıncık kanı aorta iter", "Sinüs düğümü sinyali verir", "Koşunca kaslarım oksijen ister", "Kalbim hızlanır, yetiştirir"],
    ["Lub-dub, lub-dub, durmadan atar!", "Kalbim kanı vücuda pompalar", "Her gün hareket et, kalbini koru", "Muma'yla öğrendik, hey!"])}
e.write(D, facts, script)
