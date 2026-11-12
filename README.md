# FastAPI Starter

A minimal Python API project built with FastAPI. It exposes a health-check
endpoint and a POST endpoint that accepts an integer and a string, then returns
the submitted values.

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

## Endpoints

### `GET /health1get`

Returns the service health status:

```json
{"status": "ok"}
```

### `POST /health2post`

Send a JSON request body with an integer `number` and a string `text`:

```json
{
  "number": 123,
  "text": "hello"
}
```

The response echoes the submitted values:

```json
{
  "user entered number": 123,
  "and text": "hello"
}
```

To try this endpoint in the browser, open `/docs`, choose `POST /health2post`,
select **Try it out**, enter the JSON, and select **Execute**.

Interactive API documentation is available at <http://127.0.0.1:8000/docs>
when the server is running.
