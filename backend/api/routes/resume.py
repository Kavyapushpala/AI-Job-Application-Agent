from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.orm import Session

from database.session import get_db

from services.resume_service import upload_resume
# from services.search_service import semantic_search

from repositories.resume_repositories import (
    get_all_resumes,
    get_resume_by_id,
    delete_resume
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


# ---------------- Upload Resume ----------------

@router.post("/upload")
async def upload_resume_api(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    return await upload_resume(
        file=file,
        db=db
    )


# ---------------- Get All Resumes ----------------

#@router.get("/")
#def get_resumes(
 #   db: Session = Depends(get_db)
#):

 #   return get_all_resumes(db)


# ---------------- Semantic Search ----------------

@router.get("/search")
def search_resume(
    query: str = Query(...)
):

    results = semantic_search(query)

    return {
        "query": query,
        "matches": results
    }


# ---------------- Get Resume By ID ----------------

@router.get("/{resume_id}")
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):

    resume = get_resume_by_id(
        db,
        resume_id
    )

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


# ---------------- Delete Resume ----------------

@router.delete("/{resume_id}")
def remove_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):

    resume = delete_resume(
        db,
        resume_id
    )

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return {
        "message": "Resume deleted successfully"
    }