#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter."""

import re
import cmd
import models
from shlex import split
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines a custom Holberton Command prompt

    Attributes:
        prompt (str): A custom prompt for Holberton
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF ends the console"""
        print(" ")
        return True

    def emptyline(self):
        """Function empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and save to JSON file"""
        arg_sp = split(arg)
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] in HBNBCommand.__classes:
            # Creamos nueva instancia de la forma NombreInstancia()
            print(eval(arg_sp[0])().id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        dic_objects = models.storage.all()
        arg_sp = split(arg)
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_sp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_sp[0], arg_sp[1]) in dic_objects.keys():
            print(dic_objects["{}.{}".format(arg_sp[0], arg_sp[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Update the json file."""
        dic_objects = models.storage.all()
        arg_sp = split(arg)
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_sp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_sp[0], arg_sp[1]) in dic_objects.keys():
            del dic_objects["{}.{}".format(arg_sp[0], arg_sp[1])]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances.

        Args (optional):
            Class_name: to print instances of the given classname
        """
        dic_objects = models.storage.all()
        arg_sp = split(arg)
        ouput_str = []
        if len(arg_sp) == 0:
            # imprimir todas las intancias de TODAS las clases
            for objs in dic_objects.values():
                ouput_str.append(objs.__str__())
            print(ouput_str)
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for objs in dic_objects.values():
                if arg_sp[0] == objs.__class__.__name__:
                    ouput_str.append(objs.__str__())
            print(ouput_str)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by add or update attribs.
        Save the change into the JSON file

        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """

        arg_sp = split(arg)
        # arg_sp = arg.split()
        dic_objects = models.storage.all()

        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_sp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_sp[0], arg_sp[1]) not in dic_objects.keys():
            print("** no instance found **")
        elif len(arg_sp) == 2:
            print("** attribute name missing **")
        elif len(arg_sp) == 3:
            print("** value missing **")
        else:
            format_key = "{}.{}".format(arg_sp[0], arg_sp[1])
            objeto = dic_objects[format_key]
            if len(arg_sp[3].split()) == 1:
                try:
                    setattr(objeto, arg_sp[2], eval(arg_sp[3]))
                except NameError or ValueError:
                    setattr(objeto, arg_sp[2], arg_sp[3])
            else:
                setattr(objeto, arg_sp[2], arg_sp[3])
            objeto.save()

    def do_count(self, arg):
        # return self.do_all(arg).keys().count()
        dic_objects = models.storage.all()
        arg_sp = split(arg)
        counter = 0
        for objs in dic_objects.values():
            if arg_sp[0] == objs.__class__.__name__:
                counter += 1
        print(counter)

    def default(self, arg):

        functions = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }

        arg = (arg.replace("(", ".").replace(")", ".")
               .replace('"', "").replace(",", "").split("."))
        try:
            cmd_arg = arg[0] + " " + arg[2]
            func = functions[arg[1]]
            func(cmd_arg)
        except Exception:
            print("*** Unknown syntax:", arg[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
