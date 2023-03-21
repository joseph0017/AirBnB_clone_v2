#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Table, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage
from models.city import City

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                           cascade="all, delete-orphan")
    
    @property
    def cities(self):
        """returns list of city instances"""
        get_cities = storgae.all(City).items()
        for key, value in get_cities:
            if value.state_id == self.id:
                return value
