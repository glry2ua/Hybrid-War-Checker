import glob
import re
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text
import os

INPUT_PDF_DIR  = '../data/raw_pdfs'
INPUT_HTML_DIR = '../data/raw_html'
OUTPUT_DIR     = '../data/clean_txt'

def clean_text(raw: str) -> str:
    # collapse whitespace
    text = re.sub(r'\s+', ' ', raw)
    return text.strip()

def extract_from_pdf(pdf_path: str) -> str:
    return extract_text(pdf_path)

def extract_from_html(html_path: str) -> str:
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    for tag in soup(['script', 'style']):
        tag.decompose()
    return soup.get_text(separator=' ')

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # PDFs
    for pdf in glob.glob(f'{INPUT_PDF_DIR}/*.pdf'):
        raw = extract_from_pdf(pdf)
        clean = clean_text(raw)
        out = pdf.replace('raw_pdfs', 'clean_txt').replace('.pdf', '.txt')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(clean)
    # HTMLs (optional)
    for html in glob.glob(f'{INPUT_HTML_DIR}/*.html'):
        raw = extract_from_html(html)
        clean = clean_text(raw)
        out = html.replace('raw_html', 'clean_txt').replace('.html', '.txt')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(clean)

if __name__ == '__main__':
    main()