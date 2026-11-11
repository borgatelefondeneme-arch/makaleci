"""Açık zeminli karakter görselinden saydam PNG üretir (kullanıcının verdiği robot görselleri için).

  python3 tools/cutout.py <girdi> <çıktı.png> --waist <y> [--crop x0,y0,x1,y1] [--floor y]

Gövde (bel çizgisinin üstü) opak kesilir; duman kuyruğu (altı) "renkten saydamlığa" yöntemiyle
yumuşak kenarlı alınır, böylece koyu zeminde beyaz hale kalmaz.
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def cutout(im, waist, thresh=14, floor=None):
    """RGB görsel → RGBA (aynı boyut). waist: belin y koordinatı."""
    w, h = im.size
    px = np.asarray(im.convert("RGB")).astype(np.float32)
    # Zemin düz olmayabilir (videoda yukarıdan aşağı ton değişir): her satırın zemin rengi,
    # sol ve sağ kenar şeritlerinden alınır ve dikeyde yumuşatılır.
    edge = np.concatenate([px[:, :8], px[:, -8:]], axis=1)  # (h, 16, 3)
    row = np.median(edge, axis=1)
    glob = np.median(row, axis=0)
    row = np.where(np.abs(row - glob).max(axis=1, keepdims=True) > 22, glob, row)  # kenara değen kol/el satırları
    pad = np.pad(row, ((20, 20), (0, 0)), mode="edge")
    row = np.stack([np.median(pad[i:i + 41], axis=0) for i in range(h)])
    bg = row[:, None, :]
    dist = np.abs(px - bg).max(axis=2)

    # 1) Kenarlardan taşırma: zemine bağlı açık pikseller
    flood = Image.fromarray(np.where(dist < thresh, 0, 255).astype(np.uint8), "L").copy()  # fromarray salt-okunur bellek paylaşır; taşırma için kopya şart
    # Tohumlar kenardan birkaç piksel içeride ve sık: video karelerinde en dış piksel sırası bozuk olabilir.
    m = 6
    seeds = [(x, y) for x in range(m, w - m, 24) for y in (m, h - 1 - m)] + [(x, y) for x in (m, w - 1 - m) for y in range(m, h - m, 24)]
    for seed in seeds:
        if flood.getpixel(seed) == 0:
            ImageDraw.floodfill(flood, seed, 128)
    hard = (np.asarray(flood) != 128).astype(np.float32)  # 1 = karakter
    hard = np.asarray(Image.fromarray((hard * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))).astype(np.float32) / 255
    hard = np.clip((hard - 0.35) / 0.5, 0, 1)

    # 2) Yumuşak alfa: zeminden uzaklık (duman için)
    soft = np.clip((dist - 5) / 55, 0, 1)

    # 3) Belin üstünde sert, altında yumuşak; arada 70 px geçiş
    yy = np.arange(h, dtype=np.float32)[:, None]
    k = np.clip((yy - waist) / 70, 0, 1)
    alpha = hard * (1 - k) + np.minimum(hard, soft) * k
    if floor:
        alpha = alpha * np.clip((floor - yy) / 30, 0, 1)

    # 4) Kenar renklerinden zemin payını çıkar (hale kalmasın)
    al = np.clip(alpha, 1e-3, 1)[..., None]
    rgb = np.clip((px - (1 - al) * bg) / al, 0, 255)
    return Image.fromarray(np.dstack([rgb, alpha * 255]).astype(np.uint8), "RGBA")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--waist", type=int, required=True, help="belin y koordinatı (kırpmadan sonra)")
    ap.add_argument("--crop"); ap.add_argument("--thresh", type=int, default=14)
    ap.add_argument("--floor", type=int, help="bu y'nin altı tamamen silinir (zemin gölgesi)")
    a = ap.parse_args()
    im = Image.open(a.src).convert("RGB")
    if a.crop:
        im = im.crop(tuple(int(v) for v in a.crop.split(",")))
    res = cutout(im, a.waist, a.thresh, a.floor)
    bbox = res.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    res.crop(bbox).save(a.dst)
    print(a.dst, res.crop(bbox).size, "bbox", bbox)
