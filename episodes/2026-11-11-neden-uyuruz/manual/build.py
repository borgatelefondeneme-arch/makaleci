"""Manuel sağlayıcı yanıtları (Claude API anahtarı yokken): olgular, senaryo, sahne planı.
Çalıştırma: python3 <bu dosya>"""
import json, os
D = os.path.dirname(__file__)
PID = "topic:neden-uyuruz"
CDC, KH, NHLBI, NIGMS = "CDC — About Sleep", "Nemours KidsHealth — Kids and Sleep", "NHLBI (NIH) — Why Is Sleep Important?", "NIGMS (NIH) — Circadian Rhythms"

def F(i, st, q, loc, nums=()):
    return {"id": f"f{i}", "kind": "number" if nums else "claim", "statement": st, "numbers": list(nums), "quote": q, "location": loc}

facts = {
    "paperId": PID, "basis": "full_text", "institutions": [],
    "sources": [
        {"id": "k1", "title": "Uyku hakkında (About Sleep)", "publisher": "CDC", "url": "https://www.cdc.gov/sleep/about/index.html"},
        {"id": "k2", "title": "Çocuklar ve uyku (Kids and Sleep)", "publisher": "Nemours KidsHealth", "url": "https://kidshealth.org/en/kids/not-tired.html"},
        {"id": "k3", "title": "Uyku neden önemli? (Why Is Sleep Important?)", "publisher": "NIH", "url": "https://www.nhlbi.nih.gov/health/sleep/why-sleep-important"},
        {"id": "k4", "title": "Vücut saati (Circadian Rhythms)", "publisher": "NIH", "url": "https://www.nigms.nih.gov/education/fact-sheets/Pages/circadian-rhythms"},
    ],
    "facts": [
        F(1, "Uyurken vücut, beynin sağlıklı çalışmasını ve beden sağlığını desteklemek için çalışır.", "During sleep, your body is working to support healthy brain function and maintain your physical health.", NHLBI),
        F(2, "Vücut saati (sirkadiyen ritim), bir canlının 24 saatlik döngüde yaşadığı bedensel, zihinsel ve davranışsal değişiklikleri kapsar.", "Circadian rhythms include some of the physical, mental, and behavioral changes an organism experiences over a 24-hour cycle.", NIGMS, ["24"]),
        F(3, "İnsanda ana saat beyindedir; büyük bir sinir hücresi grubudur.", "In vertebrate animals, including humans, the master clock exists in the brain. The human master clock is a large group of nerve cells", NIGMS),
        F(4, "Vücut saatini en çok ışık ve karanlık etkiler; yemek, stres, hareket, sosyal çevre ve sıcaklık da etkiler.", "Light and dark have the biggest influence on circadian rhythms, but food intake, stress, physical activity, social environment, and temperature also affect them.", NIGMS),
        F(5, "Akşam ana saat beyne daha çok melatonin üretmesini söyler; bu uyku getirir. Melatonin bir hormondur.", "In the evening, a person's master clock tells their brain to make more melatonin, causing sleepiness.", NIGMS),
        F(6, "Sabah vücut, uyanmaya yardım eden kortizol gibi hormonlar salgılar.", "In the morning, your body releases hormones that promote alertness, such as cortisol, which helps you wake up.", NHLBI),
        F(7, "Uyurken beyin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.", "As we sleep, our brains move between two types of sleep — non-REM and REM (rapid eye movement) sleep.", KH),
        F(8, "Okul çağında bir uyku döngüsü yaklaşık 90 dakika sürer.", "By the time kids start school, one complete sleep cycle lasts about 90 minutes, which is similar to an adult's.", KH, ["90"]),
        F(9, "REM olmayan uykunun üçüncü aşamasında vücut, büyüme ve gelişme için gereken hormonları salgılar.", "It's during this stage that the body releases hormones needed for growth and development.", KH),
        F(10, "REM uykusunda gözler göz kapaklarının altında hızlı hareket eder.", "The eyes move quickly under the eyelids, breathing gets faster, and the heart beats faster.", KH),
        F(11, "En canlı rüyalar REM uykusunda görülür.", "This is when we have our most vivid dreams.", KH),
        F(12, "REM uykusunda kollar ve bacaklar hareket ettirilemez.", "You can't move your arms or legs during REM sleep.", KH),
        F(13, "REM uykusu öğrenme ve hafıza için önemlidir.", "REM sleep is important for learning and memory.", KH),
        F(14, "Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.", "Sleep helps with learning and the formation of long-term memories.", NHLBI),
        F(15, "Çocuklarda ve gençlerde uyku, büyümeyi ve gelişmeyi de destekler.", "In children and teens, sleep also helps support growth and development.", NHLBI),
        F(16, "Uyurken bir tür bağışıklık hücresi daha çok çalışır; yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.", "when you sleep, a particular type of immune cell works harder. That is why people who do not sleep enough may be more likely to get colds and other infections.", NHLBI),
        F(17, "Yeterince uyumayan çocuklar dikkatini toplamakta zorlanabilir; huysuz, sinirli ya da keyifsiz olabilir.", "kids who don't get enough sleep can have trouble paying attention ... be cranky, whiny, irritable, or moody", KH),
        F(18, "6–12 yaş için önerilen günlük uyku 9–12 saattir.", "School age, 6–12 years, 9–12 hours", CDC, ["6", "12", "9"]),
        F(19, "13–17 yaş için önerilen günlük uyku 8–10 saattir.", "Teen, 13–17 years, 8–10 hours", CDC, ["13", "17", "8", "10"]),
        F(20, "Her gün aynı saatte yatıp kalkmak daha iyi uykuya yardım eder.", "Going to bed and getting up at the same time every day.", CDC),
        F(21, "Yatmadan en az 30 dakika önce elektronik cihazları kapatmak önerilir.", "Turning off electronic devices at least 30 minutes before bedtime.", CDC, ["30"]),
        F(22, "Geceleri elektronik cihazların ışığı biyolojik saati şaşırtabilir.", "Light from electronic devices at night can confuse biological clocks.", NIGMS),
        F(23, "Yatak odasının sessiz, rahatlatıcı ve serin olması önerilir.", "Keeping your bedroom quiet, relaxing, and at a cool temperature.", CDC),
        F(24, "Düzenli hareket etmek ve sağlıklı beslenmek daha iyi uykuya yardım eder.", "Exercising regularly and maintaining a healthy diet.", CDC),
    ],
}

n = 0
def L(text, f=(), spoken=None):
    global n; n += 1
    return {"id": f"l{n}", "display": text, "spoken": spoken or text, "factIds": [f"f{i}" for i in f]}

sections = [
    ("hook", [
        L("Dün gece yatağa girdin, gözlerini kapadın ve... pat! Bir anda sabah oldu."),
        L("Peki aradaki o saatlerde ne oldu? Vücudun düğmesine basılıp kapandı mı?"),
        L("Hiç de değil! Sen uyurken içeride koca bir gece vardiyası çalışıyor. Hadi, gizlice bakalım!", [1]),
    ]),
    ("context", [
        L("Ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!"),
        L("Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?"),
        L("Bilgilerimiz sağlık kurumlarının sayfalarından geliyor: CDC, NIH ve Nemours KidsHealth.", spoken="Bilgilerimiz sağlık kurumlarının sayfalarından geliyor: Si Di Si, En Ay Eyç ve Nemurs Kids Helt."),
        L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum!"),
    ]),
    ("method", [
        L("Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?"),
        L("Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır.", [2], "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır."),
        L("Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!", [3]),
        L("Ana saati en çok ışık ve karanlık etkiler.", [4]),
        L("Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.", [5]),
        L("Yani akşam esnemeye başladıysan suçlu belli: melatonin!", [5]),
    ]),
    ("finding", [
        L("Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. İki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.", [1, 7], "Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. İki tür uyku arasında gidip gelir: Rem olmayan uyku ve Rem uykusu."),
        L("Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık 90 dakika sürer.", [8], "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık doksan dakika sürer."),
        L("REM olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.", [9], "Rem olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar."),
        L("Yani büyümek, biraz da yastık işi!", [9, 15]),
        L("REM uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder. En canlı rüyalarımızı da bu sırada görürüz.", [10, 11], "Rem uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder. En canlı rüyalarımızı da bu sırada görürüz."),
        L("İlginç olan şu: REM uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!", [12], "İlginç olan şu: Rem uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!"),
        L("Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.", [13, 14]),
        L("Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.", [16]),
        L("Peki yeterince uyumazsak? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.", [17]),
        L("O zaman ne kadar uyumalıyız? 6–12 yaş arasındaysan günde 9–12 saat.", [18], "O zaman ne kadar uyumalıyız? Altı ile on iki yaş arasındaysan günde dokuz ile on iki saat."),
        L("13–17 yaş arasındaysan 8–10 saat.", [19], "On üç ile on yedi yaş arasındaysan sekiz ile on saat."),
    ]),
    ("importance", [
        L("Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?"),
        L("Bir: Her gün aynı saatte yat, aynı saatte kalk.", [20]),
        L("İki: Yatmadan en az 30 dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.", [21, 22], "İki: Yatmadan en az otuz dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir."),
        L("Üç: Odan sessiz, sakin ve serin olsun.", [23]),
        L("Dört: Her sabah nasıl hissettiğini bir kâğıda not et, hafta sonunda karşılaştır."),
    ]),
    ("limitations", [
        L("Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?", [11]),
        L("Düşün bakalım... Evet: REM uykusunda!", [11], "Düşün bakalım... Evet: Rem uykusunda!"),
        L("Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!"),
        L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
    ]),
    ("summary", [
        L("İşte bugün öğrendiklerimiz!"),
        L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
        L("Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!"),
    ]),
]
STYLE = ["cheerful children's educational song", "upbeat marching band rhythm", "cartoon theme song energy", "bright glockenspiel, snare drum, tuba, hand claps", "catchy sing-along melody", "120 BPM", "clear enthusiastic lead vocal in Turkish", "kids choir shouting along in the chorus", "major key"]
song = {
    "title": "Uyu, Büyü, Öğren!",
    "style": STYLE,
    "negativeStyle": ["sad", "slow", "dark", "heavy distortion", "mumbled vocals", "long instrumental solo"],
    "cast": [{"emoji": "🌙", "name": "Ay"}, {"emoji": "⏰", "name": "Ana Saat"}, {"emoji": "🧠", "name": "Beyin"}, {"emoji": "⭐", "name": "Yıldız"}, {"emoji": "🛏️", "name": "Yatak"}],
    "sections": [
        {"tag": "Intro", "label": "Giriş", "direction": "snare drum roll, hand claps", "lines": ["Hey! Hey! Hey!"], "durationMs": 5000},
        {"tag": "Verse 1", "label": "Kıta", "lines": ["İçimizde bir saat var, tik tak, tik tak döner", "Akşam olur, melatonin \"haydi uyku\" der"], "durationMs": 12000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Uyu, büyü, öğren, güçlen!", "Uyku senin süper gücün!", "Uyu, büyü, öğren, güçlen!", "Her gece yeniden!"], "durationMs": 12000},
        {"tag": "Verse 2", "label": "Kıta", "lines": ["Rüyalar REM'de gelir, gözler hızlı hızlı", "Öğrendiğin her şey hafızana yazılı", "Sen uyurken vücudun büyümeye çalışır", "Bağışıklık hücrelerin gece boyu çalışır"], "durationMs": 16000},
        {"tag": "Chorus", "label": "Nakarat", "lines": ["Uyu, büyü, öğren, güçlen!", "Uyku senin süper gücün!", "Ekranı kapat, aynı saatte yat", "Muma'yla öğrendik, hey!"], "durationMs": 14000},
    ],
}
script = {
    "paperId": PID, "episodeNumber": 2, "videoTitle": "Neden uyuruz?", "paperTitleTr": "Neden uyuruz?",
    "sections": [{"id": s, "lines": ls} for s, ls in sections],
    "takeaways": ["İçimizde bir saat var; melatonin uyku getirir", "Uyku, öğrenmeye ve hafızaya yardım eder", "Uyku büyümeye ve sağlığa yardım eder"],
    "nextTeaser": "Yeni bir soru, yeni bir keşif seni bekliyor!",
    "description": "Uyurken vücudumuz kapanır mı? Hiç de değil! Muma ile vücut saatini, melatonini, REM uykusunu ve rüyaları keşfediyoruz. Uyku neden öğrenmeye, büyümeye ve sağlıklı kalmaya yardım eder, kaç saat uyumalıyız? Sonunda bir haftalık uyku dedektifi görevi ve dans eden arkadaşlarımızla bir uyku şarkısı var!",
    "glossary": [
        {"term": "Melatonin", "meaning": "Akşam olunca beynimizin ürettiği ve uykumuzu getiren hormon."},
        {"term": "Hormon", "meaning": "Vücudun bir yerinden başka bir yerine haber taşıyan minik madde."},
        {"term": "Ana saat", "meaning": "Beynimizde, vücudun günlük düzenini ayarlayan sinir hücreleri grubu."},
        {"term": "REM uykusu", "meaning": "Gözlerin hızlı hareket ettiği ve en canlı rüyaların görüldüğü uyku türü."},
        {"term": "Bağışıklık", "meaning": "Vücudun mikroplara karşı kendini savunma gücü."},
        {"term": "Hafıza", "meaning": "Öğrendiklerimizi ve yaşadıklarımızı aklımızda tutma yeteneği."},
    ],
    "song": song,
}

allids = [l["id"] for s, ls in sections for l in ls]
by = {l["id"]: l for s, ls in sections for l in ls}
sec_of = {l["id"]: s for s, ls in sections for l in ls}
pos = 0
scenes = []
def S(k, visual, mascot, note=None):
    global pos
    li = allids[pos:pos + k]; pos += k
    sc = {"id": f"s{len(scenes)+1}", "section": sec_of[li[0]], "lineIds": li, "visual": visual, "mascot": mascot,
          "factIds": sorted({f for i in li for f in by[i]["factIds"]}, key=lambda x: int(x[1:]))}
    if note: sc["sourceNote"] = note
    scenes.append(sc)
def R(state, x=0.87, y=0.56, s=1.0, at=None, pose=None):
    c = {"state": state, "x": x, "y": y, "scale": s}
    if at: c["pointAt"] = {"x": at[0], "y": at[1]}
    if pose: c["pose"] = pose
    return c
BIG, SIDE, SMALL, LEFT = (0.87, 0.54, 1.15), (0.88, 0.55, 1.0), (0.91, 0.6, 0.85), (0.15, 0.5, 1.45)

S(3, {"type": "hook", "question": "Uyuyunca vücudumuz kapanır mı?", "emoji": "😴"}, R("think", *LEFT))
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Neden uyuruz?", "Uyurken içeride neler olur?", "Ne kadar uyumalıyız?"]}, R("talk", *BIG, pose="wave"))
S(2, {"type": "source-card"}, R("talk", *SIDE))
S(2, {"type": "big-number", "value": "24", "unit": "saat", "label": "Vücut saatimizin bir turu", "sub": "Pek çok değişiklik bu döngüyle tekrarlanır"}, R("point", 0.83, 0.52, 1.25, (0.3, 0.4)), "NIH (NIGMS)")
S(4, {"type": "diagram", "title": "Uykumuz nasıl gelir?", "layout": "flow", "nodes": [{"label": "Akşam olur, ışık azalır", "emoji": "🌆"}, {"label": "Ana saat beyne haber verir", "emoji": "🧠"}, {"label": "Melatonin artar", "emoji": "🧪"}, {"label": "Uykun gelir", "emoji": "🥱"}]}, R("talk", 0.92, 0.66, 0.72), "NIH (NIGMS)")
S(2, {"type": "big-number", "value": "90", "unit": "dakika", "label": "Bir uyku döngüsü (okul çağında)", "sub": "Beyin iki tür uyku arasında gidip gelir"}, R("point", 0.83, 0.52, 1.25, (0.3, 0.4)), "Nemours KidsHealth")
S(2, {"type": "quote-card", "quote": "Bu aşamada vücut, büyüme ve gelişme için gereken hormonları salgılar.", "attribution": "Nemours KidsHealth (çeviri)"}, R("talk", 0.86, 0.54, 1.15, pose="book"), "Nemours KidsHealth")
S(2, {"type": "comparison", "title": "İki tür uyku", "left": {"title": "🌙 REM olmayan uyku", "items": ["Üçüncü aşamada büyüme ve gelişme hormonları salgılanır"]}, "right": {"title": "💭 REM uykusu", "items": ["Gözler hızlı hızlı hareket eder", "En canlı rüyalar", "Kollar ve bacaklar hareket etmez"]}}, R("point", 0.91, 0.6, 0.85, (0.55, 0.45)), "Nemours KidsHealth")
S(2, {"type": "bullets", "title": "Uyku ne işe yarar?", "items": ["Öğrenmeye ve hafızaya yardım eder", "Bağışıklık hücreleri daha çok çalışır", "Büyümeyi ve gelişmeyi destekler"]}, R("talk", *BIG), "NIH (NHLBI)")
S(1, {"type": "hook", "question": "Peki yeterince uyumazsak?", "emoji": "😵‍💫"}, R("think", *LEFT), "Nemours KidsHealth")
S(2, {"type": "bar-chart", "title": "Günde kaç saat uyku?", "unit": "saat", "bars": [{"label": "6–12 yaş: en az", "value": 9, "display": "9"}, {"label": "6–12 yaş: en çok", "value": 12, "display": "12", "highlight": True}, {"label": "13–17 yaş: en az", "value": 8, "display": "8"}, {"label": "13–17 yaş: en çok", "value": 10, "display": "10", "highlight": True}]}, R("point", 0.92, 0.62, 0.75, (0.5, 0.4)), "CDC")
S(5, {"type": "bullets", "title": "Uyku dedektifi görevi 🔎", "items": ["Her gün aynı saatte yat ve kalk", "Yatmadan 30 dakika önce ekranları kapat", "Odan sessiz, sakin ve serin olsun", "Her sabah nasıl hissettiğini not et"]}, R("talk", *BIG), "CDC")
S(3, {"type": "hook", "question": "En canlı rüyaları hangi uykuda görürüz?", "emoji": "🤔"}, R("think", *LEFT))
S(1, {"type": "song"}, R("talk", 0.86, 0.52, 1.3, pose="thumbs"))
S(3, {"type": "outro"}, R("talk", *BIG))
assert pos == len(allids), (pos, len(allids))
for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": scenes})):
    json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("satır:", len(allids), "sahne:", len(scenes), "kelime:", sum(len(l["spoken"].split()) for s, ls in sections for l in ls))
