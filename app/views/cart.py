#!/usr/bin/python3

from flask import Blueprint, render_template
from flask_login import login_required

from app.utils.decorators import is_customer


cart = Blueprint("cart", __name__, url_prefix="/cart")


@cart.route("/", methods=["GET"], strict_slashes=False)
def cart_items():
    """ get all items in cart """
    return render_template("cart/cart_items.html")


@cart.route("/checkout", methods=["GET", "POST"], strict_slashes=False)
@login_required
@is_customer
def cart_checkout():
    """ get all items in cart """
    
    return render_template("cart/cart_checkout.html")