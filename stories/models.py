from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

from app import db
from app.auth.models import User
from datetime import datetime

import arrow
class Stories(db.Model):

    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key = True)
        # story's ID

    # specific post information
    title = db.Column(db.String(80))
    story_body = db.Column(db.Text)
    color = db.Column(db.String(20))
        # color to classify story

    # dateTime
    post_date = db.Column(db.DateTime)

    def __init__(self, title, story_body, color):
        # self.user_id = user_id
        self.title = title
        self.story_body = story_body
        self.color = color
        now = arrow.utcnow()
        self.post_date = now.date()
        self.story_id = story_id


# class Tag(db.model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key = True)

# class Interact(db.model):
#     # this is for the interactions between the posts
#     # ie. starring a post to read later
#     # the class name might be a little bit misleading
#     __tablename__ = 'interact'
#     id = db.Column(db.Integer, primary_key = True)
#         # the id of the interaction

