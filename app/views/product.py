#!/usr/bin/python3

from flask_login import current_user
from flask import Blueprint, render_template, request

from app.models.product import Product, ProductCategory

from config import db

products = Blueprint("products", __name__, url_prefix="/products")


@products.route("/", methods=["GET", "POST"], strict_slashes=False)
def get_products():
    """Get products"""

    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="")
    category_name = request.args.get("category", default="")

    category = ProductCategory.query.filter_by(name=category_name).first()
    if category:
        products = (
            Product.query.filter(
                db.and_(
                    Product.category_id == category.id,
                    Product.title.ilike(r"%{}%".format(query)),
                )
            )
            .order_by(Product.created_at)
            .paginate(page=page, per_page=15)
        )
    else:
        products = (
            Product.query.filter(
                db.or_(
                    Product.category_id == "",
                    Product.title.ilike(r"%{}%".format(query)),
                )
            )
            .order_by(Product.created_at)
            .paginate(page=page, per_page=15)
        )

    categories = ProductCategory.query.all()

    return render_template(
        "product/products.html",
        products=products,
        categories=categories,
    )


@products.route("/<product_id>", methods=["GET"], strict_slashes=False)
def get_product(product_id):
    """Create new product"""
    product = Product.query.filter_by(id=product_id).first()

    return render_template("product/product_detail.html", product=product)


@products.route("/search", methods=["POST"], strict_slashes=False)
def filter_product():
    """search and filter products"""
    query = request.args.get("query", default="")

    products = Product.query.order_by(Product.created_at).paginate(page=1, per_page=15)
    return render_template("product/products.html", products=products)
