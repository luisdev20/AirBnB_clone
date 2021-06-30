#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import pep8

class TestState(unittest.TestCase):
    """" Test cases class of State """

    def test_pep8_state(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/state.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_state(self):
        new_state = State()
        self.assertIs(type(new_state.name), str)

    def test_inherit_State(self):
        new_inherit = State()
        self.assertNotIsInstance(type(new_inherit), BaseModel)


if __name__ == "__main__":
    unittest.main()
