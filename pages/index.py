# -*- coding: utf-8 -*-

from flask import *
from app import *
from models.user import *
from models.location import *

@app.errorhandler(Exception)
def unhandled_exception(e):
    return u"알 수 없는 오류에요ㅠㅠ"

@app.route('/', methods=['POST', 'GET'])
def index():
    message = None
    session = db.session()
    locations = session.query(Location).all()
    session.close()

    try:
        if request.method == 'POST':
            name = request.form['name']
            phone = request.form['phone']
            age = int(request.form['age'])
            gender = request.form['gender']
            location = request.form['location']
            ideal = request.form['ideal']
            non_ideal = request.form['non_ideal']
            introduce = request.form['introduce']
            interest = request.form['interest']
            experience = request.form['experience']
            friend = request.form['friend']
            prefer_age = request.form['prefer_age']

            session = db.session()
            user = User({
                'name' : name,
                'phone' : phone,
                'age' : age,
                'gender' : gender,
                'location' : location,
                'ideal' : ideal,
                'non_ideal' : non_ideal,
                'introduce' : introduce,
                'interest' : interest,
                'experience' : experience,
                'friend' : friend,
                'prefer_age' : prefer_age
            })

            try:
                session.add(user)
                session.commit()
                message = u"성공적으로 신청했어요!"
            except:
                message = u"이미 신청한 것 같아요 :("

            session.close()

        return render_template('index.html', message = message, locations = locations)

    except:
        return render_template('index.html', message = u"알 수 없는 오류에요ㅠㅠ", locations = locations)
