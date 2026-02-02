from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.issue_controller import IssueController

bp = Blueprint('issues', __name__)
controller = IssueController()

@bp.route('/', methods=['GET'])
@jwt_required()
def get_issues():
    issues = controller.get_all_issues()
    return jsonify(issues), 200

@bp.route('/<issue_id>', methods=['GET'])
@jwt_required()
def get_issue(issue_id):
    issue = controller.get_issue_by_id(issue_id)
    if issue:
        return jsonify(issue), 200
    return jsonify({'error': 'Issue not found'}), 404

@bp.route('/', methods=['POST'])
@jwt_required()
def create_issue():
    data = request.get_json()
    user_id = get_jwt_identity()
    issue = controller.create_issue(data, user_id)
    return jsonify(issue), 201

@bp.route('/<issue_id>', methods=['PUT'])
@jwt_required()
def update_issue(issue_id):
    data = request.get_json()
    issue = controller.update_issue(issue_id, data)
    if issue:
        return jsonify(issue), 200
    return jsonify({'error': 'Issue not found'}), 404

@bp.route('/<issue_id>', methods=['DELETE'])
@jwt_required()
def delete_issue(issue_id):
    success = controller.delete_issue(issue_id)
    if success:
        return jsonify({'message': 'Issue deleted'}), 200
    return jsonify({'error': 'Issue not found'}), 404
