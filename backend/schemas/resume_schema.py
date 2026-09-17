from pydantic import BaseModel
from typing import Optional


class ResumeUploadResponse(BaseModel):
    filename: str
    message: str
    status: str


class ResumeParseResponse(BaseModel):
    filename: str
    extracted_text: str
    pages: int
    status: str


class ErrorResponse(BaseModel):
    status: str
    message: str