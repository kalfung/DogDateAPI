from flask import Blueprint, request
from init import db
from models.dog import Dog, DogSchema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required

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
    
# POST new dog - CREATE request
@dogs_bp.route('/', methods=['POST'])
@jwt_required()
def create_dog():
    # Load the incoming POST data via the schema
    dog_info = DogSchema().load(request.json)
    # Create a new Dog instance from the dog_info
    dog = Dog(
        name = dog_info['name'],
        gender = dog_info['gender'],
        breed = dog_info['breed'],
        age = dog_info['age'],
        size = dog_info['size'],
        user_id = get_jwt_identity()
    )

    # Add and commit the new dog to the session
    db.session.add(dog)
    db.session.commit()
    # Send the new dog back to the client
    return DogSchema().dump(dog), 201

# PUT or PATCH a dog - UPDATE request
@dogs_bp.route('/<int:dog_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_dog(dog_id):
    dog_info = DogSchema().load(request.json)
    stmt = db.select(Dog).filter_by(id=dog_id)
    dog = db.session.scalar(stmt)
    if dog:
        admin_or_owner_required(dog.owner.id)     
        dog.name = dog_info.get('name', dog.name)
        dog.breed = dog_info.get('breed', dog.breed)
        dog.age = dog_info.get('age', dog.age)
        dog.size = dog_info.get('size', dog.size)
        db.session.commit()
        return DogSchema(exclude=['owner']).dump(dog)
    else:
        return {'error': 'Dog not found'}, 404
    
# DELETE a dog - DELETE request
@dogs_bp.route('/<int:dog_id>', methods=['DELETE'])
@jwt_required()
def delete_dog(dog_id):
    stmt = db.select(Dog).filter_by(id=dog_id)
    dog = db.session.scalar(stmt)
    if dog:
        admin_or_owner_required(dog.owner.id) 
        db.session.delete(dog)
        db.session.commit()
        return {'confirmation': f'{dog.name} has been deleted'}, 200
    else:
        return {'error': 'Dog not found'}, 404