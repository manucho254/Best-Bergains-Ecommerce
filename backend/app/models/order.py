#!/usr/bin/python3
"""
"""

from models.base_model import BaseModel
from config import Base


class Order(BaseModel, Base):
    """_summary_"""

    __tablename__ = "orders"


class OrderItem(BaseModel, Base):
    """_summary_"""

    __tablename__ = "order_items"
