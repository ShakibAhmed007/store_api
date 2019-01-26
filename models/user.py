from db import db

class user(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self,id,name,password):
        self.id = id
        self.username = name
        self.password = password


    @classmethod
    def find_user(cls,username , password):
        return cls.query.filter_by(username = username,password = password).first()