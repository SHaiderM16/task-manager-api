from fastapi import FastAPI
from app.routers import tasks
from app.repositories import task_repository as repo

app = FastAPI()

repo.init_db()

app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "FlyRank Backend AI Engineering Assignment 2"}
