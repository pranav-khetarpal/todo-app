from typing import List, Dict
from models import TodoItem
from database import load_data, save_data

def get_todos() -> List[Dict]:
    return load_data()

def create_todo(todo: TodoItem):
    data = load_data()
    data.append(todo.model_dump())
    save_data(data)

def update_todo(id: int, todo: TodoItem):
    data = load_data()
    for index, item in enumerate(data):
        if item['id'] == id:
            data[index] = todo.model_dump()
            break
    save_data(data)

def delete_todo(id: int):
    data = load_data()
    data = [item for item in data if item['id'] != id]
    save_data(data)
