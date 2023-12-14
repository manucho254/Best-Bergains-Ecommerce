#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Address(db.Model):
    """ Address Model """

    __tablename__ = "address"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    customer_id = db.Column(
        db.String(100), db.ForeignKey("customers.id")
    )
    merchant_id = db.Column(
        db.String(100), db.ForeignKey("merchants.id")
    )
    country = db.Column(db.String(120))
    city = db.Column(db.String(120))
    address_line_1 = db.Column(db.String(120))
    address_line_2 = db.Column(db.String(120))
    zip_code = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """ """
        return "Address: {}".format(self.id)
