#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Customer(db.Model):
    """class Customer"""

    __tablename__ = "customers"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    user = db.relationship("User", backref="customers", lazy=True, uselist=False)
    customer_address = db.relationship(
        "Address",
        backref="customers",
        lazy=True,
        uselist=False
    )
    customer_orders = db.relationship("Order", backref="customers", lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Customer: {}".format(self.id)
