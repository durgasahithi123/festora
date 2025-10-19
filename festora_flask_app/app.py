import os
from flask import Flask, render_template # Add render_template for potential use
from flask_cors import CORS
from dotenv import load_dotenv

# Import the extension instances
from extensions import db, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_default_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    # Since you're serving the frontend from Flask, you might only need CORS
    # for specific API requests if they come from a different port/origin.
    # We'll keep it for the API routes.
    CORS(app, supports_credentials=True) # supports_credentials is important for session/cookies

    # Import and register blueprints
    from routes.auth_routes import auth_bp
    from routes.data_routes import data_bp
    from routes.view_routes import view_bp  # NEW: Import view blueprint

    # Register API Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(data_bp, url_prefix='/api')
    
    # NEW: Register View Blueprint for frontend routes
    app.register_blueprint(view_bp, url_prefix='/') 

    # Removed the original @app.route("/test") and index() function 
    # to keep all routes organized within Blueprints.
    # You can move it to view_routes.py if needed.
    @app.route("/test")

    def index():

        return "Hello, Heritage API!"
    
    return app

app = create_app()



if __name__ == '__main__':
    # Add context for database operations if needed, though Flask-Migrate is usually better
    with app.app_context():
        # Ensure database and tables exist on initial run if not using migrations yet
        # db.create_all() 
        pass 
        
    app.run(debug=True)