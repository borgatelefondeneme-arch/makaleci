// Manuel sağlayıcı: API anahtarı yokken aynı sözleşmeyle çalışır.
// İstemi <manualDir>/<aşama>.prompt.md'ye yazar; yanıtı <manualDir>/<aşama>.json'dan okur.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { z } from "zod";
import { fail, fmtIssues } from "../lib/io.ts";
import type { LlmRequest } from "./index.ts";

export const manualJson = async <S extends z.ZodType>(req: LlmRequest<S>): Promise<z.infer<S>> => {
  mkdirSync(req.manualDir, { recursive: true });
  const promptPath = join(req.manualDir, `${req.stage}.prompt.md`);
  const answerPath = join(req.manualDir, `${req.stage}.json`);
  writeFileSync(promptPath, `# SİSTEM\n\n${req.system}\n\n# İSTEM\n\n${req.prompt}\n\n# ÇIKTI ŞEMASI (JSON Schema)\n\n\`\`\`json\n${JSON.stringify(z.toJSONSchema(req.schema), null, 2)}\n\`\`\`\n`);
  if (!existsSync(answerPath)) {
    fail(`Claude API kimlik bilgisi yok → manuel mod.\n  İstem:  ${promptPath}\n  Yanıtı şu dosyaya JSON olarak yazıp komutu yeniden çalıştırın: ${answerPath}`);
  }
  const r = req.schema.safeParse(JSON.parse(readFileSync(answerPath, "utf8")));
  if (!r.success) fail(`${answerPath} şemaya uymuyor:\n${fmtIssues(r.error)}`);
  console.log(`manuel yanıt okundu: ${answerPath}`);
  return r.data as z.infer<S>;
};
