#!/usr/bin/python3
"""Tests the City class."""

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_city_type(self):
        """Tests the type of city class."""

        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")

    def test_city_instance(self):
        """Tests if a city object is an instance of city."""

        city = City()
        self.assertIsInstance(city, City)

    def test_city_superclass(self):
        """Tests if city is a subclass of BaseModel."""

        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_city_attributes(self):
        """Tests attributes of city class."""

        attributes = {
            'name': str,
            'state_id': str
        }
        city = City()

        for key, value in attributes.items():
            self.assertTrue(hasattr(city, key))
            self.assertEqual(type(getattr(city, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import city

        self.assertIsNotNone(city.__doc__)
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
