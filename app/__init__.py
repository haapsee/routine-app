""" main file for RoutineApp """
__version__ = '0.1'

import os
import flask

from app.views import blueprint

app = flask.Flask('RoutineApp')
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY") or 'VerySuperSecretKey'
app.register_blueprint(blueprint)
