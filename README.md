# PubMed CLI Tool

A Python command-line tool that fetches PubMed research papers and filters out authors affiliated with non-academic institutions (e.g., companies, pharma, biotech).

---

## 🚀 Features

- Searches PubMed using E-Utilities API
- Filters authors based on non-academic affiliations
- Outputs results to console or CSV
- Built with [Poetry](https://python-poetry.org) for dependency management

---

## 🧠 How Filtering Works

The tool considers an author **non-academic** if their affiliation does **not contain** keywords like:

university, institute, hospital, college, school, lab

---

## 🛠️ Setup Instructions

### 1. Clone the repository (after uploading to GitHub)
```bash
git clone https://github.com/your-username/pubmed-cli.git
cd pubmed-cli

2 . Install dependencies using Poetry
 poetry install

 📌 Usage
Search and print to console:
 poetry run python cli.py "covid vaccine"

Search and save to CSV:
 poetry run python cli.py "covid vaccine" -f results.csv

Enable debug mode:
 poetry run python cli.py "covid vaccine" -f results.csv --debug

📦 Dependencies

Python 3.10+
requests
lxml

📁 Project Structure
pubmed-cli/
├── cli.py
├── pyproject.toml
├── README.md
├── pubmed_fetcher/
│   ├── __init__.py
│   ├── fetcher.py
│   └── filters.py




