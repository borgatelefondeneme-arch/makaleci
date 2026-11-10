"""Manuel sağlayıcı yanıtları (Claude API anahtarı yokken): olgular, senaryo, sahne planı.
Çalıştırma: python3 episodes/2026-11-10-gokyuzu-neden-mavi/manual/build.py"""
import json, os
D = os.path.dirname(__file__)
PID = "topic:gokyuzu-neden-mavi"
K1 = "NASA Space Place — Why Is the Sky Blue?"
K2 = "NASA Science — Sun: Facts"

def F(i, st, q, loc=K1, nums=(), kind="claim"):
    return {"id": f"f{i}", "kind": "number" if nums else kind, "statement": st, "numbers": list(nums), "quote": q, "location": loc}

facts = {
    "paperId": PID, "basis": "full_text", "institutions": [],
    "sources": [
        {"id": "k1", "title": "Gökyüzü neden mavi? (Why Is the Sky Blue?)", "publisher": "NASA Space Place", "url": "https://spaceplace.nasa.gov/blue-sky/en/"},
        {"id": "k2", "title": "Güneş hakkında bilgiler (Sun: Facts)", "publisher": "NASA Science", "url": "https://science.nasa.gov/sun/facts/"},
    ],
    "facts": [
        F(1, "Güneş ışığı beyaz görünür ama gökkuşağının bütün renklerinden oluşur.", "The light from the Sun looks white. But it is really made up of all the colors of the rainbow."),
        F(2, "Işık enerjisi, okyanustaki enerji gibi dalgalar halinde yol alır.", "Like energy passing through the ocean, light energy travels in waves, too."),
        F(3, "Bazı ışık kısa ve kıpırtılı, bazı ışık uzun ve sakin dalgalarla ilerler.", "Some light travels in short, \"choppy\" waves. Other light travels in long, lazy waves."),
        F(4, "Mavi ışığın dalgaları kırmızı ışığın dalgalarından kısadır.", "Blue light waves are shorter than red light waves."),
        F(5, "Güneş ışığı atmosfere ulaşınca havadaki gazlar ve parçacıklar tarafından her yöne saçılır.", "Sunlight reaches Earth's atmosphere and is scattered in all directions by all the gases and particles in the air."),
        F(6, "Mavi ışık kısa ve küçük dalgalarla ilerlediği için diğer renklerden daha çok saçılır.", "Blue is scattered more than other colors because it travels as shorter, smaller waves."),
        F(7, "Ufka yaklaştıkça gökyüzü açık maviye ya da beyaza döner.", "Closer to the horizon, the sky fades to a lighter blue or white."),
        F(8, "Çok fazla saçılma renkleri yeniden karıştırır; daha çok beyaz, daha az mavi görürüz.", "All this scattering mixes the colors together again so we see more white and less blue."),
        F(9, "Güneş alçaldıkça ışığı bize ulaşmak için atmosferin daha fazlasından geçer.", "As the Sun gets lower in the sky, its light is passing through more of the atmosphere to reach you."),
        F(10, "Gün batımında mavi ışık daha da çok saçılır; kırmızılar ve sarılar doğrudan göze ulaşır.", "Even more of the blue light is scattered, allowing the reds and yellows to pass straight through to your eyes."),
        F(11, "Mars'ta gündüz gökyüzü turuncu ya da kızılımsı görünür.", "During the daytime, the Martian sky takes on an orange or reddish color."),
        F(12, "Mars'ta Güneş batarken Güneş'in çevresindeki gökyüzü mavi-gri bir ton alır.", "But as the Sun sets, the sky around the Sun begins to take on a blue-gray tone."),
        F(13, "Mars'ın atmosferi çok incedir, çoğunlukla karbondioksitten oluşur ve ince toz parçacıklarıyla doludur.", "Mars has a very thin atmosphere made mostly of carbon dioxide and filled with fine dust particles."),
        F(14, "Güneş Dünya'dan yaklaşık 150 milyon kilometre uzaktadır.", "The Sun is about 93 million miles (150 million kilometers) from Earth.", K2, ["150"]),
    ],
}

n = 0
def L(text, f=(), spoken=None):
    global n; n += 1
    return {"id": f"l{n}", "display": text, "spoken": spoken or text, "factIds": [f"f{i}" for i in f]}

sections = [
    ("hook", [
        L("Başını kaldır ve gökyüzüne bak. Masmavi, değil mi?"),
        L("Peki neden yeşil değil? Ya da mor? Ya da pembe?"),
        L("Gökyüzü neden başka bir renk değil de mavi? Hadi, bu sırrı birlikte çözelim!"),
    ]),
    ("context", [
        L("Merhaba! Ben senin robot arkadaşınım. Her gün, merak ettiğin bir soruyu birlikte araştırıyoruz."),
        L("Bugün üç şeyi merak ediyoruz. Gökyüzü neden mavi? Ufka doğru rengi neden açılıyor? Ve gün batımı neden kızıl?"),
        L("Bugünkü bilgilerimiz, uzay ajansı NASA'nın bilim sayfalarından geliyor: NASA Space Place ve NASA Science.", spoken="Bugünkü bilgilerimiz, uzay ajansı Nasa'nın bilim sayfalarından geliyor: Nasa Speys Pleys ve Nasa Sayıns."),
        L("Kaynakların bağlantılarını videonun açıklamasında bulabilirsin."),
        L("Her şey Güneş'le başlıyor. Güneş bizden yaklaşık 150 milyon kilometre uzakta!", [14], "Her şey Güneş'le başlıyor. Güneş bizden yaklaşık yüz elli milyon kilometre uzakta!"),
        L("Işığı bu upuzun yolu aşıp Dünya'mıza kadar geliyor.", [14]),
    ]),
    ("method", [
        L("Güneş ışığı gözümüze beyaz görünür. Ama aslında içinde gökkuşağının bütün renkleri saklıdır!", [1]),
        L("Kırmızı, sarı, yeşil, mavi... Hepsi bir araya gelince ışık beyaz görünür.", [1]),
        L("Gökkuşağına baktığında gördüğün o renklerin hepsi, Güneş ışığının içinde zaten vardır.", [1]),
        L("Işık, tıpkı denizdeki dalgalar gibi, dalga dalga yol alır.", [2]),
        L("Bir ip düşün. Ucundan yavaşça sallarsan uzun ve sakin dalgalar oluşur. Hızlı hızlı sallarsan kısa ve kıpır kıpır dalgalar!"),
        L("Işığın renkleri de böyledir. Bazı renkler uzun ve sakin dalgalarla, bazıları kısa ve kıpır kıpır dalgalarla ilerler.", [3]),
        L("Mavi ışığın dalgaları, kırmızı ışığın dalgalarından daha kısadır. Bunu aklında tut, çünkü birazdan çok işimize yarayacak!", [4]),
    ]),
    ("finding", [
        L("Şimdi işin sırrına geliyoruz. Dünya'mızın çevresi, atmosfer dediğimiz bir hava katmanıyla sarılıdır.", [5]),
        L("Güneş ışığı atmosfere girince havadaki gazlara ve minicik parçacıklara çarpar.", [5]),
        L("Havayı göremeyiz ama içi gazlarla ve parçacıklarla doludur.", [5]),
        L("Çarpan ışık her yöne doğru saçılır. Tıpkı oradan oraya seken küçük toplar gibi!", [5]),
        L("Ama bütün renkler aynı ölçüde saçılmaz.", [6]),
        L("Mavi ışık kısa ve küçük dalgalarla ilerlediği için diğer renklerden daha çok saçılır.", [6]),
        L("Her yana dağılan bu mavi ışık, gökyüzünün her köşesinden gözümüze ulaşır. İşte bu yüzden gökyüzünü mavi görürüz!", [5, 6]),
        L("Yani mavi renk tek bir yerden gelmez. Gökyüzünün her yanından bize doğru saçılır.", [5, 6]),
        L("Peki ufka doğru baktığında gökyüzünün renginin açıldığını hiç fark ettin mi?", [7]),
        L("Ufka yakın yerlerde gökyüzü açık maviye, hatta beyaza döner. Çünkü orada ışık o kadar çok saçılır ki renkler yeniden birbirine karışır.", [7, 8]),
        L("Akşam olunca gökyüzü bu kez kızıla boyanır. Neden mi?", [10]),
        L("Güneş alçaldıkça ışığı bize ulaşmak için atmosferin içinde daha uzun bir yol kat eder.", [9]),
        L("Bu uzun yolda mavi ışık daha da çok saçılır. Kırmızılar ve sarılar ise dosdoğru gözümüze ulaşır.", [10]),
        L("Gün batımının o güzel kızıl ve sarı renkleri işte böyle ortaya çıkar.", [10]),
    ]),
    ("importance", [
        L("Şimdi sıra sende! Küçük bir gökyüzü dedektifi olmaya ne dersin?"),
        L("Dışarı çıktığında önce yukarıya, sonra ufka doğru bak. Renk nasıl değişiyor?", [7]),
        L("Akşam olunca da gün batımındaki renkleri izle ve gördüklerini bir kâğıda çiz.", [10]),
        L("Gözlemlerini ailenle ya da arkadaşlarınla paylaş. Bakalım onlar bu sırrı biliyor mu?"),
        L("Yalnız unutma: Güneş'e asla doğrudan bakma. Gözlerin çok değerli!"),
    ]),
    ("limitations", [
        L("Bunu biliyor muydun? Her gezegenin gökyüzü mavi değildir!", [11]),
        L("Mars'ın havası bizimkinden çok farklıdır. Çok incedir ve çoğunlukla karbondioksit gazından oluşur.", [13]),
        L("Üstelik ince toz parçacıklarıyla doludur.", [13]),
        L("Bu yüzden Mars'ta gündüzleri gökyüzü turuncu ya da kızılımsı görünür.", [11, 13]),
        L("Güneş batarken ise Güneş'in çevresi mavi-gri bir renge bürünür. Bizim gökyüzümüzden ne kadar farklı, değil mi?", [12]),
        L("Şimdi hızlı bir soru! Hangi renk ışık havada daha çok saçılır?", [6]),
        L("Biraz düşün... Evet, bildin: Mavi!", [6]),
        L("Bir soru daha! Güneş ışığı gözümüze hangi renk görünür?", [1]),
        L("Evet, beyaz! Ama içinde bütün renkler saklı.", [1]),
    ]),
    ("summary", [
        L("Bugün bunu öğrendik!"),
        L("Bir: Güneş ışığı beyaz görünür ama içinde gökkuşağının bütün renkleri vardır.", [1]),
        L("İki: Hava, mavi ışığı diğer renklerden daha çok saçar. Gökyüzü bu yüzden mavidir.", [5, 6]),
        L("Üç: Gün batımında ışık daha uzun yol kat eder. Mavi saçılır, kırmızı ve sarı bize ulaşır.", [9, 10]),
        L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda senin sorunu araştırırız!"),
        L("Abone olmayı ve zili açmayı unutma. Merak etmeye devam!"),
    ]),
]
script = {
    "paperId": PID, "episodeNumber": 1, "videoTitle": "Gökyüzü neden mavi?", "paperTitleTr": "Gökyüzü neden mavi?",
    "sections": [{"id": s, "lines": ls} for s, ls in sections],
    "takeaways": ["Güneş ışığının içinde bütün renkler var", "Hava en çok mavi ışığı saçar", "Gün batımında kırmızı ve sarı bize ulaşır"],
    "nextTeaser": "Yeni bir soru, yeni bir keşif seni bekliyor!",
    "description": "Gökyüzü neden yeşil ya da mor değil de mavi? Ufka doğru rengi neden açılıyor, gün batımı neden kızıl? Robot arkadaşımızla Güneş ışığının içindeki renkleri, ışığın dalgalarını ve havanın ışığı nasıl saçtığını keşfediyoruz. Sonunda küçük bir gökyüzü dedektifi görevi de var!",
}

ids = {s: [l["id"] for l in ls] for s, ls in sections}
allids = [i for s, ls in sections for i in (l["id"] for l in ls)]
pos = 0
def take(k):
    global pos; out = allids[pos:pos + k]; pos += k; return out
def lf(lineids):
    by = {l["id"]: l for s, ls in sections for l in ls}
    return sorted({f for i in lineids for f in by[i]["factIds"]}, key=lambda x: int(x[1:]))
sec_of = {i: s for s, v in ids.items() for i in v}
scenes = []
def S(k, visual, mascot, note=None):
    li = take(k)
    sc = {"id": f"s{len(scenes)+1}", "section": sec_of[li[0]], "lineIds": li, "visual": visual, "mascot": mascot, "factIds": lf(li)}
    if note: sc["sourceNote"] = note
    scenes.append(sc)
R = lambda state, x=0.87, y=0.56, s=1.0, at=None: {"state": state, "x": x, "y": y, "scale": s, **({"pointAt": {"x": at[0], "y": at[1]}} if at else {})}
SP, SC = "NASA Space Place", "NASA Science"

S(3, {"type": "hook", "question": "Gökyüzü neden mavi?", "emoji": "🌤️"}, R("think", 0.15, 0.5, 1.45))
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Gökyüzü neden mavi?", "Ufka doğru rengi neden açılıyor?", "Gün batımı neden kızıl?"]}, R("talk", 0.87, 0.54, 1.15))
S(2, {"type": "source-card"}, R("point", 0.88, 0.55, 1.0, (0.45, 0.45)))
S(2, {"type": "big-number", "value": "150", "unit": "milyon km", "label": "Güneş'in Dünya'ya uzaklığı", "sub": "Işık bu yolu aşıp bize ulaşıyor"}, R("point", 0.83, 0.52, 1.25, (0.3, 0.4)), SC)
S(3, {"type": "quote-card", "quote": "Güneş'in ışığı beyaz görünür. Ama aslında gökkuşağının bütün renklerinden oluşur.", "attribution": "NASA Space Place (çeviri)"}, R("talk", 0.86, 0.54, 1.15), SP)
S(2, {"type": "diagram", "title": "Işık dalga dalga yol alır", "layout": "flow", "nodes": [{"label": "Işık dalgalar halinde ilerler", "emoji": "🌊"}, {"label": "Yavaş salla: uzun, sakin dalgalar", "emoji": "🐢"}, {"label": "Hızlı salla: kısa, kıpır kıpır dalgalar", "emoji": "🐇"}]}, R("talk", 0.91, 0.62, 0.8), SP)
S(2, {"type": "comparison", "title": "Kırmızı mı, mavi mi?", "left": {"title": "🔴 Kırmızı ışık", "items": ["Uzun dalgalar", "Sakin sakin ilerler"]}, "right": {"title": "🔵 Mavi ışık", "items": ["Kısa dalgalar", "Kıpır kıpır ilerler"]}}, R("think", 0.91, 0.6, 0.85), SP)
S(4, {"type": "diagram", "title": "Işık havaya girince ne olur?", "layout": "flow", "nodes": [{"label": "Güneş ışığı atmosfere girer", "emoji": "☀️"}, {"label": "Gazlara ve parçacıklara çarpar", "emoji": "💨"}, {"label": "Her yöne saçılır", "emoji": "✨"}]}, R("talk", 0.91, 0.62, 0.8), SP)
S(2, {"type": "analogy", "template": "scale", "title": "Hangi renk daha çok saçılır?", "a": {"label": "Kırmızı ışık: az saçılır", "value": 12}, "b": {"label": "Mavi ışık: çok saçılır", "value": 100}, "caption": "Mavi ışık diğer renklerden daha çok saçılır. (Çizim yalnızca fikir verir, ölçekli değildir.)"}, R("point", 0.9, 0.6, 0.85, (0.52, 0.4)), SP)
S(2, {"type": "bullets", "title": "İşte sır!", "items": ["Güneş ışığı atmosfere girer", "Hava ışığı her yöne saçar", "En çok mavi ışık saçılır"]}, R("talk", 0.87, 0.54, 1.15), SP)
S(2, {"type": "comparison", "title": "Yukarıda mı, ufukta mı?", "left": {"title": "⬆️ Yukarıda", "items": ["Gökyüzü mavi görünür"]}, "right": {"title": "↔️ Ufka yakın", "items": ["Açık mavi ya da beyaz", "Renkler yeniden karışır"]}}, R("think", 0.91, 0.6, 0.85), SP)
S(4, {"type": "diagram", "title": "Gün batımı neden kızıl?", "layout": "flow", "nodes": [{"label": "Güneş alçalır", "emoji": "🌇"}, {"label": "Işık daha uzun yol kat eder", "emoji": "🌫️"}, {"label": "Mavi daha çok saçılır", "emoji": "🔵"}, {"label": "Kırmızı ve sarı bize ulaşır", "emoji": "🔴"}]}, R("point", 0.91, 0.62, 0.8, (0.6, 0.45)), SP)
S(5, {"type": "bullets", "title": "Gökyüzü dedektifi görevi 🔎", "tone": "neutral", "items": ["Yukarıya ve ufka bak: renk nasıl değişiyor?", "Gün batımındaki renkleri kâğıda çiz", "Gördüklerini sevdiklerinle paylaş", "Güneş'e asla doğrudan bakma!"]}, R("talk", 0.87, 0.54, 1.15))
S(1, {"type": "quote-card", "quote": "Her gezegenin gökyüzü mavi değildir!", "attribution": "Bunu biliyor muydun?"}, R("think", 0.86, 0.54, 1.2), SP)
S(4, {"type": "comparison", "title": "Dünya ve Mars'ın gökyüzü", "left": {"title": "🌍 Dünya", "items": ["Gündüz: mavi", "Gün batımı: kırmızı ve sarı"]}, "right": {"title": "🔴 Mars", "items": ["Gündüz: turuncu ya da kızılımsı", "Gün batımı: Güneş'in çevresi mavi-gri"]}}, R("point", 0.91, 0.6, 0.85, (0.55, 0.45)), SP)
S(4, {"type": "hook", "question": "Hangi renk ışık daha çok saçılır?", "emoji": "🤔"}, R("think", 0.15, 0.5, 1.45), SP)
S(6, {"type": "outro"}, R("talk", 0.87, 0.54, 1.15))
assert pos == len(allids), (pos, len(allids))

for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": scenes})):
    json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("satır:", len(allids), "sahne:", len(scenes), "kelime:", sum(len(l["spoken"].split()) for s, ls in sections for l in ls))
