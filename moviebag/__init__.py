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

    # app.config.from_envvar('ENV_FILE_LOCATION')

    app.config.from_mapping(
        JWT_SECRET_KEY = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss',
        MAIL_SERVER = "localhost",
        MAIL_PORT = "1025",
        MAIL_USERNAME = "jazzgitan@yahoo.ca",
        MAIL_PASSWORD = "12345",
        MONGODB_SETTINGS = { 'host': 'mongodb://localhost/movie-bag' }
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

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

    @app.route('/')
    def index():
        return "<p>Salut Fro - index !</p>"

    @app.route('/help')
    def help():
        help_text = "<H3>GET  127.0.0.1:5000/api/muvies</H3><H4>returns all Mongo stored movies, no AUTH required</H4>" + \
        "<H3>POST 127.0.0.1:5000/api/auth/signup (with login & password)</H3><H4>returns the unique id, no AUTH required</H4>" + \
        "<H3>POST 127.0.0.1:5000/api/auth/login (with login & password)</H3><H4>returns a token no AUTH required</H4>" + \
        "<hr>" +\
        "<H3>POST 127.0.0.1:5000/api/muvies (with json movie structure)</H3><H4>returns ??? AUTH required</H4>"

        return help_text

    @app.before_request
    def before_request_func():
        print("before_request executing!", request)
        print("before_request executing!", request.get_json())
        print("before_request executing!", request.headers)

    return app


