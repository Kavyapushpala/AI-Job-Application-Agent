from vectorstore.chroma_client import resume_collection


def save_embedding(
    resume_id: int,
    text: str,
    embedding: list,
    metadata: dict
):
    """
    Store resume embedding in ChromaDB
    """

    resume_collection.add(

        ids=[str(resume_id)],

        documents=[text],

        embeddings=[embedding],

        metadatas=[metadata]

    )

    print(f"✅ Resume {resume_id} stored in ChromaDB")