#!/usr/bin/env python

from flask import Flask
import api
app = Flask(__name__)

app.register_blueprint(api.blueprint)

if __name__=='__main__':
    app.run()
