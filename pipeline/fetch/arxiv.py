"""arXiv Atom API."""
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from .common import clean, http_get, paper

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
# Genel izleyici için ilgi çekici alanlar; --arxiv-cats ile değiştirilebilir.
DEFAULT_CATS = ["astro-ph.EP", "astro-ph.GA", "physics.pop-ph", "q-bio.NC", "q-bio.PE", "cs.AI", "cs.RO", "physics.ao-ph", "cond-mat.mtrl-sci"]


def _parse(xml):
    out = []
    for e in ET.fromstring(xml).findall("a:entry", NS):
        aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1])
        if not aid:
            continue
        doi = e.findtext("x:doi", None, NS)
        jref = e.findtext("x:journal_ref", None, NS)
        published = bool(doi or jref)  # dergide yayımlanmış sürümü var
        lic = next((l.get("href") for l in e.findall("a:link", NS) if l.get("title") == "license"), None)
        out.append(paper(
            id=f"arxiv:{aid}",
            title=clean(e.findtext("a:title", "", NS)),
            abstract=clean(e.findtext("a:summary", "", NS)),
            authors=[{"name": clean(a.findtext("a:name", "", NS)), "affiliations": [clean(x.text) for x in a.findall("x:affiliation", NS)]} for a in e.findall("a:author", NS)],
            venue=clean(jref) if jref else "arXiv",
            doi=doi or f"10.48550/arXiv.{aid}",
            url=f"https://arxiv.org/abs/{aid}",
            fullTextUrl=f"https://arxiv.org/html/{aid}",
            license=lic,
            publishedAt=e.findtext("a:published", None, NS),
            isPreprint=not published,
            peerReviewStatus="peer_reviewed" if published else "preprint",
            categories=[c.get("term") for c in e.findall("a:category", NS)],
            sources=["arxiv"],
        ))
    return out


def by_id(arxiv_id):
    res = _parse(http_get(API, {"id_list": arxiv_id}))
    return res[0] if res else None


def recent(hours=48, cats=None, limit=200):
    end = datetime.now(timezone.utc)
    start = end - timedelta(hours=hours)
    f = "%Y%m%d%H%M"
    q = "(" + " OR ".join(f"cat:{c}" for c in (cats or DEFAULT_CATS)) + f") AND submittedDate:[{start.strftime(f)} TO {end.strftime(f)}]"
    return _parse(http_get(API, {"search_query": q, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": limit}))


def full_text(arxiv_id):
    """arXiv HTML sürümünden düz metin (şekiller alınmaz — yalnızca yazı)."""
    try:
        h = http_get(f"https://arxiv.org/html/{arxiv_id}", retries=2)
    except Exception:
        return None
    h = re.sub(r"(?is)<(script|style|figure|svg|math|nav|header|footer)\b.*?</\1>", " ", h)
    m = re.search(r"(?is)<article.*?</article>", h)
    text = clean(m.group(0) if m else h)
    return text if len(text) > 3000 else None
