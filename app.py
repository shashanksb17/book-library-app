from flask import Flask, jsonify
from app import create_app, db
from app.models.book import Book
from app.controllers.books import books_bp
from app.controllers.auth import auth_bp  

app = create_app()

app.register_blueprint(books_bp, url_prefix='/books', name='books_blueprint')

app.register_blueprint(auth_bp, url_prefix='/auth', name='auth_blueprint')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Book Library API'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
