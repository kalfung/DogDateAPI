from init import db

class Event(db.Model):
    __tablename__= "events"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    park_id = db.Column(db.Integer(), db.ForeignKey('parks.id'), nullable=False)
    park = db.relationship('Park', back_populates='events')