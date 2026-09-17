from sqlalchemy import text

from database.connection import engine

try:
    with engine.connect() as connection:

        result = connection.execute(text("SELECT version();"))

        print(result.fetchone())

        print("✅ Database connected successfully!")

except Exception as e:
    print("❌ Connection Failed")
    print(e)