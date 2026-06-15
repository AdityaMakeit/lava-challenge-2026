import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.embedder import get_embedding

embedding = get_embedding(
    "PM2.5 air pollution"
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])