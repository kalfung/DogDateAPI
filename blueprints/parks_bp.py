from flask import Blueprint
from init import db
from models.park import Park, ParkSchema

parks_bp = Blueprint('parks', __name__, url_prefix='/parks')

# GET all parks
@parks_bp.route('/')
def all_parks():
    stmt = db.select(Park).order_by(Park.id)
    parks = db.session.scalars(stmt).all()
    return ParkSchema(many=True).dump(parks)
    # print(parks)
    # return {}