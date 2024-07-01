from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    titulo: str
    descricao: str = None
    completado: bool = False

tarefa = [
    {
        "id": 1,
        "titulo": "Fazer a prova de Progamação IV",
        "descricao": "Fazer uma API em python para criar, listar, atualizar e excluir tarefas.",
        "completado": True
    }
]

def find_task(task_id: int):
    for task in tarefa:
        if task.id == task_id:
            return task
    return None

# Create
@app.post("/tarefa/", response_model=Task)
def create_task(task: Task):
    tarefa.append(task)
    return task

# Read
@app.get("/tarefa/", response_model=List[Task])
def get_tarefa():
    return tarefa

@app.get("/tarefa/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update
@app.put("/tarefa/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tarefa[tarefa.index(task)] = updated_task
    return updated_task

# Delete
@app.delete("/tarefa/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tarefa.remove(task)
    return task
