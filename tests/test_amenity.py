#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pep8

class TestAmenity(unittest.TestCase):
    """" Test cases class of City """

    def test_pep8_city(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/amenity.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

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
