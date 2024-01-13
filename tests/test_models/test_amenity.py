#!/usr/bin/python3
"""Tests the Amenity class."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_type(self):
        """Tests the type of Amenity class."""

        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")

    def test_amenity_instance(self):
        """Tests if an Amenity object is an instance of Amenity."""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_superclass(self):
        """Tests if Amenity is a subclass of BaseModel."""

        amenity = Amenity()
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_amenity_attributes(self):
        """Tests attributes of Amenity class."""

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(type(getattr(amenity, 'name', None)), str)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import amenity

        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == "__main__":
    unittest.main()
