#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from local_env import DB_URI, SECRET_KEY

from os import getenv

# instantiate  SQLAlchemy
db = SQLAlchemy()

# login manager
login_manager = LoginManager()


def create_app():
    """flask app creation"""
    # create the object of Flask
    app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
    migrate = Migrate(app, db)

    app.config["SECRET_KEY"] = SECRET_KEY
    # SqlAlchemy Database Configuration With Mysql
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # media and image settings
    app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
    app.config["UPLOAD_PATH"] = "products_media"

    db.init_app(app)
    
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message_category = "info"
    login_manager.init_app(app)
    
    from app.views.home import home as home_blueprint
    from app.views.auth import auth as auth_blueprint
    from app.views.customer import customers as customers_blueprint
    from app.views.merchant import merchants as merchants_blueprint
    from app.views.product import products as products_blueprint
    
    # blueprint for auth routes in our app
    app.register_blueprint(auth_blueprint)
    # blueprint for home routes in our app
    app.register_blueprint(home_blueprint)
    # blueprint for customer routes in our app
    app.register_blueprint(customers_blueprint)
    # blueprint for merchant routes in our app
    app.register_blueprint(merchants_blueprint)
    # blueprint for product routes in our app
    app.register_blueprint(products_blueprint)
    
    return app