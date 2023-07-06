#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import Base, BaseModel
from .place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from . import HBNB_TYPE_STORAGE
from .base_model import Base
from .review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(Place, cascade='all, delete', backref='user')
        reviews = relationship(Review, cascade='all, delete', backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
