import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_text


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

first_page = pages[0]

cleaned_text = clean_text(
    first_page["text"]
)

print(cleaned_text[:1000])