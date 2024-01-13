#!/usr/bin/python3
"""Tests the User class."""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests the User class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_user_type(self):
        """Tests the type of User class."""

        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    def test_user_instance(self):
        """Tests if a user object is an instance of User."""

        user = User()
        self.assertIsInstance(user, User)

    def test_user_superclass(self):
        """Tests if user is a subclass of BaseModel."""

        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_user_attributes(self):
        """Tests attributes of User class."""

        attributes = {
            'email': str,
            'password': str,
            'first_name': str,
            'last_name': str
        }
        user = User()

        for key, value in attributes.items():
            self.assertTrue(hasattr(user, key))
            self.assertEqual(type(getattr(user, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import user

        self.assertIsNotNone(user.__doc__)
        self.assertIsNotNone(User.__doc__)


if __name__ == "__main__":
    unittest.main()
