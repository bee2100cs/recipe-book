# Python standard libraries
import os

# Third-party libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



# Initialize SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    # configure the SQLite database, relative to the app instance folder
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'recipe.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # initialize the app with the extension
    db.init_app(app)

    # Specify a user loader
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Import the models to ensure they are registered with SQLAlcchemy
    from . import models

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return models.User.query.get(int(user_id))
    
    # Create the tables
    with app.app_context():
        db.create_all()

    # Blueprint for auth routes
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # Blueprint for auth routes
    from .google_auth import bp as google_bp
    app.register_blueprint(google_bp)
    # Register non-auth parts of the app lueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # Initialize the auth module
    #auth.init_app(app)

    return app

