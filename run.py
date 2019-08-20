from Section6.db_setup import db_sql # Import here to avoid the circular imports
from Section6.app import my_app


# This is a Flask decorator it is not from flask_restful
@my_app.before_first_request
def setup_db():
    db_sql.create_all()


db_sql.init_app(my_app)
my_app.run(port=5555)