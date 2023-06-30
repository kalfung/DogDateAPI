from init import db

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    name =db.Column(db.String(30), nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, nullable=False)