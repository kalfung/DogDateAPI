from os import environ

from flask import Flask
from init import db, ma, jwt, bcrypt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.dogs_bp import dogs_bp
from blueprints.parks_bp import parks_bp
from blueprints.events_bp import events_bp


def setup():
    # Creating instance of Flask object
    app = Flask(__name__)

    # Flask configuration
    # Setting database location with the DB URI
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    # JWT secret key
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

    # Passing in app object to all instances of init modules
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Registering blueprints with the app object
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dogs_bp)
    app.register_blueprint(parks_bp)
    app.register_blueprint(events_bp)
    
    @app.route("/")
    def home():
        return "Lali ho, friend!"
    return app