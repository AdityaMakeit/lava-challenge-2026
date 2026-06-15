import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.rag_pipeline import RAGPipeline


rag = RAGPipeline()

question = (
    "What were the main missions of this research project?"
)

answer = rag.answer(
    question
)

print("\nANSWER\n")
print(answer)