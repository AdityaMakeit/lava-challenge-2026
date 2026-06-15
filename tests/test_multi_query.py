import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.pdf_parser import open_pdf, extract_all_pages
from src.text_cleaner import clean_text
from src.chunker import chunk_pages
from src.embedder import load_embedding_model
from src.retriever import retrieve


pdf = open_pdf(
    "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

for page in pages:
    page["text"] = clean_text(page["text"])

chunks = chunk_pages(pages)

print(f"\nTotal Chunks: {len(chunks)}")

# Validate chunks
valid_chunks = []

for i, chunk in enumerate(chunks):

    if chunk is None:
        print(f"Chunk {i} is None")
        continue

    if not isinstance(chunk, dict):
        print(f"Chunk {i} has type {type(chunk)}")
        continue

    if "text" not in chunk:
        print(f"Chunk {i} missing text field")
        continue

    valid_chunks.append(chunk)

chunks = valid_chunks

print(f"Valid Chunks: {len(chunks)}")

model = load_embedding_model()

chunk_embeddings = model.encode(
    [chunk["text"] for chunk in chunks]
)

queries = [
    "What were the main missions of this research project?",
    "How did this research contribute to PM2.5 policy?",
    "What were the key findings?",
    "What publications resulted from this project?",
    "Which government organizations used these results?"
]

for query in queries:

    print("\n")
    print("=" * 80)
    print("QUERY:")
    print(query)
    print("=" * 80)

    query_embedding = model.encode(query)

    results = retrieve(
        query_embeddings=query_embedding,
        chunk_embeddings=chunk_embeddings,
        chunks=chunks,
        top_k=3
    )

    for result in results:

        print(
            f"\nPage {result['page']} | "
            f"Chunk {result['chunk_id']} | "
            f"Score {result['score']:.4f}"
        )

        print("-" * 40)

        print(result["text"][:300])