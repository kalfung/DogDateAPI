from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required

events_bp = Blueprint('events', __name__, url_prefix='/events')

# GET all events - READ request
@events_bp.route('/')
@jwt_required()
def all_events():
    stmt = db.select(Event).order_by(Event.id) # could order_by name instead
    events = db.session.scalars(stmt).all()
    return EventSchema(many=True).dump(events)

# GET one event - READ request
@events_bp.route('/<int:event_id>')
@jwt_required()
def get_one_event(event_id):
    stmt = db.select(Event).filter_by(id=event_id)
    event = db.session.scalar(stmt)
    if event:
        return EventSchema().dump(event)
    else:
        return {'error': 'Event not found'}, 404
    
# POST new event - CREATE request
@events_bp.route('/', methods=['POST'])
@jwt_required()
def create_event():
    # Load the incoming POST data via the schema
    event_info = EventSchema().load(request.json)
    # Create a new Dog instance from the dog_info
    event = Event(
        title = event_info['title'],
        description = event_info['description'],
        date = event_info['date'],
        time = event_info['time'],
        user_id = get_jwt_identity(),
        park_id = event_info['park_id']
    )

    # Add and commit the new event to the session
    db.session.add(event)
    db.session.commit()
    # Send the new event back to the client
    return EventSchema().dump(event), 201