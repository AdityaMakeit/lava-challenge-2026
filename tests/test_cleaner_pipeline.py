import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_pages


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

cleaned_pages = clean_pages(pages)

print("=" * 80)
print("RAW PAGE 1")
print("=" * 80)
print()

print(pages[0]["text"])

print("\n\n")

print("=" * 80)
print("CLEANED PAGE 1")
print("=" * 80)
print()

print(cleaned_pages[0]["text"])

print("\n\n")

print("=" * 80)
print("CHECKING IMPORTANT CONTENT")
print("=" * 80)

important_strings = [
    "5-1801",
    "JPMEERF20185001",
    "PM2.5"
]

for item in important_strings:

    raw_exists = item in pages[0]["text"]
    cleaned_exists = item in cleaned_pages[0]["text"]

    print(
        f"{item} | RAW={raw_exists} | CLEANED={cleaned_exists}"
    )

print("\n")

print("=" * 80)
print("LAST 50 CHARACTERS")
print("=" * 80)

print("\nRAW END:\n")
print(repr(pages[0]["text"][-50:]))

print("\nCLEANED END:\n")
print(repr(cleaned_pages[0]["text"][-50:]))