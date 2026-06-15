import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.pdf_parser import (
    open_pdf,
    extract_all_pages
)

from src.text_cleaner import clean_text
from src.chunker import chunk_pages
from src.embedder import load_embedding_model

from src.vector_store import (
    build_faiss_index,
    save_index,
    save_metadata
)


PDF_FOLDER = Path(
    "data/train_pdfs/train_pdfs"
)

all_chunks = []

pdf_files = list(
    PDF_FOLDER.glob("*.pdf")
)

print(
    f"\nFound {len(pdf_files)} PDFs"
)

for pdf_file in pdf_files:

    print(
        f"\nProcessing: {pdf_file.name}"
    )

    pdf = open_pdf(
        str(pdf_file)
    )

    pages = extract_all_pages(
        pdf
    )

    for page in pages:

        page["text"] = clean_text(
            page["text"]
        )

    chunks = chunk_pages(
        pages
    )

    for chunk in chunks:

        chunk["document_id"] = (
            pdf_file.stem
        )

    all_chunks.extend(
        chunks
    )

print(
    f"\nTotal Chunks: {len(all_chunks)}"
)

print(
    "\nLoading Embedding Model..."
)

model = load_embedding_model()

embeddings = model.encode(
    [
        chunk["text"]
        for chunk in all_chunks
    ]
)

print(
    "\nBuilding FAISS Index..."
)

index = build_faiss_index(
    embeddings
)

save_index(index)

save_metadata(
    all_chunks
)

print(
    "\nCorpus Build Complete"
)

print(
    f"Chunks Saved: {len(all_chunks)}"
)

print(
    f"Embedding Dimension: {embeddings.shape[1]}"
)
