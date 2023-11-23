#!/usr/bin/python3


from flask import Blueprint
from flask_login import login_required, current_user
from flask import render_template

from app.models.product import Product

products = Blueprint("products", __name__)


@products.route("/", methods=["POST"], strict_slashes=False)
@login_required
def add_product():
    """Create new product"""
    return render_template("index.html")


@products.route("/", methods=["GET"], strict_slashes=False)
def get_products():
    """Get products"""
    return render_template("index.html")


@products.route("/<product_id>", methods=["GET"], strict_slashes=False)
def get_product():
    """Create new product"""
    return render_template("index.html")


@products.route("/search", methods=["POST"], strict_slashes=False)
def filter_product():
    """search and filter products"""
    return render_template("index.html")