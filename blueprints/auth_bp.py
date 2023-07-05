from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date, timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from models.user import User, UserSchema

auth_bp = Blueprint('auth', __name__)

# GET all users - READ request
@auth_bp.route('/users')
@jwt_required()
def all_users():
    admin_required()
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

# GET one user - READ request
@auth_bp.route('/users/<int:user_id>')
@jwt_required()
def one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User not found'}, 404

# POST a new user - CREATE request
@auth_bp.route('/register', methods=['POST'])
def register_user():
    try:
        user_info = UserSchema().load(request.json)
        new_user = User(
            email = user_info['email'],
            username = user_info['username'],
            f_name = user_info['f_name'],
            l_name = user_info['l_name'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf8'),
            is_admin = False,
            date_created = date.today()
        )

        # Add and commit the new user
        db.session.add(new_user)
        db.session.commit()
        
        # Return the new user, excluding the password and is_admin
        return UserSchema(exclude=['password', 'is_admin']).dump(new_user), 201
    except IntegrityError:
        return {'error': 'The email address is already in use'}, 409
    
# POST login route - CREATE request
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # stmt = db.select(User).filter_by(email=request.json['email'])
        user_info = UserSchema().load(request.json)
        stmt = db.select(User).filter_by(email=user_info['email'])
        user = db.session.scalar(stmt)

        # if user and bcrypt.check_password_hash(user.password, request.json['password']):
        if user and bcrypt.check_password_hash(user.password, user_info['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(days=30))
            return {'token': token, 'user': UserSchema(exclude=['password', 'is_admin']).dump(user), 'message': f'Welcome, {user.username}'}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email and password are required'}, 401

# PUT or PATCH a user - UPDATE request
@auth_bp.route('/users/<int:user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    user_info = UserSchema().load(request.json)
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        admin_required()
        user.email = user_info.get('email', user.email)
        user.username = user_info.get('username', user.username)
        user.f_name = user_info.get('f_name', user.f_name)
        user.l_name = user_info.get('l_name', user.l_name)
        user.password = user_info.get(bcrypt.generate_password_hash('password').decode('utf8'), user.password)
        db.session.commit()
        return UserSchema(exclude=['is_admin']).dump(user)
    else:
        return {'error': 'User not found'}, 404

# PATCH a user to grant admin access - UPDATE request
@auth_bp.route('/users/<int:user_id>/grant-admin-access', methods=['PATCH'])
@jwt_required()
def grant_admin_access(user_id):
    admin_required()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        user.is_admin = True
        db.session.commit()
        return UserSchema().dump(user) # could potentially add confirmation message here
    else:
        return {'error': 'User not found'}, 404

# PATCH a user to remove admin access - UPDATE request
@auth_bp.route('/users/<int:user_id>/remove-admin-access', methods=['PATCH'])
@jwt_required()
def remove_admin_access(user_id):
    admin_required()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        user.is_admin = False
        db.session.commit()
        return UserSchema().dump(user) # could potentially add confirmation message here
    else:
        return {'error': 'User not found'}, 404

# DELETE a user - DELETE request
@auth_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        admin_required() # the actual user themself should also be able to self-delete
        db.session.delete(user)
        db.session.commit()
        return {'confirmation': 'User has been deleted'}, 200
    else:
        return {'error': 'User not found'}, 404

# Creating an admin-only access method for admin-only routes
def admin_required():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401, description='Invalid credentials')

# Creating an owner-only access method for owner-only routes
def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and (user.is_admin or user_id == owner_id)):
        abort(401, description='You must be an admin or the owner')