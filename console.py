#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
import models

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
        arg_sp = arg.split()
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] in HBNBCommand.__classes:
            new_ins = eval(arg_sp[0])()
            models.storage.save()
            print(new_ins.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        dic_objects = models.storage.all()

        arg_sp = arg.split()
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_sp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_sp[0],arg_sp[1]) in dic_objects.keys():
            print(dic_objects["{}.{}".format(arg_sp[0],arg_sp[1])])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id. Update the json file."""
        dic_objects = models.storage.all()

        arg_sp = arg.split()
        if len(arg_sp) == 0:
            print("** class name missing **")
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_sp) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_sp[0],arg_sp[1]) in dic_objects.keys():
            del dic_objects["{}.{}".format(arg_sp[0],arg_sp[1])]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances.
        
        Args (optional): 
            Class_name: to print instances of the given classname
        """
        dic_objects = models.storage.all()
        arg_sp = arg.split()
        ouput_str = []

        if len(arg_sp) == 0:
            # imprimir todas las intancias de TODAS las clases
            for objs in dic_objects.values():
                ouput_str.append(objs.__str__())
            print(ouput_str) # Imprime la direccion de la clase
        elif arg_sp[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            # imprimir las instancias UNICAMENTE de la clase dada
        #   elif "{}".format(arg_sp[0]) in dic_objects.keys():
        #   print(dic_objects["{}".format(arg_sp[0])])
        else:
            for objs in dic_objects.values():
                if arg_sp[0] == objs.__class__.__name__:
                    ouput_str.append(objs.__str__())
            print(ouput_str)

def parse(arg):
    "tokenize a string to a sSpace divided 'arguments' tuple"
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
