import flask

from app.views.user import bp as userbp

blueprint = flask.Blueprint('Views', __name__, template_folder='templates')
blueprint.register_blueprint(userbp)

@blueprint.route('/')
def home():
    """ Run Hello World """
    return flask.render_template('index.html')
