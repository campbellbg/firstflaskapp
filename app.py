# For section 5 of the course where we start adding SQLite capabilities
# A lot of this code has been copied from Section 4 and then changed to align with the SQLITE DB

# This will allow us to get environment variables
import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity  # These are the functions from the security.py file
from db_setup import get_database

from resources.item import Item, Items
from resources.user import User
from resources.store import Store, Stores

my_app = Flask('Bryan App')
my_app.secret_key = 'bob' # This would obviously not be done this way in Production code

my_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Changed database to postgreSQL that was provisioned in Heroku
# my_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + get_database()
my_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///' + get_database())

my_api = Api(my_app)

# This creates a /auth end-point automatically
# A POST to this end-point will call the authenticate function
my_jwt = JWT(app=my_app, authentication_handler=authenticate, identity_handler=identity)

# Setup the database
# setup_database(purge_records = True)

my_api.add_resource(Item, '/item/<string:item_name>')
my_api.add_resource(Items, '/items')
my_api.add_resource(User, '/user/<string:user_name>')
my_api.add_resource(Store, '/store/<string:store_name>')
my_api.add_resource(Stores, '/stores')




