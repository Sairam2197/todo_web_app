FILEPATH = "todo_list.txt"
def read_file(filepath=FILEPATH):
    """ Reads a text file and returns the context of the file"""
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_file(todo_list_arg, filepath=FILEPATH):
    """ Writes something into the file.txt """
    with open(filepath, 'w') as file:
        file.writelines(todo_list_arg)