#!/usr/bin/python3

from flask import Blueprint
from flask import render_template, request, redirect, url_for

from app.utils.validations import validate_email
from app.models.user import User
from app.utils.helpers import hash_password, verify_password

from config import db

auth = Blueprint("auth", __name__)


auth.route("/login", methods=["GET, POST"], strict_slashes=False)
def signup():
    """Create a new user account"""
    
    if request.method == "GET":
        return render_template("index.html")
    
    message = None
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
        message = "Invalid data provided"
        return redirect(url_for("auth.signup"), message=message)
    if not validate_email(email):
        message = "Email provided not valid!"
        return redirect(url_for("auth.signup"), message=message)
    if password != confirm_password:
        message = "Password and confirm password don't match."
        return redirect(url_for("auth.signup"), message=message)
    if len(password) < 6:
        message = "Password too short."
        return redirect(url_for("auth.signup"), message=message)
    
    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for("auth.login"))
    
    new_user = User(email=email, name=user_name, password=hash_password(password))
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for("auth.login"))


auth.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """Authenticate user"""
    message = None
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        message = "Invalid data provided!"
        return redirect(url_for("auth.login"), message=message)
    if not validate_email(email):
        message = "Email provided not valid!"
        return redirect(url_for("auth.login"), message=message)

    user = User.query.filter_by(
        email=email
    ).first()  # if this returns a user, then the email already exists in database

    if not user:  # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for("auth.login"))
    

    return render_template("index.html")


auth.route("/logout", methods=["POST"], strict_slashes=False)
def logout():
    """Logout user"""
    return render_template("index.html")


auth.route("/reset_password", methods=["POST"], strict_slashes=False)
def password_reset():
    """Authenticate user"""
    return render_template("index.html")


auth.route("/change_password", methods=["POST"], strict_slashes=False)
def change_password():
    """Change user password"""
    return render_template("index.html")
