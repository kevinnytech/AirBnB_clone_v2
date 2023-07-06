#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from . import HBNB_TYPE_STORAGE
from sqlalchemy.ext.declarative import declarative_base
if HBNB_TYPE_STORAGE == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key not in ['__class__']:
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from . import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        if HBNB_TYPE_STORAGE == 'db':
            dictionary = self.__dict__.copy()
            if '_sa_instance_state' in self.__dict__:
                del dictionary['_sa_instance_state']
            return dictionary
        else:
            for key, value in self.__dict__.items():
                if key == 'created_at' or key == 'updated_at':
                    value = value.isoformat()
                dictionary[key] = value
            dictionary['__class__'] = type(self).__name__
            return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from . import storage
        storage.delete(self)
