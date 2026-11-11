#!/bin/bash
# Kontrol karelerini tek sayfada toplar, ardından tam videoyu render eder. Kullanım: tools/check_and_render.sh <episodeDir>
set -e
E="$1"; rm -rf "$E/out/fq"
N=$(python3 -c "import json;print(json.load(open('$E/05_voice.json'))['totalFrames'])" 2>/dev/null || echo 12000)
AT=$(python3 -c "n=$N;print(','.join(str(int(n*x)) for x in (0.06,0.14,0.22,0.3,0.38,0.46,0.54,0.62,0.7,0.76,0.9,0.985)))")
npx tsx pipeline/render/frames.ts "$E" --at "$AT" --dir fq --scale 0.34 >/dev/null 2>&1
python3 - "$E/out/fq" <<'PY'
import sys, glob
from PIL import Image
d = sys.argv[1]; fs = sorted(glob.glob(d + "/*.jpg")); im = [Image.open(f) for f in fs]; w, h = im[0].size
s = Image.new("RGB", (w * 3, h * 4))
for i, x in enumerate(im): s.paste(x, ((i % 3) * w, (i // 3) * h))
s.save(d + "/../check.jpg", quality=82)
PY
echo "kareler hazır"
NODE_USE_ENV_PROXY=1 npx tsx pipeline/render/cli.ts "$E" 2>&1 | grep "✓\|✗\|Error" | tail -5
rm -rf "$E/out/fq"
