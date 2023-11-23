#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Product(db.Model):
    """Class Product"""

    __tablename__ = "products"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    merchant = db.relationship(
        "Merchant", backref="merchants", lazy=True, uselist=False
    )
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(
        db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None)
    )
    images = db.relationship("ProductImage", backref="product_images", lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Product: {}>".format(self.id)


class ProductImage(db.Model):
    """Class product Image"""

    __tablename__ = "product_images"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    product_id = db.Column(
        db.String(100), db.ForeignKey("product_images.id"), nullable=False
    )
    name = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(300))

    def __repr__(self):
        return "<ProductImage: {}>".format(self.id)
