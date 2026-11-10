"""Açık zeminli karakter görselinden saydam PNG üretir (kullanıcının verdiği robot görselleri için).

  python3 tools/cutout.py <girdi> <çıktı.png> --waist <y> [--crop x0,y0,x1,y1]

Gövde (bel çizgisinin üstü) opak kesilir; duman kuyruğu (altı) "renkten saydamlığa" yöntemiyle
yumuşak kenarlı alınır, böylece koyu zeminde beyaz hale kalmaz.
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--waist", type=int, required=True, help="belin y koordinatı (kırpmadan sonra)")
ap.add_argument("--crop"); ap.add_argument("--thresh", type=int, default=14)
ap.add_argument("--floor", type=int, help="bu y'nin altı tamamen silinir (zemin gölgesi)")
a = ap.parse_args()

im = Image.open(a.src).convert("RGB")
if a.crop:
    im = im.crop(tuple(int(v) for v in a.crop.split(",")))
w, h = im.size
px = np.asarray(im).astype(np.float32)
border = np.concatenate([px[:6].reshape(-1, 3), px[:, :6].reshape(-1, 3), px[:, -6:].reshape(-1, 3)])
bg = np.median(border, axis=0)

# 1) Kenarlardan taşırma: zemine bağlı açık pikseller
dist_img = Image.fromarray(np.clip(np.abs(px - bg).max(axis=2), 0, 255).astype(np.uint8))
flood = dist_img.point(lambda v: 0 if v < a.thresh else 255).convert("L")
for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (0, h // 2), (w - 1, h // 2), (w // 2, h - 1)]:
    if flood.getpixel(seed) == 0:
        ImageDraw.floodfill(flood, seed, 128)
hard = (np.asarray(flood) != 128).astype(np.float32)  # 1 = karakter
hard = np.asarray(Image.fromarray((hard * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))).astype(np.float32) / 255
hard = np.clip((hard - 0.35) / 0.5, 0, 1)

# 2) Yumuşak alfa: zeminden uzaklık (duman için)
dist = np.abs(px - bg).max(axis=2)
soft = np.clip((dist - 5) / 55, 0, 1)

# 3) Belin üstünde sert, altında yumuşak; arada 70 px geçiş
yy = np.arange(h, dtype=np.float32)[:, None]
k = np.clip((yy - a.waist) / 70, 0, 1)
alpha = hard * (1 - k) + np.minimum(hard, soft) * k
if a.floor:
    alpha *= np.clip((a.floor - yy) / 30, 0, 1)

# 4) Kenar renklerinden zemin payını çıkar (hale kalmasın)
al = np.clip(alpha, 1e-3, 1)[..., None]
rgb = np.clip((px - (1 - al) * bg) / al, 0, 255)
out = np.dstack([rgb, alpha * 255]).astype(np.uint8)
res = Image.fromarray(out, "RGBA")
bbox = res.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
res = res.crop(bbox)
res.save(a.dst)
print(a.dst, res.size, "bbox", bbox)
