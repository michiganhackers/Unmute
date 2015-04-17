from flask import Flask
from flask.json import JSONEncoder
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from enum import Enum
import arrow

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Initialize database
db = SQLAlchemy(app)

# Set up JSON encoder
class OurJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, arrow.Arrow):
                return obj.format('YYYY-MM-DDTHH:mm:ssZZ')
            if isinstance(obj, Enum):
                return obj.name
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app.json_encoder = OurJSONEncoder

# Import all modules
import stories
import pages

# Register all blueprints
app.register_blueprint(stories.blueprint)
app.register_blueprint(pages.blueprint)
