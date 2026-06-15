import sys 
from pathlib import Path 

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.pdf_parser import open_pdf , extract_all_pages
from src.text_cleaner import clean_text
from src.chunker import chunk_pages
from src.embedder import load_embedding_model 
from src.retriever import retrieve

#  Load PDF 
 
pdf = open_pdf(
     "data/train_pdfs/train_pdfs/j_0060.pdf"
)

pages = extract_all_pages(pdf)

#CLEAN 

for page in pages:
    page["text"] = clean_text(page["text"])


#chunk 
chunks = chunk_pages(pages,chunk_size = 500)

print(f"Total Chunks: {len(chunks)}")

# Embeddings 

model = load_embedding_model()

texts = [chunk["text"] for chunk in chunks]

print(type(texts))
print(type(texts[0]))
print(texts[0])

chunk_embeddings = model.encode(texts)

print(f"Embeddings Created: {len(chunk_embeddings)}")

#Query 

query = "What were the main missions of this research project?"

#Query Embedding 

query_embedding = model.encode(query)

#retrieve 

results = retrieve(query_embeddings= query_embedding, chunk_embeddings=chunk_embeddings,chunks = chunks, top_k=3)

# -------------------------
# DISPLAY
# -------------------------

print("\n" + "=" * 80)
print("TOP RESULTS")
print("=" * 80)

for result in results:

    print(
        f"\nPage: {result['page']} "
        f"| Chunk: {result['chunk_id']} "
        f"| Score: {result['score']:.4f}"
    )

    print("-" * 40)

    print(result["text"][:500])