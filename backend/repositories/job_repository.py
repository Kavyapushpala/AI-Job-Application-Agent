from sqlalchemy.orm import Session

from models.job_model import JobDescription


def save_job(
    db: Session,
    title: str,
    description: str
):

    job = JobDescription(
        title=title,
        description=description
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_all_jobs(db: Session):

    return db.query(JobDescription).all()


def get_job_by_id(
    db: Session,
    job_id: int
):

    return db.query(
        JobDescription
    ).filter(
        JobDescription.id == job_id
    ).first()