"""
Description: Setup the flask application.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(module)s: :: %(levelname)s :: %(message)s')

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# enter path to the sqlite file here. A new db is created if one does not exist.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite'

db = SQLAlchemy(app)
from library_app import models
from library_app import views
