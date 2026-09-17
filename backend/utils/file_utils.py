import os
from fastapi import UploadFile

UPLOAD_DIRECTORY = "uploads"


def create_upload_folder():
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


async def save_uploaded_file(file: UploadFile):

    create_upload_folder()

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    await file.seek(0)

    return file_path