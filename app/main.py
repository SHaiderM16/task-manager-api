from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
import os
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": True},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Submit assignment", "done": False},
]
next_id = 4  # next task ID counter


def get_task_helper(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})


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


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = get_task_helper(task_id)
    return task


@app.post("/tasks")
async def create_task(task: TaskCreate):
    global next_id

    if not task.title or task.title.strip() == "":
        raise HTTPException(400, detail={"error": "Title cannot be empty"})

    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    next_id += 1

    return new_task, 201
