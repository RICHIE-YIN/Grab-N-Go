from flask_app import app
from flask_app.controllers import users, productlistings, userprofiles, messages
import os

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # if PORT is undefined, it defaults to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
