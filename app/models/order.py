#!/usr/bin/python3
"""
"""

from config import db

from datetime import datetime
from uuid import uuid4


items = db.Table(
    "order_items",
    db.Column("order_id", db.String(100), db.ForeignKey("orders.id"), primary_key=True),
    db.Column("item_id", db.String(100), db.ForeignKey("items.id"), primary_key=True),
)


class Order(db.Model):
    """ Order Model """

    __tablename__ = "orders"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    customer_id = db.Column(
        db.String(100), db.ForeignKey("customers.id"), nullable=False
    )
    merchant_id = db.Column(
        db.String(100), db.ForeignKey("merchants.id")
    )
    order_items = db.relationship(
        "Item",
        secondary=items,
        lazy="subquery",
        backref=db.backref("orders", lazy=True),
    )
    total = db.Column(
        db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None)
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Order: {}>".format(self.id)


class Item(db.Model):
    """Order Item Model """

    __tablename__ = "items"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    product_id = db.Column(db.String(100), db.ForeignKey("products.id"))
    product = db.relationship("Product", backref="products", lazy=True, uselist=False)
    quantity = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def sub_total(self):
        """calculate the price an order item"""
        return self.quantity * self.product.price
