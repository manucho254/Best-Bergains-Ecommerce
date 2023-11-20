#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
from config import Base

from sqlalchemy import Column, String, Integer


class Customer(BaseModel, Base):
    """ """

    __tablename__ = "customers"
