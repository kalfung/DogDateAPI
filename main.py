from os import environ

from flask import Flask
from init import db, ma, jwt, bcrypt

def setup():
    # Creating instance of Flask object
    app = Flask(__name__)

    # Flask configuration
    # Setting database location with the DB URI
    app.config['SQLALECHEMY_DATEBASE_URI'] = environ.get('DB_URI')
    # JWT secret key
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

    # Passing in app object to all instances of init modules
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.get("/")
    def home():
        return "Lali ho, friend!"
    return app