# Günün Bilimi — proje kararları

Çocuklar için Türkçe, eğlenceli ve öğretici 5 dakikalık animasyonlu bilim videoları üreten hat. Bu dosya onaylanmış kararları tutar; bir karar değişirse önce burası güncellenir.

## İçerik yönü (güncel karar)

- **Ana içerik: konu bölümleri** (`kind: "topic"`). Çocukların gelişimini destekleyen ve merak ettikleri sorular ("Gökyüzü neden mavi?"). Hedef yaş 7–12, süre ~5 dk. Konuyu ve senaryoyu biz belirleriz.
- Her konu bölümünde: merak uyandıran açılış → günün sorusu ve kaynaklar → "Nasıl oluyor?" → "İşin sırrı" → **"Sen de dene"** (güvenli bir gözlem/etkinlik) → "Bunu biliyor muydun?" + kısa tekrar sorusu → "Bugün bunu öğrendik".
- Bilgiler güvenilir kurum kaynaklarından (NASA vb.) alınır; kaynak sayfası **gerçekten okunur**, alıntısı `03_facts.json`'a yazılır. Kaynakta bulunamayan bilgi/sayı senaryoya girmez.
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
- Ses önceliği: ElevenLabs (`ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_ID`) → **Piper** (yerel, `tools/setup-piper.sh`, ses `tr_TR-dfki-medium`, hız `PIPER_LENGTH_SCALE` varsayılan 1.1) → **mock** (sessiz). Piper kelime hizalaması vermez: satır satır sentezlenir, kelime damgaları hece oranıyla dağıtılır.
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
| 5 | voice | `npm run voice -- <episodeDir>` | `audio/`, `05_voice.json` |
| 6 | render | `npm run render -- <episodeDir>` | `out/video.mp4`, `out/thumbnail.png`, `out/yayin.md` |

Uçtan uca: konu bölümü `npm run episode -- --topic "<soru>"` (fetch/select atlanır), makale bölümü `npm run episode -- --url <link>`. Aşamalar çıktısı varsa atlanır; `--force` yeniden üretir, `--from <aşama>` o aşamadan başlatır.

- Bölüm kimliği: `<YYYY-AA-GG>-<slug>`; bölüm numarası (#n) `data/state.json` sayacından.
- Senaryo satırlarında iki metin: `display` (ekran) ve `spoken` (seslendirme; sayılar, yabancı adlar, DOI Türkçe okunuşla).
- Süre: konu bölümlerinde hedef ~5:00 (kapı 4:45–6:00). Sahne süresi sesten türetilir (ses + nefes payı); sahne içi vuruşlar satır başlangıç karelerine bağlanır.
- Mascot ağzı: voice aşaması kare başına genlik zarfı üretir (mock'ta kelime damgalarından sentezlenir), render aynı kodu kullanır.
- Render sessiz yapılır, ses FFmpeg ile eklenir (gerçek seste `loudnorm`).

## Video yapısı

- Açılış 5 sn: logo + "Günün Sorusu #n" (makale bölümünde "Günün Makalesi #n") + başlık (+ preprint rozeti).
- Sahne tipleri: `hook`, `source-card`, `big-number`, `bar-chart`, `line-chart`, `comparison`, `diagram`, `analogy` (şablonlar: `scale`, `fill`, `race`, `zoom`), `quote-card`, `bullets`, `outro`. Aynı tip art arda gelmez.
- **Karakter her zaman kullanıcının verdiği robottur** (cin kuyruklu, yay antenli, göğsünde "M" amblemi). Başka karakter kullanılmaz. Görseller `public/robot/` altında; kullanıcının görsel ve videosundan `tools/cutout.py` ile saydam zeminli kesildi. İki poz var: `point` (parmak havada + açık el) ve `crossed` (kollar kavuşuk). Durum → poz: `talk`/`point` → `point`, `idle`/`think` → `crossed` (+ düşünce baloncuğu). Kollar yeniden çizilmez; canlılık süzülme, kuyruk salınımı, sese göre ağız, anten yıldızı ve poz geçişleriyle sağlanır. Bölüm düzeyinde çizilir, sahneler arasında konum/ölçek yumuşak geçer. Karakterin adı henüz belirlenmedi.
- Abone ol: sürenin ~%60'ına en yakın sahne sınırında kısa alt bant; kapanışta tam kart.
- Kapanış: "Bugün bunu öğrendik" + 3 madde sırayla ✓ + abone ol + sonraki video.
- Stil: koyu lacivert zemin, 4 vurgu rengi (turkuaz, sarı, mercan, mor), yumuşak geçişler, arka planda hafif hareket. Tek kaynak: `video/theme.ts`.

## Çalışma notları

- Tarayıcı: Remotion kendi Chrome'unu indirmez; `/opt/pw-browsers/` altındaki headless shell kullanılır (`REMOTION_BROWSER` ile değiştirilebilir).
- OpenAlex anahtarsız 429 dönebiliyor; `OPENALEX_API_KEY` yoksa bu kaynak uyarıyla atlanır.
- Gizli anahtarlar yalnızca `.env`'de (repoda değil). `episodes/*/audio` ve `*.mp4` git'e girmez.
- Remotion lisansı: bireyler ve ≤3 kişilik ekipler için ücretsiz.
- Kod içi açıklamalar ve kullanıcıya dönük tüm metinler Türkçe.
