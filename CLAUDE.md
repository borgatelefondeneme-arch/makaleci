# MuMa Library — proje kararları

Çocuklar için Türkçe, eğlenceli ve öğretici 5 dakikalık animasyonlu bilim videoları üreten hat. **Kanal adı: MuMa Library** (ekranda ve seslendirmede bu ad kullanılır). Bu dosya onaylanmış kararları tutar; bir karar değişirse önce burası güncellenir.

## İçerik yönü (güncel karar)

- **Ana içerik: konu bölümleri** (`kind: "topic"`). Çocukların gelişimini destekleyen ve merak ettikleri sorular ("Gökyüzü neden mavi?"). Hedef yaş **7–14**, süre ~5 dk. Konuyu ve senaryoyu biz belirleriz.
- Her konu bölümünde: merak uyandıran açılış → günün sorusu ve kaynaklar → "Nasıl oluyor?" → "İşin sırrı" → **"Sen de dene"** (güvenli bir gözlem/etkinlik) → "Bunu biliyor muydun?" + kısa tekrar sorusu → "Bugün bunu öğrendik".
- Bilgiler güvenilir kurum kaynaklarından (NASA vb.) alınır; kaynak sayfası **gerçekten okunur**, alıntısı `03_facts.json`'a yazılır. Kaynakta bulunamayan bilgi/sayı senaryoya girmez.
- **Minik komiklikler:** bölüm başına 4–6 küçük şaka (robotun kendisiyle dalga geçmesi: uyumaz şarj olur, kapatma düğmesi yoktur; kelime oyunları). Şaka bilgi gibi sunulmaz, olguyu çarpıtmaz, kimseyle alay etmez.
- **Sabit açılış ve kapanış:** her video robotun uçarak gelmesi ve "MuMa Library'ye hoş geldin!" cümlesiyle başlar; "Bir sonraki bilim videosunda görüşürüz! Hoşça kal!" cümlesi ve robotun uçarak gitmesiyle biter. Bu cümleler voice aşamasında otomatik eklenir (`pipeline/voice/cli.ts` içinde `WELCOME`/`GOODBYE`), senaryoya yazılmaz.
- **Telaffuz:** "MuMa Library" seslendirmede okunduğu gibi "Muma Laybrıri" denir (kullanıcı onayı).
- **Kapanış şarkısı:** videonun son ~1 dakikasında konuyu özetleyen neşeli, marş/çizgi film havasında bir şarkı. Müzik **ElevenLabs Music** ile üretilir (Suno değil; ticari risk nedeniyle kullanıcı kararı). Sözleri biz yazarız (yalnızca `03_facts.json`'daki bilgilerle; rakam yok; **sözlerde şarkının adı geçmez**), API'ye `composition_plan` ile veririz; tarz tarifinde sanatçı, şarkı ya da eser adı geçmez. Toplam süre ~5 dk kalır: anlatım ~4 dk + şarkı ~1 dk.
- **Şarkı Muma'nın sesiyle söylenir** (kullanıcı kararı). Müzik modeli belirli bir sesle söyleyemediği için dolaylı yol: şarkı üretilir → vokal ayrılır (stem separation) → Muma'nın sesine dönüştürülür (speech-to-speech) → çalgılarla yeniden karıştırılır. Özgün sürüm `song.original.mp3` olarak saklanır; `--no-convert` dönüştürmeyi atlar.
- **Şarkı sahnesinde Muma yoktur.** Dans edenler konuya özel karakterlerdir (`song.cast`: emoji + ad; uyku → Ay, Ana Saat, Beyin, Yıldız, Yatak; uzay → gezegenler ve yıldızlar; DNA → DNA sarmalı vb.). Muma şarkıya davet edip sahneden çekilir, veda için geri gelir.
- **Sözlük:** her bölümde çocukların bilmeyebileceği 3–8 kelime `glossary` alanına yazılır; Muma anlatımda "Sana açıklamalarda bir sözlük bırakıyorum" der; anlamlar `yayin.md`'deki "Sözlük" bölümüne çıkar.
- **Yaşa uygunluk:** konu seçerken ve anlatırken izleyicinin 7–14 yaşında olduğu unutulmaz. Konu ne bebekçe ne ders kitabı gibi; bir fikir anlatılmadan terimi kullanılmaz, aynı anda en çok bir yeni kavram.
- Güvenlik gerektiren etkinliklerde açık uyarı (ör. "Güneş'e asla doğrudan bakma").
- Makale bölümleri (`kind: "paper"`, aşağıdaki fetch/select akışı) kodda durur ve çalışır; şu an öncelik değil.
- Giriş ve çıkış taslağı her iki türde aynıdır (açılış 5 sn, kapanışta ✓'li özet + abone ol + sıradaki video).

## Değişmez kurallar (içerik)

- **Makale şekilleri kullanılmaz.** Hiçbir aşama makaleden görsel indirmez; tüm grafikler `03_facts.json` verisinden kendi bileşenlerimizle çizilir.
- **Sayılar makaleden birebir.** Senaryodaki her sayı `03_facts.json`'da kaynak alıntısıyla bulunmalıdır; yuvarlama, "yaklaşık"a çevirme yok. Denetim geçmeyen senaryo render'a gidemez.
- **Kaynaksız iddia yok.** Her bilgi cümlesi en az bir `factId` taşır.
- **Preprint açıkça belirtilir:** açılışta rozet, seslendirmede cümle, tüm video boyunca köşe etiketi, `yayin.md`'de not. Sınıflama belirsizse preprint sayılır.
- **Abartı yok.** "Mucize", "kesin kanıtladı", "devrim" gibi ifadeler denetimde reddedilir.
- **Künye hem seste hem ekranda:** yazarlar, kurum, dergi, DOI. DOI seslendirmede **tam okunur** (kullanıcı kararı), ekranda tam yazılır.
- Yayın öncesi insan onayı şarttır; select kuyruğu onaysız ilerlemez.

## Teknoloji

- Video: Remotion (React/TypeScript) + FFmpeg. Çıktı **1920×1080, 30 fps, H.264 MP4**.
- Veri toplama (fetch): Python, yalnızca standart kütüphane. Geri kalan tüm aşamalar TypeScript (`tsx` ile çalışır).
- Şemalar: `schemas/` altında **zod**; aşamalar arası tek sözleşme budur. Her aşama çıktısını yazmadan önce, sonraki aşama okurken doğrular.
- LLM: Claude API (`@anthropic-ai/sdk`, varsayılan model `claude-opus-5-5`, `CLAUDE_MODEL` ile değişir). **Hibrit:** kimlik bilgisi yoksa `pipeline/llm/manual.ts` devreye girer — istemi `episodes/<id>/manual/<aşama>.prompt.md`'ye yazar, yanıtı `manual/<aşama>.json`'dan okur.
- Ses önceliği: ElevenLabs → **Piper** (yerel, yalnızca taslak; `tools/setup-piper.sh`) → **mock** (sessiz). **Model: `eleven_v4`** — kullanıcı kararı: bundan sonraki her videoda seslendirme bu modelle yapılır (`ELEVENLABS_MODEL` ile değişir). Aynı metin yeniden sentezlenmez (`.cache/tts`).
- Node'un `fetch`'i vekil sunucuyu kendiliğinden kullanmaz: ElevenLabs'e giden komutlar `NODE_USE_ENV_PROXY=1 ELEVENLABS_API_KEY=proxy-injected` ile çalıştırılır (bu ortamda anahtarı vekil ekler).
- **Muma'nın sesi (ElevenLabs):** kullanıcının seçtiği tasarım sesi hesaba "Muma" adıyla kaydedildi, kimliği `j6hEdvUHjDuCExVlNXTi` (`ELEVENLABS_VOICE_ID` verilmezse varsayılan budur). Her videoda aynı ses kullanılır. ElevenLabs çocuk sesi üretimini engeller; ses, yetişkin seslendirmecinin canlandırdığı parlak, heyecanlı bir çizgi film robotu olarak tarif edildi. Anahtar ortamın ağ gizlisi olarak saklı (kod içinde `ELEVENLABS_API_KEY=proxy-injected` yer tutucusu yeterli).
- **Piper sesi yalnızca taslak içindir:** eğitim verisi CC BY-NC-SA 4.0 (ticari kullanım dışı). Gelir getiren yayında ElevenLabs ya da ticari kullanıma açık bir ses kullanılır.
- Font: Nunito (başlık) + Inter (metin), `@fontsource` paketlerinden gömülü; render sırasında ağ gerekmez.

## Mimari

Altı aşama; her biri ayrı CLI, yalnızca JSON dosyalarıyla haberleşir, birbirinin kodunu import etmez (ortak: `schemas/`, `pipeline/lib/`, `pipeline/llm/`).

| # | Aşama | Komut | Çıktı (`episodes/<id>/`) |
|---|---|---|---|
| 1 | fetch | `npm run fetch -- --url <link> --out <dosya>` | `01_paper.json` |
| 2 | select | `npm run select`, `npm run queue -- list\|approve\|reject <id>` | `data/queue/*.json`, `02_selection.json` |
| 3 | script | `npm run script -- <episodeDir>` | `03_facts.json`, `03_script.json` |
| 4 | sceneplan | `npm run sceneplan -- <episodeDir>` | `04_scenes.json` |
| 4b | song | `npm run song -- <episodeDir>` | `song.mp3`, `song.original.mp3`, `05_song.json` (senaryoda şarkı yoksa atlar; yeniden üretim kota harcar, `--force` ister) |
| 5 | voice | `npm run voice -- <episodeDir>` | `audio/`, `05_voice.json` |
| 6 | render | `npm run render -- <episodeDir>` | `out/video.mp4`, `out/thumbnail.png`, `out/yayin.md` |

Uçtan uca: konu bölümü `npm run episode -- --topic "<soru>"` (fetch/select atlanır), makale bölümü `npm run episode -- --url <link>`. Aşamalar çıktısı varsa atlanır; `--force` yeniden üretir, `--from <aşama>` o aşamadan başlatır.

- Bölüm kimliği: `<YYYY-AA-GG>-<slug>`; bölüm numarası (#n) `data/state.json` sayacından.
- Senaryo satırlarında iki metin: `display` (ekran) ve `spoken` (seslendirme; sayılar, yabancı adlar, DOI Türkçe okunuşla).
- Süre: konu bölümlerinde hedef ~5:00 (kapı 4:45–6:00). Sahne süresi sesten türetilir (ses + nefes payı); sahne içi vuruşlar satır başlangıç karelerine bağlanır.
- Mascot ağzı: voice aşaması kare başına genlik zarfı üretir (mock'ta kelime damgalarından sentezlenir), render aynı kodu kullanır.
- Render sessiz yapılır, ses FFmpeg ile eklenir (gerçek seste `loudnorm`).

## Video yapısı

- Açılış (~5 sn): robot uçarak gelir + "MuMa Library" logosu + "Hoş geldin!" + "Günün Sorusu #n" (makale bölümünde "Günün Makalesi #n") + başlık (+ preprint rozeti).
- Sahne tipleri: `hook`, `source-card`, `big-number`, `bar-chart`, `line-chart`, `comparison`, `diagram`, `analogy` (şablonlar: `scale`, `fill`, `race`, `zoom`), `quote-card`, `bullets`, `song`, `outro`. Aynı tip art arda gelmez.
- **Karakter her zaman kullanıcının verdiği robottur** (cin kuyruklu, yay antenli, göğsünde "M" amblemi). Başka karakter kullanılmaz. Görseller `public/robot/` altında, `tools/cutout.py` ile saydam zeminli kesildi. Pozlar: `point` (parmak havada + açık el; yüksek çözünürlüklü özgün görselden), `crossed` (kollar kavuşuk), `book` (kitap okur), `thumbs` (başparmak), `wave` (el sallar), `fly` (kollar açık; yalnızca uçarken). Poz, sahnede `mascot.pose` ile seçilir; verilmezse durumdan türetilir (`talk`/`point` → `point`, `idle`/`think` → `crossed` + düşünce baloncuğu) ve sahne tipine göre otomatik atanır: açılış ve veda `wave`, kaynak kartı `book`, kapanış `thumbs`. **Ağız sese göre oynar** (kullanıcı bunu özellikle beğendi; korunur), anten yıldızı parlar, kuyruk salınır, sahneler arasında konum/ölçek yumuşak geçer; açılışta uçarak gelir, kapanışta uçarak gider (`MascotLayer.tsx`). Kollar yeniden çizilmez.
- Videodan kare dizisiyle oynatma denendi ve geri alındı: kesim kalitesi düşüktü ve dudak eşlemesi kayboluyordu. Kullanıcı yeni klipler verirse `tools/cutout_video.py` ile işlenir; iyi sonuç için yüksek çözünürlük, düz tek renk zemin (gölgesiz), sabit kamera gerekir. **Karakterin adı: Muma.** Kendini "Ben Muma!" diye tanıtır.
- Abone ol: sürenin ~%60'ına en yakın sahne sınırında kısa alt bant; kapanışta tam kart.
- Kapanış: "Bugün bunu öğrendik" + 3 madde sırayla ✓ + "Bir sonraki bilim videosunda görüşürüz!" + abone ol + sonraki video; robot uçarak gider.
- Stil: koyu lacivert zemin, 4 vurgu rengi (turkuaz, sarı, mercan, mor), yumuşak geçişler, arka planda hafif hareket. Tek kaynak: `video/theme.ts`.

## Çalışma notları

- Tarayıcı: Remotion kendi Chrome'unu indirmez; `/opt/pw-browsers/` altındaki headless shell kullanılır (`REMOTION_BROWSER` ile değiştirilebilir).
- OpenAlex anahtarsız 429 dönebiliyor; `OPENALEX_API_KEY` yoksa bu kaynak uyarıyla atlanır.
- Gizli anahtarlar yalnızca `.env`'de (repoda değil). `episodes/*/audio` ve `*.mp4` git'e girmez.
- Remotion lisansı: bireyler ve ≤3 kişilik ekipler için ücretsiz.
- Kod içi açıklamalar ve kullanıcıya dönük tüm metinler Türkçe.
