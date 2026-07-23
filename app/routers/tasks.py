from fastapi import APIRouter, HTTPException
from app.services import task_service
from app.errors import NotFoundError, ValidationError
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


router = APIRouter()  # group task endpoints for API-into-modules registration


@router.get("/tasks")
def get_tasks():
    return task_service.get_all_tasks()


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return task_service.get_task_by_id(task_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail={"error": e.message})


@router.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    try:
        return task_service.create_task(payload.title)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail={"error": e.message})


@router.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdate):
    try:
        return task_service.update_task(task_id, payload.title, payload.done)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail={"error": e.message})
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail={"error": e.message})


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    try:
        task_service.delete_task(task_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail={"error": e.message})
