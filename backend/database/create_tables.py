from database.base import Base
from database.connection import engine

# Import ALL models
from models.resume_model import Resume
from models.job_model import JobDescription


Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully")