# Football Stats API

A REST API built with FastAPI and MongoDB Atlas for managing football player statistics with full CRUD operations and robust data validation.

![Last Commit](https://img.shields.io/github/last-commit/Shivaa7770/FOOTBALL_STATS?style=flat-square)

## Key Features
- Production-Ready CRUD - Complete Create, Read, Update, Delete operations with proper HTTP status codes
- Cloud Database Integration - MongoDB Atlas with TLS/SSL encryption and connection health checks
- Robust Data Validation - Pydantic v2 with custom constraints: minimum length validation and non-negative integers
- Duplicate Prevention - Composite key validation on player name + club to maintain data integrity
- Auto-Generated Documentation - Interactive Swagger UI and ReDoc for API testing
- Cross-Platform SSL Fix - Resolved Mac M1/M2 certificate verification issues using certifi

## Tech Stack

| Category | Technology | Purpose |
| --- | --- | --- |
| Framework | FastAPI 0.115.5 | High-performance async REST API |
| Database | MongoDB Atlas | Cloud NoSQL with free tier |
| Validation | Pydantic v2.9.2 | Request/response data validation |
| Server | Uvicorn | ASGI server with auto-reload |
| Driver | PyMongo 4.10.1 | MongoDB official Python driver |
| SSL | certifi | Mozilla CA bundle for TLS |

## Technical Highlights

1. Error Handling: Implemented custom 400, 404, and 422 responses for duplicate entries, not found, and validation errors
2. Security: Environment variables for database credentials. .env file excluded from Git
3. Mac Compatibility: Fixed CERTIFICATE_VERIFY_FAILED error for MongoDB Atlas on macOS using tlsCAFile=certifi.where()
4. Code Quality: Separated concerns using routes, models, and database modules for maintainability

## API Endpoints

| Method | Endpoint | Description | Status Codes |
| --- | --- | --- | --- |
| GET | `/` | Health check | 200 |
| GET | `/players` | Get all players | 200 |
| POST | `/players` | Add new player | 200, 400, 422 |
| GET | `/players/{name}` | Get player by name | 200, 404 |
| PUT | `/players/{name}` | Update player stats | 200, 404, 422 |
| DELETE | `/players/{name}` | Delete player | 200, 404 |

## Setup

1. Clone repository and install dependencies:

```bash
git clone https://github.com/Shivaa7770/FOOTBALL_STATS.git
cd FOOTBALL_STATS
pip install -r requirements.txt
```

2. Create a `.env` file:

```env
MONGO_URI=your_mongodb_atlas_connection_string
```

3. Run the application:

```bash
uvicorn main:app --reload
```

4. Access API Documentation

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

## Project Structure

```text
football_stats/
├── main.py
├── database/
├── models/
├── routes/
├── services/
└── requirements.txt
```

## Sample Player Document

```json
{
  "name": "Neymar Jr",
  "club": "Santos FC",
  "country": "Brazil",
  "goals": 446,
  "assists": 257
}
```