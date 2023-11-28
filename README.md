# Book Library API Documentation

## Introduction

Welcome to the Book Library API documentation. This API provides functionalities to manage a library of books, including user authentication and CRUD operations for books.

## Authentication

### Register

- **Endpoint**: `/auth/register`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "message": "User registered successfully"
    }
    ```

### Login

- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Description**: Authenticate and login a user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "message": "Login successful"
    }
    ```

## Books

### Get All Books

- **Endpoint**: `/books/books`
- **Method**: `GET`
- **Description**: Get a list of all books.
- **Response**:
  - Status Code: `200 OK`
  - Body: Array of books

### Get a Single Book

- **Endpoint**: `/books/books/{book_id}`
- **Method**: `GET`
- **Description**: Get details of a specific book.
- **Response**:
  - Status Code: `200 OK`
  - Body: Book details

### Create a Book

- **Endpoint**: `/books/books`
- **Method**: `POST`
- **Description**: Create a new book.
- **Request Body**:
  ```json
  {
    "title": "string",
    "author": "string"
  }
  ```
- **Response**:
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "message": "Book created successfully",
      "id": "integer"
    }
    ```

### Update a Book

- **Endpoint**: `/books/books/{book_id}`
- **Method**: `PUT`
- **Description**: Update details of a specific book.
- **Request Body**:
  ```json
  {
    "title": "string",
    "author": "string"
  }
  ```
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "message": "Book updated successfully",
      "id": "integer"
    }
    ```

### Delete a Book

- **Endpoint**: `/books/books/{book_id}`
- **Method**: `DELETE`
- **Description**: Delete a specific book.
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "message": "Book deleted successfully"
    }
    ```

## API Table

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register` | POST | Register a new user. |
| `/auth/login` | POST | Authenticate and login a user. |
| `/books/books` | GET | Get a list of all books. |
| `/books/books/{book_id}` | GET | Get details of a specific book. |
| `/books/books` | POST | Create a new book. |
| `/books/books/{book_id}` | PUT | Update details of a specific book. |
| `/books/books/{book_id}` | DELETE | Delete a specific book. |

