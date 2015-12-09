# -*- coding: utf-8 -*-

from flask import *
from app import *
from models.user import *
from models.group import *

@app.errorhandler(Exception)
def unhandled_exception(e):
    return u"알 수 없는 오류에요ㅠㅠ"

@app.route('/', methods=['POST', 'GET'])
def index():
    message = None
    if request.method == 'POST':
        univ = request.form['university'].encode('utf-8')
        gender = request.form['gender'].encode('utf-8')
        names = [request.form['name0'].encode('utf-8'),
            request.form['name1'].encode('utf-8'),
            request.form['name2'].encode('utf-8')]
        phones = [request.form['phone0'].encode('utf-8'),
            request.form['phone1'].encode('utf-8'),
            request.form['phone2'].encode('utf-8')]

        if len(list(set(phones))) < 3:
            message = u"휴대폰 번호가 중복되었어요.."
            return render_template('index.html', message = message)

        if db.session.query(User).filter(User.phone.in_(phones)).count() > 0:
            message = u"이미 신청한 사람이 있어요!"
            return render_template('index.html', message = message)

        try:
            group = Group(univ, gender)
            db.session.add(group)
            db.session.commit()
            for i in range(0, 3):
                user = User(names[i], phones[i], univ, gender)
                user.group_id = group.id
                db.session.add(user)
            db.session.commit()
        except:
            message = u"알 수 없는 오류에요ㅠㅠ"

        message = u"성공적으로 신청했어요!"

    return render_template('index.html', message = message)
