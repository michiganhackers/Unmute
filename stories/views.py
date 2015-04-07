from flask import current_app
from flask.ext.restless import APIManager

from app import app, db

from stories.models import Story

manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Story, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
