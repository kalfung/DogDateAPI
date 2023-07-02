from datetime import date
from time import time

from flask import Blueprint

from init import db, ma, bcrypt, jwt

from models.user import User
from models.dog import Dog
from models.park import Park
from models.event import Event
from models.park_user import Park_User
from models.event_user import Event_User

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Created DogDateAPI tables')

@cli_bp.cli.command('delete_tables')
def delete_tables():
    db.drop_all()
    print('Deleted DogDateAPI tables')

@cli_bp.cli.command('seed_users')
def seed_users():
    users = [
        User(
            email = 'admin@dogdate.com',
            username = 'Administrator',
            f_name = 'Ad',
            l_name = 'Ministrator',
            password = bcrypt.generate_password_hash('golden123').decode('utf8'),
            is_admin = True,
            date_created = date.today()
        ),
        User(
            email = 'clark.kent@dailyplanet.com',
            username = 'sonofkrypton',
            f_name = 'Clark',
            l_name = 'Kent',
            password = bcrypt.generate_password_hash('fortressofsolitude').decode('utf8'),
            date_created = date.today()
        )
    ]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Users seeded successfully')