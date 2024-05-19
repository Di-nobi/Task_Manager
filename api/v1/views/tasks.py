from flask_jwt_extended import get_jwt_identity, jwt_required
from database import store
from api.v1.views import app_look
from flask import jsonify, abort, request
from flasgger.utils import swag_from

@app_look.route('/tasks', methods=['GET'], strict_slashes=False)
@swag_from('documentation/read_task.yml', methods=['GET'])
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
@swag_from('documentation/read_single_task.yml', methods=['GET'])
@jwt_required()
def get_a_task(task_id):
    """Retrieves a specific task"""
    usr_id = get_jwt_identity()
    if not usr_id:
        return jsonify({'message': 'Invalid JWT tokens'}), 401
    get_task = store.get_task(task_id)
    if not get_task:
        return jsonify({'message': 'Task dosent exist'})
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
@swag_from('documentation/create_task.yml', methods=['GET'])
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
    tasks = store.add_task(**kwargs)
    response = {
        'message': 'Task successfully created',
        'task_id': tasks.id
    }
    return jsonify(response), 200

@app_look.route('/tasks/<task_id>/', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/update_task.yml', methods=['GET'])
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
    return jsonify(response), 200

@app_look.route('/tasks/<task_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/delete_task.yml', methods=['GET'])
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
    return jsonify({'message': 'Task deleted successfully'}), 200