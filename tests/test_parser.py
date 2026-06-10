import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import (
    open_pdf,
    extract_all_pages
)


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

print(f"\nTotal Pages Extracted: {len(pages)}\n")

for page in pages:

    print("=" * 80)
    print(f"PAGE {page['page']}")
    print("=" * 80)

    # Show only first 300 characters
    print(page["text"][:300])

    print("\n")