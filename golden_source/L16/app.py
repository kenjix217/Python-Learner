from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "isbn": "978-0743273565"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "isbn": "978-0451524935"}
]

# Helper to find next ID
def get_next_id():
    if not books:
        return 1
    return max(book["id"] for book in books) + 1

# GET /api/books - List all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /api/books/<id> - Get specific book
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# POST /api/books - Add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400
    
    data = request.get_json()
    
    # Validation
    required_fields = ["title", "author", "year", "isbn"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Missing fields. Required: {required_fields}"}), 400

    new_book = {
        "id": get_next_id(),
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "isbn": data["isbn"]
    }
    
    books.append(new_book)
    return jsonify(new_book), 201

# DELETE /api/books/<id> - Remove a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    initial_len = len(books)
    books = [b for b in books if b["id"] != book_id]
    
    if len(books) < initial_len:
        return jsonify({"message": f"Book {book_id} deleted successfully"}), 200
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    print("Starting L16 Book API...")
    app.run(debug=True, port=5002)
