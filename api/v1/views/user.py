from flask import jsonify, request
from api.v1.views import app_look
from database import store
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app_look.route('/register', methods=['POST'], strict_slashes=False)
def register_user():
    """Registers a task user"""
    kwargs = {
        'email': request.form.get('email'),
        'password': request.form.get('password')
    }

    if kwargs['email'] is None or kwargs['password'] is None:
        return jsonify({'message': 'Incomplete registration details'}), 400
    usr = store.usr_email(kwargs['email'])
    if usr:
        return jsonify({'message': 'Account already exists'}), 400
    new_user = store.reg_user(**kwargs)
    access_token = create_access_token(identity=new_user.id)
    response = {
        'message': 'Registration successful',
        'jwt': access_token,
        'id': new_user.id
    }
    return jsonify(response), 200


@app_look.route('/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    usr = store.usr_email(email)
    if not usr:
        return jsonify({'message': 'Wrong email'}), 401
    if not usr.valid_password(password):
        return jsonify({'message': 'Wrong password'}), 401
    
    access_token = create_access_token(identity=usr.id)
    response = {
        'message': 'Successfully logged in',
        'jwt': access_token,
    }
    return jsonify(response), 200