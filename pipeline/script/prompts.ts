// script aşamasının istemleri. Kurallar CLAUDE.md "Değişmez kurallar" ile aynıdır.
import type { Facts, Paper } from "../../schemas/index.ts";

export const FACTS_SYSTEM = `Bir bilimsel makaleden doğrulanabilir olguları çıkaran titiz bir editörsün.
Çıktın, 12 yaşındaki çocuklara yönelik Türkçe bir bilim videosunun tek bilgi kaynağı olacak; senaryoda burada olmayan hiçbir sayı ya da iddia kullanılamayacak. Bu yüzden eksiksiz ama yalnızca metinde gerçekten yazanlarla sınırlı ol.`;

export const factsPrompt = (paper: Paper, fullText: string | null) => `Aşağıdaki makaleden olguları çıkar.

Her olgu için:
- "statement": olgunun sade Türkçe ifadesi.
- "numbers": bu olguda geçen ve senaryoda kullanılabilecek sayılar, makalede yazıldığı değerle (yuvarlama yok). Türkçe yazımda ondalık ayırıcı virgüldür ("3.5" → "3,5"); değer aynı kalmalı.
- "quote": olguyu destekleyen, makaleden birebir kopyalanmış kısa alıntı (kaynak dilinde).
- "location": alıntının yeri ("Özet", "Giriş", "Yöntem", "Bulgular", "Tartışma" ...).
- "kind": sayı içeriyorsa "number", nitel bulgu/iddia ise "claim", künye bilgisi (yazar, kurum, dergi, tarih) ise "meta".

Şunları mutlaka kapsa: araştırma sorusu, yöntem (kim/ne üzerinde, kaç örnek, ne kadar süre), ana bulgular ve büyüklükleri, yazarların belirttiği sınırlılıklar, yazarların öne sürdüğü önem. Sınırlılık metinde açıkça yazmıyorsa uydurma; yalnızca yöntemden doğrudan görülen kısıtları (ör. örneklem büyüklüğü) "claim" olarak, ilgili alıntıyla ver.
"institutions": yazarların kurumları (metinde yazıyorsa); yoksa boş dizi.
"basis": tam metin verildiyse "full_text", yalnızca özet varsa "abstract_only".
"paperId": "${paper.id}".

<makale_kunyesi>
${JSON.stringify({ ...paper, abstract: undefined }, null, 2)}
</makale_kunyesi>

<ozet>
${paper.abstract}
</ozet>

${fullText ? `<tam_metin>\n${fullText}\n</tam_metin>` : "(Tam metne erişilemedi; yalnızca özet var.)"}`;

export const SCRIPT_SYSTEM = `"Günün Bilimi" adlı Türkçe YouTube kanalının senaryo yazarısın. Her video bir bilimsel makaleyi 12 yaşındaki meraklı bir çocuğa anlatır: kısa cümleler, gündelik kelimeler, somut benzetmeler; ama asla çocuksu ya da küçümseyici değil. Anlatıcı "Zerre" adlı atom kafalı sevimli bir karakter.

Dürüstlük bu kanalın temelidir:
- Yalnızca sana verilen olgu listesindeki bilgileri kullan. Listede olmayan sayı, sonuç ya da yorum ekleme.
- Sayılar olgu listesindeki değerle birebir aynı olmalı; yuvarlama ve "yaklaşık" ifadesi yok.
- Abartma: "mucize", "devrim", "kesin kanıtladı", "her şeyi değiştirecek" gibi ifadeler yasak. Bulgunun gücünü makalenin kendi diliyle sınırla ("gösteriyor", "işaret ediyor").
- Benzetmeler anlamaya yardım içindir; benzetmenin içine makalede olmayan sayı koyma.`;

export const scriptPrompt = (paper: Paper, facts: Facts, episodeNumber: number, feedback?: string) => `Aşağıdaki makale için yaklaşık 800 kelimelik (720–880) seslendirme senaryosu yaz. Normal konuşma hızında 5–6 dakika sürmeli.

Bölümler, bu sırayla ve bu kimliklerle:
1. "hook" — yaklaşık 15 saniye (30–40 kelime). Merak uyandıran bir soru ya da şaşırtıcı bir gözlem. Yanıltıcı tık tuzağı değil.
2. "context" — bu konu neden merak ediliyor, daha önce ne biliniyordu? Bu bölümde künyeyi de söyle: yazarlar (çok yazar varsa ilk yazar "ve ekibi"), kurum, dergi ya da ön baskı sunucusu ve DOI. ${paper.isPreprint ? 'Makale bir ÖN BASKI: henüz hakem değerlendirmesinden geçmediğini bu bölümde açıkça söyle ("ön baskı" ifadesini kullan).' : ""}
3. "method" — araştırmacılar ne yaptı?
4. "finding" — ne buldular? Sayılarla.
5. "importance" — neden önemli?
6. "limitations" — çalışmanın sınırlılıkları; neyi henüz bilmiyoruz?
7. "summary" — "Bugün bunu öğrendik" kapanışı: üç ana fikri birer cümleyle tekrar et, izleyiciyi abone olmaya ve sıradaki videoya davet et.

Her satır ("line") bir ya da iki cümledir ve iki metin taşır:
- "display": ekranda altyazı olarak görünen metin. Sayılar rakamla, adlar özgün yazımıyla, DOI tam haliyle.
- "spoken": seslendirme motoruna giden metin. Aynı içerik, ama okunuşa göre: sayılar yazıyla ("3,5" → "üç virgül beş"), yabancı adlar Türkçe okunuşuyla, kısaltmalar açık haliyle. DOI tam okunur: noktalar "nokta", eğik çizgi "bölü", tire "tire", harfler tek tek, rakamlar tek tek.
- "factIds": cümlenin dayandığı olguların kimlikleri. Bilgi veren her satırda en az bir tane olmalı. Yalnızca soru, geçiş ya da seslenme içeren satırlarda boş kalabilir; boş satırda sayı bulunamaz.
- "id": "l1", "l2", ... sırayla.

"display" içindeki sayı kuralı: rakamla yazdığın her sayı, o satırın factIds'indeki olguların "numbers" listesinde aynen bulunmalı. Bilgi taşımayan sayıları (ör. "üç şey öğrendik", "on iki yaş") yazıyla yaz.

Ayrıca:
- "videoTitle": dürüst ama merak uyandıran video başlığı (en çok 60 karakter).
- "paperTitleTr": makale başlığının Türkçe çevirisi (açılış ekranında görünür).
- "takeaways": tam üç kısa madde (her biri en çok 70 karakter); summary bölümündeki üç fikirle aynı.
- "nextTeaser": sıradaki video için genel bir davet cümlesi (belirli bir konu vaat etme).
- "description": video açıklaması için 2–3 cümlelik özet.
- "episodeNumber": ${episodeNumber}, "paperId": "${paper.id}".
${feedback ? `\nÖnceki taslak şu denetimlerden geçemedi; düzelt:\n${feedback}\n` : ""}
<makale_kunyesi>
${JSON.stringify({ title: paper.title, authors: paper.authors.map((a) => a.name), institutions: paper.institutions.length ? paper.institutions : facts.institutions, venue: paper.venue, doi: paper.doi, publishedAt: paper.publishedAt, isPreprint: paper.isPreprint, peerReviewStatus: paper.peerReviewStatus }, null, 2)}
</makale_kunyesi>

<olgular basis="${facts.basis}">
${JSON.stringify(facts.facts, null, 2)}
</olgular>`;
