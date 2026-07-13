from fastapi.testclient import TestClient
from datetime import datetime

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FlyRank Backend AI Engineering Assignment 1"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"

    timestamp = data["timestamp"]
    assert datetime.fromisoformat(timestamp)


def test_api_v1_status_default(monkeypatch):
    monkeypatch.delenv(
        "ENVIRONMENT", raising=False
    )  # explicitly checking default env var

    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {
        "service": "backend-api-starter",
        "version": "1.0.0",
        "environment": "development",
    }


def test_api_v1_status_production(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "production")

    response = client.get("/api/v1/status")
    assert response.status_code == 200
    assert response.json() == {
        "service": "backend-api-starter",
        "version": "1.0.0",
        "environment": "production",
    }
