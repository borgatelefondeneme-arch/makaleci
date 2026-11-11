"""Manuel sağlayıcı yanıtları (Claude API anahtarı yokken): olgular, senaryo, sahne planı.
Çalıştırma: python3 <bu dosya>"""
import json, os
D = os.path.dirname(__file__)
PID = "topic:neden-uyuruz"
CDC = "CDC — About Sleep"
KH = "Nemours KidsHealth — Kids and Sleep"
NHLBI = "NIH (NHLBI) — Why Is Sleep Important?"
NHLBI2 = "NIH (NHLBI) — Your Sleep/Wake Cycle"
NIGMS = "NIH (NIGMS) — Circadian Rhythms"
SFC = "Sleep Foundation — What Is Circadian Rhythm?"
SFS = "Sleep Foundation — Stages of Sleep"
SFA = "Sleep Foundation — Adenosine and Sleep"
SFW = "Sleep Foundation — Why Is Sleep Important?"
WIKI = "Wikipedia — Suprachiasmatic nucleus"

def F(i, st, q, loc, nums=()):
    return {"id": f"f{i}", "kind": "number" if nums else "claim", "statement": st, "numbers": list(nums), "quote": q, "location": loc}

facts = {
    "paperId": PID, "basis": "full_text", "institutions": [],
    "sources": [
        {"id": "k1", "title": "About Sleep", "publisher": "CDC", "url": "https://www.cdc.gov/sleep/about/index.html"},
        {"id": "k2", "title": "Kids and Sleep", "publisher": "KidsHealth", "url": "https://kidshealth.org/en/kids/not-tired.html"},
        {"id": "k3", "title": "Why Is Sleep Important?", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"},
        {"id": "k4", "title": "Your Sleep/Wake Cycle", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/sleep/sleep-wake-cycle"},
        {"id": "k5", "title": "Circadian Rhythms", "publisher": "NIH", "url": "https://www.nigms.nih.gov/education/fact-sheets/Pages/circadian-rhythms"},
        {"id": "k6", "title": "What Is Circadian Rhythm?", "publisher": "Sleep Foundation", "url": "https://www.sleepfoundation.org/circadian-rhythm"},
        {"id": "k7", "title": "Stages of Sleep", "publisher": "Sleep Foundation", "url": "https://www.sleepfoundation.org/stages-of-sleep"},
        {"id": "k8", "title": "Adenosine and Sleep", "publisher": "Sleep Foundation", "url": "https://www.sleepfoundation.org/how-sleep-works/adenosine-and-sleep"},
        {"id": "k9", "title": "Why Is Sleep Important?", "publisher": "Sleep Foundation", "url": "https://www.sleepfoundation.org/how-sleep-works/why-do-we-need-sleep"},
        {"id": "k10", "title": "Suprachiasmatic nucleus", "publisher": "Wikipedia", "url": "https://en.wikipedia.org/wiki/Suprachiasmatic_nucleus"},
    ],
    "facts": [
        F(1, "Uyurken vücut, beynin sağlıklı çalışmasını ve beden sağlığını desteklemek için çalışır.", "During sleep, your body is working to support healthy brain function and maintain your physical health.", NHLBI),
        F(2, "Sirkadiyen ritimler, bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.", "Circadian rhythms include some of the physical, mental, and behavioral changes an organism experiences over a 24-hour cycle.", NIGMS, ["24"]),
        F(3, "İnsanda ana saat beyindedir; suprakiazmatik çekirdek (SCN) adlı yapıyı oluşturan büyük bir sinir hücresi grubudur.", "The human master clock is a large group of nerve cells that form a structure called the suprachiasmatic nucleus (SCN).", NIGMS),
        F(4, "SCN, beynin hipotalamus bölgesinde, görme sinirlerinin çaprazlaştığı yerin hemen üstündedir; binlerce nörondan oluşur.", "a small region of the brain in the hypothalamus, situated directly above the optic chiasm. ... It consists of two nuclei composed of approximately 10,000 neurons.", WIKI),
        F(5, "Sirkadiyen ritimleri en çok ışık ve karanlık etkiler.", "Light and dark have the biggest influence on circadian rhythms", NIGMS),
        F(6, "Gözlerle alınan ışık sinyalleri beyne gündüz olduğunu bildirir.", "light signals received through your eyes tell your brain that it is daytime.", NHLBI2),
        F(7, "Güneş batınca beyin uyku getiren melatonin hormonunu üretmeye başlar; kandaki melatonin akşam artar, sabaha karşı en yüksek düzeye çıkar.", "As the sun sets in the evening, the brain begins producing melatonin, a hormone that induces sleepiness. / The amount of melatonin in your bloodstream starts to increase in the evening and peaks in the early morning.", SFC + "; " + NHLBI2),
        F(8, "Uzun süre uyanık kaldıkça uyku ihtiyacı artar; bu ihtiyaç adenozin adlı bileşikle bağlantılıdır ve uyanıkken beyindeki adenozin düzeyi yükselir.", "Your body has a biological need for sleep that increases when you have been awake for a long time. A compound called adenosine is linked to this need for sleep. While you are awake, the level of adenosine in your brain continues to rise.", NHLBI2),
        F(9, "Uyurken beyin adenozini yeniden ATP'ye (enerji molekülüne) çevirir ve uyku baskısı ortadan kalkar.", "While you sleep, the brain converts adenosine back into ATP, essentially eliminating your sleep drive.", SFA),
        F(10, "Uyku dört evreden oluşur: üçü REM olmayan (N1, N2, N3), biri REM. Bir gecede dört ila altı döngü yaşanır; bir döngü ortalama 90 dakika sürer.", "one for rapid eye movement (REM) sleep and three that form non-REM (NREM) sleep / In a typical night, a person goes through four to six sleep cycles / on average they last about 90 minutes each.", SFS, ["90", "4", "6", "1", "2", "3"]),
        F(11, "Üçüncü evre (N3) derin uykudur; vücudun toparlanması ve büyümesi için kritik sayılır, bağışıklık sistemini de destekleyebilir.", "Stage 3 (N3 or deep sleep) ... Experts believe that this stage is critical to restorative sleep, allowing for bodily recovery and growth. It may also bolster the immune system", SFS, ["3"]),
        F(12, "Büyüme ve gelişme için gereken hormonlar REM olmayan uykunun üçüncü evresinde salgılanır; büyüme hormonu dokuların büyümesi ve onarılması için gereklidir.", "It's during this stage that the body releases hormones needed for growth and development. / Sleep provides the release of growth hormone necessary for the body's tissues to grow and repair damage.", KH + "; " + SFW),
        F(13, "REM uykusunda gözler kapalıyken hızla hareket eder; beyin etkinliği uyanıklık düzeyine yaklaşır; kaslar geçici olarak felç olur (atoni); en canlı rüyalar bu evrede görülür.", "brain activity picks up, nearing levels seen when you're awake. / the body experiences atonia, which is a temporary paralysis of the muscles / Even though they're closed, the eyes move rapidly / This is when we have our most vivid dreams.", SFS + "; " + KH),
        F(14, "REM uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir; uyku uzun süreli anıların oluşmasına yardım eder.", "REM sleep is believed to be essential to cognitive functions like memory, learning, and creativity. / Sleep helps with learning and the formation of long-term memories.", SFS + "; " + NHLBI),
        F(15, "Uyku, vücudun enerji tasarrufu yapmasını sağlar.", "Sleep allows people to conserve energy through an extended period of reduced activity.", SFW),
        F(16, "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.", "when you sleep, a particular type of immune cell works harder. That is why people who do not sleep enough may be more likely to get colds and other infections.", NHLBI),
        F(17, "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz ya da keyifsiz olabilir.", "kids who don't get enough sleep can have trouble paying attention ... be cranky, whiny, irritable, or moody", KH),
        F(18, "6–12 yaş için önerilen günlük uyku 9–12 saattir.", "School age, 6–12 years, 9–12 hours", CDC, ["6", "12", "9"]),
        F(19, "13–17 yaş için önerilen günlük uyku 8–10 saattir.", "Teen, 13–17 years, 8–10 hours", CDC, ["13", "17", "8", "10"]),
        F(20, "Her gün aynı saatte yatıp kalkmak daha iyi uykuya yardım eder.", "Going to bed and getting up at the same time every day.", CDC),
        F(21, "Yatmadan en az 30 dakika önce elektronik cihazları kapatmak önerilir.", "Turning off electronic devices at least 30 minutes before bedtime.", CDC, ["30"]),
        F(22, "Geceleri elektronik cihazların ışığı biyolojik saati şaşırtabilir.", "Light from electronic devices at night can confuse biological clocks.", NIGMS),
        F(23, "Birçok gencin yetişkinlerden daha geç yatmayı ve sabah daha geç kalkmayı tercih etmesi doğaldır.", "it is natural for many teens to prefer later bedtimes and to sleep later in the morning than adults.", NHLBI2),
        F(24, "Kafein temel olarak adenozin alıcılarını kapatarak etki eder.", "The primary way that caffeine works is by blocking adenosine receptors", SFA),
    ],
}

n = 0
def L(text, f=(), spoken=None):
    global n; n += 1
    return {"id": f"l{n}", "display": text, "spoken": spoken or text, "factIds": [f"f{i}" for i in f]}

sections = [
    ("hook", [
        L("Dün gece yatağa girdin, gözlerini kapadın ve... pat! Sabah oldu. Peki aradaki saatlerde ne oldu?"),
        L("Vücudun kapanmadı. Tam tersine: beynin gece boyunca planlı bir program yürüttü.", [1]),
        L("Bugün o programı adım adım çözüyoruz!"),
    ]),
    ("context", [
        L("Ben uyumam, şarj olurum. Ama insan uykusu benim şarjımdan çok daha karmaşık!"),
        L("Üç sorumuz var. Vücudumuz uyku vaktini nasıl anlıyor? Uyurken beyinde hangi evreler yaşanıyor? Ve bu kadar uyumak neye yarıyor?"),
        L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
    ]),
    ("method", [
        L("Uyku vaktini iki ayrı sistem birlikte belirler. Birincisi: biyolojik saat."),
        L("Amerikan Ulusal Sağlık Enstitüleri NIH'ye göre vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır. Buna sirkadiyen ritim denir.", [2], "Amerikan Ulusal Sağlık Enstitüleri, En Ay Eyç'e göre vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır. Buna sirkadiyen ritim denir."),
        L("Bu ritmi yöneten ana saat beynimizdedir. Adı biraz uzun: suprakiazmatik çekirdek. Kısaca SCN.", [3], "Bu ritmi yöneten ana saat beynimizdedir. Adı biraz uzun: suprakiazmatik çekirdek. Kısaca Es Si En."),
        L("SCN, beynin hipotalamus adlı bölgesinde, görme sinirlerinin çaprazlaştığı noktanın hemen üstünde yer alır ve binlerce sinir hücresinden oluşur.", [4], "Es Si En, beynin hipotalamus adlı bölgesinde, görme sinirlerinin çaprazlaştığı noktanın hemen üstünde yer alır ve binlerce sinir hücresinden oluşur."),
        L("Onu bir orkestra şefi gibi düşün: vücuttaki ritimlerin aynı tempoda çalmasını sağlar.", [3]),
        L("Şefin en önemli işareti ışıktır. Gözlerine gelen ışık, beynine şu mesajı yollar: Şu an gündüz!", [5, 6]),
        L("Güneş batınca beyin melatonin üretmeye başlar. Melatonin, uykuyu getiren bir hormondur. Kandaki miktarı akşam artar, sabaha karşı en yüksek düzeye çıkar.", [7]),
        L("İkinci sistem: uyku baskısı. Uyanık kaldığın her saat, beyninde adenozin adlı bir madde birikir.", [8]),
        L("Adenozin arttıkça uyuma ihtiyacın büyür. Uyuduğunda ise beyin bu maddeyi yeniden enerji molekülüne çevirir ve baskı ortadan kalkar.", [8, 9]),
        L("Yani gün sonunda esniyorsan tembel değilsin. Adenozin deposu doldu, o kadar!", [8]),
    ]),
    ("finding", [
        L("Peki uykuya dalınca ne olur? Sleep Foundation'a göre uyku dört evreden oluşur: üçü REM olmayan evre, biri REM.", [10], "Peki uykuya dalınca ne olur? Sliip Faundeyşın'a göre uyku dört evreden oluşur: üçü Rem olmayan evre, biri Rem."),
        L("Bu evreler sırayla bir döngü oluşturur. Bir döngü ortalama 90 dakika sürer ve bir gecede 4–6 döngü yaşarız.", [10], "Bu evreler sırayla bir döngü oluşturur. Bir döngü ortalama doksan dakika sürer ve bir gecede dört ile altı döngü yaşarız."),
        L("Üçüncü evreye derin uyku denir. Bu evre, vücudun toparlanması ve büyümesi için kritik sayılır.", [11]),
        L("KidsHealth'e göre büyüme için gereken hormonlar da bu evrede salgılanır. Yani büyümek, biraz da yastık işi!", [12], "Kids Helt'e göre büyüme için gereken hormonlar da bu evrede salgılanır. Yani büyümek, biraz da yastık işi!"),
        L("Dördüncü evre REM uykusudur. REM, hızlı göz hareketi demektir: gözlerin kapalıdır ama hızla hareket eder.", [13], "Dördüncü evre Rem uykusudur. Rem, hızlı göz hareketi demektir: gözlerin kapalıdır ama hızla hareket eder."),
        L("Bu evrede beyin etkinliği neredeyse uyanıkkenki düzeye çıkar. En canlı rüyalar da burada görülür.", [13]),
        L("Aynı anda kasların geçici olarak felç olur. Buna atoni denir. İyi ki öyle: yoksa rüyanda gol atarken yorgan havada uçardı!", [13]),
        L("REM uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir. Uyku, öğrendiklerinin uzun süreli anılara dönüşmesine yardım eder.", [14], "Rem uykusu hafıza, öğrenme ve yaratıcılık için önemli kabul edilir. Uyku, öğrendiklerinin uzun süreli anılara dönüşmesine yardım eder."),
    ]),
    ("importance", [
        L("Peki bunca saat uyumak neye yarıyor? Uyku, vücudun enerji tasarrufu yapmasını sağlar. Büyüme hormonu da dokuların büyümesine ve onarılmasına yardım eder.", [15, 12]),
        L("Bağışıklık sistemin de güçlenir. NIH'ye göre uyurken bazı bağışıklık hücreleri daha çok çalışır; az uyuyanlar nezleye daha kolay yakalanabilir.", [16], "Bağışıklık sistemin de güçlenir. En Ay Eyç'e göre uyurken bazı bağışıklık hücreleri daha çok çalışır; az uyuyanlar nezleye daha kolay yakalanabilir."),
        L("Yeterince uyumazsan dikkatini toplamak zorlaşır, keyfin de kaçabilir.", [17]),
        L("CDC'ye göre 6–12 yaş arasındakilerin günde 9–12 saat, 13–17 yaş arasındakilerin 8–10 saat uyuması önerilir.", [18, 19], "Si Di Si'ye göre altı ile on iki yaş arasındakilerin günde dokuz ile on iki saat, on üç ile on yedi yaş arasındakilerin sekiz ile on saat uyuması önerilir."),
        L("Bir ayrıntı daha: birçok gencin daha geç yatıp daha geç kalkmak istemesi doğaldır. Bu, tembellik değildir.", [23]),
        L("Şimdi sıra sende! Bir hafta boyunca uyku günlüğü tut."),
        L("Her gün aynı saatte yat ve kalk. Yatmadan en az 30 dakika önce ekranları kapat; çünkü cihazların ışığı biyolojik saati şaşırtabilir.", [20, 21, 22], "Her gün aynı saatte yat ve kalk. Yatmadan en az otuz dakika önce ekranları kapat; çünkü cihazların ışığı biyolojik saati şaşırtabilir."),
        L("Her sabah kaç saat uyuduğunu ve kendini nasıl hissettiğini not et. Hafta sonunda verilerine bak: tıpkı bir bilim insanı gibi!"),
    ]),
    ("limitations", [
        L("Bunu biliyor muydun? Kafein, adenozinin bağlandığı alıcıları kapatır. Kafeinli içeceklerin uykuyu kaçırmasının nedeni budur.", [24]),
        L("Hızlı soru! Beynimizdeki ana saatin kısa adı neydi?", [3]),
        L("Düşün bakalım... Evet: SCN!", [3], "Düşün bakalım... Evet: Es Si En!"),
        L("Bende SCN yok. Ama çok güzel bir şarj göstergem var!", [], "Bende Es Si En yok. Ama çok güzel bir şarj göstergem var!"),
        L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
    ]),
    ("summary", [
        L("İşte bugün öğrendiklerimiz!"),
        L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
        L("Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!"),
    ]),
]
STYLE = ["cheerful educational pop song", "upbeat marching band rhythm", "cartoon theme song energy", "bright glockenspiel, snare drum, tuba, hand claps", "catchy sing-along melody", "120 BPM", "clear enthusiastic lead vocal in Turkish", "group vocals shouting along in the chorus", "major key"]
song = {
    "title": "Uykunun Bilimi",
    "style": STYLE,
    "negativeStyle": ["sad", "slow", "dark", "heavy distortion", "mumbled vocals", "long instrumental solo", "lullaby"],
    "cast": [{"emoji": "☀️", "name": "Işık"}, {"emoji": "🧠", "name": "Ana saat"}, {"emoji": "🌙", "name": "Melatonin"}, {"emoji": "⏳", "name": "Adenozin"}, {"emoji": "💭", "name": "REM"}],
    "sections": [
        {"tag": "Intro", "label": "Giriş", "direction": "snare drum roll, hand claps", "lines": ["Hey! Hey! Hey!"], "durationMs": 5000},
        {"tag": "Verse 1", "label": "Kıta", "lines": ["Beynimde bir şef var, hipotalamusta", "Işık gelir gözümden, ritmi tutar ustaca", "Güneş batar, melatonin yükselir", "Adenozin birikir, uyku gelir"], "durationMs": 15000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Uyku bir bilim, uyku bir güç!", "Döngü döngü, doksan dakika", "Derin uyku onarır, REM öğretir", "Beynim her gece çalışır"], "durationMs": 13000},
        {"tag": "Verse 2", "label": "Kıta", "lines": ["Derin uykuda büyüme hormonu", "REM'de rüyalar, kaslarda atoni", "Hafıza güçlenir, bağışıklık çalışır", "Sabaha bedenim yeniden hazır"], "durationMs": 15000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Uyku bir bilim, uyku bir güç!", "Döngü döngü, doksan dakika", "Ekranı kapat, saatinde yat", "Muma'yla öğrendik, hey!"], "durationMs": 13000},
    ],
}
script = {
    "paperId": PID, "episodeNumber": 2, "videoTitle": "Neden uyuruz?", "paperTitleTr": "Neden uyuruz?",
    "sections": [{"id": s, "lines": ls} for s, ls in sections],
    "takeaways": ["Ana saat (SCN) ve melatonin uyku vaktini ayarlar", "Uyku, evrelerden oluşan döngülerle ilerler", "Derin uyku onarır; REM hafızaya ve öğrenmeye yardım eder"],
    "nextTeaser": "Yeni bir soru, yeni bir keşif seni bekliyor!",
    "description": "Uyurken beynimiz kapanmaz; planlı bir program yürütür. Bu bölümde beynimizdeki ana saati (SCN), sirkadiyen ritmi, melatonini ve adenozini; uykunun evrelerini, derin uykuyu ve REM uykusunu keşfediyoruz. Kaç saat uyumalıyız, ekran ışığı neden uykuyu kaçırır? Sonunda bir haftalık uyku günlüğü deneyi ve konuyu özetleyen bir şarkı var.",
    "glossary": [
        {"term": "Sirkadiyen ritim", "meaning": "Vücudumuzdaki değişikliklerin yaklaşık bir günlük döngüyle tekrarlanması."},
        {"term": "Suprakiazmatik çekirdek (SCN)", "meaning": "Beyindeki ana saat; vücudun günlük ritimlerini yöneten sinir hücresi grubu."},
        {"term": "Hipotalamus", "meaning": "Beynin alt kısmında, SCN'nin de bulunduğu küçük bölge."},
        {"term": "Melatonin", "meaning": "Karanlıkta beynin ürettiği ve uykuyu getiren hormon."},
        {"term": "Hormon", "meaning": "Vücudun bir yerinden başka bir yerine haber taşıyan madde."},
        {"term": "Adenozin", "meaning": "Uyanık kaldıkça beyinde biriken ve uyku ihtiyacını artıran madde."},
        {"term": "REM", "meaning": "Hızlı göz hareketi; en canlı rüyaların görüldüğü uyku evresi."},
        {"term": "Atoni", "meaning": "REM uykusunda kasların geçici olarak hareket edememesi."},
    ],
    "song": song,
}

allids = [l["id"] for s, ls in sections for l in ls]
by = {l["id"]: l for s, ls in sections for l in ls}
sec_of = {l["id"]: s for s, ls in sections for l in ls}
pos = 0
scenes = []
M = {"state": "talk", "x": 0.87, "y": 0.54, "scale": 1.15}  # ara sahnelerde kullanılmaz; yalnızca kapanışta geçerli
def S(k, visual, stickers=(), keywords=(), extra=()):
    """k satırlık sahne. stickers: kenarda süzülen simgeler; keywords: satır başına büyük anahtar kelime."""
    global pos
    li = allids[pos:pos + k]; pos += k
    sc = {"id": f"s{len(scenes)+1}", "section": sec_of[li[0]], "lineIds": li, "visual": visual, "mascot": M,
          "factIds": sorted({f for i in li for f in by[i]["factIds"]} | {f"f{e}" for e in extra}, key=lambda x: int(x[1:]))}
    if stickers: sc["stickers"] = list(stickers)
    if keywords: sc["keywords"] = (list(keywords) + [""] * k)[:k]
    scenes.append(sc)

# Her sahne en çok birkaç cümle sürer ve her cümlede ekranda bir şey değişir.
S(3, {"type": "hook", "question": "Uyurken beynimiz ne yapıyor?", "emoji": "😴"}, ["🛏️", "🌙", "⭐", "💤"], ["", "BEYİN KAPANMAZ!", "PROGRAMI ÇÖZELİM"])
S(1, {"type": "spotlight", "title": "Şarj mı, uyku mu?", "emoji": "🔋", "chips": [{"label": "Robot: şarj olur", "emoji": "🔌"}, {"label": "İnsan: uyur", "emoji": "😴"}, {"label": "Uyku çok daha karmaşık!", "emoji": "🧩"}]}, ["🤖", "⚡"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Vücudumuz uyku vaktini nasıl anlıyor?", "Uyurken beyinde hangi evreler yaşanıyor?", "Bu kadar uyumak neye yarıyor?"]}, ["❓", "🔎", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "clock", "title": "Birinci sistem: biyolojik saat", "center": "24 saat", "markers": [{"at": 12, "label": "Gündüz", "emoji": "☀️"}, {"at": 0, "label": "Gece", "emoji": "🌙"}], "note": "Şematik çizim."}, ["⏰", "🔄"], ["İKİ SİSTEM", "SİRKADİYEN RİTİM"])
S(3, {"type": "spotlight", "title": "Ana saat: SCN", "emoji": "🧠", "chips": [{"label": "Suprakiazmatik çekirdek (SCN)"}, {"label": "Hipotalamusta", "emoji": "📍"}, {"label": "Binlerce sinir hücresi", "emoji": "🔬"}, {"label": "Orkestra şefi", "emoji": "🎼"}]}, ["🎻", "🎺", "🥁"], ["SCN", "HİPOTALAMUS", "ORKESTRA ŞEFİ 🎼"])
S(1, {"type": "diagram", "title": "Şefin işareti: ışık", "layout": "flow", "nodes": [{"label": "Işık", "emoji": "☀️"}, {"label": "Göz", "emoji": "👁️"}, {"label": "Beyin: şu an gündüz!", "emoji": "🧠"}]}, ["💡", "✨"], ["IŞIK = İŞARET"])
S(1, {"type": "clock", "title": "Melatonin: uyku hormonu", "center": "Melatonin", "markers": [{"at": 19, "label": "Güneş batar: üretim başlar", "emoji": "🌆"}, {"at": 22, "label": "Akşam: kanda artar", "emoji": "📈"}, {"at": 4, "label": "Sabaha karşı: en yüksek", "emoji": "🏔️"}], "note": "Şematik çizim; saatler kişiden kişiye değişir."}, ["🧪", "🌙"], ["MELATONİN"])
S(3, {"type": "meter", "title": "İkinci sistem: uyku baskısı", "label": "Adenozin deposu", "emoji": "⏳", "phases": [{"label": "Uyanıkken birikir", "level": 0.6, "emoji": "🏃"}, {"label": "Uykuda sıfırlanır", "level": 0.08, "emoji": "😴"}, {"label": "Gün sonunda depo dolar", "level": 0.95, "emoji": "🥱"}], "note": "Şematik çizim; ölçekli değildir."}, ["🔋", "💤"], ["ADENOZİN", "UYKU BASKISI", "DEPO DOLDU 🥱"])
S(1, {"type": "spotlight", "title": "Uykunun dört evresi", "emoji": "🛌", "chips": [{"label": "N1"}, {"label": "N2"}, {"label": "N3: derin uyku", "emoji": "🌊"}, {"label": "REM", "emoji": "💭"}]}, ["🌙", "⭐"], ["DÖRT EVRE"])
S(1, {"type": "stages", "title": "Bir gece boyunca uyku döngüleri", "rows": [{"label": "REM", "emoji": "💭"}, {"label": "N1"}, {"label": "N2"}, {"label": "N3: derin uyku", "emoji": "🌊"}], "path": [1, 2, 3, 2, 0, 2, 3, 2, 0, 2, 3, 2, 0, 2, 2, 0, 2, 2, 0], "highlightRow": 0, "note": "Şematik çizim: bir döngü ortalama 90 dakika; bir gecede 4–6 döngü."}, [], ["90 DAKİKA"])
S(2, {"type": "spotlight", "title": "Üçüncü evre: derin uyku", "emoji": "🌊", "chips": [{"label": "Vücut toparlanır", "emoji": "🔧"}, {"label": "Büyüme için kritik", "emoji": "📏"}, {"label": "Büyüme hormonları salgılanır", "emoji": "🧪"}]}, ["🛌", "💪"], ["DERİN UYKU", "BÜYÜME HORMONU"])
S(2, {"type": "bullets", "title": "Dördüncü evre: REM 👀", "items": ["Gözler kapalı ama hızla hareket eder", "Beyin neredeyse uyanıkkenki kadar etkin", "En canlı rüyalar bu evrede görülür"]}, ["💭", "🌈", "🚀"], ["REM = HIZLI GÖZ HAREKETİ", "RÜYALAR 💭"])
S(1, {"type": "big-number", "value": "Atoni", "label": "REM'de kaslar geçici olarak felç olur", "sub": "Rüyandaki hareketler yatakta kalmaz", "icon": "⚽"}, ["🥅", "🛏️"], ["ATONİ"])
S(1, {"type": "spotlight", "title": "REM ne işe yarar?", "emoji": "📚", "chips": [{"label": "Hafıza", "emoji": "🗂️"}, {"label": "Öğrenme", "emoji": "✏️"}, {"label": "Yaratıcılık", "emoji": "🎨"}, {"label": "Uzun süreli anılar", "emoji": "💾"}]}, ["🧠", "✨"], ["HAFIZA + ÖĞRENME"])
S(3, {"type": "bullets", "title": "Bunca saat uyumak neye yarıyor?", "items": ["Enerji tasarrufu 🔋", "Dokular büyür ve onarılır 🧱", "Bağışıklık hücreleri daha çok çalışır 🛡️", "Dikkat ve keyif yerinde kalır 🎯"]}, ["💪", "🛡️"], ["ENERJİ + ONARIM", "BAĞIŞIKLIK 🛡️", "DİKKAT 🎯"])
S(1, {"type": "bar-chart", "title": "Önerilen günlük uyku (CDC)", "unit": "saat", "bars": [{"label": "6–12 yaş: en az", "value": 9, "display": "9"}, {"label": "6–12 yaş: en çok", "value": 12, "display": "12", "highlight": True}, {"label": "13–17 yaş: en az", "value": 8, "display": "8"}, {"label": "13–17 yaş: en çok", "value": 10, "display": "10", "highlight": True}]}, ["⏰", "😴"], ["CDC ÖNERİSİ"])
S(1, {"type": "quote-card", "quote": "Birçok gencin daha geç yatmayı ve sabah daha geç kalkmayı tercih etmesi doğaldır.", "attribution": "NIH (çeviri)"}, ["🦉", "🌙"], ["TEMBELLİK DEĞİL!"])
S(3, {"type": "bullets", "title": "Deney: bir haftalık uyku günlüğü 🔬", "items": ["Her gün aynı saatte yat ve kalk", "Yatmadan 30 dakika önce ekranları kapat", "Uyku süreni ve nasıl hissettiğini not et", "Hafta sonunda verilerini karşılaştır"]}, ["📓", "✏️", "📊"], ["DENEY ZAMANI 🔬", "EKRANLAR KAPALI 📵", "VERİ TOPLA 📊"])
S(1, {"type": "diagram", "title": "Kafein neden uyku kaçırır?", "layout": "flow", "nodes": [{"label": "Kafein", "emoji": "☕"}, {"label": "Adenozin alıcılarını kapatır", "emoji": "🔒"}, {"label": "Uyku baskısı hissedilmez", "emoji": "😳"}]}, ["🥤", "⚡"], ["KAFEİN ☕"])
S(3, {"type": "hook", "question": "Beynimizdeki ana saatin kısa adı neydi?", "emoji": "🤔"}, ["🧠", "⏰"], ["HIZLI SORU!", "SCN ✅", ""])
S(1, {"type": "song"})
S(3, {"type": "outro"})
assert pos == len(allids), (pos, len(allids))
for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": scenes})):
    json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("satır:", len(allids), "sahne:", len(scenes), "kelime:", sum(len(l["spoken"].split()) for s, ls in sections for l in ls), "karakter:", sum(len(l["spoken"]) for s, ls in sections for l in ls))
