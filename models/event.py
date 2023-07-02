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

    # relationship between events and the attendees NOT WORKING
    # attendees = db.relationship('User', secondary='event_user', back_populates='events_attending')

    park_id = db.Column(db.Integer(), db.ForeignKey('parks.id'), nullable=False)
    # park = db.relationship('Park', back_populates='events')

    def __repr__(self):
        return f'<Event "{self.title}">'

class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_time', 'park_id', 'user_id')