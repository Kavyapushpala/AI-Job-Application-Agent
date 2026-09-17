from vectorstore.chroma_client import resume_collection


def match_job_with_resumes(
    job_embedding,
    n_results=5
):

    results = resume_collection.query(
        query_embeddings=[job_embedding],
        n_results=n_results
    )

    return results