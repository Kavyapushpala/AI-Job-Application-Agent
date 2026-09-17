import json

from sqlalchemy.orm import Session

from models.resume_model import Resume

# ---------------- GET ALL ----------------

def get_all_resumes(db: Session):

    return db.query(Resume).all()


# ---------------- GET BY ID ----------------

def get_resume_by_id(
    db: Session,
    resume_id: int
):

    return db.query(Resume).filter(
        Resume.id == resume_id
    ).first()


# ---------------- DELETE ----------------

def delete_resume(
    db: Session,
    resume_id: int
):

    resume = db.query(Resume).filter(
        Resume.id == resume_id
    ).first()

    if resume:

        db.delete(resume)

        db.commit()

    return resume

def save_resume(
    db: Session,
    filename: str,
    parsed_resume: dict
):

    resume = Resume(

        filename=filename,

        name=parsed_resume.get("name"),

        email=parsed_resume.get("email"),

        phone=parsed_resume.get("phone"),

        skills=json.dumps(
            parsed_resume.get("skills", [])
        ),

        education=json.dumps(
            parsed_resume.get("education", [])
        ),

        projects=json.dumps(
            parsed_resume.get("projects", [])
        ),

        experience=json.dumps(
            parsed_resume.get("experience", [])
        ),

        certifications=json.dumps(
            parsed_resume.get("certifications", [])
        )

    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume