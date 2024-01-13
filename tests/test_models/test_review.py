#!/usr/bin/python3
"""Tests the Review class."""

import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the Review class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_review_type(self):
        """Tests the type of Review class."""

        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

    def test_review_instance(self):
        """Tests if a review object is an instance of Review."""

        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_superclass(self):
        """Tests if review is a subclass of BaseModel."""

        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_review_attributes(self):
        """Tests attributes of Review class."""

        attributes = {
            'place_id': str,
            'user_id': str,
            'text': str
        }
        review = Review()

        for key, value in attributes.items():
            self.assertTrue(hasattr(review, key))
            self.assertEqual(type(getattr(review, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import review

        self.assertIsNotNone(review.__doc__)
        self.assertIsNotNone(Review.__doc__)


if __name__ == "__main__":
    unittest.main()
