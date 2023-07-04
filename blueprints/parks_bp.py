from flask import Blueprint
from init import db
from models.park import Park, ParkSchema

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
        return {'error': 'Card not found'}, 404