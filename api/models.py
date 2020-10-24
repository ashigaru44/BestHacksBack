from .extensions.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100), unique=True)
    rank = db.Column(db.String(100))
    level = db.Column(db.Integer)
    trees = db.Column(db.Integer)
    userXP = db.Column(db.BigInteger)
    userKM = db.Column(db.Integer)
    amountOfC02 = db.Column(db.Integer)

    def __init__(self, public_id, password, nickname):
        self.public_id = public_id
        self.password = password
        self.nickname = nickname
        self.rank = "Dzban leśny"
        self.level = 0
        self.trees = 0
        self.userXP = 0
        self.userKM = 0
        self.amountOfC02 = 0
