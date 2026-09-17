import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)


resume_collection = client.get_or_create_collection(
    name="resumes"
)


job_collection = client.get_or_create_collection(
    name="jobs"
)