from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from datetime import date
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

events_bp = Blueprint('events', __name__, url_prefix='/events')
