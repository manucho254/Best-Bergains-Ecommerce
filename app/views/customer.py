#!/usr/bin/python3

from flask_login import login_required, current_user
from flask import Blueprint, render_template, request

from app.models.customer import Customer
from app.models.order import Order

from app.utils.decorators import is_customer

customers = Blueprint("customer", __name__, url_prefix="/customer")


@customers.route("/<customer_id>", methods=["GET"], strict_slashes=False)
@login_required
@is_customer
def get_customer(customer_id):
    """Get customer data
    Args:
        customer_id (string): customer id
    """
    
    customer = Customer.query.filter(customer_id == customer_id).first()
    return render_template("customer/customer.html", customer=customer)


@customers.route("/<customer_id>", methods=["PUT"], strict_slashes=False)
@login_required
@is_customer
def update_customer(customer_id):
    """Update customer data
    Args:
        customer_id (string): customer id
    """
    return render_template("customer/customer_detail.html")


@customers.route("/<customer_id>", methods=["DELETE"], strict_slashes=False)
@login_required
@is_customer
def delete_customer(customer_id):
    """Get customer data
    Args:
        customer_id (string): customer id
    """
    return render_template("customer/customer_detail.html")


@customers.route("/<customer_id>/orders", methods=["GET"], strict_slashes=False)
@login_required
@is_customer
def customer_orders(customer_id):
    """Get customer orders
    Args:
        customer_id (string): customer id
    """
    page = request.args.get("page", default=1, type=int)
    orders = (
        Order.query.filter(customer_id == customer_id)
        .order_by(Order.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("customer/customer_orders.html", orders=orders)


@customers.route(
    "/<customer_id>/orders/<order_id>", methods=["GET"], strict_slashes=False
)
@login_required
@is_customer
def customer_order(customer_id, order_id):
    """Get customer single order information
    Args:
        customer_id (string): customer id
        order_id (string): order id
    """
    order = Order.query.filter(customer_id=customer_id, id=order_id).first()

    if not order:
        return render_template("customer/customer_order.html", order=order_id)

    return render_template("customer/customer_order.html", order=order)
