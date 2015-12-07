from app import db


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    university = db.Column(db.String())
    gender = db.Column(db.String())

    def __init__(self, university, gender):
        self.university = university
        self.gender = gender

    def __repr__(self):
        return '<id {}>'.format(self.id)
