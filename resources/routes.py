from .book import BookShelf, BookPerId, BookPerTitle
from .auth import SignUp, Login

def initialize_routes(api):
    api.add_resource(BookShelf, '/bookshelf')
    api.add_resource(BookPerId, '/bookshelf/<id>')
    api.add_resource(SignUp, '/bookshelf/signup')
    api.add_resource(Login, '/bookshelf/login')
    api.add_resource(BookPerTitle, '/bookshelf/title/<title>')