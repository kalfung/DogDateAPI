from init import db, ma
from marshmallow import fields

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
    event_creator = fields.Nested('UserSchema', only=['username', 'f_name'])
    # Tell Marshmallow to user ParkSchema to serailise the 'park' field
    park = fields.Nested('ParkSchema', only=['name'])
    class Meta:
        fields = ('id', 'title', 'description', 'date', 'time', 'event_creator', 'park')