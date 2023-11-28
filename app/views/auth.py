#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required

from app.utils.validations import validate_email
from app.models.user import User
from app.models.address import Address
from app.models.customer import Customer
from app.models.merchant import Merchant
from app.utils.helpers import hash_password, verify_password

from config import db, login_manager

auth = Blueprint("auth", __name__, url_prefix="/auth")

@login_manager.user_loader
def load_user(user_id):
    """since the user_id is just the primary
    key of our user table, use it in the query for the user
    """
    return User.query.filter_by(email=user_id).first()


@auth.route("/merchant/signup", methods=["GET", "POST"], strict_slashes=False)
def merchant_signup():
    """Create a new user account"""

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("products.get_products"))
        return render_template("auth/merchant_signup.html")

    error = None
    email = request.form.get("email")
    user_name = request.form.get("username")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    country = request.form.get("country")
    city = request.form.get("city")
    phone = request.form.get("phone")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if (
        email is None
        or user_name is None
        or password is None
        or confirm_password is None
    ):
        error = "Invalid data provided"
        return redirect(url_for("auth.merchant_signup"), error=error)
    if not validate_email(email):
        error = "Email provided not valid!"
        return redirect(url_for("auth.merchant_signup"), error=error)
    if password != confirm_password:
        error = "Password and confirm password don't match."
        return redirect(url_for("auth.merchant_signup"), error=error)
    if len(password) < 6:
        error = "Password too short."
        return redirect(url_for("auth.merchant_signup"), error=error)

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for("auth.login"))

    new_user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        username=user_name,
        password=hash_password(password),
        is_merchant=True,
    )
    address = Address(country=country, city=city, phone=phone)
    merchant = Merchant(user=new_user, merchant_address=address)
    db.session.add(new_user)
    db.session.add(address)
    db.session.add(merchant)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/customer/signup", methods=["GET", "POST"], strict_slashes=False)
def customer_signup():
    """Create a new user account"""

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("products.get_products"))
        return render_template("auth/customer_signup.html")

    error = None
    email = request.form.get("email")
    user_name = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if (
        email is None
        or user_name is None
        or password is None
        or confirm_password is None
    ):
        error = "Invalid data provided"
        return redirect(url_for("auth.customer_signup"), error=error)
    if not validate_email(email):
        error = "Email provided not valid!"
        return redirect(url_for("auth.customer_signup"), error=error)
    if password != confirm_password:
        error = "Password and confirm password don't match."
        return redirect(url_for("auth.customer_signup"), error=error)
    if len(password) < 6:
        error = "Password too short."
        return redirect(url_for("auth.customer_signup"), error=error)

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for("auth.login"))

    new_user = User(
        email=email,
        username=user_name,
        password=hash_password(password),
        is_customer=True,
    )
    customer = Customer(user=new_user)
    db.session.add(new_user)
    db.session.add(customer)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET", "POST"], strict_slashes=False)
def login():
    """Authenticate user"""
    
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("products.get_products"))
        return render_template("auth/login.html")

    error = None
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        error = "Invalid data provided!"
        return redirect(url_for("auth.login"))
    if not validate_email(email):
        error = "Email provided not valid!"
        return redirect(url_for("auth.login"))
    
    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()
    
    if (
        not user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        error = "Invalid credentials provided!"
        return redirect(url_for("auth.login"))
    
    if user and verify_password(password, user.password):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, force=True, fresh=True, remember=True)
        return redirect(url_for("products.get_products"))
    else:
        error = "Invalid credentials provided!"
        return redirect(url_for("auth.login"))


@auth.route("/logout", methods=["GET"], strict_slashes=False)
@login_required
def logout():
    """Logout user"""
    
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("products.get_products"))


@auth.route("/reset_password", methods=["GET", "POST"], strict_slashes=False)
def password_reset():
    """Authenticate user"""
    return render_template("auth/reset_password.html")


@auth.route("/change_password", methods=["GET", "POST"], strict_slashes=False)
def change_password():
    """Change user password"""
    return render_template("auth/change_password.html")


@auth.route("/create_account", methods=["GET"], strict_slashes=False)
def create_account():
    """choose account to create"""
    return render_template("auth/create_account.html")
