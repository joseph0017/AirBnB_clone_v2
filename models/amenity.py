#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv

class Amenity(BaseModel):
    """
    class for Amennity,
    inherits from BaseModel and Base
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place ", secondary="place_amenity",
                                       back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
=======


class Amenity(BaseModel):
    name = ""
>>>>>>> parent of 85cab16... Update amenity.py
