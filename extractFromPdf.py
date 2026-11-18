# Muhammad Ahmad, CMS 542432, BSCS-15-D
"""
extractFromPdf.py  (runs LOCALLY)
Reads the 3 PDFs and writes raw/constitution.txt, raw/ppc.txt, raw/peca.txt.
Every page is prefixed with a line "=== PAGE n ===" (the PDFs already contain "Page n of N").

Put the PDFs in  <project>/pdfs/  (or directly in the project folder):
    Pakistan_Constitution.pdf, Penal_code.pdf, PECA.pdf
Run:  python extractFromPdf.py
"""
from pathlib import Path
import pymupdf  # PyMuPDF (new import name; old name was 'fitz')

ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "raw"
SEARCH_DIRS = [ROOT / "pdfs", ROOT / "data", ROOT]

PDFS = {                      # law key -> pdf file name
    "constitution": "Pakistan_Constitution.pdf",
    "ppc": "Penal_code.pdf",
    "peca": "PECA.pdf",
}


def find_pdf(name):
    for d in SEARCH_DIRS:
        p = d / name
        if p.exists():
            return p
    return None


def extract(law, pdf_path):
    doc = pymupdf.open(pdf_path)
    parts, empty_pages = [], []
    for i, page in enumerate(doc, start=1):
        text = page.get_text()            # plain text, reading order as PyMuPDF gives it
        if len(text.strip()) < 50:
            empty_pages.append(i)
        parts.append(f"=== PAGE {i} ===\n{text.rstrip()}\n")
    out = RAW_DIR / f"{law}.txt"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"[{law}] {pdf_path.name}: {len(doc)} pages, {sum(map(len, parts)):,} chars -> {out}")
    if empty_pages:
        print(f"   WARNING pages with almost no text (scanned? blank?): {empty_pages[:20]}")
    doc.close()


def main():
    RAW_DIR.mkdir(exist_ok=True)
    for law, name in PDFS.items():
        p = find_pdf(name)
        if p is None:
            print(f"[{law}] NOT FOUND: {name} (looked in {[str(d) for d in SEARCH_DIRS]})")
            continue
        extract(law, p)


if __name__ == "__main__":
    main()
