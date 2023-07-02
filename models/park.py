from init import db, ma

class Park(db.Model):
    __tablename__= 'parks'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    date_updated = db.Column(db.Date(), nullable=False)