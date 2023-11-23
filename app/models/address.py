#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Address(db.Model):
    """ """

    __tablename__ = "addresses"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    customer_id = db.Column(
        db.String(100), db.ForeignKey("customer_address.id"), nullable=False
    )
    merchant_id = db.Column(
        db.String(100), db.ForeignKey("merchant_address.id"), nullable=False
    )
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
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
        return "Customer: {}".format(self.id)
