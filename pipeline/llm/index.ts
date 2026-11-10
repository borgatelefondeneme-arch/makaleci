// LLM ortak arayüzü. Kimlik bilgisi varsa Claude API, yoksa manuel sağlayıcı (hibrit karar).
import type { z } from "zod";
import { claudeJson } from "./claude.ts";
import { manualJson } from "./manual.ts";

export type LlmRequest<S extends z.ZodType> = {
  stage: string; // dosya adı için: "facts", "script", "scenes", "select"
  manualDir: string; // manuel modda istem/yanıt dosyalarının yeri
  system: string;
  prompt: string;
  schema: S;
};

export const hasClaude = () => Boolean(process.env.ANTHROPIC_API_KEY || process.env.ANTHROPIC_AUTH_TOKEN);

export const generateJson = async <S extends z.ZodType>(req: LlmRequest<S>): Promise<z.infer<S>> => {
  if (process.env.LLM_PROVIDER !== "manual" && hasClaude()) return claudeJson(req);
  return manualJson(req);
};
