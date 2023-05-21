#~movie-bag/app.py

from flask import Flask, request
from .database.db import initialize_db
from .resources.movie import movies

from flask_restful import Api
from .resources.routes import initialize_routes

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .resources.errors import errors

from flask_mail import Mail

app = Flask(__name__)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

app.config.from_envvar('ENV_FILE_LOCATION')

jwt = JWTManager(app)
mail = Mail(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}


initialize_db(app)
app.register_blueprint(movies)
initialize_routes(api)

@app.route('/')
def hello():
    return {'hello': 'world'}


@app.before_request
def before_request_func():
    print("before_request executing!", request)
    print("before_request executing!", request.get_json())
    print("before_request executing!", request.headers)


app.run()
