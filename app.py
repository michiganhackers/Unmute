from flask import Flask
from flask.json import JSONEncoder
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import arrow

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

# Initialize database
db = SQLAlchemy(app)

# Set up JSON encoder
class ArrowJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, arrow.Arrow):
                return obj.format('YYYY-MM-DDTHH:mm:ssZZ')
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app.json_encoder = ArrowJSONEncoder

# Import all modules
import stories
import pages

# Register all blueprints
app.register_blueprint(stories.blueprint)
app.register_blueprint(pages.blueprint)
