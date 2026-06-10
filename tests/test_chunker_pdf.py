import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import (
    open_pdf,
    extract_all_pages
)

from src.chunker import (
    chunk_pages
)

pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

chunks = chunk_pages(
    pages,
    chunk_size=500
)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")

print(chunks[0:13])