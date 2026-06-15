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


print("\nTOTAL CHUNKS:")
print(len(all_chunks))


print("\nCREATING EMBEDDINGS...\n")

first_embedding = get_embedding(
    all_chunks[0]
)

print("Embedding Type:")
print(type(first_embedding))

print("\nEmbedding Dimension:")
print(len(first_embedding))

print("\nFirst 10 Values:")
print(first_embedding[:10])

print("\nFIRST CHUNK PREVIEW:")
print(all_chunks[0][:500])