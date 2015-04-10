from flask import Flask
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'dev':
        config = 'config.DevelopmentConfig'
    if sys.argv[1] == 'prod':
        config = 'config.ProductionConfig'
else:
    config = 'config.DevelopmentConfig'

app = Flask(__name__)
app.config.from_object(config)

# Set up login
#login_manager = LoginManager()
#login_manager.init_app(app)

# Set up database
db = SQLAlchemy(app)

# Import all modules
import stories

# Register all blueprints
app.register_blueprint(stories.blueprint)
