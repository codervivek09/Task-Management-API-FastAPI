from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Task
@router.post("/tasks")
def create_task(task: TaskCreate,
                db: Session = Depends(get_db)):

    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()

    return {"message": "Task Created"}


# Get All Tasks
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(Task).all()

    return tasks


# Update Task
@router.put("/tasks/{task_id}")
def update_task(task_id: int,
                task: TaskUpdate,
                db: Session = Depends(get_db)):

    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        return {"message": "Task not found"}

    db_task.title = task.title
    db_task.description = task.description
    db_task.status = task.status

    db.commit()

    return {"message": "Task Updated"}


# Delete Task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int,
                db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"message": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task Deleted"}