import sqlite3
from typing import Dict, List, Optional

DB_PATH = "tasks.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = (
        sqlite3.Row
    )  # makes rows behave like dictionaries (allows row["title"] instead of row[0])
    return connection


def init_db() -> None:
    connection = get_connection()
    cursor = (
        connection.cursor()
    )  # pointer that executes SQL and moves through result set

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)

    # check if table has data
    cursor.execute("SELECT COUNT(*) AS count FROM tasks")
    row = cursor.fetchone()
    count = row["count"]  # row behaving like dictionary

    if count == 0:
        # transaction to ensure either all-or-nothing seeding
        cursor.execute("BEGIN")
        try:
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                ("Refactor assignment 1", 1),  # done = 0 represent false and vice versa
            )
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                ("Test assignment 2", 0),
            )
            cursor.execute(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                ("Submit assignment 2", 0),
            )
            connection.commit()
        except Exception:
            connection.rollback()  # rolls back all three inserts
            raise
        finally:
            connection.close()
    else:
        # table already has data
        connection.close()


def get_all() -> List[Dict]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, done FROM tasks")
    rows = cursor.fetchall()

    connection.close()
    return [dict(row) for row in rows]  # convert each row to dict and return list


def get_by_id(task_id: int) -> Optional[Dict]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = ?",  # '?' represent parameterised query which prevents SQL injection
        (task_id,),  # comma for single-element tuple
    )
    row = cursor.fetchone()

    connection.close()
    return dict(row) if row else None


def create(title: str) -> Dict:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, 0))
    connection.commit()
    new_id = cursor.lastrowid

    connection.close()
    return {"id": new_id, "title": title, "done": False}


def update(
    task_id: int, title: Optional[str] = None, done: Optional[bool] = None
) -> Optional[Dict]:
    existing = get_by_id(task_id)
    if existing is None:
        return None  # return early if task-to-update doesn't exist

    set_parts = []
    parameters = []

    if title is not None:
        set_parts.append("title = ?")
        parameters.append(title)

    if done is not None:
        set_parts.append("done = ?")
        parameters.append(1 if done else 0)

    if not set_parts:
        return existing  # return current task if no fields to update

    parameters.append(task_id)

    connection = get_connection()
    cursor = connection.cursor()

    query = f"UPDATE tasks SET {', '.join(set_parts)} WHERE id = ?"
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()

    return get_by_id(task_id)


def delete(task_id: int) -> bool:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()

    deleted = (
        cursor.rowcount > 0
    )  # cursor.rowcount returns no. of rows affected by query
    connection.close()
    return deleted
