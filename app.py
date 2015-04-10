from flask import Flask
from flask.json import JSONEncoder
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import arrow

if len(sys.argv) > 1:
    if sys.argv[1] == 'dev':
        config = 'config.DevelopmentConfig'
    if sys.argv[1] == 'prod':
        config = 'config.ProductionConfig'
else:
    config = 'config.DevelopmentConfig'

app = Flask(__name__)
app.config.from_object(config)

# Set up database
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

# Register all blueprints
app.register_blueprint(stories.blueprint)
