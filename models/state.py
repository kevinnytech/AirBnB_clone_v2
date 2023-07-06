#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            from .city import City
            from . import storage

            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
