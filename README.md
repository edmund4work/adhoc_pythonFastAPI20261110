# Employee API

A Python API project built with FastAPI. It exposes employee listing, health
check, and example POST endpoints.

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

The API reads `DATABASE_URL` from a `.env` file in the project folder. Copy the
example file in PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the example values with the connection details for
your PostgreSQL database:

```text
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

The connection string fields are:

| Field | Description | Example |
| --- | --- | --- |
| `username` | PostgreSQL login for this API | `employee_api` |
| `password` | Password for that login | Your database password |
| `localhost` | Database server hostname or IP address | `localhost` |
| `5432` | PostgreSQL port (unless your server uses another port) | `5432` |
| `database_name` | Name of the database containing the procedure and tables | `company` |

Get these values from your PostgreSQL setup or database administrator. Use a
dedicated application login rather than a PostgreSQL superuser. It needs
permission to connect to the database, execute
`public.sp_list_employees(integer, integer, integer, integer)`, and read the
`public.employees`, `public.employees_department`, and `public.employees_status`
tables used by the procedure.

If the password contains URL-reserved characters, encode them in the
connection string (for example, `@` as `%40`, `:` as `%3A`, and `#` as `%23`).
Keep your real credentials in `.env`; that file is excluded by `.gitignore`.
Do not commit or share it. The checked-in `.env.example` contains placeholders
only.

The configured database must contain the `public.sp_list_employees` procedure.
After saving `.env`, start the server from the project folder with the virtual
environment active:

```powershell
python -m uvicorn main:app --reload
```

The API is available at <http://127.0.0.1:8000>.
Press `Ctrl+C` in the terminal to stop the server.

## Endpoints

### `POST /employees`

Calls `public.sp_list_employees` and returns its paginated JSON result. Send
filters and pagination values in a JSON body. All fields are optional; omitted
fields are passed as `NULL` so the procedure applies its own pagination
defaults.

| JSON field | Type | Description |
| --- | --- | --- |
| `department_id` | integer | Filter by department |
| `status_id` | integer | Filter by status |
| `page` | integer | Page number |
| `page_size` | integer | Number of records per page |

Example request body:

```json
{
  "department_id": 2,
  "status_id": 1,
  "page": 1,
  "page_size": 20
}
```

The response contains `page`, `page_size`, `total_records`, `total_pages`, and
`data`, as returned by the procedure.

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
