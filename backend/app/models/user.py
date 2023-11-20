#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
from config import Base


class User(BaseModel, Base):
    """ """

    __tablename__ = "users"
