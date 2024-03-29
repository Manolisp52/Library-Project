## This file is ran automatically the first time a Python program imports the package dbdemo
from flask import Flask
from flask_mysqldb import MySQL
from library.signup import signup
from library.login import login
from library.borrowings import borrowings
from library.reservations import reservations
from library.books import books
from library.copies import copies
from library.users import users
from library.operator import operator
from library.reviews import reviews
from library.admin import admin
from library.schools import schools
from library.categories import categories

## __name__ is the name of the module. When running directly from python, it will be 'dbdemo'
## Outside of this module, as in run.py, it is '__main__' by default
## Create an instance of the Flask class to be used for request routing
app = Flask(__name__)

## configuration of database

app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'Mysql'
app.config["MYSQL_DB"] = 'Library'
app.config["MYSQL_HOST"] = 'localhost'
app.config["SECRET_KEY"] = 'd89b74ff2b0a255299377766c8afc06ff9d6729124a9b304309b831945903c61' ## secret key for sessions (signed cookies). Flask uses it to protect the contents of the user session against tampering.
app.config["WTF_CSRF_SECRET_KEY"] = 'd89b74ff2b0a255299377766c8afc06ff9d6729124a9b304309b831945903c61' ## token for csrf protection of forms.
## secret keys can be generated by secrets.token_hex()

## initialize database connection object
db = MySQL(app)

## routes must be imported after the app object has been initialized
from library import routes
from library.signup import routes
from library.login import routes
from library.borrowings import routes
from library.reservations import routes
from library.books import routes
from library.copies import routes
from library.users import routes
from library.operator import routes
from library.reviews import routes
from library.admin import routes
from library.schools import routes
from library.categories import routes
app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(borrowings)
app.register_blueprint(reservations)
app.register_blueprint(books)
app.register_blueprint(copies)
app.register_blueprint(users)
app.register_blueprint(operator)
app.register_blueprint(reviews)
app.register_blueprint(admin)
app.register_blueprint(schools)
app.register_blueprint(categories)
