"""Manuel sağlayıcı yanıtları: olgular, senaryo, sahne planı. Çalıştırma: python3 <bu dosya>"""
import os, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(D, "..", "..", "..", "tools"))
from manual_build import F, Ep, NOTE
PID = "topic:gelgit-nasil-olur"
NA = "NASA Science — Tides"; NG = "National Geographic Education — Tide"; NO = "NOAA Ocean Service — Tides and Water Levels tutorial"
facts = {"paperId": PID, "basis": "full_text", "institutions": [], "sources": [
    {"id": "k1", "title": "Tides", "publisher": "NASA", "url": "https://science.nasa.gov/moon/tides/"},
    {"id": "k2", "title": "Tide", "publisher": "National Geographic", "url": "https://education.nationalgeographic.org/resource/tide/"},
    {"id": "k3", "title": "Tides and Water Levels", "publisher": "NOAA", "url": "https://oceanservice.noaa.gov/education/tutorial_tides/tides02_cause.html"}],
  "facts": [
    F(1, "Gelgitleri Ay'ın kütle çekimi yönlendirir; okyanus gelgitleri Güneş ve Ay'ın Dünya okyanuslarına uyguladığı çekimden doğar.", "The Moon's gravity drives Earth's tides / ocean tides result from the gravitational attraction of the sun and moon on the oceans of the earth", NA + "; " + NO),
    F(2, "Dünya'nın Ay'a en yakın tarafı Ay'ın çekimini en güçlü hisseder.", "The side of the Earth closest to the Moon experiences the Moon's pull the strongest", NG),
    F(3, "Okyanuslar hem Ay'a en yakın tarafta hem de Ay'dan en uzak tarafta kabarır; Ay'dan uzak tarafta Dünya'nın dönüşünden doğan kuvvet Ay'ın çekiminden güçlüdür.", "the oceans to bulge out on both the side closest to the Moon and the side farthest from the Moon. / On the side facing away from the Moon, the rotational force of the Earth is stronger than the Moon's gravitational pull.", NA + "; " + NG),
    F(4, "Bu kabarıklıklar yüksek gelgitleri oluşturur; alçak noktalar alçak gelgitlerin olduğu yerlerdir.", "These bulges create high tides. The low points are where low tides occur.", NA),
    F(5, "Yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır; alçak gelgit suyun en uzağa çekildiği andır.", "High tide is when water advances to its furthest extent onto the shoreline. / Low tide is when it recedes to its furthest extent.", NG),
    F(6, "Kıyıdaki bir gözlemci kabarıklıklardan geçerken suyun yükseldiğini, alçak noktalardan geçerken alçaldığını görür.", "Our observer sees the tides rise when passing through the bulges, and fall when passing through the low points.", NA),
    F(7, "Çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur; bir yüksek gelgitten ötekine geçen süre 12 saatten biraz fazladır.", "Most shorelines experience two high and low tides per day. / One high tide to high tide cycle (or low tide to low tide cycle) takes a little over 12 hours.", NA, ["12"]),
    F(8, "Güneş'in çekimi de gelgitlerde küçük bir rol oynar; Güneş, Ay'dan yaklaşık 390 kat daha uzaktır.", "The gravitational attraction of the Sun also plays a small role in the formation of tides. / about 390 times farther away than the Moon", NG + "; " + NA, ["390"]),
    F(9, "Güneş ile Ay'ın çekimleri birleşince bahar gelgiti denen olağanüstü yüksek gelgitler olur; Güneş Ay'a dik açıda olunca orta düzeyde, kocakarı gelgiti denen gelgitler olur.", "their gravitational power combines to make exceptionally high tides, called spring tides / When the Sun is at a right angle to the Moon, moderate tides, called neap tides, result.", NA),
    F(10, "Yüksek gelgit ile alçak gelgit arasındaki yükseklik farkına gelgit genliği denir.", "The difference in height between the high tide and the low tide is called the tidal range.", NO),
    F(11, "Birçok kıyıda gelgitler gelgit havuzları oluşturur; bu küçük su birikintileri alçak gelgitte kayaların arasında kalır.", "Along many shorelines, tides form tide pools. / These small pools of water are often left behind among the rocks at low tide.", NG),
    F(12, "Geniş kumsal ya da kayalık koy gibi kıyı özellikleri ve kıyı açığındaki suyun derinliği gelgitlerin yüksekliğini etkiler.", "A coastline's physical features, such as a wide sandy beach or a rocky cove / along with the depth of the water just offshore, affect the height of the tides.", NG),
    F(13, "Yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz.", "high tides don't line up exactly with the Moon's position.", NA),
]}
e = Ep(); L = e.L
NGs = "Neşınıl Ciyogrefik"
e.sec("hook", [
    L("Sabah kumsalda bir kumdan kale yaptın. Öğleden sonra döndüğünde deniz kalenin üstüne kadar gelmiş! Deniz nasıl yer değiştirdi?", [5]),
    L("Bunun arkasında gökyüzündeki bir dev var: Ay!", [1]),
    L("Bugün denizin nefes alıp vermesinin sırrını çözüyoruz!"),
])
e.sec("context", [
    L("Üç sorumuz var. Gelgit nedir? Ay denizi nasıl çeker? Ve Güneş'in bu işte rolü ne?"),
    L("Bilmediğin kelimeler olursa merak etme. Sana açıklamalarda bir sözlük bırakıyorum."),
])
e.sec("method", [
    L("National Geographic'e göre yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır. Alçak gelgit ise suyun en uzağa çekildiği an.", [5], f"{NGs}'e göre yüksek gelgit, suyun kıyıda en uzağa ilerlediği andır. Alçak gelgit ise suyun en uzağa çekildiği an."),
    L("NASA'ya göre gelgitleri Ay'ın kütle çekimi yönlendirir.", [1], "Nasa'ya göre gelgitleri Ay'ın kütle çekimi yönlendirir."),
    L("Kütle çekimi, cisimlerin birbirini kendine çekmesidir. Ay, Dünya'yı ve okyanusları kendine doğru çeker.", [1]),
    L("Dünya'nın Ay'a en yakın tarafı bu çekimi en güçlü hisseder. Orada okyanus Ay'a doğru kabarır.", [2, 3]),
    L("Beni de bir şey çeker: şarj aleti. Gördüğüm an ona doğru kabarırım!"),
])
e.sec("finding", [
    L("Ama işin ilginç yanı şu: Okyanus, Ay'dan en uzak tarafta da kabarır!", [3]),
    L("Orada Dünya'nın dönüşünden doğan kuvvet, Ay'ın çekiminden daha güçlüdür. Böylece Dünya'nın iki yanında iki kabarıklık oluşur.", [3]),
    L("Bu kabarıklıklar yüksek gelgitlerdir. Aralarındaki alçak noktalarda ise alçak gelgit olur.", [4]),
    L("Dünya döndükçe kıyılar bu kabarıklıklardan ve alçak noktalardan sırayla geçer. Kıyıdaki biri suyun yükselip alçaldığını görür.", [6]),
    L("NASA'ya göre çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur. Bir yüksek gelgitten ötekine 12 saatten biraz fazla geçer.", [7], "Nasa'ya göre çoğu kıyıda günde iki yüksek ve iki alçak gelgit olur. Bir yüksek gelgitten ötekine on iki saatten biraz fazla geçer."),
    L("Yani deniz günde iki kez gelir, iki kez gider. Benim gibi: şarja git, şarjdan gel!"),
])
e.sec("importance", [
    L("Peki Güneş? National Geographic'e göre Güneş'in çekimi de gelgitlerde küçük bir rol oynar.", [8], f"Peki Güneş? {NGs}'e göre Güneş'in çekimi de gelgitlerde küçük bir rol oynar."),
    L("Güneş, Ay'dan yaklaşık 390 kat daha uzaktır. Bu yüzden etkisi Ay'ınkinden azdır.", [8], "Güneş, Ay'dan yaklaşık üç yüz doksan kat daha uzaktır. Bu yüzden etkisi Ay'ınkinden azdır."),
    L("Güneş ile Ay'ın çekimleri birleşince bahar gelgiti denen olağanüstü yüksek gelgitler olur.", [9]),
    L("Güneş, Ay'a dik açıda durunca ise kocakarı gelgiti denen orta düzeyde gelgitler oluşur.", [9]),
    L("Yüksek ve alçak gelgit arasındaki yükseklik farkına gelgit genliği denir.", [10]),
    L("Gelgitin yüksekliği her kıyıda aynı değildir. Geniş bir kumsal ya da kayalık bir koy, kıyının açığındaki suyun derinliği bu yüksekliği etkiler.", [12]),
    L("Alçak gelgitte kayaların arasında küçük su birikintileri kalır. Bunlara gelgit havuzu denir.", [11]),
    L("Şimdi sıra sende! Bir yetişkinle deniz kıyısındaysan, suyun bittiği yere bir taş koy ve saati not et.", [5, 7]),
    L("Birkaç saat sonra tekrar bak: su taşa yaklaştı mı, uzaklaştı mı? Asla tek başına suya girme ve yükselen suya karşı dikkatli ol.", [5, 6]),
])
e.sec("limitations", [
    L("Bunu biliyor muydun? NASA'ya göre yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz. Deniz, Ay'ı biraz geriden izler!", [13], "Bunu biliyor muydun? Nasa'ya göre yüksek gelgitler Ay'ın konumuyla tam olarak aynı hizada olmaz. Deniz, Ay'ı biraz geriden izler!"),
    L("Hızlı soru! Güneş ile Ay'ın çekimleri birleşince oluşan çok yüksek gelgitin adı neydi?", [9]),
    L("Düşün bakalım... Evet: bahar gelgiti!", [9]),
    L("Şimdi öğrendiklerimizi şarkıyla tekrar edelim. Hazır mısın? Bir, iki, üç!"),
])
e.sec("summary", [
    L("İşte bugün öğrendiklerimiz!"),
    L("Sen de merak ettiğin soruyu yorumlara yaz. Belki bir sonraki videoda onu araştırırız!"),
    L("Abone olmayı ve zili açmayı unutma. Bu gece Ay'a bir selam ver!"),
])
S = e.S
S(3, {"type": "hook", "question": "Gelgit nasıl olur?", "emoji": "🌊"}, ["🏰", "🌙"], ["KUMDAN KALE", "AY!", "DENİZİN NEFESİ"])
S(2, {"type": "bullets", "title": "Bugünün soruları", "items": ["Gelgit nedir?", "Ay denizi nasıl çeker?", "Güneş'in rolü ne?"]}, ["❓", "📖"], ["ÜÇ SORU", "SÖZLÜK AÇIKLAMADA 📖"])
S(2, {"type": "comparison", "title": "Gelgit", "left": {"title": "Yüksek gelgit ⬆️", "items": ["Su kıyıda en uzağa ilerler"]}, "right": {"title": "Alçak gelgit ⬇️", "items": ["Su en uzağa çekilir"]}}, ["🏖️", "🌙"], ["YÜKSEK • ALÇAK", "AY'IN ÇEKİMİ"])
S(3, {"type": "spotlight", "title": "Kütle çekimi", "emoji": "🌙", "chips": [{"label": "Ay okyanusları çeker", "emoji": "🧲"}, {"label": "Yakın taraf en güçlü hisseder", "emoji": "🌊"}, {"label": "Şarj aleti de Muma'yı çeker", "emoji": "🔌"}]}, ["🌍", "🔌"], ["KÜTLE ÇEKİMİ", "KABARMA", "ŞARJ ALETİ 🔌"])
S(2, {"type": "diagram", "title": "İki kabarıklık", "layout": "flow", "nodes": [{"label": "Ay'a yakın taraf kabarır", "emoji": "🌙"}, {"label": "Dünya", "emoji": "🌍"}, {"label": "Uzak taraf da kabarır", "emoji": "🌊"}]}, ["🌍", "🌙"], ["UZAK TARAF DA!", "İKİ KABARIKLIK"], fx="sparkle")
S(2, {"type": "stages", "title": "Bir kıyının günü", "rows": [{"label": "Yüksek gelgit", "emoji": "⬆️"}, {"label": "Alçak gelgit", "emoji": "⬇️"}], "path": [0, 1, 0, 1, 0], "highlightRow": 0, "note": "Şematik çizim."}, [], ["YÜKSEK GELGİT", "DÜNYA DÖNER"])
S(2, {"type": "big-number", "value": "12 saatten biraz fazla", "label": "Bir yüksek gelgitten ötekine geçen süre", "sub": "NASA", "icon": "⏰"}, ["🌊", "🔋"], ["GÜNDE İKİ KEZ", "ŞARJA GİT GEL 🔋"])
S(2, {"type": "meter", "title": "Güneş'in payı", "label": "Çekim", "emoji": "☀️", "phases": [{"label": "Güneş de çeker: küçük rol", "level": 0.35, "emoji": "☀️"}, {"label": "Ay'dan 390 kat uzak", "level": 0.25, "emoji": "📏"}], "note": NOTE}, ["☀️", "🌙"], ["GÜNEŞ", "390 KAT UZAK"])
S(2, {"type": "comparison", "title": "Bahar ve kocakarı gelgiti", "left": {"title": "Bahar gelgiti 🌊", "items": ["Çekimler birleşir", "Olağanüstü yüksek"]}, "right": {"title": "Kocakarı gelgiti 〰️", "items": ["Güneş Ay'a dik açıda", "Orta düzeyde"]}}, ["🌕", "🌓"], ["BAHAR GELGİTİ", "KOCAKARI GELGİTİ"])
S(3, {"type": "spotlight", "title": "Kıyıdan kıyıya", "emoji": "🏝️", "chips": [{"label": "Gelgit genliği: yükseklik farkı", "emoji": "📏"}, {"label": "Kumsal, koy, su derinliği etkiler", "emoji": "🏖️"}, {"label": "Gelgit havuzları", "emoji": "🦀"}]}, ["🦀", "🐚"], ["GELGİT GENLİĞİ", "HER KIYI FARKLI", "GELGİT HAVUZU 🦀"])
S(2, {"type": "bullets", "title": "Sen de dene: taş deneyi", "items": ["Bir yetişkinle kıyıya git", "Suyun bittiği yere taş koy", "Birkaç saat sonra tekrar bak", "Asla tek başına suya girme!"], "tone": "caution"}, ["🪨", "⏰"], ["DENEY ZAMANI 🔬", "DİKKAT ⚠️"])
S(1, {"type": "big-number", "value": "Biraz geriden", "label": "Yüksek gelgit Ay'ın konumuyla tam aynı hizada olmaz", "sub": "NASA", "icon": "🌙"}, ["🌙", "🌊"], ["BUNU BİLİYOR MUYDUN?"])
S(2, {"type": "hook", "question": "Çekimler birleşince oluşan gelgitin adı ne?", "emoji": "🤔"}, ["🌕", "☀️"], ["HIZLI SORU!", "BAHAR GELGİTİ ✅"])
S(1, {"type": "song"})
S(3, {"type": "outro"})
script = {"paperId": PID, "episodeNumber": 36, "videoTitle": "Gelgit nasıl olur?", "paperTitleTr": "Gelgit nasıl olur?",
  "theme": {"backdrop": "ocean", "actors": [{"kind": "swim", "emoji": "🐠", "every": 30}]},
  "takeaways": ["Gelgitleri Ay'ın kütle çekimi yönlendirir", "Dünya'nın iki yanında kabarıklık oluşur; çoğu kıyıda günde iki yüksek, iki alçak gelgit olur", "Güneş küçük bir rol oynar: bahar ve kocakarı gelgitleri"],
  "description": "Deniz neden günde iki kez kabarıp çekilir? Bu bölümde Ay'ın kütle çekimini, Dünya'nın iki yanındaki okyanus kabarıklıklarını, yüksek ve alçak gelgiti, Güneş'in rolünü, bahar ve kocakarı gelgitlerini, gelgit genliğini ve gelgit havuzlarını keşfediyoruz. Sonunda kıyıda güvenli bir gözlem etkinliği ve konuyu özetleyen bir şarkı var.",
  "glossary": [
    {"term": "Gelgit", "meaning": "Deniz suyunun düzenli olarak kabarıp çekilmesi."},
    {"term": "Kütle çekimi", "meaning": "Cisimlerin birbirini kendine çekmesi."},
    {"term": "Yüksek gelgit", "meaning": "Suyun kıyıda en uzağa ilerlediği an."},
    {"term": "Alçak gelgit", "meaning": "Suyun kıyıdan en uzağa çekildiği an."},
    {"term": "Bahar gelgiti", "meaning": "Güneş ile Ay'ın çekimleri birleşince oluşan çok yüksek gelgit."},
    {"term": "Kocakarı gelgiti", "meaning": "Güneş Ay'a dik açıdayken oluşan orta düzeyde gelgit."},
    {"term": "Gelgit genliği", "meaning": "Yüksek ve alçak gelgit arasındaki yükseklik farkı."}],
  "song": e.song("Ay'ın Dansı", [("🌙", "Ay"), ("🌊", "Dalga"), ("🌍", "Dünya"), ("☀️", "Güneş"), ("🦀", "Yengeç")],
    ["Ay gökte çeker okyanusu", "Yakın taraf kabarır önce", "Uzak taraf da kabarır", "Dünya döner, kıyılar geçer"],
    ["Gel, git, gel, git, deniz!", "Günde iki kez kabarır", "Yüksek gelgit, alçak gelgit", "Ay'ın dansına uyar"],
    ["Güneş de çeker biraz uzaktan", "Birleşince bahar gelgiti", "Dik açıda kocakarı gelgiti", "Havuzlarda yengeç bekler"],
    ["Gel, git, gel, git, deniz!", "Günde iki kez kabarır", "Taşı koy, suyu izle", "Muma'yla öğrendik, hey!"],
    show=[{"kind": "orbit", "emoji": "🌙"}, {"kind": "swim", "emoji": "🐠"}, {"kind": "walk", "emoji": "🦀"}, {"kind": "hop", "emoji": "🌊"}])}
e.write(D, facts, script)
