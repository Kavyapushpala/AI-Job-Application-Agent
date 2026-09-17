from sqlalchemy.orm import Session

from repositories.job_repository import save_job

from embeddings.embedding_service import generate_embedding

from vectorstore.job_vector_repository import save_job_embedding


def create_job(
    db: Session,
    title: str,
    description: str
):

    # 1. Save job in PostgreSQL
    job = save_job(
        db=db,
        title=title,
        description=description
    )

    # 2. Generate embedding
    embedding = generate_embedding(description)

    # 3. Store embedding in ChromaDB
    save_job_embedding(
        job_id=job.id,
        text=description,
        embedding=embedding,
        metadata={
            "title": title
        }
    )

    return job