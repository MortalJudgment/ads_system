# Backend for Ads System

This is the backend for the Ads System, built using FastAPI, PostgreSQL, and SQLAlchemy.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Docker](#docker)
- [API Documentation](#api-documentation)
- [Database Configuration](#database-configuration)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/ads-system.git
    cd ads-system/backend
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Set up the database:**

    Ensure PostgreSQL is running. You can use Docker to start a PostgreSQL container:

    ```sh
    docker run --name ads-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=thefallingsky195 -e POSTGRES_DB=ads_db -p 5432:5432 -d postgres:15
    ```

2. **Run the FastAPI application:**

    ```sh
    uvicorn app.main:app --reload
    ```

    The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Testing

To run the tests, use `pytest`:

```sh
pytest tests
```

## Docker
1. Build the Docker image:

```sh
docker build -t ads-backend .
```
2. Run the Docker container:

```sh
docker run -d --name ads-backend-container -p 8000:8000 ads-backend
```

The application will be available at http://127.0.0.1:8000.

## API Documentation
- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

## Database Configuration
The database configuration is set in app/database.py. Update the SQLALCHEMY_DATABASE_URL to match your PostgreSQL configuration:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:thefallingsky195@localhost:5432/ads_db"
```