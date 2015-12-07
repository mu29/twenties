from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String(), unique=True)
    university = db.Column(db.String())
    gender = db.Column(db.String())
    group_id = db.Column(db.Integer)

    def __init__(self, name, phone, university, gender):
        self.name = name
        self.phone = phone
        self.university = university
        self.gender = gender

    def __repr__(self):
        return '<id {}>'.format(self.id)
