from flask import Blueprint, request
from init import db
from models.park import Park, ParkSchema
from datetime import date
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

parks_bp = Blueprint('parks', __name__, url_prefix='/parks')

# GET all parks - READ request
@parks_bp.route('/')
def all_parks():
    stmt = db.select(Park).order_by(Park.id) # could order_by name instead
    parks = db.session.scalars(stmt).all()
    return ParkSchema(many=True).dump(parks)

# GET one park - READ request
@parks_bp.route('/<int:park_id>')
def get_one_park(park_id):
    stmt = db.select(Park).filter_by(id=park_id)
    park = db.session.scalar(stmt)
    if park:
        return ParkSchema().dump(park)
    else:
        return {'error': 'Park not found'}, 404
    
# POST new park - CREATE request
@parks_bp.route('/', methods=['POST'])
def create_park():
    # Load the incoming POST data via the schema
    park_info = ParkSchema().load(request.json)
    # Create a new Park instance from the park_info
    park = Park(
        name = park_info['name'],
        latitude = park_info['latitude'],
        longitude = park_info['longitude'],
        date_registered = date.today(),
        last_updated = date.today()
    )

    # Add and commit the new park to the session
    db.session.add(park)
    db.session.commit()
    # Send the new park back to the client
    return ParkSchema().dump(park), 201

# PUT or PATCH park - UPDATE request
@parks_bp.route('/<int:park_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_park(park_id):
    # Load the incoming PUT or PATCH data via the schema
    park_info = ParkSchema().load(request.json)
    stmt = db.select(Park).filter_by(id=park_id)
    park = db.session.scalar(stmt)
    if park:
        admin_required()
        park.name = park_info.get('name', park.name)
        park.latitude = park_info.get('latitude', park.latitude)
        park.longitude = park_info.get('longitude', park.longitude)
        park.last_updated = date.today()
        db.session.commit()
        return ParkSchema().dump(park)
    else: 
        return {'error': 'Park not found'}, 404

# DELETE a park - DELETE request
@parks_bp.route('/<int:park_id>', methods=['DELETE'])
@jwt_required()
def delete_park(park_id):
    stmt = db.select(Park).filter_by(id=park_id)
    park = db.session.scalar(stmt)
    if park:
        admin_required()
        db.session.delete(park)
        db.session.commit()
        return {'confirmation': 'Park deleted'}, 200
    else:
        return {'error': 'Park not found'}, 404
