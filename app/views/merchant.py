#!/usr/bin/python3

from flask_login import login_required, current_user
from flask import Blueprint, request, render_template

from app.models.merchant import Merchant
from app.models.product import Product
from app.models.order import Order

from app.utils.decorators import is_merchant

from config import db

merchants = Blueprint("merchant", __name__, url_prefix="/merchant")


@merchants.route("/<merchant_id>", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def get_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    merchant = Merchant.query.filter(id=merchant_id).first()
    return render_template("merchant/merchant.html", merchant=merchant)


@merchants.route("/<merchant_id>", methods=["PUT"], strict_slashes=False)
@login_required
@is_merchant
def update_merchant(merchant_id):
    """Update merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("merchant/merchant_detail.html")


@merchants.route("/<merchant_id>", methods=["DELETE"], strict_slashes=False)
@login_required
@is_merchant
def delete_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
    """
    return render_template("merchant/merchant.html")


@merchants.route("/<merchant_id>/orders", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def merchant_orders(merchant_id):
    """Get merchant orders
    Args:
        merchant_id (string): merchant id
    """
    return render_template("merchant/merchant_orders.html")


@merchants.route(
    "/<merchant_id>/orders/<order_id>", methods=["GET"], strict_slashes=False
)
@login_required
@is_merchant
def merchant_order(merchant_id, order_id):
    """Get merchant single order
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    page = request.args.get("page", default=1, type=int)
    orders = (
        Order.query.filter(db.and_(merchant_id == merchant_id, id == order_id))
        .order_by(Order.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_orders.html", orders=orders)


@merchants.route("/<merchant_id>/products", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_products.html", products=products)


@merchants.route("/<merchant_id>/products/add", methods=["GET", "POST"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_products.html", products=products)

@merchants.route("/<merchant_id>/products/<product_id>/update", methods=["GET", "POST"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id, product_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_products.html", products=products)


@merchants.route("/<merchant_id>/products/<product_id>/delete", methods=["POST"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id, product_id):
    """Delete merchant product
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_products.html", products=products)


@merchants.route("/<merchant_id>/customers", methods=["DELETE"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id):
    """Get merchant customers
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_products.html", products=products)