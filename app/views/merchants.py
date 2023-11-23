#!/usr/bin/python3

from flask import Blueprint
from flask_login import login_required, current_user
from flask import render_template

from app.models.merchant import Merchant

merchants = Blueprint("merchants", __name__)


@merchants.route("/<merchant_id>", methods=["GET"], strict_slashes=False)
@login_required
def get_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("index.html")

@merchants.route("/<merchant_id>", methods=["PUT"], strict_slashes=False)
@login_required
def update_merchant(merchant_id):
    """Update merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("index.html")

@merchants.route("/<merchant_id>", methods=["DELETE"], strict_slashes=False)
@login_required
def delete_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("index.html")

@merchants.route("/<merchant_id>/orders", methods=["GET"], strict_slashes=False)
@login_required
def merchant_orders(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
    """
    return render_template("index.html")

@merchants.route(
    "/<merchant_id>/orders/<order_id>", methods=["GET"], strict_slashes=False
)
@login_required
def merchant_order(merchant_id, order_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("index.html")

@merchants.route(
    "/<merchant_id>/products/<product_id>", methods=["GET"], strict_slashes=False
)
@login_required
def merchant_products(merchant_id, product_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    return render_template("index.html")
