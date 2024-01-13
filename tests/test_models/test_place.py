#!/usr/bin/python3
"""Tests the Place class."""

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests the Place class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_place_type(self):
        """Tests the type of place class."""

        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")

    def test_place_instance(self):
        """Tests if a place object is an instance of Place."""

        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_superclass(self):
        """Tests if place is a subclass of BaseModel."""

        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_place_attributes(self):
        """Tests attributes of Place class."""

        attributes = {
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list
        }
        place = Place()

        for key, value in attributes.items():
            self.assertTrue(hasattr(place, key))
            self.assertEqual(type(getattr(place, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import place

        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(Place.__doc__)


if __name__ == "__main__":
    unittest.main()
