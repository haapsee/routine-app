import flask

from app.views.user import bp as userbp
from app.views.task import bp as tasksbp

blueprint = flask.Blueprint('Views', __name__, template_folder='templates')
blueprint.register_blueprint(userbp)
blueprint.register_blueprint(tasksbp)

@blueprint.route('/')
def home():
    """ Run landing page """
    return flask.render_template('index.html')
