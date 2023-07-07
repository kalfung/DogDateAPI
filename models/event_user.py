from init import db, ma
from marshmallow import fields
from marshmallow.validate import Range

class Event_User(db.Model):
    __tablename__ = 'events_users'

    id = db.Column(db.Integer, primary_key=True)
    
    date_created = db.Column(db.Date, nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    


class Event_UserSchema(ma.Schema):
#     # Validators
    event_id = fields.Integer(validation=Range(min=1))
    user_id = fields.Integer(validation=Range(min=1))

    # event = fields.Nested('EventSchema')
    # attendees = fields.List(fields.Nested('UserSchema'))
    class Meta:
        fields = ('id', 'date_created', 'event_id', 'user_id', 'event', 'attendees')