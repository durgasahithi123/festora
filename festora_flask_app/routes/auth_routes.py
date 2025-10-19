from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.db_models import User  # Ensure this import is correct
from extensions import db          # Ensure this import is correct

auth_bp = Blueprint('auth', __name__)

# --- Helper Function for Robust Data Extraction ---
def get_request_data():
    """Tries to get JSON data, falls back to form data."""
    if request.is_json:
        return request.get_json()
    else:
        # Check if form data exists
        if request.form:
            return request.form
        # Fallback if no data is present
        return {}

# ----------------------------------------------------

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Use the robust data extractor
    data = get_request_data()

    # --- Edge Case: Input Validation ---
    if not data or not data.get('email') or not data.get('password') or not data.get('name'):
        # Check if it was a Content-Type issue without data
        if not data and request.content_length and not request.is_json:
            return jsonify({'error': "Unsupported Content-Type. Send 'application/json' or standard form data."}), 415

        return jsonify({'error': 'Missing required fields: name, email, password'}), 400

    # --- Edge Case: Check if user already exists ---
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email address already registered'}), 409 # 409 Conflict

    # Assuming 'password' is present after validation
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        password_hash=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Use the robust data extractor
    data = get_request_data()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=data['email']).first()

    # --- Edge Case: Check user existence and password correctness ---
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401 # 401 Unauthorized

    # Use Flask's session to store user info
    session['user_id'] = user.id
    session['user_name'] = user.name
    
    return jsonify({
        'message': 'Login successful',
        'user': {'id': user.id, 'name': user.name, 'email': user.email}
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear() # Clear the session
    return jsonify({'message': 'Logout successful'}), 200

@auth_bp.route('/status', methods=['GET'])
def status():
    # An endpoint to check if a user is logged in
    if 'user_id' in session:
        return jsonify({
            'isLoggedIn': True,
            'user': {'id': session['user_id'], 'name': session['user_name']}
        }), 200
    else:
        return jsonify({'isLoggedIn': False}), 200