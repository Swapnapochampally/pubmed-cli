# pubmed_fetcher/filters.py

from lxml import etree
from typing import List, Dict

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "institute", "school", "hospital", "lab"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = etree.fromstring(xml_data.encode())
    results = []

    for article in root.xpath("//PubmedArticle"):
        paper = {
            "PubmedID": article.xpath("MedlineCitation/PMID/text()")[0],
            "Title": "".join(article.xpath("MedlineCitation/Article/ArticleTitle/text()")),
            "Publication Date": "".join(article.xpath(".//PubDate/Year/text()")),
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": "",
        }

        for author in article.xpath(".//Author"):
            affiliation = "".join(author.xpath(".//AffiliationInfo/Affiliation/text()"))
            name = " ".join(author.xpath("./ForeName/text()") + author.xpath("./LastName/text()"))

            if affiliation and is_non_academic(affiliation):
                paper["Non-academic Author(s)"].append(name)
                paper["Company Affiliation(s)"].append(affiliation)

                if "@" in affiliation and not paper["Corresponding Author Email"]:
                    for word in affiliation.split():
                        if "@" in word:
                            paper["Corresponding Author Email"] = word
                            break

        if paper["Non-academic Author(s)"]:
            results.append(paper)

    return results



