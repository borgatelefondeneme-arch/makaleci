// zod şemalarını JSON Schema olarak dışa aktarır (Python tarafı ve dış araçlar için).
import { mkdirSync, writeFileSync } from "node:fs";
import { z } from "zod";
import * as S from "./index.ts";

mkdirSync("schemas/json", { recursive: true });
for (const name of ["Paper", "Selection", "Facts", "Script", "ScenePlan", "Voice"] as const) {
  writeFileSync(`schemas/json/${name}.schema.json`, JSON.stringify(z.toJSONSchema(S[name]), null, 2) + "\n");
  console.log(`schemas/json/${name}.schema.json`);
}
