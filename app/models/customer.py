#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Customer(db.Model):
    """ class Customer
    """

    __tablename__ = "customers"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    customer_id = db.Column(db.String(100), db.ForeignKey("users.id"))
    user = db.relationship("User", backref="customer_user", lazy=True, uselist=False)
    address = db.relationship("Address", backref="addresses", lazy=True, uselist=False)
    orders = db.relationship("Order", backref="orders", lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Customer: {}".format(self.id)
