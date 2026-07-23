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
