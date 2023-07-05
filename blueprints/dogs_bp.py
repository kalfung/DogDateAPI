from flask import Blueprint, request
from init import db
from models.dog import Dog, DogSchema
from datetime import date
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')
