#-*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# 모듈 불러오기
# for module in MODULES:
#    __import__(module)

@app.route('/')
def index():
    return "hi"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
