# MuMa Library — proje kararları

Çocuklar için Türkçe, eğlenceli ve öğretici animasyonlu bilim videoları üreten hat (süre içeriğe göre 5–10 dakika). **Kanal adı: MuMa Library** (ekranda ve seslendirmede bu ad kullanılır). Bu dosya onaylanmış kararları tutar; bir karar değişirse önce burası güncellenir.

## İçerik yönü (güncel karar)

- **Ana içerik: konu bölümleri** (`kind: "topic"`). Çocukların gelişimini destekleyen ve merak ettikleri sorular ("Neden uyuruz?"). İzleyici 7–14 yaş; **anlatım düzeyi 10–12 yaşındaki bir çocuğa göre** ayarlanır (kullanıcı son olarak "12 yaş" dedi). Konuyu ve senaryoyu biz belirleriz.
- **Bilimsel dil (kullanıcı kararı):** senaryo okul öncesi gibi olmamalı. Gerçek terimler kullanılır ve hemen açıklanır ("ana saat" demekle yetinme: "suprakiazmatik çekirdek, kısaca SCN; hipotalamusta…"). Mekanizma anlatılır (ne, nerede, nasıl), benzetme terimin yerine değil yanına konur. Şarkı sözleri de aynı düzeyde ve senaryodaki bilimsel ifadelerden türetilir.
- **Süre içerikten türer:** süreye takılma; konu gerektiriyorsa video 10 dakikaya kadar çıkabilir (kapı 4:45–10:30).
- **Hareket kuralı (kullanıcı kararı):** hiçbir sahne "durağan kart + üstünden konuşma" olamaz; çocuk sıkılıp çıkar. Her cümlede ekranda bir şey değişir ve sahne boştayken de hareket eder. Bunun için: (1) sahne en çok 3 cümle sürer, uzun anlatım birkaç sahneye bölünür; (2) hareketli tipler tercih edilir — `clock` (dönen gün-gece kadranı), `spotlight` (ortada simge, çevresinde beliren etiketler), `stages` (sahne boyunca çizilen evre çizgisi), `meter` (dolup boşalan depo), akan noktalı `diagram`; (3) her sahneye konuyla ilgili `stickers` (kenarda süzülen, cümle başında zıplayan simgeler) ve satır başına `keywords` (büyük beliren anahtar kelime) verilir; (4) kamera sahne boyunca yavaşça yaklaşır, geçişler sahneden sahneye değişir. Şematik çizimler "Şematik çizim" notu taşır ve kaynakta olmayan sayı göstermez.
- **Bölümler birbirinin kopyası gibi durmamalı (kullanıcı kararı).** Sabit kalanlar: giriş/çıkış, köşede gezen Muma kafası, senaryo modeli ve sonda şarkı olması. Geri kalanı bölümden bölüme değişir ve `video/look.ts` içindeki `lookOf(bölüm no)` ile belirlenir: arka plan deseni (lekeler, dalgalar, nokta ızgarası, ışınlar, balonlar) ve pastel tonu, arka planda süzülen konu simgeleri, sahne giriş hareketleri, anahtar kelime etiketi (üç stil), şarkı sahnesinin düzeni (sıra, yörünge, bölünmüş sahne, dalga bandı), kafanın köşe sırası. Yeni desen/düzen eklemek serbesttir; koyu zemin yine yoktur. Görünüm değişiklikleri yalnızca **bundan sonraki** bölümlere uygulanır; teslim edilmiş videolar kullanıcı istemeden yeniden üretilmez.
- **Görseller konuya göre kurulur (kullanıcı kararı; yalnızca yeni bölümler).** Her bölümün senaryosunda `theme` yazılır: konunun geçtiği dünya (`backdrop`: `space` gökyüzü/uzay, `underground` yer altı katmanları, `meadow` çayır, `ocean` deniz altı, `storm` fırtına, `mouth` ağız içi, `aurora` kutup gecesi ve kuzey ışıkları, `sky` bulutların üstü, `micro` mikroskop görüntüsü) ve ortamda gezen karakterler (`actors`: yürür, uçar, kovalar, yüzer, kazar, zıplar, döner, sürü). Sahnelere konuya özel efekt verilir (`fx`: `blackhole` sahneyi içine çeker, `shake` sarsıntı, `flash` şimşek, `meteor`, `dig` kazı, `erupt` püskürme, `rain`, `sparkle`). Şarkıda rozet sırası yerine `song.show` ile konunun karakterleri oynar (ör. büyük dinozor küçüğü kovalar, pterozor uçar). Koyu dünyalarda (uzay, okyanus, fırtına) yazılar krem bir panonun üstünde durur; "koyu zemin yok" kararı yalnızca temasız bölümler için geçerlidir. Bileşenler: `video/components/Themed.tsx`. Konuya uyan dünya/efekt yoksa yenisi yazılır.
- **Şakalar hep aynı yerde olmaz (kullanıcı kararı).** "Açılıştan hemen sonra + soru sonrası + vedada" kalıbı kullanılmaz; şakalar her bölümde farklı sahnelere dağıtılır, bazı bölümlerde veda şakasız biter.
- **Kaynaklar cümle içinde anılır** ("NIH'ye göre…", "CDC'ye göre…", "KidsHealth'e göre…"). Kaynak bölümü/kartı ve ekrandaki "Kaynak:" etiketi **yoktur** (kullanıcı kararı); tam kaynak listesi yalnızca `yayin.md`'de durur.
- Akış: merak uyandıran açılış → günün soruları → "Nasıl oluyor?" → "İşin sırrı" → **"Sen de dene"** (güvenli bir gözlem/deney) → "Bunu biliyor muydun?" + kısa tekrar sorusu → şarkı → "Bugün bunu öğrendik".
- Bilgiler güvenilir kaynaklardan alınır; kaynak sayfası **gerçekten okunur**, alıntısı `03_facts.json`'a yazılır. Kaynakta bulunamayan bilgi/sayı senaryoya girmez — kullanıcının verdiği bilgi de okunan bir kaynakta doğrulanamazsa kullanılmaz ve kullanıcıya söylenir (ör. "SCN ~20.000 nöron" doğrulanamadı; "binlerce" denildi).
- **Minik komiklikler:** bölüm başına 4–6 küçük şaka (robotun kendisiyle dalga geçmesi: uyumaz şarj olur, kapatma düğmesi yoktur; kelime oyunları). Şaka bilgi gibi sunulmaz, olguyu çarpıtmaz, kimseyle alay etmez.
- **Sabit açılış ve kapanış:** açılış cümlesi "MuMa Library'ye hoş geldin! Merhaba, ben Muma!", kapanış cümlesi "Bir sonraki bilim videosunda görüşürüz! Hoşça kal!". İkisi de voice aşamasında otomatik eklenir (`pipeline/voice/cli.ts` içinde `WELCOME`/`GOODBYE`), senaryoya yazılmaz.
- **Telaffuz:** "MuMa Library" seslendirmede okunduğu gibi "Muma Laybrıri" denir (kullanıcı onayı).
- **Kapanış şarkısı:** videonun son ~1 dakikasında konuyu özetleyen neşeli, marş/çizgi film havasında bir şarkı. Müzik **ElevenLabs Music** ile üretilir (Suno değil; ticari risk nedeniyle kullanıcı kararı). Sözleri biz yazarız (yalnızca `03_facts.json`'daki bilgilerle; rakam yok; **sözlerde şarkının adı geçmez**), API'ye `composition_plan` ile veririz; tarz tarifinde sanatçı, şarkı ya da eser adı geçmez. Toplam süre ~5 dk kalır: anlatım ~4 dk + şarkı ~1 dk.
- **Şarkıda özgün vokal kullanılır** (kullanıcı kararı). Vokali Muma'nın sesine dönüştürme denendi ve beğenilmedi; `npm run song -- <dir> --convert` ile deneysel olarak hâlâ yapılabilir (ek kota harcar).
- **Muma'nın tam gövdesi yalnızca girişte ve çıkışta görünür** (kullanıcı kararı). Açılışta uçarak gelir, "MuMa Library'ye hoş geldin! Merhaba, ben Muma!" der ve gider; kapanış sahnesinde geri gelir, vedalaşıp uçar. **Anlatım sahnelerinde yalnızca Muma'nın kafası** köşede durur ve sahneden sahneye yer değiştirir (çoğunlukla sağ alt, bazen sol üst ya da sağ üst; kullanıcı kararı). Ağzı sese göre oynar; `HeadLayer`/`cornerOf` (`video/mascot/MascotLayer.tsx`), görsel `public/robot/head.png`. Şarkıda Muma ekranda değildir. Senaryoda yeniden selamlama/kendini tanıtma olmaz; hook doğrudan konuyla başlar.
- **Şarkı sahnesi klip havasındadır, okul öncesi gibi görünmemelidir** (kullanıcı geri bildirimi: kollu bacaklı emoji figürleri fazla çocuksu bulundu). Konuya özel karakterler (`song.cast`) rozet olarak vuruşla zıplar; sözler kelime kelime yanar.
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
- **Ses tonu (kullanıcı kararı): bağırmayan, biraz yavaş anlatım.** `voice_settings`: stability 0.7, style 0 (`pipeline/voice/providers/elevenlabs.ts`). `eleven_v4` "speed" ayarını uygulamıyor (ölçüldü); bu yüzden anlatım sentezden sonra perdesi korunarak yavaşlatılır (`VOICE_TEMPO`, varsayılan 0.93).
- **Muma'nın sesi (ElevenLabs):** kullanıcının seçtiği tasarım sesi hesaba "Muma" adıyla kaydedildi, kimliği `j6hEdvUHjDuCExVlNXTi` (`ELEVENLABS_VOICE_ID` verilmezse varsayılan budur). Her videoda aynı ses kullanılır. ElevenLabs çocuk sesi üretimini engeller; ses, yetişkin seslendirmecinin canlandırdığı parlak, heyecanlı bir çizgi film robotu olarak tarif edildi. Anahtar ortamın ağ gizlisi olarak saklı (kod içinde `ELEVENLABS_API_KEY=proxy-injected` yer tutucusu yeterli).
- **Piper sesi yalnızca taslak içindir:** eğitim verisi CC BY-NC-SA 4.0 (ticari kullanım dışı). Gelir getiren yayında ElevenLabs ya da ticari kullanıma açık bir ses kullanılır.
- Font: Manrope (sitenin yazı tipi), `@fontsource` paketinden gömülü; render sırasında ağ gerekmez.

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
- Süre: içerikten türer (kapı 4:45–10:30). Sahne süresi sesten türetilir (ses + nefes payı); sahne içi vuruşlar satır başlangıç karelerine bağlanır.
- Mascot ağzı: voice aşaması kare başına genlik zarfı üretir (mock'ta kelime damgalarından sentezlenir), render aynı kodu kullanır.
- Render sessiz yapılır, ses FFmpeg ile eklenir (gerçek seste `loudnorm`).

## Video yapısı

- Açılış (~5 sn): robot uçarak gelir + "MuMa Library" logosu + "Hoş geldin!" + "Günün Sorusu #n" (makale bölümünde "Günün Makalesi #n") + başlık (+ preprint rozeti).
- Sahne tipleri: `hook`, `source-card`, `big-number`, `bar-chart`, `line-chart`, `comparison`, `diagram`, `analogy` (şablonlar: `scale`, `fill`, `race`, `zoom`), `quote-card`, `bullets`, `clock`, `spotlight`, `stages`, `meter`, `song`, `outro`. Aynı tip art arda gelmez.
- **Karakter her zaman kullanıcının verdiği robottur** (cin kuyruklu, yay antenli, göğsünde "M" amblemi). Başka karakter kullanılmaz. Görseller `public/robot/` altında, `tools/cutout.py` ile saydam zeminli kesildi. Pozlar: `point` (parmak havada + açık el; yüksek çözünürlüklü özgün görselden), `crossed` (kollar kavuşuk), `book` (kitap okur), `thumbs` (başparmak), `wave` (el sallar), `fly` (kollar açık; yalnızca uçarken). Poz, sahnede `mascot.pose` ile seçilir; verilmezse durumdan türetilir (`talk`/`point` → `point`, `idle`/`think` → `crossed` + düşünce baloncuğu) ve sahne tipine göre otomatik atanır: açılış ve veda `wave`, kaynak kartı `book`, kapanış `thumbs`. **Ağız sese göre oynar** (kullanıcı bunu özellikle beğendi; korunur): açıklık ses genliğinden, biçim o an söylenen kelimenin ünlüsünden gelir (a/e açık, ı/i yayvan ve dişli, o/ö/u/ü yuvarlak, m/b/p kapalı), Özgün ağız poz görsellerinden silinmiştir (`tools/mouthless.py` → `*.nomouth.png`) ve ağız her zaman yeniden çizilir; görselin üstüne yama konmaz (iz bırakıyordu). Anten yıldızı parlar, kuyruk salınır, sahneler arasında konum/ölçek yumuşak geçer; açılışta uçarak gelir, kapanışta uçarak gider (`MascotLayer.tsx`). Kollar yeniden çizilmez.
- Videodan kare dizisiyle oynatma denendi ve geri alındı: kesim kalitesi düşüktü ve dudak eşlemesi kayboluyordu. Kullanıcı yeni klipler verirse `tools/cutout_video.py` ile işlenir; iyi sonuç için yüksek çözünürlük, düz tek renk zemin (gölgesiz), sabit kamera gerekir. **Karakterin adı: Muma.** Kendini "Ben Muma!" diye tanıtır.
- **YouTube kapağı** (`out/thumbnail.png`, 1280×720): konu bölümlerinde "Günün Sorusu" rozeti yoktur; başlık büyük yazılır ve kapağı doldurur (kullanıcı kararı). Açılış sahnesindeki rozet durur. Sağ alt köşede "MumaApp" yazar, altında yazısız Android ve iOS simgeleri durur (videoları MumaApp hazırlar; kullanıcı kararı; "MumaApp sunar" ifadesi beğenilmedi).
- Abone ol: sürenin ~%60'ına en yakın sahne sınırında kısa alt bant; kapanışta tam kart.
- Kapanış: "Bugün bunu öğrendik" + 3 madde sırayla ✓ + "Bir sonraki bilim videosunda görüşürüz!" + abone ol + sonraki video; robot uçarak gider.
- Stil: **açık ve sıcak** — kullanıcının sitesindeki (mumaapp-panel.web.app/tanitim) tonlar: krem zemin `#FBF8F3`, lacivert yazı `#1B2238`, kiremit→turuncu→mavi geçişli vurgu, beyaz kartlar, **Manrope** yazı tipi. Koyu zemin kullanılmaz (kullanıcı kararı). Arka planda pastel lekeler ve süzülen şekillerle hafif hareket. Tek kaynak: `video/theme.ts`.

## Çalışma notları

- Seri üretim: anahtar yokken her bölümün `manual/build.py` dosyası ortak `tools/manual_build.py` yardımcılarını kullanır (olgu/satır/sahne kurucuları, şarkı kalıbı). Örnek: `episodes/2026-11-11-fosil-nedir/manual/build.py` (eski, tek dosya) ve sonraki bölümler.

- Tarayıcı: Remotion kendi Chrome'unu indirmez; `/opt/pw-browsers/` altındaki headless shell kullanılır (`REMOTION_BROWSER` ile değiştirilebilir).
- OpenAlex anahtarsız 429 dönebiliyor; `OPENALEX_API_KEY` yoksa bu kaynak uyarıyla atlanır.
- Gizli anahtarlar yalnızca `.env`'de (repoda değil). `episodes/*/audio` ve `*.mp4` git'e girmez.
- Remotion lisansı: bireyler ve ≤3 kişilik ekipler için ücretsiz.
- Kod içi açıklamalar ve kullanıcıya dönük tüm metinler Türkçe.
