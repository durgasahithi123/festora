from flask import Blueprint, render_template

view_bp = Blueprint('view', __name__)

# 1. Main View (Works fine)
@view_bp.route('/', methods=['GET'])
def main_view():
    """Renders the main HTML page."""
    return render_template('main.html')

# 2. Calendar View (Matches 'view.calender_view')
# You must create a 'calender.html' file in your 'templates' folder.
@view_bp.route('/calender', methods=['GET'])
def calender_view():
    """Renders the calendar page."""
    # Temporarily render main.html if calender.html doesn't exist yet
    return render_template('calender.html') 

# 3. Books View (Matches 'view.books_view')
# You must create a 'books.html' file in your 'templates' folder.
@view_bp.route('/books', methods=['GET'])
def books_view():
    """Renders the books page."""
    # Temporarily render main.html if books.html doesn't exist yet
    return render_template('books.html')

# 4. Login/Signup routes are linked using 'auth.login' and 'auth.signup'.
# These must be defined in 'routes/auth_routes.py'.
# The links assume 'auth_bp' is registered in app.py with url_prefix='/api'.
# You should check if you meant to link to the API or a frontend template. 
# If they are frontend templates, they should also be defined here (or in a dedicated view blueprint).