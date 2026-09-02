import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Reads the DATABASE_URL environment variable provided by docker-compose
DATABSE_URL = os.getenv(
    'DATABASE_URL',
    'postgres://postgres:postgres@localhost:5432/postgres' ### this is dummy data
    )
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """FastAPI dependency to provide a database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()