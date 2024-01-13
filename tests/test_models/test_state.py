#!/usr/bin/python3
"""Tests the State class."""

import unittest
from models.state import State
from models.engine.file_storage import FileStorage
import os
"""from models import storage"""
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests the State class."""

    def setUp(self):
        """Does nothing"""
        pass

    def tearDown(self):
        """Resets storage."""

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_state_type(self):
        """Tests the type of State class."""

        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")

    def test_state_instance(self):
        """Tests if a state object is an instance of State."""

        state = State()
        self.assertIsInstance(state, State)

    def test_state_superclass(self):
        """Tests if state is a subclass of BaseModel."""

        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_state_attributes(self):
        """Tests attributes of state class."""

        attributes = {
            'name': str
        }
        state = State()

        for key, value in attributes.items():
            self.assertTrue(hasattr(state, key))
            self.assertEqual(type(getattr(state, key, None)), value)


class TestDocumentation(unittest.TestCase):
    """Tests for existence of docstrings"""

    def test_documentation(self):
        """Tests if the module, the class,
        and the methods are documented"""

        from models import state

        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(State.__doc__)


if __name__ == "__main__":
    unittest.main()
