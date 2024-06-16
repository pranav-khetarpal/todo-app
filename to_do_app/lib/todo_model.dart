/*
This is the basic model of stock, needed for displaying characteristics about its current price
*/
class TodoModel {
  final int id;
  String title;
  String? description;
  bool completed;

  TodoModel({
    required this.id, 
    required this.title,
    this.description,
    required this.completed,
  });

  factory TodoModel.fromJson(Map<String, dynamic> json) {
    return TodoModel(
      id: json['id'],
      title: json['title'],
      description: json['description'],
      completed: json['completed'],
    );
  }

  // Method to convert a Stock instance to a JSON map
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'completed': completed,
    };
  }
}
