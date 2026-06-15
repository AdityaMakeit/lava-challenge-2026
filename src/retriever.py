from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np 

def retrieve(
        query_embeddings,
        chunk_embeddings,
        chunks,
        top_k = 3
):
    scores = cosine_similarity(
        [query_embeddings],
        chunk_embeddings
    )[0]

    results = []

    for i, score in enumerate(scores):

        results.append({
            "score":float(score),
            "page": chunks[i]["page"],
            "chunk_id": chunks[i]["chunk_id"],
            "text": chunks[i]["text"]

})

    results.sort(key=lambda x: x["score"],reverse=True)
 
    return results[:top_k]