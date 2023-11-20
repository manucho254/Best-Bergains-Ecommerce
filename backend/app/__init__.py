from flask import Flask, Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    
    # Register blueprints here

    from app.views import app as app_views
    app.register_blueprint(app_views)

    return app