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

## **System Architecture & Data Flow**:

This single-service application focuses on robust data ingestion and relational mapping. The workflow is designed to take unstructured or semi-structured export files (like JSON or CSV) from various consumer platforms and standardize them into a queryable database.

**The Ingestion Pipeline**:

**Client Upload**: A user uploads a generic data export (e.g., a CSV of Uber rides or a JSON receipt from Swiggy) via a FastAPI POST endpoint.

**Pydantic Validation**: FastAPI uses Pydantic models to validate the incoming payload, ensuring required fields like date, amount, and vendor are present before processing.

**Normalization Engine**: The Python backend parses the raw strings. It identifies the vendor (e.g., Zomato, Rapido, BlaBlaCar), extracts the specific items purchased (e.g., "Veg Thali", "Masala Dosa"), and assigns a standardized category.

**SQLAlchemy ORM**: The cleaned, structured data is mapped to Python objects.

**PostgreSQL Persistence**: The ORM handles the complex foreign-key relationships and commits the data to the relational database.

## PostgreSQL Relational Schema
To properly categorize item-level expenses and replace manual tracking, the database must separate the transaction event from the individual items purchased during that event.

1. `merchants` Table
Stores the primary vendors to prevent duplicate string entries.

id (Primary Key, UUID)

name (String) — e.g., "Swiggy", "EatSure", "Uber", "Iralipi's Kitchen"

default_category (String) — e.g., "Food Delivery", "Transit"

2. `transactions` Table
Records the top-level receipt or booking.

id (Primary Key, UUID)

merchant_id (Foreign Key -> merchants.id)

transaction_date (Timestamp)

total_amount (Decimal)

payment_method (String)

3. `transaction_items Table`
The core of the micro-expense tracker. It breaks down a single transaction into its constituent parts for granular analytics.

id (Primary Key, UUID)

transaction_id (Foreign Key -> transactions.id)

item_name (String) — e.g., "Dal-Rice combination", "Tawa Roti", "Standard Ride"

amount (Decimal)

item_category (String) — e.g., "Meals", "Groceries", "Commute"

## Core FastAPI Endpoints
The API is structured around RESTful principles, separating the ingestion routes from the analytical retrieval routes.

`POST /api/v1/ingest/transit`

Purpose: Accepts batch uploads of transit receipts (Uber, Rapido, BlaBlaCar).

Action: Triggers the transit normalization logic to map distance, duration, and fare into the transactions table.

`POST /api/v1/ingest/food`

Purpose: Accepts batch payloads from food delivery platforms (Zomato, Swiggy, EatSure).

Action: Iterates through the itemized receipt array, logging the base platform as the merchant while categorizing specific items (like Veg Thalis or Mixed Vegetable dishes) into the transaction_items table.

`GET /api/v1/analytics/spending`

Purpose: Retrieves aggregated spending data.

Query Parameters: ?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&category=Meals

Action: Executes a SQL JOIN across the three tables to return total expenditure grouped by category or merchant over a specific time period.
