#!/usr/bin/python3
"""Defines a User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    firstname = ""
    last_name = ""
