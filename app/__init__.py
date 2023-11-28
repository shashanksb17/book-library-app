# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config  # Import the Config class

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Set the app configuration
    app.config.from_object(Config)

    db.init_app(app)

    from app.controllers.auth import auth_bp
    from app.controllers.books import books_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)

    return app
