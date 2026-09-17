from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    return _model


def generate_embedding(text: str):
    model = get_model()

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()