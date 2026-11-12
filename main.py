from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    description="A minimal FastAPI project with a health-check endpoint.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
