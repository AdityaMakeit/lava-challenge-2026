from src.embedder import load_embedding_model
from src.vector_store import (
    load_index,
    load_metadata
)

import faiss
import numpy as np


class RAGPipeline:

    def __init__(self):

        self.model = load_embedding_model()

        self.index = load_index(
            "data/index.faiss"
        )

        self.metadata = load_metadata(
            "data/metadata.json"
        )

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.model.encode(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        faiss.normalize_L2(
            query_embedding
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            if idx == -1:
                continue

            chunk = self.metadata[idx]

            results.append(
                {
                    "score": float(score),
                    **chunk
                }
            )

        return results

    def build_context(
        self,
        query,
        top_k=5
    ):

        results = self.retrieve(
            query=query,
            top_k=top_k
        )

        context = ""

        for result in results:

            context += (
                f"\n[Page {result['page']}]\n"
            )

            context += result["text"]

            context += "\n"

        return context

    def answer(
        self,
        query,
        top_k=5
    ):

        results = self.retrieve(
            query=query,
            top_k=top_k
        )

        if not results:
            return ""

        return (
            results[0]["text"]
            .replace("\n", " ")
            .strip()
        )

    def answer_with_evidence(
        self,
        query,
        top_k=5
    ):

        results = self.retrieve(
            query=query,
            top_k=top_k
        )

        if not results:

            return {
                "answer": "",
                "pages": []
            }

        answer = (
            results[0]["text"]
            .replace("\n", " ")
            .strip()
        )

        pages = sorted(
            list(
                set(
                    [
                        result["page"]
                        for result in results
                    ]
                )
            )
        )

        return {
            "answer": answer,
            "pages": pages
        }

    def search(
        self,
        query,
        top_k=5
    ):

        return self.retrieve(
            query=query,
            top_k=top_k
        )