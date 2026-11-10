// sceneplan aşaması: 03_script.json → 04_scenes.json
import { z } from "zod";
import { Facts, Scene, ScenePlan, Script } from "../../schemas/index.ts";
import { episodeDirArg, fail, loadEnv, P, readJson, writeJson } from "../lib/io.ts";
import { generateJson } from "../llm/index.ts";
import { printReport } from "../script/validate.ts";
import { SCENES_SYSTEM, scenesPrompt } from "./prompts.ts";
import { validatePlan } from "./validate.ts";

loadEnv();
const { dir } = episodeDirArg();
const p = P(dir);
const script = readJson(p.script, Script);
const facts = readJson(p.facts, Facts);
const out = await generateJson({ stage: "scenes", manualDir: p.manual, system: SCENES_SYSTEM, prompt: scenesPrompt(script, facts), schema: z.object({ scenes: z.array(Scene) }) });
const plan: ScenePlan = { paperId: script.paperId, scenes: out.scenes };
const report = validatePlan(plan, script, facts);
printReport("Sahne planı denetimi", report);
if (report.errors.length) fail("Sahne planı denetimden geçemedi.");
writeJson(p.scenes, ScenePlan, plan);
