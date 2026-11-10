// Claude API sağlayıcısı: şemaya bağlı (structured output) JSON üretir.
import Anthropic from "@anthropic-ai/sdk";
import { betaZodOutputFormat } from "@anthropic-ai/sdk/helpers/beta/zod";
import type { z } from "zod";
import { fail } from "../lib/io.ts";
import type { LlmRequest } from "./index.ts";

export const claudeJson = async <S extends z.ZodType>(req: LlmRequest<S>): Promise<z.infer<S>> => {
  const client = new Anthropic();
  const model = process.env.CLAUDE_MODEL || "claude-opus-5-5";
  console.log(`Claude API (${model}) · ${req.stage} ...`);
  try {
    const res = await client.beta.messages.parse({
      model,
      max_tokens: 16000,
      // Güvenlik sınıflandırıcısı reddederse istek sunucu tarafında yedek modelde yeniden çalışır.
      betas: ["server-side-fallback-2026-07-01"],
      fallbacks: "default",
      output_config: { effort: "high", format: betaZodOutputFormat(req.schema) },
      system: req.system,
      messages: [{ role: "user", content: req.prompt }],
    });
    if (res.stop_reason === "refusal") fail(`Claude isteği reddetti (${req.stage}): ${res.stop_details?.explanation ?? "açıklama yok"}`);
    if (res.stop_reason === "max_tokens") fail(`Claude çıktısı max_tokens sınırında kesildi (${req.stage}).`);
    if (res.parsed_output == null) fail(`Claude çıktısı şemaya göre ayrıştırılamadı (${req.stage}).`);
    return res.parsed_output as z.infer<S>;
  } catch (e) {
    if (e instanceof Anthropic.AuthenticationError) fail("ANTHROPIC_API_KEY geçersiz. Manuel mod için LLM_PROVIDER=manual kullanın.");
    if (e instanceof Anthropic.RateLimitError) fail("Claude API hız sınırı; biraz sonra yeniden deneyin.");
    if (e instanceof Anthropic.APIError) fail(`Claude API hatası ${e.status}: ${e.message}`);
    throw e;
  }
};
