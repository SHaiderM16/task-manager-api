from app.errors import NotFoundError, ValidationError
from app.repositories import task_repository as repo


def get_all_tasks():
    return repo.get_all()


def get_task_by_id(task_id: int):
    task = repo.get_by_id(task_id)
    if task is None:
        raise NotFoundError("Task", task_id)
    return task


def create_task(title: str):
    title = title.strip()
    if not title:
        raise ValidationError("Title cannot be empty")
    return repo.create(title)


def update_task(task_id: int, title: str | None = None, done: bool | None = None):
    if title is None and done is None:
        raise ValidationError("At least one field must be provided")

    if title is not None:
        title = title.strip()
        if not title:
            raise ValidationError("Title cannot be empty")

    updated = repo.update(task_id, title, done)
    if updated is None:
        raise NotFoundError("Task", task_id)
    return updated


def delete_task(task_id: int):
    if not repo.delete(task_id):
        raise NotFoundError("Task", task_id)
    return True
