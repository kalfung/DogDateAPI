from flask import Blueprint, request
from init import db
from models.park import Park, ParkSchema
from datetime import date

parks_bp = Blueprint('parks', __name__, url_prefix='/parks')

# GET all parks
@parks_bp.route('/')
def all_parks():
    stmt = db.select(Park).order_by(Park.id) # could order_by name instead
    parks = db.session.scalars(stmt).all()
    return ParkSchema(many=True).dump(parks)

# GET one park
@parks_bp.route('/<int:park_id>')
def get_one_park(park_id):
    stmt = db.select(Park).filter_by(id=park_id)
    park = db.session.scalar(stmt)
    if park:
        return ParkSchema().dump(park)
    else:
        return {'error': 'Park not found'}, 404
    
# POST new park
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