from __future__ import absolute_import

from . import blueprint
from flask import current_app, request, jsonify

@blueprint.route('/api/hello-world')
def hello_world():
    return jsonify({'text': 'Hello World'})
