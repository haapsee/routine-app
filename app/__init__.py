""" main file for RoutineApp """
__version__ = '0.1'

import os
import flask

from app.views import blueprint
from app.db.user import getUserById

app = flask.Flask('RoutineApp')
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY") or 'VerySuperSecretKey'
app.register_blueprint(blueprint)

@app.before_request
def before():

    user = flask.session.get('user')
    if user:
        authenticated_redirects = ["/", "/signin", "/signup"]
        if flask.request.path in authenticated_redirects:
            return flask.redirect("/tasks")

        flask.g.user = getUserById(user)
