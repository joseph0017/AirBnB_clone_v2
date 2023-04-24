#!/usr/bin/python3
"""Module New engine DBstorage class"""
from os import getenv
from sqlalchemy import create_engine, MetaData

user = getenv("HBNB_MYSQL_USER")
password = getenv("HBNB_MYSQL_PWD")
host = getenv("HBNB_MYSQL_HOST")
database = getenv("HBNB_MYSQL_DB")


class DBStorage():
    """Class blueprint for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor for the database storage(DBStorage)"""
        from models.base_model import Base
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user,
                    password,
                    host,
                    database),
            pool_pre_ping=True)

    def all(self, cls=None):
        """returns all the objects of the class"""
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User
        from models.place import Place


        class_list = [State, City, User, Place, Review, Amenity]

        dictionary = {}
        if cls:
            results = self.__session.query(cls)
            for record in results:
                key = "{}.{}".format(type(record).__name__, record.id)
                dictionary[key] = record
        else:
            for l in self.__classes:
                results = self.__session.query(l)
                for record in results:
                    key = "{}.{}".format(type(record).__name__, row.id)
                    my_dict[key] = record
        return my_dict

    def new(self, obj):
        """adds object to database"""
        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        """commits or saves changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """method that deletes an object"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Method that creates the db session"""
        from models.base_model import Base
        from models.state import State  
        from models.review import Review
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.place import Place 

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        session_maker = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

    def close(self):
        """ends session for the database"""
        self.__session.close()
