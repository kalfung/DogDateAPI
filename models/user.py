from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    # Creating user role. A new user by default will not be an admin
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, nullable=False)

class UserSchema(ma.Schema):
    dogs = fields.List(fields.Nested('DogSchema', exclude=['user', 'id', 'user_id']))
    # NEED TO add schema for parksusers
    parks = fields.List(fields.Nested) 

    class Meta:
        fields = ('f_name', 'email', 'dogs', 'parks')