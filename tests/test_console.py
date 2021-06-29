#!/usr/bin/python3
"""Unittest for base_model()."""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestInit(unittest.TestCase):
    """Define unittest for __init__()."""

    def updated_at_is_datetime(self):
        """Test if updated_at is a datetime type."""
        self.assertEqual(type(BaseModel().created_at), datetime)

    def updated_at_is_datetime_value(self):
        """Test if updated_at is a datetime value."""
        model_1 = BaseModel()
        self.assertEqual(model_1.updated_at, datetime.today())


if __name__ == '__main__':
    unittest.main()
