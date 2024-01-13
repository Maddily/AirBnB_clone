#!/usr/bin/python3
''' This is the module for the BaseModel Class '''

import uuid
from datetime import datetime


class BaseModel:
    '''
    This class deinfes all common attributes for other classes

    Public Instance Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The timestamp when the instance was created.
        updated_at (datetime): The timestamp when the instance was last updated
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor: Initializes an instance of the BaseModel class.

        Args:
            args (any) - Unused
            kwargs (dict) - Key/Value arguments
        '''
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        Return:
            A string representation of the instance in the format:
            "[ClassName] (uuid) {key1: value1, ...}"
        '''
        return "[{}] ({}) {}".format((self.__class__.__name__),
                                     self.id, self.__dict__)

    def save(self):
        '''
        Updates the public instance attribute
        'updated_at' with current datetime

        Saves instances
        '''

        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Return:
            A dict containing all key/values of __dict__ of the instance.
        '''
        full_dictionary = self.__dict__.copy()
        full_dictionary["created_at"] = self.created_at.isoformat()
        full_dictionary["updated_at"] = self.updated_at.isoformat()
        full_dictionary['__class__'] = self.__class__.__name__
        return full_dictionary
