from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.worker_controller import WorkerController

bp = Blueprint('workers', __name__)
controller = WorkerController()

@bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    worker_id = get_jwt_identity()
    tasks = controller.get_worker_tasks(worker_id)
    return jsonify(tasks), 200

@bp.route('/tasks/<task_id>/accept', methods=['POST'])
@jwt_required()
def accept_task(task_id):
    worker_id = get_jwt_identity()
    result = controller.accept_task(task_id, worker_id)
    return jsonify(result), 200

@bp.route('/tasks/<task_id>/complete', methods=['POST'])
@jwt_required()
def complete_task(task_id):
    worker_id = get_jwt_identity()
    data = request.get_json()
    result = controller.complete_task(task_id, worker_id, data)
    return jsonify(result), 200

@bp.route('/tasks/<task_id>/update', methods=['PUT'])
@jwt_required()
def update_task_status(task_id):
    data = request.get_json()
    result = controller.update_task_status(task_id, data)
    return jsonify(result), 200
