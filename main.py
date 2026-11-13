# Read the PostgreSQL connection string from the environment.
import os

# Load project-level settings from .env when present.
from dotenv import load_dotenv

# Type hint for the JSON response returned by the employee endpoint.
from typing import Any

# PostgreSQL driver used to call the employee stored procedure.
import psycopg

# FastAPI app and HTTP error responses.
from fastapi import FastAPI, HTTPException

# Request-body validation for the /health2post example endpoint.
from pydantic import BaseModel

load_dotenv()

# Create the API application. These details appear in the automatic docs.
app = FastAPI(
    title="Employee API",
    description="A FastAPI project with employee listing and health-check endpoints.",
    version="0.1.0",
)


# Tell FastAPI to run this function when someone sends GET /health1get.
@app.get("/health1get")
def health_check() -> dict[str, str]:
    # Return a Python dictionary; FastAPI converts it to a JSON response.
    return {"status": "ok"}


class Health2PostInput(BaseModel):
    # FastAPI checks that number is an integer and text is a string.
    number: int
    text: str


# The request body must contain both number and text.
@app.post("/health2post")
def health2post(data: Health2PostInput) -> dict[str, int | str]:
    # Return the values the user submitted.
    return {"user entered number": data.number, "and text": data.text}


class EmployeeListInput(BaseModel):
    department_id: int | None = None
    status_id: int | None = None
    page: int | None = None
    page_size: int | None = None


@app.post("/employees")
def list_employees(data: EmployeeListInput) -> dict[str, Any]:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise HTTPException(status_code=503, detail="Database is not configured")

    try:
        with psycopg.connect(database_url) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "CALL public.sp_list_employees(%s, %s, %s, %s, NULL)",
                    (data.department_id, data.status_id, data.page, data.page_size),
                )
                row = cursor.fetchone()
    except psycopg.OperationalError:
        raise HTTPException(status_code=503, detail="Database is unavailable") from None
    except psycopg.Error:
        raise HTTPException(status_code=500, detail="Failed to retrieve employees") from None

    if row is None or not isinstance(row[0], dict):
        raise HTTPException(status_code=500, detail="Invalid response from employee procedure")

    return row[0]
