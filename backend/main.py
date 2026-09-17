from fastapi import FastAPI

from api.routes.health import router as health_router
from api.routes.resume import router as resume_router
from api.routes.job import router as job_router


app = FastAPI(
    title="AI Job Application Agent",
    description="Backend API for AI Job Application Agent",
    version="1.0.0"
)


app.include_router(health_router)
app.include_router(resume_router)
app.include_router(job_router)