from init import db

class Dog(db.Model):
    __tablename__= "dogs"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String, nullable=False, default='Small')
    is_admin = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='dogs')