from flask import Blueprint, request
from init import db
from models.dog import Dog, DogSchema
from datetime import date
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

dogs_bp = Blueprint('dogs', __name__, url_prefix='/dogs')

# GET all dogs - READ request
@dogs_bp.route('/')
@jwt_required()
def all_dogs():
    stmt = db.select(Dog).order_by(Dog.id) # could order_by name instead
    dogs = db.session.scalars(stmt).all()
    return DogSchema(many=True).dump(dogs)

# GET one dog - READ request
@dogs_bp.route('/<int:dog_id>')
@jwt_required()
def get_one_dog(dog_id):
    stmt = db.select(Dog).filter_by(id=dog_id)
    dog = db.session.scalar(stmt)
    if dog:
        return DogSchema().dump(dog)
    else:
        return {'error': 'Dog not found'}, 404