from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions here
db = SQLAlchemy()
migrate = Migrate()