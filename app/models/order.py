#!/usr/bin/python3
"""
"""

from config import db

from datetime import datetime
from uuid import uuid4


products = db.Table(
    "order_items",
    db.Column("order_id", db.String(100), db.ForeignKey("orders.id"), primary_key=True),
    db.Column(
        "product_id", db.String(100), db.ForeignKey("products.id"), primary_key=True
    ),
)


class Order(db.Model):
    """Class Order"""

    __tablename__ = "orders"
    id = db.Column(db.String(100), primary_key=True, default=str(uuid4()))
    customer_id = db.Column(
        db.String(100), db.ForeignKey("orders.id"), nullable=False
    )
    order_items = db.relationship(
        "Product",
        secondary=products,
        lazy="subquery",
        backref=db.backref("orders", lazy=True),
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Order: {}>".format(self.id)
