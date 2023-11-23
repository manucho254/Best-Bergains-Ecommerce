#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from local_env import DB_URI

from os import getenv

# instantiate  SQLAlchemy
db = SQLAlchemy()


def create_app():
    """flask app creation"""
    # create the object of Flask
    app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
    migrate = Migrate(app, db)

    app.config["SECRET_KEY"] = getenv("SECRET_KEY")
    # SqlAlchemy Database Configuration With Mysql
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # media and image settings
    app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
    app.config["UPLOAD_PATH"] = "products_media"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        """since the user_id is just the primary
        key of our user table, use it in the query for the user
        """
        return User.query.get(user_id)

    # blueprint for auth routes in our app
    from app.views.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for auth routes in our app
    from app.views.customers import customers as customers_blueprint

    app.register_blueprint(customers_blueprint)

    # blueprint for auth routes in our app
    from app.views.merchants import merchants as merchants_blueprint

    app.register_blueprint(merchants_blueprint)

    # blueprint for auth routes in our app
    from app.views.orders import orders as orders_blueprint

    app.register_blueprint(orders_blueprint)

    # blueprint for auth routes in our app
    from app.views.products import products as products_blueprint

    app.register_blueprint(products_blueprint)

    return app
