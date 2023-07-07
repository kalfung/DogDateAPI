from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp
from datetime import date, datetime
from time import time_ns

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    f_name = db.Column(db.String(40), nullable=False)
    l_name = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String, nullable=False)
    # Creating user role. A new user by default will not be an admin
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, nullable=False)

    # Relationship between owners and their dogs
    dogs = db.relationship('Dog', back_populates='owner', cascade='all, delete')
    # Relationship between users and the events they create
    events_created = db.relationship('Event', back_populates='event_creator', cascade='all, delete')
    
    # Relationship between users and the events they are attending NOT WORKING
    # events_attending = db.relationship('Event', secondary='event_user', backref='attendees')

class UserSchema(ma.Schema):
    # Telling Marshmallow to use DogSchema to serialise the 'dogs' field
    dogs = fields.List(fields.Nested('DogSchema', only=['name']))
    # Telling Marshmallow to use EventSchema to serialise the 'events_created' field
    events_created = fields.List(fields.Nested('EventSchema', only=['title']))
#     # NEED TO add schema for parksusers i.e. parks_frequented
#     # parks = fields.List(fields.Nested) 

    # Validators
    email = fields.Email(unique=True)
    username = fields.String(validate=And(
        Length(min=6, max=30, error='Username must be at least 6 character long, and no more than 30 characters'),
        Regexp('^[a-zA-Z0-9]+$', error='Only letters and numbers are allowed')
    ))
    f_name = fields.String(validate=And(
        Length(min=1, max=40, error='First name must be at least 1 character long, and no more than 40 characters'),
        Regexp('^[a-zA-Z \'-]+$', error='Only letters, spaces, hyphens and apostrophes are allowed')
    ))
    l_name = fields.String(validate=And(
        Length(min=1, max=40, error='Last name must be at least 1 character long, and no more than 40 characters'),
        Regexp('^[a-zA-Z \'-]+$', error='Only letters, spaces, hyphens and apostrophes are allowed')
    ))
    password = fields.String(validate=Length(min=8, error='Password must be at least 8 characters long'))
    is_admin = fields.Boolean(default=False)
    date_created = fields.Date(load_default=date.today())
    class Meta:
        fields = ('id', 'email', 'username', 'f_name', 'l_name', 'password', 'is_admin', 'date_created', 'dogs', 'events_created')
        ordered = True