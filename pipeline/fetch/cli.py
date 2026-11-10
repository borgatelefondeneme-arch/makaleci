"""fetch aşaması.

  Tek makale : python3 -m pipeline.fetch.cli --url <arXiv|DOI|PubMed linki> --out 01_paper.json [--fulltext 01_fulltext.txt]
  Son 48 saat: python3 -m pipeline.fetch.cli --recent 48 --out data/pool/<tarih>.json
"""
import argparse
import json
import os
import re
import sys

from . import arxiv, crossref, openalex, pubmed
from .common import http_get, load_env, norm_doi
from .merge import dedupe, enrich

DOI_RE = r"10\.\d{4,9}/[^\s\"'<>?#]+"


def resolve(url):
    """Linki çözer → (paper, tam_metin | None)."""
    url = url.strip()
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([\w.\-/]+?)(?:v\d+)?(?:\.pdf)?/?$", url, re.I) or re.search(r"10\.48550/arxiv\.([\w.\-/]+)", url, re.I) or re.match(r"^arxiv:([\w.\-/]+)$", url, re.I)
    if m:
        p = arxiv.by_id(m.group(1))
        if not p:
            sys.exit(f"arXiv kaydı bulunamadı: {m.group(1)}")
        if not p["doi"].startswith("10.48550/"):  # dergi sürümü var: künyeyi zenginleştir
            enrich(p, openalex.by_doi(p["doi"]) or crossref.by_doi(p["doi"]))
        return p, arxiv.full_text(m.group(1))

    m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url) or re.match(r"^pmid:(\d+)$", url, re.I)
    if m:
        res = pubmed.by_ids([m.group(1)])
        if not res:
            sys.exit(f"PubMed kaydı bulunamadı: {m.group(1)}")
        p = res[0]
        if p["doi"]:
            enrich(p, openalex.by_doi(p["doi"]) or crossref.by_doi(p["doi"]))
        return p, _pmc_text(p)

    m = re.search(DOI_RE, url)
    doi = norm_doi(m.group(0)) if m else None
    if not doi and url.startswith("http"):
        # Yayıncı sayfası: DOI'yi meta etiketinden bul.
        page = http_get(url, retries=2)
        mm = re.search(r'name="(?:citation_doi|dc\.identifier|DC\.Identifier)"\s+content="(?:doi:)?(' + DOI_RE + ')"', page, re.I) or re.search(r"doi\.org/(" + DOI_RE + ")", page)
        doi = norm_doi(mm.group(1)) if mm else None
    if not doi:
        sys.exit("Linkten DOI çıkarılamadı. arXiv, PubMed veya DOI linki verin.")
    doi = doi.rstrip(".,;)")
    p = crossref.by_doi(doi) or openalex.by_doi(doi)
    if not p:
        sys.exit(f"DOI çözülemedi: {doi}")
    enrich(p, openalex.by_doi(doi) if "openalex" not in p["sources"] else None)
    try:
        enrich(p, pubmed.by_doi(doi))  # özet + PMC bağlantısı
    except Exception as e:
        print(f"uyarı: PubMed zenginleştirme başarısız: {e}", file=sys.stderr)
    return p, _pmc_text(p)


def _pmc_text(p):
    m = re.search(r"(PMC\d+)", p.get("fullTextUrl") or "")
    return pubmed.full_text(m.group(1)) if m else None


def recent(hours, cats):
    pool = []
    for name, fn in (("arxiv", lambda: arxiv.recent(hours, cats)), ("pubmed", lambda: pubmed.recent(hours)), ("openalex", lambda: openalex.recent(hours))):
        if name == "openalex" and not openalex.enabled():
            print("uyarı: OPENALEX_API_KEY yok, OpenAlex atlandı", file=sys.stderr)
            continue
        try:
            got = fn()
            print(f"{name}: {len(got)} makale", file=sys.stderr)
            pool += got
        except Exception as e:
            print(f"uyarı: {name} başarısız: {e}", file=sys.stderr)
    return [p for p in dedupe(pool) if p["title"] and len(p["abstract"]) > 200]


def main():
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--recent", type=int, metavar="SAAT")
    ap.add_argument("--arxiv-cats", help="virgülle ayrılmış arXiv kategorileri")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fulltext", help="tam metin (varsa) buraya yazılır")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    if a.url:
        p, text = resolve(a.url)
        if not p["title"] or not p["abstract"]:
            print("uyarı: başlık veya özet eksik — senaryo yalnızca eldeki metne dayanabilir", file=sys.stderr)
        result = p
        if a.fulltext and text:
            open(a.fulltext, "w", encoding="utf-8").write(text)
        print(f"{p['id']} · {p['peerReviewStatus']} · tam metin: {'var' if text else 'yok'}", file=sys.stderr)
    elif a.recent:
        result = recent(a.recent, a.arxiv_cats.split(",") if a.arxiv_cats else None)
        print(f"toplam {len(result)} aday", file=sys.stderr)
    else:
        ap.error("--url veya --recent gerekli")
    json.dump(result, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
