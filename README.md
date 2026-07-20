# Backend API Starter

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?style=for-the-badge&logo=fastapi)
![uv](https://img.shields.io/badge/uv-0.11-purple?style=for-the-badge&logo=uv)
![pytest](https://img.shields.io/badge/pytest-9.1-orange?style=for-the-badge&logo=pytest)
![Ruff](https://img.shields.io/badge/Ruff-0.15-red?style=for-the-badge&logo=ruff)

A minimal FastAPI backend with health checks, service status, and a **full CRUD API** for managing tasks. Built for the FlyRank BE-01 assignment – demonstrates modern Python project structure, testing, and CI-ready practices.

## Tech Stack

- **Python** 3.14+
- **FastAPI** – modern web framework
- **uv** – fast package manager
- **pytest** – testing
- **ruff** – linting + formatting
- **pre-commit** – quality gates

## Setup

```bash
# Clone the repository
git clone https://github.com/SHaiderM16/backend-api-starter.git
cd backend-api-starter

# Install dependencies
uv sync
```

## Run

```bash
# Development server with auto-reload
uv run fastapi dev app/main.py

# Production server
uv run fastapi run app/main.py
```

## API Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/` | Root message | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/api/v1/status` | Service metadata | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks/{id}` | Get a single task | 200, 404 |
| POST | `/tasks` | Create a new task | 201, 400 |
| PUT | `/tasks/{id}` | Update a task | 200, 400, 404 |
| DELETE | `/tasks/{id}` | Delete a task | 204, 404 |

## Testing with curl

Create a new task:

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task"}'
```

Expected response:

```
HTTP/1.1 201 Created
date: Mon, 20 Jul 2026 16:56:54 GMT
server: uvicorn
content-length: 41
content-type: application/json

{"id":4,"title":"Test task","done":false}
```

List all tasks:

```bash
curl -i http://localhost:8000/tasks
```

## Swagger UI

Interactive API documentation is available at [`/docs`](http://localhost:8000/docs) when the server is running.

![Swagger UI](screenshots/swagger.png)
