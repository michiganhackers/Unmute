#!/usr/bin/env python

from flask import Flask
import api
import sys
app = Flask(__name__)

app.register_blueprint(api.blueprint)

if __name__=='__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'dev':
            config = 'config.DevelopmentConfig'
        if sys.argv[1] == 'prod':
            config = 'config.ProductionConfig'
    else:
        config = 'config.DevelopmentConfig'

    app.config.from_object(config)
    app.run()
