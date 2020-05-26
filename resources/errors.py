class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class BookAlreadyExistsError(Exception):
    pass

class UpdatingBookError(Exception):
    pass

class DeletingBookError(Exception):
    pass

class BookNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "BookAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingBookError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingBookError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "BookNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}
