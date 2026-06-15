from sentence_transformers import SentenceTransformer


def load_embedding_model():
    """
    Load BGE-M3 embedding model.
    Returns a SentenceTransformer object.
    """

    model = SentenceTransformer("BAAI/bge-m3")

    return model


def get_embedding(text, model):
    """
    Create embedding for a single text.
    """

    return model.encode(text)


def get_embeddings(texts, model):
    """
    Create embeddings for multiple texts.
    """

    return model.encode(texts)