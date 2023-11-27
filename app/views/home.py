#!/usr/bin/python3
from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/", methods=["GET"], strict_slashes=False)
def home_page():
    """Landing page of the best bargains"""

    return render_template("index.html")
