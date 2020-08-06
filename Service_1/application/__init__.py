from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')                                    # Define Secret Key from environment
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                    # Dont track changes
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + ':' + getenv('MYSQL_PORT') + '/' + getenv('MYSQL_DB_NAME')) # Define DB URI from environment

db = SQLAlchemy(app)                                                                    # Define db access to URI

from application import routes