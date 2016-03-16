from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    location = db.Column(db.String(10))
    ideal = db.Column(db.String(1000))
    non_ideal = db.Column(db.String(1000))
    introduce = db.Column(db.String(1000))
    interest = db.Column(db.String(255))
    experience = db.Column(db.String(255))
    friend = db.Column(db.String(10))
    prefer_age = db.Column(db.String(10))

    def __init__(self, params):
        self.phone = paras['phone']
        self.age = paras['age']
        self.gender = paras['gender']
        self.location = paras['location']
        self.ideal = paras['ideal']
        self.non_ideal = paras['non_ideal']
        self.introduce = paras['introduce']
        self.interest = paras['interest']
        self.experience = paras['experience']
        self.friend = paras['friend']
        self.prefer_age = paras['prefer_age']

    def __repr__(self):
        return "<User(id='%d', phone='%s', age='%s', gender='%s', location='%s', ideal='%s', non_ideal='%s', introduce='%s', interest='%s', experience='%s', friend='%s', prefer_age='%s')>" % (self.id, self.phone, self.age, self.gender, self.location, self.ideal, self.non_ideal, self.introduce, self.interest, self.experience, self.friend, self.prefer_age)
