from Section6.db_setup import db_sql # Import here to avoid the circular imports
from Section6.app import my_app

db_sql.init_app(my_app)

# This is setup in this manner for Heroku. Don't run this unless we are launching run.py directly ourselves
if __name__ == '__main__':
    my_app.run(port=5555)


# This is a Flask decorator it is not from flask_restful
@my_app.before_first_request
def setup_db():
    db_sql.create_all()