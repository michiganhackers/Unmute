from __future__ import absolute_import

from flask import render_template
from app import app

from . import blueprint

@blueprint.route('/')
def index():
    return render_template('index.html')
