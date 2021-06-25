#!/usr/bin/python3
"""Represents the base model to all classes for this project."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines a Base Model class to main methods."""

    def __init__(self, *args, **kwargs):
        """Initialize public attributes

        Args:
        updated_at (time): assign current datetime when instance is created.
                       and will be updated every time you change your object.
        id (str): Generate a random UUID
        created_at (time): Assign current datetime when instance is created.
        """

        self.updated_at = datetime.today()
        self.id = str(uuid4())
        self.created_at = datetime.today()

    def __str__(self):
        """Return the human readable string format."""
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute with the current datetime"""
        return self.updated_at

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dic = self.__dict__
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
