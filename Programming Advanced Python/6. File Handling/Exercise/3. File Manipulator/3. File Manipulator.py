import os
from os import path

ERROR_MESSAGE = "An error occurred"


def create_command(file_name):
    open(file_name, "w").close()


def add_command(*args):
    with open(args[0], "a") as file:
        file.write(args[1])
        file.write('\n')


def replace_command(*args):
    if path.exists(args[0]):

        old_string = args[1]
        new_string = args[2]

        with open(args[0], "r+") as file:
            content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(content)
    else:
        print(ERROR_MESSAGE)


def delete_command(file_name):
    if path.exists(file_name):
        os.remove(file_name)
    else:
        print(ERROR_MESSAGE)


while True:
    command = input()
    if command == "End":
        break

    command_args = command.split("-")

    if command_args[0] == "Create":
        create_command(command_args[-1])

    elif command_args[0] == "Add":
        add_command(*command_args[1:])

    elif command_args[0] == "Replace":
        replace_command(*command_args[1:])

    elif command_args[0] == "Delete":
        delete_command(command_args[-1])
