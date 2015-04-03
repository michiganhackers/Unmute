from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    #The nickname is unique
    nickName = db.Column(db.String(20), unique = True)
    firstName = db.Column(db.String(30))
    lastName = db.Column(db.String(30))
    email = db.Column(db.String(80))


    def __repr__(self):
        return '<nickName = {nickName}, email = {email}'.format(nickName = self.nickName, email = self.nickName)


