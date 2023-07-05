from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp
from datetime import date

class Park(db.Model):
    __tablename__= 'parks'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    date_registered = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)

    # Relationship between parks and their events
    events = db.relationship('Event', back_populates='park', cascade='all, delete')

class ParkSchema(ma.Schema):
    # Telling marshmallow to use EventSchema to serialise 'events'
    events = fields.List(fields.Nested('EventSchema', only=['title', 'date']))
    # Validators
    name = fields.String(required=True, validate=And(
        Length(min=4, error='Name of the park must be at least 4 characters long'),
        Regexp('^[a-zA-Z \'-]+$', error='Only letters, spaces, hyphens and apostrophes are allowed')
    ))
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    date_registered = fields.Date(load_default=date.today())
    last_updated = fields.Date(load_default=date.today())

    class Meta:
        fields = ('id', 'name', 'latitude', 'longitude', 'events')
        ordered = True