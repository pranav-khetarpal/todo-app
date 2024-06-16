from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from crud import get_todos, create_todo, update_todo, delete_todo
from models import TodoItem
from schemas import TodoCreate

app = FastAPI()

# Add CORS middleware to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/read", response_model=List[TodoItem])
def read_todos() -> List[TodoItem]:
    """
    Endpoint to read all todos
    """
    # just need to return a list of todos
    return get_todos()

@app.post("/create", response_model=TodoItem)
def add_todo(todo: TodoCreate) -> TodoItem:
    """
    Endpoint to create a new todo
    """
    # add the todo to the end of the json file
    number_of_todos = len(get_todos()) + 1
    new_todo = TodoItem(id=number_of_todos, **todo.model_dump())
    create_todo(new_todo)
    return new_todo

@app.put("/update/{todo_id}", response_model=TodoItem)
def edit_todo(todo_id: int, todo: TodoCreate) -> TodoItem:
    """
    Endpoint to update an existing todo
    """
    # Check to see if the todo exists, and if so, update its contents
    existing_todos = get_todos()
    for existing_todo in existing_todos:
        if existing_todo['id'] == todo_id:
            updated_todo = TodoItem(id=todo_id, **todo.model_dump())
            update_todo(todo_id, updated_todo)
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/delete/{todo_id}")
def remove_todo(todo_id: int):
    """
    Endpoint to delete a todo
    """
    # remove the todo from the .json file
    delete_todo(todo_id)
    return {'message': 'Todo deleted successfully'}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
