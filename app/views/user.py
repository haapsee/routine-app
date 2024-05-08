import re
from flask import Blueprint, render_template, request
from email.utils import parseaddr

bp = Blueprint('user_page', __name__, template_folder='templates')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    errors = []

    if request.method == 'POST':
        data = None
        if request.content_type == 'application/x-www-form-urlencoded':
            data = request.form

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        validate_password = data.get('validatepassword')

        if not firstname:
            errors.append("Firstname is required")
        if not lastname:
            errors.append("Lastname is required")
        if not email:
            errors.append("Email is required")
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            errors.append("Email is not valid")
        if not password:
            errors.append("Password is required")
        elif len(password) < 8:
            errors.append("Password must contain 8 characters")
        elif password != validate_password:
            errors.append("Password and validate password must match!")

    return render_template('signup.html', errors=errors)
