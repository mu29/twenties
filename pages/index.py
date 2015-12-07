# -*- coding: utf-8 -*-

from flask import *
from app import *
from models.user import *
from models.group import *

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        error = None
        univ = request.form['university'].encode('utf-8')
        gender = request.form['gender'].encode('utf-8')
        names = [request.form['name0'].encode('utf-8'),
            request.form['name1'].encode('utf-8'),
            request.form['name2'].encode('utf-8')]
        phones = [request.form['phone0'].encode('utf-8'),
            request.form['phone1'].encode('utf-8'),
            request.form['phone2'].encode('utf-8')]
        # for param in request.form:
        #     print param
        #     value = request.form[param].encode('utf-8')
        #     if 'university' in param: univ = value
        #     if 'gender' in param: gender = value
        #     if 'name' in param: names.append(value)
        #     if 'phone' in param: phones.append(value)

        # 휴대폰 번호 검사하자
        if len(list(set(phones))) < 3:
            error = "휴대폰 번호가 중복되었습니다."

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
            errors.append("이미 등록된 휴대폰 번호입니다.")

        #apply_db.put(names, phones, university, gender)
        return "success"
    return render_template('index.html')
