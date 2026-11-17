"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:kanimiz-ne-ise-yarar"
KH = "Nemours KidsHealth — Blood"; AS = "American Society of Hematology — Blood Basics"; ML = "MedlinePlus (NIH) — Blood"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Blood", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/blood.html"},
    {"id": "k2", "title": "Blood Basics", "publisher": "Amerikan Hematoloji Derneği", "url": "https://www.hematology.org/education/patients/blood-basics"},
    {"id": "k3", "title": "Blood", "publisher": "MedlinePlus", "url": "https://medlineplus.gov/blood.html"}],
  "facts": [
    F(1, "Kanın dört ana bileşeni vardır: plazma, alyuvarlar, akyuvarlar ve trombositler.", "It has four main components: plasma, red blood cells, white blood cells, and platelets.", AS),
    F(2, "Plazma; besinler, proteinler, hormonlar ve atık maddeler içeren sarımsı bir sıvıdır; kanın yarısından fazlası plazmadır; kan yaklaşık yüzde 55 plazma ve yüzde 45 kan hücresinden oluşan bir karışımdır.", "Plasma (pronounced: PLAZ-muh) is a yellowish fluid that has nutrients, proteins, hormones, and waste products. / Over half of your blood is plasma. / a mixture of about 55% plasma and 45% blood cells.", KH + "; " + ML + "; " + AS, ["55", "45"]),
    F(3, "Kanın görevi oksijeni ve besinleri vücudun her yerine götürmektir; kan karbondioksiti ve diğer atıkları akciğerlere, böbreklere ve sindirim sistemine taşır.", "The function of blood is to bring oxygen and nutrients to all the parts of the body so they can keep working. / Blood carries carbon dioxide and other waste materials to the lungs, kidneys, and digestive system", KH),
    F(4, "Alyuvarlar oksijen taşıyan hemoglobin proteinini içerir; hemoglobin akciğerlerde oksijen alınca kan parlak kırmızı rengini alır; alyuvarlar oksijeni akciğerlerden doku ve organlara götürür.", "a protein that carries oxygen. / Blood gets its bright red color when hemoglobin picks up oxygen in the lungs. / Red blood cells (RBC) deliver oxygen from your lungs to your tissues and organs.", KH + "; " + ML),
    F(5, "Alyuvar, ortası basık, iki yüzü içe çökük bir disk biçimindedir.", "The shape of a red blood cell is a biconcave disk with a flattened center", AS),
    F(6, "Bir alyuvar ortalama 120 gün yaşar.", "A red blood cell survives an average of 120 days. / Red blood cells live about 120 days", AS + "; " + ML, ["120"]),
    F(7, "Farklı türdeki akyuvarlar bakteri ve virüs gibi mikroplarla savaşır; akyuvarlar vücudu enfeksiyondan korur.", "Different types of white blood cells (WBCs) fight germs, such as bacteria and viruses. / White blood cells protect the body from infection.", KH + "; " + AS),
    F(8, "Trombositler pıhtılaşmaya yardım eden minik hücrelerdir; bir kan damarı yırtılınca o bölgede toplanıp sızıntıyı kapatmaya yardım ederler.", "are tiny oval-shaped cells that help in the clotting process. / When a blood vessel breaks, platelets gather in the area and help seal off the leak.", KH),
    F(9, "Kemiklerin içindeki süngerimsi madde olan kemik iliği yeni kan hücreleri yapar.", "Bone marrow, the spongy material inside your bones, makes new blood cells. / RBCs are made in the inside part of bones called the bone marrow.", ML + "; " + KH),
    F(10, "Toplam vücut ağırlığının yaklaşık yüzde 7 ile 8'i kandır.", "About 7% to 8% of your total body weight is blood.", AS, ["7", "8"]),
    F(11, "Kalp her atışta kanı vücuda pompalar; atardamarlar oksijenli kanı kalpten vücudun geri kalanına taşır; kan toplardamarlarla kalbe ve akciğerlere geri döner.", "With each heartbeat, the heart pumps blood throughout our bodies, carrying oxygen to every cell. / Arteries carry oxygenated blood (blood that has gotten oxygen from the lungs) from the heart to the rest of the body. / Blood then travels through veins back to the heart and lungs", KH),
    F(12, "Dört kan grubu vardır: A, B, AB ya da O; ayrıca kan Rh pozitif ya da Rh negatiftir.", "There are four blood types: A, B, AB, or O. / Also, blood is either Rh-positive or Rh-negative.", ML),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; ML_ = "Medlayn Plas"
e.sec("hook", [
    L("Dizini sıyırdığında kırmızı bir damla belirir. Birkaç gün sonra da yerinde bir kabuk oluşur. Bu kırmızı sıvı ne, ve o kabuğu kim yaptı?", [8]),
    L("Kan, vücudunda hiç durmadan dolaşan bir taşıma ağıdır."),
    L("Bugün minicik olup bir kan damarının içinde yolculuğa çıkıyoruz!", [11]),
])
e.sec("context", [
    L("Üç sorumuz var. Kan neyden oluşur? Hangi hücre ne iş yapar? Ve kan nerede üretilir?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre kanın görevi, oksijeni ve besinleri vücudunun her yerine götürmektir. Böylece her bölüm çalışmaya devam eder.", [3], f"{KHs}'e göre kanın görevi, oksijeni ve besinleri vücudunun her yerine götürmektir. Böylece her bölüm çalışmaya devam eder."),
    L("Kan dönüşte karbondioksiti ve diğer atıkları akciğerlere, böbreklere ve sindirim sistemine taşır.", [3]),
    L("Benim damarlarımda kan yok, kablo var. Ben de elektrik taşırım, ama kabuk bağlamam!"),
    L("Amerikan Hematoloji Derneği'ne göre kanın dört ana bileşeni var: plazma, alyuvarlar, akyuvarlar ve trombositler.", [1]),
    L("Kan yaklaşık yüzde 55 plazma ve yüzde 45 kan hücresinden oluşur.", [2], "Kan yaklaşık yüzde elli beş plazma ve yüzde kırk beş kan hücresinden oluşur."),
    L("Plazma sarımsı bir sıvıdır. İçinde besinler, proteinler, hormonlar ve atık maddeler taşır.", [2]),
])
e.sec("finding", [
    L("Kana kırmızı rengini veren alyuvarlardır. Alyuvarların içinde hemoglobin denen, oksijen taşıyan bir protein vardır.", [4]),
    L("Hemoglobin akciğerlerde oksijeni yakalayınca kan parlak kırmızı olur. Sonra alyuvarlar bu oksijeni dokulara ve organlara götürür.", [4]),
    L("Alyuvar, ortası basık bir disk gibidir; iki yüzü de içe doğru çöküktür.", [5]),
    L("MedlinePlus'a göre bir alyuvar yaklaşık 120 gün yaşar.", [6], f"{ML_}'a göre bir alyuvar yaklaşık yüz yirmi gün yaşar."),
    L("Benim pilim yüz yirmi gün dayansaydı, ne güzel olurdu!"),
    L("Akyuvarlar vücudun savunma ekibidir. Farklı türdeki akyuvarlar bakteri ve virüs gibi mikroplarla savaşır.", [7]),
    L("Trombositler ise minik tamircilerdir. Bir kan damarı yırtılınca o bölgede toplanır ve sızıntıyı kapatmaya yardım ederler.", [8]),
    L("Buna pıhtılaşma denir. Dizindeki o kabuk da pıhtılaşmanın bir parçasıdır.", [8]),
])
e.sec("importance", [
    L("Peki bu hücreler nerede üretilir? Kemiklerinin içindeki süngerimsi madde olan kemik iliğinde!", [9]),
    L("Kemik iliği sürekli yeni kan hücreleri yapar. Böylece eskiyen hücrelerin yerine yenileri gelir.", [9, 6]),
    L("Kanı dolaştıran ise kalptir. Kalp her atışta kanı tüm vücuduna pompalar.", [11]),
    L("Atardamarlar, akciğerlerden oksijen almış kanı kalpten vücudun geri kalanına taşır.", [11]),
    L("Kan sonra toplardamarlarla kalbe ve akciğerlere geri döner. Böylece döngü yeniden başlar.", [11]),
    L("Herkesin bir kan grubu vardır. MedlinePlus'a göre dört kan grubu var: A, B, AB ve O. Kan ayrıca Rh pozitif ya da Rh negatiftir.", [12], f"Herkesin bir kan grubu vardır. {ML_}'a göre dört kan grubu var: A, B, A B ve O. Kan ayrıca R h pozitif ya da R h negatiftir."),
    L("Benim kan grubum yok. Olsa olsa yağ grubum var!"),
    L("Şimdi sıra sende! Kalbinin pompaladığı kanı hissedebilirsin. İki parmağını bileğinin iç tarafına, başparmak hizasına hafifçe koy.", [11]),
    L("Hafif vuruşları hissediyor musun? Her vuruş, kalbinin bir atışıdır. Bir de zıpladıktan sonra dene: vuruşlar değişiyor mu?", [11]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Amerikan Hematoloji Derneği'ne göre vücut ağırlığının yaklaşık yüzde 7 ile 8'i kandır!", [10], "Bunu biliyor muydun? Amerikan Hematoloji Derneği'ne göre vücut ağırlığının yaklaşık yüzde yedi ile sekizi kandır!"),
    L("Hızlı soru! Alyuvarların içinde oksijen taşıyan proteinin adı neydi?", [4]),
    L("Düşün bakalım... Evet: hemoglobin!", [4]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Kalbin hep neşeyle atsın!"),
])
S = e.S
S(3, {"type": "hook", "question": "Kanımız ne işe yarar?", "emoji": "🩸"}, ["🩹", "❤️"], ["KIRMIZI DAMLA", "TAŞIMA AĞI", "DAMAR YOLCULUĞU"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Kan neyden oluşur?", "Hangi hücre ne iş yapar?", "Kan nerede üretilir?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(3, {"type": "diagram", "title": "Kanın işi", "layout": "cycle", "nodes": [{"label": "Oksijen ve besin götürür", "emoji": "🫁"}, {"label": "Hücreler çalışır", "emoji": "⚙️"}, {"label": "Atıkları geri taşır", "emoji": "♻️"}]}, ["🔌", "🫁"], ["OKSİJEN + BESİN", "ATIKLAR", "KABLOLU MUMA 🔌"])
S(3, {"type": "bar-chart", "title": "Kanın bileşimi (%)", "unit": "%", "bars": [{"label": "Plazma", "value": 55, "display": "%55", "highlight": True}, {"label": "Kan hücreleri", "value": 45, "display": "%45"}]}, ["💧", "🔴"], ["DÖRT BİLEŞEN", "PLAZMA %55", "SARIMSI SIVI"])
S(3, {"type": "spotlight", "title": "Alyuvar", "emoji": "🔴", "chips": [{"label": "Hemoglobin: oksijen taşır", "emoji": "🫁"}, {"label": "Kana kırmızı renk", "emoji": "🎨"}, {"label": "Ortası basık disk", "emoji": "💿"}]}, ["🫁", "🔴"], ["HEMOGLOBİN", "PARLAK KIRMIZI", "DİSK 💿"])
S(2, {"type": "big-number", "value": "120 gün", "label": "Bir alyuvarın ortalama ömrü", "sub": "MedlinePlus", "icon": "🔴"}, ["⏳", "🔋"], ["120 GÜN", "PİL ÖMRÜ 🔋"])
S(3, {"type": "comparison", "title": "Savunma ve tamir", "left": {"title": "Akyuvar 🛡️", "items": ["Bakteri ve virüslerle savaşır"]}, "right": {"title": "Trombosit 🩹", "items": ["Yırtılan damarda toplanır", "Sızıntıyı kapatır: pıhtılaşma"]}}, ["🦠", "🩹"], ["AKYUVARLAR", "TROMBOSİTLER", "KABUK 🩹"], fx="sparkle")
S(2, {"type": "meter", "title": "Kemik iliği", "label": "Yeni hücre", "emoji": "🦴", "phases": [{"label": "Süngerimsi madde", "level": 0.4, "emoji": "🧽"}, {"label": "Sürekli yeni kan hücresi", "level": 0.9, "emoji": "🏭"}], "note": NOTE}, ["🦴", "🏭"], ["KEMİK İLİĞİ", "FABRİKA 🏭"])
S(3, {"type": "stages", "title": "Kanın turu", "rows": [{"label": "Kalp pompalar", "emoji": "❤️"}, {"label": "Atardamarlar: vücuda", "emoji": "➡️"}, {"label": "Toplardamarlar: geri", "emoji": "⬅️"}, {"label": "Kalp ve akciğerler", "emoji": "🫁"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 0, "note": "Şematik çizim."}, [], ["KALP ❤️", "ATARDAMAR", "TOPLARDAMAR"])
S(2, {"type": "spotlight", "title": "Kan grupları", "emoji": "🅰️", "chips": [{"label": "A, B, AB, O", "emoji": "🩸"}, {"label": "Rh pozitif ya da negatif", "emoji": "➕"}]}, ["🩸", "🛢️"], ["KAN GRUBU", "YAĞ GRUBU 🛢️"])
S(2, {"type": "bullets", "title": "Sen de dene: nabzını bul", "items": ["İki parmak bileğin iç tarafına", "Hafifçe bastır", "Vuruşları hisset", "Zıpladıktan sonra tekrar dene"]}, ["❤️", "⏱️"], ["DENEY ZAMANI 🔬", "HER VURUŞ BİR ATIŞ"])
S(1, {"type": "big-number", "value": "%7–8", "label": "Vücut ağırlığının kan olan payı", "sub": "Amerikan Hematoloji Derneği", "icon": "⚖️"}, ["⚖️", "🩸"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Oksijen taşıyan proteinin adı ne?", "emoji": "🤔"}, ["🔴", "🫁"], ["HIZLI SORU!", "HEMOGLOBİN ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 34, "videoTitle": "Kanımız ne işe yarar?", "paperTitleTr": "Kanımız ne işe yarar?",
  "theme": {"backdrop": "micro", "actors": [{"kind": "swim", "emoji": "🔴", "every": 30}]},
  "takeaways": ["Kan; plazma, alyuvar, akyuvar ve trombositlerden oluşur", "Alyuvarlar hemoglobinle oksijen taşır, akyuvarlar mikroplarla savaşır, trombositler yarayı kapatır", "Kan hücrelerini kemik iliği yapar, kalp kanı vücuda pompalar"],
  "description": "Kanımız neyden oluşur ve ne işe yarar? Bu bölümde plazmayı, hemoglobinle oksijen taşıyan alyuvarları, mikroplarla savaşan akyuvarları, yarayı kapatan trombositleri, kan hücrelerini üreten kemik iliğini, atardamar ve toplardamarlarla kanın turunu ve kan gruplarını keşfediyoruz. Sonunda nabız bulma etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Plazma", "meaning": "Kanın sıvı bölümü; besin, protein, hormon ve atık taşır."},
    {"term": "Alyuvar", "meaning": "Hemoglobin sayesinde oksijen taşıyan kırmızı kan hücresi."},
    {"term": "Hemoglobin", "meaning": "Alyuvarlarda oksijen taşıyan protein."},
    {"term": "Akyuvar", "meaning": "Mikroplarla savaşan beyaz kan hücresi."},
    {"term": "Trombosit", "meaning": "Yırtılan damarda toplanıp pıhtılaşmaya yardım eden minik hücre."},
    {"term": "Kemik iliği", "meaning": "Kemiklerin içindeki, kan hücrelerini üreten süngerimsi madde."},
    {"term": "Atardamar", "meaning": "Kanı kalpten vücuda taşıyan damar."},
    {"term": "Toplardamar", "meaning": "Kanı vücuttan kalbe geri getiren damar."}],
  "song": e.song("Kırmızı Nehir", [("🩸", "Kan"), ("🔴", "Alyuvar"), ("🛡️", "Akyuvar"), ("🩹", "Trombosit"), ("❤️", "Kalp")],
    ["Kalp pompalar, kan yola çıkar", "Atardamardan vücuda akar", "Plazma taşır besinleri", "Toplardamardan geri döner"],
    ["Kırmızı nehir, durmadan akar!", "Alyuvar oksijen taşır", "Hemoglobinle parlak kırmızı", "Her hücreye hayat taşır"],
    ["Akyuvar savaşır mikropla", "Trombosit kapatır yarayı", "Kemik iliği yapar yenisini", "Kabuk bağlar dizimde"],
    ["Kırmızı nehir, durmadan akar!", "Alyuvar oksijen taşır", "Bileğine dokun, nabzını say", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "swim", "emoji": "🔴"}, {"kind": "hop", "emoji": "❤️"}, {"kind": "swim", "emoji": "🛡️"}, {"kind": "hop", "emoji": "🩹"}])}
e.write(D, facts, script)
