# FastAPI Starter

A minimal Python API project built with FastAPI. It exposes one endpoint,
`GET /health`, which can be used to confirm that the service is running.

## Requirements

- Python 3.10 or newer

## Setup

Open the project folder in a terminal. In VS Code, choose **Terminal > New
Terminal**. Create and activate a virtual environment, then install the
dependencies.

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

With the virtual environment active, start the server from the project folder.
Use the command for your terminal:

macOS or Linux:

```bash
python -m uvicorn main:app --reload
```

Windows PowerShell:

```powershell
python -m uvicorn main:app --reload
```

The API is available at <http://127.0.0.1:8000>.
Press `Ctrl+C` in the terminal to stop the server.

## Endpoint

### `GET /health`

Returns the service health status:

```json
{"status": "ok"}
```

Interactive API documentation is available at <http://127.0.0.1:8000/docs>
when the server is running.
