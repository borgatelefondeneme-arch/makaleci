"""Crossref — DOI çözümleme (dergi, lisans, kurum, yayın türü). OpenAlex yokken yedek."""
import os

from .common import clean, get_json, looks_like_preprint_venue, paper


def by_doi(doi):
    params = {"mailto": os.environ["CONTACT_EMAIL"]} if os.environ.get("CONTACT_EMAIL") else None
    try:
        m = get_json(f"https://api.crossref.org/works/{doi}", params)["message"]
    except Exception:
        return None
    venue = (m.get("container-title") or [None])[0] or (m.get("institution") or [{}])[0].get("name") or m.get("publisher")
    pre = m.get("type") == "posted-content" or looks_like_preprint_venue(venue)
    parts = (m.get("published") or m.get("issued") or {}).get("date-parts", [[None]])[0]
    date = "-".join(f"{int(x):02d}" for x in parts if x) if parts and parts[0] else None
    lic = next((l["URL"] for l in m.get("license", []) if l.get("content-version") in ("vor", "unspecified", None)), None) or next((l["URL"] for l in m.get("license", [])), None)
    known = m.get("type") in ("journal-article", "proceedings-article", "posted-content")
    return paper(
        id=f"doi:{doi}",
        title=clean((m.get("title") or [""])[0]),
        abstract=clean(m.get("abstract")),
        authors=[{"name": " ".join(x for x in [a.get("given"), a.get("family")] if x) or a.get("name", ""), "affiliations": [x["name"] for x in a.get("affiliation", []) if x.get("name")]} for a in m.get("author", [])],
        venue=venue,
        doi=doi,
        url=f"https://doi.org/{doi}",
        license=lic,
        publishedAt=date,
        isPreprint=bool(pre) or not known,  # belirsizse temkinli taraf: preprint say
        peerReviewStatus="preprint" if pre else ("peer_reviewed" if known else "unknown"),
        categories=m.get("subject", [])[:6],
        sources=["crossref"],
    )
