import logging
from fastapi import FastAPI, HTTPException
import sqlite3
import uvicorn

from actions import *
from models import Task

# configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# criar a API
app = FastAPI()

# criar o cursor para o banco de dados
cursor:sqlite3.Cursor

# inicializar o banco de dados junto a api
@app.on_event("startup")
def get_or_create_db():
    global cursor
    cursor = get_sql_cursor()
    init_db(cursor=cursor)

# criar rota padrao (home page)
@app.get("/")
async def home():
    return {"message": "Bem-vindo ao Tasks API!"}

# criar rota para listar todas as tarefas
@app.get("/tasks", response_model=List[Task])
async def get_all_tasks():
    try:
        cursor = get_sql_cursor()
        tasks = read_all_tasks(cursor)
        return tasks
    except sqlite3.Error as e:
        logger.error(f"Erro no banco de dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")

# criar rota para listar uma tarefa específica
@app.get("/tasks/{id}")
async def get_task_by_id(id: int):
    try:
        cursor = get_sql_cursor()
        task = read_task_by_id(cursor, id)
        return task
    except sqlite3.Error as e:
        logger.error(f"Erro no banco de dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")

# criar rota para adicionar uma tarefa
@app.post("/tasks")
async def add_task(task: Task):
    try:
        cursor = get_sql_cursor()
        write_task(cursor, task)
        return {"message": "Tarefa adicionada com sucesso!"}
    except sqlite3.Error as e:
        logger.error(f"Erro no banco de dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")

# criar rota para atualizar uma tarefa
@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    try:
        cursor = get_sql_cursor()
        update_task_by_id(cursor, id, task)
        return {"message": "Tarefa atualizada com sucesso!"}
    except sqlite3.Error as e:
        logger.error(f"Erro no banco de dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")

# criar rota para deletar uma tarefa
@app.delete("/tasks/{id}")
async def delete_task(id: int):
    try:
        cursor = get_sql_cursor()
        delete_task_by_id(cursor, id)
        return {"message": "Tarefa deletada com sucesso!"}
    except sqlite3.Error as e:
        logger.error(f"Erro no banco de dados: {e}")
        raise HTTPException(status_code=500, detail="Erro ao acessar o banco de dados.")

# modulo de inicialização para rodar a api localmente
if __name__ == "__main__":
    uvicorn.run(app, port=8000)

# uvicorn main:app --reload
