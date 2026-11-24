"""Bölüm videolarından dikey (1080×1920) kısa videolar üretir. Ses ve görüntü, bölümün kendi videosundan birebir kesilir.

Kullanım: python3 tools/make_shorts.py <episodeDir> <spec.json>
spec.json: [{"name": "kanca", "first": "<ilk satırın başı>", "last": "<son satırın başı>", "headline": "Üst başlık"},
            {"name": "sarki", "song": true, "headline": "♪ Şarkı adı"}]
Çıktı: <episodeDir>/out/shorts/<n>-<name>.mp4 (ve aynı adla .jpg kapak)
"""
import json, os, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
VW, VH = 1080, 608  # ortadaki yatay video
VY = 640            # ortadaki videonun üst kenarı
FD = "node_modules/@fontsource/manrope/files/manrope-{sub}-{w}-normal.woff"
# Manrope web paketi alt kümelere bölünmüştür: ç, ö, ü "latin"de; ğ, ı, ş, İ "latin-ext"te. Harf harf doğru dosya seçilir.
class Mixed:
    def __init__(self, size, w):
        self.a = ImageFont.truetype(FD.format(sub="latin", w=w), size); self.b = ImageFont.truetype(FD.format(sub="latin-ext", w=w), size)
        self.c = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    def pick(self, ch):
        o = ord(ch)
        # fontsource "latin" aralığı: U+0000–00FF, U+0131 (ı), U+2000–206F (tire, tırnak, nokta); ğ, ş, İ, Ğ, Ş "latin-ext"te
        if o < 0x100 or o == 0x131 or 0x2000 <= o <= 0x206F: return self.a
        if 0x100 <= o <= 0x24F: return self.b
        return self.c  # ♪ gibi Manrope'ta olmayan simgeler
def tlen(d, text, f): return sum(d.textlength(ch, font=f.pick(ch)) for ch in text)
def draw(d, x, y, text, f, fill, **kw):
    for ch in text:
        d.text((x, y), ch, font=f.pick(ch), fill=fill, **kw); x += d.textlength(ch, font=f.pick(ch))
NAVY, CREAM, ORANGE = (27, 34, 56), (251, 248, 243), (226, 110, 58)

def times(E):
    v = json.load(open(f"{E}/05_voice.json")); s = json.load(open(f"{E}/03_script.json")); sc = json.load(open(f"{E}/04_scenes.json"))
    text = {l["id"]: l["display"] for sec in s["sections"] for l in sec["lines"]}
    scm = {x["id"]: x for x in sc["scenes"]}
    out = []
    for x in v["scenes"]:
        for i, lid in enumerate(scm[x["sceneId"]]["lineIds"]):
            out.append((text[lid], (x["startFrame"] + x["lineStartFrames"][i]) / v["fps"], (x["startFrame"] + x["lineEndFrames"][i]) / v["fps"]))
    return v, s, out

def find(lines, prefix):
    for t, a, b in lines:
        if t.startswith(prefix): return a, b
    raise SystemExit(f"Satır bulunamadı: {prefix}")

def overlay(path, headline, number):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    # üst başlık kartı
    f = Mixed(76, 800)
    wrapped = textwrap.wrap(headline, 20)
    lh = 92; bh = 70 + lh * len(wrapped)
    top = VY - 60 - bh
    d.rounded_rectangle([60, top, W - 60, top + bh], 44, fill=CREAM + (245,))
    for i, line in enumerate(wrapped):
        tw = tlen(d, line, f)
        draw(d, (W - tw) / 2, top + 30 + i * lh, line, f, NAVY)
    # bölüm rozeti
    fb = Mixed(40, 700)
    tag = f"MuMa Library · #{number}"
    tw = tlen(d, tag, fb)
    d.rounded_rectangle([(W - tw) / 2 - 30, top - 90, (W + tw) / 2 + 30, top - 20], 35, fill=ORANGE + (255,))
    draw(d, (W - tw) / 2, top - 82, tag, fb, (255, 255, 255))
    # alt çağrı
    y = VY + VH + 70
    f2 = Mixed(58, 800); f3 = Mixed(44, 700)
    d.rounded_rectangle([140, y - 30, W - 140, y + 160], 44, fill=NAVY + (235,))
    for txt, fn, col, dy in (("Tam video kanalda!", f2, CREAM, 0), ("Abone ol, zili aç", f3, (255, 214, 170), 84)):
        tw = tlen(d, txt, fn)
        draw(d, (W - tw) / 2, y + dy, txt, fn, col)
    im.save(path)

def render(E, a, b, headline, number, out, maxdur=None):
    ov = out[:-4] + ".overlay.png"; overlay(ov, headline, number)
    dur = b - a
    # şarkı 60 sn sınırını az aşarsa, perde korunarak hafifçe hızlandırılır (son kelime kesilmesin)
    k = dur / maxdur if maxdur and dur > maxdur else 1.0
    od = dur / k
    fil = (f"[0:v]split[bg][fg];"
           f"[bg]scale=-2:{H},crop={W}:{H},boxblur=30:3,eq=brightness=-0.12[bgb];"
           f"[fg]scale={VW}:{VH}[fgs];"
           f"[bgb][fgs]overlay=0:{VY}[base];[base][1:v]overlay=0:0,setpts=PTS/{k:.5f},format=yuv420p[v];"
           f"[0:a]atempo={k:.5f},afade=t=in:d=0.25,afade=t=out:st={max(0, od - 0.6):.2f}:d=0.6[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", f"{E}/out/video.mp4", "-i", ov,
                    "-filter_complex", fil, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-r", "30", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{min(2.0, od / 3):.2f}", "-i", out, "-frames:v", "1", "-q:v", "3", out[:-4] + ".jpg"], check=True)
    os.remove(ov)
    print(f"✓ {out} ({od:.1f} sn{'' if k == 1 else f', x{k:.3f}'})")

def main():
    E, spec = sys.argv[1].rstrip("/"), json.load(open(sys.argv[2]))
    v, s, lines = times(E)
    os.makedirs(f"{E}/out/shorts", exist_ok=True)
    for i, c in enumerate(spec, 1):
        if c.get("song"):
            sg = v["song"]; first = sg["sections"][0]["lines"][0]["startFrame"] / v["fps"]
            a, b = first - 0.2, sg["endFrame"] / v["fps"]
        else:
            a = 0.0 if c.get("from_start") else find(lines, c["first"])[0] - 0.25
            b = find(lines, c["last"])[1] + 0.45
        render(E, a, b, c["headline"], s["episodeNumber"], f"{E}/out/shorts/{i}-{c['name']}.mp4", 59.5 if c.get("song") else None)

if __name__ == "__main__":
    main()
