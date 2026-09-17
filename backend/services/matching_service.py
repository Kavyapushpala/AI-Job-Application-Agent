from embeddings.embedding_service import generate_embedding

from vectorstore.matching_repository import (
    match_job_with_resumes
)


def match_job(job_description: str):

    # Generate embedding for job
    job_embedding = generate_embedding(
        job_description
    )

    # Search similar resumes
    results = match_job_with_resumes(
        job_embedding
    )

    matches = []

    if results["ids"]:

        for i in range(
            len(results["ids"][0])
        ):

            distance = results["distances"][0][i]

            similarity = 1 - distance

            matches.append({

                "resume_id":
                    results["ids"][0][i],

                "match_score":
                    round(
                        similarity * 100,
                        2
                    ),

                "metadata":
                    results["metadatas"][0][i]

            })

    return matches