#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os




class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """
        getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import storage
        from models.city import City
        city_list = []
        get_cities = storage.all(City).items
        for key, value in get_cities:
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
