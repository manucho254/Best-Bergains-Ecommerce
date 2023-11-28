#!/usr/bin/python3
"""_create dummy db data_
"""
from app.models.product import Product, ProductCategory
from app.models.merchant import Merchant

from config import db

import requests

import random


categories = [
    "Computing",
    "Electronics",
    "Sporting Goods",
    "Garden & Outdoors",
    "Musical Instruments",
    "Phones & Tablets",
    "Toys & Games",
    "Pet Supplies",
    "Home & Office",
    "Automobile",
    "Health & Beauty",
    "Baby Products",
    "Industrial & Scientific",
    "Fashion",
]

import uuid
for name in categories:
    new_id = uuid.uuid4()
    print(ProductCategory.query.filter_by(name=name).first())
    if not ProductCategory.query.filter_by(name=name).first():
        category = ProductCategory(id=new_id, name=name)
        db.session.add(category)
        db.session.commit()


merchant = Merchant.query.filter_by(id="5976155c-14c7-4126-83f7-f82afab84ecb").first()


req = requests.get("https://fakestoreapi.com/products")
data = req.json()

category = ProductCategory.query.filter(name == "Fashion").first()
print(data)
for prod in data:
    new_id = uuid.uuid4()
    if not Product.query.filter_by(title=prod.get("title")).first():
        product = Product(
            id=new_id,
            merchant=merchant,
            title=prod.get("title"),
            category=category,
            price=prod.get("price"),
            description=prod.get("description"),
        )
        try:
            db.session.add(category)
            db.session.add(product)
            db.session.commit()
        except Exception as e:
              pass

