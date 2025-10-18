from flask import Blueprint, jsonify
from models.db_models import Festival, Temple, Book, Food

data_bp = Blueprint('data', __name__)

@data_bp.route('/festivals', methods=['GET'])
def get_festivals():
    festivals_list = Festival.query.all()
    
    # --- Edge Case: No data found ---
    if not festivals_list:
        return jsonify([]), 200 # Return empty list, not an error

    # Convert object list to dictionary list
    output = [{
        'id': f.id, 'name': f.name, 'date': f.date,
        'description': f.description, 'image_url': f.image_url
    } for f in festivals_list]
    
    return jsonify(output), 200

@data_bp.route('/temples', methods=['GET'])
def get_temples():
    temples_list = Temple.query.all()
    output = [{
        'id': t.id, 'name': t.name, 'location': t.location,
        'description': t.description, 'image_url': t.image_url
    } for t in temples_list]
    return jsonify(output), 200

# --- Implement /books and /foods endpoints similarly ---
@data_bp.route('/books', methods=['GET'])
def get_books():
    books_list = Book.query.all()
    output = [{
        'id': b.id, 'title': b.title, 'author': b.author,
        'religion': b.religion, 'description': b.description
    } for b in books_list]
    return jsonify(output), 200

@data_bp.route('/foods', methods=['GET'])
def get_foods():
    foods_list = Food.query.all()
    output = [{
        'id': f.id, 'name': f.name, 'region': f.region,
        'description': f.description, 'image_url': f.image_url
    } for f in foods_list]
    return jsonify(output), 200