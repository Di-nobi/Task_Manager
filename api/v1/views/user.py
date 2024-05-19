from flask import jsonify, request
from api.v1.views import app_look
from database import store
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flasgger.utils import swag_from
from flask_socketio import emit

@app_look.route('/register', methods=['POST'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Register a new user',
    'description': 'Registers a new user with email and password and returns a JWT token upon successful registration',
    'parameters': [
        {
            'name': 'email',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'The email address of the user'
        },
        {
            'name': 'password',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'The password for the user'
        }
    ],
    'responses': {
        '200': {
            'description': 'Registration successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    },
                    'jwt': {
                        'type': 'string',
                        'description': 'JWT token for the registered user'
                    },
                    'id': {
                        'type': 'string',
                        'description': 'The UUID of the registered user'
                    }
                }
            }
        },
        '400': {
            'description': 'Incomplete registration details or account already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            }
        },
    }
}, methods=['POST'])
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
    from api.v1.app import socketio
    socketio.emit('registration_response', {'jwt': access_token}, to='/')
    return jsonify(response), 200


@app_look.route('/login', methods=['POST'], strict_slashes=False)
@swag_from({
    'tags': ['Users'],
    'summary': 'Login a user',
    'description': 'Logs in a user with email and password and returns a JWT token upon successful authentication',
    'parameters': [
        {
            'name': 'email',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'The email address of the user'
        },
        {
            'name': 'password',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'The password for the user'
        }
    ],
    'responses': {
        '200': {
            'description': 'Successfully logged in',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    },
                    'jwt': {
                        'type': 'string',
                        'description': 'JWT token for the authenticated user'
                    }
                }
            }
        },
        '401': {
            'description': 'Wrong email or password',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Error message'
                    }
                }
            }
        },
    }
}, methods=['POST'])
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
    from api.v1.app import socketio
    socketio.emit('Logged_in', {'jwt': access_token}, to='/')
    return jsonify(response), 200