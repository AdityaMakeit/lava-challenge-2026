import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_text
from src.chunker import chunk_text


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

chunks = chunk_text(
    clean_text(pages[0]["text"]),
    page_number=1
)

print(chunks[0])