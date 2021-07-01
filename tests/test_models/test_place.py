#!/usr/bin/python3
"""
    This module contains test cases for base_case.py
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """" Test cases class of Place """

    def test_hasattr(self):
        new_place = Place()
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))

    def test_place(self):
        new_place = Place()
        self.assertIs(type(new_place.city_id), str)
        self.assertIs(type(new_place.user_id), str)
        self.assertIs(type(new_place.name), str)
        self.assertIs(type(new_place.description), str)
        self.assertIs(type(new_place.number_rooms), int)
        self.assertIs(type(new_place.number_bathrooms), int)
        self.assertIs(type(new_place.max_guest), int)
        self.assertIs(type(new_place.price_by_night), int)
        self.assertIs(type(new_place.latitude), float)
        self.assertIs(type(new_place.longitude), float)
        self.assertIs(type(new_place.amenity_ids), list)

    def test_inherit_Place(self):
        new_inherit = Place()
        self.assertIsInstance(new_inherit, BaseModel)


if __name__ == "__main__":
    unittest.main()
