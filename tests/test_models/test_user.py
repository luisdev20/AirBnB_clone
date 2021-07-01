#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """" Test cases class of User """

    def test_hasattr(self):
        new_user = User()
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))

    def test_user(self):
        new_user = User()
        self.assertIs(type(new_user.email), str)
        self.assertIs(type(new_user.password), str)
        self.assertIs(type(new_user.first_name), str)
        self.assertIs(type(new_user.last_name), str)

    def test_inherit_User(self):
        new_inherit = User()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
