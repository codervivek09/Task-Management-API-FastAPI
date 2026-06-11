from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user, task

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

@app.get("/")
def home():
    return {"message": "Task Management API"}