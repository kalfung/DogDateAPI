from init import db, ma
from marshmallow import fields

VALID_SIZES = ['Small', 'Medium', 'Large']

class Dog(db.Model):
    __tablename__= 'dogs'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String, nullable=False, default='Small')

    # Relationship between dogs and their owners
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('User', back_populates='dogs')

    # def __repr__(self):
    #     return f'<DOG "{self.name}: {self.breed}">'

class DogSchema(ma.Schema):
    # Tell Marshmallow to use UserSchema to serialise the 'owner' field
    owner = fields.Nested('UserSchema', only=['username', 'f_name'])
    class Meta:
        fields = ('name', 'gender', 'breed', 'age', 'size', 'owner')
        ordered = True