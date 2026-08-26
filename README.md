# micro-finance-api
Developed a containerized FastAPI backend to ingest and normalize fragmented transactional data from local transit and food delivery applications.

Project Structure:

[ Local Transit & Food App Exports (JSON/CSV) ]
                     |
                     | (Data Upload)
                     v
+---------------------------------------------------+
|             FASTAPI BACKEND SERVICE               |
| - RESTful Ingestion Endpoints                     |
| - Request Authentication (JWT)                    |
| - Schema Validation (Pydantic)                    |
+---------------------------------------------------+
                     |
                     v
+---------------------------------------------------+
|              NORMALIZATION ENGINE                 |
| - Vendor Name Standardization                     |
| - Item-Level Data Extraction                      |
| - Expense Categorization Algorithm                |
+---------------------------------------------------+
                     |
                     | (Structured Queries via SQLAlchemy ORM)
                     v
+---------------------------------------------------+
|              POSTGRESQL DATABASE                  |
| - Users & Accounts Tables                         |
| - Transactions Table (Foreign Keys mapping)       |
| - Categories & Merchants Tables                   |
+---------------------------------------------------+