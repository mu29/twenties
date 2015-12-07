#-*- coding: utf-8 -*-

from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from load_modules import MODULES
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

def init():
    for module in MODULES:
        __import__(module)
