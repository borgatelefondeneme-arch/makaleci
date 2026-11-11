"""Kullanıcının robot videosunu saydam zeminli kare dizisine çevirir.

  python3 tools/cutout_video.py <video> <png_klasörü> [--seq public/robot/seq --height 900]

Bel hizası kamera yakınlaştıkça değiştiği için birkaç anahtar karede elle ölçülüp aradeğerlenir.
Çıktı: tam çözünürlüklü PNG'ler (saydam video için) ve isteğe bağlı küçültülmüş WebP dizisi (Remotion için).
"""
import argparse
import glob
import os
import subprocess
import tempfile

import numpy as np
from PIL import Image

from cutout import cutout

# kare no → belin alt kenarı (px, 784×1168 karede)
WAIST = {1: 545, 25: 550, 49: 590, 97: 630, 145: 650, 193: 690, 217: 700, 233: 690, 265: 680, 313: 645, 361: 590}

ap = argparse.ArgumentParser()
ap.add_argument("video"); ap.add_argument("out")
ap.add_argument("--seq"); ap.add_argument("--height", type=int, default=900)
a = ap.parse_args()

tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a.video, "-vsync", "0", os.path.join(tmp, "%04d.png")], check=True)
frames = sorted(glob.glob(os.path.join(tmp, "*.png")))
os.makedirs(a.out, exist_ok=True)
if a.seq:
    os.makedirs(a.seq, exist_ok=True)
keys = sorted(WAIST)
for n, path in enumerate(frames, start=1):
    waist = float(np.interp(n, keys, [WAIST[k] for k in keys]))
    im = Image.open(path).convert("RGB")
    # İlk karelerde zemin gölgesi var: en alt şerit silinir.
    res = cutout(im, waist, thresh=10, floor=1090 if n < 170 else None)
    res.save(os.path.join(a.out, f"{n:04d}.png"))
    if a.seq:
        w, h = res.size
        res.resize((round(w * a.height / h), a.height), Image.LANCZOS).save(os.path.join(a.seq, f"{n:04d}.webp"), quality=84, method=4)
print(len(frames), "kare →", a.out, a.seq or "")
