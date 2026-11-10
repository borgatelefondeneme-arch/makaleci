"""Ortak yardımcılar: HTTP, Paper sözlüğü, metin temizleme. Yalnızca standart kütüphane."""
import html
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

UA = "gunun-bilimi/0.1"


def load_env(path=".env"):
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            m = re.match(r"\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$", line)
            if m and m.group(2) and m.group(1) not in os.environ:
                os.environ[m.group(1)] = m.group(2).strip("'\"")


def http_get(url, params=None, timeout=40, retries=4, headers=None):
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (400, 401, 403, 404):
                raise
        except Exception as e:  # ağ hatası: bekle, yeniden dene
            last = e
        time.sleep(2 ** (i + 1))
    raise last


def get_json(url, params=None, **kw):
    return json.loads(http_get(url, params, **kw))


def clean(text):
    """Etiketleri ve fazla boşluğu temizler."""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s*\S+@\S+\.\w+\.?", "", text)  # e-posta adresleri künyeye taşınmaz
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def norm_doi(doi):
    if not doi:
        return None
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip(), flags=re.I)
    return doi or None  # DOI büyük/küçük harfe duyarsızdır; yazımı korunur, karşılaştırma küçük harfle


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def paper(**kw):
    """Paper şemasına (schemas/index.ts) uyan sözlük; eksik alanlar güvenli varsayılanla dolar."""
    p = {
        "kind": "paper", "id": "", "title": "", "abstract": "", "authors": [], "institutions": [], "venue": None,
        "doi": None, "url": "", "fullTextUrl": None, "license": None, "publishedAt": None,
        "isPreprint": True, "peerReviewStatus": "unknown", "categories": [], "sources": [],
        "fetchedAt": now_iso(),
    }
    p.update(kw)
    p["doi"] = norm_doi(p["doi"])
    if not p["institutions"]:
        seen = []
        for a in p["authors"]:
            for aff in a.get("affiliations", []):
                if aff and aff not in seen:
                    seen.append(aff)
        p["institutions"] = seen
    return p


PREPRINT_HOSTS = ("arxiv", "biorxiv", "medrxiv", "chemrxiv", "research square", "ssrn", "preprints", "psyarxiv", "osf")


def looks_like_preprint_venue(venue):
    v = (venue or "").lower()
    return any(h in v for h in PREPRINT_HOSTS)
