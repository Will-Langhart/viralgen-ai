from flask import Blueprint, jsonify

automation_bp = Blueprint('automation', __name__)

@automation_bp.route('/schedule', methods=['POST'])
def schedule_post():
    return jsonify({"status": "Post scheduled successfully!"})
