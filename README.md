# Backend API Starter

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?style=for-the-badge&logo=fastapi)
![uv](https://img.shields.io/badge/uv-0.11-purple?style=for-the-badge&logo=uv)
![pytest](https://img.shields.io/badge/pytest-9.1-orange?style=for-the-badge&logo=pytest)
![Ruff](https://img.shields.io/badge/Ruff-0.15-red?style=for-the-badge&logo=ruff)

A minimal FastAPI backend with health checks and service status endpoints. Built for the FlyRank BE-01 assignment – demonstrates modern Python project structure, testing, and CI-ready practices.

## Tech Stack

- **Python** 3.14+
- **FastAPI** – modern web framework
- **uv** – fast package manager
- **pytest** – testing
- **ruff** – linting + formatting
- **pre-commit** – quality gates

## Why FastAPI?

FastAPI provides:
- Automatic OpenAPI documentation (`/docs`)
- Pydantic validation (useful for future AI/ML work)
- Native async support
- Built-in dependency injection

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

## Test

```bash
uv run pytest -v
```

## Lint & Format

```bash
# Lint
uv run ruff check

# Format
uv run ruff format
```

## API Endpoints

| Method | Endpoint | Description | Example Response |
|--------|----------|-------------|------------------|
| GET | `/` | Root message | `{"message": "FlyRank Backend AI Engineering Assignment 1"}` |
| GET | `/health` | Health check | `{"status": "ok", "timestamp": "2026-07-13T08:55:53+00:00"}` |
| GET | `/api/v1/status` | Service metadata | `{"service": "backend-api-starter", "version": "1.0.0", "environment": "development"}` |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ENVIRONMENT` | `development` | Runtime environment (development, staging, production) |
