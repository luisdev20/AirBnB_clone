#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """" Test cases class of State """

    def test_hasattr(self):
        new_state = State()
        self.assertTrue(hasattr(new_state, "name"))

    def test_state(self):
        new_state = State()
        self.assertIs(type(new_state.name), str)

    def test_inherit_State(self):
        new_inherit = State()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
