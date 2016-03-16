from app import db

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)

    def __init__(self, params):
        self.name = params['name']

    def __repr__(self):
        return "<Location(id='%d', name='%s')>" % (self.id, self.name)
