from extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Festival(db.Model):
    __tablename__ = "festivals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50))  # Using String for flexibility (e.g., "Varies")
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))


class Temple(db.Model):
    __tablename__ = "temples"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=False)
    # This model was missing the image_url too
    image_url = db.Column(db.String(255))


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100))
    religion = db.Column(db.String(50))
    description = db.Column(db.Text)
    # 🚀 ADD THIS LINE
    image_url = db.Column(db.String(255))


class Food(db.Model):
    __tablename__ = "foods"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
