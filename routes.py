from flask import Blueprint, request, jsonify
from extensions import db
from models import Task

task_bp = Blueprint("task_bp", __name__, url_prefix="/tasks")

@task_bp.route("", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status
        } for t in tasks
    ])

@task_bp.route("", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(
        title=data["title"],
        description=data["description"]
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }), 201

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Task updated successfully"})

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200
