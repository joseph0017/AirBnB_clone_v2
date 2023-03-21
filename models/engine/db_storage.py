#!/usr/bin/python3
"""
module for class DBStorage 
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session


user = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
database = getenv("HBNB_MYSQL_DB")
env = getenv("HBNB_ENV")

class DBStorage():
    """class for Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine =  create_engine(
          'mysql+mysqldb://{}:{}@localhost/{}'
          .format(user, password,
                  host, database), pool_pre_ping=True)
        
    def all(self, cls=None):
        """
        returns all objects in the database
        """
        rows = []
        class_array = [User, State, City, Amenity, Place, Review]
        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}
            
        
 
    def new(self, obj):
        """add object to database"""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """commit or save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an obj"""
        if obj:
            self.__session.delete(obj)
            self.save()
            
     def reload(self):
        """Create all tables in the db"""
        if getenv("env") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        make_session = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(make_session)
        self.__session = Session()

    def close(self):
        """close"""
        self.__session.close()
