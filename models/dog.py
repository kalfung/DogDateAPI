from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, OneOf

VALID_GENDERS = ['Male', 'Female']
VALID_SIZES = ['Small', 'Medium', 'Large']

class Dog(db.Model):
    __tablename__= 'dogs'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String, nullable=False)
    breed = db.Column(db.String(60), nullable=False)
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
    # Validators
    name = fields.String(validate=And(
        Length(min=1, max=30, error='Name of the dog must be at least 1 character long, and no more than 30 characters'),
        Regexp('^[a-zA-Z \'-]+$', error='Only letters, spaces, hyphens and apostrophes are allowed')
    ))
    gender = fields.String(validate=[OneOf(['Male', 'Female'])])
    breed = fields.String(validate=And(
        Length(min=3, max=60, error='Breed of the dog must be at least 3 characters long, and no more than 60 characters'),
        Regexp('^[a-zA-Z \'-]+$', error='Only letters, spaces, hyphens and apostrophes are allowed')
    ))
    age = fields.Integer(error='Age of the dog must be an integer value')
    size = fields.String(default='Small', validate=[OneOf(['Small', 'Medium', 'Large'])])

    class Meta:
        fields = ('id', 'name', 'gender', 'breed', 'age', 'size', 'owner')
        ordered = True