from embeddings.embedding_service import generate_embedding


text = """
Python developer with experience in FastAPI,
Machine Learning, PostgreSQL and React.
"""

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])