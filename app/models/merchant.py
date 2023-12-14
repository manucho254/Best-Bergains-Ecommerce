#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Merchant(db.Model):
    """ Merchant Model """

    __tablename__ = "merchants"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    user = db.relationship("User", backref="merchants", lazy=True, uselist=False)
    merchant_address = db.relationship(
        "Address", backref="merchants", lazy=True, uselist=False
    )
    products = db.relationship("Product", backref="merchants", lazy=True)
    merchant_orders = db.relationship("Order", backref="merchants", lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Merchant: {}".format(self.id)
