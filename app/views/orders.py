#!/usr/bin/python3

from flask import Blueprint
from flask_login import login_required, current_user
from flask import render_template

from app.models.order import Order

orders = Blueprint("orders", __name__)


@orders.route("/", methods=["POST"], strict_slashes=False)
@login_required
def new_order():
    """Create a new order"""
    return render_template("index.html")