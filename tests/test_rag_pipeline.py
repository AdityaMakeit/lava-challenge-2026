import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.rag_pipeline import RAGPipeline


rag = RAGPipeline()

query = (
    "What were the main missions "
    "of this research project?"
)

results = rag.retrieve(
    query,
    top_k=3
)

print("\nTOP RESULTS")

for result in results:

    print("\n")
    print("=" * 80)

    print(
        f"Page: {result['page']}"
    )

    print(
        f"Score: {result['score']:.4f}"
    )

    print("-" * 40)

    print(
        result["text"][:1000]
    )

print("\n")
print("=" * 80)
print("CONTEXT")
print("=" * 80)

print(
    rag.build_context(
        query,
        top_k=3
    )
)