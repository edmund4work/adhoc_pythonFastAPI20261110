# Import the FastAPI class so we can create an API application.
from fastapi import FastAPI
from pydantic import BaseModel

# Create the API application. These details appear in the automatic docs.
app = FastAPI(
    title="FastAPI Starter",
    description="A minimal FastAPI project with a health-check endpoint.",
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
