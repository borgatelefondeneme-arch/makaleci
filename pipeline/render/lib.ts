// render yardımcıları: props birleştirme, Remotion paketi, tarayıcı seçimi.
import { bundle } from "@remotion/bundler";
import { existsSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { EpisodeProps, Facts, Paper, ScenePlan, Script, Voice } from "../../schemas/index.ts";
import { P, readJson } from "../lib/io.ts";

export const loadProps = (dir: string): EpisodeProps => {
  const p = P(dir);
  const paper = readJson(p.paper, Paper);
  const facts = readJson(p.facts, Facts);
  // API'ler kurum vermediyse makale metninden çıkarılanlar kullanılır.
  if (!paper.institutions.length) paper.institutions = facts.institutions;
  const props = { paper, script: readJson(p.script, Script), plan: readJson(p.scenes, ScenePlan), voice: readJson(p.voice, Voice), sources: facts.sources };
  return EpisodeProps.parse(props);
};

// Remotion kendi Chrome'unu indirmesin: önce REMOTION_BROWSER, sonra ortamdaki headless shell.
export const browserExecutable = (): string | undefined => {
  if (process.env.REMOTION_BROWSER) return process.env.REMOTION_BROWSER;
  const root = "/opt/pw-browsers";
  if (!existsSync(root)) return undefined;
  for (const d of readdirSync(root).filter((x) => x.startsWith("chromium_headless_shell")).sort().reverse()) {
    for (const sub of readdirSync(join(root, d))) {
      const exe = join(root, d, sub, "chrome-headless-shell");
      if (existsSync(exe)) return exe;
    }
  }
  return undefined;
};

export const browserOpts = () => ({ browserExecutable: browserExecutable(), chromeMode: "headless-shell" as const, logLevel: "error" as const });

export const makeBundle = async () => {
  process.stdout.write("Remotion paketi hazırlanıyor ... ");
  const serveUrl = await bundle({ entryPoint: resolve("video/index.ts"), outDir: resolve(".remotion-bundle") });
  console.log("tamam");
  return serveUrl;
};
