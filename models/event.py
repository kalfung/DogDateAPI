from init import db, ma

class Event(db.Model):
    __tablename__= 'events'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    park_id = db.Column(db.Integer(), db.ForeignKey('parks.id'), nullable=False)
    # park = db.relationship('Park', back_populates='events')

class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date_time', 'park_id')