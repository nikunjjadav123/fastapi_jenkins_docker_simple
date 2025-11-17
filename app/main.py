from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str

@app.get("/")
def home():
    return {"message": "FastAPI + Jenkins + Docker! This is testing"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: Todo):
    todos.append(todo)
    return {"msg": "Todo added", "todo": todo}
