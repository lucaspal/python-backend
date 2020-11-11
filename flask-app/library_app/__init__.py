"""
Description: Setup the flask application.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.secret_key = 'dev'

# enter path to the sqlite file here. A new db is created if one does not exist.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite'

db = SQLAlchemy(app)
from library_app import models
from library_app import views
