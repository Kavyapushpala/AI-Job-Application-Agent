from fastapi import UploadFile, HTTPException

ALLOWED_EXTENSIONS = [".pdf"]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_file_type(file: UploadFile):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )


async def validate_file_size(file: UploadFile):
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 5 MB."
        )

    await file.seek(0)