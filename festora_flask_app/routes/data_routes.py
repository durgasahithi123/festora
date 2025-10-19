from flask import Blueprint, jsonify
from models.db_models import Festival, Temple, Book, Food

data_bp = Blueprint("data", __name__)


@data_bp.route("/festivals", methods=["GET"])
def get_festivals():
    festivals_list = Festival.query.all()
    if not festivals_list:
        return jsonify([]), 200
    output = [
        {
            "id": f.id,
            "name": f.name,
            "date": f.date,
            "description": f.description,
            "image_url": f.image_url,  # ✅ This one was correct
        }
        for f in festivals_list
    ]
    return jsonify(output), 200


@data_bp.route("/temples", methods=["GET"])
def get_temples():
    temples_list = Temple.query.all()
    output = [
        {
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "description": t.description,
            "image_url": t.image_url,  # 🚀 ADDED THIS LINE
        }
        for t in temples_list
    ]
    return jsonify(output), 200


@data_bp.route("/books", methods=["GET"])
def get_books():
    books_list = Book.query.all()
    output = [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "religion": b.religion,
            "description": b.description,
            "image_url": b.image_url,  # 🚀 ADDED THIS LINE
        }
        for b in books_list
    ]
    return jsonify(output), 200


@data_bp.route("/foods", methods=["GET"])
def get_foods():
    foods_list = Food.query.all()
    output = [
        {
            "id": f.id,
            "name": f.name,
            "region": f.region,
            "description": f.description,
            "image_url": f.image_url,  # 🚀 ADDED THIS LINE
        }
        for f in foods_list
    ]
    return jsonify(output), 200
