import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_text
from src.chunker import chunk_text
from src.embedder import get_embedding


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

print(f"Pages Found: {len(pages)}")

all_chunks = []

for page in pages:

    cleaned_text = clean_text(
        page["text"]
    )

    chunks = chunk_text(
        cleaned_text,
        chunk_size=500
    )

    all_chunks.extend(chunks)

print(f"Total Chunks: {len(all_chunks)}")

print("\nEmbedding first chunk...")

print("\nChunk Type:")
print(type(all_chunks[0]))

embedding = get_embedding(
    all_chunks[0]
)

print("\nEmbedding Created Successfully")

print("\nEmbedding Dimension:")
print(len(embedding))

print("\nChunk Preview:")
print(all_chunks[0][:300])

print("\nFirst 10 Embedding Values:")
print(embedding[:10])