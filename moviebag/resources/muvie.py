#~movie-bag/resources/muvie.py

from flask import Response, request, jsonify
from moviebag.database.models import Movie, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity



from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from moviebag.resources.errors import SchemaValidationError, MovieAlreadyExistsError, \
InternalServerError, UpdatingMovieError, DeletingMovieError, MovieNotExistsError



class TestApi(Resource):
  def get(self):
    data = User.objects().to_json()
    return Response(data, mimetype="application/json", status=200)

  @jwt_required()
  def post(self):
    body = request.get_json()
    print(body)
    data = User.objects().to_json()
    return Response(data, mimetype="application/json", status=200)





class MuviesApi(Resource):
    def get(self):
        # query = Movie.objects()
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            movie =  Movie(**body, added_by=user)
            movie.save()
            user.update(push__movies=movie)
            user.save()
            id = movie.id
            ob = dict()
            print("ID is:", {'id': str(id)})
            ob['id'] = str(id)
            # data = User.objects().to_json()
            # return Response({'id': str(id)}, mimetype="application/json", status=200)
            # return Response(ob.to_json(), mimetype="application/json", status=200)

            # return jsonify({ "allo": "fro"})


        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class MuvieApi(Resource):
    @jwt_required()
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Movie.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMovieError
        except Exception:
            raise InternalServerError

    @jwt_required()
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects.get(id=id, added_by=user_id)
            movie.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            movies = Movie.objects.get(id=id).to_json()
            return Response(movies, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError
