from .extensions.database import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100), unique=True)


    def __init__(self, public_id, password, nickname):
      self.public_id = public_id
      self.password = password
      self.nickname = nickname
   
   

