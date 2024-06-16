import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'todo_model.dart'; // Adjust the import according to your actual file structure

class TodoTile extends StatelessWidget {
  // The TodoModel object containing the information for the ToDo
  final TodoModel todo;
  final Function(TodoModel) updateTodo;
  final Function(TodoModel) deleteTodo;
  final Function(bool?) onChanged;

  const TodoTile({
    super.key,
    required this.todo,
    required this.updateTodo,
    required this.deleteTodo,
    required this.onChanged,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(left: 25.0, right: 25.0, top: 25.0),
      child: Slidable(
        endActionPane: ActionPane(
          motion: const StretchMotion(),
          children: [
            SlidableAction(
              onPressed: (context) => deleteTodo(todo),
              icon: Icons.delete,
              backgroundColor: Colors.red.shade300,
              borderRadius: BorderRadius.circular(12),
            ),
            SlidableAction(
              onPressed: (context) => updateTodo(todo),
              icon: Icons.edit,
              backgroundColor: Colors.blue.shade300,
              borderRadius: BorderRadius.circular(12),
            ),
          ],
        ),
        child: Container(
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: [
              BoxShadow(
                color: Colors.grey.withOpacity(0.5),
                spreadRadius: 1,
                blurRadius: 5,
                offset: const Offset(0, 3),
              ),
            ],
          ),
          child: Row(
            children: [
              Checkbox(
                value: todo.completed,
                onChanged: onChanged,
              ),
              Expanded(
                child: Text(
                  todo.title,
                  style: TextStyle(
                    decoration: todo.completed ? TextDecoration.lineThrough : null,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
