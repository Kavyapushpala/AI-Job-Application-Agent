from embeddings.embedding_service import generate_embedding
from vectorstore.search_repository import search_resumes


def semantic_search(query: str):

    embedding = generate_embedding(query)

    results = search_resumes(embedding)

    formatted_results = []

    if results["ids"]:

        for i in range(len(results["ids"][0])):

            formatted_results.append({

                "resume_id": results["ids"][0][i],

                "similarity": round(
                    1 - results["distances"][0][i],
                    3
                ),

                "metadata": results["metadatas"][0][i]

            })

    return formatted_results