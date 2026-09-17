from fastapi import APIRouter, Depends
from fastapi import HTTPException
from fastapi import Form

from sqlalchemy.orm import Session

from database.session import get_db

from services.job_service import create_job

from services.matching_service import match_job

from repositories.job_repository import (
    get_all_jobs,
    get_job_by_id
)


router = APIRouter(
    prefix="/job",
    tags=["Job"]
)


# Create Job Description

@router.post("/create")
def create_job_api(
    title: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):

    job = create_job(
        db=db,
        title=title,
        description=description
    )

    return {
        "message": "Job description created successfully",
        "job_id": job.id,
        "title": job.title
    }


# Get All Jobs

@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):

    return get_all_jobs(db)

#Match the jobs
@router.post("/match")
def match_resumes(
    description: str = Form(...)
):

    results = match_job(
        description
    )

    return {
        "job_description": description,
        "matches": results
    }

# Get Job By ID

@router.get("/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job_by_id(
        db,
        job_id
    )

    if job is None:

        raise HTTPException(
            status_code=404,
            detail="Job description not found"
        )

    return job