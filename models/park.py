from init import db, ma

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
    class Meta:
        fields = ('id', 'name', 'latitude', 'longitude')