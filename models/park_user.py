from init import db, ma

class Park_User(db.Model):
    __tablename__ = 'parks_users'

    id = db.Column(db.Integer, primary_key=True)

    park_id = db.Column(db.Integer, db.ForeignKey('parks.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
