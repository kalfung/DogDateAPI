from init import bcrypt
from datetime import date

from models.user import User
from models.dog import Dog
from models.park import Park
from models.event import Event

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
            email = 'kal.el@krypton.com',
            username = 'truesonofkrypton',
            f_name = 'Kal',
            l_name = 'El',
            password = bcrypt.generate_password_hash('krpytonite').decode('utf8'),
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

# dogs
# parks
# events