# cli.py

import argparse
import csv
from pubmed_fetcher.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from pubmed_fetcher.filters import parse_pubmed_xml

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    if args.debug:
        print(f"[DEBUG] Query: {args.query}")

    ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"[DEBUG] Found {len(ids)} PubMed IDs")

    xml_data = fetch_pubmed_details(ids)
    papers = parse_pubmed_xml(xml_data)

    if not papers:
        print("[INFO] No papers with non-academic authors found.")
        return

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=papers[0].keys())
            writer.writeheader()
            writer.writerows(papers)
        print(f"[INFO] Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
