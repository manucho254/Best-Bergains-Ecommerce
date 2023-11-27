#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Merchant(db.Model):
    """Class merchant"""

    __tablename__ = "merchants"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    user = db.relationship("User", backref="merchants", lazy=True, uselist=False)
    merchant_address = db.relationship(
        "Address",
        backref="merchants",
        lazy=True,
        uselist=False
    )
    product_id = db.Column(
        db.String(100), db.ForeignKey("products.id")
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Customer: {}".format(self.id)
