import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_text
from src.chunker import chunk_pages
from src.embedder import load_embedding_model

from src.vector_store import (
    build_faiss_index,
    save_index
)

from src.metadata_store import (
    save_metadata
)


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

for page in pages:
    page["text"] = clean_text(
        page["text"]
    )

chunks = chunk_pages(pages)

print(f"Total Chunks: {len(chunks)}")

model = load_embedding_model()

embeddings = model.encode(
    [chunk["text"] for chunk in chunks]
)

index = build_faiss_index(
    embeddings
)

save_index(
    index,
    "data/index/faiss.index"
)

save_metadata(
    chunks,
    "data/index/metadata.pkl"
)

print(
    f"\nSaved {len(chunks)} chunks"
)

print(
    f"Embedding Dimension: {embeddings.shape[1]}"
)