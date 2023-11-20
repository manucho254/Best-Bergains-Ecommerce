#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
from config import Base


class Product(BaseModel, Base):
    """_summary_"""

    __tablename__ = "products"
