from init import db, ma

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

class DogSchema(ma.Schema):
    class Meta:
        fields = ('name', 'gender', 'breed', 'age', 'size', 'owner')