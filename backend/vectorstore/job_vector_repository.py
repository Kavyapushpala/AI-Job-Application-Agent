from vectorstore.chroma_client import job_collection


def save_job_embedding(
    job_id: int,
    text: str,
    embedding: list,
    metadata: dict
):

    job_collection.add(
        ids=[f"job_{job_id}"],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

    print(f"✅ Job {job_id} stored in ChromaDB")