from flask import Blueprint, jsonify, request

from models import TaskStore
from utils import clean_title, validate_title

bp = Blueprint("tasks", __name__)
store = TaskStore()


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify([t.to_dict() for t in store.all()])


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not validate_title(title):
        return jsonify({"error": "Judul tidak valid"}), 400
    task = store.add(clean_title(title))
    return jsonify(task.to_dict()), 201


@bp.route("/tasks/<int:task_id>/done", methods=["PUT"])
def mark_done(task_id):
    task = store.get(task_id)
    if task is None:
        return jsonify({"error": "Task tidak ditemukan"}), 404
    task.done = True
    return jsonify(task.to_dict())


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if not store.delete(task_id):
        return jsonify({"error": "Task tidak ditemukan"}), 404
    return jsonify({"message": "Task dihapus"})