from flask import Blueprint, Response, request
from app.database.models import Movie
from flask_jwt_extended import jwt_required


movies = Blueprint('movies', __name__)

@movies.route('/movies', methods = ['GET'])
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@jwt_required
@movies.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200

@jwt_required
@movies.route('/movies/<int:index>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

@jwt_required
@movies.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200
