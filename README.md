# Günün Bilimi

Bilimsel makaleleri 12 yaş seviyesinde Türkçe anlatan 5-6 dakikalık animasyonlu videolara çeviren üretim hattı.
Kararlar ve kurallar: [CLAUDE.md](CLAUDE.md).

```bash
npm install
cp .env.example .env                       # anahtarlar isteğe bağlı; yoksa manuel LLM + mock ses
npm run episode -- --url <makale linki>    # fetch → script → sceneplan → voice → render
npm run frames  -- episodes/<id>           # örnek kareler (out/frames/)
npm run studio                             # Remotion stüdyosu (örnek veriyle)
```

Günlük akış: `npm run fetch -- --recent 48 --out data/pool/<tarih>.json` → `npm run select -- data/pool/<tarih>.json` → `npm run queue -- list` / `approve <id>` → `npm run episode -- --episode episodes/<id>`.

Claude API anahtarı yokken script ve sceneplan aşamaları istemi `episodes/<id>/manual/<aşama>.prompt.md` dosyasına yazar ve yanıtı `manual/<aşama>.json` dosyasından bekler.

`episodes/_demo` uydurma veriyle tüm sahne tiplerini dener (`npx tsx episodes/_demo/make.ts`); gerçek bir makale değildir.
