from pydantic import BaseModel, create_model
from typing import Optional

# criar o modelo de query
query_params = {"row_number": (int, 0)}
query_model = create_model("Query", **query_params)

# criar o modelo de resposta
class Task(BaseModel):
    task_id: Optional[int] = None
    title: str
    description: str
    category: str
    status: bool