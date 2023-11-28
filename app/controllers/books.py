from flask import Blueprint, jsonify, request
from app.models.book import Book
from app import db

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'title': book.title, 'author': book.author} for book in books]
    return jsonify(book_list)

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})

@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')

    if not title or not author:
        return jsonify({'error': 'Both title and author are required'}), 400

    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()

    return jsonify({'message': 'Book created successfully', 'id': new_book.id}), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)

    db.session.commit()

    return jsonify({'message': 'Book updated successfully', 'id': book.id})

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted successfully'})
