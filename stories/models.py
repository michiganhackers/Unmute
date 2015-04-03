from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

from app import db
from app.auth.models import User
from datetime import datetime

class Stories(db.Model):
    # this is for each individual post
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key = True)
        # story's ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        # author's ID
    user = db.relationship('User', backref = db.backref('stories', lazy = 'dynamic'))
        # connecting authors to their stories

    # specific post information
    title = db.Column(db.String(80))
        # number is size of the string
    story_body = db.Column(db.Text)
    color = db.Column(db.String(20))
        # color to classify story

    # tags
    # tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable = True)
    # tag = db.relationship('Tag', backref = db.backref('stories', lazy = 'dynamic'))

    # dateTime
    post_date = db.Column(db.DateTime)

    # fields for the updated
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable = True)
    story = db.relationship('Story', backref = db.backref('stories', lazy = 'dynamic'))

    def __init__(self, user_id, title, story_body, color):
        self.user_id = user_id
        self.title = title
        self.story_body = story_body
        self.color = color
        self.post_date =


# class Tag(db.model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key = True)


class Interact(db.model):
    # this is for the interactions between the posts
    # ie. starring a post to read later
    # the class name might be a little bit misleading
    __tablename__ = 'interact'
    id = story_id
        # the id of the post that you "like"