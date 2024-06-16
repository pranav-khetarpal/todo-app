from typing import Optional
from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
