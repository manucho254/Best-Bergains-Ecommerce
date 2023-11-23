#!/usr/bin/python3

from flask import Blueprint
from flask_login import login_required, current_user
from flask import render_template

from app.models.customer import Customer

customers = Blueprint("customers", __name__)


@customers.route("/<customer_id>", methods=["GET"], strict_slashes=False)
@login_required
def get_customer(customer_id):
    """Get customer data
    Args:
        customer_id (string): customer id
    """
    return render_template("index.html")

@customers.route("/<customer_id>", methods=["PUT"], strict_slashes=False)
@login_required
def update_customer(customer_id):
    """Update customer data
    Args:
        customer_id (string): customer id
    """
    return render_template("index.html")

@customers.route("/<customer_id>", methods=["DELETE"], strict_slashes=False)
@login_required
def delete_customer(customer_id):
    """Get customer data
    Args:
        customer_id (string): customer id
    """
    return render_template("index.html")

@customers.route("/<customer_id>/orders", methods=["DELETE"], strict_slashes=False)
@login_required
def customer_orders(customer_id):
    """Get customer orders
    Args:
        customer_id (string): customer id
    """
    return render_template("index.html")


@customers.route(
    "/<customer_id>/orders/<order_id>", methods=["DELETE"], strict_slashes=False
)
@login_required
def customer_order(customer_id, order_id):
    """Get customer orders
    Args:
        customer_id (string): customer id
    """
    return render_template("index.html")
