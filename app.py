from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://stefanie:5Xj7x5kKRbqFSDM@cluster0-juzew.gcp.mongodb.net/test?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)

# export ENV_FILE_LOCATION=./.env
