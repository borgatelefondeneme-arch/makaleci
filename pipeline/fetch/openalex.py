"""OpenAlex. Anahtarsız istekler 429 dönebildiği için OPENALEX_API_KEY yoksa atlanır."""
import os
from datetime import datetime, timedelta, timezone

from .common import get_json, looks_like_preprint_venue, paper

API = "https://api.openalex.org/works"


def enabled():
    return bool(os.environ.get("OPENALEX_API_KEY"))


def _auth():
    p = {"api_key": os.environ["OPENALEX_API_KEY"]}
    if os.environ.get("CONTACT_EMAIL"):
        p["mailto"] = os.environ["CONTACT_EMAIL"]
    return p


def _abstract(inv):
    if not inv:
        return ""
    pos = sorted((i, w) for w, idxs in inv.items() for i in idxs)
    return " ".join(w for _, w in pos)


def _to_paper(w):
    loc = w.get("primary_location") or {}
    src = loc.get("source") or {}
    venue = src.get("display_name")
    pre = w.get("type") == "preprint" or src.get("type") == "repository" or looks_like_preprint_venue(venue) or loc.get("version") == "submittedVersion"
    oa = w.get("open_access") or {}
    return paper(
        id=w["id"].rsplit("/", 1)[-1] and f"openalex:{w['id'].rsplit('/', 1)[-1]}",
        title=w.get("title") or "",
        abstract=_abstract(w.get("abstract_inverted_index")),
        authors=[{"name": a["author"]["display_name"], "affiliations": [i["display_name"] for i in a.get("institutions", [])]} for a in w.get("authorships", [])],
        venue=venue,
        doi=w.get("doi"),
        url=w.get("doi") or w["id"],
        fullTextUrl=oa.get("oa_url"),
        license=loc.get("license"),
        publishedAt=w.get("publication_date"),
        isPreprint=bool(pre),
        peerReviewStatus="preprint" if pre else "peer_reviewed",
        categories=[c["display_name"] for c in (w.get("concepts") or [])[:6]],
        sources=["openalex"],
    )


def by_doi(doi):
    if not enabled():
        return None
    try:
        return _to_paper(get_json(f"{API}/https://doi.org/{doi}", _auth()))
    except Exception:
        return None


def recent(hours=48, limit=200):
    if not enabled():
        return []
    since = (datetime.now(timezone.utc) - timedelta(hours=hours)).strftime("%Y-%m-%d")
    r = get_json(API, {"filter": f"from_publication_date:{since},has_abstract:true,language:en,type:article|preprint", "sort": "publication_date:desc", "per-page": min(limit, 200), **_auth()})
    return [_to_paper(w) for w in r.get("results", [])]
