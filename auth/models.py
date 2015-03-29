from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

from app import db

class User(UserMixin, db.Model):
    pass # TODO
