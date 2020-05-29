from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Book, User
import json

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, BookAlreadyExistsError, InternalServerError, UpdatingBookError, DeletingBookError, BookNotExistsError


class BookShelf(Resource):

    @jwt_required 
    def get(self):
        try:
            user_id = get_jwt_identity()
            books = Book.objects(added_by=user_id).to_json() 
            a = json.loads(books)
            if len(a) == 0 :
                return Response('your bookshelf is empty')
            else:
                return Response(books, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError
            
    @jwt_required 
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            book = Book(**body, added_by=user)
            book.save()
            user.update(push__books=book)
            user.save()
            id = book.id
            message = book.title + ' has been saved'
            return Response(message, status=201)
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError as e:
            return str(e), 500
        except NotUniqueError:
            raise BookAlreadyExistsError
        except Exception as e:
            raise InternalServerError
 

class BookPerId(Resource):

    @jwt_required 
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Book.objects.get(id=id).update(**body)
            message = str(book.title) + ' has been updated'
            return Response(message, status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingBookError
        except ValidationError as e:
            return str(e), 500
        except Exception:
            raise InternalServerError 
 
    @jwt_required 
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id, added_by=user_id)
            message = str(book.title) + ' has been deleted'
            book.delete()
            return Response(message, status=200)
        except DoesNotExist:
            raise DeletingBookError
        except Exception:
            raise InternalServerError

    @jwt_required 
    def get(self, id):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(id=id, added_by=user_id).to_json()
            return Response(book, mimetype="application/json", status=200)
        except DoesNotExist:
            raise BookNotExistsError
        except Exception:
            raise InternalServerError


class BookPerTitle(Resource):

    @jwt_required 
    def get(self, title):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(title=title, added_by=user_id).to_json()
            return Response(book, mimetype="application/json", status=200)
        except DoesNotExist:
            raise BookNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required 
    def put(self, title):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(title=title, added_by=user_id)
            body = request.get_json()
            Book.objects.get(title=title, added_by=user_id).update(**body)
            message = str(book.title) + ' has been updated'
            return Response(message, status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingBookError
        except ValidationError as e:
            return str(e), 500
        except Exception:
            raise InternalServerError 
 
    @jwt_required 
    def delete(self, title):
        try:
            user_id = get_jwt_identity()
            book = Book.objects.get(title=title, added_by=user_id)
            message = str(book.title) + ' has been deleted'
            book.delete()
            return Response(message, status=200)
        except DoesNotExist:
            raise DeletingBookError
        except Exception:
            raise InternalServerError


