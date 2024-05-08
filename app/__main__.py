""" main file for RoutineApp """
__version__ = '0.1'

import os
from app import app

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 5000
    app.run(host='0.0.0.0', port=port, debug=True)
