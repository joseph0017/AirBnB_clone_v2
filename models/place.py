#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Table, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from os import getenv


storage_type = "HBNB_TYPE_STORAGE"
if(storage_type) == "db":
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                         Column("place_id", String(60),
                                ForeignKey="places.id",
                                nullable=False),
                         Column("amenity_id", String(60),
                                ForeignKey="amenities.id",
                                nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    
    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Review
        instances with place_id equals to the current Place.id
        """
        new_list = []
        query = storage.all().items()
        for key, value in query:
            if self.id == value.place_id:
                new_list.append(value)
        return new_list
        
    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Amenity
        instances with amenity_ids equals to the current Amenity.id
        """
        new_list = []
        query = storage.all().items()
        for key, value in query:
            if self.id == value.amenity_ids:
                new_list.append(value)
        return new_list
    
    @amenities.setter
    def amenities(self, obj):
        """
        Setter attribute that handles append method for adding an Amenity.id
        to the attribute amenity_ids.
        """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
