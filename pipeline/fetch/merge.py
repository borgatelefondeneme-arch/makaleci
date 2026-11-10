"""Kaynakları birleştirme: DOI/başlık üzerinden tekilleştirme ve alan zenginleştirme."""
import re


def _key(p):
    return (p["doi"] or "").lower() or re.sub(r"\W+", "", p["title"].lower())[:80]


def enrich(base, other):
    """base'in boş alanlarını other'dan doldurur; preprint sinyallerini birleştirir."""
    if not other:
        return base
    for k in ("abstract", "venue", "license", "publishedAt", "fullTextUrl", "doi", "title"):
        if not base.get(k) and other.get(k):
            base[k] = other[k]
    if len(other.get("abstract") or "") > len(base.get("abstract") or "") * 1.5:
        base["abstract"] = other["abstract"]
    if not base["institutions"] and other["institutions"]:
        base["institutions"] = other["institutions"]
    if other["authors"] and not any(a["affiliations"] for a in base["authors"]) and len(other["authors"]) == len(base["authors"]):
        base["authors"] = other["authors"]
    if not base["authors"]:
        base["authors"] = other["authors"]
    base["categories"] = list(dict.fromkeys(base["categories"] + other["categories"]))
    base["sources"] = list(dict.fromkeys(base["sources"] + other["sources"]))
    # Hakemlik: kaynaklar çelişirse veya belirsizse preprint sayılır (temkinli taraf).
    statuses = {base["peerReviewStatus"], other["peerReviewStatus"]} - {"unknown"}
    if statuses == {"peer_reviewed"}:
        base["peerReviewStatus"], base["isPreprint"] = "peer_reviewed", False
    elif "preprint" in statuses:
        base["peerReviewStatus"], base["isPreprint"] = "preprint", True
    return base


def dedupe(papers):
    out = {}
    for p in papers:
        k = _key(p)
        out[k] = enrich(out[k], p) if k in out else p
    return list(out.values())
