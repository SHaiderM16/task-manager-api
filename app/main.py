from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
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


@app.get("/", summary="Root endpoint", description="Returns application's purpose")
async def root():
    return {"message": "FlyRank Backend AI Engineering Assignment 1"}


@app.get(
    "/health",
    summary="Backend server's health check",
    description="Returns status and current timestamp",
)
async def health():
    timestamp = datetime.now(timezone.utc).isoformat()

    return {"status": "ok", "timestamp": timestamp}


@app.get(
    "/api/v1/status",
    summary="App's name, version, environment",
    description="Returns application's name, version, and current development environment",
)
async def status():
    env = os.getenv("ENVIRONMENT", "development")

    return {"service": "backend-api-starter", "version": "1.0.0", "environment": env}


@app.get("/tasks", summary="List all tasks", description="Returns full list of tasks")
async def get_tasks():
    return tasks


@app.get(
    "/tasks/{task_id}",
    summary="Get single task",
    description="Returns one task by its ID",
)
async def get_task(task_id: int):
    task = get_task_helper(task_id)
    return task


@app.post(
    "/tasks", summary="Create new task", description="Adds new task to tasks list"
)
async def create_task(task: TaskCreate):
    global next_id

    if not task.title or task.title.strip() == "":
        raise HTTPException(400, detail={"error": "Title cannot be empty"})

    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    next_id += 1

    return JSONResponse(content=new_task, status_code=201)


@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates task's title and/or done status",
)
async def update_task(task_id: int, task: TaskUpdate):
    to_update_task = get_task_helper(task_id)

    if task.title is None and task.done is None:
        raise HTTPException(
            400, detail={"error": "At least one of title or done must be provided"}
        )

    if task.title is not None:
        if task.title.strip() == "":
            raise HTTPException(400, detail={"error": "Title cannot be empty"})
        to_update_task["title"] = task.title

    if task.done is not None:
        to_update_task["done"] = task.done

    return JSONResponse(content=to_update_task, status_code=200)


@app.delete(
    "/tasks/{task_id}",
    summary="Delete task",
    description="Removes task from the tasks list",
)
async def delete_task(task_id: int):
    to_delete_task = get_task_helper(task_id)
    tasks.remove(to_delete_task)
    return Response(status_code=204)
