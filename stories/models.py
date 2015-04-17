from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy_utils import ArrowType, ChoiceType
from app import db

from datetime import datetime
from enum import Enum

import arrow

ColorEnum = Enum('ColorEnum', ['red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue',
        'light_blue', 'cyan', 'teal', 'green', 'light_green', 'lime', 'yellow', 'amber',
        'orange', 'deep_orange', 'brown', 'grey', 'blue_grey'])

class Story(db.Model):
    __tablename__ = 'stories'

    id = db.Column(db.Integer, primary_key = True)
    # story's ID

    # specific post information
    title = db.Column(db.String(128))
    story_body = db.Column(db.String(2048))

    color = db.Column(ChoiceType(ColorEnum, impl=db.Integer()), nullable=False, default=ColorEnum.blue)
    # color to classify story

    # post time
    post_date = db.Column(ArrowType(), nullable=False)

    # Location
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    def __init__(self, title, story_body, color, latitude, longitude):
        # self.user_id = user_id
        self.title = title
        self.story_body = story_body
        self.color = ColorEnum[color]
        self.latitude = latitude
        self.longitude = longitude
        self.post_date = arrow.utcnow()
