#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """" Test cases class of City """

    def test_hasattr(self):
        new_city = City()
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "name"))

    def test_city(self):
        new_state = City()
        self.assertIs(type(new_state.state_id), str)
        self.assertIs(type(new_state.name), str)

    def test_hasattr(self):
        new_city = City()
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertTrue(hasattr(new_city, "name"))

    def test_inherit_City(self):
        new_inherit = City()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
