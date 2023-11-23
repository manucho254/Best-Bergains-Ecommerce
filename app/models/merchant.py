#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Merchant(db.Model):
    """ Class merchant
    """

    __tablename__ = "merchants"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    merchant_id = db.Column(db.String(100), db.ForeignKey("users.id"))
    user = db.relationship("User", backref="users", lazy=True, uselist=False)
    address = db.relationship("Address", backref="addresses", lazy=True, uselist=False)
    product_id = db.Column(db.String(100), db.ForeignKey('merchants.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Customer: {}".format(self.id)
