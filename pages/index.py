# -*- coding: utf-8 -*-

from flask import *
from app import *
from database.apply_db import apply_db

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        university = request.form['university'].encode('utf-8')
        gender = request.form['gender'].encode('utf-8')

        names = [request.form['name0'].encode('utf-8'),
            request.form['name1'].encode('utf-8'),
            request.form['name2'].encode('utf-8')]

        phones = [request.form['phone0'].encode('utf-8'),
            request.form['phone1'].encode('utf-8'),
            request.form['phone2'].encode('utf-8')]

        if len(list(set(phones))) < 3:
            print "중복"

        apply_db.put(names, phones, university, gender)
        return "success"
    return render_template('index.html')
