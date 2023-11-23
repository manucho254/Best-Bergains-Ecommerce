from config import app
from flask import render_template
from flask import Blueprint

customers = Blueprint("", __name__)

app.route("", methods=["GET"], strict_slashes=False)
def home_page():
    """Landing page of the best bargains"""

    return render_template("index.html")
