#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines a custom Holberton Command prompt

    Attributes:
        prompt (str): A custom prompt for Holberton
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF ends the console"""
        return True

    def emptyline(self):
        """Function empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and save to JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] in HBNBCommand.__classes:
            new_ins = eval(arg[0])()
            new_ins.save()
            print(new_ins.id)
        else:
            print("** class doesn't exist **")

def parse(arg):
    "tokenize a string to a space divided 'arguments' tuple"
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
