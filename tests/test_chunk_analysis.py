import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_pages
from src.chunker import chunk_pages


# -----------------------------
# Load PDF
# -----------------------------
pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

cleaned_pages = clean_pages(pages)

chunks = chunk_pages(
    cleaned_pages,
    chunk_size=500
)

# -----------------------------
# Basic Stats
# -----------------------------
print("=" * 80)
print("CHUNK ANALYSIS REPORT")
print("=" * 80)

print(f"\nTotal Pages  : {len(cleaned_pages)}")
print(f"Total Chunks : {len(chunks)}")

# -----------------------------
# Length Statistics
# -----------------------------
lengths = [len(chunk["text"]) for chunk in chunks]

print("\nLENGTH STATISTICS")
print("-" * 40)

print(f"Smallest Chunk : {min(lengths)} chars")
print(f"Largest Chunk  : {max(lengths)} chars")
print(f"Average Chunk  : {sum(lengths) / len(lengths):.2f} chars")

# -----------------------------
# Per Chunk Analysis
# -----------------------------
print("\nCHUNK DETAILS")
print("-" * 40)

for chunk in chunks:

    length = len(chunk["text"])

    print(
        f"Page={chunk['page']:2} | "
        f"Chunk={chunk['chunk_id']:2} | "
        f"Length={length:4}"
    )

# -----------------------------
# Small Chunks Warning
# -----------------------------
print("\nSMALL CHUNKS (<100 chars)")
print("-" * 40)

small_chunks = 0

for chunk in chunks:

    if len(chunk["text"]) < 100:

        small_chunks += 1

        print(
            f"Page {chunk['page']} | "
            f"Chunk {chunk['chunk_id']} | "
            f"Length {len(chunk['text'])}"
        )

print(f"\nTotal Small Chunks: {small_chunks}")

# -----------------------------
# Largest Chunk Preview
# -----------------------------
largest_chunk = max(
    chunks,
    key=lambda x: len(x["text"])
)

print("\nLARGEST CHUNK PREVIEW")
print("-" * 40)

print(
    f"Page {largest_chunk['page']} | "
    f"Chunk {largest_chunk['chunk_id']} | "
    f"Length {len(largest_chunk['text'])}"
)

print()

print(largest_chunk["text"][:500])

print("\n")

# -----------------------------
# First 5 Chunks Preview
# -----------------------------
print("=" * 80)
print("FIRST 5 CHUNKS PREVIEW")
print("=" * 80)

for chunk in chunks[:5]:

    print(
        f"\nPage {chunk['page']} | "
        f"Chunk {chunk['chunk_id']} | "
        f"Length {len(chunk['text'])}"
    )

    print("-" * 40)

    print(chunk["text"][:200])

    print("\n")