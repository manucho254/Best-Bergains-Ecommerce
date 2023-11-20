#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
from config import Base

from sqlalchemy import Column, String, Integer


class Merchant(BaseModel, Base):
    """ """

    __tablename__ = "merchants"
