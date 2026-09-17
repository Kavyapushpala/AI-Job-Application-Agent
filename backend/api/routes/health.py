from fastapi import APIRouter
router= APIRouter(
    tags=["Health"]
)
@router.get("/")
def home():
    return {"message": "Welcome 2 ai job application agent API!"}
@router.get("/health")
def health_check():
    return {"status": "running","message":"API is healthy"}