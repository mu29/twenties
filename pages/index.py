# -*- coding: utf-8 -*-

from flask import *
from app import *

@app.route('/')
def index():
    return "hi"
