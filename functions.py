def get_todos(filepath="todos.txt"):
    """Get the TO-DOs from a text file and return them as a list"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the TO-DOs to a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def add_todo(todo):
    todos = get_todos()
    todos.append(todo)
    write_todos(todos)


def delete_todo(index):
    todos = get_todos()
    todos.pop(index)
    write_todos(todos)