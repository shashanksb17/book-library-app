# app.py

from flask import Flask, jsonify
from app import create_app, db
from app.models.book import Book
from app.controllers.books import books_bp
from app.controllers.auth import auth_bp  # Import the auth blueprint

app = create_app()

# Register the books blueprint with a unique name
app.register_blueprint(books_bp, url_prefix='/books', name='books_blueprint')

# Register the auth blueprint with a unique name
app.register_blueprint(auth_bp, url_prefix='/auth', name='auth_blueprint')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Book Library API'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before running the app
    app.run(debug=True)
