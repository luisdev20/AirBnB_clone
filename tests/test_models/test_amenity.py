#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """" Test cases class of City """

    def test_hasattr(self):
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))

    def test_amenity(self):
        new_amenity = Amenity()
        self.assertIs(type(new_amenity.name), str)

    def test_inherit_amenity(self):
        new_inherit = Amenity()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
