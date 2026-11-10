"""PubMed E-utilities."""
import os
import xml.etree.ElementTree as ET

from .common import clean, http_get, get_json, paper

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
MONTHS = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def _auth():
    p = {"tool": "gunun-bilimi"}
    if os.environ.get("NCBI_API_KEY"):
        p["api_key"] = os.environ["NCBI_API_KEY"]
    if os.environ.get("CONTACT_EMAIL"):
        p["email"] = os.environ["CONTACT_EMAIL"]
    return p


def _date(art):
    d = art.find(".//ArticleDate") or art.find(".//PubDate")
    if d is None or not d.findtext("Year"):
        return None
    mo = d.findtext("Month") or "1"
    mo = MONTHS.get(mo[:3], None) if not mo.isdigit() else int(mo)
    return f"{d.findtext('Year')}-{int(mo or 1):02d}-{int(d.findtext('Day') or 1):02d}"


def _parse(xml):
    out = []
    for art in ET.fromstring(xml).findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID")
        ids = {i.get("IdType"): (i.text or "") for i in art.findall(".//ArticleIdList/ArticleId")}
        types = [t.text for t in art.findall(".//PublicationType")]
        pre = "Preprint" in types
        authors = []
        for a in art.findall(".//AuthorList/Author"):
            name = " ".join(x for x in [a.findtext("ForeName"), a.findtext("LastName")] if x) or a.findtext("CollectiveName") or ""
            if name:
                authors.append({"name": name, "affiliations": [clean(x.text) for x in a.findall(".//Affiliation") if x.text]})
        abstract = " ".join(clean("".join(t.itertext())) for t in art.findall(".//Abstract/AbstractText"))
        pmc = ids.get("pmc")
        out.append(paper(
            id=f"pmid:{pmid}",
            title=clean("".join(art.find(".//ArticleTitle").itertext())) if art.find(".//ArticleTitle") is not None else "",
            abstract=abstract,
            authors=authors,
            venue=art.findtext(".//Journal/Title"),
            doi=ids.get("doi"),
            url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            fullTextUrl=f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/" if pmc else None,
            publishedAt=_date(art),
            isPreprint=pre,
            peerReviewStatus="preprint" if pre else "peer_reviewed",
            categories=[m.findtext("DescriptorName") for m in art.findall(".//MeshHeading")][:10],
            sources=["pubmed"],
        ))
    return out


def by_ids(pmids):
    if not pmids:
        return []
    return _parse(http_get(BASE + "efetch.fcgi", {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml", **_auth()}))


def by_doi(doi):
    r = get_json(BASE + "esearch.fcgi", {"db": "pubmed", "term": f"{doi}[doi]", "retmode": "json", **_auth()})
    ids = r.get("esearchresult", {}).get("idlist", [])
    return by_ids(ids[:1])[0] if ids else None


def recent(hours=48, term="(journal article[pt] OR preprint[pt]) AND hasabstract AND english[la]", limit=200):
    # edat = PubMed'e giriş tarihi; "son 48 saat" için yayın tarihinden daha güvenilir.
    days = max(1, round(hours / 24))
    r = get_json(BASE + "esearch.fcgi", {"db": "pubmed", "term": term, "reldate": days, "datetype": "edat", "retmax": limit, "retmode": "json", "sort": "pub_date", **_auth()})
    return by_ids(r.get("esearchresult", {}).get("idlist", []))


def full_text(pmcid):
    """PMC açık erişim tam metni (varsa) düz yazı olarak."""
    try:
        xml = http_get(BASE + "efetch.fcgi", {"db": "pmc", "id": pmcid.replace("PMC", ""), "retmode": "xml", **_auth()}, retries=2)
        body = ET.fromstring(xml).find(".//body")
        if body is None:
            return None
        for tag in ("fig", "table-wrap", "supplementary-material"):
            for parent in body.iter():
                for child in [c for c in parent if c.tag == tag]:
                    parent.remove(child)
        text = clean(" ".join(body.itertext()))
        return text if len(text) > 3000 else None
    except Exception:
        return None
