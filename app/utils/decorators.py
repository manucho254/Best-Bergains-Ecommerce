#!/usr/bin/python3
""" module for decorator functions
"""

from functools import wraps

from flask import request, redirect, url_for

from flask_login import current_user, logout_user

from config import db


def is_merchant(f):
    """ wrapper function for merchant routes
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None:
            return redirect(url_for("auth.login", next=request.url))
        if current_user.is_customer:
            user = current_user
            user.authenticated = False
            db.session.add(user)
            db.session.commit()
            logout_user()
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def is_customer(f):
    """ wrapper function for customer routes
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user is None:
            return redirect(url_for("auth.login", next=request.url))
        if current_user.is_merchant:
            user = current_user
            user.authenticated = False
            db.session.add(user)
            db.session.commit()
            logout_user()
            return redirect(url_for("auth.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function
