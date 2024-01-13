#!/usr/bin/python3
''' This module houses the FileStorage class '''

import os
import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    '''
    Serializes instances to a JSON file and deserializes JSON file to instances

    Private class attributes:
        - __file_path (str): path to the JSON file
        - __objects (dict): stores all objects by <class name>.id

    Public instance methods:
        - all(self): returns dictionary __objects
        - new(self, obj): sets in __objects, obj with its key
        - save(self): serializes __objects to JSON file
        - reload(self): deserializes JSON file to __objects
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary private instance __objects
        '''

        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets objs with their keys into __objects
            format: <obj class name>.id

        Args:
            obj (dict): dictionary of key/value pairs
        '''

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Saves serializes __objects to the JSON file into __file_path
        '''
        obj_dict = FileStorage.__objects
        serialized_objs = {}
        for obj in obj_dict.keys():
            serialized_objs[obj] = obj_dict[obj].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        '''
        Reloads Objects from json file
        Deserialize the JSON file specified by __file_path
        Populate the __objects dictionary with the deserialized instances.
        If the JSON file does not exist, no exception will be raised.
        '''

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                serialized_objs = json.load(f)

            for value in serialized_objs.values():
                class_name = value['__class__']
                obj = globals()[class_name](**value)
                self.new(obj)
