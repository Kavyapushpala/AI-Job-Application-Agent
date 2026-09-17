from vectorstore.chroma_client import resume_collection


def search_resumes(query_embedding, n_results=5):
    """
    Search the most similar resumes from ChromaDB
    """

    results = resume_collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results