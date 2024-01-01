#!/usr/bin/python3
"""Contains the DBStorage class"""
from sqlalchemy import create_engine, MetaData
import os
from models.base_model import BaseModel
from sqlalchemy.orm import sessionmaker, declarative_base
Session = sessionmaker()
Base = declarative_base()


class DBStorage:
    """This is the class that creates a new engine"""
    __engine = None
    __session = None

    user = os.getenv("HBNB_MYSQL_USER")
    pwd = os.getenv("HBNB_MYSQL_PWD")
    localhost = os.getenv("HBNB_MYSQL_HOST")
    database = os.getenv("HBNB_MYSQL_DB")

    def __init__(self):
        """Initializing the engine"""

        conn_string = f"mysql+mysqldb://{user}:{pwd}@{localhost}/{database}"
        self.__engine = create_engine(conn_string, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)

        if cls is not None:
            print(self.__session.query(cls).all())
        else:
            classes = [User, State, City, Amenity, Place, Review]
            results = []
            for obj in classes:
                print(self.__session.query(obj).all())

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from sqlalchemy.orm import sessionmaker, declarative_base
        from sqlalchemy.orm import scoped_session

        Session = sessionmaker(expire_on_commit=False)
        Session = scoped_session(Session)
        Base = declarative_base()

        Base.metadata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
