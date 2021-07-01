#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """" Test cases class of Review """

    def test_pep8_review(self):
        """pep8 test.
        Makes sure the Python code is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/review.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_hasattr(self):
        new_review = Review()
        self.assertTrue(hasattr(new_review, "place_id"))
        self.assertTrue(hasattr(new_review, "user_id"))
        self.assertTrue(hasattr(new_review, "text"))

    def test_review(self):
        new_review = Review()
        self.assertIs(type(new_review.place_id), str)
        self.assertIs(type(new_review.user_id), str)
        self.assertIs(type(new_review.text), str)

    def test_inherit_Review(self):
        new_inherit = Review()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
