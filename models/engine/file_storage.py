#!/usr/bin/python3
"""Define the file_storage module."""

from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """Serializes and deserializes JSON file to instances and vice

    Attributes:
        file_path (str): path to the JSON file.
        objects (dic): dictionary empty and will store all objetcs
                       by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key: <obj class name>.id"""
        objname = obj.__class__.__name__
        self.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
                                            # key: obj.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as json_f:
            json.dump(json_data, json_f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                jload = json.load(f)
                """ for i, j in jload.items():
                    if "BaseModel" in i:
                        self.__objects[i] = BaseModel(**j)
                    elif "User" in i: """
                """Here will view the update of User class"""
                """ self.__objects[i] = User(**j) """

                """
                -----------------------------------------------
                Nos quedamos aqui:
                Corregir el User deberia salir BaseModel, tmb el doble corchete ex. [User]] 
                Nos quedamos analizando el las lineas 59 y 60 por tema del diccionario.
                -------------------------------------------------
                """
                for key, obj_atr in jload.items():
                    """class_name: Call to all class"""
                    class_name = obj_atr["__class__"]
                    self.__objects[key] = eval(class_name)(**obj_atr)

        except FileNotFoundError:
            pass
