def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todos_local, filepath="todos.txt"):
    with open(filepath, 'w') as file_local:
        todo_local = file_local.writelines(todos_local)


# The below block runs when function.py module has been run but other modules will not be able to run this since
# __name__ is the name of this file i.e. function in this case
if __name__ == "__main__":
    print("hello")
