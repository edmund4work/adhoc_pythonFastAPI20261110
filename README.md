# FastAPI Starter

A minimal Python API project built with FastAPI. It exposes one endpoint,
`GET /health`, which can be used to confirm that the service is running.

## Requirements

- Python 3.10 or newer

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the API

```bash
uvicorn main:app --reload
```

The API is available at <http://127.0.0.1:8000>.

## Endpoint

### `GET /health`

Returns the service health status:

```json
{"status": "ok"}
```

Interactive API documentation is available at <http://127.0.0.1:8000/docs>
when the server is running.
