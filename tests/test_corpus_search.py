import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.rag_pipeline import RAGPipeline


rag = RAGPipeline()

queries = [
    "What were the main missions of this research project?",
    "How did this research contribute to PM2.5 policy?",
    "What publications resulted from this project?",
    "What were the key findings?",
    "Which government organizations used these results?"
]

for query in queries:

    print("\n")
    print("=" * 80)
    print("QUERY")
    print("=" * 80)
    print(query)

    results = rag.retrieve(
        query=query,
        top_k=5
    )

    print("\n")
    print("=" * 80)
    print("TOP RESULTS")
    print("=" * 80)

    for result in results:

        print(
            f"\nDocument: {result['document_id']}"
        )

        print(
            f"Page: {result['page']}"
        )

        print(
            f"Chunk: {result['chunk_id']}"
        )

        print(
            f"Score: {result['score']:.4f}"
        )

        print("-" * 40)

        print(
            result["text"][:500]
        )