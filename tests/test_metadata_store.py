import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.metadata_store import (
    save_metadata,
    load_metadata
)

sample = [
    {
        "document_id": "test",
        "page": 1,
        "chunk_id": 0,
        "char_count": 100,
        "text": "Hello World"
    }
]

save_metadata(
    sample,
    "data/test_metadata.json"
)

loaded = load_metadata(
    "data/test_metadata.json"
)

print(loaded)