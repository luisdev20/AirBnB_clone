#!/usr/bin/python3

from models.base_model import BaseModel


def __init__(self, file_path, objects):
    """ Instantation of Filestorage class

    Args:
        file_path (str): path to the JSON file.
        objects (dic): dictionary empty and will store all objetcs
                       by <class name>.id
    """
    self.__file_path = file_path
    self.__objects = objects
    

@property
def all(self):
    """Returns the dictionary __objects."""
    return self.__objects
    

def new(self, obj):
    """Sets in __objects the obj with key <obj class name>.id"""
    objname = obj.__class__.__name__
    self.__object["{}.{}".format(objname, obj.id)] = obj

def save(self):
    """Serializes __objects to the JSON file (path: __file_path)"""


def reload(self):
    """Deserializes the JSON file to __objects"""


