from fastapi import UploadFile
from sqlalchemy.orm import Session
from embeddings.embedding_service import generate_embedding
from vectorstore.vector_repository import save_embedding
from utils.validators import (
    validate_file_size,
    validate_file_type
)

from utils.file_utils import save_uploaded_file
from utils.pdf_reader import extract_text_from_pdf

# Use whichever parser you're currently using
from services.gemini_parser import parse_resume_with_gemini
# OR
# from services.parser_service import parse_resume

from repositories.resume_repositories import save_resume


async def upload_resume(
    file: UploadFile,
    db: Session
):

    validate_file_type(file)
    await validate_file_size(file)

    file_path = await save_uploaded_file(file)

    extracted_text, pages = extract_text_from_pdf(file_path)

    # Gemini Parser
    parsed_resume = parse_resume_with_gemini(extracted_text)

    # If you're still using regex:
    # parsed_resume = parse_resume(extracted_text)

    saved_resume = save_resume(
        db=db,
        filename=file.filename,
        parsed_resume=parsed_resume
    )

    embedding = generate_embedding(extracted_text)

    save_embedding(

    resume_id=saved_resume.id,

    text=extracted_text,

    embedding=embedding,

    metadata={
        "filename": file.filename,
        "candidate_name": parsed_resume.get("name")
    }

)

    return {
        "message": "Resume uploaded successfully",
        "resume_id": saved_resume.id,
        "filename": saved_resume.filename,
        "resume_data": parsed_resume
    }