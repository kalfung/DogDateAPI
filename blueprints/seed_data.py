from init import bcrypt
from datetime import date

from models.user import User
from models.dog import Dog
from models.park import Park
from models.event import Event
from models.event_user import Event_User

# seed data for users
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
    ),
    User(
        email = 'lois.lane@dailyplanet.com',
        username = 'intrepidreporter',
        f_name = 'Lois',
        l_name = 'Lane',
        password = bcrypt.generate_password_hash('Metropolis').decode('utf8'),
        date_created = date.today()
    ),
    User(
        email = 'brucewayne@wayneenterprises.com',
        username = 'darkknight',
        f_name = 'Bruce',
        l_name = 'Wayne',
        password = bcrypt.generate_password_hash('crimealley').decode('utf8'),
        date_created = date.today()
    ),
    User(
        email = 'kalhounfarrer@gmail.com',
        username = 'kalfar',
        f_name = 'Kalhoun',
        l_name = 'Farrer',
        password = bcrypt.generate_password_hash('warrioroflight').decode('utf8'),
        date_created = date.today()
    ),
    User(
        email = 'johnjones@dc.comics',
        username = 'martianmanhunter',
        f_name = 'John',
        l_name = 'Jones',
        password = bcrypt.generate_password_hash('stayawayfromfire').decode('utf8'),
        date_created = date.today()
    ),
    User(
        email = 'dianaprince@island.com',
        username = 'wonderwoman',
        f_name = 'Diana',
        l_name = 'Prince',
        password = bcrypt.generate_password_hash('amazon').decode('utf8'),
        date_created = date.today()
    ),
    User(
        email = 'wallywest@speedster.com',
        username = 'theflash',
        f_name = 'Wally',
        l_name = 'West',
        password = bcrypt.generate_password_hash('redandyellow').decode('utf8'),
        date_created = date.today()
    )    
]

# seed data for dogs
dogs = [
    Dog(
        name = 'Krypto',
        gender = 'Male',
        breed = 'Labrador',
        age = 30,
        size = 'Large',
        user_id = 2
    ),
    Dog(
        name = 'Speedy',
        gender = 'Male',
        breed = 'Greyhound',
        age = 3,
        size = 'Large',
        user_id = 8
    ),
    Dog(
        name = 'Ace',
        gender = 'Male',
        breed = 'Rottweiler',
        age = 5,
        size = 'Large',
        user_id = 4
    ),
    Dog(
        name = 'Shifty',
        gender = 'Female',
        breed = 'Husky',
        age = 3,
        size = 'Large',
        user_id = 6
    ),
    Dog(
        name = 'Bumper',
        gender = 'Male',
        breed = 'Golden Retriever',
        age = 9,
        size = 'Large',
        user_id = 5
    ),
    Dog(
        name = 'Bella',
        gender = 'Female',
        breed = 'French Bulldog',
        age = 6,
        user_id = 5
    ),
    Dog(
        name = 'Athena',
        gender = 'Female',
        breed = 'German Shepherd',
        age = 7,
        size = 'Large',
        user_id = 7
    ),
    Dog(
        name = 'Scoop',
        gender = 'Female',
        breed = 'Beagle',
        age = 3,
        user_id = 3
    )
]

# seed data for parks
parks = [
    Park(
        name = 'Belmore Dog Park',
        latitude = -33.914696, 
        longitude = 151.096235,
        date_registered = date.today(),
        last_updated = date.today()
    ),
    Park(
        name = 'Enmore Dog Park',
        latitude = -33.902398, 
        longitude = 151.174394,
        date_registered = date.today(),
        last_updated = date.today()
    ),
    Park(
        name = 'Sydenham Dog Park',
        latitude = -33.916021, 
        longitude = 151.168344,
        date_registered = date.today(),
        last_updated = date.today()
    )
]

# seed data for events
events = [
    Event(
        title = 'Super Pets Meetup',
        description = 'Meetup for superheroes and their dogs',
        date = '2023-08-31',
        time = '09:00:00',
        user_id = 4,
        park_id = 2
    ),
    Event(
        title = 'Big dogs Meetup',
        description = 'Meetup for owners of large dogs',
        date = '2023-09-30',
        time = '09:00:00',
        user_id = 2,
        park_id = 3
    ),
    Event(
        title = 'Retrievers meetup',
        description = 'Meetup for owners of labrador and golden retrievers',
        date = '2023-09-30',
        time = '15:00:00',
        user_id = 5,
        park_id = 1
    )
]

# seed data for events_users
events_users = [
    
    # Attendees for event 1
    Event_User(
        event_id = 1,
        user_id = 2,
        date_created = date.today()
    ),
    Event_User(
        event_id = 1,
        user_id = 4,
        date_created = date.today()
    ),
    Event_User(
        event_id = 1,
        user_id = 6,
        date_created = date.today()
    ),
    Event_User(
        event_id = 1,
        user_id = 7,
        date_created = date.today()
    ),
    Event_User(
        event_id = 1,
        user_id = 8,
        date_created = date.today()
    ),
    
    # Attendees for event 2
    Event_User(
        event_id = 2,
        user_id = 2,
        date_created = date.today()
    ),
    Event_User(
        event_id = 2,
        user_id = 4,
        date_created = date.today()
    ),
    Event_User(
        event_id = 2,
        user_id = 5,
        date_created = date.today()
    ),
    Event_User(
        event_id = 2,
        user_id = 6,
        date_created = date.today()
    ),
    Event_User(
        event_id = 2,
        user_id = 7,
        date_created = date.today()
    ),
    Event_User(
        event_id = 2,
        user_id = 8,
        date_created = date.today()
    ),
    
    # Attendees for event 3
    Event_User(
        event_id = 3,
        user_id = 2,
        date_created = date.today()
    ),
    Event_User(
        event_id = 3,
        user_id = 5,
        date_created = date.today()
    )
]

# Seed data for parks_users to be added