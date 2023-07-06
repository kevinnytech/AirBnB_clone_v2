#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of clas"""
        if cls is None:
            return self.__objects
        else:
            modeldict = {key: obj for key,
                         obj in self.__objects.items() if type(obj) == cls}
            return modeldict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = type(obj).__name__ + '.' + obj.id
        self.all().update({key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from ..base_model import BaseModel
        from ..user import User
        from ..place import Place
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    classname = key.split(".")[0]
                    self.all()[key] = classes[classname](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete obj from __objects if it’s inside
        if obj is equal to None, the method should do nothing
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
            self.save()

    def close(self):
        """calls reload() method for deserializing the JSON file to objects"""
        self.reload()
