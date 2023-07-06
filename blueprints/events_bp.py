from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from models.event_user import Event_User
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity
from blueprints.auth_bp import admin_required, admin_or_owner_required

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
        return {'error': 'We could not find the event you were looking for'}, 404
    
# POST new event - CREATE request
@events_bp.route('/', methods=['POST'])
@jwt_required()
def create_event():
    # Load the incoming POST data via the schema
    event_info = EventSchema().load(request.json)
    # Create a new Event instance from the event_info
    event = Event(
        title = event_info['title'],
        description = event_info['description'],
        date = event_info['date'],
        time = event_info['time'],
        user_id = get_jwt_identity(), # creator of the event
        park_id = event_info['park_id']
    )

    # Add and commit the new event to the session
    db.session.add(event)
    db.session.commit()
    
    # Adding creator of event to the events_users association table
    event_user = Event_User(
        date_created = date.today(),
        event_id = event.id,
        user_id = get_jwt_identity() # creator of the event
    )
    
    # Add and commit the user as event attendee to the session
    db.session.add(event_user)
    db.session.commit()
        
    # Send the new event back to the client
    return EventSchema().dump(event), 201
    
# PUT or PATCH an event - UPDATE request
@events_bp.route('/<int:event_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_event(event_id):
    event_info = EventSchema().load(request.json)
    stmt = db.select(Event).filter_by(id=event_id)
    event = db.session.scalar(stmt)
    if event:
        admin_or_owner_required(event.event_creator.id)      
        event.title = event_info.get('title', event.title)
        event.description = event_info.get('description', event.description)
        event.date = event_info.get('date', event.date)
        event.time = event_info.get('time', event.time)
        event.park_id = event_info.get('park_id', event.park_id)
        db.session.commit()
        return EventSchema(exclude=['event_creator']).dump(event)
    else:
        return {'error': 'We could not find the event you were looking for'}, 404
    
# DELETE an event - DELETE request
@events_bp.route('/<int:event_id>', methods=['DELETE'])
@jwt_required()
def delete_event(event_id):
    stmt = db.select(Event).filter_by(id=event_id)
    event = db.session.scalar(stmt)
    if event:
        admin_or_owner_required(event.event_creator.id)
        db.session.delete(event)
        db.session.commit()
        return {'confirmation': f'{event.title} has been deleted'}, 200
    else:
        return {'error': 'We could not find the event you were looking for'}, 404