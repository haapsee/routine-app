import re
import flask

from flask import Blueprint, render_template, request, redirect, session
#from email.utils import parseaddr
from app.db.user import createUser, authenticateUser


bp = Blueprint('user_page', __name__, template_folder='templates')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    errors = []

    if request.method == 'POST':
        user = None
        data = None

        if request.content_type == 'application/x-www-form-urlencoded':
            data = request.form

        if not data:
            data = dict()

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

        if not len(errors):
            user = createUser(firstname=firstname, lastname=lastname, email=email, password=password)

        if user:
            return redirect("/signin", code=302)

    return render_template('signup.html', errors=errors)


@bp.route("/signin", methods=["GET", "POST"])
def signin():
    errors = []

    if request.method == "POST":
        data = None
        user = None

        if request.content_type == "application/x-www-form-urlencoded":
            data = request.form
        if not data:
            data = dict()

        email = data.get('email')
        password = data.get('password')

        if not email:
            errors.append("Email is required")
        if not password:
            errors.append("Password is required")
        if not len(errors):
            user = authenticateUser(email, password)
        if user:
            session["user"] = user.id

    return render_template("signin.html", errors=errors)

@bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/", code=302)

