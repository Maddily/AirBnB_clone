#!/usr/bin/python3
''' This module houses the FileStorage class '''

import os
import json


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

        from models.base_model import BaseModel

        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets objs with their keys into __objects
            format: <obj class name>.id

        Args:
            obj (dict): dictionary of key/value pairs
        '''

        from models.base_model import BaseModel

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        Saves serializes __objects to the JSON file into __file_path
        '''

        from models.base_model import BaseModel

        serialized_objs = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        '''
        Reloads Objects from json file
        Deserialize the JSON file specified by __file_path
        Populate the __objects dictionary with the deserialized instances.
        If the JSON file does not exist, no exception will be raised.
        '''

        from models.base_model import BaseModel

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                serialized_objs = json.load(f)

            for key, obj_dict in serialized_objs.items():
                class_name = obj_dict['__class__']
                FileStorage.__objects[key] = eval(class_name)(**obj_dict)
