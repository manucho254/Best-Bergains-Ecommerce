#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.user import User
from models.customer import Customer
from models.merchant import Merchant
from models.order import Order
from models.product import Product

from config import Base

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
    "user": User,
    "Customer": Customer,
    "merchant": Merchant,
    "product": Product,
    "order": Order,
}


class DBStorage:
    """interacts with the MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        DB_USER = getenv("DB_USER")
        DB_PWD = getenv("DB_PWD ")
        DB_HOST = getenv("DB_HOST")
        DB_NAME = getenv("DB_NAME")
        ENV = getenv("ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                DB_USER, DB_PWD, DB_HOST, DB_NAME
            )
        )
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for obj in classes:
            if cls is None or cls is classes[obj] or cls is obj:
                objs = self.__session.query(classes[obj]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, obj_id):
        """method to retrieve one object.
        Args:
             cls: class
             id: string representing the object ID
        """
        if cls and obj_id:
            objects = self.all(cls)
            full_name = cls.__name__ + "." + obj_id
            return objects.get(full_name)
        else:
            return None

    def count(self, cls=None):
        """count the number of objects in storage.
        Args:
             cls: class
        """

        return len(self.all(cls))
