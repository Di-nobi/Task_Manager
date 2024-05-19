from flask_jwt_extended import get_jwt_identity, jwt_required
from database import store
from api.v1.views import app_look
from flask import jsonify, abort, request
from flasgger.utils import swag_from
from flask_socketio import emit
@app_look.route('/tasks', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Get all tasks',
    'description': 'Retrieves a list of all tasks',
    'responses': {
        '200': {
            'description': 'Successful request',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        '__class__': {
                            'type': 'string',
                            'description': 'Class name of the instance'
                        },
                        'created_at': {
                            'type': 'string',
                            'format': 'date-time',
                            'description': 'Time of creation of the instance'
                        },
                        'id': {
                            'type': 'string',
                            'description': 'The UUID of the task instance'
                        },
                        'name': {
                            'type': 'string',
                            'description': 'Task name'
                        }
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid JWT tokens',
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
    },
    'security': [
        {
            'JWT': []
        }
    ]
}, methods=['GET'])
@jwt_required()
def get_all():
    usr_id = get_jwt_identity()
    if not usr_id:
        return jsonify({'message': 'Invalid JWT tokens'}), 401
    tasks_list = []
    for count in store.get_tasks():
        tasks_list.append(count.to_dict())
    return jsonify(tasks_list), 200

@app_look.route('/tasks/<task_id>', methods=['GET'], strict_slashes=False)
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Get a specific task',
    'description': 'Retrieves details of a specific task by task ID',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'The ID of the task to retrieve'
        }
    ],
    'responses': {
        '200': {
            'description': 'Successful request',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'string',
                        'description': 'The UUID of the task instance'
                    },
                    'subject': {
                        'type': 'string',
                        'description': 'Task subject'
                    },
                    'comment': {
                        'type': 'string',
                        'description': 'Task comment'
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Time of creation of the task'
                    },
                    'status': {
                        'type': 'string',
                        'description': 'Task status'
                    },
                    'due_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Due date of the task'
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid JWT tokens',
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
        '404': {
            'description': 'Task doesnt exist',
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
    },
    'security': [
        {
            'JWT': []
        }
    ]
}, methods=['GET'])
@jwt_required()
def get_a_task(task_id):
    """Retrieves a specific task"""
    usr_id = get_jwt_identity()
    if not usr_id:
        return jsonify({'message': 'Invalid JWT tokens'}), 401
    get_task = store.get_task(task_id)
    if not get_task:
        return jsonify({'message': 'Task dosent exist'}), 404
    response = {
        'id': get_task.id,
        'subject': get_task.subject,
        'comment': get_task.comment,
        'created_at': get_task.created_at,
        'status': get_task.status,
        'due_date': get_task.due_date
    }

    return jsonify(response), 200

@app_look.route('/tasks', methods=['POST'], strict_slashes=False)
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Create a new task',
    'description': 'Creates a new task with the provided details',
    'parameters': [
        {
            'name': 'subject',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'The subject of the task'
        },
        {
            'name': 'comment',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'description': 'Additional comments about the task'
        },
        {
            'name': 'due_date',
            'in': 'formData',
            'required': True,
            'type': 'string',
            'format': 'date-time',
            'description': 'The due date of the task'
        }
    ],
    'responses': {
        '200': {
            'description': 'Task successfully created',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    },
                    'task_id': {
                        'type': 'string',
                        'description': 'The UUID(Integer) of the created task'
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid JWT tokens',
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
        '400': {
            'description': 'Invalid input data',
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
    },
    'security': [
        {
            'JWT': []
        }
    ]
}, methods=['POST'])
@jwt_required()
def create_task():
    """Creates a specific task"""
    usr_id = get_jwt_identity()
    if not usr_id:
        return jsonify({'message': 'Invalid JWT tokens'}), 401
    
    kwargs = {
        'subject': request.form.get('subject'),
        'comment': request.form.get('comment'),
        'due_date': request.form.get('due_date'),
        'user_id': usr_id
    }

    if kwargs['subject'] is None or kwargs['due_date'] is None or kwargs['comment'] is None:
        return jsonify({'message': 'Invalid input data'}), 400
    tasks = store.add_task(**kwargs)
    response = {
        'message': 'Task successfully created',
        'task_id': tasks.id
    }

    from api.v1.app import socketio
    socketio.emit('task_created', {'task': tasks.to_dict()}, to='/')
    return jsonify(response), 200

@app_look.route('/tasks/<task_id>/', methods=['PUT'], strict_slashes=False)
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Update a specific task',
    'description': 'Updates the details of a specific task by task ID',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'The ID of the task to update'
        },
        {
            'name': 'subject',
            'in': 'formData',
            'required': False,
            'type': 'string',
            'description': 'The subject of the task'
        },
        {
            'name': 'comment',
            'in': 'formData',
            'required': False,
            'type': 'string',
            'description': 'Additional comments about the task'
        },
        {
            'name': 'status',
            'in': 'formData',
            'required': False,
            'type': 'string',
            'description': 'The status of the task'
        },
        {
            'name': 'due_date',
            'in': 'formData',
            'required': False,
            'type': 'string',
            'format': 'date-time',
            'description': 'The due date of the task'
        }
    ],
    'responses': {
        '200': {
            'description': 'Task Info Updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    },
                    'subject': {
                        'type': 'string',
                        'description': 'Updated subject of the task'
                    },
                    'comment': {
                        'type': 'string',
                        'description': 'Updated comment of the task'
                    },
                    'status': {
                        'type': 'string',
                        'description': 'Updated status of the task'
                    },
                    'due_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Updated due date of the task'
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid JWT token or Task doesnt exist',
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
    },
    'security': [
        {
            'JWT': []
        }
    ]
}, methods=['PUT'])
@jwt_required()
def update_info(task_id):
    """Updates the details of a specific task"""
    usr = get_jwt_identity()
    if not usr:
        return jsonify({'message': 'Invalid JWT token'})
    get_task = store.get_task(task_id)
    if not get_task:
        return jsonify({'message': 'This task doesnt exist'}), 401
    
    kwargs = {
        'subject': request.form.get('subject'),
        'comment': request.form.get('comment'),
        'status': request.form.get('status'),
        'due_date': request.form.get('due_date')
    }

    if kwargs['subject']:
        get_task.subject = kwargs['subject']
    else:
        get_task.subject

    if kwargs['comment']:
        get_task.comment = kwargs['comment']
    else:
        get_task.comment

    if kwargs['status']:
        get_task.status = kwargs['status']
    else:
        get_task.status

    if kwargs['due_date']:
        get_task.due_date = kwargs['due_date']
    else:
        get_task.due_date

    store.save()
    response = {
        'message': 'Task Info Updated successfully',
        'subject': get_task.subject,
        'comment': get_task.comment,
        'status': get_task.status,
        'due_date': get_task.due_date

    }

    from api.v1.app import socketio
    socketio.emit('task_updated', {'task': get_task.to_dict()}, to='/')
    return jsonify(response), 200

@app_look.route('/tasks/<task_id>', methods=['DELETE'], strict_slashes=False)
@swag_from({
    'tags': ['Tasks'],
    'summary': 'Delete a specific task',
    'description': 'Deletes a specific task by task ID',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'required': True,
            'type': 'string',
            'description': 'The ID of the task to delete'
        }
    ],
    'responses': {
        '200': {
            'description': 'Task deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'Success message'
                    }
                }
            }
        },
        '401': {
            'description': 'Invalid JWT token or Task doesnt exist',
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
    },
    'security': [
        {
            'JWT': []
        }
    ]
}, methods=['DELETE'])
@jwt_required()
def del_task(task_id):
    """Deletes a task from the database"""
    usr = get_jwt_identity()
    if not usr:
        return jsonify({'message': 'Invalid JWT token'}), 401
    get_task = store.get_task(task_id)
    if not get_task:
        return jsonify({'message': 'Task doesnt exist'}), 401
    store.delete(get_task)
    store.save()
    from api.v1.app import socketio
    socketio.emit('task_deleted', {'task_id': task_id}, to='/')
    return jsonify({'message': 'Task deleted successfully'}), 200