#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines a custom Holberton Command prompt

    Attributes:
        prompt (str): A custom prompt for Holberton
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF ends the console"""
        return True

    def emptyline(self):
        """Function empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
