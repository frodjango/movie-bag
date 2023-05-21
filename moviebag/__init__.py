#~movie-bag/app.py

import os
import logging


from flask import Flask, request
from .database.db import initialize_db
from .resources.movie import movies

from flask_restful import Api
from .resources.routes import initialize_routes

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .resources.errors import errors

from flask_mail import Mail

def create_app(test_config=None):

    app = Flask(__name__)
    api = Api(app, errors=errors)
    bcrypt = Bcrypt(app)

    app.config.from_envvar('ENV_FILE_LOCATION')

    app.jwt = JWTManager(app)
    app.mail = Mail(app)

    # removed in chapter 6
    # app.config['MONGODB_SETTINGS'] = {
    #     'host': 'mongodb://localhost/movie-bag'
    # }


    initialize_db(app)
    app.register_blueprint(movies)
    initialize_routes(api)

    with app.app_context():
        log_level = logging.DEBUG

        # Uncomment following lines if you only want to have logging within a file
        #
        for handler in app.logger.handlers:
            print("FOUND A LOGGER")
            app.logger.removeHandler(handler)

        root = os.path.dirname(os.path.abspath(__file__))
        logdir = os.path.join(root, 'logs')

        if not os.path.exists(logdir):
            os.mkdir(logdir)
        log_file = os.path.join(logdir, 'app.log')
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        app.logger.addHandler(handler)

        # set logging level to lower level - to witness all
        # V1 app.logger.setLevel(log_level)
        # V2 logging.basicConfig(format='CONSOLE: %(levelname)s:%(message)s', level=logging.DEBUG)

        # Format messaging
        # [2022-04-04 17:37:27,433] CRITICAL in hello: critical

        myFormat = '[DUDE ! %(asctime)s] %(levelname)s in %(module)s: %(message)s'
        defaultFormatter = logging.Formatter(myFormat)
        handler.setFormatter(defaultFormatter)
        logging.basicConfig(format=myFormat, level=log_level)


    @app.route('/hello')
    def hello():
        return "<p>Hello, World!</p>"


    @app.before_request
    def before_request_func():
        print("before_request executing!", request)
        print("before_request executing!", request.get_json())
        print("before_request executing!", request.headers)

    return app


