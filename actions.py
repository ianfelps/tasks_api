import logging
import sqlite3
from typing import List, Optional

from models import Task

# configurar o logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# configurar o banco de dados
DATABASE_URI = "local.db"
_connection: sqlite3.Connection

# pegar o cursor do banco de dados
def get_sql_cursor(connection: Optional[sqlite3.Connection] = None) -> sqlite3.Cursor:
    global _connection
    _connection = connection or sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return _connection.cursor()

# inicializar o banco de dados (criar a tabela se ela não existir)
def init_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS task_dataset(
            task_id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            category TEXT,
            status BOOL
        );
        """
    )

# listar todas as tarefas
def read_all_tasks(cursor: sqlite3.Cursor) -> List[Task]:
    cursor.execute("SELECT * FROM task_dataset;")
    tasks = cursor.fetchall()
    return [
        Task(task_id=row[0], title=row[1], description=row[2], category=row[3], status=bool(row[4]))
        for row in tasks
    ]

# listar uma tarefa específica
def read_task_by_id(cursor: sqlite3.Cursor, task_id: int) -> Optional[Task]:
    cursor.execute("SELECT * FROM task_dataset WHERE task_id = ?;", (task_id,))
    task = cursor.fetchone()
    if task is None:
        return None
    return Task(task_id=task[0], title=task[1], description=task[2], category=task[3], status=bool(task[4]))

# adicionar uma tarefa
def write_task(
        cursor: sqlite3.Cursor, 
        task: Task, 
        connection: Optional[sqlite3.Connection] = None
    ) -> None:
    connection = _connection or connection
    if not connection:
        raise ValueError("Nenhuma conexao com o banco de dados encontrada!")
    
    query = "INSERT INTO task_dataset(title, description, category, status) VALUES (?,?,?,?)"
    values_tuple = (
        task.title,
        task.description,
        task.category,
        task.status
    )
    cursor.execute(query, values_tuple)
    connection.commit()
    logger.debug(f"{task} escrita com sucesso no DB!")

# atualizar uma tarefa
def update_task_by_id(
        cursor: sqlite3.Cursor, 
        task_id: int, 
        task: Task, 
        connection: Optional[sqlite3.Connection] = None
    ) -> None:
    connection = _connection or connection
    if not connection:
        raise ValueError("Nenhuma conexao com o banco de dados encontrada!")
    
    query = "UPDATE task_dataset SET title=?, description=?, category=?, status=? WHERE task_id=?"
    values_tuple = (
        task.title,
        task.description,
        task.category,
        task.status,
        task_id
    )
    cursor.execute(query, values_tuple)
    connection.commit()
    logger.debug(f"{task} atualizada com sucesso no DB!")

# deletar uma tarefa
def delete_task_by_id(
        cursor: sqlite3.Cursor, 
        task_id: int, 
        connection: Optional[sqlite3.Connection] = None
    ) -> None:
    connection = _connection or connection
    if not connection:
        raise ValueError("Nenhuma conexao com o banco de dados encontrada!")
    
    query = "DELETE FROM task_dataset WHERE task_id=?"
    cursor.execute(query, (task_id,))
    connection.commit()
    logger.debug(f"Tarefa com id {task_id} deletada com sucesso do DB!")
