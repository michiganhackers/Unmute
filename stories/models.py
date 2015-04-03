from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin

from app import db
from app.auth.models import User
from datetime import datetime
import arrow
class Stories(db.Model):
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key = True)
    #The author's ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref = db.backref('stories', lazy = 'dynamic'))

    #the rest of the thing
    title = db.Column(db.String(80))
    story_body = db.Column(db.Text)
    color = db.Column(db.String(20))

    #dateTime
    post_date = db.Column(db.DateTime)

    #the fields for the updated
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable = True)
    story = db.relationship('Stories', backref = db.backref('stories', lazy = 'dynamic'), uselist=False)

    def __init__(self, user_id, title, story_body, color,
        story_id):
        self.user_id = user_id
        self.title = title
        self.story_body = story_body
        self.color = color
        now = arrow.utcnow()
        self.post_date = now.date()
        self.story_id = story_id

