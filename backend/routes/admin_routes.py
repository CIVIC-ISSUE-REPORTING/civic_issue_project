from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.admin_controller import AdminController

bp = Blueprint('admin', __name__)
controller = AdminController()

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    stats = controller.get_dashboard_stats()
    return jsonify(stats), 200

@bp.route('/assign', methods=['POST'])
@jwt_required()
def assign_issue():
    data = request.get_json()
    result = controller.assign_issue_to_worker(
        data.get('issue_id'),
        data.get('worker_id')
    )
    return jsonify(result), 200

@bp.route('/analytics', methods=['GET'])
@jwt_required()
def analytics():
    analytics_data = controller.get_analytics()
    return jsonify(analytics_data), 200

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = controller.get_all_users()
    return jsonify(users), 200
