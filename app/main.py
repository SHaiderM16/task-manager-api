from fastapi import FastAPI
from datetime import datetime, timezone
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FlyRank Backend AI Engineering Assignment 1"}


@app.get("/health")
async def health():
    timestamp = datetime.now(timezone.utc).isoformat()

    return {"status": "ok", "timestamp": timestamp}


@app.get("/api/v1/status")
async def status():
    env = os.getenv("ENVIRONMENT", "development")

    return {"service": "backend-api-starter", "version": "1.0.0", "environment": env}
