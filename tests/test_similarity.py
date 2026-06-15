import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from src.embedder import load_embedding_model

model = load_embedding_model()

text1 = "PM2.5 air pollution"
text2 = "air quality contamination"
text3 = "football match"

emb1 = model.encode(text1)
emb2 = model.encode(text2)
emb3 = model.encode(text3)

similarity_12 = emb1 @ emb2
similarity_13 = emb1 @ emb3

print()
print("PM2.5 vs Air Quality:")
print(similarity_12)

print()
print("PM2.5 vs Football:")
print(similarity_13)