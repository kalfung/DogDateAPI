from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Event(db.Model):
    __tablename__= 'events'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    
    # relationship between events and the users that create them
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    event_creator = db.relationship('User', back_populates='events_created')

    # relationship between events and the venue
    park_id = db.Column(db.Integer(), db.ForeignKey('parks.id'), nullable=False)
    park = db.relationship('Park', back_populates='events')

    # relationship between events and the attendees in event_user table NOT WORKING
    # attendees = db.relationship('User', secondary='event_user', backref='events_attending')

    # def __repr__(self):
    #     return f'<Event "{self.title} {self.description}">'

class EventSchema(ma.Schema):
    # Tell Marshmallow to use UserSchema to serialise the 'event_creator' field
    event_creator = fields.Nested('UserSchema', only=['username', 'f_name', 'id'])
    # Tell Marshmallow to user ParkSchema to serialise the 'park' field
    park = fields.Nested('ParkSchema', only=['name'])
    # Validators
    title = fields.String(validate=And(
        Length(min=4, max=100, error='Title of the event must be at least 4 characters long, and no more than 100 characters'),
        Regexp('^[a-zA-Z0-9 \'-]+$', error='Only letters, numbers, spaces, hyphens and apostrophes are allowed')
    ))
    description = fields.String(validate=Length(max=1000, error='Description of the event cannot be more than 1000 characters'))
    date = fields.Date(error_messages={'invalid': 'Invalid date. Please use the YYYY-MM-DD format'})
    time = fields.Time(error_messages={'invalid': 'Invalid time. Please use the 24 hour HH:MM format'})
    user_id = fields.Integer()
    park_id = fields.Integer()
    class Meta:
        fields = ('id', 'title', 'description', 'date', 'time', 'park_id', 'park', 'event_creator', 'attendees')
        ordered = True