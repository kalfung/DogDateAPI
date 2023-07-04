from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
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
    
    # Relationship between users and the parks they frequent 

class UserSchema(ma.Schema):
    # Telling Marshmallow to use DogSchema to serialise the 'dogs' field
    dogs = fields.List(fields.Nested('DogSchema', exclude=['user_id', 'owner']))
    # Telling Marshmallow to use EventSchema to serialise the 'events_created' field
    events_created = fields.List(fields.Nested('EventSchema', exclude=['id', 'user_id']))
#     # NEED TO add schema for parksusers i.e. parks_frequented
#     # parks = fields.List(fields.Nested) 

    class Meta:
        fields = ('email', 'username', 'f_name', 'password', 'is_admin', 'dogs', 'events_created')