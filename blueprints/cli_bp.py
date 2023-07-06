from time import time

from flask import Blueprint

from init import db, ma, bcrypt, jwt

from models.user import User
from models.dog import Dog
from models.park import Park
from models.event import Event
from models.park_user import Park_User
from models.event_user import Event_User
from blueprints.seed_data import users, parks, dogs, events, events_users

cli_bp = Blueprint('db', __name__)

# CLI command to delete existing tables in DB and create new tables
@cli_bp.cli.command('create')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Created DogDateAPI tables')

# CLI command to delete existing tables in DB TEMPORARY
@cli_bp.cli.command('delete_tables')
def delete_tables():
    db.drop_all()
    print('Deleted DogDateAPI tables')

# CLI command to seed users table only in DB TEMPORARY
@cli_bp.cli.command('seed_users')
def seed_users():
    # Users
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Users seeded successfully')

# CLI command to seed tables
@cli_bp.cli.command('seed_tables')
def seed_tables():
    # Users
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Users seeded successfully')

    # Dogs
    db.session.query(Dog).delete()
    db.session.add_all(dogs)
    db.session.commit()
    print('Seeded dogs successfully')

    # Parks
    db.session.query(Park).delete()
    db.session.add_all(parks)
    db.session.commit()
    print('Seeded parks successfully')

    # Events
    db.session.query(Event).delete()
    db.session.add_all(events)
    db.session.commit()
    print('Seeded events successfully')

    # Events_users
    db.session.query(Event_User).delete()
    db.session.add_all(events_users)
    db.session.commit()
    print('Seeded events_users successfully')

    print('All data seeded successfully')