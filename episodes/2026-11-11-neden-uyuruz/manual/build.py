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
        L("Merhaba! Ben senin robot arkadaşınım. Gerçi ben uyumam, şarj olurum. Ama uykuyu çok merak ediyorum!"),
        L("Bir kere uyumayı denedim. Bir türlü kapanamadım. Meğer kapatma düğmem yokmuş!"),
        L("Bugün üç şeyi merak ediyoruz. Neden uyuruz? Uyurken içeride neler olur? Ve ne kadar uyumalıyız?"),
        L("Bugünkü bilgilerimiz sağlık kurumlarının sayfalarından geliyor: CDC, NIH ve Nemours KidsHealth.", spoken="Bugünkü bilgilerimiz sağlık kurumlarının sayfalarından geliyor: Si Di Si, En Ay Eyç ve Nemurs Kids Helt."),
        L("Kaynakların bağlantıları videonun açıklamasında."),
    ]),
    ("method", [
        L("Önce şunu çözelim: Vücudun, uyku vaktinin geldiğini nereden biliyor?"),
        L("Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik 24 saatlik bir döngüyle tekrarlanır.", [2], "Çünkü içinde bir saat var! Vücudumuzdaki pek çok değişiklik yirmi dört saatlik bir döngüyle tekrarlanır."),
        L("Bu saatin patronu beynindedir. Adı: ana saat. Merak etme, pili bitmez!", [3]),
        L("Ana saati en çok ışık ve karanlık etkiler.", [4]),
        L("Akşam olunca ana saat beynine şöyle der: Daha çok melatonin üret! Melatonin bir hormondur ve uykunu getirir.", [5]),
        L("Yani akşam esnemeye başladıysan suçlu belli: melatonin!", [5]),
        L("Sabah olunca işler değişir. Vücudun, uyanmana yardım eden kortizol gibi hormonlar salgılar.", [6]),
    ]),
    ("finding", [
        L("Şimdi işin sırrına geliyoruz. Uyuyunca beynin kapanmaz. Tam tersine, vücudun beynini ve sağlığını korumak için çalışır.", [1]),
        L("Beynin iki tür uyku arasında gidip gelir: REM olmayan uyku ve REM uykusu.", [7], "Beynin iki tür uyku arasında gidip gelir: Rem olmayan uyku ve Rem uykusu."),
        L("Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık 90 dakika sürer.", [8], "Okul çağındaki çocuklarda bir uyku döngüsü yaklaşık doksan dakika sürer."),
        L("REM olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar.", [9], "Rem olmayan uykunun üçüncü aşamasında vücudun, büyüme ve gelişme için gereken hormonları salgılar."),
        L("Yani büyümek, biraz da yastık işi!", [9, 15]),
        L("REM uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder.", [10], "Rem uykusunda ise gözlerin, kapalı göz kapaklarının altında hızlı hızlı hareket eder."),
        L("En canlı rüyalarımızı da bu sırada görürüz.", [11]),
        L("İlginç olan şu: REM uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!", [12], "İlginç olan şu: Rem uykusunda kollarını ve bacaklarını oynatamazsın. Düşünsene, yoksa rüyanda gol atarken yorgan havada uçardı!"),
        L("REM uykusu öğrenme ve hafıza için de önemlidir.", [13], "Rem uykusu öğrenme ve hafıza için de önemlidir."),
        L("Uyku, öğrenmeye ve uzun süreli anıların oluşmasına yardım eder.", [14]),
        L("Seni hastalıklardan da korur. Sen uyurken bir tür bağışıklık hücresi daha çok çalışır.", [16]),
        L("Bu yüzden yeterince uyumayanlar nezleye ve başka enfeksiyonlara daha kolay yakalanabilir.", [16]),
        L("Yani uyku tembellik değil. Uyku, vücudunun en önemli işlerinden biri!", [1]),
        L("Peki yeterince uyumazsak ne olur? Dikkatimizi toplamak zorlaşır. Huysuz ve keyifsiz olabiliriz.", [17]),
        L("O zaman ne kadar uyumalıyız? 6–12 yaş arasındaysan günde 9–12 saat.", [18], "O zaman ne kadar uyumalıyız? Altı ile on iki yaş arasındaysan günde dokuz ile on iki saat."),
        L("13–17 yaş arasındaysan 8–10 saat.", [19], "On üç ile on yedi yaş arasındaysan sekiz ile on saat."),
        L("Kaç saat uyuduğunu merak mı ettin? Yattığın ve kalktığın saate bak, aradaki saatleri say."),
    ]),
    ("importance", [
        L("Şimdi sıra sende! Bir haftalık uyku dedektifi görevine hazır mısın?"),
        L("Bir: Her gün aynı saatte yat, aynı saatte kalk.", [20]),
        L("İki: Yatmadan en az 30 dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir.", [21, 22], "İki: Yatmadan en az otuz dakika önce ekranları kapat. Çünkü geceleri elektronik cihazların ışığı vücut saatini şaşırtabilir."),
        L("Üç: Odan sessiz, sakin ve serin olsun. Gün içinde de bol bol hareket et.", [23, 24]),
        L("Dört: Her sabah kendine sor: Bugün nasıl hissediyorum? Bir kâğıda not et, hafta sonunda karşılaştır."),
    ]),
    ("limitations", [
        L("Bunu biliyor muydun? Vücut saatini yalnızca ışık etkilemez. Yemek, hareket ve sıcaklık da etkiler.", [4]),
        L("Şimdi hızlı soru zamanı! En canlı rüyalarımızı hangi uykuda görürüz?", [11]),
        L("Düşün bakalım... Evet: REM uykusunda!", [11], "Düşün bakalım... Evet: Rem uykusunda!"),
        L("Ben mi? Ben rüya görmem. Ama şarj olurken bazen elektrikli koyun sayıyorum!"),
        L("Bir soru daha! Akşam olunca uykumuzu getiren hormonun adı neydi?", [5]),
        L("Me-la-to-nin! Söylemesi bile insanın uykusunu getiriyor.", [5], "Melatonin! Söylemesi bile insanın uykusunu getiriyor."),
    ]),
    ("summary", [
        L("Bugün bunu öğrendik!"),
        L("Bir: İçimizde bir saat var. Akşam olunca melatonin uykumuzu getirir.", [2, 5]),
        L("İki: Uyurken beynimiz çalışmaya devam eder. Uyku, öğrenmeye ve hafızaya yardım eder.", [7, 14]),
        L("Üç: Uyku büyümemize ve hastalıklardan korunmamıza yardım eder.", [15, 16]),
        L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
        L("Abone olmayı ve zili açmayı unutma. Ben de gidip biraz şarj olayım!"),
    ]),
]
script = {
    "paperId": PID, "episodeNumber": 2, "videoTitle": "Neden uyuruz?", "paperTitleTr": "Neden uyuruz?",
    "sections": [{"id": s, "lines": ls} for s, ls in sections],
    "takeaways": ["İçimizde bir saat var; melatonin uyku getirir", "Uyku, öğrenmeye ve hafızaya yardım eder", "Uyku büyümeye ve sağlığa yardım eder"],
    "nextTeaser": "Yeni bir soru, yeni bir keşif seni bekliyor!",
    "description": "Uyurken vücudumuz kapanır mı? Hiç de değil! Robot arkadaşımızla vücut saatini, melatonini, REM uykusunu ve rüyaları keşfediyoruz. Uyku neden öğrenmeye, büyümeye ve sağlıklı kalmaya yardım eder, kaç saat uyumalıyız? Sonunda bir haftalık uyku dedektifi görevi de var!",
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
R = lambda state, x=0.87, y=0.56, s=1.0, at=None: {"state": state, "x": x, "y": y, "scale": s, **({"pointAt": {"x": at[0], "y": at[1]}} if at else {})}
BIG, SIDE, SMALL, LEFT = (0.87, 0.54, 1.15), (0.88, 0.55, 1.0), (0.91, 0.6, 0.85), (0.15, 0.5, 1.45)

S(3, {"type": "hook", "question": "Uyuyunca vücudumuz kapanır mı?", "emoji": "😴"}, R("think", *LEFT))
S(3, {"type": "bullets", "title": "Bugünün soruları", "items": ["Neden uyuruz?", "Uyurken içeride neler olur?", "Ne kadar uyumalıyız?"]}, R("talk", *BIG))
S(2, {"type": "source-card"}, R("point", *SIDE, at=(0.45, 0.45)))
S(2, {"type": "big-number", "value": "24", "unit": "saat", "label": "Vücut saatimizin bir turu", "sub": "Pek çok değişiklik bu döngüyle tekrarlanır"}, R("point", 0.83, 0.52, 1.25, (0.3, 0.4)), "NIH (NIGMS)")
S(4, {"type": "diagram", "title": "Uykumuz nasıl gelir?", "layout": "flow", "nodes": [{"label": "Akşam olur, ışık azalır", "emoji": "🌆"}, {"label": "Ana saat beyne haber verir", "emoji": "🧠"}, {"label": "Melatonin artar", "emoji": "🧪"}, {"label": "Uykun gelir", "emoji": "🥱"}]}, R("talk", 0.92, 0.66, 0.72), "NIH (NIGMS)")
S(1, {"type": "comparison", "title": "Akşam mı, sabah mı?", "left": {"title": "🌙 Akşam", "items": ["Melatonin artar", "Uykun gelir"]}, "right": {"title": "☀️ Sabah", "items": ["Kortizol gibi hormonlar salgılanır", "Uyanmana yardım eder"]}}, R("think", *SMALL), "NIH (NIGMS, NHLBI)")
S(3, {"type": "big-number", "value": "90", "unit": "dakika", "label": "Bir uyku döngüsü (okul çağında)", "sub": "Beyin iki tür uyku arasında gidip gelir"}, R("point", 0.83, 0.52, 1.25, (0.3, 0.4)), "Nemours KidsHealth")
S(2, {"type": "quote-card", "quote": "Bu aşamada vücut, büyüme ve gelişme için gereken hormonları salgılar.", "attribution": "Nemours KidsHealth (çeviri)"}, R("talk", 0.86, 0.54, 1.15), "Nemours KidsHealth")
S(4, {"type": "comparison", "title": "İki tür uyku", "left": {"title": "🌙 REM olmayan uyku", "items": ["Üçüncü aşamada büyüme ve gelişme hormonları salgılanır"]}, "right": {"title": "💭 REM uykusu", "items": ["Gözler hızlı hızlı hareket eder", "En canlı rüyalar", "Kollar ve bacaklar hareket etmez", "Öğrenme ve hafıza için önemli"]}}, R("point", 0.91, 0.6, 0.85, (0.55, 0.45)), "Nemours KidsHealth")
S(4, {"type": "bullets", "title": "Uyku ne işe yarar?", "items": ["Öğrenmeye ve hafızaya yardım eder", "Bağışıklık hücreleri daha çok çalışır", "Büyümeyi ve gelişmeyi destekler"]}, R("talk", *BIG), "NIH (NHLBI)")
S(1, {"type": "hook", "question": "Peki yeterince uyumazsak?", "emoji": "😵‍💫"}, R("think", *LEFT), "Nemours KidsHealth")
S(3, {"type": "bar-chart", "title": "Günde kaç saat uyku?", "unit": "saat", "bars": [{"label": "6–12 yaş: en az", "value": 9, "display": "9"}, {"label": "6–12 yaş: en çok", "value": 12, "display": "12", "highlight": True}, {"label": "13–17 yaş: en az", "value": 8, "display": "8"}, {"label": "13–17 yaş: en çok", "value": 10, "display": "10", "highlight": True}]}, R("point", 0.92, 0.62, 0.75, (0.5, 0.4)), "CDC")
S(5, {"type": "bullets", "title": "Uyku dedektifi görevi 🔎", "items": ["Her gün aynı saatte yat ve kalk", "Yatmadan 30 dakika önce ekranları kapat", "Odan sessiz, sakin ve serin olsun", "Her sabah nasıl hissettiğini not et"]}, R("talk", *BIG), "CDC")
S(1, {"type": "quote-card", "quote": "Vücut saatini yalnızca ışık etkilemez. Yemek, hareket ve sıcaklık da etkiler.", "attribution": "Bunu biliyor muydun?"}, R("think", 0.86, 0.54, 1.2), "NIH (NIGMS)")
S(5, {"type": "hook", "question": "En canlı rüyaları hangi uykuda görürüz?", "emoji": "🤔"}, R("think", *LEFT))
S(6, {"type": "outro"}, R("talk", *BIG))
assert pos == len(allids), (pos, len(allids))
for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": scenes})):
    json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("satır:", len(allids), "sahne:", len(scenes), "kelime:", sum(len(l["spoken"].split()) for s, ls in sections for l in ls))
