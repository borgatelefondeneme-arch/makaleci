"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:beynimiz-nasil-calisir"
KH = "Nemours KidsHealth — All About the Brain & Nervous System"; BF = "BrainFacts (Society for Neuroscience) — The Neuron"; NH = "NIH (NHLBI) — Why Is Sleep Important?"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "All About the Brain & Nervous System", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/brain.html"},
    {"id": "k2", "title": "The Neuron", "publisher": "BrainFacts", "url": "https://www.brainfacts.org/brain-anatomy-and-function/anatomy/2012/the-neuron"},
    {"id": "k3", "title": "Why Is Sleep Important?", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"}],
  "facts": [
    F(1, "Beyin ne düşündüğünü ve hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.", "The brain controls what you think and feel, how you learn and remember, and the way you move and talk.", KH),
    F(2, "Beyin ve omurilik kemikle korunur: beyin kafatası kemikleriyle; ayrıca meninks denen zar katmanları ve beyin omurilik sıvısıyla yastıklanır.", "the brain by the bones of the skull / cushioned by layers of membranes called meninges and a special fluid called cerebrospinal fluid.", KH),
    F(3, "Büyük beynin sağ ve sol yarısı vardır, bunlara yarım küre denir; dört lobu vardır: alın, yan, şakak ve art kafa lobu.", "The cerebrum has right and left halves, called hemispheres. / These are called lobes, and there are four of them: the frontal, parietal, temporal, and occipital lobes.", KH),
    F(4, "Alın lobu karmaşık düşünmenin çoğunu yapar; yan lob dokunma, tat ve sıcaklık bilgisini işler; şakak lobu sesleri ve dili anlamamızı sağlar; art kafa lobu gözlerden gelen görsel bilgiyi işler.", "The frontal lobe, located behind the forehead, does much of the work of complex thinking / The parietal lobe, located behind the frontal lobe, processes information about touch, taste, and temperature. / The temporal lobe, found near the ears, lets us understand sounds and language / The occipital lobe, in the rear of the brain, processes light and other visual information from the eyes", KH),
    F(5, "Beyincik denge, hareket ve koordinasyondan sorumludur; beyin sapı nefes alma, kalp atışı, kan basıncı ve yutma gibi otomatik işlevleri kontrol eder.", "is responsible for balance, movement, and coordination. / It also controls many of the body's automatic functions, like breathing, heart rate, blood pressure, swallowing", KH),
    F(6, "Nöron, beynin temel çalışma birimidir; bilgi iletmek için özelleşmiş bir hücredir; nöronların çoğunda hücre gövdesi, akson ve dendritler bulunur.", "The neuron is the basic working unit of the brain, a specialized cell designed to transmit information / Most neurons have a cell body, an axon, and dendrites.", BF),
    F(7, "Dendritler hücre gövdesinden uzanır ve diğer nöronlardan mesaj alır; akson elektrik uyarılarını iletir; sinapslar bir nöronun diğeriyle iletişim kurduğu temas noktalarıdır; nöronlar bilgiyi elektrokimyasal bir süreçle aktarır.", "Dendrites extend from the neuron cell body and receive messages from other neurons. / they transmit electrical impulses along their axons / Synapses are the contact points where one neuron communicates with another. / All neurons relay information to each other through a complex electrochemical process", BF + "; " + KH),
    F(8, "Aksonların boyu santimetrenin küçük bir kesrinden yaklaşık bir metreye ya da daha fazlasına kadar değişebilir; birçok akson elektrik sinyallerinin iletimini hızlandıran katmanlı bir miyelin kılıfla kaplıdır.", "which can range in length from a tiny fraction of an inch (or centimeter) to three feet (about one meter) or more. / Many axons are covered with a layered myelin sheath, which accelerates the transmission of electrical signals", BF),
    F(9, "Beyinde milyarlarca nöron vardır; beyin, nörondan en az on kat fazla glia hücresi içerir.", "The brain has billions of them, and they have many specialized jobs. / The brain contains at least ten times more glia than neurons.", KH + "; " + BF, ["10"]),
    F(10, "Büyüyüp öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider; bu yüzden araba sürmek ilk öğrenirken çok dikkat ister ama sonra kendiliğinden yapılır; beyinde dolaşan mesajlar belleğin temeli olan yollar oluşturur.", "As you grow and learn, messages travel from one neuron to another over and over, / It's why driving takes so much concentration when someone first learns, but later it is second nature. / As these messages travel through the brain, they too create pathways that serve as the basis of memory.", KH),
    F(11, "Birçok bilim insanı beyni yeni şeyler öğrenmeye ve yeni bağlantılar kurmaya zorlamanın önemli olduğuna inanır.", "Many scientists believe it's important to keep challenging it to learn new things and make new connections", KH),
    F(12, "Uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder; yeterince ya da kaliteli uyumamak odaklanmayı ve net düşünmeyi zorlaştırabilir.", "Sleep helps with learning and the formation of long-term memories. / Not getting enough sleep or enough high-quality sleep can lead to problems focusing on tasks and thinking clearly.", NH),
]}
e = Ep(); L = e.L
KHs = "Kids Helt"; EN = "En Ay Eyç"; BFs = "Breyn Fekts"
e.sec("hook", [
    L("Şu an bu cümleyi duyuyor, anlıyor ve hatırlıyorsun. Bunu yapan, kafatasının içindeki organ: beynin!", [1]),
    L("Beyin bu kadar işi nasıl yapar? Ve yeni bir şey öğrendiğinde içinde ne değişir?"),
    L("Bugün beyninin içine, sinir hücrelerinin dünyasına gidiyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Beynin bölümleri ne iş yapar? Sinir hücreleri nasıl haberleşir? Ve öğrendiğimizde ne olur?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("KidsHealth'e göre beyin; ne düşündüğünü, ne hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder.", [1], f"{KHs}'e göre beyin; ne düşündüğünü, ne hissettiğini, nasıl öğrenip hatırladığını, nasıl hareket edip konuştuğunu kontrol eder."),
    L("Bu değerli organı kafatası korur. Ayrıca zar katmanları ve özel bir sıvı onu yastık gibi sarar.", [2]),
    L("En büyük bölüm büyük beyindir. Sağ ve sol iki yarıya ayrılır; bunlara yarım küre denir.", [3]),
    L("Büyük beynin dört lobu vardır. Alnının arkasındaki alın lobu, karmaşık düşünmenin çoğunu yapar.", [3, 4]),
    L("Yan lob dokunma, tat ve sıcaklık bilgisini işler. Kulaklarına yakın şakak lobu, sesleri ve dili anlamanı sağlar.", [4]),
    L("Başının arkasındaki art kafa lobu ise gözlerinden gelen görüntüleri işler.", [4]),
    L("Beyincik dengeni ve hareketlerinin uyumunu sağlar. Beyin sapı ise nefes alma ve kalp atışı gibi otomatik işleri yönetir.", [5]),
    L("Benim de bir işlemcim var. Ama dört lobu yok; olsa olsa dört düğmesi var!"),
])
e.sec("finding", [
    L("Şimdi beynin yapı taşlarına bakalım. BrainFacts'e göre beynin temel çalışma birimi nörondur: bilgi iletmek için özelleşmiş bir hücre.", [6], f"Şimdi beynin yapı taşlarına bakalım. {BFs}'e göre beynin temel çalışma birimi nörondur: bilgi iletmek için özelleşmiş bir hücre."),
    L("Beyninde milyarlarca nöron var.", [9]),
    L("Bir nöronun hücre gövdesi, dendritleri ve bir aksonu vardır. Dendritler başka nöronlardan gelen mesajları alır.", [6, 7]),
    L("Akson mesajı bir elektrik uyarısı olarak iletir. Bazı aksonlar santimetrenin küçük bir parçası kadar kısa, bazıları bir metreye kadar uzundur.", [7, 8]),
    L("Birçok akson, miyelin denen katmanlı bir kılıfla kaplıdır. Miyelin, elektrik sinyalini hızlandırır.", [8]),
    L("İki nöronun buluştuğu temas noktasına sinaps denir. Mesaj burada bir nörondan ötekine geçer.", [7]),
    L("Yani beynin, elektrik ve kimyasalları birlikte kullanan dev bir haberleşme ağıdır.", [7]),
])
e.sec("importance", [
    L("Peki öğrendiğinde ne olur? KidsHealth'e göre öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider.", [10], f"Peki öğrendiğinde ne olur? {KHs}'e göre öğrendikçe mesajlar bir nörondan ötekine tekrar tekrar gider."),
    L("Bu mesajlar beyninde yollar oluşturur ve bu yollar belleğin temelidir.", [10]),
    L("Bu yüzden yeni bir şey ilk başta çok dikkat ister, ama tekrar ettikçe kolaylaşır. Bisiklete binmeyi düşün!", [10]),
    L("Birçok bilim insanı, beyni hep yeni şeyler öğrenmeye zorlamanın önemli olduğuna inanır. Böylece yeni bağlantılar kurulur.", [11]),
    L("Uyku da çok önemli. Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.", [12], f"Uyku da çok önemli. Amerikan Ulusal Sağlık Enstitüleri, {EN}'ye göre uyku öğrenmeye ve uzun süreli anıların oluşmasına yardım eder."),
    L("Yeterince uyumazsan odaklanmak ve net düşünmek zorlaşabilir.", [12]),
    L("Ben uyumam, ama yeniden başlatınca ben de daha iyi düşünürüm!"),
    L("Şimdi sıra sende! Hiç denemediğin bir şeyi seç: örneğin ayakkabı bağını yeni bir yöntemle bağlamak.", [10]),
    L("Bir hafta boyunca her gün dene ve kaç saniyede yaptığını not et. Süre kısalıyor mu? İşte beynindeki yol güçleniyor!", [10]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? Beyninde, nöronlardan en az on kat fazla glia denen yardımcı hücre vardır.", [9]),
    L("Hızlı soru! İki nöronun buluştuğu temas noktasının adı neydi?", [7]),
    L("Düşün bakalım... Evet: sinaps!", [7]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bu gece de iyi uyu; beynin teşekkür edecek!"),
])
S = e.S
S(3, {"type": "hook", "question": "Beynimiz nasıl çalışır?", "emoji": "🧠"}, ["💡", "⚡"], ["", "ÖĞRENİNCE NE DEĞİŞİR?", "SİNİR HÜCRELERİ"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Beynin bölümleri ne iş yapar?", "Sinir hücreleri nasıl haberleşir?", "Öğrendiğimizde ne olur?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "spotlight", "title": "Beyin", "emoji": "🧠", "chips": [{"label": "Düşünme ve duygular", "emoji": "💭"}, {"label": "Öğrenme ve hatırlama", "emoji": "📚"}, {"label": "Hareket ve konuşma", "emoji": "🗣️"}, {"label": "Kafatası ve sıvıyla korunur", "emoji": "🛡️"}]}, ["💡", "🛡️"], ["KONTROL MERKEZİ", "KORUNUR 🛡️"])
S(3, {"type": "stages", "title": "Büyük beynin dört lobu", "rows": [{"label": "Alın lobu: düşünme", "emoji": "💭"}, {"label": "Yan lob: dokunma, tat, sıcaklık", "emoji": "✋"}, {"label": "Şakak lobu: ses ve dil", "emoji": "👂"}, {"label": "Art kafa lobu: görme", "emoji": "👁️"}], "path": [0, 0, 1, 1, 2, 2, 3, 3], "highlightRow": 0, "note": "Şematik çizim."}, [], ["YARIM KÜRELER", "ALIN LOBU", "YAN VE ŞAKAK LOBU"])
S(1, {"type": "big-number", "value": "Art kafa lobu", "label": "Gözlerden gelen görüntüleri işler", "sub": "KidsHealth", "icon": "👁️"}, ["🖼️", "🧠"], ["GÖRME 👁️"])
S(2, {"type": "comparison", "title": "Beyincik ve beyin sapı", "left": {"title": "Beyincik ⚖️", "items": ["Denge", "Hareket uyumu"]}, "right": {"title": "Beyin sapı 🫀", "items": ["Nefes alma", "Kalp atışı"]}}, ["🤸", "🤖"], ["OTOMATİK İŞLER", "DÖRT DÜĞME 😅"])
S(2, {"type": "spotlight", "title": "Nöron", "emoji": "🔌", "chips": [{"label": "Beynin temel birimi", "emoji": "🧱"}, {"label": "Bilgi iletir", "emoji": "📨"}, {"label": "Milyarlarca nöron", "emoji": "🔢"}]}, ["🧠", "⚡"], ["NÖRON", "MİLYARLARCA"])
S(3, {"type": "diagram", "title": "Mesajın yolculuğu", "layout": "flow", "nodes": [{"label": "Dendrit: mesajı alır", "emoji": "🌿"}, {"label": "Hücre gövdesi", "emoji": "⚪"}, {"label": "Akson: elektrik uyarısı", "emoji": "⚡"}, {"label": "Miyelin hızlandırır", "emoji": "🚀"}]}, ["📨", "🧠"], ["DENDRİT", "AKSON ⚡", "MİYELİN"])
S(2, {"type": "meter", "title": "Sinaps", "label": "Mesaj", "emoji": "✉️", "phases": [{"label": "İki nöronun temas noktası", "level": 0.5, "emoji": "🤝"}, {"label": "Elektrik + kimya: dev ağ", "level": 0.9, "emoji": "🕸️"}], "note": NOTE}, ["⚡", "🧪"], ["SİNAPS", "ELEKTROKİMYASAL AĞ"])
S(3, {"type": "diagram", "title": "Öğrenince ne olur?", "layout": "flow", "nodes": [{"label": "Mesaj tekrar tekrar gider", "emoji": "🔁"}, {"label": "Beyinde yol oluşur", "emoji": "🛤️"}, {"label": "Bellek", "emoji": "💾"}, {"label": "İş kolaylaşır", "emoji": "🚲"}]}, ["📚", "🧠"], ["TEKRAR 🔁", "YOLLAR = BELLEK", "BİSİKLET 🚲"])
S(1, {"type": "spotlight", "title": "Yeni şeyler öğren", "emoji": "🧩", "chips": [{"label": "Beyni zorla", "emoji": "💪"}, {"label": "Yeni bağlantılar", "emoji": "🔗"}]}, ["📖", "🎨"], ["YENİ BAĞLANTILAR"])
S(3, {"type": "comparison", "title": "Uyku ve öğrenme", "left": {"title": "Yeterli uyku 😴", "items": ["Öğrenmeye yardım eder", "Uzun süreli anılar"]}, "right": {"title": "Az uyku 🥱", "items": ["Odaklanmak zor", "Net düşünmek zor"]}}, ["🌙", "🤖"], ["UYKU 😴", "AZ UYKU 🥱", "YENİDEN BAŞLAT 🔄"])
S(2, {"type": "bullets", "title": "Sen de dene: yeni beceri", "items": ["Hiç denemediğin bir şey seç", "Bir hafta her gün dene", "Süreyi not et", "Süre kısalıyor mu?"]}, ["⏱️", "📓"], ["DENEY ZAMANI 🔬", "YOL GÜÇLENİYOR 🛤️"])
S(1, {"type": "big-number", "value": "10 kat", "label": "Gliadan, nörondan en az bu kadar fazla", "sub": "BrainFacts", "icon": "🧠"}, ["🔬", "✨"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "İki nöronun buluştuğu noktanın adı ne?", "emoji": "🤔"}, ["🧠", "🤝"], ["HIZLI SORU!", "SİNAPS ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 27, "videoTitle": "Beynimiz nasıl çalışır?", "paperTitleTr": "Beynimiz nasıl çalışır?",
  "theme": {"backdrop": "micro", "actors": []},
  "takeaways": ["Beynin lobları, beyinciği ve beyin sapı farklı işler yapar", "Nöronlar elektrik ve kimyasallarla sinapslarda haberleşir", "Tekrar ve uyku öğrenmeyi güçlendirir"],
  "description": "Beynimiz düşünmeyi, hatırlamayı ve hareket etmeyi nasıl yönetir? Bu bölümde büyük beynin yarım kürelerini ve dört lobunu, beyinciği ve beyin sapını; nöronları, dendritleri, aksonları, miyelini ve sinapsları keşfediyoruz. Öğrendiğimizde beynimizde ne değişir, uyku neden önemlidir? Sonunda yeni beceri etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Büyük beyin", "meaning": "Beynin en büyük bölümü; iki yarım küreden ve dört lobdan oluşur."},
    {"term": "Lob", "meaning": "Büyük beynin farklı işler yapan bölümlerinden her biri."},
    {"term": "Beyincik", "meaning": "Dengeyi ve hareketlerin uyumunu sağlayan beyin bölümü."},
    {"term": "Beyin sapı", "meaning": "Nefes alma, kalp atışı gibi otomatik işleri yöneten bölüm."},
    {"term": "Nöron", "meaning": "Bilgi ileten sinir hücresi."},
    {"term": "Akson", "meaning": "Nöronun mesajı elektrik uyarısı olarak ileten uzun uzantısı."},
    {"term": "Miyelin", "meaning": "Aksonu saran ve sinyali hızlandıran kılıf."},
    {"term": "Sinaps", "meaning": "İki nöronun haberleştiği temas noktası."}],
  "song": e.song("Kafamdaki Ağ", [("🧠", "Beyin"), ("⚡", "Sinyal"), ("🤝", "Sinaps"), ("💾", "Bellek"), ("😴", "Uyku")],
    ["Alın lobu düşünür, şakak duyar", "Art kafa görür, yan lob dokunur", "Beyincik dengede tutar beni", "Beyin sapı nefesimi yönetir"],
    ["Nöron nörona mesaj yollar!", "Dendrit alır, akson iletir", "Sinapsta buluşur, ağ büyür", "Kafamda bir şehir ışıl ışıl"],
    ["Miyelin kılıf hızlandırır", "Tekrar ettikçe yollar açılır", "Yollar bellek olur, iş kolaylaşır", "Uyku gelir, anılar kalır"],
    ["Nöron nörona mesaj yollar!", "Dendrit alır, akson iletir", "Yeni bir şey dene, her gün biraz", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "hop", "emoji": "💡"}, {"kind": "hop", "emoji": "🧠"}, {"kind": "hop", "emoji": "⚡"}, {"kind": "hop", "emoji": "📚"}])}
e.write(D, facts, script)
