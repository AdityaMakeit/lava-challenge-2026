import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import faiss
import numpy as np

from src.embedder import load_embedding_model
from src.vector_store import (
    load_index,
    load_metadata
)


query = (
    "What were the main missions "
    "of this research project?"
)

model = load_embedding_model()

query_embedding = model.encode(
    [query]
).astype(np.float32)

faiss.normalize_L2(
    query_embedding
)

index = load_index()

scores, ids = index.search(
    query_embedding,
    3
)

metadata = load_metadata()

print("\nTOP RESULTS\n")

for score, idx in zip(
    scores[0],
    ids[0]
):

    chunk = metadata[idx]

    print(
        f"\nPage: {chunk['page']}"
    )

    print(
        f"Score: {score:.4f}"
    )

    print("-" * 40)

    print(
        chunk["text"][:500]
    )