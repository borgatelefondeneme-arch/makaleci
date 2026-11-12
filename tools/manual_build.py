"""Manuel sağlayıcı (Claude API anahtarı yokken) için ortak yardımcılar.
Bölümün manual/build.py dosyası bunu içe aktarır: olgu, satır ve sahne kurucuları + JSON yazımı."""
import json, os

STYLE = ["cheerful educational pop song", "upbeat marching band rhythm", "adventurous cartoon theme energy", "bright glockenspiel, snare drum, tuba, hand claps", "catchy sing-along melody", "120 BPM", "clear enthusiastic lead vocal in Turkish", "group vocals shouting along in the chorus", "major key"]
NEG = ["sad", "slow", "dark", "heavy distortion", "mumbled vocals", "long instrumental solo", "lullaby"]
NOTE = "Şematik çizim; ölçekli değildir."
M = {"state": "talk", "x": 0.87, "y": 0.54, "scale": 1.15}  # yalnızca kapanışta geçerli

def F(i, st, q, loc, nums=()):
    return {"id": f"f{i}", "kind": "number" if nums else "claim", "statement": st, "numbers": list(nums), "quote": q, "location": loc}

class Ep:
    def __init__(self):
        self.n = 0; self.sections = []; self.scenes = []; self.pos = 0
    def L(self, text, f=(), spoken=None):
        self.n += 1
        return {"id": f"l{self.n}", "display": text, "spoken": spoken or text, "factIds": [f"f{i}" for i in f]}
    def sec(self, sid, lines):
        self.sections.append((sid, lines))
    def _idx(self):
        self.allids = [l["id"] for s, ls in self.sections for l in ls]
        self.by = {l["id"]: l for s, ls in self.sections for l in ls}
        self.sec_of = {l["id"]: s for s, ls in self.sections for l in ls}
    def S(self, k, visual, stickers=(), keywords=(), extra=(), fx=None):
        """k satırlık sahne. stickers: kenarda süzülen simgeler; keywords: satır başına büyük anahtar kelime."""
        if not self.scenes: self._idx()
        li = self.allids[self.pos:self.pos + k]; self.pos += k
        sc = {"id": f"s{len(self.scenes)+1}", "section": self.sec_of[li[0]], "lineIds": li, "visual": visual, "mascot": M,
              "factIds": sorted({f for i in li for f in self.by[i]["factIds"]} | {f"f{e}" for e in extra}, key=lambda x: int(x[1:]))}
        if fx: sc["fx"] = fx
        if stickers: sc["stickers"] = list(stickers)
        if keywords: sc["keywords"] = (list(keywords) + [""] * k)[:k]
        self.scenes.append(sc)
    def song(self, title, cast, v1, c1, v2, c2, show=None):
        """Şarkı: giriş + kıta + nakarat + kıta + nakarat (~61 sn)."""
        extra = {"show": show} if show else {}
        return {**extra, "title": title, "style": STYLE, "negativeStyle": NEG, "cast": [{"emoji": e, "name": nm} for e, nm in cast],
                "sections": [
                    {"tag": "Intro", "label": "Giriş", "direction": "snare drum roll, hand claps", "lines": ["Hey! Hey! Hey!"], "durationMs": 5000},
                    {"tag": "Verse 1", "label": "Kıta", "lines": v1, "durationMs": 15000},
                    {"tag": "Chorus", "label": "Nakarat", "lines": c1, "durationMs": 13000},
                    {"tag": "Verse 2", "label": "Kıta", "lines": v2, "durationMs": 15000},
                    {"tag": "Chorus", "label": "Nakarat", "lines": c2, "durationMs": 13000}]}
    def write(self, D, facts, script):
        assert self.pos == len(self.allids), (self.pos, len(self.allids))
        script["sections"] = [{"id": s, "lines": ls} for s, ls in self.sections]
        script.setdefault("nextTeaser", "Yeni bir soru, yeni bir keşif seni bekliyor!")
        for name, data in (("facts", facts), ("script", script), ("scenes", {"scenes": self.scenes})):
            json.dump(data, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        sp = [l["spoken"] for s, ls in self.sections for l in ls]
        print("satır:", len(sp), "sahne:", len(self.scenes), "kelime:", sum(len(x.split()) for x in sp), "karakter:", sum(len(x) for x in sp))
