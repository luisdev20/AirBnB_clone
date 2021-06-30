#!/usr/bin/python3
"""Represents the base model to all classes for this project."""

from uuid import uuid4
from datetime import datetime
import models


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

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, date)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the human readable string representation format."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
