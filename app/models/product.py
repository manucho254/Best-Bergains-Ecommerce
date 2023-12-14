#!/usr/bin/python3
"""
"""
from config import db

from datetime import datetime
from uuid import uuid4


class Product(db.Model):
    """ Product Model """

    __tablename__ = "products"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    merchant_id = db.Column(db.String(100), db.ForeignKey("merchants.id"))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(
        db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None)
    )
    images = db.relationship(
        "ProductImage", backref="product", lazy=True, uselist=False
    )
    category_id = db.Column(db.String(100), db.ForeignKey("product_categories.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Product: {}>".format(self.id)


class ProductImage(db.Model):
    """Class product Image"""

    __tablename__ = "product_images"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    product_id = db.Column(db.String(100), db.ForeignKey("products.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    file_path = db.Column(db.String(300))

    def __repr__(self):
        return "<ProductImage: {}>".format(self.name)


class ProductCategory(db.Model):
    """class product category"""

    __tablename__ = "product_categories"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    name = db.Column(db.String(100), nullable=False, unique=True)
    products = db.relationship(
        "Product", backref="product_categories", lazy=True
    )

    def __repr__(self):
        return "<ProductCategory: {}>".format(self.name)
