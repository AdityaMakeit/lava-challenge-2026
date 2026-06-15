import os
import json
import faiss
import numpy as np


def build_faiss_index(chunk_embeddings):

    embeddings = np.array(
        chunk_embeddings,
        dtype=np.float32
    )

    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(embeddings)

    return index


def save_index(
    index,
    path="data/index/faiss.index"
):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    faiss.write_index(
        index,
        path
    )


def load_index(
    path="data/index/faiss.index"
):

    return faiss.read_index(
        path
    )


def save_metadata(
    chunks,
    path="data/index/metadata.json"
):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_metadata(
    path="data/index/metadata.json"
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)