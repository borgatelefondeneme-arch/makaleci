"""Poz görsellerindeki özgün ağzı siler (çevredeki yüz renginden doldurur) → <poz>.nomouth.png

Ağız render sırasında yeniden çizildiği için özgün gülüşün üstüne yama koymak iz bırakıyordu.
Burada ağız bölgesi, her satırda sol ve sağ kenardaki yüz rengi arasında doğrusal geçişle doldurulur.

  python3 tools/mouthless.py
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# poz: (merkez x, merkez y, yarı genişlik, yarı yükseklik, eğim°)
MOUTHS = {
    "point": (366, 351, 52, 26, 0),
    "crossed": (254, 181, 42, 19, -7),
    "thumbs": (212, 179, 18, 18, 0),
    "book": (206, 243, 26, 17, 0),
    "wave": (230, 205, 44, 26, 0),
}
for name, (cx, cy, rx, ry, rot) in MOUTHS.items():
    im = Image.open(f"public/robot/{name}.png").convert("RGBA")
    px = np.asarray(im).astype(np.float32)
    h, w = px.shape[:2]
    mask_img = Image.new("L", (w, h), 0)
    box = Image.new("L", (rx * 2 + 1, ry * 2 + 1), 0)
    ImageDraw.Draw(box).ellipse([0, 0, rx * 2, ry * 2], fill=255)
    box = box.rotate(-rot, expand=True, resample=Image.BICUBIC)
    mask_img.paste(box, (cx - box.width // 2, cy - box.height // 2))
    hard = np.asarray(mask_img) > 127
    fill = px.copy()
    for y in np.unique(np.nonzero(hard)[0]):
        xs = np.nonzero(hard[y])[0]
        x0, x1 = xs.min() - 4, xs.max() + 4
        a, b = px[y, x0 - 3:x0 + 1, :3].mean(axis=0), px[y, x1:x1 + 4, :3].mean(axis=0)
        t = np.linspace(0, 1, x1 - x0 + 1)[:, None]
        fill[y, x0:x1 + 1, :3] = a * (1 - t) + b * t
    # dolguyu yumuşat ve kenarı tüylendirerek özgün görüntüye karıştır
    soft = np.asarray(Image.fromarray(fill[..., :3].astype(np.uint8)).filter(ImageFilter.GaussianBlur(2.2))).astype(np.float32)
    m = np.asarray(mask_img.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32)[..., None] / 255
    out = px.copy()
    out[..., :3] = px[..., :3] * (1 - m) + soft * m
    Image.fromarray(out.astype(np.uint8), "RGBA").save(f"public/robot/{name}.nomouth.png")
    print(name, "→", f"public/robot/{name}.nomouth.png")
