from flask_bcrypt import generate_password_hash, check_password_hash
from .db import db

class Book(db.Document):

    title = db.StringField(required=True, unique=True)
    author = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    #rating = db.IntField(min_value=1, max_value=5, required=True)
    #summary = db.StringField(max_length=500)
    added_by = db.ReferenceField('User')


class User(db.Document):

    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    books = db.ListField(db.ReferenceField('Book', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
 
    def check_password(self, password):
       return check_password_hash(self.password, password)


User.register_delete_rule(Book, 'added_by', db.CASCADE)
