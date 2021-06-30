#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.base_model import BaseModel
from models.city import City
import pep8

class TestCity(unittest.TestCase):
    """" Test cases class of City """

    def test_pep8_city(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/city.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_city(self):
        new_state = City()
        self.assertIs(type(new_state.state_id), str)
        self.assertIs(type(new_state.name), str)

    def test_inherit_City(self):
        new_inherit = City()
        self.assertNotIsInstance(type(new_inherit), BaseModel)


if __name__ == "__main__":
    unittest.main()
