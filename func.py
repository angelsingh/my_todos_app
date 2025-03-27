FILEPATH = "todoswebapp.txt"

def get_todos(filepath=FILEPATH):
    """Read the to-do items from a file and return as a list."""
    try:
        with open(filepath, 'r') as file:
            todos_local = file.readlines()
    except FileNotFoundError:
        todos_local = []  # Return an empty list if file doesn't exist
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list to a file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)