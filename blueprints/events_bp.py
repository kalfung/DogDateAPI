from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from datetime import date
from flask_jwt_extended import jwt_required
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