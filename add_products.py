#!/usr/bin/python3
"""_create dummy db data_
"""
from app.models.product import Product, ProductCategory
from app.models.merchant import Merchant
from app.models.user import User
from app.models.address import Address

from app.utils.helpers import hash_password

from config import db

import requests

import random
import uuid


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

""" Add all categories to database
"""
for name in categories:
    new_id = uuid.uuid4()
    if not ProductCategory.query.filter_by(name=name).first():
        category = ProductCategory(id=new_id, name=name)
        db.session.add(category)
        db.session.commit()


current_user = User.query.filter_by(email="merchant@gmail.com").first()

""" create new user
"""
user = User(
    username="Nucho and Irine",
    first_name="Irine",
    last_name="Manucho",
    email="merchant@gmail.com",
    password=hash_password("testing"),
    is_merchant=True,
)

user = User.query.filter_by(email="merchant@gmail.com").first()


if user is None:
    """create new user"""
    user = User(
        username="Nucho and Irine",
        first_name="Irine",
        last_name="Manucho",
        email="merchant@gmail.com",
        password=hash_password("testing"),
        is_merchant=True,
    )

""" create merchant address
"""
address = Address(country="Kenya", city="kanairo", phone="0700000000")

""" create new merchant
"""
merchant = Merchant(user=user, merchant_address=address)
db.session.add(user)
db.session.add(address)
db.session.add(merchant)

merchant = Merchant.query.filter_by(user=user).first()

if merchant is None:
    """create new merchant"""
    merchant = Merchant(user=user, merchant_address=address)

try:
    db.session.add(user)
    db.session.add(address)
    db.session.add(merchant)
    db.session.commit()
except Exception as e:
    pass

req = requests.get("https://fakestoreapi.com/products")
data = req.json()

for prod in data:
    new_id = uuid.uuid4()
    if not Product.query.filter_by(title=prod.get("title")).first():
        category_name = random.choice(categories)
        print(category_name)
        category = ProductCategory.query.filter_by(name=category_name).first()
        product = Product(
            id=new_id,
            title=prod.get("title"),
            price=prod.get("price"),
            description=prod.get("description"),
        )
        category.products.append(product)
        merchant.products.append(product)
        try:
            db.session.add(category)
            db.session.add(merchant)
            db.session.add(product)
            db.session.commit()
        except Exception as e:
            pass

db.session.commit()
