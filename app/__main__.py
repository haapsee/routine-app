""" main file for RoutineApp """
__version__ = '0.1'

import os
from app import app
from app.db import db
from app.models import base

if __name__ == '__main__':
    engine = db.getEngine()
#    base.Base.metadata.drop_all(engine)
    base.Base.metadata.create_all(engine)
    port = os.environ.get('FLASK_PORT') or 5000
    app.run(host='0.0.0.0', port=port, debug=True)
