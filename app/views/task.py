from flask import Blueprint, redirect, request, session, render_template

from app.models import task

bp = Blueprint('task_page', __name__, template_folder='templates')

@bp.route('/tasks')
def tasks():
    errors = []
    user = 1
    if request.method == 'POST':
        pass
    return render_template('tasks.html')
