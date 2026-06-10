import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.chunker import chunk_text


text = "ABCDEFGHIJKL"

chunks = chunk_text(
    text,
    chunk_size=4
)

print(chunks)