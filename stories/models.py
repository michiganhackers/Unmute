from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import UserMixin

from sqlalchemy_utils import ArrowType

from app import db

from util import create_named_tuple
#from app.auth.models import User
from datetime import datetime

import arrow

class Story(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key = True)
    # story's ID

    # specific post information
    title = db.Column(db.String(128))
    story_body = db.Column(db.String(2048))

    ColorEnum = create_named_tuple('red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue',
            'light_blue', 'cyan', 'teal', 'green', 'light_green', 'lime', 'yellow', 'amber',
            'orange', 'deep_orange', 'brown', 'grey', 'blue_grey')

    color = db.Column(db.Enum(*ColorEnum._asdict().values()), nullable=False, default=ColorEnum.blue)
    # color to classify story

    # post time
    post_date = db.Column(ArrowType(), nullable=False)

    # Location
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    def __init__(self, title, story_body, color):
        # self.user_id = user_id
        self.title = title
        self.story_body = story_body
        self.color = color
        now = arrow.utcnow()
        self.post_date = now.date()
