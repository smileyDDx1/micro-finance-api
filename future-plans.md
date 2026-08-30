1. add code review tool - like code-rabbit
2. V2 updates:
The five core dependencies currently in your requirements.txt are sufficient to launch a minimal viable product using Python's standard library for regular expressions and environment variables. 
However, adding four specific tools will elevate the architecture to an enterprise standard and directly support the testing experience required for a backend developer interview.

a.Alembic (Database Migrations): Currently, Base.metadata.create_all builds tables from scratch on startup, but it cannot safely alter them if you add or modify a column later. 
Alembic is the industry-standard migration tool for SQLAlchemy that tracks and applies schema changes without wiping your existing PostgreSQL data.

b.pydantic-settings (Environment Management): While Python's built-in os.getenv() works, pydantic-settings is the FastAPI standard for securely loading, parsing, and validating environment variables (like the database connection string) directly from a local .env file.

c.thefuzz (Normalization Logic): Raw transactional data from platforms like Swiggy, Zomato, or Uber is often inconsistent or misspelled. 
thefuzz utilizes Levenshtein distance for fuzzy string matching, allowing the normalization engine to confidently assign variations to the correct standardized merchant record.

d.pytest & httpx (Testing): pytest structures unit tests to check the functionalities of backend components, while httpx serves as the asynchronous test client that pings the FastAPI endpoints, proving high availability and reliable code execution.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------