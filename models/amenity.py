#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
