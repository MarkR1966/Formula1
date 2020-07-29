from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' + getenv('MYSQL_HOST') + ':' + getenv('MYSQL_PORT') + '/' + getenv('MYSQL_DB_NAME'))

db = SQLAlchemy(app)

from application import routes